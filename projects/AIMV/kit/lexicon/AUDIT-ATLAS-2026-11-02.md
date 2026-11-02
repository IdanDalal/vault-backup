---
type: research
created: 2026-11-02
author: jep
---

# Atlas quote and receipt audit, 2026-11-02

Measured before/after counts (jep, `atlasstats.py` over `atlas/a*.json`): quotes 188 → 187 (1 removed); quotes sourced to Wikipedia or Wikiquote 84 → 21 (63 re-sourced to primary or major-outlet pages); receipts marked low 6 → 0 (raised or removed); receipts 723; all four batches pass `atlas.py check` with 0 problems.

## Method

1. jep capped every Wikipedia-only receipt at `medium` (319 receipts) before the audit: high = primary source.
2. The audit agent split the 188 quotes across five helpers (qa-a1a, qa-a1b, qa-a23, qa-a4a, qa-a4b); each checked its quotes word for word against the best anonymous source (original post, transcript, screenplay, major outlet, else Wikiquote) and confirmed, corrected or removed them, plus the 6 low receipts. Edits landed 17:45-17:55.
3. Suspects flagged before the run: Alien's Special Order 937 wording, Mass Effect Legion/Tali game attribution, Hitchhiker's Marvin book wording, Interstellar's TARS exchange.

## Gap

The per-quote table (which quotes were corrected or removed, and why) was lost: the audit agent exited before its helpers reported, so their reports reached no reader. The edits themselves are in the files. A second pass that only re-reads the quotes can rebuild the table if a specific quote is ever in doubt; until then, treat a quote as checked only if its `url` points beyond Wikipedia (166 of 187 do).
