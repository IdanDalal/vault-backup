#!/usr/bin/env python3
"""Daily refresh of the Cash Console: prices into the vault notes, public market data, rebuild.

Usage:  python refresh.py          (Task Scheduler runs refresh.cmd, which calls this)
Steps:  1. update_prices.py   last_price in companies/*.md, fx in Money.md, portfolio_value in Idi.md / Mom.md
        2. fetch_market.py    data/market.json: 1y closes, USD/ILS history, Polymarket odds
        3. console.py         Cash-Console.html rebuilt with everything embedded
Each step's exit code is logged; a failing step does not stop the next one, so a stale price
still ships with fresh odds and the other way round. Log: data/refresh.log (one block per run).
"""
import subprocess, sys, time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / "data" / "refresh.log"


def run(name):
    t0 = time.time()
    p = subprocess.run([sys.executable, str(HERE / name)], capture_output=True, text=True, cwd=str(HERE), encoding="utf-8", errors="replace")
    tail = (p.stdout.strip().splitlines() or [""])[-1]
    err = (p.stderr.strip().splitlines() or [""])[-1]
    line = f"  {name:<18} exit {p.returncode} in {time.time() - t0:5.1f}s  {tail}" + (f"  | {err}" if err else "")
    print(line)
    return line, p.returncode


def main():
    (HERE / "data").mkdir(exist_ok=True)
    lines = [f"== refresh {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
    codes = []
    for name in ("update_prices.py", "fetch_market.py", "console.py"):
        line, code = run(name)
        lines.append(line); codes.append(code)
    lines.append(f"  done: {'ok' if not any(codes) else 'with failures ' + str(codes)}")
    with LOG.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    text = LOG.read_text(encoding="utf-8").splitlines()
    if len(text) > 400:
        LOG.write_text("\n".join(text[-300:]) + "\n", encoding="utf-8")
    return 1 if any(codes) else 0


if __name__ == "__main__":
    sys.exit(main())
