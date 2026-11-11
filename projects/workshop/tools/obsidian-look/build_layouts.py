"""Build STAGE/workspaces.json and STAGE/appearance.json for D:\\work\\vault.

- Idi's three saved workspaces (archived Curtains config), adapted: files that exist here,
  plugin-only panels (calendar, recent-files) swapped for core panels.
- A new "Workshop" layout: Board.canvas beside Idi's Whiteboard.
Usage: python -I build_layouts.py ARCHIVE_OBSIDIAN_DIR LIVE_OBSIDIAN_DIR VAULT_ROOT STAGE_DIR
"""
import copy
import datetime
import io
import json
import os
import secrets
import shutil
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
arch, live, vault, stage = sys.argv[1:5]
WB = "Idi's Whiteboard.md"
REF = "projects/workshop/Workshop.md"
BOARD = "projects/workshop/Board.canvas"
CORE = {"markdown", "canvas", "graph", "localgraph", "bookmarks", "all-properties", "outline", "backlink",
        "outgoing-link", "tag", "file-explorer", "search"}
now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")

old = json.load(open(os.path.join(arch, "workspaces.json"), encoding="utf-8"))
cur = json.load(open(os.path.join(live, "workspace.json"), encoding="utf-8"))


def nid():
    return secrets.token_hex(8)


def leaves(node, acc):
    if node.get("type") == "leaf":
        acc.append(node)
    for c in node.get("children", []):
        leaves(c, acc)
    return acc


out, notes = {}, []
for name, ws in old["workspaces"].items():
    ws = copy.deepcopy(ws)
    md_seen = 0
    has = {l["state"]["type"] for side in ("main", "left", "right") for l in leaves(ws[side], [])}
    for side in ("main", "left", "right"):
        for l in leaves(ws[side], []):
            st = l["state"]
            t = st["type"]
            if t == "calendar":
                new = "backlink" if "backlink" not in has else "tag"
                st.clear()
                st.update({"type": new, "state": {"file": WB} if new == "backlink" else {"sortOrder": "frequency", "useHierarchy": True}})
                has.add(new)
                notes.append("%s: calendar panel (plugin) -> %s" % (name, new))
            elif t == "recent-files":
                st.clear()
                st.update({"type": "bookmarks", "state": {}})
                notes.append("%s: recent-files tab (plugin) -> bookmarks" % name)
            elif t == "markdown":
                st["state"]["file"] = WB if md_seen == 0 else REF
                md_seen += 1
            elif t == "search":
                st["state"]["query"] = ""
            elif isinstance(st.get("state"), dict) and "file" in st["state"]:
                st["state"]["file"] = WB
            st.pop("title", None)
    ws["mtime"] = now
    out[name] = ws

canvas_id, wb_id = nid(), nid()
left = copy.deepcopy(cur["left"])
left["collapsed"] = True
right = copy.deepcopy(cur["right"])
right["collapsed"] = True
out["Workshop"] = {
    "main": {"id": nid(), "type": "split", "direction": "vertical", "children": [
        {"id": nid(), "type": "tabs", "dimension": 76, "children": [
            {"id": canvas_id, "type": "leaf", "state": {"type": "canvas", "state": {
                "file": BOARD, "viewState": {"x": 1230, "y": 735, "zoom": -0.66}},
                "icon": "lucide-layout-dashboard", "title": "Board"}}]},
        {"id": nid(), "type": "tabs", "dimension": 24, "children": [
            {"id": wb_id, "type": "leaf", "state": {"type": "markdown", "state": {
                "file": WB, "mode": "source", "source": False}, "icon": "lucide-file", "title": "Idi's Whiteboard"}}]}]},
    "left": left, "right": right, "left-ribbon": copy.deepcopy(cur["left-ribbon"]),
    "active": wb_id, "mtime": now}

existing = os.path.join(live, "workspaces.json")
kept = []
if os.path.exists(existing):
    have = json.load(open(existing, encoding="utf-8"))
    for n, w in have.get("workspaces", {}).items():
        if n not in out:
            out[n] = w
            kept.append(n)
        else:
            out[n + " (Idi's, before 11-11)"] = w
            kept.append(n + " (renamed copy)")
result = {"workspaces": out, "active": "Workshop"}

# validation
problems = []
for name, ws in out.items():
    if name in kept:
        continue
    for side in ("main", "left", "right"):
        for l in leaves(ws[side], []):
            t = l["state"]["type"]
            if t not in CORE:
                problems.append("%s: non-core panel %s" % (name, t))
            f = (l["state"].get("state") or {}).get("file")
            if f and not os.path.isfile(os.path.join(vault, f)):
                problems.append("%s: missing file %s" % (name, f))
    ids = [n["id"] for side in ("main", "left", "right") for n in leaves(ws[side], [])]
    if ws.get("active") and ws["active"] not in ids:
        problems.append("%s: active leaf id not in layout" % name)

os.makedirs(os.path.join(stage, "snippets"), exist_ok=True)
with open(os.path.join(stage, "workspaces.json"), "w", encoding="utf-8", newline="") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
appearance = {"theme": "obsidian", "cssTheme": "Minimal", "accentColor": "#8a5cf4", "showViewHeader": False,
              "baseFontSize": 15, "showRibbon": True, "enabledCssSnippets": ["idi-black", "properties-layout"]}
with open(os.path.join(stage, "appearance.json"), "w", encoding="utf-8", newline="") as f:
    json.dump(appearance, f, indent=2)
shutil.copyfile(os.path.join(arch, "snippets", "properties-layout.css"), os.path.join(stage, "snippets", "properties-layout.css"))

print("workspaces:", list(out.keys()))
print("kept from the live file:", kept or "none (no workspaces.json existed)")
for n in notes:
    print("  swap:", n)
print("problems:", problems or "none")
for name, ws in out.items():
    ts = {}
    for side in ("main", "left", "right"):
        for l in leaves(ws[side], []):
            ts[l["state"]["type"]] = ts.get(l["state"]["type"], 0) + 1
    print("  %-34s %s" % (name, ts))
