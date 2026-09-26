---
type: proposal
created: 2026-09-13
author: jep
status: active
priority: high
project: daily-note-system
---

# Daily note system, v0 proposal (research digest)

Done-state of this file: Idi can rule on the four decisions at the bottom by index, and jep can build v0 the same day from this spec alone. Nothing built this session; this was a thinking session.

Research receipts: five agents ran in parallel for 15 minutes without a crash (the 09-06 crashes came from research output returned inline; this time each agent wrote to a file and returned under 200 words). Raw findings, every claim graded and linked: `projects/daily-note-research/` (env-vault, env-history, web-pkm, web-agents). The one citation that shapes the design most, Chi et al. 2026, was re-fetched from arXiv by jep and matches.

## 1. What the evidence says

1. **The Today block worked.** 8 rewrites in 4 days (09-08 to 09-11), 9 of 11 dominoes reached done, cross-conversation starting prompts were pasted within 3 minutes, sessions opened by index ("item #2 on the Whiteboard"). Receipt: `daily-note-research/env-history.md` §1, §3. High confidence.
2. **It died on 09-11** when it became a 2,300-word paste vehicle and the next two sessions ran in the main checkout without rewriting it. Cost estimates were dropped after v2; the 5-minute slot item was carried 4 versions. Same file, "What failed". High confidence.
3. **The Dump section got zero lines in 5 days.** You draft in the Whiteboard and paste into the terminal. The Context slot: 6 offers, 0 answers. Both are drop signals by your own rule. High confidence.
4. **Ownership is the one abandonment cause with a preregistered study.** Chi, Rietsche, Göldi, Ungar, Guntuku 2026 (arXiv 2605.12344, N=470): LLM-written goals scored higher on SMART quality (d=2.26) yet lost ownership (d=1.38) and commitment (d=1.19); two weeks later 46.6% acted on 2+ goals versus 72.8% for self-authored. Ownership mediated the whole gap; goal quality mediated nothing. Single study, no replication yet, no co-authoring condition tested. This is a direct hit on "jep writes Do X" and it reconciles with finding 1 only because every Today-block domino came from your own rulings and queue. Rule that follows: every domino cites your sentence.
5. **If-then format replicates.** Implementation intentions d=0.65 (Gollwitzer & Sheeran 2006, 94 tests); the 2024 update over 642 tests keeps a positive range (0.27 to 0.66, secondary source) with the largest effect for cue + action ("after X, at Y, do Z"). Medium confidence on the range.
6. **Controlling voice converts refuge into duty.** Self-determination meta-analysis (Ntoumanis 2020, g=0.41 autonomous motivation): non-controlling language plus a stated rationale carry the largest effects. "Must", "should", "have to" are the controlling markers. Your 2024 templates were built on MUST/SHOULD tiers. High confidence on the classification, medium on magnitude for adults.
7. **Zeigarnik does not replicate** (2025 meta-analysis, 37 studies, recall ratio 0.99). The usable parts: the urge to resume an interrupted task, and Masicampo & Baumeister 2011, where a concrete plan for an unfinished goal quiets it as well as finishing does. So an undone domino gets a next step written, never a bare carry.
8. **Third-person log lines are safe and modest.** Kross 2014, replicated by Orvell 2021; the 2023 meta-analysis rates the advantage small-to-moderate with uncertain quality. Fine for the journal; no performance claim.
9. **Rollover needs an age counter and a kill rule.** No study; practitioner consensus from Forster's Autofocus dismissal, Carroll's rewrite-or-strike, OmniFocus "sea of red" complaints, Sunsama rollover fatigue. The Obsidian rollover plugin has no counter.
10. **Repetition trains skimming.** Clinical reminder acceptance fell ~30% per repeated reminder (transfer is analogical). The 2026-09-02 digest ran ~1,900 words with "47th consecutive" nulls. Medium confidence.
11. **Scheduling, from the docs (code.claude.com, fetched 09-13):** cloud routines see a fresh GitHub clone only, no local files, so they cannot write this vault. Desktop scheduled tasks need the Desktop app open and awake and may fire a 09:00 task at 23:00. In-session `/loop` and crons fire only in an open idle session, expire after 7 days, up to 30 minutes of jitter, no catch-up. A SessionStart hook fires on startup and resume, its stdout becomes context, 30-second limit. High confidence.
12. **Your 2024 templates** (6 files, 93 to 148 lines each): the same hygiene and meal checklist built six ways, seven levels deep, identical every day, no done-state, no rollover, no external author. Salvage: verb-first lines, the single "why I am doing all this" line, tiers as ordering. Drop: mood scales, habit checkboxes, time-of-day blocks you do not keep.

## 2. v0 design

Two files, one rule each.

`daily/Today.md`: the permanent tab. jep renders the whole file from a template every morning, so a second run produces the same file (~25 lines cap). Your section at the bottom is yours; jep reads it and never edits it.

`daily/YYYY-MM-DD.md`: the archive, written at rollover from yesterday's Today. Third person, one line per domino, with receipt. Your text carried over verbatim under your heading.

Domino line = cue + action + done-state + cost + your source sentence + jep's one-clause reason. Cap 3. Slot 3 stays empty when nothing earns it (v7 precedent). No "must", "should", "have to". Sources in order: your Whiteboard, your captures and terminal words, TELOS Current Focus and goals.md Active table, open `projects/` threads, `due:` notes last (47 mornings empty).

Done detection at rollover, in order: your `[x]` > a git receipt (commit touching the named path after the note was written) > nothing. Chat inference never marks done; it may write "looks done, confirm by index". Undone: "carried x1" with a next step written. At "carried x3": forced re-decision line, kill / shrink to one step / date it, with jep's pick.

Empty day costs nothing: no mood, no streak, no counter shown, no filler. Counters stay in `intent-log.md`.

### Mock of tomorrow's file

```
---
type: daily
date: 2026-09-14
created: 2026-09-14
author: jep
---
# Monday 2026-09-14

Yesterday: Idi asked for the daily-note research; jep delivered the proposal (receipt: projects/daily-note-system-2026-09-13.md). Carried: none.

## Today
1. [ ] d1 After the first coffee, open `projects/daily-note-system-2026-09-13.md` and type four indices under Yours. Done = four rulings typed. ~10 min. Your words 09-13: "let's make it work, let's make it stick". jep's reason: v0 gets built the same day.
2. [ ] d2 Pick the D1 2020s render: 3, or a round-3 number. Done = one number typed. ~2 min. Your words 09-10 14:20: "3 is the best pick". jep's reason: the portrait is due 09-29 and the pick unblocks the print test.
3. Nothing third today.

## Yours (jep reads, never edits)

```

### Rollover output for the same day, in `daily/2026-09-14.md`

```
## Log
- Idi ruled on the daily-note proposal, A/A/A/B (receipt: Yours section, 09-14 09:41).
- d2 not done, carried x1. Next step: reply with one digit.
```

## 3. Trigger: options

| | A. hq session cron + hook catch-up | B. Windows Task Scheduler + headless claude | C. Cloud routine |
|---|---|---|---|
| Runs where | the always-on psmux `hq` session | a fresh `claude -p` process | Anthropic cloud |
| Local vault | yes | yes | no, GitHub clone only |
| Timing | 07:07 daily, up to 30 min jitter; hook writes the note if missing on first open | exact clock | exact clock |
| Billing | plan | plan | plan, daily run cap |
| Failure | 7-day expiry (jep re-arms weekly via `loop.md`); dies if hq closes | OAuth expiry, permission stalls, no session context, logs unread | cannot reach the tab |

**jep recommends A.** It runs where the context and the hooks already live, it costs nothing new, and the hook covers the miss. Say the word to overrule.

## 4. Home: options

| | A. `daily/Today.md` fixed tab + dated archive | B. dated file each day, Obsidian "open daily note on startup" | C. keep the Whiteboard Today block |
|---|---|---|---|
| Permanent tab | yes, never re-opened | one click each morning | yes |
| Your journal archive | yes, third person, dated | yes | no |
| Whiteboard | becomes wholly yours (release valve, drafts) | same | mixed authorship continues |

**jep recommends A.** It matches "permanently open tab" literally and gives the Whiteboard back to you.

## 5. Risks, named

1. Ownership erosion if jep starts inventing dominoes (finding 4). Guard: the source-sentence field is mandatory; a domino with no sentence of yours does not get written.
2. Two writers on one open file. Obsidian saves within seconds, so the window is small; jep checks the file's modification time and aborts the rewrite if it is newer than the run start.
3. Rewrite stops when a session runs outside the worktree (09-12, 09-13). Guard: the morning run is one job with one prompt, independent of any working session.
4. The note goes unread and nobody notices. Guard: weekly probe, days with a toggled checkbox or an index reply; three zero-days in a row triggers a format change before any content change.
5. Cost estimates were dropped in the old block. Guard: cost is a template field; missing cost fails the render.

## 6. Iteration plan

Week 1: v0 exactly as mocked, jep triggers the run by hand each morning from the hq session (zero automation, zero tools). Week 2: add trigger A. Week 3: first weekly probe, then your grand spec, one feature per week, each earning its place.

## 7. Rulings needed (reply under Yours or in the terminal, by index)

1. Trigger: A, B or C (section 3).
2. Home: A, B or C (section 4).
3. Rollover time: at 07:07 (A) or at your first session of the day (B). jep recommends A; planning stays before your arrival.
4. Journal line acceptance: jep writes "Idi did X" from a receipt alone (A), or only after you accept by index (B). jep recommends A with "unverified" marked plainly where no receipt exists.
