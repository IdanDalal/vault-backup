---
type: project
created: 2026-11-04
author: jep
status: active
---

# "Pay Attention" proof: R30 defects fixed

Verdict: all 4 named R30 defects fixed, plus 9 more from the lead's frame sweep and 6 from a blind critic; every fix eyed at 30 fps on the final render; all gates hold. Watch: `D:\work\AIMVs\ours\pa-song\proof\p2-proof-fix-0m52-1m21.mp4` (song 52.3-81.6 s; the R30 cut stays beside it for comparison). Follows [[handoff-2026-11-04-pay-attention-plates]] section 2; rulings in [[kit-next-video]].

## 1. Idi's R30 list

| # | Idi's words | cause (verified in code) | fix | verified at |
|---|---|---|---|---|
| 1 | vertical line disappearing at ~00:03 | the scale's post is the cursor, switched to idle blink at the end of "late": off in 1 frame at 56.0 | post stays solid while the scale is in frame | 55.85-56.48, 30 fps |
| 2 | stuck circle at ~00:05, clips over the tunnel ~10 s | the unlit far point drawn LAST, at the vanishing point the camera flies at: never moves, over every desk 57-69 s | drawn first (behind rings, stream, desks); shown only in the drain, from 66.7 s | 57-69 s, 8 fps; full frames 58.7, 62.5 |
| 3 | confusing/clipping transitions | 8 separate causes, rows 3a-3h in section 2 | each fixed | per row |
| 4 | bright light spawning at full brightness | lamp on in 3 frames at 69.08 | ignition: strike on the downbeat, 2 flickers, full by +0.45 s, bloom grows with it | 69.05-69.55 |
| 5 | "and others" | lead sweep (12 grids at 8 fps, 5 seams at 30 fps) + blind critic | section 2 | |

## 2. Everything else fixed

| row | song time | defect | fix |
|---|---|---|---|
| 3a | 57.05 | LATE + ? drawn over the first desk | fall behind the desks once the tilt lands |
| 3b | 57.4-67.2 | blue stream's near end swept the whole frame like a searchlight; its glow drew over desks | near end fades from 700 units ahead; glow pass removed |
| 3c | 58.2, 61.4, 62.7, 63.8, 67.05 | desks dissolved behind a hard vertical clip slicing letters | soft-edged dissolve (each desk drawn offscreen, gradient mask) |
| 3d | 67.4-68.4 | a near ring's arc sat still at the frame edge while the camera landed | rings go out with the room light in the drain |
| 3e | 71.15 | ATTENTION dropped to a ghost in 1 frame: the push read as a cut | words fly out past the frame first, fade after |
| 3f | 71.1-71.3 (critic) | push missed the O: the O slid off while the eye moved to centre | the O travels with the eye; eye stays in the counter |
| 3g | 73.3, 74.3 | iris letters collided ("TT"), word broke at the ring's seam ("TIOA") | letter count at the glyphs' inner end, whole words per ring |
| 3h | 76.15-76.22 | turn = 2D squash through edge-on: card flip; L21 words squashed to a sliver | turn = a pan (a 180-degree yaw): eye's face out left, view out in from the right, same beat |
| 3i | 77.83 (critic) | window wiped the iris in 2 frames | view out grows with the window: iris passes round the camera |
| 3j | 78.05 | hand of ? tripled, screens doubled: glow layer unclipped under the window | glow clipped to the pupil; inside view hands the room to the window |
| 3k | 78.13 | room key light, dim, chair, desk gap all in 1 frame; hand jumped right | each eased over 0.35-0.65 s; hand slides |
| 3l | 78.05-79.30 (critic) | hand cut by the top edge | hand set deeper in the room |
| 3m | 79.40 (critic) | hand vanished bright | hand and its lights fade with its height |
| 3n | 55.98 (critic) | ?'s halo died as it left the pan | its light falls with it |

## 3. Critic findings kept by design (reason)

| song time | critic's line | kept because |
|---|---|---|
| 53.67 | beam snaps to 9 degrees | the slam on "star" (card L19) |
| 54.42 | "question"'s shadow cast upward | the ? is a light below the word |
| 55.42 | "question" shrinks in 1 frame | its small place, as LATE slams (same kit move as PAY) |
| 56.3-57.2 | LATE + ? hold screen position | the camera follows them down (card: "the camera tilts down after them") |
| 67.3-68.95 | 1.6 s near-black with one point | the drain to one point before the lamp (card pad 1) |
| 80.55 | "there" between the rows | THERE sits in the empty seat (card L23) |

## 4. Gates (final render, 52.3-81.6)

| gate | R30 proof | now |
|---|---|---|
| check sync | 36/36 | 36/36, negative control 0 |
| check edge/overlap/clash/stillness | 0 | 0 (turn's views registered as transit) |
| check type-scale | 6 (inherited KC class) | 6 |
| clarity lyric / micro contrast | 0 / 2 | 0 / 4 |
| lifecycle | 4 boundary rows | same 4 (52.72 and 81.33 cuts: neighbour plates) |
| flash / flips | 0 / 0 | 0 / 0 |
| avsync on beat / lift | 69 % / 4.5x | 66.7 % / 4.3x (bar 45 %, 2x) |
| flight beat gain | 1.26 | 0.98 (the stream's on-beat glow is gone) |

## 5. Not done

1. **Object gate**: a pixel pop/stuck detector was written and calibrated on the R30 proof; it failed (441 pop events from grain and dots; missed the far point). Dropped. An exact gate needs alpha on every registered box in `lifecycle.ts`: an engine change for its own session. Until then the lead's frame-grid sweep is the object check.
2. Flight beat gain fell to 0.98 (null 0.88): the flight counts the beat less. Candidate: the rings' on-beat flare a little stronger. Not touched.
3. No 4K, no particle re-panel (the dot count is unchanged).

## 6. Open design calls (Idi's eye)

1. The flight's 10 desks carry the same essay (the joke: copy-paste across the class); the critic could not tell it is a forward flight.
2. The 1.6 s drain to near-black before the lamp.
3. In L22, PAY ATTENTION sits over the hand of ? for 1.6 s.

## 7. Receipts

- Engine `D:\work\aimv-lab\pay-attention`: commits `20504d4` (R30 fixes), `afacb19` (critic round); files `app\src\scenes\late.ts`, `chorus1.ts`
- Render `out\p2-proof.mp4` (1758 frames, 196 s); gates `out\p2-gates\`
- Proof copy `D:\work\AIMVs\ours\pa-song\proof\p2-proof-fix-0m52-1m21.mp4`

## 8. Round 3 (Idi 11-05, after watching the fix)

Idi's notes: the title overflowing every card; the pupil's class and the class after the turn disagreed (two circles, a bright light in one only, a blank board); a table-y shape materialised in front of the class with its text over the board; ATTENTION stuck to the screen through the swipe (against plan v2 Q2).

| Idi's note | cause (verified) | fix | verified |
|---|---|---|---|
| title overflow | 1310 px of title on a 1300 px card | title fitted to the card's inner width (dots too) | full frame 62.5 |
| two rooms disagree | L21 put the class INSIDE the pupil, L22 found it again OUTSIDE: two separately drawn rooms, differently lit, board text skipped when small | one room: the pupil is a mirror of the room the eye faces (reversed); the catchlight is the room's lamp, placed so its mirrored projection lands on the catchlight; the turn faces that same room directly, full frame; board words always drawn, board lit in both views; lamp drawn at the catchlight's size | stills 75.6 / 77.4; 30 fps turn + landing |
| chair materialising | a flat screen drawing faded in over the room | a 3D chair at the front desk from the first frame (seen in the mirror); the camera descends onto it; L23's words placed by its projection, clear of the board | 30 fps descent + rest |
| ATTENTION stuck in the swipe | drawn in screen space while the world panned | L22's words set on the eye's face; the turn waits for ATTENTION's reading time (end + 0.4 s) and they leave with the face | 30 fps turn 76.85-77.48 |

Also from a second blind critic (standards A consistency, B nothing stuck but the meter, C text fits): the corridor's top light was a fixed screen point for 10 s (now ceiling lights over the rings, passed under); the hand washed out in the room (its lights' reach now scales with mark size); labels showed through fading-in cards (bodies opaque first); THERE touched the seat line; REGISTER line unreadable (15 px, full paper); the lamp half-cut at the top edge during the descent (drawn only while in frame).

Kept by design (critic flagged again): the camera following LATE down; the drain to near-black before the lamp; the empty-slot planks before L23's words are sung; THERE between the rows; the GOLD STAR's blue rim (emitted light, look A).

Gates: sync 36/36, 0 edge/overlap/clash/stillness, type-scale 6 (inherited); clarity lyric 0, micro contrast 10 (far ROW labels fading in fog, pan labels); lifecycle 4 boundary rows; flash 0; flips 0; beat 68.8 % at 4.5x chance.

Receipts: engine `d9a1e49`; proof `D:\work\AIMVs\ours\pa-song\proof\p2-proof-fix2-0m52-1m21.mp4`.

## 9. R31 (Idi 11-05): the zoom replaces the swipe; the standard

Idi named the meta-issue: things appeared and vanished "on a whim"; the target is "reality-based-rules" on screen with "physics-defying"/impossible things still happening. Recorded as R31 in [[kit-next-video]]; the standard as 7 rules in [[video2-standard-r31-2026-11-05]].

| change | how | verified |
|---|---|---|
| keep the zoom-in, lose the swipe | after L22's ATTENTION the camera pushes into the pupil until its edge passes the frame's corners (beat 77.57); L22's words scale with the eye's face and fly out (as L20's through the O); from that frame the same projection is drawn directly: mirrored, in the eye's own units (line weights unchanged), on the pupil's ink ground, the lamp at the catchlight's place, size and light | full frames 77.53 vs 77.57 compared side by side: geometry, line weight, light match; 30 fps grids 76.85-78.13 |
| through the looking glass | reflected things stay reversed (the board); the sung words are born in that world and read forward | stills 78.6-80.9 |
| empty slots on the frame edge | the chair's slots appear 0.4 s after the handover | check: 0 lyric-safe |

Gates: sync 36/36, 0 edge/overlap/clash/lyric-safe/stillness, type-scale 5 (inherited); clarity lyric 0; lifecycle 4 boundary rows; flash 0; flips 0; beat 75 % at 4.9x chance. Engine `a005760`; proof `D:\work\AIMVs\ours\pa-song\proof\p2-proof-fix3-0m52-1m21.mp4`.

Next: the whole video (R31), plates by wave, state in `D:\work\aimv-lab\pa-video\briefs\plates-plan.md`.
