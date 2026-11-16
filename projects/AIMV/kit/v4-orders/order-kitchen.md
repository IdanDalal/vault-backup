---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: kitchen (2:42.7-3:15.5, 32.7 s)

Scene file `app/src/scenes/kitchen.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| kitchen-s01 | 3:04.5 | small | Clear the leftover I CAN'T FOR | When TAKE, THE TEST and YOU leave the first reply, the whole bubble scrolls away with them. Why: From 3:03 to 3:06 the bubble stays on screen reading I CAN'T FOR, a broken sentence next to the new reply. | Do it |
| kitchen-s02 | 2:55.0 | small | Keep the mirrored clock out of the inside view | Seen from inside the screen, the reversed clock and the reversed HER / AI labels in the top right corner stay dark until the camera is on her side. Why: From 2:50 to 2:59 they sit in the corner as unreadable shapes while the viewer is reading three other text groups. | Do it |
| kitchen-s03 | 2:50.6 | medium | Give the word cards letter-shaped shadows | Each standing card throws the shadow of its letters across the table, away from the lamp. Why: The plan asked for it and the frames show only a flat oval of light, so the lamp does little to the words it lights. | Do it |
| kitchen-s04 | 2:53.0 | medium | Echo the classroom tricks in each bounce | The four trick messages arrive in the blue bubble look of the eight tricks at the dark desks (0:57 to 1:09), and each one bounces off the glass with an empty reply where the essay came back. Why: The ruling on v2 note 13 makes this moment the callback where the tutor refuses each trick. In the frames the kitchen tricks are grey handwriting and the link to the desks is hard to see. | Do it |
| kitchen-s05 | 2:45.5 | small | Pull focus on I CAN. | For the wait on I CAN. the lens holds the words sharp and lets the dark kitchen behind go soft, then returns. Why: You ruled the lens effects in (R35). This focus pull is already built behind a switch and gives the 2 second wait a camera event. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. This plate's events are listed under it.
  - 2:44.6-2:46.3, focus: the AI's slot while I CAN. is written (already coded in `_pa-lens.ts`, mode L)
  - 2:46.9, ca + kick: I WON'T. slams
  - 2:57.1-2:59.9, focus: the camera swings round the screen's edge: the glass passes through focus
  - 3:12.0-3:15.4, bloom, then breathe: the ? streams into the lamp, which swells; on 'dark' the light closes round her answer
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 75 % of the time, 3.1 moves per 10 s, 23 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `kitchen-e01` The five scene labels (IT'S LATE, ONE LAMP, THE KITCHEN TABLE, FRACTIONS, AND A TEST AT 8:00) stop being a list: each attaches to the thing it names and dims, or leaves once used. They sit unchanged for about 10 s while four quadrants move around them (2:52.5-2:55.0, the most crowded stretch of the second half). Basis: critic B dwell (high), two-focus (high); audit: card words 8.6-11.0 s.
- `kitchen-e02` Light and reading in one place at 3:05.0-3:13.5: the lamp flare is the largest, brightest thing for 9 s while all reading happens in small boxed rows beside it, in one framing for 18 frames; the line SO, WHAT'S A HALF OF A HALF stays 7.7-8.9 s after it is sung. Basis: critic B two-focus + dwell (high); audit dwell (14 words; bars, clock, labels 11 s).
- `kitchen-e03` The clock reads as a clock from its first frame: for 9 s (2:50-2:59) its segments read as the letters r:e. Basis: critic B stray (med).
- `kitchen-e04` Check at 30 fps: a blue table panel over the labels for one frame (2:56.5); the white receipt that is there for 4 frames and gone (2:53.5-2:55.0; `slip:bait` enters with no cue at 2:54.1). Basis: critic B exit x2 (med); audit events.
- `kitchen-e05` The lamp's pole runs through the typed line and the cursor (2:44.5-2:47.0) and through the IT'S LATE label (2:54); the handwritten TO THINK floats outside the screen attached to nothing (3:00.0-3:02.5). Basis: critic B stray x2 (med); lead's eye on f_00175.
- `kitchen-e06` The stacked trick bubbles cut each other's text mid-line (2:52-2:56: ASLEEP and two more lines show as half-letters under the next bubble). The newest bubble covers the older ones whole, or they fan apart. Build with the room item on the trick bubbles. Basis: the PC's own model flagged the cut text 5 s in a row; lead's eye on f_00175.

- dwell, family `card:w` x13: 2:48.8-2:59.9 = 11.2 s (median member 9.3 s)
- dwell, family `w` x7: 2:51.7-2:59.8 = 8.1 s (median member 5.0 s)
- dwell, family `opt` x3: 3:09.3-3:15.5 = 6.1 s (median member 6.0 s)
- dwell, family `trick0` x2: 2:51.3-2:57.4 = 6.1 s (median member 6.1 s)
- dwell, object `clock`: 3:04.4-3:15.5 = 11.1 s, motionless 68 % of it, up to 0.6 % of the frame
- dwell, object `card:w463`: 2:48.9-2:59.8 = 10.9 s, motionless 66 % of it, up to 0.6 % of the frame
- dwell, object `card:w466`: 2:49.9-2:59.8 = 9.9 s, motionless 70 % of it, up to 0.6 % of the frame
- dwell, object `clock`: 2:50.3-3:00.1 = 9.8 s, motionless 65 % of it, up to 0.7 % of the frame
- dwell, object `card:w467`: 2:50.2-2:59.8 = 9.7 s, motionless 71 % of it, up to 1.4 % of the frame
- dwell, object `reel`: 3:05.9-3:15.5 = 9.5 s, motionless 71 % of it, up to 0.7 % of the frame
- dwell, object `card:w468`: 2:50.6-2:59.9 = 9.3 s, motionless 75 % of it, up to 0.7 % of the frame
- dwell, object `card:w469`: 2:51.1-2:59.8 = 8.7 s, motionless 77 % of it, up to 1.0 % of the frame
- dwell, object `optlabel`: 3:08.8-3:15.5 = 6.7 s, motionless 75 % of it, up to 0.8 % of the frame
- dwell, object `opt0`: 3:09.3-3:15.5 = 6.1 s, motionless 78 % of it, up to 0.8 % of the frame
- dwell, lyric line 52 ("I can’t ..."): 2 words stay 6.8-7.1 s after they are sung (leave 3:07.3)
- dwell, lyric line 54 ("So, what’s a half ..."): 11 words stay 7.1-8.9 s after they are sung (leave 3:15.5)
- dwell, lyric line 55 ("I ..."): 1 words stay 6.1-6.1 s after they are sung (leave 3:15.5)
- repeat, "late": 2:52.8-2:57.4, up to 2 on screen at once (LATE, / PLEASE ACT AS MY LATE GRANDMOTHE)
- entries in place: 14, 9 on a music cue (64 %; chance 46 %)
- exits in place: 7, 6 on a music cue (86 %; chance 56 %)
- no cue: entry of `slip:bait` at 2:54.1 (1.0 % of the frame, lived 1.7 s)
- no cue: entry of `opt1` at 3:09.5 (0.4 % of the frame, lived 6.0 s)

Blind critic (2 fps sheets, saw nothing but frames):

- 2:44.5-2:47.0 STRAY (med): a thin lamp outline stands directly behind the typed line; its pole touches or runs through the text and the cursor [centre]
- 2:48.5-2:49.5 TWO-FOCUS (low): three labels arrive in three places within 1 s while the lamp bulb lights [lower-centre, right, far left]
- 2:48.5-2:59.0 DWELL (high): labels "IT'S LATE," "ONE LAMP," "THE KITCHEN TABLE," (joined by "FRACTIONS," and "AND A TEST AT 8:00") sit unchanged for about 10 s (22 frames) while everything else moves around them [centre]
- 2:50.0-2:59.0 STRAY (med): a segment-display fragment reads as "r:e" for 9 s; it reads as clock digits only from 184.5 [top-right of the screen]
- 2:51.0-2:57.0 STRAY (low): chat bubble cut by the edge at 171.0 (arriving); bubbles cut by the left edge at 177.0 (leaving) [left edge of the screen]
- 2:52.5-2:55.0 TWO-FOCUS (high): typing top-left, five static labels mid-frame, chat bubbles swapping bottom-left, a white receipt with a counter bottom-right, plus the lamp bulb [all four quadrants]
- 2:53.5-2:55.0 EXIT (med): white receipt present for 4 frames, gone at 175.5 while the rest of the frame is unchanged [bottom-right]
- 2:56.5-2:56.5 EXIT (med): a blue table panel sits over the labels for one frame, covers part of "AND A TEST AT 8:00", gone at 177.0 [centre-left]
- 2:59.5-2:59.5 STRAY (low): the screen's text reads back-to-front (mirrored) for one frame during the camera swing [right]
- 3:00.0-3:02.5 STRAY (med): handwritten "TO THINK" floats outside the screen, unchanged for 6 frames, attached to nothing visible [top-right, above the screen]
- 3:02.0-3:05.5 STRAY (low): line reads "I CAN'T FOR" (middle words gone) for 8 frames [pill on the screen]
- 3:04.5-3:04.5 STRAY (low): "THE TEST" paper cut by the bottom frame edge, only its title strip visible [bottom edge]
- 3:05.0-3:13.5 TWO-FOCUS (high): the lamp bulb with a wide flare is the brightest and largest thing on screen; all reading happens in small rows to its right; a ticking clock at the top is a third [left vs right]
- 3:05.0-3:13.5 DWELL (med): same framing of lamp and screen for 9 s (18 frames); the lamp flare and the row "SO, WHAT'S A HALF OF A HALF," do not change for 14 or more frames [whole frame]
- 3:14.0-3:14.0 STRAY (low): rows cut mid-word by a shrinking mask ("A HALF OF A HAL", "TYPES") [centre]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 33 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 36 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.15 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 50 % appear in place, 35 % travel in along a main direction, 14 % diagonally; the next word sits to the right of the last one 68 % of the time, below it 14 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, RIGID 2:42.5-2:48.0 (med): large rectangular screen outline, one short horizontal row of text; from 165.0 a vertical bezel line cuts the frame at three quarters width
- blind critic, ORGANIC 2:47.5-2:48.5 (med): text turning blue and breaking into a spreading dust cloud
- blind critic, RIGID 2:50.0-2:57.0 (med): monospace rows and pill boxes inside a rectangle; the tilt of the screen is the only relief
- blind critic, ORGANIC 2:57.5-2:59.0 (med): glowing handwritten "SHE'S ASKING ME" writing on over the typed rows
- blind critic, ORGANIC 3:00.0-3:04.0 (high): side-on camera, diagonal table edge and lamp arm, paper tumbling out of the screen onto the table, text lying on the table surface
- blind critic, RIGID 3:05.0-3:09.5 (high): rectangle screen, stacked pill boxes, monospace rows, left-aligned, added top to bottom
- blind critic, RIGID 3:10.0-3:13.5 (high): five rows of boxed monospace text inside a rectangle
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): placements and his rulings

- reflection at the kitchen laptop. Reason in the line: attention looking back. **Not look-tested in phase 1 and not ruled: the plate builder may propose it on a still.**
- geometry at the kitchen's fractions. Reason in the line: her homework. **Not look-tested in phase 1 and not ruled: the plate builder may propose it on a still.**
- Rulings are Idi's taps on the decision page of 2026-11-16 (R36; record `D:\work\vault\projects\AIMV\kit\v4-phase1-2026-11-16.md` section 7). The look tests ran on a bare stage: fit each effect to the plate, keep the sung word readable on its beat.

## 6b. Film rules from R36 (Idi, 2026-11-16)

- Colour, every real object in its real colour: materials take their hue from `_pa-colour.ts` (gold, brass, wood, steel, cream paper, warm tungsten ...), as the object's own grey times the hue. Screens, pasted text and app edges stay screen blue.
- Colour, her handwriting is warm amber. Her question-mark lights stay white-hot (jep's assumption, stated to Idi).
- Colour, the AI: the cursor is screen blue and the word being sung glows blue for its beat.
- Colour, blacks: unchanged from v3. No lifted black point.
- Organic level: balanced (R36). First sketch: `v4org.ts` moment kitchen at level 1.
- Film rules from the phase 0 audit: exits land on cues; one copy of a word per frame unless a hold is the design; a sung line leaves within its bars; type stays inside the frame on every hold; one focus at a time.

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 162.74 195.45 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
