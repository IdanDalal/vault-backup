---
tags:
  - cash
---

# Cash — hub

High-conviction, long-term portfolio of exponential technologies. Foundation: **MAGNA MOBSTA** (Alex Wissner-Gross) — extended by knockout tournament to US-listed, profitable incumbents only. Locked **2026-07-24**: 19 positions, 66/20/14 across three tiers.

## The map

- [[allocation]] — the locked plan: tiers, percentages, earmarks, tournament casualties, decision log
- [[Idi]] — my dollars, drift tracking, IPO earmarks
- [[Mom]] — the mirrored portfolio (same %, her $) + her HTML dashboard
- [[Money]] — FX conversions, transaction ledger, tax reference
- `Cash.base` — the sheet engine: Allocation · Dollars · IPO War Room · Drift · The Bench
- `Ledger.base` — every penny: All Transactions · FX · Buys · Dividends
- `companies/` — one note per company (19 active + 6 benched), each with thesis, watch-list, and log
- `dashboard/` — the HTML presentation layer (`python3 dashboard/build.py` regenerates)

## The full allocation

![[Cash.base#Allocation]]

## The bench

Six casualties kept warm, each with a re-entry trigger — when its news matches its trigger, reopen the case:

![[Cash.base#The Bench]]

## Standing next steps

- [x] Set `total_usd` in [[Idi]] and [[Mom]] *(2026-08-21 — Mom's is provisional until her ₪→$ conversion)*
- [ ] Execute [[transition]] — the sell/buy worksheet at live prices (checklist inside)
- [ ] Log the first FX conversion in [[Money]]
- [ ] As purchases happen: update `shares` in company notes, log buys in the ledger; `python3 dashboard/update_prices.py` refreshes every `last_price` + drift automatically
- [ ] **~Sep 2026:** Anthropic IPO war-room conversation (convert GOOGL −2, AMZN −2)
- [ ] **When OpenAI's S-1 goes public:** OpenAI war-room conversation (convert MSFT −3)
- [ ] Rebuild + resend Mom's dashboard after any change
