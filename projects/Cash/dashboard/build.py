#!/usr/bin/env python3
"""Build the Cash presentation dashboards from the vault's company notes.

Usage:  python3 build.py            # builds Cash-Idi.html and Cash-Mom.html
Reads:  ../companies/*.md frontmatter, total_usd from ../Idi.md and ../Mom.md
Output: self-contained, mobile-first HTML — safe to send as a file.
"""
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASH = HERE.parent

TIERS = {1: "The Core", 2: "Silicon Backbone", 3: "Adjacent Exponentials"}


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---"):
        return {}
    end = text.index("\n---", 3)
    d = {}
    for line in text[4:end].splitlines():
        line = line.strip()
        if not line or line.startswith("-") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith('"'):
            v = json.loads(v)
        else:
            try:
                v = int(v)
            except ValueError:
                try:
                    v = float(v)
                except ValueError:
                    pass
        d[k.strip()] = v
    return d


def load_companies():
    rows = [frontmatter(p) for p in sorted((CASH / "companies").glob("*.md"))]
    rows = [r for r in rows if r.get("status") == "active"]
    for r in rows:
        r["total"] = r["pct"] + r["earmark_pct"]
    rows.sort(key=lambda r: (r["tier"], -r["total"], r["ticker"]))
    return rows


def fmt_usd(x):
    return f"${x:,.0f}"


def bar_row(r, max_total, total_usd):
    base_w = r["pct"] / max_total * 100
    earm_w = r["earmark_pct"] / max_total * 100
    tier = r["tier"]
    dollars = fmt_usd(total_usd * r["total"] / 100) if total_usd > 0 else "—"
    earm_seg = (
        f'<span class="seg earm t{tier}" style="width:{earm_w:.2f}%"></span>'
        if r["earmark_pct"] else ""
    )
    badge = (
        f'<span class="badge">+{r["earmark_pct"]}% → {r["earmark_for"]}</span>'
        if r["earmark_pct"] else ""
    )
    return f"""
      <div class="row">
        <div class="row-head">
          <span class="tick">{r["ticker"]}</span>
          <span class="comp">{r["company"]}</span>
          {badge}
          <span class="nums"><b>{r["total"]}%</b> · {dollars}</span>
        </div>
        <div class="bar"><span class="seg t{tier}" style="width:{base_w:.2f}%"></span>{earm_seg}</div>
        <div class="conv">{r["conviction"]}</div>
      </div>"""


def build(name, rows):
    total_usd = frontmatter(CASH / f"{name}.md").get("total_usd", 0) or 0
    max_total = max(r["total"] for r in rows)
    tier_pct = {t: sum(r["total"] for r in rows if r["tier"] == t) for t in TIERS}

    tiles = f"""
      <div class="tiles">
        <div class="tile"><div class="tile-v">{len(rows)}</div><div class="tile-l">positions</div></div>
        <div class="tile"><div class="tile-v">{tier_pct[1]}/{tier_pct[2]}/{tier_pct[3]}</div><div class="tile-l">tier split %</div></div>
        <div class="tile"><div class="tile-v">{fmt_usd(total_usd) if total_usd else "—"}</div><div class="tile-l">total invested</div></div>
      </div>"""

    comp_bar = "".join(
        f'<span class="seg t{t}" style="width:{tier_pct[t]}%"></span>' for t in TIERS
    )
    legend = "".join(
        f'<span class="chip"><span class="dot t{t}"></span>{TIERS[t]} · {tier_pct[t]}%</span>'
        for t in TIERS
    )

    sections = ""
    for t, tname in TIERS.items():
        section_rows = "".join(
            bar_row(r, max_total, total_usd) for r in rows if r["tier"] == t
        )
        sections += f"""
      <section>
        <h2><span class="dot t{t}"></span>Tier {t} — {tname} <span class="h2-pct">{tier_pct[t]}%</span></h2>
        {section_rows}
      </section>"""

    unset = (
        ""
        if total_usd
        else f'<p class="note">Dollar amounts appear once <code>total_usd</code> is set in <code>{name}.md</code> and this page is rebuilt.</p>'
    )

    html = HTML_TEMPLATE
    for token, value in {
        "%%TITLE%%": f"Cash — {name}",
        "%%TILES%%": tiles,
        "%%COMPBAR%%": comp_bar,
        "%%LEGEND%%": legend,
        "%%SECTIONS%%": sections,
        "%%UNSET%%": unset,
        "%%DATE%%": date.today().isoformat(),
    }.items():
        html = html.replace(token, value)

    out = HERE / f"Cash-{name}.html"
    out.write_text(html)
    return out


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%%</title>
<style>
  :root {
    color-scheme: light;
    --surface: #fcfcfb; --page: #f9f9f7;
    --ink: #0b0b0b; --ink-2: #52514e; --muted: #898781;
    --hairline: #e1e0d9; --border: rgba(11,11,11,0.10);
    --t1: #2a78d6; --t1-light: #86b6ef;
    --t2: #eb6834; --t3: #1baf7a;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      color-scheme: dark;
      --surface: #1a1a19; --page: #0d0d0d;
      --ink: #ffffff; --ink-2: #c3c2b7; --muted: #898781;
      --hairline: #2c2c2a; --border: rgba(255,255,255,0.10);
      --t1: #3987e5; --t1-light: #1c5cab;
      --t2: #d95926; --t3: #199e70;
    }
  }
  * { box-sizing: border-box; margin: 0; }
  body {
    background: var(--page); color: var(--ink);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
    padding: 16px; display: flex; justify-content: center;
  }
  main { width: 100%; max-width: 640px; }
  header h1 { font-size: 1.5rem; margin-bottom: 2px; }
  header p { color: var(--ink-2); font-size: 0.9rem; margin-bottom: 16px; }
  .tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 16px; }
  .tile { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 10px 12px; }
  .tile-v { font-size: 1.25rem; font-weight: 700; }
  .tile-l { font-size: 0.75rem; color: var(--muted); }
  .compbar { display: flex; gap: 2px; height: 14px; border-radius: 4px; overflow: hidden; margin-bottom: 8px; }
  .compbar .seg { display: block; height: 100%; }
  .legend { display: flex; flex-wrap: wrap; gap: 6px 14px; margin-bottom: 20px; font-size: 0.85rem; color: var(--ink-2); }
  .chip { display: inline-flex; align-items: center; gap: 6px; }
  .dot { width: 10px; height: 10px; border-radius: 3px; display: inline-block; flex: none; }
  .t1 { background: var(--t1); } .t2 { background: var(--t2); } .t3 { background: var(--t3); }
  .earm.t1 { background: var(--t1-light); }
  section { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 14px 14px 6px; margin-bottom: 14px; }
  h2 { font-size: 1rem; display: flex; align-items: center; gap: 8px; padding-bottom: 10px; border-bottom: 1px solid var(--hairline); }
  .h2-pct { margin-left: auto; color: var(--muted); font-weight: 500; }
  .row { padding: 10px 0; border-bottom: 1px solid var(--hairline); }
  .row:last-child { border-bottom: 0; }
  .row-head { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
  .tick { font-weight: 700; }
  .comp { color: var(--ink-2); font-size: 0.85rem; }
  .nums { margin-left: auto; font-size: 0.9rem; font-variant-numeric: tabular-nums; }
  .badge { font-size: 0.7rem; color: var(--ink-2); border: 1px solid var(--border); border-radius: 999px; padding: 1px 7px; white-space: nowrap; }
  .bar { display: flex; gap: 2px; height: 8px; margin: 6px 0 4px; }
  .bar .seg { display: block; height: 100%; border-radius: 0 4px 4px 0; }
  .bar .seg:first-child { border-radius: 4px 0 0 4px; }
  .bar .seg:only-child { border-radius: 4px; }
  .conv { font-size: 0.8rem; color: var(--muted); }
  .note { color: var(--ink-2); font-size: 0.85rem; margin-bottom: 14px; }
  footer { color: var(--muted); font-size: 0.75rem; text-align: center; padding: 10px 0 20px; }
  code { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 0 4px; font-size: 0.85em; }
</style>
</head>
<body>
<main>
  <header>
    <h1>%%TITLE%%</h1>
    <p>MAGNA MOBSTA, extended — high-conviction, long-term, exponential technologies</p>
  </header>
  %%TILES%%
  <div class="compbar">%%COMPBAR%%</div>
  <div class="legend">%%LEGEND%%</div>
  %%UNSET%%
  %%SECTIONS%%
  <footer>Locked 2026-07-24 · rebuilt %%DATE%% · lighter bar segments are IPO earmarks (convert at the OpenAI / Anthropic listings)</footer>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    rows = load_companies()
    assert sum(r["total"] for r in rows) == 100, "allocation must sum to 100"
    for name in ("Idi", "Mom"):
        out = build(name, rows)
        print(f"built {out.name}: {len(rows)} positions, sums to 100%")
