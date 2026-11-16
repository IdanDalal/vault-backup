---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: verse4 (3:28.0-3:58.2, 30.2 s)

Scene file `app/src/scenes/verse4.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| verse4-s01 | 3:33.0 | medium | Add camera kicks on the flight's beats | The camera takes a short jolt on the strong beats of the flight: each calendar pad standing up, each split of the rings, each stamp on the test. Why: This verse has the lowest on-beat score in the film, 40 % against a 45 % bar. The plan for the next round already names kicks here. | Do it |
| verse4-s02 | 3:45.2 | small | Let the eight beams leave by a cause | The beams swing away or dim over a few frames as SOMEWHERE NEW lands, on the beat. Why: At 3:45.25 all eight beams switch off in one frame, about 11 frames off the beat. The whole-video critic listed it. | Do it |
| verse4-s03 | 3:50.7 | large | Fill the other windows with raised hands | Each window of the wall shows a small classroom of raised ? hands like ours, and the camera pulls back once more to show a city of them. Why: The plan was a pull-back from classroom to school to city to a stadium of hands. The build stops at one wall, and its other windows hold rows of grey discs that do not look like hands. | Do it |
| verse4-s04 | 3:39.9 | medium | Turn the infinity sign into the 8 | When the infinity sign lifts off the test it stands upright and becomes the 8 that the paper's line and the eight heads then pick up. Why: An infinity sign on its side is an 8. The idea is on the list made from your v2 note 7 and was never tried on stills. | Do it |
| verse4-s05 | 3:31.7 | small | Lift the calendar pads into the frame | SEP, OCT, NOV and DEC stand higher and a little longer, so each month and its 0 reads whole before the next one. Why: On the frames SEP and OCT pass half cut by the bottom edge while the line above them is also being read. | Do it |

## 2. Idi's pinned notes (verbatim)

- `note-verse4-211` at 3:30.7: "The "WHY"s shouldn't move - they should multiply. Perhaps even keep them as the questions "she" asks "by July" or something. Also, I think only the word "WHY" should be in that font, and the word "THAT" should be in the same font as the rest of the words."
  - jep's reply in the room: Taken as written: the WHYs stay where they land and multiply, one per ask, and they remain as her questions through 'by July'. WHY alone keeps her handwriting face; THAT returns to the lyric face. It goes into verse 4's work order for v4.

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. This plate's events are listed under it.
  - 3:28.0-3:29.5, exposure: the flight into the white light: overexposed, then adapting
  - 3:36.9-3:39.6, bloom: the 0 widens into a glowing infinity sign
  - 3:43.0-3:45.3, flare + breathe: the eight heads: a streak from every beam (already coded in `_pa-lens.ts`, mode L)
  - 3:51.0, fov: the dive back in over the crowd of hands
  - 3:28-3:58, kick: small camera kicks on the visual hits that land on kicks (film-s06: 40 % on the beat today)
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 34 % of the time, 4.6 moves per 10 s, 41 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s06` Verse 4 hits the beat more often: Add visual hits on the kicks in 3:28-3:58.
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `verse4-e01` One QUESTIONS and one 400 per frame at 3:34.5-3:36.0 (QUESTIONS twice, 400 three times; QUESTIONS ASKED up to 7 at once from 3:32.4). Basis: critic B repeat (high); audit repeat rows.
- `verse4-e02` Calm the camera and keep type inside the frame: HUNDREDS DAILY cut in half by the top (3:33.0), the lyric block cut by the right edge (3:42.5), a holed grey bar at the frame edge (3:32.0), cards and hands cut by the bottom (3:54.5). This plate has the film's most camera reversals (41). Basis: critic B stray x4 (high, high, med, med); camera probe.
- `verse4-e03` One focus at 3:48.5-3:54.0: seven kinds of thing in one frame at 3:53.5; four areas at 3:48.5 with the hand's wrist touching ANY QUESTIONS?. Basis: critic B two-focus (high, med).
- `verse4-e04` The bulb-grid picture at 3:50.0-3:51.0 comes back unchanged in chorus 3 at 4:10.5. The second showing differs: more bulbs lit, a different framing. Seam item with chorus3. Basis: critic B repeat (med).
- `verse4-e05` Exits land on cues: 8 of 28 in-place exits sit on a music cue (chance 40 %). Counts toward film-s06. Basis: audit events.

- repeat, "attention": 3:40.4-3:44.7, up to 3 on screen at once (3.2.2  Multi-Head Attention / Attention Is All / parallel attention)
- repeat, "questions": 3:32.4-3:36.4, up to 7 on screen at once (QUESTIONS ASKED)
- repeat, "music": 3:53.7-3:55.0, up to 8 on screen at once (MUSIC)
- repeat, "story": 3:53.7-3:55.0, up to 8 on screen at once (STORY)
- repeat, "colour": 3:53.7-3:54.9, up to 8 on screen at once (COLOUR)
- entries in place: 5, 5 on a music cue (100 %; chance 53 %)
- exits in place: 12, 2 on a music cue (17 %; chance 40 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 3:30.0-3:32.5 REPEAT (high): "WHY" four times in a row for 6 frames; "AND THEN" twice at 210.0-210.5 [centre]
- 3:31.0-3:32.5 TWO-FOCUS (med): lyric block on top, glowing WHY row in the middle, calendar pages flipping months below [top, middle, bottom]
- 3:32.0-3:32.5 STRAY (med): a grey bar with a row of holes enters at the frame edge, cut off; at 212.0 it sits under the clock [bottom-right corner, then bottom-left]
- 3:33.0-3:33.0 STRAY (high): "HUNDREDS DAILY" huge and cut in half by the top frame edge [top edge]
- 3:34.5-3:36.0 REPEAT (high): "QUESTIONS" twice (large handwritten, and the "QUESTIONS/DAY" label); the number 400 three times at 215.5-216.0 ("400/DAY", "QUESTIONS/DAY 400", "400 / 0") [centre]
- 3:36.5-3:36.5 STRAY (low): small grey rectangle stub left where the calendar was [above the panel]
- 3:38.5-3:38.5 STRAY (low): the infinity sign looks doubled or smeared [results box on the paper]
- 3:40.0-3:42.0 TWO-FOCUS (med): a paper with a readable heading at left, light rings in the centre, a lyric block growing at right [left, centre, right]
- 3:42.5-3:42.5 STRAY (high): lyric block cut by the right frame edge ("SHE G", "QUESTI", "THEN AN") [right edge]
- 3:43.5-3:44.5 TWO-FOCUS (med): a white receipt slides in bottom-left with lines being added while eight beams and a three-line lyric fill the centre [bottom-left vs centre]
- 3:47.5-3:49.0 STRAY (low): "ANY QUESTIONS?" leaves its panel, drifts left and down, and ends dim beside the hand [left, then bottom-left]
- 3:48.0-3:48.0 STRAY (low): half a glowing disc cut by the bottom edge for one frame [bottom edge, centre]
- 3:48.5-3:49.0 TWO-FOCUS (med): glowing hand left of centre, "ONE HAND UP IN THE AIR," top-right, text panel right of centre, "ANY QUESTIONS?" bottom-left; the wrist of the hand touches "ANY QUESTIONS?" [four areas]
- 3:50.0-3:51.0 TWO-FOCUS (med): big two-line lyric over a grid of boxed bulb rows, with a tiny cluster of hands in the centre [whole frame]
- 3:51.0-3:51.0 STRAY (low): letters look doubled, with a ghost outline [both lyric lines]
- 3:52.0-3:53.0 STRAY (low): an empty dark rectangle sticks out behind the blue panel on its left side [left of the blue panel]
- 3:53.5-3:54.0 TWO-FOCUS (high): blue panel with wireframe cards and four tiny labels, floating "?" bubbles, lyric at the panel foot, a row of hands below, a new handwritten line starting at left [whole frame]
- 3:54.5-3:54.5 STRAY (med): wireframe cards, a "STORY" label and hands cut by the bottom frame edge; one blue line alone mid-right [bottom edge and mid-right]
- 3:55.0-3:58.0 STRAY (low): the list panel runs off the right frame edge while its left edge is inset [right edge]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 32 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 23 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.32 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 36 % appear in place, 42 % travel in along a main direction, 22 % diagonally; the next word sits to the right of the last one 60 % of the time, below it 18 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, RIGID 3:33.5-3:37.0 (high): calendar rectangle, a dark rectangle panel laid over it, rows of bold capitals, grid of dots
- blind critic, ORGANIC 3:43.0-3:44.5 (high): ring of eight lights, beams fanning out in every direction, lights wandering off
- blind critic, RIGID 3:45.0-3:45.5 (med): grid of window rectangles under block capitals
- blind critic, RIGID 3:46.0-3:48.0 (med): grid of desks, rectangle text panel, rows of capitals
- blind critic, ORGANIC 3:48.5-3:49.0 (high): a hand built from question marks rising
- blind critic, RIGID 3:50.0-3:51.0 (med): grid of boxes each holding a straight row of dots
- blind critic, ORGANIC 3:55.0-3:58.0 (high): slanted handwritten list writing itself on, line by line
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- fractal at 3:37 INFINITY. Reason in the line: self-similar without end.
- electricity at 3:41 the eight attention heads. Reason in the line: current = attention switching on.
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 207.97 238.20 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
