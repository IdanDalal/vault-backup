---
type: reference
created: 2026-08-21
updated: 2026-09-10
author: jep
tags:
  - cash
---

# Transition worksheet - GOOGL to 19 positions (pooled account, whole shares)

Arithmetic implementing the locked [[allocation]] at the prices in `companies/*.md` (Yahoo, fetched 2026-09-10; USD/ILS 3.0165). The plan, sizing, and timing are Idi's decisions; this sheet only converts the locked percentages into share counts. Before executing on a later day: `python dashboard/update_prices.py` then `python dashboard/transition.py`.

One pool (ruling 2026-09-09): Mom's ₪40,000 already sits in Idi's ONE ZERO account, so both owners' money buys one set of positions at the shared percentages. Ownership is tracked as a stake: Mom's stake = her dollars received at conversion ÷ pool value at that moment, and every later value, dividend and gain splits by that fraction (fund-unit accounting). Whole shares only: ONE ZERO's quantity field rejects decimals (confirmed in-app 2026-09-03), so the fractional tables of 08-21 and 09-03 are superseded. Method: exhaustive search over floor or floor+1 shares per position, objective = sum of absolute drift in points + 0.5 × idle cash %.

**Inputs:** Idi $18,185.75 (= 55 GOOGL @ $330.65) + Mom $13,012.31 (exact, from the fx fill) = **pool $31,198.06**, Mom's stake 41.7%

## Step 0 - the conversion (Mom's ₪ → $)

Convert ₪40,000 to dollars inside the app before any order. Log it as an `fx` transaction with the exact ₪ paid, $ received and fee; the $ received becomes Mom's stake and replaces the provisional figure above (rerun this script with it as the second argument). The table below carries $25.17 of slack, so a conversion fee under that leaves the share counts valid.

## Step 1 - the sale (Idi)

| | |
|---|---|
| GOOGL held | 55 shares |
| GOOGL kept (10% of the pool, whole) | **9 shares** |
| GOOGL sold | **46 shares** |
| Proceeds at $330.65 | $15,209.90 (before fees) |
| Cost of sold shares (@ $334.87) | $15,404.02 |
| Nominal USD gain | **−$194.12** |

### Tax inputs for the accountant (data, no conclusions)

| | at purchase 2026-01-29 | at sale (2026-09-10 rate) |
|---|---|---|
| USD/ILS | 3.0968 | 3.0165 |
| Sold-shares value in ₪ | ₪47,703.17 (cost) | ₪45,880.66 (proceeds) |

Shekel-terms result: **−₪1,822.51** against the −$194.12 dollar result, because the dollar moved -2.6% against the shekel since purchase. Israeli capital-gains tax on foreign securities interacts with the currency move; whether this counts as a gain, a loss, or neither is the accountant question flagged in [[Money]]. Bring both rows.

## Step 2 - the buys (pooled, whole shares)

18 buys. At zero this run: none. Sum of absolute drift 6.1 points; cash left $25.17.

| Ticker | Target % | Price $ | Shares | $ | Actual % | Drift |
|---|---|---|---|---|---|---|
| MSFT | 11 | 491.65 | 7 | 3,441.55 | 11.0 | +0.0 |
| GOOGL | 10 | 330.65 | *keep 9* | 2,975.85 | 9.5 | -0.5 |
| AMZN | 9 | 252.40 | 11 | 2,776.40 | 8.9 | -0.1 |
| NVDA | 9 | 223.67 | 12 | 2,684.04 | 8.6 | -0.4 |
| AAPL | 6 | 315.34 | 6 | 1,892.04 | 6.1 | +0.1 |
| AVGO | 6 | 364.38 | 5 | 1,821.90 | 5.8 | -0.2 |
| META | 6 | 653.69 | 3 | 1,961.07 | 6.3 | +0.3 |
| SPCX | 5 | 147.55 | 11 | 1,623.05 | 5.2 | +0.2 |
| TSLA | 4 | 367.81 | 3 | 1,103.43 | 3.5 | -0.5 |
| TSM | 6 | 435.36 | 4 | 1,741.44 | 5.6 | -0.4 |
| ASML | 4 | 1,729.52 | 1 | 1,729.52 | 5.5 | +1.5 |
| SKHY | 4 | 198.63 | 6 | 1,191.78 | 3.8 | -0.2 |
| LLY | 4 | 1,124.21 | 1 | 1,124.21 | 3.6 | -0.4 |
| AMD | 3 | 521.10 | 2 | 1,042.19 | 3.3 | +0.3 |
| MU | 3 | 1,027.77 | 1 | 1,027.77 | 3.3 | +0.3 |
| CEG | 3 | 293.90 | 3 | 881.71 | 2.8 | -0.2 |
| GEV | 3 | 951.04 | 1 | 951.04 | 3.0 | +0.0 |
| PLTR | 2 | 169.53 | 4 | 678.12 | 2.2 | +0.2 |
| VRT | 2 | 262.89 | 2 | 525.78 | 1.7 | -0.3 |
| **Σ** | **100** | | | **31,172.90** | **99.9** | |

Order type: LIMIT (ONE ZERO offers LIMIT, STOP LIMIT, and MARKET when open). Sell limit a touch under the bid, buy limits about 0.3% over the ask, so fills are immediate with a cap. Regular session 16:30 to 23:00 Israel time. Fees reduce what is buyable; log every real fill in `transactions/` with its exact price and fee, then the Drift view shows reality against this sheet.

## Logging fills: Cash Console

`dashboard/Cash-Console.html` is the execution console (offline, one file, phone or PC). Open it, tap a plan step, type the fill price and fee, save. It tracks cash in both currencies, Mom's stake, drift against the pool as each fill lands, slippage against this sheet, open lots in shekel terms, and a query lab over the whole dataset. Data stays in that browser; the Export tab produces vault transaction files for jep and a JSON backup. Add `?demo` to the URL to see it fully executed with sample fills. Rebuild after a price refresh: `python dashboard/update_prices.py && python dashboard/transition.py && python dashboard/console.py`.

## Execution checklist

- [x] Fractional shares in ONE ZERO: no (quantity field rejects decimals, 2026-09-03)
- [ ] Fee per trade / package price: read it off the order confirmation step, log it with the first fill
- [~] W-8BEN: banker asked 2026-09-09, no answer yet; dividends were received before. Not a gate.
- [ ] Accountant questions sent: (1) NIS-terms loss vs USD-terms gain on the GOOGL sale (table above); (2) Mom's money invested inside Idi's account: how gains and tax attribute between them
- [ ] Convert ₪40,000 → $ in the app → log the `fx` transaction with exact rate and fee, put the $ received in `total_usd` in [[Mom]]
- [ ] Sell 46 GOOGL → log the `sell` transaction
- [ ] 18 buys per the Step 2 table → log each `buy`
- [ ] After all fills: paste the console's Export tab to jep, then `python dashboard/update_prices.py` and `python dashboard/build.py`, send Mom her page
