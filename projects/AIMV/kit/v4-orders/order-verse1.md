---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: verse1 (0:09.1-0:27.9, 18.7 s)

Scene file `app/src/scenes/verse1.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| verse1-s01 | 0:27.4 | small | Give LOCK and its padlock size | Set "LOCK it" as large as POCKET for its two beats, or push in on it, so the shackle's snap and spring are visible. Why: You asked for a real lock in the O. In v3 the padlock is about 45 px tall at 1080p and its snap lasts 3 frames, in a corner of a board that fills only the bottom third of the frame. | Do it |
| verse1-s02 | 0:17.6 | small | Real Phaedrus text in the small print | Replace the three grey lines at the top of the printed page with the actual passage from Phaedrus 275a in a public-domain translation. Why: The page is labelled PHAEDRUS 275a, yet its small print is the song's own line repeated twice. A paused frame shows filler where a real quote could sit. | Do it |
| verse1-s03 | 0:14.6 | small | Clear the label under the tape | Stop the measuring tape short of the PHAEDRUS 275a label, or move the label above the tape. Why: At 0:14.6 the tape slides over the label and a ghost of its letters shows through the tape's right end, beside NOW. | Do it |
| verse1-s04 | 0:27.6 | medium | Tighter final framing on the board | End the last pull-back closer so the board fills about half the frame height; the class plate would open from the same closer view. Why: From 0:26 the top two thirds of the frame is bare wall with one lamp, and every chalk row is small. The framing was chosen to match the next plate's first frame, so both must move together. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 75 % of the time, 3.7 moves per 10 s, 0 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `verse1-e01` One copy of the Socrates line. Its typed words stay 6.2-7.4 s after they are sung (to 0:17.1) and at 0:17.2-0:20.3 every word of it is on screen twice. The handwriting is the keeper; the typed line leaves once the pen has caught up. Basis: audit dwell (5 words) + 11 repeat rows; critic A repeat (low).
- `verse1-e02` Give three vanishing acts a cause on a cue: "years ago" (0:15.0), "THE" and "'S" of THE INK'S (0:18.5). Each is present in one frame and gone in the next while its neighbours stay. Basis: critic A exit x2 (med); film rule: exits land on cues.
- `verse1-e03` One focus through 0:15.5-0:20.5: six text items in four typefaces at 0:15.5; small lyric far left against the large THE INK'S (0:16-0:18); the new line bottom-left while INK breaks into particles on the right (0:19); that line cut by the left edge at 0:20.5. Finish one event before the next starts and keep the sung line inside the frame. Basis: critic A two-focus x3 (high, med), stray (high).
- `verse1-e04` The POCKET strip dims when it is written and leaves on the first downbeat of the class plate. It stays 6.5 s (0:24.5-0:31.0), the last 3.5 s after it has stopped being written, glowing under the new lines. Seam item with class. Basis: critic A dwell (high), two-focus at 0:28 (high); audit: board 7.8 s.
- `verse1-e05` The ruled slab behind INK at 0:16.0 and its dark shadow copy of THE INK: give it a purpose the eye can see, or remove it. Basis: critic A stray (med).

- dwell, object `page`: 0:09.2-0:21.1 = 12.0 s, motionless 78 % of it, up to 100.0 % of the frame
- dwell, object `board`: 0:20.0-0:27.9 = 7.8 s, motionless 34 % of it, up to 38.8 % of the frame
- dwell, object `board:odds`: 0:20.0-0:27.9 = 7.8 s, motionless 44 % of it, up to 2.3 % of the frame
- dwell, lyric line 4 ("Socrates said writing makes ..."): 5 words stay 6.2-7.4 s after they are sung (leave 0:17.1)
- repeat, "socrates": 0:17.2-0:20.3, up to 2 on screen at once (Socrates)
- repeat, "said": 0:17.2-0:20.3, up to 4 on screen at once (said)
- repeat, "writing": 0:17.2-0:20.3, up to 2 on screen at once (writing)
- repeat, "makes": 0:17.2-0:20.3, up to 2 on screen at once (makes)
- repeat, "memory": 0:17.2-0:20.3, up to 2 on screen at once (memory)
- repeat, "weak": 0:17.2-0:20.3, up to 2 on screen at once (weak,)
- repeat, "know": 0:17.2-0:20.3, up to 2 on screen at once (know)
- repeat, "student": 0:17.2-0:20.3, up to 2 on screen at once (student)
- entries in place: 7, 7 on a music cue (100 %; chance 26 %)
- exits in place: 6, 3 on a music cue (50 %; chance 56 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 0:15.0-0:15.5 EXIT (med): "two thousand years ago" becomes "two thousand"; "years ago" is gone while the timeline bar under it stays [bottom-left of the board]
- 0:15.5-0:15.5 TWO-FOCUS (high): six text items in four typefaces at once: "He feared" at the left margin overlapping the board edge, two handwriting lines, a large italic "THE" mid-board, a third handwriting line, bold "two thousand", the timeline bar, the corner label [whole frame]
- 0:16.0-0:16.5 STRAY (med): a tall narrow ruled slab stands behind the word, with a dark shadow copy of "THE INK" under the white one at 16.0 s; its purpose is not visible [center, behind "INK"]
- 0:16.0-0:18.0 TWO-FOCUS (med): small lyric words ("He feared", "and now") with a glowing cursor line sit far left while the large "THE INK'S" builds on the right; at 17.5-18.0 s a tall vertical line and letter debris hang at the left [far left margin vs center-right]
- 0:17.0-0:19.5 REPEAT (low): the paragraph looks like the same sentence written several times in a row [top of the board, small paragraph]
- 0:18.5-0:19.0 EXIT (med): "THE INK'S" becomes "INK"; "THE" and "'S" are gone between two frames while the line under it stays [large title on the board]
- 0:19.0-0:19.5 TWO-FOCUS (high): bold "I'm made of / and I remember" appears bottom-left with a cursor and glow while on the right "INK" breaks into particles above "THE ONLY PLACE he ISN'T DEAD" [bottom-left vs right]
- 0:20.0-0:20.5 TWO-FOCUS (med): four areas at once: lyric top-left, the sign "THE ONLY PLACE he ISN'T DEAD", an empty blackboard, single words lighting up over the desks [top-left, top, middle, lower third]
- 0:20.5-0:20.5 STRAY (high): lyric is cut by the left frame edge: "m made of / nd I remember" [top-left corner]
- 0:21.5-0:22.0 TWO-FOCUS (med): "Your te..." starts on the board while the five-word row "every word I've ever read" still sits lit above the desks [blackboard top-left vs row above the desks]
- 0:24.0-0:27.5 TWO-FOCUS (high): up to five clusters on one strip: lyric lines at left, tiny blue equations, "Now the POCKET" in a glowing blue box, an odds counter with "LOST", then "answers back, and nobody can ever" and "LACK it" at the right [along the strip, left to right]
- 0:24.5-0:31.0 DWELL (high): the strip stays on screen for 14 frames; after 27.5 s it is no longer being written, only shrunk and stacked under newer text, still glowing blue [strip with "POCKET"]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 37 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 43 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.37 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 28 % appear in place, 54 % travel in along a main direction, 18 % diagonally; the next word sits to the right of the last one 75 % of the time, below it 13 %
- tracked boxes drawn rotated or in perspective: 16.5 % (film 1.4 %)
- blind critic, ORGANIC 0:10.0-0:15.0 (high): cursive handwriting grows letter by letter behind a glowing pen head; curves and uneven baselines; the calmest single focus in these 150 s
- blind critic, RIGID 0:22.5-0:27.5 (med): one wide flat strip, all text in short left-to-right rows, boxes inside the box
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- smoke at 0:09 Socrates' spoken words. Reason in the line: speech disperses, the ink copy stays.
- ink in water at 0:19 "I'm made of ink". Reason in the line: the singer's body.
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 9.14 27.87 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
