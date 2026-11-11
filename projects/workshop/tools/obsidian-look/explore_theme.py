"""Explore Minimal's @settings blocks against Idi's stored Style Settings values. Read-only.
Usage: python explore_theme.py PYLIB THEME_CSS STYLE_DATA_JSON [OTHER_STYLE_DATA_JSON]"""
import io
import json
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, sys.argv[1])
import yaml  # noqa: E402

css = open(sys.argv[2], encoding="utf-8").read()
data = json.load(open(sys.argv[3], encoding="utf-8"))
blocks = re.findall(r"/\*\s*@settings(.*?)\*/", css, flags=re.S)
defs = {}
for b in blocks:
    y = yaml.safe_load(b.replace("\t", "    "))
    sec = y["id"]
    for s in y["settings"]:
        if "id" in s:
            defs[(sec, s["id"])] = s
    print("section", sec, "settings", len(y["settings"]))

by_type = {}
missing = []
for k, v in data.items():
    parts = k.split("@@")
    sec, sid = parts[0], parts[1]
    mode = parts[2] if len(parts) > 2 else ""
    d = defs.get((sec, sid))
    if not d:
        missing.append((k, v))
        continue
    by_type.setdefault(d["type"], []).append((sid, mode, v, d.get("format"), d.get("opacity"), d.get("default"),
                                              [a.get("id") + ":" + a.get("format", "") for a in d.get("alt-format", [])] if d.get("alt-format") else ""))
for t, items in by_type.items():
    print()
    print("==", t, len(items))
    for it in items:
        print("   ", it)
print()
print("== ids absent from this theme version:", len(missing))
for k, v in missing:
    print("   ", k, "=", v)

# defaults that are ON without any stored value
print()
print("== class-toggle with default true, not stored as false:")
for (sec, sid), d in defs.items():
    if d["type"] == "class-toggle" and d.get("default") is True and data.get(sec + "@@" + sid) is not False:
        print("   ", sec, sid)
print("== class-select defaults not overridden:")
for (sec, sid), d in defs.items():
    if d["type"] == "class-select" and (sec + "@@" + sid) not in data:
        print("   ", sec, sid, "default=", d.get("default"), "options=", [o if isinstance(o, str) else o.get("value") for o in d.get("options", [])][:6])

if len(sys.argv) > 4:
    other = json.load(open(sys.argv[4], encoding="utf-8"))
    print()
    print("== differences vs the other config:")
    for k in sorted(set(data) | set(other)):
        if data.get(k) != other.get(k):
            print("   ", k, ":", data.get(k), "|", other.get(k))
