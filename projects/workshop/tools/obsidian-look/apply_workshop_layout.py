"""Make the live layout file equal the saved 'Workshop' layout, so the next
"Reload app without saving" opens it. Backs up the current layout first. Atomic replace.
Usage: python -I apply_workshop_layout.py OBSIDIAN_DIR BACKUP_PATH ZOOM"""
import io
import json
import os
import shutil
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
obs, backup, zoom = sys.argv[1], sys.argv[2], float(sys.argv[3])
live_p = os.path.join(obs, "workspace.json")
cur = json.load(open(live_p, encoding="utf-8"))
ws = json.load(open(os.path.join(obs, "workspaces.json"), encoding="utf-8"))["workspaces"]["Workshop"]
os.makedirs(os.path.dirname(backup), exist_ok=True)
shutil.copyfile(live_p, backup)

new = {k: ws[k] for k in ("main", "left", "right", "left-ribbon", "active")}
new["lastOpenFiles"] = cur.get("lastOpenFiles", [])


def leaves(n, acc):
    if n.get("type") == "leaf":
        acc.append(n)
    for c in n.get("children", []):
        leaves(c, acc)
    return acc


for l in leaves(new["main"], []):
    if l["state"]["type"] == "canvas":
        l["state"]["state"]["viewState"]["zoom"] = zoom
tmp = live_p + ".jep-tmp"
with open(tmp, "w", encoding="utf-8", newline="") as f:
    json.dump(new, f, indent=2, ensure_ascii=False)
json.load(open(tmp, encoding="utf-8"))
os.replace(tmp, live_p)
print("live layout replaced; backup at", backup)
for l in leaves(new["main"], []):
    print("  main leaf:", l["state"]["type"], l["state"]["state"].get("file"), l["state"]["state"].get("viewState", ""))
print("  left collapsed:", new["left"].get("collapsed"), "| right collapsed:", new["right"].get("collapsed"))
