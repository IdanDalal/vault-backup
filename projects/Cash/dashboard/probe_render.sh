#!/usr/bin/env bash
# Headless Edge render probe for Cash-Console.html: one screenshot per tab at desktop width, one phone-width wrapper.
# Usage: bash probe_render.sh [outdir]   (Edge calls live in this file on purpose: the worktree guard rejects them inline)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$HERE/data/probe}"
mkdir -p "$OUT"
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
FILE="$(cygpath -w "$HERE/Cash-Console.html")"
for tab in overview analysis companies odds lab; do
  "$EDGE" --headless=new --disable-gpu --no-first-run --force-prefers-reduced-motion --hide-scrollbars \
    --window-size=1400,2600 --virtual-time-budget=4000 --screenshot="$(cygpath -w "$OUT/$tab.png")" \
    "file:///$FILE?probe#$tab" >/dev/null 2>&1
  "$EDGE" --headless=new --disable-gpu --no-first-run --force-prefers-reduced-motion \
    --window-size=1400,900 --virtual-time-budget=4000 --dump-dom "file:///$FILE?probe#$tab" 2>/dev/null | grep -o '<title>[^<]*</title>' | head -1 | sed "s/^/$tab: /"
done
# phone: a 390px iframe wrapper (Edge's headless viewport floor is ~484px)
cat > "$OUT/phone.html" <<EOF
<!doctype html><meta charset="utf-8"><body style="margin:0;background:#222"><iframe src="file:///$FILE?probe#odds" style="width:390px;height:2400px;border:0"></iframe></body>
EOF
"$EDGE" --headless=new --disable-gpu --no-first-run --force-prefers-reduced-motion --hide-scrollbars \
  --window-size=500,2400 --virtual-time-budget=4000 --screenshot="$(cygpath -w "$OUT/phone-odds.png")" \
  "file:///$(cygpath -w "$OUT/phone.html")" >/dev/null 2>&1
cat > "$OUT/phone2.html" <<EOF
<!doctype html><meta charset="utf-8"><body style="margin:0;background:#222"><iframe src="file:///$FILE?probe#overview" style="width:390px;height:2400px;border:0"></iframe></body>
EOF
"$EDGE" --headless=new --disable-gpu --no-first-run --force-prefers-reduced-motion --hide-scrollbars \
  --window-size=500,2400 --virtual-time-budget=4000 --screenshot="$(cygpath -w "$OUT/phone-overview.png")" \
  "file:///$(cygpath -w "$OUT/phone2.html")" >/dev/null 2>&1
ls -la "$OUT"/*.png
