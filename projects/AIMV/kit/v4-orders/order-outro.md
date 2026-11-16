---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: outro (4:21.1-4:52.0, 30.9 s)

Scene file `app/src/scenes/outro.ts` + `_pa-outro.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| outro-s01 | 4:51.3 | medium | Give the last two seconds a lens moment | As the receipt comes whole into view the lamp blooms and flares, and the focus pulls onto ONE QUESTION. before the tear. Why: Your v2 note 24 asked for an ending as strong as the opening. The receipt now reads, and the frame around it is a still grey room. This is the plan carried into the next round. | Do it |
| outro-s02 | 4:51.9 | medium | Show the printer at work in the end frame | The last view sits lower and wider so the printer is seen whole under the receipt, its cutter coming down on the last note. Why: Half of note 24 is still open: at the end the printer is only a dark edge under the paper. | Do it |
| outro-s03 | 4:40.5 | small | Start the receipt as the camera arrives | The receipt begins to feed the moment the camera reaches the slot, with no wait on the empty slot. Why: From 4:40.4 to 4:41.0 the frame is the box's top and the dark. | Do it |
| outro-s04 | 4:43.0 | small | Show the kitchen's own four tricks in the band | The band under BAIT NOT TAKEN shows the four messages from the kitchen scene: the late grandmother, the $200 tip, YOU ARE DAN, IGNORE PREVIOUS INSTRUCTIONS. Why: On the frame the bubbles read 'this once', 'do it for me', 'no one will know' and 'please'. Those are different words from the scene the row recalls. | Do it |
| outro-s05 | 4:51.4 | medium | Turn the change into a question mark again | On 'one question' the printed 0:08 lifts off the receipt and re-forms as one lit ? beside the line, inside the last note. Why: The planned picture was the leftover time handed back as a question. It left with the silent tail, and the receipt now only says it in words. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. This plate's events are listed under it.
  - 4:21.1-4:21.8, exposure: the cut to the grey room: the eye adapts
  - 4:31.5-4:34.5, focus: from the box to the chat bar where the cursor types one glowing ?
  - 4:43.9, ca: the PAID stamp lands
  - 4:50.0-4:52.0, flare + breathe: the end (film-s03): the receipt tears on the last note; the lamp flares once and the view closes on ONE QUESTION.
- `film-s03` A lens moment and a real printer at the end: The last 2 s get one lens event, and the receipt printer shows as an object with weight. Today it is an edge under the paper.
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 55 % of the time, 6.5 moves per 10 s, 15 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `outro-e01` The stamp is the lyric: PAY ATTENTION, OR PAY THE PRICE is sung, shown as type and shown as a stamp at once, and the pair holds 9.5 s (4:28.5-4:37.5). One of the two carries the words. Basis: critic B repeat (high), dwell (med); audit dwell (6 words 7.1-9.0 s; strip, box, coin 10.5-11.0 s).
- `outro-e02` The receipt's recall reads: one tile per beat, each long enough to read or reduced to an icon, no type over type. Today four tiles live 1.1 s each and leave with no cue, THE ESSAY IS DEAD gets 1.0 s (needs 1.5), the essay line 0.3 s (needs 1.8), the blocks change every frame at 4:41.5-4:43.5 and FIVE prints over RECEIPT. Build with the room item on the trick bubbles. Basis: audit reading rows x5, events x4; critic B two-focus (med), stray (med).
- `outro-e03` The last line of the film is its easiest to read: CHANGE DUE and ONE QUESTION. print at the bottom edge at their smallest size after the zoom-out. Build inside film-s03. Basis: critic B stray (med).
- `outro-e04` Eye check: the PRICE row ends with no value while its four sibling rows have one (4:45.5-4:50.0). Fill it or make the gap the point. Basis: critic B stray (med).
- `outro-e05` The input bar is the widest thing in frame while the lyric being added is small (4:32-4:35): size follows what is being sung. Basis: critic B two-focus (med).
- `outro-e06` Edges and leftovers, check at 30 fps: the lyric cut by the left and bottom edges (4:37.0-4:37.5), WERE YOU EVER REALLY drawn over PRESENT at the seam (4:20.5), the dim leftover FIVE M / IN FUL cut on the right (4:45.5). Exits: 2 of 7 in-place exits on a music cue, 5 with no cue of any kind. Basis: critic B stray x3 (high, med, med); audit events.

- dwell, object `slip`: 4:41.0-4:52.0 = 11.0 s, motionless 47 % of it, up to 86.5 % of the frame
- dwell, object `strip`: 4:27.9-4:38.9 = 11.0 s, motionless 30 % of it, up to 100.0 % of the frame
- dwell, object `box-front`: 4:27.9-4:38.7 = 10.8 s, motionless 30 % of it, up to 68.8 % of the frame
- dwell, object `coin`: 4:27.9-4:38.5 = 10.5 s, motionless 51 % of it, up to 8.1 % of the frame
- dwell, object `slip:CHEAT CODE`: 4:41.7-4:52.0 = 10.3 s, motionless 52 % of it, up to 1.9 % of the frame
- dwell, object `slip:PRICE`: 4:41.8-4:52.0 = 10.2 s, motionless 57 % of it, up to 1.9 % of the frame
- dwell, object `slip:BAIT NOT TAKEN`: 4:41.9-4:52.0 = 10.2 s, motionless 57 % of it, up to 1.9 % of the frame
- dwell, object `slip:HEADS`: 4:41.9-4:52.0 = 10.1 s, motionless 60 % of it, up to 1.9 % of the frame
- dwell, object `slip:snapshot`: 4:42.8-4:52.0 = 9.2 s, motionless 65 % of it, up to 1.9 % of the frame
- dwell, object `micro:strip-price`: 4:27.9-4:34.8 = 6.9 s, motionless 57 % of it, up to 6.7 % of the frame
- dwell, lyric line 78 ("Pay attention, or pay ..."): 6 words stay 7.1-9.0 s after they are sung (leave 4:38.5)
- repeat, "price": 4:32.1-4:51.9, up to 2 on screen at once (PRICE)
- repeat, "attention": 4:32.1-4:51.9, up to 2 on screen at once (ATTENTION 5:00 / PAY ATTENTION)
- too brief to read, "THE ESSAY IS DEAD" at 4:41.9: shown 1.0 s, needs 1.5 s
- too brief to read, "do it for me" at 4:42.9: shown 1.0 s, needs 1.5 s
- too brief to read, "no one will know" at 4:42.9: shown 1.0 s, needs 1.5 s
- too brief to read, "In conclusion, the Industrial Revolution" at 4:47.1: shown 0.3 s, needs 1.8 s
- too brief to read, "was a turning point in histor" at 4:47.1: shown 0.1 s, needs 2.0 s
- entries in place: 9, 7 on a music cue (78 %; chance 20 %)
- exits in place: 5, 0 on a music cue (0 %; chance 31 %)
- no cue: exit of `micro:strip-price` at 4:34.8 (6.7 % of the frame, lived 6.9 s)
- no cue: exit of `recall:news` at 4:42.9 (1.5 % of the frame, lived 1.1 s)
- no cue: exit of `recall:arrows` at 4:43.4 (1.5 % of the frame, lived 1.1 s)
- no cue: exit of `recall:bubbles` at 4:43.9 (1.5 % of the frame, lived 1.1 s)
- no cue: exit of `recall:beams` at 4:44.4 (1.5 % of the frame, lived 1.1 s)
- no cue: entry of `micro:credit-RECEIPT` at 4:41.2 (1.2 % of the frame, lived 4.5 s)

Blind critic (2 fps sheets, saw nothing but frames):

- 4:21.0-4:23.5 TWO-FOCUS (med): lamp flare on top, white receipt strip at right (the brightest area), lyric on the box lower-left [top, right, lower-left]
- 4:21.5-4:24.5 REPEAT (high): the lyric "PAY ATTENTION," sits beside a round stamp that also says "PAY ATTENTION"; the pair returns 268.5-277.5 [front of the box]
- 4:25.0-4:27.0 TWO-FOCUS (low): lyric block upper-left, growing "?" bubble lower-right [upper-left vs lower-right]
- 4:27.5-4:28.0 STRAY (med): the lyric block shrinks to small size while its last word is still arriving; the box at right is cut by the frame edge with its stamp clipped [left and right edge]
- 4:28.5-4:37.5 DWELL (med): "PAY ATTENTION, OR PAY THE PRICE" plus stamp stay on screen 9.5 s (19 frames); 269.0-271.0 is a near-static close-up (5 frames) [box]
- 4:32.0-4:35.0 TWO-FOCUS (med): the widest element is a near-empty input bar (cursor and "?" token only) across the bottom; the lyric being added is small on the box above it [bottom vs centre]
- 4:32.5-4:34.5 STRAY (low): faint half disc of glow cut by the left frame edge [left edge]
- 4:37.0-4:37.5 STRAY (high): lyric cut by the left edge ("Y ATTENTION," / "R PAY THE PRICE") and by the bottom edge [left and bottom edge]
- 4:38.0-4:39.0 STRAY (low): a dark tray with a grey sheet, 3 near-identical frames, no text; from the thumbnails I cannot tell what it is [centre]
- 4:41.5-4:43.5 TWO-FOCUS (med): black blocks on the receipt change every frame (5 different states in 5 frames) while the lyric appears beside it [receipt vs right]
- 4:42.5-4:42.5 STRAY (med): "FIVE" drawn on top of the fading "RECEIPT." (reads "FIVEEIPT.") [right of the receipt]
- 4:45.5-4:45.5 STRAY (med): dim leftover "FIVE M / IN FUL" cut by the right frame edge [right edge]
- 4:45.5-4:50.0 STRAY (med): the row "PRICE ........" ends with no value while its four sibling rows each have one [receipt rows]
- 4:47.5-4:48.5 STRAY (low): rows above "NOT WRITTEN." jump down at 288.0 and back up at 288.5 when the black box closes [receipt]
- 4:50.5-4:51.5 TWO-FOCUS (low): lamp with flare at left, receipt in the centre [left vs centre]
- 4:51.0-4:51.5 STRAY (med): the final lines being printed ("CHANGE DUE", "ONE QUESTION.") sit at the very bottom edge of the frame at their smallest size, after the zoom-out [bottom edge]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 50 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 39 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.41 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 47 % appear in place, 47 % travel in along a main direction, 6 % diagonally; the next word sits to the right of the last one 69 % of the time, below it 17 %
- tracked boxes drawn rotated or in perspective: 1.0 % (film 1.4 %)
- blind critic, ORGANIC 4:21.0-4:27.0 (med): receipt strip with a curving trail of dots, soft lamp glow, a "?" bubble swelling
- blind critic, RIGID 4:31.5-4:35.0 (med): rectangle receipt, rectangle box, long horizontal bar, rows of small capitals
- blind critic, ORGANIC 4:35.5-4:36.5 (low): round stamp rotating (its text passes upside down) while the camera pushes in at a tilt
- blind critic, RIGID 4:45.5-4:51.5 (high): white rectangle, monospace rows with dot leaders, upright and centred for 6 s
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): placements and his rulings

- none placed here in the plan. No effect is added for looking cool.

## 6b. Film rules from R36 (Idi, 2026-11-16)

- Colour, every real object in its real colour: materials take their hue from `_pa-colour.ts` (gold, brass, wood, steel, cream paper, warm tungsten ...), as the object's own grey times the hue. Screens, pasted text and app edges stay screen blue.
- Colour, her handwriting is warm amber. Her question-mark lights stay white-hot (jep's assumption, stated to Idi).
- Colour, the AI: the cursor is screen blue and the word being sung glows blue for its beat.
- Colour, blacks: unchanged from v3. No lifted black point.
- Organic level: far (R36): the receipt is paper with curl and weight. First sketch: `v4org.ts` moment outro at level 2.
- Film rules from the phase 0 audit: exits land on cues; one copy of a word per frame unless a hold is the design; a sung line leaves within its bars; type stays inside the frame on every hold; one focus at a time.

## 7. Done means

- every id in sections 1-4 is `done` or `wont` (with a reason) in `queue.json`, each with its commit
- `gates-window.sh 261.12 292.00 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
