---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: class (0:27.9-0:52.7, 24.9 s)

Scene file `app/src/scenes/class.ts` + `_pa-class.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| class-s01 | 0:52.5 | medium | Lay LEAN's line in sung order | Place INSTEAD YOU at left, LEAN in the middle and ON MY WEIGHT at right, so the eye travels left to right as the line is sung. Why: At 0:52 the groups sit upper right, centre, then left. The sung order is "instead you leaned on my weight". The left slot was chosen so the next plate's first words land there, so both plates move together. | Do it |
| class-s02 | 0:45.9 | small | Soften the board behind the phone | While the phone is in view, throw the board behind it out of focus or dim it, so the phone's copy of the words is the one that reads. Why: At 0:45-0:46 THEY SAID, the cursor and YOUR HAND each show twice, once in the phone and once larger behind it. The builder's report lists the doubled words and left them. You ruled yes to focus effects. | Do it |
| class-s03 | 0:38.0 | small | Show one essay card whole | Tilt the camera down a little at 0:36-0:38, or enlarge the front row's cards, so one pasted essay reads whole before GUIDE. Why: The paste is the subject of the line, yet the cards are small and the nearest row is cut by the frame's bottom edge during GUIDE. | Do it |
| class-s04 | 0:40.0 | small | Give the dead lamp a job | Let the unlit hanging lamp sway or flicker once as GUIDE's last i lands, or frame it out during the hold. Why: After it dies at 0:28 the lamp hangs unlit in frame for about 12 s, large at top right during GUIDE, with no action. Your note 8 was about objects that sit in frame and do nothing. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 63 % of the time, 4.4 moves per 10 s, 8 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `class-e01` The 2022 headline panel leaves one bar after the hole joke lands. The panel holds about 9 s (0:34-0:43), five of those seconds as "2022 THE ___ IS DEAD", and line 11 stays 6.0-8.1 s after it is sung. Basis: audit dwell (headline 8.8 s, 7 words); critic A dwell (med).
- `class-e02` The second wall of WRITE IT FOR ME bubbles (0:35.5) differs from the first (0:31.5): fewer, changed or answered. Today it is the same 15 bubbles twice. Basis: critic A repeat (high).
- `class-e03` The essay reads once. In the wall at 0:36.9-0:41.4 "Industrial Revolution" is on screen up to 18 times, and the same text returns for 10.9 s in the next plate. One readable essay here; the other desks carry ruled lines. Build together with late-e01. Basis: audit repeat rows (up to 18 at once) + cross-plate texts; Idi's pinned note on late.
- `class-e04` One THEY SAID and one IN YOUR HAND at 0:45-0:46 (boxed two and three times in a frame); the lone SAID box leaves with THEY (it stays 0:46.5-0:51.0 across three pictures). Basis: critic A repeat (high), stray (med).
- `class-e05` Reading time: "Explain it to me" 0.5 s (needs 1.5), "THE ESSAY IS DEAD" 0.6 s (1.5), the worksheet header 1.4 s (1.8), "write me an essay on the industrial revolution" 1.9 s (2.5). Each gets its time, or shrinks to texture nobody is asked to read. Basis: audit reading rows (inventory gate: 0.25 s a word + 0.5 s).
- `class-e06` Edges, check at 30 fps and fix what holds 0.5 s or more: "due tonight" cut by the left edge (0:32.5, 0:35.5), blue cards cut mid-word (0:41.0), a pale band along the left edge (0:50-0:51), a grey block where the next handwritten word will be (0:48.0). Basis: critic A stray x4 (med).

- dwell, object `micro:kicker`: 0:32.6-0:41.4 = 8.8 s, motionless 48 % of it, up to 1.1 % of the frame
- dwell, object `headline`: 0:34.2-0:43.0 = 8.8 s, motionless 35 % of it, up to 13.2 % of the frame
- dwell, object `micro:ticker`: 0:32.6-0:41.3 = 8.8 s, motionless 49 % of it, up to 0.6 % of the frame
- dwell, object `reel`: 0:32.6-0:41.3 = 8.8 s, motionless 49 % of it, up to 2.1 % of the frame
- dwell, lyric line 11 ("In twenty, twenty, twenty-two ..."): 7 words stay 6.0-8.1 s after they are sung (leave 0:41.1)
- repeat, "pasted": 0:36.9-0:42.0, up to 10 on screen at once (PASTED 13 · ASKED 0 / PASTED 23:58 · 0 EDITS / PASTED 23:59 · 0 EDITS)
- repeat, "edits": 0:37.2-0:42.0, up to 9 on screen at once (PASTED 23:58 · 0 EDITS / PASTED 23:59 · 0 EDITS)
- repeat, "industrial": 0:36.9-0:41.4, up to 18 on screen at once (In conclusion, the Industrial Re / Industrial Revolution)
- repeat, "revolution": 0:36.9-0:41.4, up to 18 on screen at once (In conclusion, the Industrial Re / Industrial Revolution)
- repeat, "desk": 0:37.2-0:41.4, up to 9 on screen at once (DESK 22 / DESK 26 / DESK 27)
- repeat, "headlines": 0:37.0-0:41.1, up to 2 on screen at once (HEADLINES · EDUCATION / headlines)
- repeat, "conclusion": 0:37.2-0:41.3, up to 9 on screen at once (In conclusion, the Industrial Re)
- repeat, "twenty": 0:37.0-0:41.0, up to 3 on screen at once (twenty, / twenty-two)
- too brief to read, "Explain it to me" at 0:30.9: shown 0.5 s, needs 1.5 s
- too brief to read, "THE ESSAY IS DEAD" at 0:35.1: shown 0.6 s, needs 1.5 s
- too brief to read, "WORKSHEET 7B · NAME __________ · DUE TONIGHT" at 0:45.4: shown 1.4 s, needs 1.8 s
- too brief to read, "write me an essay on the industrial revolution" at 0:48.0: shown 1.9 s, needs 2.5 s
- entries in place: 2, 2 on a music cue (100 %; chance 25 %)
- exits in place: 21, 15 on a music cue (71 %; chance 64 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 0:28.0-0:28.0 TWO-FOCUS (high): new lyric box "Every kid in class" on top, the old strip with glowing "POCKET" in the middle, a row of question-mark spheres rising at the bottom [top, middle, bottom]
- 0:28.5-0:30.5 TWO-FOCUS (med): the lyric is the smallest object in frame; the glowing question-mark spheres and blue squares around it are larger and brighter [center stack vs lower half]
- 0:31.5-0:32.5 REPEAT (high): the same phrase "WRITE IT FOR ME" in about 15 blue bubbles in one frame [lower two thirds]
- 0:32.5-0:35.5 STRAY (med): handwritten "due tonight" is cut by the left frame edge ("onight", "e tonight") [left edge, mid height]
- 0:33.0-0:34.5 STRAY (low): the border of the lyric box runs off the top of the frame, so the box looks cropped [top edge]
- 0:33.5-0:35.0 TWO-FOCUS (med): the lyric adds words in the top box while a larger headline types letter by letter in the panel under it ("2022 / THE ESSAY IS DE..."); two lines being written at once [top box vs panel below]
- 0:35.5-0:40.5 DWELL (med): "2022 THE ___ IS DEAD" with a hole where "ESSAY" was sits for 11 frames; the whole panel has been up since 33.0 s [panel, lower half]
- 0:36.0-0:36.5 TWO-FOCUS (high): lyric stack on top, "due tonight" in handwriting, the headline panel, two rows of blue bubbles, a lamp; five kinds of object in one small frame [whole frame]
- 0:38.5-0:40.5 TWO-FOCUS (low): the growing word "guiiiide" and the static panel "2022 THE ___ IS DEAD" under it have similar weight; two older lyric lines also remain above [upper-left vs lower-left]
- 0:41.0-0:41.0 STRAY (med): two blue cards are cut mid-word by the frame ("strial Revolution", "Industrial Re"); the right card runs under the clock [bottom edge]
- 0:42.5-0:42.5 STRAY (low): a small grey slab hangs under the bar in an otherwise empty frame [top-left, under a thin status bar]
- 0:43.0-0:46.0 STRAY (low): a tall thin vertical white line stands alone, far from any text, for 7 frames; at 45.0-46.0 s a second copy appears inside the tablet [right third]
- 0:45.0-0:46.0 REPEAT (high): "THEY SAID" is boxed twice in one frame (outside and inside the tablet); at 46.0 s a third "SAID" box shows on the sheet at right; "IN YOUR HAND" shows twice at 45.5-46.0 s [left half and right edge]
- 0:45.0-0:46.0 TWO-FOCUS (high): a blue-edged tablet holding a small copy of the layout, the original layout still around it, bold "IN YOUR HAND" between them cut by the sheet edge, and a worksheet with a clip sliding in from the right [tablet at left vs sheet at right]
- 0:46.5-0:51.0 STRAY (med): the boxed word "SAID" sits alone, without "THEY", for 10 frames across three different pictures [top-left]
- 0:48.0-0:48.0 STRAY (med): a grey block sits where the next handwritten word will be, this frame only [bottom-left, after "and"]
- 0:50.0-0:51.0 STRAY (med): a pale grey vertical band lies along the left edge beside an otherwise black frame [left edge, full height]
- 0:51.5-0:51.5 STRAY (med): large blurred "LEA.. IT BY HEART," is cut by the top frame edge [top edge]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 43 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 41 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.29 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 27 % appear in place, 45 % travel in along a main direction, 28 % diagonally; the next word sits to the right of the last one 70 % of the time, below it 13 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, ORGANIC 0:28.0-0:30.5 (med): spheres spread in a V with depth and light beams, round shapes against the boxes
- blind critic, RIGID 0:31.0-0:35.0 (high): a pyramid grid of identical rounded rectangles, then two stacked rectangles with rows of type
- blind critic, RIGID 0:46.5-0:49.0 (high): worksheet: boxed tag, numbered line, dashed rectangle, blue rectangle inside it; the handwritten "and THEY didn't understand" at 48.0-49.0 s is the only loose mark
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- typewriter, stamp at 0:32 the 2022 headline. Reason in the line: print is the medium of headlines and bills.
- stretch at 0:38 GUIIIIDE (exists). Reason in the line: the held vowel.
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 27.87 52.72 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
