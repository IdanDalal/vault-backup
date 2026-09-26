#!/usr/bin/env python3
"""Fetch public market data for the Cash Console into data/market.json.

Usage:  python fetch_market.py            (run by refresh.py; safe to run by hand)
Sources, all anonymous (no key, no account, no signup):
  1. Yahoo Finance chart endpoint: one year of daily closes per active ticker, plus USD/ILS (ILS=X)
  2. Frankfurter (frankfurter.dev, ECB reference rates): one year of USD/ILS daily fixes
  3. Polymarket Gamma API: the events in data/polymarket-watch.json, plus the month-end
     "close above ___" price ladder for every active ticker when Polymarket lists one
Writes: data/market.json. A ticker or source that fails keeps its previous data (merge), so one
bad night never blanks the console. Read-only on the internet; writes only data/market.json.
"""
import json, re, sys, time, urllib.parse, urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASH = HERE.parent
DATA = HERE / "data"
OUT = DATA / "market.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36",
      "Accept": "application/json,text/plain,*/*"}
YAHOO = "https://query2.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=1y"
FRANK = "https://api.frankfurter.dev/v1/{start}..?base=USD&symbols=ILS"
GAMMA = "https://gamma-api.polymarket.com/events?slug={slug}"
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]


def get_json(url, tries=3, timeout=20):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (attempt + 1))
    print(f"  FAIL {url[:90]} ({last})")
    return None


def field(text, key):
    m = re.search(rf"^{key}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None


def active_tickers():
    out = []
    for p in sorted((CASH / "companies").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        if field(t, "status") == "active" and field(t, "ticker"):
            out.append(field(t, "ticker"))
    return out


def yahoo_history(sym):
    d = get_json(YAHOO.format(sym=urllib.parse.quote(sym)))
    try:
        r = d["chart"]["result"][0]
        ts, closes = r["timestamp"], r["indicators"]["quote"][0]["close"]
        meta = r.get("meta", {})
    except (TypeError, KeyError, IndexError):
        return None
    hist = []
    for t, c in zip(ts, closes):
        if c is None:
            continue
        hist.append([datetime.fromtimestamp(t, timezone.utc).date().isoformat(), round(float(c), 4)])
    if not hist:
        return None
    return {"history": hist, "last": round(float(meta.get("regularMarketPrice") or hist[-1][1]), 4),
            "prev_close": hist[-2][1] if len(hist) > 1 else None,
            "currency": meta.get("currency", ""), "date": hist[-1][0]}


def frankfurter_history():
    start = (date.today() - timedelta(days=370)).isoformat()
    d = get_json(FRANK.format(start=start))
    if not d or "rates" not in d:
        return None
    return sorted([[k, round(float(v["ILS"]), 4)] for k, v in d["rates"].items() if "ILS" in v])


def slim_market(m):
    try:
        prices = json.loads(m.get("outcomePrices") or "[]")
        outcomes = json.loads(m.get("outcomes") or "[]")
    except ValueError:
        prices, outcomes = [], []
    yes = None
    if prices:
        i = outcomes.index("Yes") if "Yes" in outcomes else 0
        try:
            yes = round(float(prices[i]), 4)
        except (ValueError, IndexError):
            yes = None
    return {"q": m.get("question", ""), "g": m.get("groupItemTitle", "") or "", "yes": yes,
            "vol": round(float(m.get("volumeNum") or m.get("volume") or 0)), "liq": round(float(m.get("liquidityNum") or m.get("liquidity") or 0)),
            "w1": m.get("oneWeekPriceChange"), "m1": m.get("oneMonthPriceChange"), "end": (m.get("endDate") or "")[:10],
            "closed": bool(m.get("closed")), "slug": m.get("slug", "")}


def polymarket_event(slug, cap):
    d = get_json(GAMMA.format(slug=urllib.parse.quote(slug)))
    if not d:
        return None
    e = d[0]
    markets = [slim_market(m) for m in e.get("markets", [])]
    markets = [m for m in markets if m["yes"] is not None and not m["closed"]]
    if not markets:
        return None
    ladder = all(re.fullmatch(r"\$?[\d,.]+[kKmMbBtT]?", m["g"]) for m in markets) and len(markets) >= 3
    if not ladder:
        markets.sort(key=lambda m: -(m["vol"] or 0))
        markets = markets[:cap]
    return {"title": e.get("title", ""), "slug": slug, "vol": round(float(e.get("volume") or 0)), "liq": round(float(e.get("liquidity") or 0)),
            "end": (e.get("endDate") or "")[:10], "markets": markets, "ladder": ladder}


def ladder_slugs(tickers):
    today = date.today()
    out = []
    for k in (0, 1):
        m = (today.month - 1 + k) % 12
        y = today.year + (today.month - 1 + k) // 12
        out += [(tk, f"{tk.lower()}-above-in-{MONTHS[m]}-{y}", f"{MONTHS[m][:3].title()} {y}") for tk in tickers]
    return out


def main():
    DATA.mkdir(exist_ok=True)
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    tickers = active_tickers()
    prices, history = dict(old.get("prices", {})), dict(old.get("history", {}))
    failed = []
    print(f"prices: {len(tickers)} tickers + ILS=X from Yahoo")
    for sym in tickers + ["ILS=X"]:
        h = yahoo_history(sym)
        time.sleep(0.6)
        if not h:
            failed.append(sym)
            continue
        prices[sym] = {"last": h["last"], "prev_close": h["prev_close"], "date": h["date"], "currency": h["currency"]}
        history[sym] = h["history"]
    for sym in list(prices):
        if sym != "ILS=X" and sym not in tickers:
            prices.pop(sym, None); history.pop(sym, None)
    fx_hist = frankfurter_history()
    fx = dict(old.get("fx", {}))
    if fx_hist:
        fx = {"source": "frankfurter.dev (ECB reference)", "history": fx_hist, "now": fx_hist[-1][1], "date": fx_hist[-1][0]}
    else:
        failed.append("frankfurter")
    if "ILS=X" in prices:
        fx["yahoo_now"] = prices["ILS=X"]["last"]

    watch = json.loads((DATA / "polymarket-watch.json").read_text(encoding="utf-8"))
    cap = int(watch.get("max_markets_per_event") or 12)
    groups = []
    print(f"polymarket: {sum(len(g['slugs']) for g in watch['groups'])} watched events + month-end ladders for {len(tickers)} tickers")
    for g in watch["groups"]:
        evs = []
        for slug in g["slugs"]:
            e = polymarket_event(slug, cap)
            time.sleep(0.4)
            if e:
                evs.append(e)
            else:
                failed.append("pm:" + slug)
        groups.append({"name": g["name"], "emoji": g.get("emoji", ""), "events": evs})
    ladders = []
    for tk, slug, label in ladder_slugs(tickers):
        e = polymarket_event(slug, 99)
        time.sleep(0.3)
        if e and e["ladder"]:
            e["ticker"] = tk; e["month"] = label
            ladders.append(e)
    pm_old = old.get("polymarket", {})
    polymarket = {"fetched": datetime.now().strftime("%Y-%m-%d %H:%M"), "groups": groups, "ladders": ladders}
    if not any(g["events"] for g in groups) and pm_old.get("groups"):
        polymarket = pm_old; failed.append("polymarket (kept previous)")

    out = {"fetched": datetime.now().strftime("%Y-%m-%d %H:%M"), "price_date": max((p["date"] for k, p in prices.items() if k != "ILS=X"), default=""),
           "sources": {"prices": "Yahoo Finance chart endpoint, daily closes, 1y", "fx": "frankfurter.dev (ECB) + Yahoo ILS=X", "odds": "Polymarket Gamma API"},
           "failed": failed, "prices": prices, "history": history, "fx": fx, "polymarket": polymarket}
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    n_ok = len([t for t in tickers if t in prices and t not in failed])
    print(f"wrote {OUT.name}: {n_ok}/{len(tickers)} tickers, {sum(len(h) for h in history.values())} closes, fx {fx.get('now')} ({fx.get('date')}), "
          f"{sum(len(g['events']) for g in groups)} events, {len(ladders)} ladders, {OUT.stat().st_size // 1024} KB"
          + (f"; FAILED: {', '.join(failed)}" if failed else ""))
    return 0 if n_ok else 1


if __name__ == "__main__":
    sys.exit(main())
