---
type: reference
created: 2026-08-21
author: jep
tags:
  - cash
---

# Transition worksheet — GOOGL → 19 positions

Arithmetic implementing the locked [[allocation]] at live 2026-08-21 prices (Yahoo, fetched 2026-08-21; USD/ILS 2.9876). The plan, sizing, and timing are Idan's decisions; this sheet only converts the locked percentages into share counts. Rerun `dashboard/update_prices.py` and rebuild before executing if days have passed — prices drift.

**Inputs:** Idi total $18,736.85 (= 55 GOOGL @ $340.67) · Mom total $13,389.57 (provisional: ₪40,000 @ 2.9876, unconverted)

## Step 1 — the sale (Idi)

| | |
|---|---|
| GOOGL held | 55 shares |
| GOOGL kept (10% target) | **5.500 shares** |
| GOOGL sold | **49.500 shares** |
| Proceeds at $340.67 | $16,863.17 (before fees) |
| Cost of sold shares (@ $334.87) | $16,576.06 |
| Nominal USD gain | **+$287.10** |

### Tax inputs for the accountant (data, no conclusions)

| | at purchase 2026-01-29 | at sale (2026-08-21 rate) |
|---|---|---|
| USD/ILS | 3.0968 | 2.9876 |
| Sold-shares value in ₪ | ₪51,332.74 (cost) | ₪50,380.41 (proceeds) |

Shekel-terms result: **−₪952.33** despite the +$287.10 dollar gain, because the dollar weakened ~3.5% since purchase. Israeli capital-gains tax on foreign securities interacts with the currency move; whether this counts as a gain, a loss, or neither is exactly the accountant question flagged in [[Money]]. Bring both rows.

## Step 2 — the buys

Fractional shares to 3 decimals (ONE ZERO supports fractional buys, per Ynet 2026 — confirm in-app before executing; if the app rounds to 2 decimals, use its rounding and let the Drift view absorb the crumbs). GOOGL row is the *kept* position, no buy needed for Idi; every share count for Mom is a buy, after her ₪→$ conversion replaces the provisional total.

| Ticker | Target % | Price $ | Idi $ | Idi shares | Mom $ | Mom shares |
|---|---|---|---|---|---|---|
| MSFT | 11 | 481.15 | 2,061.05 | 4.284 | 1,472.85 | 3.061 |
| GOOGL | 10 | 340.67 | 1,873.68 | *keep 5.500* | 1,338.96 | 3.930 |
| AMZN | 9 | 260.11 | 1,686.32 | 6.483 | 1,205.06 | 4.633 |
| NVDA | 9 | 216.85 | 1,686.32 | 7.776 | 1,205.06 | 5.557 |
| AAPL | 6 | 311.30 | 1,124.21 | 3.611 | 803.37 | 2.581 |
| AVGO | 6 | 364.03 | 1,124.21 | 3.088 | 803.37 | 2.207 |
| META | 6 | 545.83 | 1,124.21 | 2.060 | 803.37 | 1.472 |
| SPCX | 5 | 134.00 | 936.84 | 6.991 | 669.48 | 4.996 |
| TSLA | 4 | 345.13 | 749.47 | 2.172 | 535.58 | 1.552 |
| TSM | 6 | 416.00 | 1,124.21 | 2.702 | 803.37 | 1.931 |
| ASML | 4 | 1,750.31 | 749.47 | 0.428 | 535.58 | 0.306 |
| SKHY | 4 | 163.08 | 749.47 | 4.596 | 535.58 | 3.284 |
| LLY | 4 | 1,244.40 | 749.47 | 0.602 | 535.58 | 0.430 |
| AMD | 3 | 469.45 | 562.11 | 1.197 | 401.69 | 0.856 |
| MU | 3 | 974.33 | 562.11 | 0.577 | 401.69 | 0.412 |
| CEG | 3 | 272.92 | 562.11 | 2.060 | 401.69 | 1.472 |
| GEV | 3 | 966.01 | 562.11 | 0.582 | 401.69 | 0.416 |
| PLTR | 2 | 173.96 | 374.74 | 2.154 | 267.79 | 1.539 |
| VRT | 2 | 264.63 | 374.74 | 1.416 | 267.79 | 1.012 |
| **Σ** | **100** | | **18,736.85** | | **13,389.57** | |

Fees reduce what's actually buyable; log every real fill in `transactions/` with its exact price and fee, then the Drift view shows reality against this sheet.

## Execution checklist

- [ ] Confirm in the ONE ZERO app: fractional shares available, and the fee per trade / package price
- [ ] Confirm W-8BEN status with ONE ZERO (see [[Money]] tax section)
- [ ] Accountant question sent: NIS-terms loss vs USD-terms gain on the GOOGL sale (table above)
- [ ] Idi: sell 49.500 GOOGL → log the `sell` transaction
- [ ] Idi: 18 buys per the table → log each `buy`
- [ ] Mom: ₪→$ conversion → log the `fx` transaction with exact rate and fee, update `total_usd` in [[Mom]]
- [ ] Mom: 19 buys per the recomputed table (rerun prices first)
- [ ] After all fills: `python3 dashboard/update_prices.py` then `python3 dashboard/build.py`, send Mom her page
