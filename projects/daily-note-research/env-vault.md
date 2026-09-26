---
type: research
created: 2026-09-13
author: Agent env-vault
project: daily-note-system
---

# Vault inventory for the daily-note redesign (read-only sweep, 2026-09-13)

Scope: D:\work\vault, PC clone. Whiteboard git history on this PC ends at d0aab31 (2026-08-28); later edits are uncommitted (`git status`: Whiteboard M, projects/intent.md untracked). Digests 09-03 to 09-07 exist only under `.claude/worktrees/cash-console/daily/digests/`; main's newest is 2026-09-02.

## 1. inbox/DAILY-TEMPLATE-EXAMPLES/ (6 files, all Idi's 2024-era templates)

Shared skeleton: frontmatter `Date`, `Weekday`, `Type: Daily Note` via Templater `<% tp.date.now(...) %>`; `## Journal` ("Yesterday was a <weekday> and I felt..." + "Today I feel..."); then a to-do tree. Capitalized keys, no `type/created/author`. Plugins: Templater only (community-plugins.json; no `.obsidian/plugins/` folder on this PC, so enabled by name, uninstalled here, medium confidence). No Dataview. Content is 2024 (car service dates, Death Stranding, MIRO pill).

- `Daily Note Template (MSCW).md` (121 lines). MUST / SHOULD / CAN / WON'T tiers; `<mark>` colors (orange verb, magenta time `@08:00`, red Won't); six-deep "And" chains (wake → brush → hair → face → shake). Good: verb-first imperatives, time anchors, "WON'T FORGET WHY I'M DOING ALL THIS!". Bad: 60+ static checkboxes, hygiene and identity at equal weight, mark tags unreadable in source. Salvage: tiers, verb-first, one WON'T line.
- `Daily Note Template (Chronological).md` (93 lines). Seven numbered time blocks ("8AM 1/7" to "Always & Never 7/7"), journal last. Bad: assumes a fixed schedule he does not keep ("Wake up whenever", daily/2026-04-13.md:50). Salvage: numbered blocks with a counter, journal last.
- `Daily Note Template (Chaos).md` (119 lines). Flat list, journal fill-in stems ("I played Death Stranding and..."), check-in scale 0/5 to 6/5. Salvage: journal stems as third-person rewrite targets ("I did" → "Idi did"), the check-in.
- `Daily Note Template (Balance).md` (115 lines). Chaos plus bold stems (**I went**, **I organized**). Salvage: nothing beyond Chaos.
- `Daily Note Template (Tracker).md`, `Tracking Habits Template.md` (148 lines each, byte-similar). `---` between items, `# @00:00` headings inside bullets, YouTube channels as checkbox trees. Salvage: `---` chunking only.

Pattern: the same list built six ways in 2024, each longer, none survived. All six are open self-generated obligation lists, the "duty" register parts-registry.md:117 says gets "dosed away". None has a done-state, rollover rule, or external author.

## 2. templates/daily-note.tpl.md, daily/*.md, daily/digests/

- `templates/daily-note.tpl.md`: frontmatter `type: daily, date, created, author: Idi, tags: [daily], energy, mood, sleep, exercise/meditation/reading/deep_work: false`; `## Morning Intentions` ("What will I protect today?"), `## Log` ("What actually happened?"), `## Evening Reflection` ("What reinforced my capacity to act?"), `## Tasks`. `.obsidian/daily-notes.json` points the core Daily Notes plugin at `daily/` + this template. `author: Idi` in the template makes every note created from it read-only to jep.
- `daily/`: 4 notes. 2026-04-05 blank; 2026-04-13 Captures + pasted terminal exchange ("Wake up whenever, do nothing, sleep whenever... I must begin tracking my time"); 2026-07-05 the only filled one ("My decision from yesterday to start this habit of daily notes"); 2026-07-06 blank. Habit lasted one day. Captures ever: 3. Sleep/energy never held a value (loop-review 08-30:48).
- `daily/digests/`: 44 files on main, 06-29 to 09-02, plus 09-03 to 09-07 in the worktree. Read fully: 2026-09-02 (~1,900 words), 2026-08-31, 2026-08-30-loop-review (~3,900 words), 2026-09-07.
- Section order: Today's Orders (`due:` sweep, `status: active` count), Yesterday's Numbers (null counter), a topical essay (boot timestamps, tag retention, billing scrutiny), Tutoring ("unruled, day N"), Stale Inbox top 3 of 12, Unchanged counters, Infrastructure L1 to L4, Audit.
- Why unread: (a) nulls with counters every morning: "zero hits, 47th consecutive", "18th consecutive null", "day 22"; (b) ~2,000 words against his 400-word ceiling; (c) plumbing content, nothing actionable in a minute; (d) Telegram on a laptop cron, no PC port (pc-hq-collaboration-environment.md:54,74); (e) open decisions ("one word settles it") without one ordered domino.
- Signal it carries: git-diff recovery of his deleted Whiteboard prose (08-30 §3); autocommit-timestamp proxy for daily onset (08-30:64); stale-inbox aging; "Decisions queued for one interactive session" (08-30:137-146); the zone-7 questions (08-30:154-184).
- sitrep-2026-09-03.md:14: "No daily note since daily/2026-07-06.md; zero Captures ever. The designed 15-min/day ritual has never been run by the human side." Line 45: "no digest prompt reads [telos/]; no daily template field."

## 3. .vault-config/prompts/ (verbatim) and the runner

- `morning-digest.md`: "Gather today's orders: search the vault (projects/, areas/, inbox/, daily/) for notes with `due:` frontmatter, due today, overdue (status != done), next 3 days; plus projects with status: active. Read yesterday's daily note; if its Captures hold the evening numbers (sleep hrs / energy 1–5), copy them into that note's frontmatter... Flag up to 3 inbox items untouched >7 days... Write the full digest to `daily/digests/YYYY-MM-DD.md` (type: digest, author: jep). Send a compact version (≤12 lines) to Telegram... Clinical tone. If anything is ambiguous, do nothing destructive and say so."
- `loop-review.md`: "Assemble the week's feedback packet for Idi's 30-minute Sunday sitting (SELF-MAX zones 6–7): read the last 7 daily notes and digests. Compile: (1) ordered vs happened; (2) signals; (3) his own words, 3–5 captures quoted verbatim; (4) environment reactions; (5) open items. Close with the three zone-7 questions... prefer his words over summaries of his words."
- `evening-ping.md`: "Send one short Telegram message to chat 6139758667: 'Evening ledger, three numbers: sleep last night (hrs), energy today (1 to 5), and one line: drift or win?...' Then stop; replies are handled by the capture protocol (ADR-007)." (dash in the original dropped) Retired by Idi 2026-08-16; log stopped 08-16 21:00.
- Infrastructure: laptop crontab `3 9 * * *` morning-digest, `53 21 * * *` evening-ping, `17 9 * * 0` loop-review, via `~/bin/run-agent.sh` (inbox/standing-prompts-draft.md:32-36). Runner, `claude-vault`, write-guard are NOT in the repo (pc-hq-collaboration-environment.md:40). PC side: "digest crons as PC scheduled tasks with `claude -p`" is a to-do (same file:74), never built. `due:` substrate `bases/calendar.base`; zero `due:` notes for 47 mornings (digest 09-07:14).

## 4. Rules from intent.md, emissary-maintenance.md, intent-log.md, parts-registry.md, wins-jar.md

- intent.md dominoes rule: "1 to 3 dominoes, ordered, each with a done-state and a rough cost, named before Idi has to choose"; "Three is the cap"; he "picks by index or overrules. Target: zero deliberation on his side." Location (Option A 09-08): "the top block of `Idi's Whiteboard.md`, headed 'Today'... everything under the 'Dump' heading is Idi's release valve, read by jep and never edited." Tie-break: "external signal pending (a student, Mom, Dad) > a done-state one step away > highest TELOS VVR alignment > newest." Sources: Whiteboard queue, open threads in projects/, TELOS goals, `due:` notes.
- intent.md meta-rules binding the note: 1 "Ask WHAT, never HOW"; 3 "Unverified: say so first"; 4 receipts; 7 context slot ≤2 prompts, never re-asked; 8 "Idi performs the update on any counter he sees... jep stages, Idi accepts by index"; 9 "Planning is jep's slot and happens before Idi arrives. Idi arrives to doing"; 10 inversion check.
- intent.md done-states: Digest = "deltas only; 12-line Telegram cap; nulls reported once with a counter"; Vault file = "frontmatter type, created, author: jep; reference docs are scan-able keyword lines"; Quest list = "bounded scope; acceptance criteria per item; explicit done state; pre-tested by jep."
- intent.md taste: "The minimal amount with lossless compression"; "Refuge = crafted, tested, verified lists. Duty = open self-generated obligation. Package work as quests"; the style bans; "Build the forcing function before the goal." His slots: a good week = "high agency, high output/throughput, 'Getting Rendered' frequently, income>expenses, minimal tears/crying"; done-states that matter first = "Quest list (level-designer) and Research/reading."
- intent-log.md: one row per session, H and V/D, "Diagnostic only; never a score"; counters "live in `projects/intent-log.md`, never here" (Whiteboard line 11).
- emissary-maintenance.md: criterion "it must run even if Idi does nothing today"; budget ≤15 min/day: morning "Read the daily digest. Today's orders are already written. ≤2 min", dump "~0 willpower", evening 3 numbers ≤3 min, Sunday Loop Review 30 min "The only place orders get written"; "Drain-don't-chase... The Emissary never pings uninvited"; "three dead reincarnations (Jan / April / Sovereign Nexus), same vault, opposite fuel source."
- parts-registry.md:113-127: "There is no internal Taskmaster (empty chair)"; "Open lists have no win condition... A done-state is the precondition for a W"; "jep is the studio. Deliverables... ship as crafted quest-lists: bounded scope, acceptance criteria, verification receipts, an explicit 'done' state." Line 150, Idi 09-08: current work is a "bounty", "one simple, basic, arbitrary, temporary objective"; "the Whiteboard Today block is a notice board." Line 85, the Cat on waking: every candidate answer to "what should I do?" is "fake, artificial, external, or otherwise non-motivating." Line 129: "a counter, never a curve; monotonic; the child performs the update" applied to Idi.
- wins-jar.md: "W = a self-generated list that reached its done state, with a receipt"; Built vs Received; "Transcription is below the line"; "Idi performs the update... accepts by index"; "No prizes, no targets"; "streaks, commit counts: jep's layer only, never shown as a score"; "jep sessions are never Ws."

## 5. Idi's Whiteboard.md

- Current (51 words, jep block dated 2026-09-11 18:40): `# Today (jep block; rewritten ...)`, "One domino: a fresh session for the black tactical scene. Copy everything between the two rules below into the new session as its first message, then attach `D:\work\screens\XCOM-BLACK.png`", an empty paste zone between `---` rules, "Counters live in `projects/intent-log.md`, never here.", then `# Dump (yours; jep reads, never edits)`, empty.
- Git history on this PC: first commit 3f7a52f 2026-06-10 (a 20-word vocabulary list plus an LG/H block), then 07-05, 07-13, 08-23 to 08-28 (17 autocommits). No committed version holds a Today block; the 09-08 to 09-11 rewrites are uncommitted here (branch worktree-intent-layer per memory).
- Usage 08-23 to 08-28: paste a long reply to jep, autocommit captures it, delete within 30 to 60 min. 08-24 18:30 the ~900-word S5 debrief, gone 19:00 (5fac9c2 → 27d3d25); 08-25 15:00 "figure out if I'm wasting my time, energy, and tokens again or if I can finally find something to help me create a 'Life Operating System' with Obsidian and daily notes and healthy habits and such" (e58800c); 08-27 "Nodepad!" (9160cad). Bursts of 400 to 900 words, file used as a chat box, then wiped. Since the PC became HQ it is his reply channel.

## 6. telos/ (Read tool only)

- TELOS.md Current Focus (2026-09-09): 1 Tutoring K & D; 2 Cash (IPO ~Sep/Oct); 3 Studio, D1 portrait before 2026-09-29; 4 HQ; 5 XCOM 2; 6 Curtains; 7 I4. Core Insight: "Signal-void, system requires external forcing functions"; "Empty chair: No internal taskmaster; the seat fills by recruitment (Dad, Cash, the girls' schedule, jep)."
- core/goals.md Active table: `Tutoring | girls return, words written | weekly`, `Cash | 17 buys + 1 sale executed | before the IPO`, `Studio | one D1 portrait rendered | 2026-09-29`. Goal Design Template: "What is the forcing function? Minimum viable outcome? Who will know if I don't do it?" "Common failure mode: Zero-stakes environment + no external signal = infinite foundation-building." Signal Stack row: `Whiteboard | Today block, dominoes | daily`.
- system/strategies.md: "Good strategies create forcing functions, not motivation"; PDAC (Plan, Delegate, Assess, Codify); Cult of Done "Abandon if > 1 week old with no progress", "Failure counts as done"; Proactive Agency Level 3 "Act at right moment without prompting" (jep at level 3 by ruling, T45); Red Team Sunday "One Uncomfortable Truth"; Strategy Stack "Review: morning digest (laptop) + Today block".
- system/challenges.md: baseline = "Getting out of bed: No external reason to rise", "Emotional regulation", "Maintaining hygiene"; "The 'battle' is generating signals internally that most people receive externally"; "No external forcing function → Daily prompt / tap on shoulder"; "Choice paralysis → dominoes rule".
- identity/voice.md: text, async; "1:1 feels like being a child with an adult defining reality"; draining = small talk, emotional labor, confrontation; "focus on content, not delivery"; "Definitely NOT learning by doing" (Dec 2025, older than tutoring).

## 7. Prior planning-system notes (grep: daily note, morning ritual, bullet journal, time-block, release valve, dominoes)

- `projects/sitrep-2026-09-03.md:14,45`: "Human side never ran"; TELOS never read by any prompt.
- `projects/identity-refresh-2026-09.md` T14/T16/T19/T45/T48: dominoes written into TELOS 09-08; T48 "The 'ONE thing to do next' view it asked for is the Today block."
- `inbox/standing-prompts-draft.md` (89 days stale): the three prompts + cron lines.
- `inbox/nate-b-jones-second-brain.md` (147 days, `author: Idi`): one line, "Learn about Nate B Jones' second brain engineering principles."
- `inbox/SELF-MAX/`: Self-Maximize intro + hoe_math Levels charts, source of "zones 6–7".
- `daily/2026-04-13.md:47-63`, his own spec: "step 1 must be tracking to capture current state... it must evolve into prospective allocation, the loop, and beyond"; "making plans in a calendar as a sort-of biophysical contract where my attention is committing."
- Zero hits for "bullet journal", "time-block", "morning ritual" outside the 2024 templates; `areas/` empty; `atomic-notes/` no hits.

## 8. Frontmatter conventions the note must obey

- vault CLAUDE.md: every note `type` + `created`; `author: jep` (never `author: Idi`); status enum tasks `todo | in-progress | waiting | done`, projects `active | paused | done | archived`; priority `high | low` only; dates `YYYY-MM-DD`.
- Existing: daily notes `type: daily`, digests `type: digest`, `tags: [daily]`, extra keys `date, energy, mood, sleep, exercise, meditation, reading, deep_work`.
- jep write scope: `daily/`, `projects/`, `areas/`, `bases/`, `inbox/`; vault root writable in practice (Today block rewritten 09-08 to 09-11). Bash lines naming `.obsidian/`, `atomic-notes/`, `telos`, `.vault-config` are guard-blocked (hit twice this sweep).
- A note from the template carries `author: Idi`, read-only to jep. A jep note holding his reply zone mixes authors; the Whiteboard precedent solves it with headed blocks ("jep block" / "yours; jep reads, never edits").

## Design constraints extracted

1. jep writes the note before Idi arrives; rollover is jep's (meta-rule 9).
2. 1 to 3 dominoes, ordered, each with done-state and rough cost; three is the cap; tie-break order fixed (intent.md).
3. Every domino is a bounty: "specific monster, specific reward, done when the head is delivered" (registry:150). No open obligation lines, no habit checklists (what killed the 2024 templates).
4. Morning read ≤2 min (emissary-maintenance:23): ≤400 words, scannable lines, numbered for reply by index.
5. Deltas only; a null gets one counter line or nothing; no plumbing (tags, cron, monitor) in the note.
6. Idi performs every counter update; jep stages, he accepts by index (meta-rule 8, wins-jar). Done items become W candidates with receipts, never auto-jarred.
7. No streaks, rates, or scores shown to him. Journal lines are facts with receipts ("Idi did X, path/commit").
8. His reply zone stays under its own heading; jep reads it, never edits (Whiteboard precedent, `author: Idi` rule).
9. Frontmatter `type`, `created`, `author: jep`, `date`; status enum and `YYYY-MM-DD`; new keys need a ruling before Bases depend on them.
10. Runs even if Idi does nothing today; undone dominoes roll forward with an age count; Cult of Done expiry (>1 week) is proposed, never applied silently.
11. Drain-don't-chase: no pings, no Telegram; the open tab is the only channel.
12. Domino sources in order: his Dump zone, open threads in projects/, TELOS Current Focus + goals.md Active table, then `due:` notes (empty 47 days, fallback only).
13. Style bans apply inside the note; the name is Idi.
14. Context slot: ≤2 optional prompts at the end, never re-asked (meta-rule 7).
15. The note names its own done-state ("done when one index is typed under Reply"); rollover records verified versus assumed.

## Open questions for Idi

1. Home: `Idi's Whiteboard.md` stays the permanent tab and dated `daily/` notes become the journal archive (recommended), or the dated note becomes the tab?
2. Does the sleep/energy evening ledger die with the Telegram ping, or move into the note as one optional line?
3. Rollover at midnight, or at the first jep session of the day?
4. Do undone dominoes expire after 7 days (Cult of Done) or persist until he strikes them?
5. Does a journal line ("Idi did X") need his acceptance by index before it is written, or is jep's receipt enough?
