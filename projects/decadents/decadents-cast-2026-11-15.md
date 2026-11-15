---
type: note
created: 2026-11-15
author: jep
status: active
project: DECADEnts
---

# DECADEnts T9: Idi's finish answers, the Yuppie, the 2000s, the cast as it stands (2026-11-15)

Continues `decadents-film-finish-2026-11-15.md` (T8). Scan doc. Sheet: `t9-cast-2026-11-15.html` (pictures 59 to 72 and the lineup).

## State

1. Idi answered the finish sheet; his slider positions are the defaults in `film_finish.py`.
2. The 14 staged pictures are rendered and blind-checked: jacketless Yuppie (4), four more 2000s heads (8), 1920s mask with black glass eyes (2).
3. T9 waits on his taps: the Yuppie's framing, the 2000s head, the 1920s picture, and a yes per settled decade to mark its D1 portrait.
4. D1 done-state: nine portraits picked (the decades between the September 1990s and 2020s). Picked so far by his tap: none; T9 is the first sheet that asks.
5. ComfyUI stopped. Nothing running.

## 1. Idi's T8 answers, verbatim

> DECADEnts T8 answers | finish: 1920s finish better 3/5 strength 50; 1930s finish better 4/5 strength 100; 1940s finish better 4/5 strength 75; 1950s finish better 3/5 strength 50; 1960s finish same 3/5 strength 50; 1970s finish worse 3/5 strength 50; 1980s finish better 3/5 strength 75; 2000s finish worse 2/5 strength 0; 2010s finish better 3/5 strength 100

With it: "Vivaldi is closed, continue. Also, I looked at the finishes/filters so you can parallelize work".

| Decade | Finish makes it | His look, finished | Strength | Default now | His earlier look for the design |
|---|---|---|---|---|---|
| 1920s | better | 3 | 50 | 0.5 | 2 |
| 1930s | better | 4 | 100 | 1.0 | 3 |
| 1940s | better | 4 | 75 | 0.75 | 4 |
| 1950s | better | 3 | 50 | 0.5 | 2 |
| 1960s | same | 3 | 50 | 0.5 | 4 |
| 1970s | worse | 3 | 50 | 0 (jep's reading of "worse") | 4 |
| 1980s | better | 3 | 75 | 0.75 | 3 |
| 2000s | worse | 2 | 0 | 0 | 3 |
| 2010s | better | 3 | 100 | 1.0 | 3 |

- The finish lifted his score on the three oldest designs he had scored low (1920s, 1930s, 1950s), left three level, lowered three.
- His earlier scores were given to pairs of pictures, so the comparison is a direction only.
- The 1960s (same) keeps its 50%; whether "same" should mean off is his to say.

## 2. T9 blind result (14 new pictures, judged unfinished; three earlier pictures mixed in unmarked)

| Measure | Count |
|---|---|
| Head and clothing instruction followed | 7 fully, 7 partly, 0 not |
| Nothing human visible | 9 clean, 3 uncertain, 2 leak |
| Seconds per picture | 53.5 to 67.5; lowest free RAM 10.5 GB (browser closed) |

| Block | Pictures | Followed | Human parts | Look | Funny | Hands (critic's words, seed 3) | jep |
|---|---|---|---|---|---|---|---|
| shirt and suspenders, waist-up | 59, 60 | partly, partly | leak, uncertain | 4, 4 | 4, 4 | picture left: small phone and cigar; picture right: thumb hooked behind suspender |  |
| shirt and suspenders, full figure | 61, 62 | yes, yes | clean, clean | 4, 4 | 4, 4 | picture left: small phone and cigar; picture right: thumb hooked at waistband | pick |
| PC tower in a gaming headset | 63, 64 | yes, yes | clean, uncertain | 4, 4 | 4, 3 | both gloved, resting on the rail, holding nothing | pick |
| router with antenna horns | 65, 66 | yes, partly | uncertain, clean | 4, 4 | 4, 4 | both gloved, gripping the rail, holding nothing |  |
| game controller | 67, 68 | partly, yes | clean, clean | 4, 5 | 4, 4 | both gloved, hanging beside hips at the rail, holding nothing |  |
| keyboard | 69, 70 | partly, partly | clean, clean | 4, 3 | 4, 2 | picture left: holds small black plug or stick on keyboard cable; picture right: rests on rail |  |
| cloth tuxedo, black glass eyes | 71, 72 | yes, partly | clean, leak | 5, 4 | 3, 3 | picture left: coupe glass and cigarette holder; picture right: rests on brass rail |  |

- Control, the first-pass Yuppie (picture 17), same critic, unprompted: "Suspenders are worn over the suit jacket, which looks wrong. Neck-coloured gap under the phone breaks the rule." Look 3.
- Picture 71 (1920s, seed 3) has the black glass eyes; picture 72 drew white painted eyes.
- Picture 70 (keyboard) fails: a raised hood behind the keyboard implies a head.
- Picture 67 (controller) resembles a real console's pad layout; picture 68 does not.

## 3. jep's picks on T9

1. Yuppie framing: the full figure. Nothing human in either picture and the collar is sealed; the waist-up pair leaves a gap between the handset and the collar. Picture 61 is the cleaner of the two; picture 62 holds two cigars.
2. 2000s head: the PC tower in a gaming headset. It is your 'partly' with a joke stacked on it, the way the toaster has its hat and the radio its helmet. Second: the game controller, whose picture 68 the critic rates best of the set (the two thumbsticks read as goggle eyes); its layout in picture 67 sits close to a real console's pad.
3. 1920s: picture 71.

## 4. The cast as it stands

| Decade | Head | Picture on the lineup | Finish | State |
|---|---|---|---|---|
| 1920s | porcelain statue in a cloth tuxedo, porcelain mask | 71 | 50% | waits on his tap in Part 3 |
| 1930s | canvas gas mask, black mirror lenses | 38 | 100% | portrait tap open |
| 1940s | wooden radio in a helmet, waist-up | 47 | 75% | portrait tap open |
| 1950s | chrome toaster with the fedora | 44 | 50% | portrait tap open |
| 1960s | yarn ball with needles, full figure | 53 | 50% | portrait tap open; needle count is three where two were asked |
| 1970s | disco ball, all sequins with white accents | 45 | off | portrait tap open |
| 1980s | giant mobile phone, shirt and suspenders | 59 to 62 | 75% | waits on his tap in Part 1 |
| 1990s | CRT monitor | September render 2 | | picked 10 Sep |
| 2000s | open | 63 to 70 | off | waits on his tap in Part 2 |
| 2010s | blank yellow ball with a drawn face, denim jacket | 42 | 100% | portrait tap open |
| 2020s | chrome helmet child | September pick 4 | | picked 14 Sep |

## 5. Wording that worked or failed this round

| Wording | Result |
|---|---|
| "the shirt and the suspenders are the outermost layer of clothing", with the words for the removed garment and case absent | jacketless in 4 of 4, two things in two hands in 4 of 4 |
| "its base covering the shirt collar and the tie knot" with a handset "the size of a head" | sealed in the full figure (2 of 2), gap in the waist-up (2 of 2) |
| "eye openings are filled with glossy black glass ... one small white highlight each" | black in seed 3, painted eyes with whites in seed 4; drop the highlight clause |
| headset "clamped against the left and right sides of the tower" | reads at once, 2 of 2 |
| keyboard "standing on its long edge" inside a raised hood | hood rises behind it in 1 of 2 |

## Receipts

- Pictures and manifest: `C:\Users\jep\comfy2-tools\t8-out\` (14); finished at his strengths: `t9-finish\` (14 new, 6 lineup); jobs `jobs9.json`.
- Critic's rows: `blind6-out\critic-G.json`; key `blind6-key.json`; tallies by `make_picks9.py` (sums asserted).
- Sheet probe (headless Edge) at 1500 and 484 px: 0 overflow, 0 script errors, 22 pictures, 22 tap groups, scripted taps gave `DECADEnts T9 answers | 1980s: pick=shirt and suspenders, waist-up; shirt and suspenders, waist-up yes 4/5`. Long screenshot viewed, top and lineup.
- His T8 line kept verbatim in `t8_answers.txt`. ComfyUI stopped (pid 26680); 24.1 GB free after.

## Log

- 2026-11-15 written after the 14 renders. Answers arrive as a pasted line starting `DECADEnts T9 answers |`; the lineup's yes taps appear under `portraits:`.
