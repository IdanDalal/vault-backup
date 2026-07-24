---
date: 2026-01-01
type: fx
ticker: ""
nis_out: 0
usd_in: 0
fee_nis: 0
fee_usd: 0
shares: 0
price_usd: 0
note: ""
tags:
  - cash-tx
---

# Transaction template

Copy this file into `transactions/`, rename it `YYYY-MM-DD type detail`
(e.g. `2026-08-02 fx 10000usd`, `2026-08-03 buy NVDA`), then fill only the
fields that apply — leave the rest at their defaults:

| type | fill in |
|---|---|
| `fx` | `nis_out` (₪ paid), `usd_in` ($ received), `fee_nis` |
| `buy` | `ticker`, `shares`, `price_usd`, `fee_usd` |
| `sell` | `ticker`, `shares`, `price_usd` (sale price), `usd_in` (net proceeds), `fee_usd` |
| `dividend` | `ticker`, `usd_in` (net received), `fee_usd` (tax withheld) |

The ledger views in [[Money]] pick the file up automatically.
