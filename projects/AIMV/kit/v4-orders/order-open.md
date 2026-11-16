---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: open (0:00.0-0:09.1, 9.1 s)

Scene file `app/src/scenes/open.ts` + `_pa-open.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| open-s01 | 0:07.2 | small | Clean paper under the receipt print | Remove the diagonal shading lines from the receipt paper where the print sits, so the credit letters stand on plain white. Why: At 0:07 the shading lines run through the small letters and thin them, most of all the "5:00". | Do it |
| open-s02 | 0:06.7 | small | Hold the finished receipt two seconds | Print the slip faster so it is whole by 0:06.2, and keep the tear on its beat at 0:07.7. Why: The slip rests whole for 1.6 s. The builder's report names this as short of a 2 s reading hold, and the credits live nowhere else in the opening. | Do it |
| open-s03 | 0:05.6 | small | Let the price tag read in flight | Stretch the tag's flight to the corner from 0.5 s to about 1 s with its letters sharp, and show 5:00.00 for a few frames before the clock rolls down. Why: The tag is a blurred strip for about 8 frames, so the link between the price and the clock is easy to miss. The builder lists it among the three moments they are least sure of. | Do it |
| open-s04 | 0:07.8 | medium | One lens event on the tear | Add a short focus pull or exposure dip that follows the torn slip as it flies at the viewer. Why: You ruled yes to lens effects and none is in v3. The slip already travels toward the lens here, so the effect has a cause on screen. | Do it |
| open-s05 | 0:05.8 | small | Keep the box resting on the sheet | When the chat box shrinks to one row at 0:05.5, slide the fact sheet up with it so the two stay in contact. Why: From 0:02 the box sits on the sheet's top edge, as if propped by it. After the shrink a dark gap opens between them and the box floats. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 66 % of the time, 7.7 moves per 10 s, 7 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `open-e01` The fact sheet leaves whole. From 0:06.0 its header strip sits half in frame, cut by the bottom edge, while the receipt is the subject. Basis: critic A stray (med); audit: sheet on screen 6.9 s.
- `open-e02` Give the SO. stamp its own beat: the box stops typing while the stamp lands (0:02.5-0:05.0 both write at once). Basis: critic A two-focus (med). Eye check before building.
- `open-e03` One copy of each receipt row during the hand-over at 0:07.7-0:08.1 (RECEIPT, TITLE, ARTIST, CHORUS OF MINDS are each drawn twice for 0.4 s); PAY ATTENTION reads once on the receipt (up to 4 ATTENTIONs at 0:06.0-0:08.1). Basis: audit repeat rows.

- dwell, object `composer`: 0:00.3-0:08.2 = 7.9 s, motionless 66 % of it, up to 25.9 % of the frame
- dwell, object `sheet`: 0:01.8-0:08.7 = 6.9 s, motionless 58 % of it, up to 100.0 % of the frame
- dwell, object `micro:sheet-head`: 0:01.8-0:08.3 = 6.5 s, motionless 61 % of it, up to 4.3 % of the frame
- repeat, "attention": 0:06.0-0:08.1, up to 4 on screen at once (ATTENTION 5:00 / PAY ATTENTION)
- entries in place: 2, 2 on a music cue (100 %; chance 0 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 0:02.5-0:05.0 TWO-FOCUS (med): the box keeps typing new words while the card under it shows a headline and a large circular "SO." stamp that is bigger and rounder than anything in the box [text box upper-middle vs document card directly below]
- 0:05.0-0:05.0 STRAY (low): the highlighted line "FIVE MINUTES OF ATTENTION." starts left of the box border and a lone "T" with cursor sits on the line above it [left end of the text box]
- 0:06.0-0:07.5 STRAY (med): the header strip of the document card stays half in frame, cut by the bottom edge, while the receipt and "Keep the receipt." are the subject [bottom edge, center]
- 0:08.5-0:08.5 STRAY (low): a small grey square with a glow under it, visible in this frame only [bottom-left corner of a thin rectangle outline]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 42 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 50 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.49 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 47 % appear in place, 47 % travel in along a main direction, 5 % diagonally; the next word sits to the right of the last one 73 % of the time, below it 20 %
- tracked boxes drawn rotated or in perspective: 0.6 % (film 1.4 %)
- blind critic, RIGID 0:00.0-0:07.5 (med): stacked upright rectangles only: text box, document card under it, receipt; all text in left-to-right rows
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- none placed here in the plan. No effect is added for looking cool.

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 0.00 9.14 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
