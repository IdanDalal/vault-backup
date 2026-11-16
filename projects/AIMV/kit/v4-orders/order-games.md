---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: games (1:44.1-2:18.5, 34.4 s)

Scene file `app/src/scenes/games.ts` + `_pa-games.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| games-s01 | 1:49.6 | small | Clear the cut-off letters top left | Frame out or hide the large letters "or" and the thin lines from the earlier chat box that sit outside the game screen's border at the top left. Why: They are left over from the fact scene's glass, half cut by the frame edge, and they stay there for all 34 s of the plate. They read as an error. | Do it |
| games-s02 | 2:00.1 | small | Sung order for THAT'S A SKIP | Shift SKIP right so THAT'S A can sit to its left. Why: At 2:00 the top row reads SKIP THAT'S A FRAME BY, while the song says "That's a skip". SKIP keeps its place from the line before, so the row needs room on its left side. | Do it |
| games-s03 | 1:57.5 | small | Turn the arena card upright again | Finish the roll back to upright when the camera pulls out to the level at 1:57, or complete a full turn on "neither sweat at all". Why: VICTORY and BEATING THE BOSS stay upside down for about 8 s, long after the roll has made its point. The fix report expects a critic to call it a mirror. | Do it |
| games-s04 | 1:45.5 | medium | Show the desk screen's edge | During the pull-back at 1:45 and again before the cut at 2:18, show the bezel of the desk screen and a sliver of the room behind it. Why: The game and the glass around it are one flat plane, so the camera's drift gives no depth. The fix report names real depth as the part left unbuilt. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. The event list for this plate is written in phase 1 (R35: each event has a cause on screen and a short window).
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 93 % of the time, 1.7 moves per 10 s, 8 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `games-e01` The dotted border changes with the level. It frames every picture for 34 s at one size and place, and the camera is still for 93 % of the plate. Basis: critic A dwell (high); camera probe (still 93 %, the film's highest).
- `games-e02` The header tabs earn their stay or leave: INFINITE LIVES, GOD MODE ON, SPEEDRUNNERS sit 21-27 s after they are sung. Each tab changes state when its level ends (struck, greyed, counted) or leaves. Basis: audit dwell (6 words, to 2:18.6); critic A dwell (high); lead's eye at 2:10.
- `games-e03` The trophies act on the line. They stand for 10.7 s (2:07.9-2:18.6, motionless 89-94 % of it) and the three *cheat enabled marks sit motionless for 6.8 s. One event per trophy, on the beat. Basis: audit dwell (trophy x3, fine x3); critic A dwell (high).
- `games-e04` The upside-down VICTORY inset leaves when the speedrun line starts (unchanged 1:55.5-2:03.0). Basis: critic A dwell (med); audit: level, bars, victory 7.8 s, motionless 75-83 %.
- `games-e05` Nothing on top of a sung line: the white label over AND EVERY LOBBY SEES YOUR STATS (2:07.5); three lyric lines cut on the left (2:03.0). Check HE on the border (1:47.0) and the garbled zoom frame (1:51.0) at 30 fps. Basis: critic A stray x4 (high, high, med, med).
- `games-e06` `wall2` (65 % of the frame) leaves at 1:52.9 with no cue: move its exit onto the kick. Basis: audit events.
- `games-k01` KEPT: the walls of ESSAY and WORK (1:51.5-1:52.0, about 60 copies for 1 s each). A wall of one word is the picture of the grind. Basis: audit repeat rows; critic A repeat (high), ruled by the lead.

- dwell, family `trophy` x3: 2:07.9-2:18.6 = 10.7 s (median member 10.7 s)
- dwell, family `fine` x3: 2:11.7-2:18.6 = 6.8 s (median member 6.8 s)
- dwell, family `past:w` x3: 1:57.2-2:03.5 = 6.3 s (median member 6.3 s)
- dwell, object `arena`: 1:51.2-2:03.6 = 12.3 s, motionless 54 % of it, up to 61.4 % of the frame
- dwell, object `shelf-panel`: 2:07.8-2:18.6 = 10.7 s, motionless 85 % of it, up to 50.3 % of the frame
- dwell, object `trophy0`: 2:07.9-2:18.6 = 10.7 s, motionless 89 % of it, up to 2.3 % of the frame
- dwell, object `trophy1`: 2:07.9-2:18.6 = 10.7 s, motionless 94 % of it, up to 2.3 % of the frame
- dwell, object `trophy2`: 2:07.9-2:18.6 = 10.7 s, motionless 94 % of it, up to 2.3 % of the frame
- dwell, object `game-label`: 2:07.9-2:16.2 = 8.2 s, motionless 85 % of it, up to 0.6 % of the frame
- dwell, object `level`: 1:55.7-2:03.6 = 7.9 s, motionless 75 % of it, up to 16.6 % of the frame
- dwell, object `bar-YOU`: 1:55.7-2:03.6 = 7.9 s, motionless 81 % of it, up to 3.5 % of the frame
- dwell, object `victory`: 1:55.7-2:03.5 = 7.8 s, motionless 83 % of it, up to 2.3 % of the frame
- dwell, object `bar-BOSS`: 1:55.7-2:03.5 = 7.8 s, motionless 83 % of it, up to 3.5 % of the frame
- dwell, lyric line 31 ("Infinite lives, god mode ..."): 5 words stay 26.1-27.1 s after they are sung (leave 2:18.6)
- dwell, lyric line 33 ("Speedrunners ..."): 1 words stay 21.1-21.1 s after they are sung (leave 2:18.6)
- repeat, "answer": 1:44.2-2:18.5, up to 3 on screen at once (ANSWER / answer’s)
- repeat, "hint": 1:44.2-2:18.5, up to 2 on screen at once (HINT / hint,)
- repeat, "mode": 2:07.9-2:18.5, up to 2 on screen at once (GOD MODE / −GOD MODE)
- repeat, "cheat": 2:11.7-2:18.5, up to 3 on screen at once (*cheat enabled)
- repeat, "enabled": 2:11.7-2:18.5, up to 3 on screen at once (*cheat enabled)
- repeat, "work": 1:51.8-1:52.8, up to 63 on screen at once (WORK)
- entries in place: 40, 36 on a music cue (90 %; chance 49 %)
- exits in place: 37, 23 on a music cue (62 %; chance 50 %)
- no cue: exit of `wall2` at 1:52.9 (64.9 % of the frame, lived 1.7 s)
- no cue: entry of `decayed297` at 1:49.3 (2.4 % of the frame, lived 2.2 s)

Blind critic (2 fps sheets, saw nothing but frames):

- 1:44.0-2:18.0 DWELL (high): the same dotted rectangular border, same size and place, frames every picture for 34 s [whole frame]
- 1:45.0-1:50.0 STRAY (high): a text fragment "or" (first "r") cut by the left frame edge, plus a thin horizontal line running from the left edge to the border lower down; it stays in every frame for 33 s [top-left corner, outside the dotted border]
- 1:47.0-1:47.0 STRAY (med): bright letters "HE" sit on the dotted border, cut off, this frame only [right side, mid height]
- 1:48.0-1:50.5 TWO-FOCUS (med): the lyric is dim grey text; the badge "REMEMBER THE JOURNEY" beside it has a bright outline and brighter text [centre-left vs centre-right]
- 1:51.0-1:51.0 STRAY (med): a zoomed frame with huge letters cut by the right edge ("ACHIEVE", "REM / THE") and blocky garbled glyphs at the left [whole frame]
- 1:51.5-1:52.0 REPEAT (high): "ESSAY" and then "WORK" written about 12 times in rows that fill the frame and run off both sides [whole frame]
- 1:51.5-2:18.0 DWELL (high): the header line "INFINITE LIVES, GOD MODE ON," stays for 26 s; after "SPEEDRUNNERS" is added at 116.5 s it does not change again [top strip inside the border]
- 1:52.5-1:52.5 TWO-FOCUS (low): large grey "EYES ON THE BOARD" with blue bars vs a small boxed caption starting bottom-left [centre vs bottom-left]
- 1:53.5-1:54.0 STRAY (low): the caption box sits on top of the inner panel's corner; at 114.0 s it is an empty box [bottom-left]
- 1:55.0-1:56.5 TWO-FOCUS (med): the panel text is upside down ("VICTORY", "BEATING THE BOSS") while an upright caption keeps adding words bottom-left [centre vs bottom-left]
- 1:55.5-2:03.0 DWELL (med): the upside-down "VICTORY" panel stays for 16 frames, large until 116.5 s, then as a small inset that does not change [centre, then small inset at right]
- 1:59.0-1:59.5 TWO-FOCUS (med): the sentence lights up across the top ("SKIP THAT'S A FRAME BY") while its next line sits at the bottom-left, with the inset between [top row vs bottom row]
- 2:00.0-2:02.5 TWO-FOCUS (med): "SKIP THAT'S A FRAME BY" across the top, a track line with a moving marker, the upside-down inset, and three lyric lines filling in at bottom-left [top row, middle band, bottom-left]
- 2:02.0-2:02.5 STRAY (low): a small label "ANY %" touches the bottom of the word [top-left, under "SKIP"]
- 2:03.0-2:03.0 STRAY (high): three lyric lines are cut on the left ("LEVEL 'CAUSE THEY KNOW IT / EY EARN BY PRACTICE / D INVENTING THEIR OWN GAME") [left edge of the border]
- 2:04.0-2:04.5 EXIT (low): the heading "IN SINGLE-PLAYER" is gone while the small box under it stays [top centre]
- 2:05.5-2:05.5 TWO-FOCUS (med): a text box lies on top of the card grid and hides most of it, with a heading above and a lone "AND" below [centre]
- 2:07.5-2:07.5 STRAY (high): a small white label covers the middle of "AND EVERY LOBBY SEES YOUR STATS" [lower-centre, on the lyric line]
- 2:08.5-2:18.0 DWELL (high): three trophies on a shelf stay for 20 frames; the changes are an oval drawn around them at 131.0 s and a dimming at 137.0 s [upper-centre]
- 2:12.5-2:13.5 STRAY (low): a wide blue caption box, mostly empty, overlaps the bottom of the profile panel [bottom-left]
- 2:16.5-2:17.0 EXIT (low): the letters "GA" sit by the box corner at 136.5 s and are gone at 137.0 s, while "ME" lands at the end of the caption [left of the caption box]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 31 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 35 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.21 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 32 % appear in place, 28 % travel in along a main direction, 40 % diagonally; the next word sits to the right of the last one 75 % of the time, below it 6 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, RIGID 1:44.0-1:50.0 (high): a dotted rectangular border, pixel capitals in rows, square key slots, a boxed badge
- blind critic, RIGID 1:50.0-2:00.0 (high): boxes inside boxes: dotted border, header strip, inner panel, bars, caption box; pixel capitals in rows; the tilt at 114.5-115.0 s is the only break
- blind critic, RIGID 2:00.0-2:10.0 (high): dotted border, header strip, blue panel, card grid, boxed captions: three levels of nested rectangles in most frames
- blind critic, ORGANIC 2:06.5-2:07.0 (low): the cards tilt and jostle out of their grid for two frames
- blind critic, RIGID 2:10.0-2:18.0 (high): the same nested rectangles as the two sheets before, with a wide caption box added
- blind critic, ORGANIC 2:11.0-2:18.0 (med): one hand-drawn oval, the only curve inside the border for 34 s
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): first-pass placements

- neon at 1:44 games (or chorus2's shop, one of the two). Reason in the line: a sign that sells.
- Each is proven on a still in phase 1 before it is built (rule of 10-27: an effect needs a reason in the line).

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 104.13 138.54 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
