#!/usr/bin/env python3
"""Rebuild ../transition.md: whole-share plan for the pooled account (Idi + Mom).

Usage:  python update_prices.py && python transition.py [YYYY-MM-DD] [mom_usd]
        mom_usd = the exact dollars Mom's NIS conversion produced; until it is
        known, MOM_NIS / fx_rate_planning is used as a provisional figure.
Method: one pool (both owners' money sits in the same ONE ZERO account), one
        set of targets. Exhaustive search over floor / floor+1 shares per
        position, GOOGL included (it decides how many of the 55 to sell),
        objective = sum of absolute drift in points + 0.5 x idle cash %.
Writes: ../transition.md, total_usd in ../Idi.md and ../Mom.md, Mom's rate callout.
"""
import itertools, re, sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASH = HERE.parent
ORDER = ["MSFT","GOOGL","AMZN","NVDA","AAPL","AVGO","META","SPCX","TSLA","TSM",
         "ASML","SKHY","LLY","AMD","MU","CEG","GEV","PLTR","VRT"]
HELD, COST, FX_BUY = 55, 334.87, 3.0968
MOM_NIS = 40000
CASH_WEIGHT = 0.5

def fm(p, k):
    return re.search(rf"^{k}:\s*(.*)$", p.read_text(encoding="utf-8"), re.M).group(1).strip()

def setf(p, k, v):
    t = p.read_text(encoding="utf-8")
    p.write_text(re.sub(rf"^{k}:.*$", f"{k}: {v}", t, count=1, flags=re.M), encoding="utf-8")

def solve(P, T, budget, fixed):
    free = [t for t in ORDER if t not in fixed]
    fl = {t: int(budget * T[t] / 100 // P[t]) for t in free}
    best = None
    for bits in itertools.product((0, 1), repeat=len(free)):
        sh = {t: fl[t] + x for t, x in zip(free, bits)}
        sh.update(fixed)
        tot = sum(sh[t] * P[t] for t in ORDER)
        if tot > budget:
            continue
        c = sum(abs(sh[t] * P[t] / budget * 100 - T[t]) for t in ORDER) + CASH_WEIGHT * (budget - tot) / budget * 100
        if best is None or c < best[0]:
            best = (c, sh, tot)
    return best

def main():
    today = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    mom_actual = float(sys.argv[2]) if len(sys.argv) > 2 else None
    P = {t: float(fm(CASH / "companies" / f"{t}.md", "last_price")) for t in ORDER}
    T = {t: int(fm(CASH / "companies" / f"{t}.md", "pct")) + int(fm(CASH / "companies" / f"{t}.md", "earmark_pct")) for t in ORDER}
    fx = float(fm(CASH / "Money.md", "fx_rate_planning"))
    g = P["GOOGL"]
    idi = round(HELD * g, 2)
    mom = mom_actual if mom_actual else round(MOM_NIS / fx, 2)
    pool = round(idi + mom, 2)
    drift, sh, spent = solve(P, T, pool, {})
    keep = sh["GOOGL"]
    sold = HELD - keep
    proceeds, cost_sold = sold * g, sold * COST
    gain = proceeds - cost_sold
    nis_c, nis_p = cost_sold * FX_BUY, proceeds * fx
    nis_d = nis_p - nis_c
    m = lambda x: f"{x:,.2f}"
    sign = lambda x: "+" if x >= 0 else "−"
    rows = "\n".join(
        f"| {t} | {T[t]} | {m(P[t])} | {f'*keep {keep}*' if t == 'GOOGL' else sh[t]} | {m(sh[t]*P[t])} | {sh[t]*P[t]/pool*100:.1f} | {sh[t]*P[t]/pool*100-T[t]:+.1f} |"
        for t in ORDER)
    buys = sum(1 for t in ORDER if t != "GOOGL" and sh[t] > 0)
    zeros = [t for t in ORDER if sh[t] == 0]
    out = f"""---
type: reference
created: 2026-08-21
updated: {today}
author: jep
tags:
  - cash
---

# Transition worksheet - GOOGL to 19 positions (pooled account, whole shares)

Arithmetic implementing the locked [[allocation]] at the prices in `companies/*.md` (Yahoo, fetched {today}; USD/ILS {fx}). The plan, sizing, and timing are Idi's decisions; this sheet only converts the locked percentages into share counts. Before executing on a later day: `python dashboard/update_prices.py` then `python dashboard/transition.py`.

One pool (ruling 2026-09-09): Mom's ₪{MOM_NIS:,} already sits in Idi's ONE ZERO account, so both owners' money buys one set of positions at the shared percentages. Ownership is tracked as a stake: Mom's stake = her dollars received at conversion ÷ pool value at that moment, and every later value, dividend and gain splits by that fraction (fund-unit accounting). Whole shares only: ONE ZERO's quantity field rejects decimals (confirmed in-app 2026-09-03), so the fractional tables of 08-21 and 09-03 are superseded. Method: exhaustive search over floor or floor+1 shares per position, objective = sum of absolute drift in points + {CASH_WEIGHT} × idle cash %.

**Inputs:** Idi ${m(idi)} (= {HELD} GOOGL @ ${m(g)}) + Mom ${m(mom)} ({'exact, from the fx fill' if mom_actual else f'provisional: ₪{MOM_NIS:,} @ {fx}, unconverted'}) = **pool ${m(pool)}**, Mom's stake {mom/pool*100:.1f}%

## Step 0 - the conversion (Mom's ₪ → $)

Convert ₪{MOM_NIS:,} to dollars inside the app before any order. Log it as an `fx` transaction with the exact ₪ paid, $ received and fee; the $ received becomes Mom's stake and replaces the provisional figure above (rerun this script with it as the second argument). The table below carries ${m(pool-spent)} of slack, so a conversion fee under that leaves the share counts valid.

## Step 1 - the sale (Idi)

| | |
|---|---|
| GOOGL held | {HELD} shares |
| GOOGL kept (10% of the pool, whole) | **{keep} shares** |
| GOOGL sold | **{sold} shares** |
| Proceeds at ${m(g)} | ${m(proceeds)} (before fees) |
| Cost of sold shares (@ ${COST}) | ${m(cost_sold)} |
| Nominal USD gain | **{sign(gain)}${m(abs(gain))}** |

### Tax inputs for the accountant (data, no conclusions)

| | at purchase 2026-01-29 | at sale ({today} rate) |
|---|---|---|
| USD/ILS | {FX_BUY} | {fx} |
| Sold-shares value in ₪ | ₪{m(nis_c)} (cost) | ₪{m(nis_p)} (proceeds) |

Shekel-terms result: **{sign(nis_d)}₪{m(abs(nis_d))}** against the {sign(gain)}${m(abs(gain))} dollar result, because the dollar moved {(fx/FX_BUY-1)*100:+.1f}% against the shekel since purchase. Israeli capital-gains tax on foreign securities interacts with the currency move; whether this counts as a gain, a loss, or neither is the accountant question flagged in [[Money]]. Bring both rows.

## Step 2 - the buys (pooled, whole shares)

{buys} buys. At zero this run: {', '.join(zeros) or 'none'}. Sum of absolute drift {drift:.1f} points; cash left ${m(pool-spent)}.

| Ticker | Target % | Price $ | Shares | $ | Actual % | Drift |
|---|---|---|---|---|---|---|
{rows}
| **Σ** | **100** | | | **{m(spent)}** | **{spent/pool*100:.1f}** | |

Order type: LIMIT (ONE ZERO offers LIMIT, STOP LIMIT, and MARKET when open). Sell limit a touch under the bid, buy limits about 0.3% over the ask, so fills are immediate with a cap. Regular session 16:30 to 23:00 Israel time. Fees reduce what is buyable; log every real fill in `transactions/` with its exact price and fee, then the Drift view shows reality against this sheet.

## Logging fills: Cash Console

`dashboard/Cash-Console.html` is the execution console (offline, one file, phone or PC). Open it, tap a plan step, type the fill price and fee, save. It tracks cash in both currencies, Mom's stake, drift against the pool as each fill lands, slippage against this sheet, open lots in shekel terms, and a query lab over the whole dataset. Data stays in that browser; the Export tab produces vault transaction files for jep and a JSON backup. Add `?demo` to the URL to see it fully executed with sample fills. Rebuild after a price refresh: `python dashboard/update_prices.py && python dashboard/transition.py && python dashboard/console.py`.

## Execution checklist

- [x] Fractional shares in ONE ZERO: no (quantity field rejects decimals, 2026-09-03)
- [ ] Fee per trade / package price: read it off the order confirmation step, log it with the first fill
- [~] W-8BEN: banker asked 2026-09-09, no answer yet; dividends were received before. Not a gate.
- [ ] Accountant questions sent: (1) NIS-terms loss vs USD-terms gain on the GOOGL sale (table above); (2) Mom's money invested inside Idi's account: how gains and tax attribute between them
- [ ] Convert ₪{MOM_NIS:,} → $ in the app → log the `fx` transaction with exact rate and fee, put the $ received in `total_usd` in [[Mom]]
- [ ] Sell {sold} GOOGL → log the `sell` transaction
- [ ] {buys} buys per the Step 2 table → log each `buy`
- [ ] After all fills: paste the console's Export tab to jep, then `python dashboard/update_prices.py` and `python dashboard/build.py`, send Mom her page
"""
    (CASH / "transition.md").write_text(out, encoding="utf-8")
    setf(CASH / "Idi.md", "total_usd", idi)
    setf(CASH / "Mom.md", "total_usd", mom)
    mp = CASH / "Mom.md"
    mp.write_text(re.sub(r"at the 2026-\d\d-\d\d rate of ₪[\d.]+/\$", f"at the {today} rate of ₪{fx}/$",
                         mp.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"transition.md rebuilt {today}: pool ${m(pool)} (Mom {mom/pool*100:.1f}%), sell {sold} GOOGL @ ${m(g)}, {buys} buys, "
          f"spent ${m(spent)}, left ${m(pool-spent)}, drift {drift:.1f}, zeros {zeros}")
    for t in ORDER:
        print(f"  {t:5} {sh[t]:2d} @ {P[t]:>9,.2f}  {sh[t]*P[t]/pool*100:4.1f}% vs {T[t]:2d}")

if __name__ == "__main__":
    main()
