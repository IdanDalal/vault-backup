---
type: research
created: 2026-09-13
author: Agent web-agents
project: daily-note-system
---

# Web research: AI-written daily notes, scheduling, rollover guardrails

Scope: 12 pages fetched (2 blocked: Medium 403, PMC captcha), 16 searches. Grades: docs / study / practitioner / vendor / anecdote. Confidence per line. Date: 2026-09-13.

## Q1. AI daily briefings, PAI / Kai / TELOS

- Miessler PAI Dec-2025: TELOS = "Life goals and project tracking" skill; SessionStart hook step 1 "Load CORE context (identity, principles, contacts)"; Skills pre-loaded into system prompt at startup. No file-level TELOS spec published on that page. Source: danielmiessler.com/blog/personal-ai-infrastructure-december-2025. Grade: practitioner. Confidence: high.
- Miessler daily brief = intel pipeline, his words: "Parse all of what they're saying, Turn that into a daily Intel report for myself, Parse the daily ones and turn into a weekly one, Turn that into a monthly one". Sourcing = external feeds (news, people he follows), never his own task state. No format, length, or delivery spec published. Same URL. Grade: practitioner. Confidence: high.
- PAI 5.0 (2026): TELOS at `USER/TELOS/` holds "Mission, goals, beliefs, challenges, wisdom / Narratives, problems, strategies, models"; "Read at every session start"; "Frame every recommendation". Memory tiers: WORK (active project state), LEARNING (what worked), KNOWLEDGE (typed graph). "Ideal State Criteria (ISC) verifiable with single tool probes" = his verify-against-intent gate. No daily-plan feature described, no pruning mechanism described. Source: danielmiessler.com/blog/announcing-pai-5-life-operating-system. Grade: practitioner. Confidence: high.
- Staleness in PAI is handled by hand-editing: "When you discover a better way to do something, update the Skill files once". No automated de-duplication. Same Dec-2025 URL. Grade: practitioner. Confidence: high.
- Neither Miessler post reports reading his own outputs over weeks. Absence noted, gap unfilled. Confidence: high that the pages are silent.
- Morning-brief builders (unicodeveloper, Moun R., Ball) all source from external feeds (calendar, inbox, news); one line found on longevity: "the problem with getting a decent brief from a one-off prompt is what happens on week two, and week twenty" (search snippet, Medium page itself 403). Source: medium.com/@unicodeveloper/how-i-built-an-ai-agent-that-briefs-me-like-the-president-every-morning-71ad148f673a. Grade: anecdote. Confidence: low (snippet only).
- Google Gemini "Daily Brief" (vendor, 2026): opt-in, background, pulls Gmail + Calendar, "skimmable". Source: blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/. Grade: vendor. Confidence: medium. Relevance: industry converges on skimmable + sourced-from-your-own-data, no evidence on retention.
- Claude Desktop docs name "morning briefings that pull from your calendar and inbox" as a first-class scheduled-task use case. Source: code.claude.com/docs/en/desktop-scheduled-tasks. Grade: docs. Confidence: high.

## Q2. LLM + Obsidian daily-note workflows, what broke

- classmethod (JP dev blog): two slash commands, `daily-morning.md` (calendar via Python, read yesterday's "tomorrow" section, ask user to confirm todos, create note) and `daily-evening.md` (mark `[x]`, strike missed as `~~event~~`, 6 reflection questions). Rollover = yesterday's "tomorrow" block becomes today's todo with user edits. Trigger: manual only, "Semi-automation rather than full automation (requires command execution and permission approval)". Broke: permission prompts fire even with settings.json allows. No idempotency handling. 3 weeks of manual use preceded the build. Source: dev.classmethod.jp/en/articles/automate-obsidian-daily-notes-claude-code/. Grade: practitioner. Confidence: high.
- alexjlowe: interactive journal command, quick (<2 min) and full (<10 min) modes, rotating questions per weekday to avoid monotony, git sync for mobile. Why it stuck: removes the blank page. Two weeks of use reported, nothing longer. Source: alexjlowe.substack.com/p/building-a-daily-journal-command. Grade: anecdote. Confidence: high (for what it claims).
- "Stop calling it memory" (substack): five failure modes of markdown-as-agent-memory: no querying, no relationship traversal, scale ceiling ("dumping massive amounts of text into the context window every session"), no schema enforcement (formats drift session to session), concurrent-write corruption ("Two agents can't safely read and write the same markdown file simultaneously"). Source: limitededitionjonathan.substack.com/p/stop-calling-it-memory-the-problem. Grade: practitioner. Confidence: high.
- Hallucinated connections: "The model will hallucinate connections between notes if you ask synthesis questions without constraining the output to what you've actually written"; the "do not include anything I didn't write" constraint "is not optional". Source: pixelnthings.com/connect-obsidian-to-claude-code/ (search snippet). Grade: practitioner. Confidence: medium.
- Stale context: "CLAUDE.md drift is a real problem if you write it once and never update the Active Context section, the document becomes stale noise". Same pixelnthings snippet. Grade: practitioner. Confidence: medium.
- Large vaults: Claude Code "is sampling based on recency and relevance signals", so scope with explicit paths, no vault-wide sweeps. Same snippet. Grade: practitioner. Confidence: medium.
- AI slop in a vault: author cannot later tell own thoughts from AI text, "own thoughts get diminished by AI Slop", search results fill with generated noise; advice is keep AI output out of the vault or fenced. Source: ssp.sh/brain/using-obsidian-with-ai/. Grade: practitioner. Confidence: medium.
- Concurrency risk applies here: Obsidian tab open + agent rewriting the same file; Obsidian reloads external edits but an unsaved in-editor change loses. Inference from the substack claim, no direct test found. Confidence: medium.

## Q3. Scheduling options for Claude Code (docs, verified 2026-09-13)

Comparison table, verbatim from docs (code.claude.com/docs/en/scheduled-tasks, grade docs, confidence high):

| | Cloud routine | Desktop task | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | your machine | your machine |
| Machine on | no | yes | yes |
| Open session | no | no | yes |
| Local files | no (fresh clone) | yes | yes |
| Permission prompts | none, autonomous | per task | inherits |
| Min interval | 1 h | 1 min | 1 min |

- `/loop`: session-scoped, fires only while Claude Code is running and idle, "Closing the terminal or letting the session exit stops them firing"; backgrounding the session keeps loops alive without a terminal; recurring tasks expire after 7 days; "No catch-up for missed fires"; jitter up to 30 min on recurring (pick a minute other than :00/:30); restored on `--resume`/`--continue` except self-paced loops; `loop.md` at `.claude/loop.md` or `~/.claude/loop.md` sets the default prompt. Source: code.claude.com/docs/en/scheduled-tasks. Grade: docs. Confidence: high.
- Cloud routines: "Routines are available on Pro, Max, Team, and Enterprise plans"; fresh clone of a GitHub repo each run, pushes to `claude/`-prefixed branches; no local file access; "Routines draw down subscription usage the same way interactive sessions do" plus a daily run cap; without usage credits "additional runs are rejected until the window resets"; `/schedule` needs a claude.ai login and is hidden if `ANTHROPIC_API_KEY` is set; green status "does not mean the task in your prompt succeeded". Source: code.claude.com/docs/en/routines. Grade: docs. Confidence: high. Fit for this vault: poor (write-only via branch, vault push is read-only token, Obsidian tab reads local disk).
- Desktop scheduled tasks: Windows and macOS, Desktop app 1.1.5368+; "only fires while the app is open and your computer is awake"; missed runs: "Desktop starts exactly one catch-up run for the most recently missed time and discards anything older"; "A task scheduled for 9am might run at 11pm if your computer was asleep all day. If timing matters, add guardrails to the prompt itself"; permission mode per task, "always allow" learned on first run; prompt lives at `~/.claude/scheduled-tasks/<task-name>/SKILL.md`; optional isolated worktree per run; skips logged with reason (asleep, previous run in progress). Source: code.claude.com/docs/en/desktop-scheduled-tasks. Grade: docs. Confidence: high. Caveat: requires the Desktop app, which is a separate install from the CLI in psmux; unverified whether it runs under the `jep` Standard user.
- Headless `claude -p`: one prompt in, one result out, exit; `--continue` resumes most recent session; `--allowedTools` pre-approves tools; `--output-format json` returns result + session_id + cost; `--max-turns`. Source: code.claude.com/docs/en/headless (snippet, page not fetched). Grade: docs. Confidence: medium. Windows Task Scheduler launching `claude -p` = plain OS cron; billing = same plan usage as interactive; failure modes: OAuth token expiry, permission stalls (use `--allowedTools` or a settings allowlist), no session context unless `--continue`. Confidence: medium (assembled from wmedia.es and search snippets).
- wmedia.es comparison: cron + `claude -p` "reserved for rare cases where none of the three native options fits"; Cloud "doesn't see your uncommitted changes". Source: wmedia.es/en/tips/claude-code-schedule-vs-loop-vs-cron. Grade: practitioner. Confidence: high.
- SessionStart hook: fires on `startup|resume|clear|compact|fork` (matcher); plain-text stdout becomes context Claude sees; default timeout 30 s for SessionStart; MCP-tool hooks skipped at SessionStart. Fires in `-p` runs too (fetch summariser's inference, verify). Stop hook receives `last_assistant_message`, can block stop with exit 2. SessionEnd cannot inject context. Source: code.claude.com/docs/en/hooks. Grade: docs. Confidence: high for matcher/stdout/timeout, medium for `-p` behaviour.
- SessionStart note: since v2.1.0 hook output is injected silently, no user-visible banner. Source: claudefa.st/blog/tools/hooks/session-lifecycle-hooks (snippet). Grade: practitioner. Confidence: medium.
- `--continue` pattern: the running `hq` psmux session + `claude --continue` already is the always-on process; `/loop` inside it satisfies "requires open session" and inherits vault permissions and hooks; 7-day expiry means re-arming weekly or a `loop.md`. Inference from docs. Confidence: high.

## Q4. Design patterns humans keep following, evidence

- Implementation intentions (if-then plans naming when/where/how): Gollwitzer & Sheeran 2006, 94 tests, 8,000+ participants, d = 0.65 on goal attainment, robust to publication-bias correction. Source: sciencedirect.com/science/chapter/bookseries/abs/pii/S0065260106380021 and goalsandprogress.com/implementation-intentions-gollwitzer-how-to/. Grade: study (meta-analysis). Confidence: high on the number, medium on generalising to self-authored daily plans (lab tasks and health behaviours dominate).
- 2024 meta-analysis, 642 tests: d between .27 and .66; larger when plan has contingent if-then format, motivation high, plan rehearsed at least once. Source: researchgate.net/publication/378870694 (snippet). Grade: study. Confidence: medium. Implication: "Do X at <trigger>" beats "Do X"; a domino line should carry its cue.
- Effect drops for sustained complex behaviour (exercise d = 0.31 vs medication d = 0.79). Source: goalsandprogress.com summary of the 2006 paper. Grade: study. Confidence: medium. Implication: one-shot dominoes get the big effect; open-ended projects do not.
- "One next physical action" (GTD next action): no controlled study found; overlaps with the how-component of implementation intentions above. Grade: anecdote for GTD, study for the component. Confidence: medium.
- Receipts / verification against intent: Miessler ISC "verifiable with single tool probes"; Claude routines docs warn green status is no proof. Grade: practitioner + docs. Confidence: high that both recommend it, no outcome data.
- Propose, human accepts by index: no external evidence found beyond the classmethod morning flow (agent proposes yesterday's carry-over, user confirms). Grade: practitioner. Confidence: low as a general finding.
- Deltas only / tiered reporting: uxtigers (Nielsen) "Tiered notifications interrupt only for true blocks, digest the milestones, and archive the rest"; "resumption summary rebuilds context: what you asked, what I decided, what it cost, what I need from you". Source: uxtigers.com/post/progressive-disclosure. Grade: practitioner (UX authority, no study). Confidence: medium.
- Repetition kills response: clinical decision support, reminder acceptance dropped 30% per extra reminder per encounter and 10% per five-point rise in share of repeated reminders. Source: ncbi.nlm.nih.gov/pmc/articles/PMC5387195/ (snippet). Grade: study. Confidence: medium. Alert response fell ~2.7%/week, 50% to 35% over 36 weeks (PMC10677116 snippet). Grade: study. Confidence: medium. Both from medicine, transfer is analogical.
- Progressive disclosure for agents: load only what the step needs. Sources: mindstudio.ai, ardalis.com/optimizing-ai-agents-with-progressive-disclosure/. Grade: practitioner. Confidence: high that it is standard advice.

## Q5. Rewrite-step guardrails

- Detect "done": explicit checkbox toggled by the human is the only signal with zero inference; classmethod's evening flow asks the user per item. Inferring done from chat history reproduces the "agent claims things happened" failure. Git receipts (commit touching the named path since the note was written) are the one machine-checkable proxy and match Miessler's single-probe ISC. Grade: practitioner + inference. Confidence: high for the ordering, no study.
- Anti-hallucination constraint (pixelnthings): output nothing the human did not write or that a probe did not return. Confidence: medium.
- Idempotency: agents retry 15 to 30% of tool calls; appends duplicate on retry; fix = read whole file, modify in memory, write whole file, so the end state is "file contains X" (fast.io/resources/ai-agent-idempotent-operations/, agentpatterns.ai). Render the whole note from template each run (devopsaitoolkit.com/blog/writing-idempotent-automation-scripts/). Key each line with a stable id so "find and update, never duplicate" works. Grade: practitioner. Confidence: high.
- When to run: Desktop docs make the case against a fixed clock on a sleeping machine (run may land at 23:00); `/loop` has no catch-up; first-session-of-day is what SessionStart `startup|resume` matcher gives for free. Manual trigger (a slash command) is what both Obsidian practitioners actually shipped. Grade: docs + practitioner. Confidence: high.
- Skipped day: Desktop runs one catch-up for the latest missed slot and drops older ones; copy that rule: on rollover, process every unrolled note in date order but write only one "Today". No source handles multi-day gaps for notes; inference. Confidence: medium.
- Concurrency: one writer per file; Obsidian open tab plus agent write is the two-writer case the substack warns about. Confidence: medium.

## Q6. Anti-patterns

- Autonomy threat: "resistance to AI often reflects perceived autonomy threats rather than dissatisfaction with performance or accuracy"; mismatched recommendations produce psychological reactance; aligned ones "feel right". Source: tandfonline.com/doi/full/10.1080/10447318.2025.2587927 and researchgate.net/publication/390341814. Grade: study (consumer + reactance theory). Confidence: medium. Implication: second-person orders sourced from his own TELOS and his own queue read as aligned; orders invented by the agent read as threats.
- Digest fatigue: see Q4 clinical numbers; push open rates down 31% since 2020 (clean.email, vendor stat). Grade: vendor. Confidence: low.
- Memory files grow unbounded: "Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding" (arXiv 2608.11095): agentic prompts grow +226% over lifetime, +4.9 net instructions per commit, deletion unsafe once rationale is lost; rationale comments cut excess 99.3%. Source: arxiv.org/html/2608.11095v1. Grade: study (preprint). Confidence: medium. Implication: the rolling note must be fixed-size with yesterday archived, never accreted.
- MEMORY.md only first 200 lines auto-load (israynotarray.com, snippet). Grade: practitioner. Confidence: medium.
- AI slop in vault (ssp.sh): provenance loss, search noise. Grade: practitioner. Confidence: medium. Mitigation: `author: jep` frontmatter plus one file, never spread.
- Over-automation: both shipped Obsidian workflows stayed semi-automatic on purpose (permission prompts, user confirms carry-over). Grade: practitioner. Confidence: high.
- Schema drift: same fact formatted differently each session (substack). Mitigation: fixed template rendered each run. Confidence: high.
- Green-status trap: routine ran, task failed silently (routines docs). Confidence: high.

## Recommended mechanics

1. Trigger = SessionStart hook (`startup|resume`) in the `hq` session plus a manual slash command; skip clock-time cron on this machine (sleep, no catch-up, 23:00 runs).
2. Hook script is plain (PowerShell or Python): it checks "is today's note present", prints the rollover instruction as context; the model writes the note in the first turn. Keeps the hook under the 30 s limit.
3. Render the whole daily note from a template every run; never append. Idempotent by construction.
4. Stable ids per domino (`d1`, `d2`, `d3`) and a fixed block layout: Today / Journal / Carried. Find-and-update by id.
5. Done detection order: his checkbox `[x]` > git receipt (commit touching the named path after note time) > nothing. Chat inference never sets done; it may propose "looks done, confirm".
6. Each domino line = cue + action + done-state + cost: "After the K/D lesson, render D1 portrait v2 (done: file at projects/decadents/, cost ~40 min)". If-then format per Gollwitzer.
7. Cap 3 dominoes, source order per intent.md tie-break; rewrite yesterday's undone as carried with a counter (`carried x2`), never restated fresh.
8. Journal lines third person, one per confirmed done, with receipt path. Unconfirmed items get "unverified" in the line.
9. Multi-day gap: roll every unrolled day in order, write one Today, note "N days skipped" once.
10. Fixed size: the note never exceeds ~25 lines; yesterday's file is the archive, MEMORY.md and intent-log.md take at most one line per day.
11. Re-arm any `/loop` weekly or use `loop.md`; treat routines as unusable (no local files, read-only token).
12. Weekly probe: count days he toggled a checkbox; three zero-days in a row = the note is unread, change format before adding content.

## Pitfalls to design against

1. Agent-invented tasks read as autonomy threats; only TELOS, project files, Whiteboard Dump, and his own captures may seed a domino.
2. Appending on retry duplicates lines; rendering from template prevents it.
3. Rewriting while the Obsidian tab holds unsaved edits loses his text; write when he is away, or check mtime and abort if newer than the hook's start.
4. Done inferred from chat = fabricated journal.
5. Repeating an unchanged domino verbatim trains skimming (30% drop per repeat in clinical data).
6. Note or memory accretion (+226% lifetime growth pattern).
7. Green run status without a receipt.
8. Clock-time scheduling on a machine that sleeps.
