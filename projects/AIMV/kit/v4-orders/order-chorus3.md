---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: chorus3 (3:58.2-4:21.1, 22.9 s)

Scene file `app/src/scenes/chorus3.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| chorus3-s01 | 4:14.5 | medium | Make the hanging ? the size of its line | The thrown ? is as tall as the words HANGING IN THE AIR. Its arc starts at the test sheet and stops at the middle of the frame. Why: On the frames the ? is about 2 % of the frame's height, between the word cards. The line is about this object and the eye cannot find it. | Do it |
| chorus3-s02 | 4:08.5 | large | Let the lifted lamp light the city | The lamp that leaves the game screen grows as it rises, the camera follows it out of the window, and the dark things of earlier scenes light one by one as its light reaches them. Why: That was the planned picture for this line. In the build the lamp is a small dot at the left edge for 3 seconds and the city lights up later, on another line. | Do it |
| chorus3-s03 | 4:07.0 | medium | Give the lamp line the wall | BUT A QUESTION IS A LAMP is set large on the classroom wall or across the frame, and the game dialog box carries only the cheat code. Why: It is the song's central line, and here it is the smallest text on screen, under a larger PAY ATTENTION from the line before. | Do it |
| chorus3-s04 | 4:11.5 | medium | Slow the move up the wall to a full beat | The rise from the classroom window to her kitchen takes a whole beat, with the lamp visibly leading the camera. Why: The move takes under half a second and blurs. The automatic check still reads it as a cut, and the builder lists it as the moment least sure of. | Do it |
| chorus3-s05 | 3:59.1 | medium | Save the strongest colour for this chorus | If the colour talk after this watch adds a colour or a warmer light, its full strength first appears on ATTENTION here, and earlier scenes stay below it. Why: The plan saved the full brightness range for this chorus. On the frames the step up is a brighter grey room, a small change. Colour is still open under R35. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. This plate's events are listed under it.
  - 3:58.9, ca + exposure: ATTENTION slams and the room lights up: the first frame with the full value range
  - 4:05.5-4:07.5, flare: a point of light lifts off the screen on A QUESTION IS A LAMP
  - 4:15.7-4:18.0, fov: the flight into the pupil, rhyming with chorus 1
  - 4:18.0-4:21.1, focus: the words lift toward the camera and pass through focus
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 48 % of the time, 4.4 moves per 10 s, 6 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `chorus3-e01` The callback list (1. THE THIRD TWENTY to 4. EIGHT HEADS) stops standing as a list for 12 s: a row lights when its picture returns and leaves when it has. Basis: audit dwell strings (11.8-12.0 s each), family `list` 8.3 s.
- `chorus3-e02` One PAY ATTENTION at a time: twice in a frame at 4:06.0-4:07.5 (background and card); four text layers with no gap at 4:08.0-4:09.5; a second small stack inside the giant lyric at 4:10.5. Basis: critic B repeat (high), two-focus (med, high).
- `chorus3-e03` The kitchen's five labels come back changed and clear of the lyric (4:12.5-4:15.5: unchanged, under a new three-line lyric, with the lamp flare touching line 1). Basis: critic B two-focus (high), repeat (med).
- `chorus3-e04` Type inside the frame: ATTENTION cut by the top (3:59.5, 4:05.5), THEN SOME MORE cut on the left (4:10.5), the lyric cut on the left (4:16.0). Basis: critic B stray x4 (high, med, high, high).
- `chorus3-e05` Strays, check at 30 fps: an empty black square mid-frame for 3.5 s (4:00-4:03), bright streaks from the top edge (4:00.0), a sliver of a pale panel behind the card (4:04-4:06). Basis: critic B stray x3 (med).

- dwell, family `w` x49: 3:58.2-4:21.1 = 22.9 s (median member 1.9 s)
- dwell, family `list` x4: 4:03.5-4:11.8 = 8.3 s (median member 8.2 s)
- repeat, "heart": 4:03.6-4:11.6, up to 2 on screen at once (2. HEART FROM LEARN / HEART)
- repeat, "fractions": 4:11.7-4:16.7, up to 2 on screen at once (FRACTIONS TEST / FRACTIONS,)
- repeat, "test": 4:11.7-4:16.7, up to 3 on screen at once (FRACTIONS TEST / TEST / TEST AT 8:00)
- repeat, "answer": 4:00.3-4:03.0, up to 2 on screen at once (ANSWER: B)
- repeat, "attention": 4:06.5-4:08.0, up to 2 on screen at once (ATTENTION)
- entries in place: 14, 14 on a music cue (100 %; chance 33 %)
- exits in place: 3, 1 on a music cue (33 %; chance 44 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 3:58.5-3:58.5 STRAY (low): a small scribble mark alone [mid-right]
- 3:59.0-3:59.5 TWO-FOCUS (med): "PAY ATTENTION", list panel, big hand cut by the left edge and a row of small hands; one frame later a crowd of hands, desks, a bright panel and a cut-off word [whole frame]
- 3:59.5-3:59.5 STRAY (high): "ATTENTION" cut in half by the top frame edge [top edge]
- 4:00.0-4:03.0 STRAY (med): an empty black square sits in the middle for 3.5 s between the lyric and the phone shape [centre]
- 4:00.0-4:00.5 STRAY (med): bright vertical streaks hang from the top edge behind the lyric [top edge]
- 4:04.0-4:06.0 STRAY (med): a sliver of a pale text panel sticks out from behind the card [behind the blue card, upper-left]
- 4:05.5-4:06.0 STRAY (med): background "ATTENTION" cut by the top frame edge [top edge]
- 4:06.0-4:07.5 REPEAT (high): "PAY ATTENTION" twice in one frame: large in the background and again on the blue card (also 243.5 with the card below) [background and card]
- 4:08.0-4:09.5 TWO-FOCUS (med): four text layers packed with no gap ("THROUGHOUT THE NIGHT", "PAY", "ATTENTION", "YOU HOLD UP HIGH") over a small text panel; lines touch; a lamp dot sits far left [centre]
- 4:10.0-4:10.0 STRAY (low): a tiny blue card left at the bottom edge [bottom edge, centre]
- 4:10.5-4:11.0 TWO-FOCUS (high): giant two-line lyric, a small "PAY ATTENTION / YOU HOLD UP HIGH" stack in the centre, boxed rows of bulbs and "?" all around [whole frame]
- 4:10.5-4:11.0 STRAY (high): "THEN SOME MORE" cut by the left frame edge ("N SOME MORE") [left edge]
- 4:10.5-4:11.0 REPEAT (med): same picture as 230.0-231.0: the same two lyric lines over the same grid of bulb rows [whole frame]
- 4:11.5-4:12.5 TWO-FOCUS (med): a panel of bright white grid cells at left and a panel of white cup shapes at right flank the centre where the lyric types [left and right of the centre panel]
- 4:12.5-4:15.5 TWO-FOCUS (high): a new three-line lyric laid over five returning labels, the lamp flare touching the end of line 1, a paper on the table [centre panel]
- 4:12.5-4:15.5 REPEAT (med): the five labels from 168.5-179.0 are back, unchanged [centre panel]
- 4:16.0-4:16.0 STRAY (high): lyric cut by the left frame edge ("'S A QUESTION," / "D IT'S HANGING" / "THE AIR") [left edge]
- 4:17.5-4:20.0 STRAY (low): a row of blue squares cut by the top frame edge [top edge]
- 4:18.5-4:19.5 STRAY (low): "WERE YOU EVER REALLY" sits on the wireframe desk lines; a line runs through or along the text [centre]
- 4:20.5-4:20.5 STRAY (med): "WERE YOU EVER REALLY" drawn over "PRESENT": two texts overlap, next to the clock corner [bottom]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 43 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 32 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.30 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 21 % appear in place, 68 % travel in along a main direction, 11 % diagonally; the next word sits to the right of the last one 64 % of the time, below it 9 %
- tracked boxes drawn rotated or in perspective: 0.0 % (film 1.4 %)
- blind critic, ORGANIC 4:02.5-4:02.5 (low): the phone shape tilts and slides out
- blind critic, RIGID 4:04.0-4:07.0 (med): square blue card, boxed line, row of square arrow keys
- blind critic, ORGANIC 4:15.5-4:16.0 (high): an almond eye shape opens with "PAY ATTENTION" inside it
- blind critic, RIGID 4:17.0-4:20.0 (high): thin straight wireframe desk, grid floor, centred rows of capitals
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): placements and his rulings

- dancing at "hanging in the air". Reason in the line: words that hang and sway. **BUILD (R36). Kit `hangWord`; worked example window dancing.**
- Rulings are Idi's taps on the decision page of 2026-11-16 (R36; record `D:\work\vault\projects\AIMV\kit\v4-phase1-2026-11-16.md` section 7). The look tests ran on a bare stage: fit each effect to the plate, keep the sung word readable on its beat.

## 6b. Film rules from R36 (Idi, 2026-11-16)

- Colour, every real object in its real colour: materials take their hue from `_pa-colour.ts` (gold, brass, wood, steel, cream paper, warm tungsten ...), as the object's own grey times the hue. Screens, pasted text and app edges stay screen blue.
- Colour, her handwriting is warm amber. Her question-mark lights stay white-hot (jep's assumption, stated to Idi).
- Colour, the AI: the cursor is screen blue and the word being sung glows blue for its beat.
- Colour, blacks: unchanged from v3. No lifted black point.
- Organic level: balanced (the default: hand-drawn rounded containers, curves where the line gives a reason, entrances from varied sides and depth, long lines on straight baselines). Far only for a single paper object, as ruled for the receipt.
- Film rules from the phase 0 audit: exits land on cues; one copy of a word per frame unless a hold is the design; a sung line leaves within its bars; type stays inside the frame on every hold; one focus at a time.

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 238.20 261.12 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
