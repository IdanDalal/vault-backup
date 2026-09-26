#!/usr/bin/env python3
"""Build Cash-Console.html: the offline execution + ledger + analysis app.

Usage:  python update_prices.py && python transition.py [date] [mom_usd] && python console.py [date] [mom_usd]
Reads:  ../companies/*.md (targets, tiers, last_price), ../Money.md (fx),
        ../Mom.md (total_nis), ../transactions/*.md (seed ledger),
        transition.py's solver (the whole-share plan).
Writes: Cash-Console.html, self-contained: no CDN, works offline on a phone.
Data entered in the page lives in that browser's localStorage; the page's
Export tab hands it back as vault transaction files or JSON.
"""
import json, re, sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASH = HERE.parent
sys.path.insert(0, str(HERE))
import transition  # noqa: E402


def fm(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.index("\n---", 3)
    d = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith(" ") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith('"'):
            try:
                v = json.loads(v)
            except ValueError:
                v = v.strip('"')
        else:
            for cast in (int, float):
                try:
                    v = cast(v)
                    break
                except ValueError:
                    pass
        d[k.strip()] = v
    return d


WIKI = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def section(path, name):
    """First paragraph under '## <name>' in a company note, wikilinks unwrapped, as one plain line."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## " + re.escape(name) + r"\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return ""
    para = m.group(1).strip().split("\n\n")[0]
    para = WIKI.sub(lambda k: k.group(2) or k.group(1), para)
    return re.sub(r"\s+", " ", para.replace("**", "")).strip()


def log_tail(path, n=3):
    """Last n '## Log' bullets of a company note, newest first, as plain lines."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Log\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return []
    items = [re.sub(r"\s+", " ", i.strip().lstrip("- ").replace("**", "")) for i in re.split(r"\n(?=- )", m.group(1).strip()) if i.strip()]
    return [WIKI.sub(lambda k: k.group(2) or k.group(1), i) for i in items][-n:][::-1]


def main():
    today = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    tickers, P, T = {}, {}, {}
    bench = []
    for p in sorted((CASH / "companies").glob("*.md")):
        c = fm(p)
        tk = c["ticker"]
        if c.get("status") != "active":
            bench.append({"ticker": tk, "company": c.get("company", ""), "layer": c.get("layer", "") or "", "status": c.get("status", ""),
                          "cut": section(p, "Why it was cut"), "reentry": section(p, "Re-entry trigger"), "log": log_tail(p)})
            continue
        P[tk] = float(c.get("last_price") or 0)
        T[tk] = int(c.get("pct") or 0) + int(c.get("earmark_pct") or 0)
        tickers[tk] = {"company": c.get("company", ""), "tier": int(c.get("tier") or 0), "target": T[tk], "ref": P[tk],
                       "earmark": c.get("earmark_for", "") or "", "layer": c.get("layer", "") or "", "conviction": c.get("conviction", "") or "",
                       "shares_vault": int(c.get("shares") or 0), "thesis": section(p, "Thesis"), "watch": section(p, "Watch"), "log": log_tail(p)}
    fx = float(fm(CASH / "Money.md").get("fx_rate_planning") or 0)
    mom_nis = float(fm(CASH / "Mom.md").get("total_nis") or transition.MOM_NIS)
    g = P["GOOGL"]
    idi_value = round(transition.HELD * g, 2)
    mom_usd = float(sys.argv[2]) if len(sys.argv) > 2 else round(mom_nis / fx, 2)
    pool = round(idi_value + mom_usd, 2)
    drift, sh, spent = transition.solve(P, T, pool, {})
    keep = sh["GOOGL"]
    plan = [{"step": "fx", "nis": mom_nis, "note": "Mom's conversion"},
            {"step": "sell", "ticker": "GOOGL", "shares": transition.HELD - keep, "ref": g, "note": f"keep {keep}"}]
    for tk in transition.ORDER:
        if tk == "GOOGL" or sh[tk] <= 0:
            continue
        plan.append({"step": "buy", "ticker": tk, "shares": sh[tk], "ref": P[tk], "note": f"target {T[tk]}%"})

    seed = []
    for p in sorted((CASH / "transactions").glob("*.md")):
        if p.name.startswith("_"):
            continue
        t = fm(p)
        seed.append({"id": "seed-" + re.sub(r"[^A-Za-z0-9]+", "-", p.stem).strip("-"), "date": str(t.get("date", "")), "type": t.get("type", ""),
                     "ticker": t.get("ticker", "") or "", "owner": t.get("owner", "") or "", "shares": t.get("shares", 0) or 0,
                     "price_usd": t.get("price_usd", 0) or 0, "limit_usd": t.get("limit_usd", 0) or 0, "usd_in": t.get("usd_in", 0) or 0, "nis_out": t.get("nis_out", 0) or 0,
                     "fee_usd": t.get("fee_usd", 0) or 0, "fee_nis": t.get("fee_nis", 0) or 0, "fx_rate": t.get("fx_rate", 0) or 0,
                     "note": t.get("note", "") or "", "created": str(t.get("created", today))})

    # Executed mode: once the ledger holds the GOOGL sale, the plan becomes the record of what was done,
    # Idi's value at pooling = the 55 GOOGL valued at the sale price net of the sale fee, and the plan date is the sale date.
    sells = [t for t in seed if t["type"] == "sell" and t["ticker"] == "GOOGL"]
    executed = ""
    if sells:
        s = sells[0]; today = str(s["date"])
        idi_value = round(transition.HELD * s["price_usd"] - s["fee_usd"], 2)
        done = [t for t in seed if str(t["date"]) == today]
        plan = ([{"step": "fx", "nis": t["nis_out"], "note": "Mom's conversion"} for t in done if t["type"] == "fx"]
                + [{"step": "sell", "ticker": s["ticker"], "shares": s["shares"], "ref": s["price_usd"], "note": "executed"}]
                + [{"step": "buy", "ticker": t["ticker"], "shares": t["shares"], "ref": t["limit_usd"] or t["price_usd"], "note": "executed"}
                   for t in done if t["type"] == "buy"])
        executed = (f"Executed {today}: {len(plan)} steps from the app's records. Reference = the limit typed where known, else the fill. "
                    "Fees are the app's estimates until settlement. Log any later trade from the Ledger tab.")
    # $ start balance: what the pre-pool ledger spent without a logged conversion, so cash reads 0 before the plan date
    pre = [t for t in seed if str(t["date"]) < today]
    usd_start = round(sum(t["shares"] * t["price_usd"] + t["fee_usd"] for t in pre if t["type"] == "buy")
                      - sum(t["usd_in"] for t in pre if t["type"] in ("fx", "sell", "dividend")), 2)
    # ₪ start balance: every shekel that entered the pool through a logged conversion (fee included), else Mom's ₪ before conversion
    fx_rows = [t for t in seed if t["type"] == "fx"]
    nis_start = round(sum(t["nis_out"] + t["fee_nis"] for t in fx_rows), 2) if fx_rows else mom_nis
    data = {
        "built": datetime.now().strftime("%Y-%m-%d %H:%M"), "plan_date": today, "price_date": date.today().isoformat(), "plan_from": today,
        "executed": executed,
        "fx_planning": fx, "tickers": tickers, "bench": bench, "plan": plan, "seed": seed,
        "layers": sorted({t["layer"] for t in tickers.values() if t["layer"]}),
        "settings": {"idi_value_at_pooling": idi_value, "nis_start": nis_start, "usd_start": usd_start, "fx_now": fx},
        "pool": {"idi": idi_value, "mom": mom_usd, "total": pool, "spent": round(spent, 2), "drift": round(drift, 2)},
    }
    # v3: public market data (1y closes, USD/ILS history, Polymarket odds) from fetch_market.py, embedded when present
    mpath = HERE / "data" / "market.json"
    market = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else None
    if market:
        data["market"] = market
        if market.get("price_date"):
            data["price_date"] = market["price_date"]
    tpl = (HERE / "console_template.html").read_text(encoding="utf-8")
    html = tpl.replace("%%DATA%%", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace("%%FX_PLANNING%%", str(fx))
    out = HERE / "Cash-Console.html"
    out.write_text(html, encoding="utf-8")
    print(f"built {out.name}: {len(tickers)} tickers, plan {len(plan)} steps (sell {transition.HELD - keep} GOOGL, "
          f"{len(plan) - 2} buys), seed {len(seed)} tx, pool ${pool:,.2f}, "
          f"market {'fetched ' + market['fetched'] if market else 'MISSING (run fetch_market.py)'}, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
