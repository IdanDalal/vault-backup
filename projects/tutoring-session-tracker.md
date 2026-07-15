---
type: project
created: 2026-07-15
status: active
author: jep
tags:
  - tutoring
---

# Tutoring — Session Tracker (spec + template)

The private log behind [[tutoring-session-skeleton]]. One copy per student (copy the template below into `tutoring-tracker-<student>.md`). It answers three questions: *what's due for retrieval today* (feeds warm-up block 2), *which methods carry words for this kid* (the n=1 experiment), and *what goes in the parent note*. The kid never sees it — this is where no-scorekeeping is enforced, because struggles live here and nowhere else.

## Design rules (what makes ≤3 min/session real)

1. **Track cohorts, not words.** The 5–7 words introduced in one session move up the retention ladder together as one row. Word-level bookkeeping (~7 rows/session, hundreds of rows by winter) is the version of this tracker that dies by week six.
2. **Log misses only.** A clean warm-up is one checkmark on the cohort row. Only exceptions get written: a missed word drops out of its cohort into the **limbo list**.
3. **Limbo mechanics:** a limbo word is retried every session (regardless of ladder) until it hits twice in a row, then rejoins its origin cohort — which has meanwhile advanced, so the word simply got extra reps. Slight over-spacing, acceptable on purpose.
4. **Cohort advances on a mostly-clean retrieval** (≥ all-but-one hit, misses go to limbo). Next-due = today + rung interval, rounded to the first session on/after that date.
5. **Rung intervals come from the student's frequency** (see [[tutoring-session-skeleton]]): 2x/wk → next-session, 2wk, 1mo, 3mo. 1x/wk → 1wk, 1mo, 3mo. After a clean 3mo retrieval a cohort is **solid**: unscheduled, recycled naturally in stories and games, audited by the ~3-month re-run of [[tutoring-universal-baseline]].
6. **Baseline inventory = cohort S0.** Words the student already owned at first contact (the UAB scoring sheet's inventory) enter at the 1mo rung — owned, verified lightly.
7. **The parent-note teach-prompt is scheduled retrieval in disguise.** Pick it from the *newest* cohort — for 1x/week students that lands a retrieval event exactly in the seven-day hole the ladder can't reach.

## Pre-session minute

Open the tracker, read two things: cohort rows whose *next due* ≤ today, plus the whole limbo list. That's the warm-up's guest list. (Block 2 game shapes: hide-and-seek the flashcards, Simon Says with due words, "teach me again — I forgot".)

## Post-session three minutes

Tick/advance the due cohorts, move misses to limbo, add the new cohort row, fill one session-log entry, send the parent note straight from it.

---

## TEMPLATE (copy below this line per student)

```markdown
---
type: project
created: <date>
status: active
author: jep
tags: [tutoring]
student: <name, age>
frequency: 1x | 2x per week
---

# Tracker — <Student>

Running total: **N words** (sum of cohort sizes; the parent-note ledger number)

## Cohort ledger
Rungs: new → next-session → 2wk → 1mo → 3mo → solid   (1x/wk: new → 1wk → 1mo → 3mo → solid)

| Cohort | Introduced | Words (+wow) | Method | Rung | Next due | Clean checks |
| ------ | ---------- | ------------ | ------ | ---- | -------- | ------------ |
| S0 | <baseline date> | <owned inventory from UAB> | (pre-owned) | 1mo | <date> | |
| S1 | | | | new | next session | |

## Limbo (retry every session; 2 consecutive hits → rejoin origin cohort)
- <word> (S_, missed <date> at <rung>) — hits: ☐☐

## Session log
### S1 — YYYY-MM-DD (45 min)
- **Due today:** S0 @ 1mo → clean / misses: …
- **New cohort:** S1 words above; method: TPR | story | game | song
- **Unprompted production (story slot):** …
- **Grid vs kid** (what actually happened): …
- **Win → parent note:** 🌟 …  🆕 running total …  🎁 teach-prompt from S1: …
- **Next session:** due cohorts …, limbo …, teaching idea …

## Method scoreboard (update ~monthly, from cohort rows + limbo origins)
| Method | Cohorts carried | Limbo rate | Verdict |
| ------ | --------------- | ---------- | ------- |
```

---

## What this feeds

- **Warm-up (block 2):** the pre-session minute *is* the query "what's due."
- **n=1 experiments:** each cohort row carries its method; limbo entries carry their origin — a method whose cohorts keep leaking words into limbo loses; check the scoreboard monthly, teach more through what wins.
- **Parent notes:** the 🌟/🆕/🎁 line in each session entry is the note, pre-written — copy, translate, send. Running total is always current at the top.
- **Option B transition:** when the running total crosses ~100–150, the skeleton's story-spine transition is due.
- **LG/H, privately:** words at rung ≥ 2wk per hour taught — never shown to kid or parents as a number; the parents get the can-do ledger instead.
