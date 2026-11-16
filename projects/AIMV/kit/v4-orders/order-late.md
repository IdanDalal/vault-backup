---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: late (0:52.7-1:09.6, 16.9 s)

Scene file `app/src/scenes/late.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| late-s01 | 1:07.9 | small | Longer rest for the last essay | Type PRETTY PLEASE one beat earlier so its essay card rests about 1 s before the room goes dark. Why: The last card is read for 0.53 s, the shortest of the eight, and it is the card that becomes the lamp. | Do it |
| late-s02 | 0:55.0 | small | Make NO CHANGE readable | Set the readout "NO CHANGE" large enough to read in passing, and drop or shrink the two pan labels. Why: The readout carries the point of the scale: the question weighs nothing once the star is in. It is under 13 px tall and the clarity check flags it. | Do it |
| late-s03 | 1:02.5 | medium | Let the tricks light the classroom | Let each waking screen's light reach the board and the desk rows for a moment, so "due tonight" or the room's shape shows as the camera passes. Why: From 0:57 to 1:08 the frame is near black apart from two screens and a bubble. The link to the classroom at 0:28 rests on dark desk outlines alone. | Do it |
| late-s04 | 1:09.1 | small | Lens flare on the lamp strike | Switch on the short flare streak that was built and tested for the lamp's strike, about a quarter of a second long. Why: You ruled yes to lens effects apart from colour. This is the lamp's first light, and a test clip of this exact moment exists. | Do it |

## 2. Idi's pinned notes (verbatim)

- `note-late-69` at 1:09.3: "From 0:57 to 1:08 the repeating, boring, barely-coherent essay text (Industrial Revolution In conclusion...) stays on screen WAY too much, and the funny prompts stay too little."
  - jep's reply in the room: Agreed, and it is the first entry of the efficiency audit: the essay card holds about 10 s while each trick shows under 2 s. In v4 the tricks get the time and the size, the essay shrinks to a stamp-sized repeat that lands once per trick. This stretch (0:52-1:21) is the proof plate, so you see it first.

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 25 % of the time, 4.2 moves per 10 s, 9 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `late-e01` Invert the time between the tricks and the essay (Idi's pinned note). Each of the eight prompts reads large for 1.5 s or more; the essay lands once per trick at stamp size; never two identical cards in one frame; the eight tricks do not share one four-step cycle. Basis: Idi's note; audit: essay family 0:58.2-1:09.1 = 10.9 s, prompts shown 0.9 s against 1.5 s needed; critic A dwell + repeat (high): twin cards at 0:59, 1:02, 1:04.5, 1:05, the same cycle four times.
- `late-e02` No bubble under a card border and no card text cut mid-word by the frame (1:02.0, 1:02.5, 1:05.0, 1:07.5, 1:08.0). Basis: critic A stray x2 (med). Mostly falls out of late-e01.
- `late-e03` The scale's readout holds a value long enough to read: today each TILT value lives 0.1 s. One settled value, or steps of 0.3 s or more. Basis: audit: micro TILT labels 0.1 s each, no cue; room dossier ref gap ("the small readout that explains the joke is hard to read").
- `late-e04` Exits land on cues. First test of the film rule: of 7 in-place exits here 2 sit on a music cue and 4 have no cue of any kind. Basis: audit events (chance level 40 %).
- `late-k01` KEPT: the gold star on the left against the lyric and the question mark on the right (0:53.5-0:55.5). The two pans are the picture. Basis: critic A two-focus (med), ruled by the lead.

- dwell, family `essay` x8: 0:58.2-1:09.1 = 10.9 s (median member 2.3 s)
- repeat, "industrial": 0:58.2-1:09.0, up to 4 on screen at once (Industrial Revolution / Industrial Revolution was)
- repeat, "revolution": 0:58.2-1:09.0, up to 4 on screen at once (Industrial Revolution / Industrial Revolution was)
- repeat, "pasted": 0:59.3-1:08.4, up to 2 on screen at once (PASTED 23:58 · 0 EDITS)
- repeat, "edits": 0:59.3-1:08.4, up to 2 on screen at once (PASTED 23:58 · 0 EDITS)
- repeat, "desk": 0:59.3-1:05.2, up to 2 on screen at once (DESK 18 / DESK 19)
- repeat, "conclusion": 0:59.3-1:05.2, up to 2 on screen at once (In conclusion, the)
- repeat, "turning": 0:59.3-1:05.2, up to 2 on screen at once (a turning point in history.)
- repeat, "point": 0:59.3-1:05.2, up to 2 on screen at once (a turning point in history.)
- too brief to read, "ACT AS MY LATE" at 0:58.4: shown 0.9 s, needs 1.5 s
- too brief to read, "IT'S FOR A NOVEL." at 1:01.1: shown 0.9 s, needs 1.5 s
- entries in place: 8, 4 on a music cue (50 %; chance 38 %)
- exits in place: 7, 2 on a music cue (29 %; chance 40 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 0:53.5-0:55.5 TWO-FOCUS (med): a gold star (the only warm colour in these 150 s) sits on the left while the lyric and a glowing "?" build on the right [left pan vs upper-right]
- 0:54.0-0:55.0 REPEAT (low): "question" shows twice: the white word and a dark copy offset behind it [upper-right]
- 0:58.0-1:08.0 DWELL (high): the same "Industrial Revolution" card with the same three lines is in almost every frame for 10 s; the same four-step cycle (bubble alone, card plus bubble, two cards, two cards zoomed) runs four times [left half, sometimes both halves]
- 0:59.0-0:59.5 REPEAT (high): two identical cards "Industrial Revolution / In conclusion, the Industrial Revolution was a turning point in history." side by side [left and right halves]
- 0:59.5-0:59.5 STRAY (med): both cards are cut mid-word by the frame ("ial Revolution", "Industrial Rev") [left and right edges]
- 1:00.5-1:04.0 TWO-FOCUS (med): a text card on the left and a brighter text bubble on the right, far apart, at 60.5-61.0 s and 63.5-64.0 s (also 58.0-58.5 s) [left card vs right bubble]
- 1:02.0-1:05.0 REPEAT (high): twin identical cards again at 62.0, 62.5, 64.5 and 65.0 s [left and right halves]
- 1:02.0-1:08.0 STRAY (med): in the zoomed frames (62.0, 62.5, 65.0, 67.5, 68.0 s) card text is cut mid-word by the frame ("strial Revolution", "Industrial Revolu", "evolution") [left and right edges]
- 1:02.0-1:05.0 STRAY (low): a large blue square sits directly under the clock digits at 62.0, 62.5, 64.5 and 65.0 s [bottom-right corner]
- 1:02.5-1:05.0 STRAY (med): a speech bubble overlaps the card's bottom border and its text is partly hidden or tangled with the border ("EACHER SAID", "JUST A FIRS") [lower-left of the left card]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 44 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 35 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.83 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 64 % appear in place, 36 % travel in along a main direction, 0 % diagonally; the next word sits to the right of the last one 40 % of the time, below it 50 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, ORGANIC 0:52.0-0:56.0 (high): a balance scale tips on a diagonal, words tumble and rotate ("LEAN", "LATE"), a round glowing "?" and a five-point star; curves and angles, nothing boxed
- blind critic, RIGID 0:57.0-1:08.0 (high): only rectangles for 11 s: cards, speech bubbles, blue squares, faint desk outlines; all text monospace rows
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- fire, ember at 1:07 the last essay burning into the lamp (a small ember exists). Reason in the line: grow what is there.
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 52.72 69.58 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
