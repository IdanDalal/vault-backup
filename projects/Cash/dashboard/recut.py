#!/usr/bin/env python3
"""Re-cut the buys against actual cash after the sale. Usage: python recut.py <cash_usd> [fee_pct] [googl_kept]"""
import re, sys
from pathlib import Path
import transition as tr

CASH = Path(__file__).resolve().parent.parent
cash = float(sys.argv[1]); fee = float(sys.argv[2]) if len(sys.argv) > 2 else 0.003; kept = int(sys.argv[3]) if len(sys.argv) > 3 else 9

def fm(p, k): return float(re.search(rf"^{k}:\s*(.*)$", p.read_text(encoding="utf-8"), re.M).group(1))
P = {t: fm(CASH / "companies" / f"{t}.md", "last_price") for t in tr.ORDER}
T = {t: int(fm(CASH / "companies" / f"{t}.md", "pct")) + int(fm(CASH / "companies" / f"{t}.md", "earmark_pct")) for t in tr.ORDER}
buyable = cash / (1 + fee)
budget = kept * P["GOOGL"] + buyable
d, sh, spent = tr.solve(P, T, budget, {"GOOGL": kept})
buys = spent - kept * P["GOOGL"]
print(f"cash {cash:,.2f} | buyable {buyable:,.2f} | shares {buys:,.2f} + fees {buys * fee:,.2f} = {buys * (1 + fee):,.2f} | left {cash - buys * (1 + fee):,.2f} | drift {d:.1f}")
for t in tr.ORDER:
    if t != "GOOGL":
        print(f"  {t:5} {sh[t]:2d} @ {P[t]:>9,.2f}  ${sh[t] * P[t]:>9,.2f}  {sh[t] * P[t] / budget * 100:4.1f}% vs {T[t]}")
