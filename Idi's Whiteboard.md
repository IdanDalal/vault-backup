---
type: reference
created: 2026-11-11
author: jep
project: Cash
status: in-progress
---

# Mom's full exit, 2026-11-11: options, numbers, preflight

Prices: close of 2026-11-10 and thin premarket of 11-11 13:48 (Yahoo). Rates: Bank of Israel 3.161 (11-10), Yahoo mid 3.1721. Nothing here is sized for execution; share counts get re-cut from live prices before 16:30. Receipts: `catchup.md`, `market.md`, `tax-fees.md`, `positions.json`, `scenarios.py` in this folder.

## 1. Mom's numbers

| Item | Close 11-10 | Premarket 11-11 |
|---|---|---|
| Pool | $26,526.74 | $27,150.74 |
| Unit value (1.00000 on 09-10) | 0.93695 | 0.95899 |
| Mom: 10,285.65 units, 36.33% | $9,637.11 | $9,863.81 |
| In shekels at mid 3.1721 | ₪30,570 | ₪31,289 |
| In hand, ZERO track, 5 sell fees, bank rate 0.5 to 1.0% under mid | ₪29,840 to ₪29,990 | ₪30,550 to ₪30,710 |
| In hand, +ONE track (no sell fees, no conversion fee, same rate assumption) | ₪30,260 to ₪30,420 | ₪30,980 to ₪31,130 |
| Lifetime: in ₪40,000, out ₪8,000 (10-21) plus today | ₪-1,580 to ₪-2,160 | ₪-870 to ₪-1,450 |

- Confidence: stake high (file-derived units, fetched prices). Bank rate medium (October: 0.5 to 1.0% under reference). +ONE row low until the app confirms the track.
- Tax on her: ₪0 under the proposed rule (section 4).
- Her payout is fixed by unit value at the fills. Which tickers get sold changes fees and tax, and your leftover portfolio. It changes nothing else for her.

## 2. Sell lists (11-10 close; premarket variants in `scenarios.py` output)

| Option | Sells | Orders | Fees on ZERO | Realized $ | Tax est. ₪ (low / mid / high) | Your leftover drift |
|---|---|---|---|---|---|---|
| A | 5 MSFT, 9 AMZN, 4 AAPL, 11 SPCX, 1 ASML | 5 | $120 | +219 | 0 / 178 / 385 | 67 pts |
| B | 4 MSFT, 7 AMZN, 3 AAPL, 2 AVGO, 6 SPCX, 1 ASML, 1 LLY | 7 | $168 | +387 | 31 / 310 / 542 | 50 pts |
| C | 2 MSFT, 4 GOOGL, 4 AMZN, 2 AAPL, 2 AVGO, 8 SPCX, 2 TSM, 1 ASML, 1 LLY | 9 | $216 | -51 | 0 / 29 / 410 | 36 pts |
| C10 | 2 MSFT, 2 GOOGL, 4 AMZN, 3 AAPL, 2 AVGO, 6 SPCX, 2 TSM, 1 ASML, 1 AMD, 1 LLY | 10 | $240 | +92 | 0 / 119 / 437 | 30 pts |
| D | 6 GOOGL, 12 NVDA, 5 AVGO, 10 SPCX, 3 TSM, 1 ASML (losers only) | 6 | $144 | -1,401 | 0 / 0 / 0 | 68 pts |
| E | Buyout: Idi pays Mom about ₪30,500 from outside, nothing sold | 0 | $0 | 0 | 0 | 14 pts |

- Drift = sum over 19 positions of |weight minus locked target|, in points, on Idi's post-exit pool ($16,890). Today, whole pool: 14.2.
- Why drift jumps: single shares cannot be sliced. After the exit ASML (1 share) = 8.9% against 4%, LLY (1 share) = 8.5% against 4%.
- Tax low = netted against this year's realized losses, fees deductible. Mid = netted, fees not deductible. High = 25% on every gaining sale, no netting (worst-case withholding before any refund).
- Top earners whole (LLY, AAPL, MSFT, AMZN): raises $8,278, $1,360 short, tax ₪316 / 537 / 648, drift 69. Rejected.
- Recommendation: C on ZERO, C10 on +ONE, E if fundable.

## 3. Cost levers

1. Order count on ZERO: $24 per order (0.30% only above $8,000). Floor 5 orders = $120.
2. Track upgrade: +ONE reportedly gives 10 free trades a month and 0% conversion fee for ₪89 a month, prorated, effective immediately. Source: press and search snippets (Calcalist 2026-06-24, ice 2026-09-02); the bank's own tariff blocks scripted reads. Unverified whether same-day trades get the new price. ONE track (₪49): 0.1%, minimum $8.
3. One conversion, never several. Fee on ZERO: 0.15%, minimum $5. The bank's rate against reference costs more than the fee: ₪150 to ₪300 on ₪30,000.
4. Sell order within the day: losers first, winners after. The year's tax is the same either way (Regulation 9 nets gains and losses across the tax year in the account); the order decides whether cash gets withheld and refunded later.
5. Conversion day: US banks are closed today (Veterans Day). Meitav halts dollar conversions today; ONE ZERO unverified. Expect the shekel leg on 11-12 or later.

## 4. Tax rule (medium-high confidence; ONE ZERO's own mechanics unverified)

- Per lot: A = (sale $ minus cost $) × sale-day rate. B = sale $ × sale-day rate minus cost $ × purchase-day rate. Both positive: 25% × the lower. Both negative: the smaller loss counts. Mixed signs: zero. Bank of Israel representative rates. FIFO. Source: Supreme Court, Moses (2016-2017), as described by CPA Amnon Ben-Shushan (2024); Meitav worked example.
- Today: rate 3.023 on 09-10, 3.086 on 01-29, 3.161 now. The dollar rose, so gains are taxed on the dollar gain × 3.161, and a September lot down less than about 4.4% in dollars gives no deductible loss.
- Realized so far in 2026 (jep's computation from the transaction files): GOOGL 09-10 loss about ₪-952; October sells about ₪+508 before fees. Net ₪-444 without fees, ₪-1,028 with fees deducted.
- Proposed rule between Idi and Mom: she pays 5 sell fees (the floor) and the conversion, as in October. Extra orders and any tax stay with Idi, who also keeps the loss offsets. Idi's ruling.
- Buyout tax: the pool holds a net unrealized loss (-$1,584), so her share of embedded gain is negative and the strict "sale by her" reading produces no tax. Legal characterisation of an informal family pool: no source found. Accountant question, low stakes at these numbers.

## 5. Market facts that touch the list

- 10-29 to 11-10: S&P 500 -2.6%, Nasdaq 100 -5.7%, semiconductor index -13.2%. 11-05: S&P -4.36%. 11-09: S&P +2.35%.
- Premarket 11-11: Nasdaq futures +1.9%. NVDA, VRT, MU, SKHY, GEV +4.5% to +8.1%. LLY -1.2%, AAPL -0.6%.
- NVDA earnings 11-17 after close; options price about 8.3%. D sells all 12 NVDA before it; C keeps them.
- After a one-day S&P drop of 4% or more, the next 21 sessions: positive 55% against 60% for all days, spread two to three times wider (agent's arithmetic, 164 events, unreviewed).
- Losers of the past week tend to bounce over 1 to 4 weeks (Jegadeesh 1990; Lehmann 1990; averages across thousands of stocks). Winners that retail investors sold beat the losers they kept by 3.4 points over a year (Odean 1998, 10,000 accounts, 1987 to 1993).
- Anthropic IPO pricing projected near 11-18 (one forecaster, low confidence). C sells 4 GOOGL and 4 AMZN, the Anthropic earmark positions.

## 6. Preflight in the app, before 16:30

1. Dollar balance. Ledger says $169.46; last app reading in the files is $63.32 before the October sells.
2. Holdings screen against the 19 share counts in section 3 of `catchup.md`.
3. October 20 sell confirmations: any tax line (מס). Settles whether ONE ZERO withholds per sale.
4. Track (מסלול): ZERO, ONE or +ONE; the upgrade screen's exact terms for foreign trades and conversion.
5. Whether a dollar-to-shekel conversion is offered today.

## 7. Open

- Idi's pick: A, B, C, C10, D or E.
- Order sheet: written after the pick, re-cut at live prices.
- After fills: unit value at fill prices, Mom's payout, one conversion, transaction files, `Mom.md` to zero units.

