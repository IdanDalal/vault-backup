---
type: research
created: 2026-11-11
author: Agent env-history
project: workshop
---

# Planning-system autopsy and inventory (read-only sweep, 2026-11-11)

Sources: canonical vault `D:\work\vault` (branch `main`), `D:\work\laptop-archive\CORPUS-June-2026`, `D:\work\captures`. Git queries read-only. "inferred" marks anything without a direct receipt.

## 0. Three corrections to the brief

- `daily/Today.md` is frozen only in jep's block. Idi's "Yours" zone changed in 176 commits on 31 distinct days, 09-26 to 11-11 `git log main -- daily/Today.md`. He drafts prompts there, pastes them into the terminal, wipes them.
- Two different "modified Eisenhower" definitions exist: Idi's axes (Jan) and the OneTalos due-date variant (April ADR). Only the second was encoded. See section 3.
- `daily/` = 7 notes + 56 digests (63 files). Idi-authored: 4 `grep "^author: Idi" daily/`.

## 1. Timeline of attempts

**A. 2024 Idiverse daily templates (Sept to Oct 2024)**
- Built: six Templater templates (MSCW, Chronological, Chaos, Balance, Tracker, Tracking Habits), 93 to 148 lines, 60+ static checkboxes `projects/daily-note-research/env-vault.md:12-22`. Archive folders `00_Archive-01_Daily Notes` and `00_Archive-02_BuJo` exist empty in the backup `laptop-archive\CORPUS-June-2026\Vaults BACKUPS\Idiverse\00_Archive`.
- Idi's own use: template mtimes 2024-09-25 to 2024-10-16 `inbox/DAILY-TEMPLATE-EXAMPLES/`; one surviving filled note, 121 lines `NEXUS BACKUP\data\inbox\2024-10-03 Thursday.md`. About 3 weeks (inferred from mtimes). The only attempt Idi's own hand ran.
- Death: "122 lines = overwhelm", "All manual = burnout", "Unchecked boxes = guilt", "No prioritization" `NEXUS BACKUP\projects\daily-touchpoints\PLAN.md:186-195`.

**B. Sovereign Nexus (Dec 2025 to Feb 2026)**
- Built: 527-file rig, "Machinery, not thought" `_CORPUS-MAP\MAP.md:15`; daily template with sections Today (MUST) / Upcoming (SCHEDULED) / Important (SHOULD) / Someday (CAN) / Throughout / Captures / Won't / Done `NEXUS BACKUP\vault\templates\daily.md`; Slack capture append; daily-touchpoints plan 02-08 (inbox, drain, digest under 150 words; 4 of 8 blocks "NOT BUILT") `PLAN.md:67-76`.
- Use: 4 daily notes (01-28, 01-30, 01-31, 02-09) `NEXUS BACKUP\vault\daily\`. Journal stems unfilled on 01-28 and 02-09; bodies are agent session summaries; 02-09 Captures hold the same three machine summaries appended three times. No line by Idi's hand found (inferred). Plan next actions: 0 of 13 ticked.
- Death: "Fragmentation - work happened but wasn't tracked", "sessions restart instead of continue" `NEXUS BACKUP\data\handoffs\2026-01-28-meta-triage-coherence.md:37-43`; "Each death was at Step Minus One, mistaking the stack for the thing" `_CORPUS-MAP\JEP-ESSENCE.md:29`. Idi, 04-13: "That's why I haven't been working with you on anything for months" `daily/2026-04-13.md:60`.

**C. April laptop vault (ADR-002, 2026-04-05)**
- Built: folders, frontmatter schema, permissions, `templates/daily-note.tpl.md` (energy, mood, sleep, four habit booleans), Telegram capture. Six bases specified, three shipped: "Shipping six Bases against an empty vault is aspirational theater" `NEXUS BACKUP\data\decisions\ADR-006-bases-materialized-views.md:16`. Kanban, eisenhower, habits, energy bases never shipped.
- Idi's use: one day. 04-13: two captures (11:04, 15:15) plus a pasted terminal exchange `daily/2026-04-13.md:43-63`. 04-05 is the blank template with raw `<% tp.date %>` tags. Next vault commit after 04-06: 06-10 `git log main --reverse`.
- Death: no trigger of any kind; template broken at birth (Templater trigger off) `projects/workspace-cleanup/audit-vault.md:24`; his stated state: "Wake up whenever, do nothing, sleep whenever" `daily/2026-04-13.md:60`.

**D. June emissary (06-10 to 09-26)**
- Built: laptop cron morning digest (56 files, 06-29 to 09-26, five Loop Reviews), evening ping, `bases/calendar.base`, Telegram `c:` capture.
- Idi's use: one filled daily note, 07-05 ("My decision from yesterday to start this habit of daily notes." `daily/2026-07-05.md:22`); 07-06 blank. "Habit lasted one day. Captures ever: 3" `env-vault.md:27`. Evening ping killed by his order 08-16: "the evening ping must go" `projects/sitrep-2026-09-03.md:15`. "The designed 15-min/day ritual has never been run by the human side" `sitrep-2026-09-03.md:14`. Digest readership: unknown.
- jep's side: about 2,000 words per digest against a 400-word ceiling; "zero hits, 47th consecutive" `env-vault.md:30`.
- Death: (1) human inputs never arrived; (2) digest content was nulls and plumbing; (3) the laptop clone was blind to PC work: digest 09-26 reports "No file in `projects/` changed since 2026-08-30 14:50. Day 27" `daily/digests/2026-09-26.md:19` while the PC intent-log holds 46 session rows for 09-08 to 09-19; (4) producer died at the 09-26 write flip, "producer dead since 09-26" `audit-vault.md:50`.

**E. `Idi's Whiteboard.md` as scratch pad (06-10 to 09-26), unplanned**
- Idi's use: 106 commits on 26 distinct days, two of them jep's (takeover, retire) `git log main -- "Idi's Whiteboard.md"`; "paste-then-delete within 30 min; content survives only in git diffs" `sitrep-2026-09-03.md:14`. Emptied 09-26, retired by ruling R9 10-05 (commit `f6ee6cd`).

**F. Whiteboard Today block (09-08 to 09-11)**
- Built: 1 to 3 dominoes with done-states; 8 versions in 4 days. 9 of 11 dominoes done, all closed inside a terminal session. Dump zone: 0 lines in 5 days `daily-note-research/env-history.md:27-68,130`.
- Death: v8 became a 2,300-word paste vehicle; he used the file path and deleted the body; sessions on 09-12 and 09-13 never rewrote it `env-history.md:116,133`.

**G. `daily/Today.md` v0 + phone captures (09-13 to 09-19)**
- Built: skill `C:\Users\jep\.claude\skills\daily-note\SKILL.md`, fixed tab, dated archive, captures repo.
- Use: 3 renders (09-13, 09-14, 09-19), 2 archives. Checkboxes ticked by Idi: 0 (all three still `[ ]` at HEAD). Phone captures ever: 2 (09-13 test, 09-19 XCOM questions) `git -C D:\work\captures log`.
- Death: section 2.

**H. Wins jar and intent-log (side mechanisms)**: jar frozen 09-05. Intent-log is the only mechanism still running: 105 rows 09-08 to 11-10, H total 2 (09-11, 10-26), V/D 247/261 `projects/intent-log.md`. It needs nothing from Idi.

## 2. After 2026-09-19

Why the jep block stopped:
- Trigger was memory-only. 09-13 row: "Not done: SessionStart hook (settings.json guarded)". 09-19 row: "the memory-only trigger missed on 09-17; hook still pending" `projects/intent-log.md` rows 09-13, 09-19. No `SessionStart` or `daily-note` string in `C:\Users\jep\.claude\settings.json` today (grep, 0 hits).
- 59 intent-log rows after 09-19; zero mention a rollover. The 10-04 audit flagged it ("one rollover run fixes `Today.md`" `workspace-cleanup/cleanup-report-2026-10-04.md:78`); still not run.
- The dominoes went stale within hours. d1 done 09-19 11:38 (captures commit `8cc1874`, `"openBehavior": "daily"`); d2 answered same day `projects/XCOM/faction-orders-covert-actions-2026-09-19.md`; neither ticked. d3 (eight DECADEnts numbers) pending since 09-14; DECADEnts is "Frozen" in Idi's 11-11 text.
- After the phone toggle fix, zero further captures (last sync 2026-09-19 11:38).
- External signal ended: tutoring chapter closed 09-25 (memory index); PC instability 09-21. The tie-break's first source ("external signal pending") emptied (inferred).
- Sessions open on a prompt Idi already drafted in the Yours zone, so every session starts in doing mode and the rollover has no owner (inferred from the 176-commit pattern).
- Per-project handoff files took over "what next" (`projects/AIMV/kit/handoff-*.md`; 12 intent-log rows 10-15 to 11-05 mention a handoff) (inferred).

What Idi did instead (intent-log rows + file changes per ISO week `git log main --name-only`; Cash counts are the daily console refresh task, machine noise):

| Week | Work |
|---|---|
| W38 09-14..20 | DECADEnts round 4, Cash Console v3, XCOM jepFixes and config rulings (20 rows), one rollover |
| W39 09-21..27 | BSODs, tutoring closed 09-25, write flip 09-26, Cash v4, I4 verdict |
| W40 09-28..10-04 | I4 + constraints thread, workspace cleanup audit |
| W41 10-05..11 | name guard, history rewrite, repo recreate; no project work logged |
| W42 10-12..18 | AIMV "Knowledge Cutoff" starts (idea drafted in Yours 10-12), 13 rows |
| W43 10-19..25 | AIMV typography and escalation passes, local agents pilot, Cash withdrawal |
| W44 10-26..11-01 | AIMV parity, polish, release; video live 11-01; XCOM campaign setup |
| W45 11-02..08 | AIMV video 2 "Pay Attention" (332 file changes, 26 rows), XCOM Amalgamation |
| W46 11-09..11 | XCOM card audits, AIMV collab overhaul, this workshop |

Pattern: one or two projects absorb everything; his 11-11 words: "randomly choose any project an work on it (like I do every day)".

## 3. The modified Eisenhower matrix

- Source thread saved 2026-01-28: `NEXUS BACKUP\data\inbox\RedditEisenhower.txt`. OneTalos, lines 141-145: "Q1: Tasks that are due today Q2: Chronological list of tasks with due dates in the future (quick glance of what's coming up Q3: Tasks without a due date, but are still important (this gets the most activity for me) Q4: Tasks without a due date that aren't urgent"; "the left side is all items with a due date (typically recurring tasks), while the right is more one-off tasks"; "I get through my tasks that are due today (Q1), then pivot to either getting ahead on tomorrow (Q2) or other high priority items (Q3)."
- Idi's own modification, different axes: "Eisenhower matrix reddit thread y-axis: valuable/useful/functional/beneficial, x-axis: hard/long/demanding/" `NEXUS BACKUP\vault\atomic_notes\2026-01-04-prompts.md:20` (twin `_forks\NEXUS-Idiverse\Prompts.md:6`). Restated 01-28: "Y-axis: valuable/useful/functional/beneficial; X-axis: hard/long/demanding/effortful ... Based on Reddit thread they read. Not yet designed." `handoffs\2026-01-28-meta-triage-coherence.md:51-55`.
- First build, 01-28: the Nexus daily template sections (MUST = "Due today, hard deadlines, fires"; SCHEDULED = "Has future date - quick glance"; SHOULD = "High value, no deadline - do after Today is clear"; CAN = "Low priority - review weekly") `NEXUS BACKUP\vault\templates\daily.md:30-52`. OneTalos quadrants fused with his 2024 MSCW tiers.
- Second build, April: "Modified Eisenhower Matrix (OneTalos variant)": Q1 Do Now `due = today`; Q2 Coming Up `due > today`; Q3 Important, No Deadline `due empty AND priority high`; Q4 Backlog `due empty AND priority low`. "Eisenhower placement is derived, not stored" `NEXUS BACKUP\data\decisions\ADR-002-obsidian-vault-architecture.md:224-247,293`.
- Gap: Idi's value-by-effort axes were never implemented anywhere. `eisenhower.base` was never shipped `ADR-006:40`.
- Survivors in the live vault: "Priority is `high` or `low` only - these drive Eisenhower quadrant placement" `CLAUDE.md`; "Routing lens (modified Eisenhower) | inbox → calendar/kanban ... A lens, never a maintained file" `projects/emissary-maintenance.md:47`. Zero hits for "OneTalos" in `D:\work\vault` or `D:\work\PKMS`.

## 4. Machinery today

- `bases/atomic-notes.base`: folder `atomic-notes`. Matches 1 note.
- `bases/calendar.base`: any note with `due`. Matches 2, both closed-chapter tutoring tasks due 09-06 and 09-07, `status: todo`, 65 days overdue.
- `bases/projects.base`: `type == "project"`. Matches 201; 181 are AIMV working files (188 show as "Active Projects"). View is unusable as a project list.
- `bases/recent.base`: md modified in 30 days. Works.
- `templates/`: one file, `daily-note.tpl.md`, `author: Idi`, mood/sleep/habit fields. `.obsidian/daily-notes.json` points the core Daily Notes button at it (`"folder": "daily", "template": "templates/daily-note.tpl"`), so that button creates a note jep cannot edit, with raw Templater tags.
- `atomic-notes/`: `The Telescope Metaphore.md` ("The Telescope, The Sun, And The Flame"), Idi's, no frontmatter.
- `.obsidian/core-plugins.json`: 21 on, including daily-notes, templates, bases, properties, canvas, bookmarks, backlink, graph, sync; 10 off, among them slash-command, workspaces, zk-prefixer, webviewer. `community-plugins.json`: templater-obsidian, obsidian-annotator, third-mind-reader. No Kanban, Calendar, Tasks or Dataview plugin. `app.json`: line numbers on, nothing else.
- `.vault-config/prompts/`: morning-digest, loop-review, evening-ping. All dead: "cron prompts, Telegram | dead" `audit-vault.md:177`.
- PC scheduled tasks (Get-ScheduledTask): `Vault autocommit`, `Vault nightly tag`, `Cash Console refresh`, `psmux-hq`. No digest, no daily-note task.
- Skill: `C:\Users\jep\.claude\skills\daily-note\SKILL.md` (v0; triggers: stale-on-first-session, "rollover", the word "captures"). None under `D:\work\vault\.claude\skills\` except obsidian-bases and obsidian-markdown.
- `D:\work\captures\`: 2 files (`2026-09-19.md`, `README.md`); 7 commits 09-13 to 09-19; last capture 2026-09-19 11:24.
- `inbox/` 24 files, nothing routed since creation (first-commit date, age at 11-11):
  - `nate-b-jones-second-brain.md` 04-13 capture, `author: Idi`, one line, 211 d
  - `SELF-MAX/` 6 files (2 md, 4 png, 15 MB) 06-10, 154 d: Self-Maximize intro, levels charts
  - `seed-telescope-x-bowstring.md` 06-10, 154 d: jep seed for an atomic note
  - `standing-prompts-draft.md` 06-10, 154 d: cron wiring draft, dead
  - `TUTORING/` 3 video transcripts 07-05, 129 d
  - `P4C-research.md` 07-06, 128 d: Philosophy for Children research
  - `parts-registry-draft.md` 08-17, 86 d: superseded by `projects/parts-registry.md`
  - `Studio Preflight.html` 08-28, 75 d; `weekly-archive.bat` 08-29, 74 d
  - `DAILY-TEMPLATE-EXAMPLES/` 6 templates, dropped 09-13, 59 d
  - `Guide.txt`, `Transcript.txt` 09-13, 59 d: git-sync guide and video transcript for phone capture
- Vault root strays: `wins-jar.md` (older twin of `projects/wins-jar.md`), `Untitled.md`, `work/`, `Library/`, one epub.

## 5. Idi's stated requirements and complaints (verbatim)

1. 2026-01-04: "y-axis: valuable/useful/functional/beneficial, x-axis: hard/long/demanding/" `2026-01-04-prompts.md:20`
2. 04-13: "step 1 must be tracking to capture current state, but ideally the entire system's purpose is to transform current state to ideal state, so it must evolve into prospective allocation, the loop, and beyond" `daily/2026-04-13.md:53-56`
3. 04-13: "I view making plans in a calendar as a sort-of biophysical contract where my attention is committing to spend time in\on\with something\someone\whatever" `:56-58`
4. 04-13: "I want to commit to spending time on the most important things to me, and then even if I fail, I'll know where\how\why." `:61-63`
5. 08-25: "figure out if I'm wasting my time, energy, and tokens again or if I can finally find something to help me create a "Life Operating System" with Obsidian and daily notes and healthy habits and such." `daily/digests/2026-08-30-loop-review.md:84`
6. 09-08: "I know I have lots of tokens I can use, and I know I have many things to use them on, and I don't know which one(s?) to use them on now/first/most." Same message: "proposed-but-not-implemented solutions like Eisenhauer matrices, Kanban boards, daily notes, habit dashboards, bullet journals, to-do lists"; "a shared, persistent, collaborative space like Obsidian" `daily-note-research/env-history.md:33`
7. 09-08: "I typed the whole prompt/text in the whiteboard and pasted here, as always." `env-history.md:35`
8. 09-08: current work is "more like a 'bounty' than a 'quest'... one simple, basic, arbitrary, temporary objective" `projects/parts-registry.md:150`
9. 09-10: "I feel like I'm exerting A LOT of energy trying to understand what you mean and what I should do and how to respond" `env-history.md:40`
10. 09-10: "collaborate smoothly with a minimum amount of robotic actions from me like copy-pasting, clicking buttons and waiting" `env-history.md:41`
11. 09-12: "We should be as efficient as possible, as long as we ONLY remove noise and never signal." `env-history.md:48`
12. 09-14: "A batch sounds perfect. That's the throughput I was alluding to." `daily/Today.md:14`
13. 09-19: "the note's name was 2026-09-13, and I had to manually change the last digit to 9" `daily/Today.md:12`
14. 11-11: "I'm EXTREMELY inefficient by not having enough rules, ineffective by not following the ones I have, paralyzed by too many choices, overwhelmed by too many possibilities, and confused by too many files, folders, lists, urls" `git show 1744aca:daily/Today.md`
15. 11-11: "We must create a lab/workshop/kitchen to allocate resources (my time/attention/energy, your tokens, my 4090's tokens, and more) and manage all of our projects" (same commit)
16. 11-11, the wish list: "Atomic notes (we already have a foundation in the Idiverse), Daily notes, Literature notes, Habit dashboards, a Kanban board, a Calendar, an Eisenhower matrix ... We must connect the TELOS and Wins Jar to our daily process/workflow." Also: "We tried this several times before, and failed." Context he gathered: `D:\work\PKMS` (same commit)

Tension: items 5, 6, 16 ask for the tool set attempts A to D built and he never fed; items 7, 9, 10 describe what he does in practice.

## 6. Frontmatter census (522 md in `projects/` 443, `daily/` 63, `inbox/` 16; PowerShell scan of the first YAML block)

- `type`: project 201, digest 56, none (no frontmatter) 47, reference 38, research 36, key missing 29, report 21, buy 19, note 13, daily 7, sell 7, lesson-record 6, "Daily Note" 6, idea 5, project-brief 4, proposal 3, fx 3, task 2, quest 2, 11 other values at 1 or 2.
- `status`: active 258, done 8, in-progress 7, todo 7, bench 6 (off-enum), paused 4, "#child" 3 (off-enum), archived 1, waiting 1.
- `due`: 2. `priority`: 10 (all `high`). `project`: 68. `scheduled`: 0. `type: task`: 2. `session_date`: 9. `energy`/`sleep` keys: 4, all empty. Non-empty `tags`: 7.
- `author`: jep 415, Idi 5, agents 8+.
- Reading: a Kanban over `type: task` shows 2 cards; a calendar shows 2 overdue zombies; `status: active` on 258 notes carries no information.

## Causes of death, ranked (six attempts: A 2024, B Nexus, C April, D emissary, F Today block, G Today.md)

1. **Designed input slot never fed by Idi's hand** (journal fields, evening numbers, Dump zone, checkboxes): 5 of 6 (B, C, D, F, G). A is the exception and died of the opposite, all-manual burnout.
2. **No trigger that fires without someone remembering** (digest never built, cron on a machine that died, rewrite only at commit time, memory-only skill trigger): 5 of 6 (B, C, D, F, G).
3. **Output too long or mostly noise** (121-line note, triplicated captures, 2,000-word null digests, 2,300-word block): 4 of 6 (A, B, D, F).
4. **Machinery shipped ahead of content** (bases over an empty vault, `due:` empty for 47 mornings, 527-file rig): 3 of 6 (B, C, D).
5. **Open obligation lists with no done-state** (static checkbox trees, Throughout/Won't lists, habit booleans): 3 of 6 (A, B, C).
6. **System lived where the work did not** (laptop clone vs PC, Obsidian vs terminal, main checkout vs worktree sessions): 3 of 6 (D, F, G).
7. **External signal ended or was absent** (months idle before April; tutoring closed 09-25): 2 of 6 (C, G; inferred).
8. **One project absorbed everything and brought its own handoff file**: 1 of 6 (G; inferred).

What survived every attempt: a blank free-text zone in an always-open tab that he types into and wipes (Whiteboard 106 commits, then Yours 176 commits); replies by index; literal paste-ready lines; per-project handoff files; jep-only logs that ask nothing of him.
