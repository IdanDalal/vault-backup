---
type: report
created: 2026-11-11
author: jep
status: active
project: workshop
---

# Workshop report, 2026-11-11

**Unverified:** the Bases tabs (Now, Board, Matrix, Literature) have never been seen rendered. Obsidian runs under Idi's Windows account and jep cannot see its window or its version. The Board tab needs Obsidian 1.14.4 or later (changelog 2026-10-05). Everything else below was checked by `hub_check.py`; its output is in section 9.

## 1. Verdict

A small board got built, and five of the seven tools on the wish list did not, on evidence. Six earlier attempts at this system died of two causes, each hitting five of six: a slot Idi was meant to fill and never filled, and a routine with no trigger except someone remembering. The board built today has neither. It is eleven project cards plus live views over them, and the only routine it needs is one jep already performs at the end of every session (105 log rows from 09-08 to 11-10).

## 2. What killed the six attempts

Full receipts: [[projects/workshop/research/env-history|env-history]].

| Cause of death | Hit | Consequence for today's build |
|---|---|---|
| A slot Idi had to feed (journal fields, evening numbers, checkboxes, Dump zone) | 5 of 6 | No field on the board is his to fill |
| No trigger without someone remembering | 5 of 6 | Views are live Bases queries; nothing is rendered daily |
| Output too long or mostly nulls | 4 of 6 | Now shows three rows today |
| Machinery shipped before content | 3 of 6 | Eleven real cards exist before the first view opens |
| Open lists with no done-state | 3 of 6 | Every card states "Done means" |
| The system lived where the work did not | 3 of 6 | W4 below: the board can sit above the Yours zone |

What survived every attempt: a blank zone Idi types into and wipes (Whiteboard 106 commits, then the Yours zone 176 commits on 31 days since 09-26), replies by index, per-project handoff files, and logs that ask nothing of him.

## 3. Three premises in the 11-11 brief that the record contradicts

1. "Not having enough rules." The vault holds dozens. The ones that held are enforced by a machine (the write guard, the status enum) or performed by jep (the session log). The ones that lapsed lived in memory, including jep's own "render Today.md at the first session of the day", which missed for 53 days and missed again this morning. Today's build adds one rule for Idi (two active projects) and makes the rest checkable by a script.
2. "`Today.md` hasn't changed in almost 2 months." jep's block froze on 09-19. The Yours zone under it is the most-used surface in the vault.
3. The wish list (atomic notes, daily notes, literature notes, habit dashboards, Kanban, calendar, Eisenhower matrix) is the same list as 08-25 and 09-08. Attempts A to D built most of it. Two of the sources Idi supplied warn against exactly this: Odysseas's "Frankenstein's monster of a setup", and Tris's "drop off when you think the complexity is right for you".

## 4. What the sources say

Seven literature notes: `projects/workshop/sources`. None of the seven measured anything; each is one practitioner's report.

- Tris, parts I to III: one capture place, read yesterday's notes daily ("read, not do"); atomic notes with a claim for a filename and one `up` parent; one question, "What should I be doing right now?"; project notes with a state and a next action.
- Odysseas, both videos: literature notes are source-bound, atomic notes are context-free and one idea each; start bare.
- Eero Alvar: the risk in learning with an AI is skipping the struggle; the learner's raw thinking is the agent's best data.
- OneTalos: the due-date matrix. Idi's own January axes (value by effort) are a second, different design that was never built until today.

## 5. Built today

| Thing              | Where                                  | What it does                                                                                               |
| ------------------ | -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Home page          | `projects/workshop/Workshop.md`        | Now, Board, Matrix, Dated, rules, resources, jar, library on one page                                      |
| 11 project cards   | `projects/workshop/hubs/`              | One per project: status, next step, whose move, Idi's minutes, entry file, done-state, outside-vault paths |
| Board views        | `bases/workshop.base`                  | Now (active, by whose move), Board (Kanban by status, drag to freeze), Matrix (value by effort), All       |
| Library views      | `bases/library.base`                   | Literature and Atomic tables                                                                               |
| 7 literature notes | `projects/workshop/sources/`           | The six videos and the Reddit thread, timestamped, with what was checked                                   |
| Checker            | `projects/workshop/tools/hub_check.py` | Fields, link targets, the cap of two, each card's date against the session log                             |
| Evidence           | `projects/workshop/research/`          | Autopsy of six attempts; map of where files, lists and 9,454 URLs sit                                      |
| Session rule       | header of `projects/intent-log.md`     | The log row and the card get written together                                                              |
| Jar candidate      | `projects/wins-jar.md`                 | C5 staged: "Knowledge Cutoff" live 11-01                                                                   |

## 6. Left unbuilt, with the reason

| Wish | Decision | Reason |
|---|---|---|
| Atomic-note practice | Held for W1 | One atomic note in the vault; one staged candidate untouched for 154 days |
| Literature notes by Idi's hand | Held for W2 | Same slot problem; jep wrote the seven instead |
| Habit dashboard | Held for W3 | 2024 habit checkboxes burned out in three weeks; the evening ping was ended by Idi's order 08-16; four energy/sleep fields exist, all empty |
| Calendar | Existing `calendar.base` reused | Obsidian has no calendar view for Bases (roadmap: planned). The vault has 2 dated notes, both dead |
| Daily note render | Retired in favour of live views | The render is what froze |
| Session-start hook | Unbuilt | The write guard protects `settings.json` from jep |
| Local model on notes | Unbuilt | Its ruled role (10-25) is triage: it can pick candidates for W1, and the writing stays with Idi |

## 7. Rulings (reply by index; the first option in each is jep's pick)

**W1. Atomic notes: what is the practice?**

| | Option | What it does |
|---|---|---|
| A | On your pull, one at a time | You type `stage one`; jep stages one candidate with context from the Idiverse or your Yours-zone history; you type the note. No daily slot. Nothing breaks if you never pull |
| B | Daily processing, Tris's way | Each morning you sort yesterday's fleeting notes and write atomics. Needs your hand daily, the cause that ended five of six attempts |
| C | Shelved | The Idiverse card moves to archived |

**W2. Literature notes: whose words?**

| | Option | What it does |
|---|---|---|
| A | jep writes the source note | As the seven today: claims, timestamps, what was checked. Your words go into atomic notes only |
| B | jep lays out highlights, you write under each | Odysseas's method in full. The struggle stays yours (Alvar's warning); it is a slot you would have to feed |

**W3. Habit dashboard?**

| | Option | What it does |
|---|---|---|
| A | None | Nothing to feed, nothing to abandon |
| B | One habit, counted from a receipt jep can read | You name the habit; jep counts it from files or commits. No checkbox, and by the jar's rule no streak or rate is shown |

**W4. Where does the board live?**

| | Option | What it does |
|---|---|---|
| A | Above your Yours zone in `daily/Today.md` | jep replaces its frozen 09-19 block with the three-row Now table and a link to Workshop. Your zone stays byte for byte. The board sits in the tab you already keep open |
| B | Only on `Workshop.md` | `Today.md` keeps its 09-19 block; you open Workshop when you want it |

jep did not touch `daily/Today.md` today: you were typing in it this morning.

## 8. Your hand, and two words

1. **TELOS Current Focus** is dated 2026-09-09. It opens with tutoring, which closed 09-25, and it omits AIMV, the project with the most sessions since 10-12. Text matching the board, for your hand: `1. AIMV: "Pay Attention" in review (v3)` / `2. XCOM campaign` / `3. Workshop` / `Frozen: Tutoring (K and D closed 09-25), I4, Curtains, DECADEnts, Kid Studio. Standing: Cash, HQ.`
2. **Value cells.** jep guessed `value` on all eleven cards, with the basis written on each. The Matrix is only as true as those cells.
3. Say **"chain the check"** and jep adds one fail-safe line to the 30-minute autocommit script, so stale cards get flagged by the clock.
4. Say **"audit worktrees"** and jep lists which of the 23 old vault copies are pushed and safe to remove. Nothing gets deleted without a second word.

## 9. Receipts

- `python -I projects/workshop/tools/hub_check.py`, run 2026-11-11: `hubs 11 | active 3 | errors 0 | warnings 1`, the warning being `WIP: 3 active (AIMV, Workshop, XCOM), cap is 2`. Its first run returned one error, `Cash: STALE, card says last 2026-10-22, session log has 2026-10-23`: jep's own mistake, caught and corrected, along with two softer date mismatches (HQ, I4).
- Both `.base` files parse as YAML; views found: Now (table), Board (kanban), Matrix (table), All (table); Literature, Atomic. Formula parentheses and quotes balance.
- Kanban syntax (`type: kanban`, `groupBy`, `groupOrder`) and the drag behaviour read from obsidian.md/help/bases/syntax and /views/kanban on 2026-11-11.
- Six transcripts fetched with `youtube-transcript-api` (anonymous) and read in full: 3,391 + 3,299 + 2,967 + 3,456 + 2,180 + 8,818 words. Titles and channels from YouTube's oEmbed endpoint.
- Reddit thread via the Arctic Shift archive; matches Idi's saved copy of 2026-01-28.
- AIMV Review Room queried 2026-11-11: 0 notes.
- Branch `worktree-workshop-2026-11-11`; files copied into `D:\work\vault` for Obsidian.
- Not verified: any rendering inside Obsidian; the Obsidian version; whether `order:` sets Kanban card fields (the docs do not say).

## 10. Risks

1. Rule 4 (card updated with the log row) is still a rule jep must follow. The checker turns a miss into an ERROR line; until "chain the check", something has to run the checker.
2. `value` is a guess on every card.
3. jep reads one side of the machine: the live Idiverse, bookmarks and eleven `D:\` folders are closed to it. Any index is partial until that changes.
4. The alternative jep weighed: no board at all, only the cap of two plus the handoff files that already work. The board earns its place only if the Matrix or the Board changes one decision in the next two weeks. If neither does, archive it.

## 11. Idi's rulings, 2026-11-11 afternoon, and what each became

**Unverified:** `Board.canvas`, the four pane bases, the Morning table and the corrected "Days quiet" column have not been seen rendered.

| Ruling, in his words | Done | Where |
|---|---|---|
| "all four tables appear" | Receipt for the morning build; Obsidian kept `type: kanban` and `groupOrder` when it rewrote the file | `bases/workshop.base` |
| "Days quiet" shows `Cannot find function "round" on type Duration` | Subtracting two dates gives a Duration; the formula now subtracts `number(date)`, documented as milliseconds. Same bug fixed in `calendar.base` and `projects.base` | three base files |
| W1 B, daily processing | Morning pass defined; 7 fleeting notes staged from his own idea stubs in `D:\work\PKMS\Ideas`, wording verbatim; Idiverse card set to active | `Workshop.md`, `inbox/fleeting` |
| W2 B, his words under jep's highlights | The 7 literature notes rebuilt: 49 verbatim highlights, each with space under it; `processed` flag per source | `projects/workshop/sources` |
| W3 A | No habit dashboard | none |
| "Delete Today.md" | Deleted after proof that the file equalled its committed copy (`8feeaeb`) and its Yours zone was empty. The daily-note procedure and `intent.md` now point at the Whiteboard and the board | `daily/Today.md` gone; dated archives kept |
| "The board should have its own file" | `Board.canvas`: six cards on one canvas, each base card live | `projects/workshop/Board.canvas`, `panes/` |
| "a workspace/layout using the Obsidian Workspaces core plugin" | **Blocked for jep.** The write guard denies jep Obsidian's config folder ("managed by the app, not by Claude"), where layouts are stored. His hand, three steps, on `Workshop.md` | section One screen |
| "update TELOS Current Focus" | **Blocked for jep.** The guard denies jep the TELOS folder ("jep reads only"), by his own 09-08 ruling. Paste-ready text was handed over in the terminal | his hand |
| "chain the check" | One fail-safe line in the 30-minute autocommit script; verdict note rewritten only on change | `C:\Users\jep\hq\vault-autocommit.sh`, `board-check.md` |
| "audit worktrees" | 23 audited: 18 safe to remove (10,985 files, 1,247 MB), 3 hold files found nowhere else, 2 live. Nothing removed | `research/worktree-audit-2026-11-11.md` |
| "good guessing on the values" | All eleven `value` cells marked confirmed | cards |
| XCOM next step | "Describe the issues in your new screenshots, then fix them with jep" | `hubs/XCOM.md` |
| I4 next step | jep's move: find the screenplay or a transcript, settle every checkable item on the rewatch list, leave him the interpretation. Starts when the card is dragged to active | `hubs/I4.md` |

Two things this round changed in the risks above: risk 1 is closed by the clock check, and risk 2 by his confirmation. One is new: W1 B and W2 B are the kind of slot that ended five of six earlier attempts. The test is cheap: the Morning table either shrinks or it does not. If its count is unchanged on 2026-11-25, the ruling gets revisited.

## 12. Third round, 2026-11-11: permissions, the black look, worktrees, Agent View

Idi's screenshot `D:\work\screens\Board.png` shows the canvas rendering as built and the "Days quiet" column showing numbers. jep measured three flaws on it and re-laid the canvas (2460 by 1470 units): the paused column cut off its seventh card, the Morning card scrolled after 8 of 14 rows, the check card showed its properties in place of its verdict. **The new layout is unseen.**

### Opening Obsidian's config to jep

Facts, read from Windows on 2026-11-11:

- Obsidian runs under Idi's Windows account, which is an administrator. jep is a standard user in a separate session.
- Every file in the vault, the deny list and the guard script are owned by `jep` with full control. The guard hook is the only barrier, and it only watches jep's Claude Code tools.
- A plugin is code that Obsidian runs as Idi. Whoever can write into the config's `plugins` folder can run code as him.

| | What stays closed to jep | What it does |
|---|---|---|
| A (jep's pick) | Plugin code only: the `plugins` folder and `community-plugins.json` | jep can build workspaces, themes, snippets, hotkeys, appearance and core-plugin switches. Plugins get installed by Idi, in Obsidian's own browser |
| B | Nothing | jep can also install and edit plugins. Anything that ever steers jep wrongly can then run as Idi |
| C | Everything, as today | Idi builds layouts by hand |

To enact A, Idi's hand, in Notepad: open `D:\work\vault\.vault-config\write-deny.list` and replace the line `/home/jep/vault/.obsidian/**` with these two lines:

```
/home/jep/vault/.obsidian/plugins/**
/home/jep/vault/.obsidian/community-plugins.json
```

Dry run, done by loading the real guard's functions against a copy of the list with that change: workspaces, appearance, themes, snippets, hotkeys and core-plugins come out allowed for both the editor and the shell; `plugins/…/main.js`, `plugins/…/data.json` and `community-plugins.json` stay denied; atomic notes, TELOS and the deny list itself stay denied.

A Windows-level lock on the `plugins` folder (an administrator takes ownership and denies jep write) would hold against anything running as jep, where the hook holds only against jep's own tools. It is a second step, on his word.

### The black look

Found: [[projects/workshop/research/obsidian-foundation-2026-11-11|obsidian foundation]]. Three hand-named workspaces and about 90 colour and style values on pure black, identical in three archived configs. The rebuild needs no plugin code and starts the moment A is enacted.

### Worktrees and Agent View

18 SAFE worktree folders removed, every branch kept; 6 remain. Row-by-row advice for the Agent View (delete 22 of 29 rows): [[projects/workshop/research/worktree-audit-2026-11-11|worktree audit]], last two sections.

TELOS Current Focus was pasted by Idi on 11-11; the cards' `telos` column follows it.

## 13. Fourth round, 2026-11-11: the black layout, built

Idi enacted option A (the deny list now closes only `plugins/` and `community-plugins.json`) and ordered "build the black layout". **Unverified: unseen in Obsidian.**

Built and installed into the vault's Obsidian config: Minimal 9.1.4, the generated snippet `idi-black` (his 88 surviving values and 44 switches, no plugin), his own `properties-layout` snippet, his three layouts adapted to this vault, and a new `Workshop` layout (board 76 %, Whiteboard 24 %, sidebars folded). Details, checks, rollback: [[projects/workshop/research/obsidian-foundation-2026-11-11|obsidian foundation]], section 5. Generators kept in `projects/workshop/tools/obsidian-look/`.

To see it: Ctrl+P → "Reload app without saving", then left ribbon → "Manage workspace layouts" → `Workshop` → Load.
