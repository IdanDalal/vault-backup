---
type: project
created: 2026-10-17
author: jep
status: active
---

# Knowledge Cutoff: chorus 1 proof on the new engine (2026-10-17)

Verdict: **the chorus 1 proof is built and rendered on our copy of P(Doom)'s engine: 27.7 s (0:34.4-1:02.1), 5 scenes, 9 set-ups (the bible plans 11 here: `spinning` and `turnedout` have 1 each so far), every check green: 61 of 61 words lit on time, 0 frame-edge, title-safe or overlap issues in 277 sampled frames, CPU reference matching the GPU at 49-58 dB. One bible target is missed: type scale (section 4).** Watch it: `D:\work\AIMVs\ours\video\proof\kc-chorus1-proof.mp4`; beside v6: `v6-vs-proof-1.jpg`, `v6-vs-proof-2.jpg` in the same folder.

Follows [[knowledge-cutoff-treatment-2026-10-17]] (the style bible), [[engine-probe-p2-2026-10-17]].

## 1. What is on screen

| time | scene | what happens |
|---|---|---|
| 0:34.4 | `june` | a split-flap board carries "My knowledge stopped in June"; each word's flaps land on its sung start; JUNE slams yellow with a camera punch, the caret blinking after it; through the hold every word before JUNE flips back to blank and the camera pushes into JUNE alone |
| 0:37.4 | `tune` A | a piano roll: the singer's real notes (pitch read from the vocal stem) as solid bars past the caret playhead; the model's predictions as hollow yellow outlines ahead of it, all wrong, turning into grey dashed misses |
| 0:41.9 | `tune` B | paper: WHAT I MADE / TRUE? table, three pasted claims (`music videos`, `a million views`, `a sibling above me`); a check lands on "made", "there", "true" |
| 0:44.8 | `tune` C | a greyed `check sources` toggle; on "check" the knob tries and springs back, tooltip `unavailable in this session`; on "you" the caret crosses the line and stops after YOU, which holds yellow through the 2.3 s note |
| 0:50.2, 0:56.1 | `cutoff` ×2 | KNOWLEDGE huge; three stamped CUT-OFF!s, each sliced by the yellow blade on "off", halves parting, the next landing between them (visit 2 sweeps the other way) |
| 0:52.6 | `spinning` | an engraved line-art globe turning under a fixed yellow meridian labelled MY CUTOFF; meridians that just passed it trail yellow; spin speeds up on "spinning"; KEPT holds yellow |
| 0:59.1 | `turnedout` | paper: a PROFILE card (`self-reported, June`) with its June guesses in grey ink: `an assistant`, `before July`, `answering`; the caret strikes them through one per beat, then waits in NAME |

## 2. Verified, and how

| check | result | receipt |
|---|---|---|
| per-word sync | 61 of 61 words show yellow in their box one frame after they light; negative control (0.25 s earlier): 0 of 61 | `kc-engine\out\proof\check.json` (`scripts/check.ts`) |
| frame edge, title-safe 96 px, nothing over the lyric | 0 issues in 277 frames (every 0.1 s). The first pass found 849: the push-in cropped MY KNOWLEDGE STOPPED at the frame edge (fixed: the forgetting wave), fading halves crossing title-safe (fixed), and the board's own frame (reclassified) | same |
| CPU reference (SwiftShader) vs Vulkan | 49.1 to 58.1 dB PSNR on 6 frames (above 40 dB: no visible difference) | `refcheck.sh` |
| every launch on the 4090 | renderer string printed per launch: Vulkan, RTX 4090 | render logs |
| file | 27.66 s, 1920x1080, 60 fps, `yuv420p(tv, bt709)`, AAC; copy md5-identical (`36c4d61f…`) | ffmpeg probe |
| render speed | 1,660 frames in 85.9 s (19.3 frames/s, adaptive motion blur 12-324 sub-frames) | render log |
| by eye | stills of every set-up, both sheets, viewed by me | `out\wip\`, `out\proof\` |

## 3. Bible rules, as built

1. One glowing colour (yellow), "June" once per frame, no October, no day numbers, no filled drawings, no generated images: met (checked by eye on the sheets).
2. Chorus hop on every chorus word; tense words held yellow (don't/know, Tell/tell/is, can't/I'll/believe, kept): built.
3. One change to the bible, written back into it: `june` puts the whole line on the board (the three-flap version would have shown "June" twice), and adds the forgetting wave.

## 4. Not met, not done

1. **Type scale: 3.9x to 5.7x** (largest to smallest type per frame), against the bible's 10x and the references' 9.7-16.6x. The display type is big (KNOWLEDGE ~190 px) but the small labels are 15-20 px; the fix is bigger heroes per set-up (the JUNE push and the cuts already get there) or fewer, larger labels.
2. Sparse stretches: the roll is empty 0:38.8-0:40.5 because the singer is silent there (the old "1.9 s hold on new" was a gap); the predictions keep coming, but the frame is quiet.
3. Not watched at speed by a person yet: Idi's eye is the next gate.
4. Choruses 2 and 3 (visits 2-3 of every module) and the other 13 modules: not built.

## 5. The engine (`D:\work\aimv-lab\kc-engine\`)

1. P(Doom)'s engine core copied with its MIT notice (`LICENSE-pdoom-engine.txt`); none of its scenes, song, lyrics or plates.
2. Changed: palette (our tokens on its key names), fonts (Anybody, JetBrains Mono, Newsreader, Caveat: OFL, licence files in `app/public/fonts/licenses/`, static instances by `tools/make_fonts.py`), bloom threshold above paper (paper never glows), amber halation, Vulkan default, a Windows mkdir fix.
3. Data: `tools/build_data.py` (483 words from the forced-aligned timing, beats, per-section downbeats because the beat grid drifts, loudness envelopes), `tools/build_pitch.py` (pitch per word from the vocal stem).
4. Ours: `src/scenes/_kc.ts` (karaoke, hop, caret, backgrounds, the box registry the checks read), five scenes, `src/timeline.ts`, `scripts/check.ts`, `kc.sh` (tsc, stills, sheet, video, check).
