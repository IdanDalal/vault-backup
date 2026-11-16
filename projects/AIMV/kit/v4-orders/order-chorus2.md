---
type: brief
created: 2026-11-16
author: jep
---

# v4 work order: chorus2 (2:18.5-2:42.7, 24.2 s)

Scene file `app/src/scenes/chorus2.ts`. Shared kits (`_pa.ts`, `_pa-lens.ts`, the phase 1 text and organic kits) are read-only for the builder. State: `briefs/v4/queue.json` (one row per id below; one item = one commit).

## 1. Idi's answers in the room

| id | at | size | proposal | what to do | his verdict |
|---|---|---|---|---|---|
| chorus2-s01 | 2:29.9 | small | Remove the stray grey blade and sliver | The grey blade that crosses from the left edge at 2:29.8 to 2:30.1 goes, and so does the pale grey sliver on the dish's left edge from 2:31.7 to 2:36. Why: Neither has a visible source. Both carry the receipt's paper texture, so they look like a leftover piece of the fallen receipt drawn in the wrong place. | Do it |
| chorus2-s02 | 2:19.9 | small | Show the sale when the key is pressed | When the cursor reaches the fast-forward key on 'skip', the key lights for a beat and the receipt's 1 SKIP row prints at that moment. Why: The planned picture is a button for sale. In the frames the cursor slips behind the key and nothing marks a purchase, so the shop reads only through the receipt. | Do it |
| chorus2-s03 | 2:28.8 | medium | Give the dark slide something to pass | During the 3 second slide along the counter the camera passes more tags for other paid shortcuts, each lit for a moment as it goes by. Why: From 2:28.6 to 2:30.4 the frame holds an unlit card and a faint ring. It is the emptiest stretch of the plate. | Do it |
| chorus2-s04 | 2:35.0 | medium | Move closer while the apps eat YOU | The camera pushes in on the pie's centre across the two 'more's so YOU, OU, U fills a quarter of the frame. Why: The centre hole is about a ninth of the frame's width and the straps are smaller still. The builder lists this moment as one that may read as smudges. | Do it |
| chorus2-s05 | 2:34.0 | small | Keep the pie's labels upright and larger | SLEEP, STUDY and FRIENDS stay readable from the viewer's side as the pie turns, at a larger size, until their slices are nearly gone. Why: At 2:35 FRIENDS is upside-down and STUDY is on its side, both small. These three words say what the apps are eating. | Do it |

## 3. Film-level items that land here

- `film-s01` Lens effects, plate by plate: Each plate gets a short list of lens events: focus pulls, flare, glow, colour fringing, a wide-angle bulge, a kick on the beat. Each one has a cause on screen and a short window, and the base look returns after it. The clock in the corner stays clean. This plate's events are listed under it.
  - 2:21.9, ca: the tag passes edge-on as it flips to TWICE
  - 2:23.4, bloom: the ONCE stamp flashes white
  - 2:30.4-2:32.6, bloom + flare: the glass letters of ATTENTION fill with light
  - 2:37.9-2:40.0, exposure: the ? turns white-hot and lights the counter
  - 2:40.0-2:42.7, fov: the dive onto the coin's dot
- `film-s05` A camera that rests less: More travel between holds across the film: longer pushes, more rides like the hook ride at 1:38. This plate in v3: camera still 59 % of the time, 7.9 moves per 10 s, 27 reversals (film 60.8 %, 4.4; reference films 30-40 %, 4.9-6.9).
- `film-s04` colour and `film-s07` blue beyond screens: ruled on the phase 1 decision page, then applied here.

## 4. Efficiency (Idi's note 1): flags from v3

Engine data, 0 tokens: candidates until an eye confirms. A draw can be hidden behind another object; the capture holds boxes, not alpha.

**Lead's rulings (these are the order):**

- `chorus2-e01` The opening's credit block scrolls off the receipt as the first chorus line prints. It rides for 10 s (2:18.6-2:28.7) and is a third reading of the same rows (open 2 s, here 10 s, outro 9 s). Basis: audit dwell strings + cross-plate texts.
- `chorus2-e02` The FREE to TWICE flip gets its own beat (today it lands in the frame where BILL YOU prints), and the TWICE tag reacts or leaves (unchanged 2:21.5-2:28.0). Basis: critic A two-focus (med), dwell (med).
- `chorus2-e03` The fractions sheet enters after the line lands and clear of the receipt: at 2:24-2:27 it is the brightest thing in frame while the lyric prints, with its title half hidden ("RACTIONS"). Basis: critic A two-focus (med), stray (med).
- `chorus2-e04` The wheel: the dark disc waits out of frame until its cue (it pokes in at 2:32.0 for 2.5 s), YOU at the hub reads whole and once (2:34-2:35), the empty ring leaves with its PAY ATTENTION token (it stays 4.5 s, 2:37.5-2:41.5). Basis: critic B stray x3 (med).
- `chorus2-e05` The receipt prints in rhythm: `1 SKIP` (2:23.9) and `price?` (2:26.4) appear with no cue; 2 of 7 in-place entries sit on a music cue (chance 48 %). Basis: audit events.

- dwell, object `skip-key`: 2:18.6-2:28.8 = 10.2 s, motionless 53 % of it, up to 0.9 % of the frame
- dwell, object `micro:credit-KEEP IT`: 2:18.6-2:28.6 = 10.1 s, motionless 41 % of it, up to 0.7 % of the frame
- dwell, object `micro:credit-PRICE`: 2:18.6-2:26.7 = 8.1 s, motionless 43 % of it, up to 0.7 % of the frame
- dwell, lyric line 39 ("They’ll sell you ways ..."): 13 words stay 6.5-9.5 s after they are sung (leave 2:28.8)
- repeat, "attention": 2:18.6-2:28.6, up to 2 on screen at once (ATTENTION 5:00 / PAY ATTENTION)
- entries in place: 6, 1 on a music cue (17 %; chance 48 %)

Blind critic (2 fps sheets, saw nothing but frames):

- 2:18.5-2:22.0 TWO-FOCUS (med): the lyric prints on a bright receipt at left; a white-outlined "FREE" tag on a stand with a sign above it sits at the right [left-centre vs right]
- 2:18.5-2:27.0 DWELL (low): the receipt's header block (title, artist, made by, price, keep it) stays for 18 frames, cut by the top edge from 140.5 to 144.5 s [top of the receipt]
- 2:21.5-2:21.5 TWO-FOCUS (med): the tag flips from "FREE" to "TWICE" in the same frame where the receipt prints "BILL YOU" [receipt vs tag]
- 2:21.5-2:28.0 DWELL (med): the "TWICE" tag stays unchanged for 14 frames [right, on the stand]
- 2:23.5-2:23.5 STRAY (low): a short bright white bar, this frame only [top edge, above the receipt]
- 2:24.0-2:27.0 TWO-FOCUS (med): a second sheet, pure white, appears beside the grey receipt and is the brightest thing in frame while the lyric is still printing on the receipt; a bare bulb also appears above [centre, right of the receipt]
- 2:24.0-2:28.0 STRAY (med): the white sheet's title is half hidden by the receipt ("RACTIONS") [centre, behind the receipt]
- 2:28.5-2:29.5 STRAY (low): a dark rectangle hanging from the top-right, an ellipse outline on the floor cut by the right edge, and at 149.5 s a grey sliver entering from the left edge; nothing to read [right edge and left edge]
- 2:32.0-2:34.5 STRAY (med): a dark disc pokes in from the corner, cut by the frame edge, for 2.5 s before anything uses it [bottom-right corner]
- 2:34.0-2:35.0 STRAY (med): the word "YOU" at the hub is half covered (reads "OU" or "DU"); at 155.0 a second "YOU" shows at the bottom of the wheel in the same frame [hub of the wheel]
- 2:35.5-2:35.5 STRAY (low): one small blue square alone, far from the wheel [top-left]
- 2:37.5-2:41.5 STRAY (med): a large empty ring stays after the "PAY ATTENTION" token has left it; nothing inside it for 4.5 s [top-left]
- 2:38.5-2:41.5 TWO-FOCUS (med): lyric block lower-left, glowing question mark with a second lyric block at right, empty ring top-left: three areas far apart [lower-left vs right]
- 2:42.0-2:42.0 STRAY (low): lower-left lyric block cut by the left frame edge ("T ON A") during the zoom [left edge]

## 5. Less rigid (Idi's note 3): this plate's reading

| measure | this plate | v3 film | What Counts | P(Doom) | Simulation's Ending |
|---|---|---|---|---|---|
| edges lying flat or upright (11 % = no preference) | 40 % | 39 % | 31 % | 28 % | 36 % |
| edge length on long straight lines | 22 % | 34 % | 24 % | 25 % | 30 % |
| hard corners per 1000 edge pixels | 0.09 | 0.28 | 0.06 | 0.08 | 0.19 |

Reading checked once against blind eyes: v3 frames the critics called RIGID read 37 % straight and 40 % flat-or-upright, frames they called ORGANIC 29 % and 30 %. Direction of travel toward the two parity films; the stills of phase 1 decide, the number shows how far the plate moved.

- lyric words (engine data): 27 % appear in place, 51 % travel in along a main direction, 22 % diagonally; the next word sits to the right of the last one 41 % of the time, below it 22 %
- tracked boxes drawn rotated or in perspective: 2.5 % (film 1.4 %)
- blind critic, RIGID 2:18.5-2:27.0 (med): an upright strip of paper with monospace rows, an upright tag on an upright stand, a squared sign above it
- blind critic, ORGANIC 2:27.0-2:28.0 (med): the receipt tips over and falls flat on a diagonal
- blind critic, ORGANIC 2:32.5-2:39.5 (high): round wheel with text bent around its rim, wedges filling, token spinning inside rings, a brush-drawn question mark
- levers (plan section 7): lyric on curved paths, rounded and hand-drawn containers, more of her handwriting, entrances from every side and from depth, curves for cords, trails and smoke, camera arcs, eased drift. Which ones this plate takes is set after the phase 1 look tests.

## 6. Text effects (Idi's note 2): placements and his rulings

- neon at 2:18 the shop that bills twice (or games, one of the two). Reason in the line: a sign that sells. **BUILD (R36). The film's one neon sign. Kit `neonText`; worked example window neon-shop.**
- geometry at 2:32 the pie chart (exists). Reason in the line: her homework. **Exists in v3; keep.**
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
- `gates-window.sh 138.54 162.74 <name> all` passes: sung words lit, 0 flashes, 0 brightness jumps
- `audit.py` re-run on the new build: this plate's section 4 rows are gone or ruled kept
- seams with both neighbours checked at 30 fps; a blind critic round on 8 fps sheets; the lead's eye on every window
