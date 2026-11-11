---
type: note
created: 2026-11-11
author: jep
status: active
---

# Workshop

One question: **what gets the next hour?** This page is the reference. The one-screen view is [[projects/workshop/Board.canvas|Board.canvas]]. Idi's typing surface is [[Idi's Whiteboard]].

## One screen

`Board.canvas` holds six cards: Now, Morning, the clock check, the jar, the Board, the Matrix. Shift+1 zooms the canvas to fit the window.

Saving it as a layout takes Idi's hand, once (Obsidian's config folder is closed to jep by the write guard):

1. Settings → Core plugins → Workspaces: on.
2. Open `Board.canvas`; drag the `Idi's Whiteboard` tab to the right edge so both show.
3. Left ribbon → "Manage workspace layouts" → type `Workshop` → Save.

Coming back to it: the same icon → Load.

## Now

Active projects, grouped by whose move it is.

![[workshop.base#Now]]

## Board

Drag a card to another column to freeze or thaw a project. The drag rewrites that card's `status`.

![[workshop.base#Board]]

## Matrix

Idi's moves only, frozen projects included. His January axes: value, by the effort of the next step.

![[workshop.base#Matrix]]

## Morning pass

Ruled 2026-11-11 (W1 B, W2 B). What waits is the Morning table.

![[library.base#Morning]]

1. **Fleeting notes** (`inbox/fleeting`): read each one. Under 2 minutes: do it. Belongs to a project: say so. Unclear: leave it. An idea: write its atomic note. Tick `processed` when it is spent.
2. **One source** (`projects/workshop/sources`): write under its highlights in your own words. Tick `processed` when the source is spent.
3. **Atomic notes** go in `atomic-notes/`, typed by Idi. Filename = the claim. `up` = one parent note. `maturity` = baby, child or adult.

jep's side:
- A link or a title typed on the Whiteboard after `source:` is an order: jep lays out its highlights as a new literature note.
- A Whiteboard or phone-capture line that opens with `idea:`, `thought:`, `note:` or `remember:` becomes a fleeting note, original wording kept in a callout.
- jep leaves alone every line under a highlight, and everything in `atomic-notes/`.

## Dated

Anything in the vault with a `due:` this week. Empty on most days so far.

![[calendar.base#This Week]]

## Rules

1. **Two projects active at a time.** A third thaws when one freezes. Four are active today (AIMV, XCOM, Idiverse, Workshop).
2. One 4090 job at a time: a render, or the local model.
3. Two agents at once; findings go to files.
4. Every session ends with two writes: the session-log row, and that project's card (`next`, `ball`, `cost_min`, `effort`, `last`).
5. Idi's inputs: the Whiteboard, a reply by index, a drag, a tick, and his own words in the Morning pass.

Rules 2 to 4 are jep's to keep. Rule 1 is Idi's, by drag.

## Resources

| Resource | Holds | Spent on | Limit |
|---|---|---|---|
| Idi's attention | one thing at a time | the Idi group in Now, cheapest first | rule 1 |
| jep (Max plan) | background sessions | cards with `ball: jep`, and whatever Idi orders | rule 3; weekly plan usage (two limit stops on 11-05) |
| 4090 | one job | renders for AIMV, DECADEnts, Kid Studio; the local model for triage | rule 2 |
| Codex CLI (ChatGPT plan) | mechanical edits | on jep's call | none hit yet |

## Card fields

| Field | Values | Who sets it |
|---|---|---|
| `status` | active, paused, done, archived | Idi (drag) or jep on his word |
| `next` | one step, one line | jep, at session end |
| `ball` | Idi, jep, 4090, none | jep |
| `cost_min` | Idi's minutes for the next step | jep |
| `value` | high, low | Idi (all eleven confirmed 11-11) |
| `effort` | low = 15 minutes or less of Idi's time, else high | jep |
| `last` | date of the last session | jep |
| `entry` | the one file to open first | jep |
| `telos` | the Current Focus line it serves | jep reads, Idi's hand edits TELOS |

## Jar

Built 204 / Received 103, still since 2026-09-05. Reply `W C4` or `W C5` to accept.

![[projects/wins-jar#Candidates and rulings pending]]

## How it stays true

- The vault's 30-minute autocommit runs `hub_check.py --write` ("chain the check", 11-11). It checks every card (fields, links, the cap of two, each `last` date against `projects/intent-log.md`) and rewrites the note below only when the verdict changes.

![[projects/workshop/board-check]]

- Reports: [[projects/workshop/workshop-report-2026-11-11|workshop report 2026-11-11]] (with the afternoon rulings), [[projects/workshop/research/worktree-audit-2026-11-11|worktree audit]]
- Evidence: [[projects/workshop/research/env-history|six earlier attempts]], [[projects/workshop/research/asset-map|asset map]]
- All views in one file: `bases/workshop.base` (Now, Board, Matrix, All) and `bases/library.base` (Morning, Literature, Atomic, Fleeting). The canvas uses one small base per card, in `projects/workshop/panes`.
