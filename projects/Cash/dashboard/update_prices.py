#!/usr/bin/env python3
"""Refresh live prices across the Cash portfolio.

Usage:  python3 update_prices.py
Does:   1. fetches each active company's price from Yahoo Finance's public
           chart endpoint (no account, no key, no signup)
        2. rewrites `last_price:` in ../companies/<TICKER>.md
        3. recomputes `portfolio_value:` in ../Idi.md and ../Mom.md
           (sum of shares x last_price across active companies)
        4. rewrites `fx_rate_planning:` in ../Money.md with the live USD/ILS rate
        5. prints a drift summary (actual % vs target %) for anything held

Run it before looking at the Drift view, before a buy session, or before
rebuilding the dashboards (build.py). Read-only on the internet; writes only
inside projects/Cash/.
"""
import json, re, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASH = HERE.parent
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}


def quote(symbol):
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.load(r)["chart"]["result"][0]["meta"]["regularMarketPrice"]
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def get_field(text, key):
    m = re.search(rf"^{key}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None


def set_field(path, key, value):
    text = path.read_text()
    new = re.sub(rf"^{key}:.*$", f"{key}: {value}", text, count=1, flags=re.M)
    if new != text:
        path.write_text(new)
        return True
    return False


def main():
    companies = []
    for p in sorted((CASH / "companies").glob("*.md")):
        text = p.read_text()
        if get_field(text, "status") != "active":
            continue
        companies.append({
            "path": p,
            "ticker": get_field(text, "ticker"),
            "shares": float(get_field(text, "shares") or 0),
            "pct": float(get_field(text, "pct") or 0) + float(get_field(text, "earmark_pct") or 0),
        })

    failed = []
    for c in companies:
        price = quote(c["ticker"])
        time.sleep(0.7)
        if price is None:
            failed.append(c["ticker"])
            c["price"] = None
            continue
        c["price"] = price
        set_field(c["path"], "last_price", price)

    fx = quote("ILS=X")
    if fx:
        set_field(CASH / "Money.md", "fx_rate_planning", fx)

    held = [c for c in companies if c["shares"] > 0 and c["price"]]
    portfolio_value = round(sum(c["shares"] * c["price"] for c in held), 2)
    for name in ("Idi", "Mom"):
        set_field(CASH / f"{name}.md", "portfolio_value", portfolio_value if name == "Idi" else 0)

    print(f"updated {len(companies) - len(failed)}/{len(companies)} prices"
          + (f" (FAILED: {', '.join(failed)})" if failed else ""))
    if fx:
        print(f"USD/ILS planning rate -> {fx}")
    print(f"Idi portfolio_value -> ${portfolio_value:,.2f}")
    for c in held:
        actual = c["shares"] * c["price"] / portfolio_value * 100
        print(f"  {c['ticker']}: {c['shares']:g} sh x ${c['price']:,.2f} = "
              f"${c['shares']*c['price']:,.2f}  actual {actual:.1f}% vs target {c['pct']:g}%")


if __name__ == "__main__":
    main()
