---
type: literature
created: 2026-11-11
author: jep
source: https://www.reddit.com/r/productivity/comments/1aha52f/the_eisenhower_matrix_sounds_interesting_but_what/
by: u/OneTalos (comment), thread by u/SirToxe
medium: reddit thread
read_via: Arctic Shift archive (reddit.com and the Wayback Machine refuse automated fetches); Idi's own saved copy from 2026-01-28 in the laptop archive
evidence: one user's setup in the TickTick app, comment score 11
tags:
  - literature
---

# OneTalos - the Eisenhower matrix for one person

## The thread

The poster works alone and asks what to do with "urgent, not important" when nobody exists to delegate to.

## OneTalos's answer (verbatim quadrants)

- "Q1: Tasks that are due today"
- "Q2: Chronological list of tasks with due dates in the future (quick glance of what's coming up"
- "Q3: Tasks without a due date, but are still important (this gets the most activity for me)"
- "Q4: Tasks without a due date that aren't urgent"
- Layout: "the left side is all items with a due date (typically recurring tasks), while the right is more one-off tasks."
- Routine: "I get through my tasks that are due today (Q1), then pivot to either getting ahead on tomorrow (Q2) or other high priority items (Q3)." Q4 rarely gets done, and he accepts that.

Other voices in the thread: EdwardJMunson (score 20) calls the matrix mostly an illusion that makes you name the tasks you must do; CaptainRhetorica (score 9) has too many tasks to place and never made it work.

## Two "modified Eisenhower" versions exist in Idi's history

| Version | Axes | Status |
|---|---|---|
| OneTalos | has a due date / has none, crossed with today-or-high / later-or-low | Encoded in April (ADR-002) as `due` + `priority: high\|low`. No view ever shipped. |
| Idi's own, 2026-01-04 | "y-axis: valuable/useful/functional/beneficial, x-axis: hard/long/demanding/effortful" | Restated 01-28 as "Not yet designed". Never built. |

Receipts: `research/env-history.md` section 3.

## Use in the workshop

- The vault holds 2 notes with a `due:` date, both dead. OneTalos's left half (Q1, Q2) would be empty on every day so far.
- Idi's own axes answer the question he keeps asking, which project gets the next hour. Built as the Matrix view over the project hubs: `value` crossed with `effort`.
- OneTalos's left half is kept as the Dated view. It fills the day anything gets a `due:`.
