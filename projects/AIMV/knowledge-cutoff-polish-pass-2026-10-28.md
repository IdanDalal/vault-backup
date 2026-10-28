---
type: project
created: 2026-10-28
author: jep
status: active
---

# Knowledge Cutoff: polish pass done, full7b rendered (2026-10-28)

Follows [[handoff-2026-10-27-polish]] (your verdict on full6, P1, P2, your 13 notes, rulings 1-9, all standing).

**Watch:** `D:\work\AIMVs\ours\video\full7\kc-full-1080p.mp4` (194.1 s, 1080p60; render full7b). Sheet: `full7-sheet.jpg` beside it.

## The floor, measured blind (three panels, refs mixed in, never told which video)

| | full6 | full7 | full7b | refs (full7b panel) |
|---|---|---|---|---|
| mean, gap to the refs | 0.79 below | 0.29 below | 0.32 below | R1 3.63, R3 3.12, R4 3.67 |
| windows scored 2 or less (the floor) | 29 % | 18 % | 14 % | 0-19 % |
| windows scored 4+ | 16 % | 30 % | 30 % | 27-62 % |
| tag: timing (lingering, overlapping) | 49 % | 43 % | 27 % | 12-23 % |
| tag: glass (stuck to the screen) | 54 % | 11 % | 8 % | 8-15 % |
| tag: drawn picture | 23 % | 33 % | 40 % | 35-65 % |

Method: every 2 s of our video plus 26 random windows of each ref, 4 frames per window, shuffled, two labellers per panel with 20 shared windows (they agree within 1 point on 19-20 of 20). New labellers and a new shuffle each time. Limits: labellers can recognise our lyrics; tags vary by labeller, so compare our column with the refs' column in the same panel. Receipts: kc-engine `reports/q0-panel.md`, `q2-panel.md`, `q4-panel.md`.

## Your 13 notes, as built

| # | your note | full7b |
|---|---|---|
| 1, 11 | as few 2D / UI / subtitle layers as possible; drop the commentary | all 28 asides gone; 16 other screen-stuck layers removed or moved onto the set; the chat, the toggle, the profile card and the ticker became objects in rooms (glass 54 % to 8 %) |
| 2 | dust slower, bigger, more text | 11 past sessions burn to dust over 2.1 s; only "first time" survives |
| 3 | atoms rough, quick, "name" lingers; amateur timing everywhere | about 1,700 ink grains lift off "magic," and write "name" into the letter's empty To: box; the card lifts off and takes "name" with it. Timing defects found by a new frame-by-frame tool: 179 on full6, 25 on full7b, all of a named, accepted kind |
| 4 | font cycling over the waiting blank, shared with "casting spells... word" | the blank before "word" and "inferred" is the model's next-token menu: candidates (world, lord, wand / offered, informed, inferno) cycle with probability bars and settle on the sung onset; the rest of both lines are dictionary entries |
| 5 | pick the music app (a DAW), lose the 3D timeline | one DAW arrangement: "+2 days" on its ruler, BEATS drawn as MIDI notes on the 16ths |
| 6 | RECEIPTS needs time | a frame-height thermal slip prints RECEIPTS and fades letter by letter to NO RECORD from 26.3 s, about 2 s |
| 7 | view counter = old and flat; the stadium | an empty stadium fills ring by ring, flashbulbs, 96 camera rigs, a dancer drawn in one line; the counter lives on the stadium scoreboard |
| 8 | tomorrow: whole frame, the grey line is the cutoff, a real gag, the cut waits | the road is the model's timeline; the lit post is "last row of training data"; the line stands at the post and "tomorrow" alone lands past it; people from beyond the line carry later date tags; the cut waits for "tomorrow" to finish |
| 9 | copies with no reason (river, checkmark word, fuse) | 41 borrowed techniques audited for a Knowledge Cutoff reason: 7 removed (river, the leetspeak decay, the Messi wave...), 20 rebuilt from our own objects (fuse = the algae's blue light turning into our yellow; frustum's far plane = the cutoff line; the page wall lifts as one block...) |
| 10 | "scored" as a kicked ball in an arch | the six letters ride one parabola over the ARG keeper (your June pick), the arch peaks on the cutoff line, the letters drop into the net one by one and it bulges; about 1.2 s in one shot |
| 12 | hard-to-read text; a clarity standard | standard calibrated on 61 text boxes of R1, R3, R4 (sung word 28 px cap, label 13 px, contrast 4.5:1, speed, letter spacing on curves); flagged sung words 41 to 17, the rest are words moving fast through a transition |
| 13 | camera stops and zooms randomly; boring pauses; the garbage pile out of frame; moves only while sung | the heap is in frame from the first CUT-OFF (7 % of frame height) to the last (35 %), every piece seen landing, JUNE's flaps fall onto it; undeclared dead stops 4 to 0; zoom share of camera motion 62 % to 43 %; time in moves of 3 s+ 2.2 % to 6.9 % (R1 20.5, R4 14.2); motion still leans toward the sung words (correlation 0.21 to 0.14; refs 0.00-0.06); the beat sync you liked is unchanged |

P1 (the oldest scenes): every set-up ranked by how little it changed since v1 (picture similarity plus an eye label); the bottom of the list (outro, the view counter, the essay pull-quote, the letter card, the dlss blank, the session) was rebuilt.

## Gates on the whole render (full7b)

All 483 sung words light (4K, negative control 0); beat 2.26 whole, choruses rising 2.33 < 2.53 < 2.59 (full6 2.07; 1.94 / 2.35 / 2.44); cut timing -12 ms against the drum hit; 1 brightness flip (the allowed whip into the outro); the loop's last frame matches frame 0 at 42.0 dB (full6 39.4; a sub-frame bug blended the tail into it, fixed); the 35 dB silence unchanged; text repeats 59 (18 are the next-token menus by design). 12 small check rows left in four spots (tune2's TRUE touching the sheet's crop marks; one frame of two words at 65.08; a stamp edge at 33.2), listed in kc-engine `reports/q3-fix-b2.md`.

## Not done, honestly

1. **The floor that is left**: the blind panel's weakest plates on full7b are turnedout2 (the card still reads as a form with the line typed under it), jimothy's opening (74-76 s), tune2/tune3 (the line on the piano roll and in the corridor still reads as a caption to strangers), born 22-26 s (DAW into stadium, busy). This is where a next pass would start.
2. **Frame travel** is short of the refs: long moves 6.9 % of the time (target 10 %+). The fix round traded some travel for clean cuts.
3. Panels are noisy between rounds (the refs' own means move 0.1-0.15); the trend across three panels is consistent, single numbers are not.

## How the pass ran

Phase 0 measured before any art (blind panel, timing tool, clarity standard, camera, the oldest scenes, the borrowed-technique audit); six plate owners rebuilt their plates against written rulings; I looked at every owner's window myself and sent back what failed (the "scored" blob became your arch; the stadium that did not fill; the colliding road words); full7, two independent critics, a second panel, a fix round, full7b, a third panel. Three usage-limit stops and one API outage cost time; every stop was checkpointed, nothing was lost. Engine commits through `e913daf` and later (kc-engine `D:\work\aimv-lab\kc-engine`).
