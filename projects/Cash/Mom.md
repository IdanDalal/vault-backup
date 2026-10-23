---
total_usd: 10285.65
total_nis: 40000
portfolio_value: 9853.59
tags:
  - cash
---

# Mom — mirrored portfolio

The mirror rule: **identical percentages, her own dollars.** This note embeds the exact same Base views as [[Idi]] — because the views read `total_usd` from the note that embeds them, setting her amount in this note's properties is the *only* difference between the two portfolios. The mirroring is structural, never a promise to keep manually.

> [!info] One pooled account since 2026-09-10. `total_usd` = her stake: $13,031.69 received for ₪40,000 at 3.0694 (fee ₪60.01 on top), logged in [[Money]]. Idi's stake in [[Idi]] is $18,374.63 (55 GOOGL valued at the $329 sale price net of the sale fee, $18,049.60, plus $325.03 he converted on 2026-09-11 to cover the trade fees). Her share of the pool = 13,031.69 ÷ (13,031.69 + 18,374.63) = 41.5%; `portfolio_value` here is the pool value times that share, written by `dashboard/update_prices.py`.

> [!info] 2026-10-21: ₪8,000 out to her. `total_usd` now counts fund units: 13,031.69 minus the 2,746.04 units her withdrawal redeemed at the 2026-10-20 pool value ($2,602.30 converted for her + $127.79 of the sale fees), = 10,285.65. Idi's units: 18,026.23 after his ₪1,000. Her share = 10,285.65 ÷ 28,311.88 = 36.33%. Records: `transactions/2026-10-21 withdraw mom.md` and `... withdraw idi.md`.

## Her dollars

![[Cash.base#Dollars]]

## The plan (percentages)

![[Cash.base#Allocation]]

---

> [!tip] Her deliverable is the HTML dashboard
> Mom doesn't read Obsidian — she gets a mobile-friendly page. Rebuild it after any change:
> ```
> python3 dashboard/build.py
> ```
> …then send her `dashboard/Cash-Mom.html` (it's fully self-contained — works offline, on any phone).
