"""hub_check.py - prove the Workshop board is true.

Usage:  python -I hub_check.py [VAULT_ROOT]
Reads only. Exit code 0 = clean, 1 = at least one ERROR.

Checks, per hub in projects/workshop/hubs/:
  1. required properties present, enums respected
  2. every wikilink (frontmatter and body) points at a file that exists
  3. `last` is not older than the newest session-log row naming the project
Checks, board-wide:
  4. active hubs <= WIP_CAP
  5. every note under projects/workshop has type, created, author
  6. banned characters and words in every file under projects/workshop
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

WIP_CAP = 2
STATUS = {"active", "paused", "done", "archived"}
BALL = {"Idi", "jep", "4090", "none"}
HILO = {"high", "low"}
REQUIRED = ["type", "created", "author", "status", "next", "ball", "value", "effort", "last", "entry"]
# words in the session log's Session column that mean "this row belongs to that hub"
LOG_KEYS = {
    "AIMV": ["aimv", "pay attention", "knowledge cutoff"],
    "XCOM": ["xcom"],
    "Workshop": ["workshop"],
    "I4": ["i4", "inception"],
    "DECADEnts": ["decadents"],
    "Curtains": ["curtains"],
    "Cash": ["cash"],
    "Kid Studio": ["kid studio", "kidstudio", "studio v"],
    "Tutoring": ["tutoring"],
    "HQ": ["hq", "worktree", "laptop", "name guard", "local agent", "local model", "bsod"],
    "Idiverse": ["idiverse", "atomic note"],
}
BANNED = ["—", "load-bearing", "Idan "]

root = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ws = os.path.join(root, "projects", "workshop")
hubs_dir = os.path.join(ws, "hubs")
errors, warns = [], []


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm, key = {}, None
    for line in parts[1].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            fm[key] = val
        elif key and line.strip().startswith("- "):
            fm[key] = (fm[key] + " " + line.strip()[2:]).strip()
    return fm, parts[2]


# index every file in the vault once, skipping copies and git internals
by_rel, by_base = set(), {}
for d, dirs, files in os.walk(root):
    dirs[:] = [x for x in dirs if x not in (".git", ".claude", ".obsidian", "node_modules")]
    for fn in files:
        rel = os.path.relpath(os.path.join(d, fn), root).replace("\\", "/")
        by_rel.add(rel.lower())
        by_base.setdefault(os.path.splitext(fn)[0].lower(), []).append(rel)
        by_base.setdefault(fn.lower(), []).append(rel)


def link_ok(target):
    t = target.split("|")[0].split("#")[0].strip()
    if not t:
        return True
    low = t.lower()
    if "/" in low:
        return low in by_rel or (low + ".md") in by_rel
    return low in by_base


def links_in(text):
    return re.findall(r"!?\[\[([^\]]+)\]\]", text)


# session log: newest row date per hub
log_last = {}
log_path = os.path.join(root, "projects", "intent-log.md")
if os.path.exists(log_path):
    for line in read(log_path).splitlines():
        m = re.match(r"^\|\s*(\d{4}-\d{2}-\d{2})[^|]*\|([^|]*)\|", line)
        if not m:
            continue
        date, session = m.group(1), m.group(2).lower()
        for hub, keys in LOG_KEYS.items():
            if any(k in session for k in keys):
                if date > log_last.get(hub, ""):
                    log_last[hub] = date
else:
    warns.append("session log not found: projects/intent-log.md")

rows, active = [], []
for fn in sorted(os.listdir(hubs_dir)):
    if not fn.endswith(".md"):
        continue
    name = fn[:-3]
    text = read(os.path.join(hubs_dir, fn))
    fm, body = frontmatter(text)
    for k in REQUIRED:
        if not fm.get(k):
            errors.append(f"{name}: missing property `{k}`")
    if fm.get("type") != "hub":
        errors.append(f"{name}: type is `{fm.get('type')}`, expected `hub`")
    if fm.get("status") not in STATUS:
        errors.append(f"{name}: status `{fm.get('status')}` outside {sorted(STATUS)}")
    if fm.get("ball") not in BALL:
        errors.append(f"{name}: ball `{fm.get('ball')}` outside {sorted(BALL)}")
    for k in ("value", "effort"):
        if fm.get(k) not in HILO:
            errors.append(f"{name}: {k} `{fm.get(k)}` outside high/low")
    if fm.get("last") and not re.match(r"^\d{4}-\d{2}-\d{2}$", fm["last"]):
        errors.append(f"{name}: last `{fm['last']}` is not YYYY-MM-DD")
    if fm.get("cost_min") and not fm["cost_min"].isdigit():
        errors.append(f"{name}: cost_min `{fm['cost_min']}` is not a whole number")
    newest = log_last.get(name, "")
    if newest and fm.get("last") and newest > fm["last"]:
        errors.append(f"{name}: STALE, card says last {fm['last']}, session log has {newest}")
    if name not in LOG_KEYS:
        warns.append(f"{name}: no session-log keywords in LOG_KEYS, staleness unchecked")
    if fm.get("status") == "active":
        active.append(name)
    rows.append((name, fm.get("status", "?"), fm.get("ball", "?"), fm.get("last", "?"), newest or "-"))

if len(active) > WIP_CAP:
    warns.append(f"WIP: {len(active)} active ({', '.join(active)}), cap is {WIP_CAP}")

for d, dirs, files in os.walk(ws):
    for fn in files:
        p = os.path.join(d, fn)
        rel = os.path.relpath(p, root).replace("\\", "/")
        if not fn.endswith(".md"):
            continue
        text = read(p)
        fm, _ = frontmatter(text)
        for k in ("type", "created", "author"):
            if not fm.get(k):
                errors.append(f"{rel}: frontmatter missing `{k}`")
        for target in links_in(text):
            if not link_ok(target):
                errors.append(f"{rel}: link target missing: [[{target}]]")
        if "/research/" in rel:
            continue  # agent-written evidence files quote older text verbatim
        for b in BANNED:
            if b in text:
                errors.append(f"{rel}: banned text {b!r} x{text.count(b)}")

print(f"vault: {root}")
print(f"{'hub':<12}{'status':<10}{'ball':<6}{'last':<12}log newest")
for r in rows:
    print(f"{r[0]:<12}{r[1]:<10}{r[2]:<6}{r[3]:<12}{r[4]}")
print(f"\nhubs {len(rows)} | active {len(active)} | errors {len(errors)} | warnings {len(warns)}")
for w in warns:
    print("WARN  " + w)
for e in errors:
    print("ERROR " + e)
sys.exit(1 if errors else 0)
