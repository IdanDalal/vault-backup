---
type: note
created: 2026-11-11
author: jep
status: active
---

# Workshop

One question: **what gets the next hour?** Every table below is live. It reads the eleven cards in `projects/workshop/hubs`, so nothing here needs a daily render.

## Now

Active projects, grouped by whose move it is.

![[workshop.base#Now]]

## Board

Drag a card to another column to freeze or thaw a project. The drag rewrites that card's `status`.

![[workshop.base#Board]]

## Matrix

Your moves only, frozen projects included. Your January axes: value, by the effort of the next step. `value` is jep's guess on every card; change the cell to overrule.

![[workshop.base#Matrix]]

## Dated

Anything in the vault with a `due:` this week. Empty on most days so far.

![[calendar.base#This Week]]

## Rules

1. **Two projects active at a time.** A third thaws when one freezes. Workshop is the third today and freezes when its done-state holds.
2. One 4090 job at a time: a render, or the local model.
3. Two agents at once; findings go to files.
4. Every session ends with two writes: the session-log row, and that project's card (`next`, `ball`, `cost_min`, `effort`, `last`).
5. Nothing here asks Idi to fill a field. His inputs stay the three that survived every attempt: the Yours zone, a reply by index, a drag.

Rules 2 to 5 are jep's to keep. Rule 1 is Idi's, by drag.

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
| `value` | high, low | Idi; jep's guess until he changes it |
| `effort` | low = 15 minutes or less of Idi's time, else high | jep |
| `last` | date of the last session | jep |
| `entry` | the one file to open first | jep |
| `telos` | the Current Focus line it serves | jep reads, Idi's hand edits TELOS |

## Jar

Built 204 / Received 103, still since 2026-09-05. Reply `W C4` or `W C5` to accept.

![[projects/wins-jar#Candidates and rulings pending]]

## Library

![[library.base#Literature]]

## How it stays true

- `python -I projects/workshop/tools/hub_check.py` checks every card: fields, links, the cap of two, and each `last` date against `projects/intent-log.md`. jep runs it at the end of every session.
- Report and open rulings: [[projects/workshop/workshop-report-2026-11-11|workshop report 2026-11-11]]
- Evidence: [[projects/workshop/research/env-history|six earlier attempts]], [[projects/workshop/research/asset-map|asset map]]
