---
total_usd: 13389.57
total_nis: 40000
portfolio_value: 0
tags:
  - cash
---

# Mom — mirrored portfolio

The mirror rule: **identical percentages, her own dollars.** This note embeds the exact same Base views as [[Idi]] — because the views read `total_usd` from the note that embeds them, setting her amount in this note's properties is the *only* difference between the two portfolios. The mirroring is structural, never a promise to keep manually.

> [!info] `total_usd` is provisional: ₪40,000 at the 2026-08-21 rate of ₪2.9874/$. Her money has not been converted yet; when the real ₪→$ conversion happens, log it in [[Money]] and replace `total_usd` with the actual $ received.

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
