---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: fact (1:21.3-1:44.1, 22.8 s)

Scene file `app/src/scenes/fact.ts` + `_pa-fact.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| fact-s01 | 1:41.3 | medium | A room beyond the glass | During the low ride, draw the dark classroom beyond the glass's far edge: desk rows and blue screens in the distance. Why: The ride is the plate's one low-angle shot and the top third of the frame is flat black. The glass is the front desk's screen, so the room is there to show. The builder lists the black as a doubt. | Do it |
| fact-s02 | 1:42.5 | medium | Stay on the ride through the pad | Keep the low riding view until about 1:43.5 and rise to the top view only for the last half second. Why: The ride lasts about 2 s, then 2 s of instrumental sit on a flat frame the builder calls dense. Your reference rides its trail for nearly 5 s. | Do it |
| fact-s03 | 1:40.5 | small | Speed in the lens on the ride | Widen the lens a little and add a brief edge fringe as the line reels her in, easing back when she reaches the button. Why: You ruled yes to lens effects with a cause on screen. The reel-in is a clear cause, and the ride has no sense of speed beyond the words passing. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. This plate's events are listed under it.
  - 1:21.3-1:23.3, focus: the slip travels ahead of the camera; the front-desk screen comes into focus as it lands
  - 1:25.5, ca: the padlock snaps shut on ANSWER
  - 1:38.5-1:40.1, flare + kick: the ANSWER button lights; the hook bites its edge
  - 1:40.1-1:42.0, focus: the low tilted view across the glass: near words sharp, the far edge soft
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 43 % of the time, 5.3 moves per 10 s, 20 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `fact-e01` The tape section holds the sung line whole. At 1:32.0-1:35.0 the first lyric is cut by the left edge for 3 s while text sits in three places with chips, month marks and a bracket caption. Frame it, and stage the three text areas one after another. Basis: critic A stray (high), two-focus (high).
- `fact-e02` The THEY diagram leaves or drops to texture one bar after it completes (done by 1:38, on screen to 1:43.5 under newer lines). One glowing question mark at a time (2 to 3 in a frame at 1:38-1:42). Basis: critic A dwell (med), two-focus x2 (high), repeat (med).
- `fact-e03` Edges, check at 30 fps: "built 'em too" cut by the bottom (1:35.0), three words cut by the bottom (1:41.5-1:42.0), the panel's bottom slice left in frame at the top (1:29.0), empty outline shapes at the top edge (1:38.0). Basis: critic A stray x4 (med).
- `fact-e04` Stop drawing the WHAT DO YOU KNOW? card and its ANSWER and HINT chips when the hook ride leaves them. The engine draws them through all of games (34.4 s); the lead's eye at 2:10 finds them hidden. Seam item with games. Basis: audit cross-plate texts; lead's eye on f_00131.

- dwell, family `w` x16: 1:36.1-1:44.1 = 8.0 s (median member 3.2 s)
- dwell, object `w260`: 1:36.1-1:44.1 = 8.0 s, motionless 42 % of it, up to 2.5 % of the frame
- dwell, object `w261`: 1:36.2-1:44.1 = 8.0 s, motionless 42 % of it, up to 3.1 % of the frame
- dwell, object `inv-labels`: 1:36.6-1:44.1 = 7.5 s, motionless 44 % of it, up to 9.5 % of the frame
- dwell, object `composer`: 1:21.3-1:28.5 = 7.1 s, motionless 64 % of it, up to 34.4 % of the frame
- dwell, object `hint-chip`: 1:37.1-1:44.1 = 7.1 s, motionless 40 % of it, up to 4.5 % of the frame
- dwell, object `tape`: 1:28.8-1:35.7 = 6.8 s, motionless 4 % of it, up to 4.5 % of the frame
- dwell, object `card`: 1:23.4-1:29.7 = 6.3 s, motionless 52 % of it, up to 54.9 % of the frame
- repeat, "answer": 1:38.8-1:44.1, up to 3 on screen at once (ANSWER / answer’s)
- repeat, "hint": 1:39.5-1:44.1, up to 2 on screen at once (HINT / hint,)
- repeat, "mode": 1:32.8-1:35.6, up to 2 on screen at once (APRIL 2025 · CLAUDE LEARNING MOD / CHATGPT · STUDY MODE)
- repeat, "april": 1:33.4-1:35.5, up to 2 on screen at once (APRIL 2025 · CLAUDE LEARNING MOD / April)
- repeat, "learning": 1:33.5-1:35.6, up to 3 on screen at once (APRIL 2025 · CLAUDE LEARNING MOD / GEMINI · GUIDED LEARNING / learning)
- entries in place: 4, 3 on a music cue (75 %; chance 25 %)
- exits in place: 4, 1 on a music cue (25 %; chance 60 %)
- no cue: entry of `inv-labels` at 1:36.6 (9.5 % of the frame, lived 7.5 s)

Blind critic (2 fps sheets, saw nothing but frames):

- 1:22.5-1:22.5 STRAY (low): a blank grey rectangle fills the middle of the frame between cut-off blue squares [top centre]
- 1:23.0-1:24.0 TWO-FOCUS (med): three overlapping rectangles: the typing box, a blue panel half hidden under it, a tilted note card still finishing its own sentence; small fragments of the panel peek out between them [centre]
- 1:25.0-1:27.5 STRAY (low): a thin outline of another box lies above the panel, cut by the top of the frame [top edge]
- 1:26.5-1:27.5 TWO-FOCUS (med): the lyric line, a rolling digit counter beside it, a hint box lighting up white at bottom-right, and the "FREE" tag all change or shine at once [inside the panel]
- 1:29.0-1:29.0 STRAY (med): the bottom slice of the panel (lock and hint box) is still in frame, cut by the top edge, while the new lyric sits in the centre [top-left corner]
- 1:32.0-1:35.0 STRAY (high): the first lyric is cut by the left frame edge for 6 frames ("makers BUILT / arning MODE", "kers BUILT", "LT / E"); at 93.5 s the label and line under the tape are cut too [left edge, upper half]
- 1:33.5-1:35.0 TWO-FOCUS (high): lyric text in three places (upper-left, under the tape at left, lower-right), two toggle chips with labels, month marks on the tape, and "THEY'RE all here" with bracket lines at the top [whole frame]
- 1:35.0-1:35.0 STRAY (med): the last lyric line "built 'em too" is cut by the bottom of the frame [bottom edge, centre]
- 1:35.5-1:35.5 STRAY (low): small tick marks and a piece of a rectangle outline poke up from the bottom edge in a nearly empty frame [bottom edge]
- 1:36.0-1:43.5 DWELL (med): the "THEY" three-arrow diagram is on screen for 16 frames; it is complete by 98.0 s and then sits under newer lines [centre, later lower half]
- 1:38.0-1:38.0 STRAY (med): empty outline shapes: a rounded corner line running off the top-left and an empty rounded box top-right [top edge, left and right]
- 1:38.0-1:39.0 REPEAT (med): two or three question marks in one frame: a large glowing one, a hook-shaped one by the button, one in the diagram [upper-left, upper-middle, lower-middle]
- 1:38.5-1:39.0 TWO-FOCUS (high): a new lyric line with a blue "ANSWER" button, a dotted path and a big glowing "?" on top; the finished three-arrow diagram with its own glowing "?" below [upper half vs lower half]
- 1:40.0-1:42.5 TWO-FOCUS (high): new upright words ("the", "but", "worth", "question's", "ride") appear among older text lying sideways, arrows, a blue button and two or three glowing question marks; the eye has no place to rest for 6 frames [whole frame]
- 1:41.5-1:42.0 STRAY (med): several words are cut by the bottom of the frame ("question's", "back,", "hint,") [bottom edge]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 44 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 34 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.22 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 24 % appear in place, 54 % travel in along a main direction, 22 % diagonally; the next word sits to the right of the last one 65 % of the time, below it 11 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, RIGID 1:25.0-1:28.0 (high): nested rectangles: panel, header field, answer field, hint field, digit boxes, hanging tag; every text line is a horizontal row
- blind critic, ORGANIC 1:36.0-1:37.5 (med): three arrows fan out from one word, a round glowing "?"; the cleanest diagram in the sheet
- blind critic, ORGANIC 1:39.5-1:42.5 (high): the whole layout tips into a slanted plane seen from depth; text runs on diagonals and verticals; the strongest depth move in these 150 s
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- 3D travel at 1:38 the hook ride (exists). Reason in the line: "worth the ride".
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 81.33 104.13 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
