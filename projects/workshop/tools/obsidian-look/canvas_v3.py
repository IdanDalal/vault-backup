"""Board.canvas layout v3, for the Workshop layout's canvas pane (76 % of the window).

Measured on D:\\work\\screens\\Layout.png (2026-11-11 16:15): the pane shows 2634 x 1905 canvas
units at zoom -0.66, aspect 1.382. One table row = 30 units.
Tables stack on the left; the Board (two columns: active, paused) takes the right edge full height.
Canvas 2032 x 1470 units, aspect 1.382: zoom-to-fit gives about 0.80, 27 % larger than before.
Keeps node ids and each node's other fields. Usage: python -I canvas_v3.py WORKTREE_ROOT"""
import json
import os
import sys

root = sys.argv[1]
P = "projects/workshop/"
path = os.path.join(root, P, "Board.canvas")
old = json.load(open(path, encoding="utf-8"))
by_id = {n["id"]: n for n in old["nodes"]}
layout = {
    "00000000b0a2d001": (0, 0, 1392, 270),       # Now: toolbar, header, up to 2 groups, 4 rows
    "00000000b0a2d006": (0, 290, 1392, 410),     # Matrix: 3 groups, 8 rows
    "00000000b0a2d002": (0, 720, 1392, 570),     # Morning: 2 groups, 14 rows
    "00000000b0a2d003": (0, 1310, 686, 160),     # clock check
    "00000000b0a2d004": (706, 1310, 686, 160),   # jar
    "00000000b0a2d005": (1412, 0, 620, 1470),    # Board: 2 columns, room for 9 cards
}
JAR = ("**Jar** Built 204 / Received 103, still since 2026-09-05. Waiting: C4, C5 (reply `W C4`, `W C5`).\n\n"
       "[[projects/wins-jar|Open the jar]] · [[projects/workshop/Workshop|Rules and fields]]")
order = ["00000000b0a2d001", "00000000b0a2d006", "00000000b0a2d002", "00000000b0a2d003", "00000000b0a2d004", "00000000b0a2d005"]
assert set(order) == set(by_id), "node set changed: %s" % sorted(by_id)
lines = []
for i in order:
    n = dict(by_id[i])
    n["x"], n["y"], n["width"], n["height"] = layout[i]
    if n["type"] == "text":
        n["text"] = JAR
    keys = ["id", "type", "x", "y", "width", "height"] + [k for k in n if k not in ("id", "type", "x", "y", "width", "height")]
    lines.append("\t\t" + json.dumps({k: n[k] for k in keys}, separators=(",", ":"), ensure_ascii=False))
NL = chr(10)
text = "{" + NL + "\t\"nodes\":[" + NL + ("," + NL).join(lines) + NL + "\t]," + NL + "\t\"edges\":" + json.dumps(old.get("edges", []), separators=(",", ":")) + NL + "}"
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(text)
chk = json.load(open(path, encoding="utf-8"))
ns = chk["nodes"]
w = max(n["x"] + n["width"] for n in ns) - min(n["x"] for n in ns)
h = max(n["y"] + n["height"] for n in ns) - min(n["y"] for n in ns)
print("nodes", len(ns), "canvas", w, "x", h, "aspect %.3f" % (w / h))
for a in range(len(ns)):
    for b in range(a + 1, len(ns)):
        A, B = ns[a], ns[b]
        if A["x"] < B["x"] + B["width"] and B["x"] < A["x"] + A["width"] and A["y"] < B["y"] + B["height"] and B["y"] < A["y"] + A["height"]:
            print("OVERLAP", A["id"][-1], B["id"][-1])
pane_w, pane_h = 1667, 1206
scale = min(pane_w * 0.97 / w, pane_h * 0.97 / h)
print("fit scale in a %dx%d CSS px pane: %.3f (was 0.633); one table row = %.1f CSS px = %.0f device px at 175 %%" % (pane_w, pane_h, scale, 30 * scale, 30 * scale * 1.75))
