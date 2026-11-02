"""AIMV lexicon: validate batch files and render ../kit-lexicon.md.

  python -I lexicon.py check entries/<batch>.json   validate one batch against SCHEMA.md
  python -I lexicon.py build                        merge all batches, count ref usage, render ../kit-lexicon.md

Ref transcripts are read from D:/work/AIMVs/lyrics (outside the vault, third-party text);
only counts enter the vault. Override with env AIMV_LYRICS / AIMV_KC_LYRICS.
"""
import glob, json, os, re, sys
from collections import Counter
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
LYR = os.environ.get("AIMV_LYRICS", "D:/work/AIMVs/lyrics")
KC = os.environ.get("AIMV_KC_LYRICS", "D:/work/AIMVs/ours/release/lyrics.txt")
OUT = os.path.join(HERE, "..", "kit-lexicon.md")

DOMAINS = ["everyday", "body", "mind", "love", "family", "school", "work", "money", "law-state", "war",
           "faith-myth", "sport-games", "music", "screen", "science", "nature", "craft"]
STAKES = ["jobs", "wallet", "mind", "heart", "body", "state", "planet", "species"]
REGISTERS = ["tender", "funny", "ominous", "awe", "defiant", "sad", "smug", "panicked", "hopeful"]
RELS = ["part-of", "pairs-with", "opposite", "causes", "same-family", "rhymes"]
CONF = ["high", "medium", "low"]
WIDE = 8  # calibrated 2026-11-02 on 252 entries: median width 7; 8+ = top 68 (27 %)
REQ = ["id", "forms", "ai", "senses", "idioms", "anchors", "pivots", "enact", "sound", "stakes",
       "registers", "neighbors", "risk", "notes"]


def terms():
    return {t["id"]: t for t in json.load(open(os.path.join(HERE, "terms.json"), encoding="utf-8"))["terms"]}


def check_entry(e, T):
    errs = []
    i = e.get("id", "?")
    for k in REQ:
        if k not in e:
            errs.append(f"{i}: missing {k}")
    if errs:
        return errs
    if i not in T:
        errs.append(f"{i}: id not in terms.json")
    if not e["forms"]:
        errs.append(f"{i}: forms empty")
    if not isinstance(e.get("associates", []), list):
        errs.append(f"{i}: associates must be a list")
    a = e["ai"]
    for k in ("sense", "origin", "url", "confidence"):
        if k not in a:
            errs.append(f"{i}: ai.{k} missing")
    if a.get("confidence") not in CONF:
        errs.append(f"{i}: ai.confidence {a.get('confidence')!r}")
    if not e["senses"]:
        errs.append(f"{i}: no senses")
    for s in e["senses"]:
        if s.get("domain") not in DOMAINS:
            errs.append(f"{i}: domain {s.get('domain')!r}")
        if not s.get("meaning") or "phrase" not in s:
            errs.append(f"{i}: sense row incomplete")
    for p in e["pivots"]:
        if not p.get("line") or len(p.get("senses", [])) < 2:
            errs.append(f"{i}: pivot needs line + 2 senses")
        elif len(p["line"].split()) > 12:
            errs.append(f"{i}: pivot over 12 words: {p['line']}")
        for d in p.get("senses", []):
            if d != "ai" and d not in DOMAINS:
                errs.append(f"{i}: pivot sense {d!r}")
    for k in ("music", "picture", "type"):
        if k not in e["enact"]:
            errs.append(f"{i}: enact.{k} missing")
    so = e["sound"]
    for k in ("syllables", "stress", "rhymes", "slant"):
        if k not in so:
            errs.append(f"{i}: sound.{k} missing")
    for x in e["stakes"]:
        if x not in STAKES:
            errs.append(f"{i}: stake {x!r}")
    for x in e["registers"]:
        if x not in REGISTERS:
            errs.append(f"{i}: register {x!r}")
    for n in e["neighbors"]:
        if n.get("id") not in T:
            errs.append(f"{i}: neighbor {n.get('id')!r} not in terms.json")
        if n.get("rel") not in RELS:
            errs.append(f"{i}: rel {n.get('rel')!r}")
    for an in e["anchors"]:
        if not an.get("name") or "what" not in an:
            errs.append(f"{i}: anchor incomplete")
    txt = json.dumps(e, ensure_ascii=False)
    if "\u2014" in txt:
        errs.append(f"{i}: em dash present")
    return errs


def cmd_check(arg):
    """arg = a batch name (checks every entries/<batch>-p*.json and entries/<batch>.json) or one file path."""
    T = terms()
    if arg.endswith(".json"):
        paths, batch = [arg], re.sub(r"-p\d+$", "", os.path.splitext(os.path.basename(arg))[0])
    else:
        batch = arg
        paths = sorted(glob.glob(os.path.join(HERE, "entries", batch + "-p*.json")) + glob.glob(os.path.join(HERE, "entries", batch + ".json")))
    E, errs = [], []
    for p in paths:
        try:
            E += json.load(open(p, encoding="utf-8"))
        except Exception as ex:
            errs.append(f"{os.path.basename(p)}: invalid JSON: {ex}")
    errs += [x for e in E for x in check_entry(e, T)]
    ids = [e.get("id") for e in E]
    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        errs.append(f"duplicate ids: {dup}")
    want = {k for k, t in T.items() if t["batch"] == batch}
    miss = sorted(want - set(ids)) if want else []
    print(f"{batch}: {len(paths)} file(s), {len(E)} entries, {len(errs)} problems, {len(miss)} of {len(want)} ids not yet written")
    for x in errs:
        print("  " + x)
    if miss:
        print("  not yet written: " + ", ".join(miss))
    return 1 if errs else 0


def form_regex(forms):
    alts = sorted({f.lower() for f in forms if f.strip()}, key=len, reverse=True)
    return re.compile(r"(?<![a-z0-9])(" + "|".join(re.escape(a) for a in alts) + r")(?![a-z0-9])")


def load_lyrics():
    """Official lyrics (LYR/official/<song>.txt, the maker's own text) win over Whisper transcripts.
    Returns {song: text}, {song: "official" | "whisper"}, kc text."""
    songs, src = {}, {}
    for p in sorted(glob.glob(os.path.join(LYR, "*.lyrics.txt"))):
        name = os.path.basename(p)[:-len(".lyrics.txt")]
        off = os.path.join(LYR, "official", name + ".txt")
        path, src[name] = (off, "official") if os.path.exists(off) else (p, "whisper")
        lines = [re.sub(r"^\[[0-9:]+\]\s*", "", l) for l in open(path, encoding="utf-8") if not l.startswith("#")]
        songs[name] = " ".join(lines).lower().replace("’", "'")
    kc = open(KC, encoding="utf-8").read().lower().replace("’", "'") if os.path.exists(KC) else ""
    return songs, src, kc


def esc(s):
    return str(s).replace("|", "/").replace("\n", " ")


def cmd_build():
    T = terms()
    E = {}
    for p in sorted(glob.glob(os.path.join(HERE, "entries", "*.json"))):
        if os.path.basename(p).startswith("_"):
            continue
        for e in json.load(open(p, encoding="utf-8")):
            E[e["id"]] = e
    if "attention" not in E:
        for e in json.load(open(os.path.join(HERE, "entries", "_example.json"), encoding="utf-8")):
            E[e["id"]] = e
    problems = [x for e in E.values() for x in check_entry(e, T)]
    songs, src, kc = load_lyrics()
    n_off = sum(1 for v in src.values() if v == "official")
    for i, e in E.items():
        doms = sorted({s["domain"] for s in e["senses"]})
        e["_domains"] = doms
        e["_width"] = len(doms) + 1
        e["_class"] = "wide" if e["_width"] >= WIDE else ("mid" if e["_width"] >= 5 else "narrow")
        e["_native"] = [d for d in ("music", "screen") if d in doms]
        rx = form_regex(e["forms"] + [T[i]["term"].split(" (")[0]] if i in T else e["forms"])
        e["_refs"] = {n: len(rx.findall(t)) for n, t in songs.items() if rx.search(t)}
        e["_kc"] = len(rx.findall(kc))
    order = sorted(E.values(), key=lambda e: (-e["_width"], -len(e["_native"]), T.get(e["id"], {}).get("term", e["id"])))
    wide = [e for e in order if e["_class"] == "wide"]
    coll = []
    for a, b in combinations(wide, 2):
        shared = (set(a["_domains"]) & set(b["_domains"])) - {"everyday"}
        if len(shared) >= 4:
            coll.append((len(shared), a["id"], b["id"], sorted(shared)))
    coll.sort(key=lambda x: (-x[0], x[1], x[2]))
    missing = sorted(set(T) - set(E))

    L = ["---", "type: project", "created: 2026-11-02", "author: jep", "status: active", "---", "",
         "# Lexicon (the word kit)", "",
         "Generated by `lexicon/lexicon.py build` from `lexicon/entries/*.json`; edit the JSON, never this file. Schema: `lexicon/SCHEMA.md`. "
         f"Ref usage = how many of {len(songs)} reference songs use the term's own word family (`forms`; `associates` such as synonyms and homophones are never counted), plus the KC lyric. "
         f"Lyrics: {n_off} songs from the makers' official text (`D:\\work\\AIMVs\\lyrics\\official\\`), {len(songs) - n_off} from Whisper transcripts, marked `~` on each card (mishearings likely, e.g. P(Doom)'s \"orthogonality thesis\" heard as \"or the banality thesis\").", "",
         f"Entries {len(E)} of {len(T)} | wide (width {WIDE}+) {len(wide)} | mid (5-{WIDE - 1}) {sum(1 for e in E.values() if e['_class'] == 'mid')} | medium-native (music or screen sense) {sum(1 for e in E.values() if e['_native'])} | "
         f"Idi's seeds {sum(1 for e in E.values() if T.get(e['id'], {}).get('idi_seed'))} | unused in all refs {sum(1 for e in E.values() if not e['_refs'])} | schema problems {len(problems)}", ""]
    if missing:
        L += [f"Not yet written ({len(missing)}): " + ", ".join(missing), ""]
    L += ["## Index (widest first)", "",
          "| term | width | domains | native | refs | KC | best pivot |", "|---|---|---|---|---|---|---|"]
    for e in order:
        t = T.get(e["id"], {"term": e["id"], "idi_seed": False})
        star = " (Idi)" if t.get("idi_seed") else ""
        piv = e["pivots"][0]["line"] if e["pivots"] else ""
        L.append(f"| [[#^{e['id']}\\|{esc(t['term'])}]]{star} | {e['_width']} | {', '.join(e['_domains'])} | {'+'.join(e['_native'])} | "
                 f"{len(e['_refs'])} | {e['_kc']} | {esc(piv)} |")
    L += ["", "## Domain clusters (premise seeds: a song set in one life domain where these AI terms all mean something)", "",
          "| domain | wide terms with a sense here | count |", "|---|---|---|"]
    for d in DOMAINS:
        if d == "everyday":
            continue
        hits = [T.get(e["id"], {"term": e["id"]})["term"] for e in wide if d in e["_domains"]]
        if hits:
            L.append(f"| {d} | {', '.join(hits)} | {len(hits)} |")
    L += ["", "## Collisions (wide pairs sharing 4+ domains beyond everyday: combination candidates)", ""]
    if coll:
        L += ["| shared | pair | domains |", "|---|---|---|"]
        for n, a, b, d in coll[:80]:
            L.append(f"| {n} | {T.get(a, {'term': a})['term']} + {T.get(b, {'term': b})['term']} | {', '.join(d)} |")
        if len(coll) > 80:
            L.append(f"\n{len(coll) - 80} more pairs not shown.")
    else:
        L.append("none yet")
    L += ["", "## Cards", ""]
    for e in order:
        t = T.get(e["id"], {"term": e["id"], "kind": "?", "idi_seed": False})
        L.append(f"### {t['term']}")
        L.append(f"- `{e['id']}` | {t['kind']} | width {e['_width']} ({e['_class']}) | native {'+'.join(e['_native']) or '-'}"
                 f"{' | Idi seed' if t.get('idi_seed') else ''} ^{e['id']}")
        a = e["ai"]
        L.append(f"- AI: {a['sense']}. Origin: {a['origin']}{' ' + a['url'] if a['url'] else ''} [{a['confidence']}]")
        L.append("- senses: " + "; ".join(f"**{s['domain']}** {s['meaning']} (\"{s['phrase']}\")" for s in e["senses"]))
        L.append(f"- forms (counted): {', '.join(e['forms'])}"
                 + (f" | associates (not counted): {', '.join(e['associates'])}" if e.get("associates") else ""))
        if e["idioms"]:
            L.append("- idioms: " + ", ".join(e["idioms"]))
        if e["anchors"]:
            L.append("- anchors: " + "; ".join(f"{x['name']}: {x['what']}{' ' + x['url'] if x.get('url') else ''}" for x in e["anchors"]))
        if e["pivots"]:
            L.append("- pivots (jep drafts): " + " / ".join(f"\"{p['line']}\" ({'+'.join(p['senses'])})" for p in e["pivots"]))
        en = e["enact"]
        L.append(f"- enact: music: {en['music']} | picture: {en['picture']} | type: {en['type']}")
        so = e["sound"]
        L.append(f"- sound: {so['syllables']} syl, {so['stress']}; rhymes {', '.join(so['rhymes'])}; slant {', '.join(so['slant'])}")
        L.append(f"- stakes {', '.join(e['stakes']) or '-'} | registers {', '.join(e['registers']) or '-'}")
        if e["neighbors"]:
            L.append("- neighbors: " + ", ".join(f"[[#^{n['id']}|{T.get(n['id'], {'term': n['id']})['term']}]] ({n['rel']})" for n in e["neighbors"] if n["id"] in E)
                     + ("" if all(n["id"] in E for n in e["neighbors"]) else " + " + ", ".join(n["id"] for n in e["neighbors"] if n["id"] not in E) + " (unwritten)"))
        refs = ", ".join(f"{k}{'~' if src[k] == 'whisper' else ''} {v}" for k, v in sorted(e["_refs"].items(), key=lambda kv: -kv[1]))
        L.append(f"- refs: {len(e['_refs'])} of {len(songs)} songs{': ' + refs if refs else ''} | KC {e['_kc']}")
        if e["risk"]:
            L.append(f"- risk: {e['risk']}")
        if e["notes"]:
            L.append(f"- note: {e['notes']}")
        L.append("")
    if problems:
        L += ["## Schema problems", ""] + [f"- {p}" for p in problems]
    open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print(f"built {OUT}: {len(E)} entries, {len(wide)} wide, {len(coll)} collisions, {len(problems)} problems, {len(missing)} missing")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "check":
        sys.exit(cmd_check(sys.argv[2]))
    elif len(sys.argv) >= 2 and sys.argv[1] == "build":
        cmd_build()
    else:
        print(__doc__)
