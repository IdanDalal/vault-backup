---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: exam (3:15.5-3:28.0, 12.5 s)

Scene file `app/src/scenes/exam.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| exam-s01 | 3:21.4 | large | Rebuild the ten seconds as a camera solo | The countdown digits become a physical flip clock the camera dives through. Lens effects hit on the kicks, the camera passes the earlier scenes at speed, and it lands on the crack of PENCILS DOWN. Why: This is the ruling on your v2 note 19. The stretch in v3 is still the v2 picture: a still timer during the loudest instrumental of the song. | Do it |
| exam-s02 | 3:19.0 | medium | Make the passing night bigger than a corner clock | While the clock spins from 10:07 to 7:59, the kitchen's lamp pool and word cards come back behind the screen and the light swings across them like a night passing. Why: From 3:17 to 3:21 the only thing changing is a clock about 3 % of the frame's height in a frame that is mostly black. | Do it |
| exam-s03 | 3:25.5 | small | Even out the last three seconds | 0:03, 0:02 and 0:01 each hold the same length, one per beat. Why: On the frames 0:03 holds about 0.6 s, 0:02 about 0.45 s and 0:01 about 0.25 s. The whole-video critic also saw the countdown run at an uneven rate. | Do it |
| exam-s04 | 3:27.7 | small | Add the lens punch on the crack | On the crack the lens bulges and the edges fringe with colour for 5 frames, then the picture returns to normal. Why: You ruled the lens effects in (R35). This one is already built behind a switch, and the crack is the second-strongest hit in the song. | Do it |
| exam-s05 | 3:27.9 | medium | Hold ME WHY into the next verse | The words ME WHY keep their exact place and size from NOW ASK ME WHY through the crack until the next verse sings 'She asked me why'. Why: Your v2 note 10 asks for repeated phrases to hold their place. This pair was skipped only because the plate is due a rebuild. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s02` The exam instrumental becomes the camera's solo: 3:17-3:27: the countdown digits become a physical flip clock, the camera dives through it and tours the earlier motifs fast, lens events land on the kicks, and it lands on PENCILS DOWN.
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 82 % of the time, 3.2 moves per 10 s, 3 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `exam-e01` A QUARTER / NOW ASK ME WHY leaves on the solo's first kick. It holds for 12 s, the longest lyric hold in the film (median word stay here 8.7 s; film 2 s). Her three dots are the thread that stays. Build inside film-s02. Basis: critic B dwell (high); audit dwell (4 words 8.3-9.1 s, herdots 11.2 s).
- `exam-e02` The timer card and test header stand motionless for 6.6 s (87 % of it); the small clock enters at 3:17.1 and leaves at 3:20.9 with no cue. Both fold into the flip clock of film-s02. Basis: audit dwell + events.

- dwell, family `room:w` x6: 3:15.5-3:28.0 = 12.5 s (median member 3.2 s)
- dwell, object `room:w545`: 3:15.5-3:28.0 = 12.5 s, motionless 80 % of it, up to 0.6 % of the frame
- dwell, object `timer`: 3:20.9-3:28.0 = 7.0 s, motionless 84 % of it, up to 4.4 % of the frame
- dwell, object `timercard`: 3:21.4-3:28.0 = 6.6 s, motionless 87 % of it, up to 13.2 % of the frame
- dwell, lyric line 56 ("Now ask me why ..."): 4 words stay 8.3-9.1 s after they are sung (leave 3:24.8)
- entries in place: 8, 6 on a music cue (75 %; chance 4 %)
- exits in place: 2, 0 on a music cue (0 %; chance 8 %)
- no cue: entry of `clock` at 3:17.1 (1.1 % of the frame, lived 3.9 s)
- no cue: exit of `clock` at 3:20.9 (1.1 % of the frame, lived 3.9 s)

Blind critic (2 fps sheets, saw nothing but frames):

- 3:15.5-3:27.5 DWELL (high): "A QUARTER / NOW ASK ME WHY" stays on for 12 s (25 frames); the three dots under it stay 196.0-205.0 (19 frames) [centre, then lower-right, then above the countdown]
- 3:16.5-3:16.5 STRAY (low): a lone cursor bar with nothing beside it (digits arrive at 197.0) [top-left]
- 3:17.0-3:20.5 TWO-FOCUS (med): clock digits racing top-left; lyric and pulsing dots lower-right; a far diagonal [top-left vs lower-right]
- 3:21.0-3:25.5 STRAY (low): a thin vertical bar shows in some frames and is absent in others (seen at 201.0, 201.5, 203.5 to 205.5), like a text cursor on a timer [right of the countdown digits]
- 3:21.5-3:25.0 STRAY (low): the lyric block sits shifted right of the panel: neither centred on it nor lined up with an edge [above the countdown panel]
- 3:27.5-3:27.5 TWO-FOCUS (low): cracks, "PENCILS DOWN.", ghost of "NOW ASK ME WHY" and ghost of "0:00" all in one frame [whole frame]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 46 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 25 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.36 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 33 % appear in place, 50 % travel in along a main direction, 17 % diagonally; the next word sits to the right of the last one 100 % of the time, below it 0 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, RIGID 3:21.0-3:26.0 (med): rounded rectangle with segment digits, lyric in a straight row above, dots in a row below
- blind critic, ORGANIC 3:26.5-3:28.0 (high): letters of "PENCILS DOWN." tumbling in on a curve, cracks radiating from one point across the full frame, shards flying off the corners
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- none placed here in the plan. No effect is added for looking cool.

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 195.45 207.97 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
