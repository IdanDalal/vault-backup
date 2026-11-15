---
type: note
created: 2026-11-15
author: jep
status: active
project: DECADEnts
---

# DECADEnts T8: Idi's T7 answers, the film finish, staged renders (2026-11-15)

State after Idi's T8 answers and the 14 renders: `decadents-cast-2026-11-15.md`.

Continues `decadents-concepts-2026-11-15.md` (T6 and T7). Scan doc. Sheet: `t8-finish-2026-11-15.html`. Tool: `film_finish.py` (this folder; working copy in `C:\Users\jep\comfy2-tools\`).

## State

1. Idi ruled A on 2026-11-15: the film finish in code. Built, applied to his best picture per decade, blind-tested twice.
2. Result: the finish dates the photograph (7 of 9 to its own decade, both rounds) and costs polish (the critics' look score drops). Whether it lifts Idi's own score is what the T8 taps and sliders measure.
3. Staged, not rendered: 14 pictures from his T7 answers (jacketless Yuppie, four more 2000s heads, the 1920s mask with black eyes). They wait on his word with the browser closed.
4. Nothing running. ComfyUI was not started in this round.

## 1. Idi's T7 answers, verbatim

> DECADEnts T7 answers | 2000s: pick=none, keep looking; energy drink can no 3/5; case-modded PC tower partly 3/5; subwoofer box no 4/5 | 1920s: pick=statue in a cloth tuxedo; statue, all porcelain partly 3/5; statue in a cloth tuxedo yes 2/5 | 1930s: black mirror lenses yes 3/5 | 2010s: pick=drawn face, denim jacket; drawn face, hoodie partly 3/5; drawn face, denim jacket yes 3/5 | 1950s: toaster with the hat (kept) yes 2/5 | 1970s: all sequins, white accents (kept) yes 4/5 | 1940s-2: pick=radio, waist-up, fixed; radio, waist-up, fixed yes 4/5; radio, full figure same 3/5 | 1960s-2: pick=yarn ball, full figure; yarn ball, waist-up, period print same 4/5; yarn ball, full figure same 4/5 | 1980s-2: mobile phone, waist-up, fixed no 2/5; mobile phone, full figure no 2/5 | note=Regarding the Yuppie: no execution looks good. Can't hold 3 things (suitcase, phone, cigar) at once. Can't have suspenders above jacket - in fact, shouldn't have a jacket at all.

With it: "A sounds good. Also:" and the line above.

| Decade | His answer | What it decides |
|---|---|---|
| 1920s | pick = statue in a cloth tuxedo (yes, 2/5); all porcelain partly 3/5 | his reading overrules jep's pick; execution is the open part |
| 1930s | black mirror lenses yes, 3/5 | head settled |
| 1940s | radio waist-up fixed: better, 4/5; full figure same, 3/5 | waist-up carries the Soldier |
| 1950s | toaster with the hat yes, 2/5 | head settled, look low |
| 1960s | pick = full figure; both framings same, 4/5 | full figure carries the Hippie Grandma |
| 1970s | all sequins, white accents yes, 4/5 | head and look settled |
| 1980s | both second passes no, 2/5; his note | no accepted picture: no jacket, two hands for two things |
| 2000s | pick = none, keep looking; PC tower partly 3/5; energy can no 3/5; subwoofer no 4/5 | head still open |
| 2010s | pick = denim jacket (yes, 3/5); hoodie partly 3/5 | denim carries the Influencer |

His note, verbatim: "Regarding the Yuppie: no execution looks good. Can't hold 3 things (suitcase, phone, cigar) at once. Can't have suspenders above jacket - in fact, shouldn't have a jacket at all."

jep's picks he overruled or declined: 1920s all porcelain (he chose the cloth tuxedo), 2000s PC tower (partly), radio full figure (he chose waist-up), phone waist-up fixed (no).

## 2. The film finish

| Decade | Shown on | Recipe |
|---|---|---|
| 1920s | picture 36 | Silent-film still: orthochromatic grey, glowing highlights, coarse grain, dark corners, dust and scratches. |
| 1930s | picture 38 | Large-format documentary print: full grey scale, soft corners, fine grain, a few specks, silver-warm paper. |
| 1940s | picture 47 | Kodachrome slide: dense blacks, heavy reds, cool shadows, soft lens, visible grain, slight colour misregister. |
| 1950s | picture 44 | Kodachrome advertising page: dense saturated colour, highlight glow, warm cast, fine grain. |
| 1960s | picture 53 | Faded Ektachrome snapshot: lifted blacks, magenta-red drift, soft lens, grain, an orange light leak. |
| 1970s | picture 45 | Drugstore colour print: yellowed, low black density, green-cyan shadows, soft, grainy. A light touch; this picture already had its print. |
| 1980s | picture 17 | Compact-camera flash print: hot centre, falloff, saturated warm colour, reddish blacks, a burned-in orange date. |
| 2000s | picture 30 | Early digital compact: clipped highlights, over-sharpened edges, purple fringe, blotchy colour noise, JPEG blocks. |
| 2010s | picture 42 | Phone photo through a 2015 filter: milky blacks, teal shadows, warm highlights, dark corners. |

- Run one: `python_embeded/python.exe -I film_finish.py <decade> <in.jpg> <out.jpg> [strength 0..1]`.
- Run many: `python_embeded/python.exe -I film_finish.py --batch jobs8.json` (3.2 s for nine pictures).
- Same pixel size out as in; grain seeded from the file name, so a rerun reproduces the file.
- A white print border inside the picture is detected and kept as tinted paper, free of grain and blur.
- Python: the second ComfyUI's (`C:\Users\jep\comfy2\ComfyUI_windows_portable\python_embeded\python.exe`), for Pillow and numpy. No GPU, no model.

## 3. Blind test (a critic who never saw the code; originals and finished shuffled; each photograph dated before the target was known)

| Measure | Round 1 (first recipes) | Round 2 (after one tuning pass, the version delivered) |
|---|---|---|
| Originals dated to their own decade | 1 of 9 | 3 of 9 |
| Finished dated to their own decade | 7 of 9 | 7 of 9 |
| Period feel, 1 to 5, original to finished | 2.00 to 3.89 | 2.33 to 3.67 |
| Finished judged "laid on afterwards": yes, unsure, no | 2, 6, 1 | 4, 3, 2 |
| Critic's look, original to finished | 4.00 to 3.67 | 4.00 to 3.22 |

Each round had its own critic, so the rounds differ by judge as well as by recipe. The tuning pass did not raise the scores. Both rounds miss the same two: the 1950s reads as 1960s, the 1960s reads as 1970s.

Round 2 per decade:

| Decade | Dated as: original, finished | Period | Laid on | Look | Critic's note on the finished picture |
|---|---|---|---|---|---|
| 1920s | 2020s, 1920s | 2 to 3 | yes | 4 to 3 | Soft focus, heavy grain and low contrast suit the era. White dust, scratch line and rounded frame look like stock overlay. |
| 1930s | 2020s, 1930s | 2 to 4 | unsure | 4 to 4 | Soft tonal range, grain, edge falloff and specks pass. Grain is a little even and fine detail still slightly crisp. |
| 1940s | 2020s, 1940s | 1 to 3 | yes | 4 to 3 | Rich warm dyes and softness help. Coarse even grain is wrong for 1940s colour slide film and reads as overlay. |
| 1950s | 2010s, 1960s | 2 to 4 | no | 4 to 4 | Highlight glow, gentle softness, warm faded dyes and fine grain feel like real colour film, perhaps a decade late. |
| 1960s | 2020s, 1970s | 2 to 3 | yes | 4 to 3 | Faded dyes and cream border help, reads later than 1960s. Even haze and uniform grain sit on top like a wash. |
| 1970s | 1970s, 1970s | 3 to 4 | unsure | 4 to 3 | Lifted blacks, soft detail, grain and bordered print pass well. Fade is very even, no colour shift toward magenta or yellow. |
| 1980s | 2020s, 1980s | 2 to 4 | no | 4 to 4 | Orange date stamp, hard flash, red bloom, grain and soft lens match a compact camera print. Grain slightly even. |
| 2000s | 2000s, 2000s | 3 to 4 | unsure | 4 to 2 | Sharpening halos, blocky compression and crushed tones match an early digicam. Halos are heavy enough to look reprocessed. |
| 2010s | 2010s, 2010s | 4 to 4 | yes | 4 to 3 | Matte blacks, warm fade, fake grain and vignette are a phone filter, which is true to the 2010s. |

## 4. Next tuning, from the two critics (not done)

| Finding | Seen in | Direction |
|---|---|---|
| Grain is even and reads as an overlay | 1940s, 1960s, 1930s, 1980s, both rounds | clumped grain that varies with density, finer for colour slide stock |
| 1950s and 1960s read a decade late | both rounds | 1950s: denser dyes, no fade; 1960s: less magenta drift, a square or 4:3 crop |
| Dust and scratch look like stock overlay | 1920s, 1930s | fewer, softer, irregular |
| Sharpening halos heavy | 2000s (look 4 to 2) | halve the unsharp amount |
| Fade very even | 1970s | add a yellow or magenta shift across the frame |

Idi's slider positions come first: they say how much finish he wants before any of this is tuned.

## 5. Staged renders (wait on Idi's word, browser closed)

| Block | Picture brief | Why |
|---|---|---|
| shirt and suspenders, waist-up | a giant early 1980s mobile phone handset the size of a head, grey slab, rubber antenna, keypad facing the camera, its base covering the shirt collar; the figure wears a shirt and suspenders as the outer layer | Your note applied: the shirt and the suspenders are the outer layer. One hand holds the phone and the cigar, the other hooks a thumb behind a suspender. |
| shirt and suspenders, full figure | a giant early 1980s mobile phone handset the size of a head, grey slab, rubber antenna, keypad facing the camera, its base covering the shirt collar; the figure wears a shirt and suspenders as the outer layer | The same in a tall frame: two hands, two jobs. Phone and cigar in one, the other thumb behind a suspender. |
| PC tower in a gaming headset | a black desktop PC tower with a glowing green side window and an open disc tray, wearing a chunky black gaming headset with a boom microphone | Your 'partly', with the stacked joke the toaster and the radio have: the rig wears the headset. The voice-chat trash-talker. |
| router with antenna horns | a black Wi-Fi router standing upright, a row of small green lights across its front, two thick black antennas rising from its top corners | Always online. Two antennas for horns, and a row of green lights that blink when he talks. |
| game controller | a giant black game controller of an invented design, upright, two round thumbsticks side by side, a cross pad, four coloured buttons, grips pointing down | Thumbsticks that can roll and buttons that mash when he rages. An invented design, no real console. |
| keyboard | a black computer keyboard as wide as the shoulders, standing on its long edge, keys facing the camera, a few keys missing, four red keys | The keyboard warrior, literally. Keys missing from rage. |
| cloth tuxedo, black glass eyes | a porcelain statue (blank white porcelain head and porcelain hands) in a real cloth tuxedo, wearing a black and gold porcelain mask whose two eye openings are filled with black glass | Your pick, with the one defect fixed: black glass in the mask's eye openings, the same rule as the 1930s lenses. |

- Prompts: `C:\Users\jep\comfy2-tools\t8_prompts.json` (7 prompts, 2 seeds each, 14 pictures, about 14 minutes).
- Run: start ComfyUI with the two flags, then `python -I t4_run.py hy3 t8_prompts.json t8-out 3,4`, then stop ComfyUI.
- The prompts leave out the words for what he removed (the outer garment, the case): naming a thing draws it.
- On the sheet he can tap skip per block; untouched means render.

## 6. Cast status

| Decade | Head | Status | His last look score |
|---|---|---|---|
| 1920s | porcelain statue in a cloth tuxedo, porcelain mask | his pick; black mask eyes staged | 2 |
| 1930s | canvas gas mask, black mirror lenses | settled | 3 |
| 1940s | wooden radio in a helmet, waist-up | settled | 4 |
| 1950s | chrome toaster with the fedora | settled | 2 |
| 1960s | yarn ball with needles, full figure | settled | 4 |
| 1970s | disco ball, all sequins with white accents | settled | 4 |
| 1980s | giant mobile phone | head settled; no accepted picture; jacketless render staged | 2 |
| 1990s | CRT monitor | done in September | |
| 2000s | open | four more heads staged | |
| 2010s | blank yellow ball with a drawn face, denim jacket | settled | 3 |
| 2020s | chrome helmet child | done in September | |

## Receipts

- Tool: `film_finish.py`; jobs: `jobs8.json`; finished pictures: `C:\Users\jep\comfy2-tools\t8-finish\`.
- Critics' rows: `blind5-out\critic-E.json` (round 1), `critic-F.json` (round 2); keys `blind5-key.json`, `blind5-key-F.json`; tallies by `make_picks8.py`.
- Sheet probe (headless Edge) at 1500 and 484 px: 0 overflow, 0 script errors, 9 stacks with 0 misaligned, slider at 70 set opacity 0.7, scripted taps gave `DECADEnts T8 answers | finish: 1920s finish better 4/5 strength 70 | staged yuppie: shirt and suspenders, waist-up skip`. Screenshots viewed.
- His T7 line kept verbatim in `t7_answers.txt`.

## Log

- 2026-11-15 written after Idi's ruling A and his T7 answers. Answers arrive as a pasted line starting `DECADEnts T8 answers |`.
