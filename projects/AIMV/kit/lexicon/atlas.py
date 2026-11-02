"""AIMV atlas (people, orgs, institutions, places, events, fiction): validate batches and render ../kit-atlas.md.

  python -I atlas.py check <batch>     validate atlas/<batch>-p*.json (or one file path)
  python -I atlas.py build             render ../kit-atlas.md and atlas-backlinks.json (read by lexicon.py build)

Ref lyrics are read with lexicon.load_lyrics (official text preferred over Whisper).
"""
import glob, json, os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lexicon as LX  # noqa: E402

OUT = os.path.join(HERE, "..", "kit-atlas.md")
KINDS = ["person", "company", "lab", "institution", "place", "law", "event", "work-film", "work-tv", "work-book", "work-game", "universe"]
RELS = ["works-at", "founded", "leads", "rival", "invested-in", "made", "adapted-from", "regulates", "measures", "located-in",
        "depicts", "inspired", "same-family"]
REQ = ["id", "what", "forms", "aka", "receipts", "quotes", "name_play", "pivots", "visuals", "lexicon", "links", "stakes",
       "registers", "risk", "notes"]
KIND_TITLES = [("person", "People"), ("lab", "Labs"), ("company", "Companies"), ("institution", "Institutions"),
               ("law", "Laws"), ("event", "Events and documents"), ("place", "Places"), ("work-film", "Films"),
               ("work-tv", "TV"), ("work-book", "Books"), ("work-game", "Games"), ("universe", "Universes")]


def master():
    return {t["id"]: t for t in json.load(open(os.path.join(HERE, "atlas.json"), encoding="utf-8"))["entities"]}


def check_entry(e, A, T):
    errs, i = [], e.get("id", "?")
    for k in REQ:
        if k not in e:
            errs.append(f"{i}: missing {k}")
    if errs:
        return errs
    if i not in A:
        errs.append(f"{i}: id not in atlas.json")
    if not e["what"].get("line") or not re.match(r"^\d{4}-\d{2}-\d{2}$", e["what"].get("asof", "")):
        errs.append(f"{i}: what.line / what.asof (YYYY-MM-DD)")
    if not e["receipts"]:
        errs.append(f"{i}: no receipts")
    for r in e["receipts"]:
        if not r.get("claim") or "url" not in r or "date" not in r or r.get("confidence") not in LX.CONF:
            errs.append(f"{i}: receipt incomplete: {r.get('claim', '')[:40]}")
    for q in e["quotes"]:
        if not q.get("text") or not q.get("who") or "url" not in q or "date" not in q or "where" not in q:
            errs.append(f"{i}: quote incomplete")
    for p in e["pivots"]:
        if not p.get("line") or len(p.get("readings", [])) < 2:
            errs.append(f"{i}: pivot needs line + 2 readings")
        elif len(p["line"].split()) > 12:
            errs.append(f"{i}: pivot over 12 words: {p['line']}")
    for x in e["lexicon"]:
        if x.get("id") not in T:
            errs.append(f"{i}: lexicon id {x.get('id')!r} not in terms.json")
    for x in e["links"]:
        if x.get("id") not in A:
            errs.append(f"{i}: link {x.get('id')!r} not in atlas.json")
        if x.get("rel") not in RELS:
            errs.append(f"{i}: rel {x.get('rel')!r}")
    for x in e["stakes"]:
        if x not in LX.STAKES:
            errs.append(f"{i}: stake {x!r}")
    for x in e["registers"]:
        if x not in LX.REGISTERS:
            errs.append(f"{i}: register {x!r}")
    if "—" in json.dumps(e, ensure_ascii=False):
        errs.append(f"{i}: em dash present")
    return errs


def load_batch(arg):
    if arg.endswith(".json"):
        return [arg], re.sub(r"-p\d+$", "", os.path.splitext(os.path.basename(arg))[0])
    return sorted(glob.glob(os.path.join(HERE, "atlas", arg + "-p*.json"))), arg


def cmd_check(arg):
    A, T = master(), LX.terms()
    paths, batch = load_batch(arg)
    E, errs = [], []
    for p in paths:
        try:
            E += json.load(open(p, encoding="utf-8"))
        except Exception as ex:
            errs.append(f"{os.path.basename(p)}: invalid JSON: {ex}")
    errs += [x for e in E for x in check_entry(e, A, T)]
    ids = [e.get("id") for e in E]
    errs += [f"duplicate id {k}" for k, v in Counter(ids).items() if v > 1]
    want = {k for k, t in A.items() if t["batch"] == batch}
    miss = sorted(want - set(ids))
    print(f"{batch}: {len(paths)} file(s), {len(E)} entries, {len(errs)} problems, {len(miss)} of {len(want)} ids not yet written")
    for x in errs:
        print("  " + x)
    if miss:
        print("  not yet written: " + ", ".join(miss))
    return 1 if errs else 0


def cmd_build():
    A, T = master(), LX.terms()
    E = {}
    for p in sorted(glob.glob(os.path.join(HERE, "atlas", "*.json"))):
        if os.path.basename(p).startswith("_"):
            continue
        for e in json.load(open(p, encoding="utf-8")):
            E[e["id"]] = e
    if "her" not in E:
        for e in json.load(open(os.path.join(HERE, "atlas", "_example.json"), encoding="utf-8")):
            E[e["id"]] = e
    problems = [x for e in E.values() for x in check_entry(e, A, T)]
    songs, src, kc = LX.load_lyrics()
    back = defaultdict(list)   # lexicon id -> atlas ids
    inbound = defaultdict(list)
    for i, e in E.items():
        rx = LX.form_regex(e["forms"]) if e["forms"] else None
        e["_refs"] = {n: len(rx.findall(t)) for n, t in songs.items() if rx and rx.search(t)}
        e["_kc"] = len(rx.findall(kc)) if rx else 0
        for x in e["lexicon"]:
            back[x["id"]].append(i)
        for x in e["links"]:
            inbound[x["id"]].append(i)
    json.dump({k: sorted(v) for k, v in back.items()}, open(os.path.join(HERE, "atlas-backlinks.json"), "w", encoding="utf-8"), indent=1)
    name = lambda i: A.get(i, {"name": i})["name"]
    missing = sorted(set(A) - set(E))
    L = ["---", "type: project", "created: 2026-11-02", "author: jep", "status: active", "---", "",
         "# Atlas (who, what, where the AI world talks about)", "",
         "Generated by `lexicon/atlas.py build` from `lexicon/atlas/*.json`; edit the JSON, never this file. Schema: `lexicon/ATLAS-SCHEMA.md`. Sibling of [[kit-lexicon]] (Idi's option B, 2026-11-02): lexicon terms link here and back. "
         "Ref usage counts only distinctive `forms` over the same lyric set as the lexicon.", "",
         f"Entries {len(E)} of {len(A)} | " + " | ".join(f"{t} {sum(1 for e in E.values() if A.get(e['id'], {}).get('kind') == k)}" for k, t in KIND_TITLES)
         + f" | named by Idi {sum(1 for e in E.values() if A.get(e['id'], {}).get('idi_named'))} | receipts {sum(len(e['receipts']) for e in E.values())} | quotes {sum(len(e['quotes']) for e in E.values())} | schema problems {len(problems)}", ""]
    if missing:
        L += [f"Not yet written ({len(missing)}): " + ", ".join(missing), ""]
    L += ["## Index", "", "| entry | kind | what | lexicon links | refs | KC |", "|---|---|---|---|---|---|"]
    for k, _ in KIND_TITLES:
        for e in sorted((e for e in E.values() if A.get(e["id"], {}).get("kind") == k), key=lambda e: name(e["id"])):
            a = A.get(e["id"], {})
            tag = " (Idi)" if a.get("idi_named") else (" ([MASK])" if a.get("mask") else "")
            L.append(f"| [[#^{e['id']}\\|{LX.esc(name(e['id']))}]]{tag} | {k} | {LX.esc(e['what']['line'])[:110]} | "
                     f"{', '.join(x['id'] for x in e['lexicon'])} | {len(e['_refs'])} | {e['_kc']} |")
    for k, title in KIND_TITLES:
        group = sorted((e for e in E.values() if A.get(e["id"], {}).get("kind") == k), key=lambda e: name(e["id"]))
        if not group:
            continue
        L += ["", f"## {title}", ""]
        for e in group:
            a = A.get(e["id"], {})
            L.append(f"### {name(e['id'])}")
            L.append(f"- `{e['id']}` | {k} | as of {e['what']['asof']}{' | named by Idi' if a.get('idi_named') else ''}{' | [MASK] cast' if a.get('mask') else ''} ^{e['id']}")
            L.append(f"- what: {e['what']['line']}")
            if e["aka"]:
                L.append(f"- aka: {', '.join(e['aka'])}")
            L.append("- receipts: " + "; ".join(f"{r['claim']} ({r['date']}){' ' + r['url'] if r['url'] else ''} [{r['confidence']}]" for r in e["receipts"]))
            if e["quotes"]:
                L.append("- quotes: " + "; ".join(f"\"{q['text']}\" ({q['who']}, {q['where']}, {q['date']}){' ' + q['url'] if q['url'] else ''}" for q in e["quotes"]))
            if e["name_play"]:
                L.append("- name play: " + "; ".join(f"**{x['play']}** {x['how']}" for x in e["name_play"]))
            if e["pivots"]:
                L.append("- pivots (jep drafts): " + " / ".join(f"\"{p['line']}\" ({' + '.join(p['readings'])})" for p in e["pivots"]))
            if e["visuals"]:
                L.append("- visuals: " + "; ".join(e["visuals"]))
            if e["lexicon"]:
                L.append("- lexicon: " + "; ".join(f"[[kit-lexicon#^{x['id']}|{T[x['id']]['term']}]] {x['how']}" for x in e["lexicon"] if x["id"] in T))
            if e["links"]:
                L.append("- links: " + ", ".join(f"[[#^{x['id']}|{name(x['id'])}]] ({x['rel']})" for x in e["links"]))
            if inbound.get(e["id"]):
                L.append("- linked from: " + ", ".join(f"[[#^{j}|{name(j)}]]" for j in sorted(set(inbound[e["id"]]))))
            refs = ", ".join(f"{n}{'~' if src[n] == 'whisper' else ''} {c}" for n, c in sorted(e["_refs"].items(), key=lambda kv: -kv[1]))
            L.append(f"- forms (counted): {', '.join(e['forms']) or '-'} | refs: {len(e['_refs'])} of {len(songs)}{': ' + refs if refs else ''} | KC {e['_kc']}")
            L.append(f"- stakes {', '.join(e['stakes']) or '-'} | registers {', '.join(e['registers']) or '-'}")
            if e["risk"]:
                L.append(f"- risk: {e['risk']}")
            if e["notes"]:
                L.append(f"- note: {e['notes']}")
            L.append("")
    if problems:
        L += ["## Schema problems", ""] + [f"- {p}" for p in problems]
    open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print(f"built {OUT}: {len(E)} entries, {len(problems)} problems, {len(missing)} missing, {sum(len(v) for v in back.values())} lexicon back-links")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "check":
        sys.exit(cmd_check(sys.argv[2]))
    elif len(sys.argv) >= 2 and sys.argv[1] == "build":
        cmd_build()
    else:
        print(__doc__)
