#!/usr/bin/env python3
"""Write the 2026-09-10 execution into ../transactions/ from the ONE ZERO app's own records
(order history + order details + balance screens, read 2026-09-11). Idempotent: overwrites the same 20 files.
Fees on buys are the app's "estimated fees" ($24 each, the larger of $24 or 0.30%); confirm after settlement."""
import re
from pathlib import Path

CASH = Path(__file__).resolve().parent.parent
TX = CASH / "transactions"
DATE = "2026-09-10"
# ticker: (shares, fill price, limit typed, order time)
BUYS = {"MSFT": (7, 492.00, 492, "17:33"), "AMZN": (11, 252.22, 0, ""), "AVGO": (5, 363.80, 0, ""), "TSM": (4, 430.54, 0, ""),
        "META": (3, 657.59, 0, ""), "LLY": (1, 1127.37, 0, ""), "AAPL": (6, 320.12, 0, ""), "NVDA": (13, 218.35, 0, ""),
        "TSLA": (3, 367.69, 0, ""), "SPCX": (11, 149.88, 0, ""), "PLTR": (4, 167.88, 0, ""), "AMD": (2, 509.25, 0, ""),
        "SKHY": (6, 190.68, 0, ""), "VRT": (1, 250.41, 252, "18:05"), "GEV": (1, 936.01, 0, ""), "MU": (1, 985.48, 0, ""),
        "CEG": (3, 289.53, 0, ""), "ASML": (1, 1701.54, 0, "")}
FEE_BUY = 24.00


def write(name, fields, title, body):
    fm = "\n".join(f"{k}: {v}" for k, v in fields.items())
    (TX / f"{name}.md").write_text(f"---\n{fm}\ntags:\n  - cash-tx\n---\n\n# {title}\n\n{body}\n", encoding="utf-8")


def base(**kw):
    d = {"date": DATE, "type": "", "ticker": '""', "owner": '""', "nis_out": 0, "usd_in": 0, "fee_nis": 0, "fee_usd": 0,
         "shares": 0, "price_usd": 0, "limit_usd": 0, "fx_rate": 0, "note": '""', "created": "2026-09-11", "author": "jep"}
    d.update(kw); return d


write(f"{DATE} fx 13032usd", base(type="fx", owner='"mom"', nis_out=40000, usd_in=13031.69, fee_nis=60.01, fx_rate=3.0694,
      note='"Mom\'s conversion. App: ₪40,000 at 3.0694, fee ₪60.01 charged as a separate ₪ line; dollar account showed $13,031.69 before the sale."'),
      f"{DATE} - fx ₪40,000 → $13,031.69", "Effective ₪/$ = (40,000 + 60.01) / 13,031.69 = 3.0741. Mom's stake in the pool starts here.")

write(f"{DATE} sell GOOGL", base(type="sell", ticker='"GOOGL"', shares=46, price_usd=329.00, limit_usd=329, usd_in=15088.60, fee_usd=45.40, fx_rate=3.0694,
      note='"LIMIT 329, filled 46/46 at 329.00, order 17:17. Fee 0.30% = $45.40 (app: estimated). Net $15,088.60. Order id ends 4350."'),
      f"{DATE} - sell 46 GOOGL @ $329.00", "Keeps 9 of the original 55 (bought 2026-01-29 at $334.87). Cost of sold shares $15,404.02, USD result −$315.02 before fees; shekel terms in [[transition]].")

for t, (sh, px, lim, when) in BUYS.items():
    write(f"{DATE} buy {t}", base(type="buy", ticker=f'"{t}"', shares=sh, price_usd=px, limit_usd=lim, fee_usd=FEE_BUY, fx_rate=3.0694,
          note=f'"LIMIT order, filled {sh}/{sh} at {px:.2f}{(", limit " + str(lim)) if lim else ""}{(", " + when) if when else ""}. Fee $24 = app estimate (larger of $24 or 0.30%), pending settlement."'),
          f"{DATE} - buy {sh} {t} @ ${px:.2f}", f"Gross ${sh * px:,.2f}, with the estimated fee ${sh * px + FEE_BUY:,.2f}.")

# shares in company notes
held = {t: v[0] for t, v in BUYS.items()}; held["GOOGL"] = 9
for t, sh in held.items():
    p = CASH / "companies" / f"{t}.md"; s = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"^shares:.*$", f"shares: {sh}", s, count=1, flags=re.M), encoding="utf-8")
gross = sum(sh * px for sh, px, _, _ in BUYS.values())
print(f"wrote 20 transactions; buys gross ${gross:,.2f}, est. fees ${18 * FEE_BUY + 45.40:,.2f}; shares set on 19 company notes")
