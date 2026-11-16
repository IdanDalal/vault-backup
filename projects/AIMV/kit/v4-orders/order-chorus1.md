---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: chorus1 (1:09.6-1:21.3, 11.7 s)

Scene file `app/src/scenes/chorus1.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| chorus1-s01 | 1:20.9 | small | Clean letters on PRESENT | Draw PRESENT in plain white without the shading lines through its letters, and enlarge the register line under it or cut it to three words. Why: At 1:20 the shading lines cut through PRESENT, the word the joke lands on. The register line is 10.5 px tall, the one label the clarity check still flags here. | Do it |
| chorus1-s02 | 1:12.0 | small | A glint on each pupil step | Let the light in the pupil flare for a few frames each time the pupil widens, staying inside the pupil. Why: After the note 14 fix the light is a 2 to 3 px glint for the eye's first two seconds. The builder reports the eye has less life there than before. | Do it |
| chorus1-s03 | 1:17.3 | medium | Focus pull into the pupil | As the camera enters the pupil at 1:17, pull focus from the iris letters to the room behind them. Why: The flight into a reflection is the plate's one impossible move and it has no lens cue. You ruled yes to focus effects, with a cause on screen. | Do it |
| chorus1-s04 | 1:15.0 | medium | Bigger hand in the pupil | Push the camera further toward the pupil during 1:13-1:15 so the raised hand fills more of the frame before PAY ATTENTION covers it. Why: The hand is the chorus's picture of a question and stands about a tenth of the frame tall, on view for about 1.5 s before the word lands over it. | MY WAY: "We should do what you said, and more importantly: the hand is an amateur-level visual, not even close to the quality of any of the refs - we should make it MUCH more conceptually and technically complex than "question marks in the rough shape of a human hand"." |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 71 % of the time, 1.7 moves per 10 s, 0 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `chorus1-e01` The title lands alone at 1:15.5: both handwriting lines, the rings and the pupil scene are still up when it arrives. They leave or dim first. Build with chorus1-s04 (the hand, Idi's MY WAY). Basis: critic A two-focus (high, med).
- `chorus1-e02` The curling column of script that hangs from the top edge at 1:17.0-1:18.5 leaves with the eye scene, or gets a cause. Basis: critic A stray (med).
- `chorus1-e03` Exits land on cues: 2 of 10 in-place exits sit on a music cue (chance 27 %). Basis: audit events.

- entries in place: 1, 1 on a music cue (100 %; chance 17 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 1:11.0-1:16.5 REPEAT (low): the word "ATTENTION" is written many times around the rings; at 75.5-76.5 s the large title "PAY ATTENTION" sits on top of the same rings [iris]
- 1:14.5-1:15.0 TWO-FOCUS (med): handwriting above ("It's a question,"), handwriting below ("hand up in the air"), and a tiny lit scene with a hand inside the pupil [top arc, pupil, bottom arc]
- 1:15.5-1:15.5 TWO-FOCUS (high): the large title lands across the eye while both handwriting lines, the rings and the pupil scene are still there [whole frame]
- 1:17.0-1:17.5 TWO-FOCUS (low): a bright round glow top-left, a column of script glyphs top-right, a row of blue screens across the middle; no text to anchor on [top-left, top-right, horizon]
- 1:17.0-1:18.5 STRAY (med): a curling column of script glyphs hangs from the top edge, cut by it, shrinking over 4 frames; it looks like a leftover of the eye scene [top-right]
- 1:17.0-1:22.5 DWELL (low): the row of blue screens along the horizon stays for 12 frames with little change [top band]
- 1:20.5-1:22.0 TWO-FOCUS (med): large glowing "there" in the middle of a five-line stack in four type sizes; from 81.0 s a small note also starts typing at the bottom [desk centre vs desk bottom]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 36 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 28 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.20 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 52 % appear in place, 48 % travel in along a main direction, 0 % diagonally; the next word sits to the right of the last one 74 % of the time, below it 11 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, ORGANIC 1:11.0-1:16.5 (high): an almond eye outline, rings of text turning inside it, handwriting on arcs above and below; almost no straight line in frame
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- electricity at 1:09 the lamp strike. Reason in the line: current = attention switching on.
- reflection at 1:11 the pupil (exists). Reason in the line: attention looking back.
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 69.58 81.33 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
