---
fx_rate_planning: 3.30
tags:
  - cash
---

# Money — FX, ledger, taxes

The "secondary numbers" sheet: every shekel, every fee, every conversion, every day.

> [!todo] `fx_rate_planning` is a placeholder
> It's for rough planning math only (e.g. "how many ₪ do I need for $10k?"). Update it whenever you check the real rate. **Real** conversions are never estimated — they're logged as transactions with the exact rate and fee from that minute.

## How to log a transaction

1. Copy [[_template]] inside `transactions/`.
2. Rename it `YYYY-MM-DD type detail` — e.g. `2026-08-02 fx 10000usd` or `2026-08-03 buy NVDA`.
3. Fill only the fields for that type (the template has the field guide).
4. Done — every view below updates instantly.

The **Effective ₪/$** column is the number your bank hopes you never compute: `(₪ paid + fee) / $ received` — the all-in true rate of each conversion, comparable across banks, brokers, and days.

## Ledger

### Everything

![[Ledger.base#All Transactions]]

### FX conversions (₪ → $)

![[Ledger.base#FX]]

### Buys, grouped by stock

![[Ledger.base#Buys]]

### Dividends

![[Ledger.base#Dividends]]

## Taxes — the reference layer

- **Capital gains (Israel):** ~25% on *real* gains for individuals. For foreign securities the taxable gain calculation interacts with the ₪/$ exchange-rate move — the currency component matters, which is exactly why the FX ledger above records every conversion precisely.
- **US dividend withholding:** the US withholds tax on dividends from US-listed stocks (treaty rate for Israeli residents is typically 25%). File a **W-8BEN** with the broker; log the withheld amount in the transaction's `fee_usd`.
- **US estate-tax exposure:** US-situs assets (which US-listed stocks are) held by non-US persons can be subject to US estate tax above a ~$60k threshold. Directly relevant to a two-generation portfolio — worth a professional's opinion on account structure *before* the sums grow.

> [!danger] Not tax advice
> These are research notes to bring to an Israeli accountant, not conclusions. Verify every number before acting on it.
