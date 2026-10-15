---
type: project
created: 2026-10-15
author: jep
status: active
---

# Knowledge Cutoff video - build session 1 (2026-10-15)

Verdict: **plan steps 1-4 built and machine-checked; Gates 1 and 2 wait on Idi.** Follows [[handoff-2026-10-15-video]]; scene plan in [[knowledge-cutoff-scene-plan-2026-10-15]].

## 1. Waiting on Idi (two gates, one question each)

| Gate | Where | What it is | Question |
|---|---|---|---|
| 1 PASSED (Idi 2026-10-15: "Clicks land on the words, I think."; final confirmation at Gate 3, words lighting on screen) | `D:\work\AIMVs\ours\video\gate1\` | `1-full-song-clicks.mp3` = the whole song with a high tick on every word and a deeper tock at each line start. `2-before-after.mp3` = 15 s of chorus 1 with the OLD word times, a pause, then the NEW ones | Do the clicks land on the words? If not, name the time where it drifts |
| 2 PASSED (Idi 2026-10-15: "Keep all 9.") | `D:\work\AIMVs\ours\video\gate2\style-frames.jpg` (full size in `style-frames-frames\`) | 9 real frames of the video, numbered | Keep or strike each by number; say what to change in plain words |

## 2. What changed

1. **Sync**: `D:\work\aimv-lab\kc-video\sync\kc-timing-v2.json` (original untouched). Rule per word: forced alignment when its score is good (318 words); else the vocal onset nearest Whisper + 0.17 s (110); line starts from the voice's loudness rise (16); else Whisper + fixed offset (39). Built by `build_timing_v2.py`. Found on the stem: the triple "Cut-off!" is sung 0.55 s apart, Whisper spaced it 0.42 s; the held "to be" at 1:54 sits 0.7 s later than Whisper said.
2. **Renderer**: `kc-video\render.js`: 4 parallel Edge workers, lossless PNG frames, BT.709 colour tags.
3. **World**: `kc-video\world.html`: one camera over two levels (chat window; the memory inside the cursor, 6 rooms on a 4x2 grid), camera path built from the corrected times and the 13 moves in the scene plan, every word placed in its room, rooms drawn (letter, hall, calendar room, margins, spark, page).
4. **Scene plan** (step 3): [[knowledge-cutoff-scene-plan-2026-10-15]].
5. **Style frames** (step 4): the Gate 2 sheet.

## 3. Verified, with receipts

| Check | Result | Receipt |
|---|---|---|
| Timing data | 483 of 483 words, starts in order, every word on screen 3+ frames | `build_timing_v2.py` output |
| Line starts vs voice | median 0.000 s (partly circular: 16 of 23 lines use that same loudness method) | same |
| Independent: voice energy rises at the word start | peaks at the corrected start (+0.17); Whisper's peaked 0.1 s early | same |
| Click reel | decoded the mp3, found 483 of 483 clicks, each within 1 ms of its time | `sync\verify_reel.py` |
| 4 workers vs 1 | frame-identical (PSNR infinite); 114-170 frames/s vs 52 | `tests\bench.sh` |
| Colour tags | `yuv420p(tv, bt709)` | ffmpeg probe |
| Every word lit on time, on screen, 24 px+ | 483 of 483 at word start + 1 frame; none lit 0.15 s early | `check_sync.js` |
| No hard cuts | full render: cut detector went 21 flags → 1 weak flag (1:01.4, score 5.2; the proof's real cuts score 6.5-40); frames inspected: continuous move | `tests\scdet.sh` |
| No black frames | 0 | `tests\full_skeleton.sh` |

## 4. Failed or not done

1. **GPU render path failed**: black frames with 1 and 4 workers, even with the flags of the earlier one-off probe. Parked; the software path already renders 3:12.6 in 39 s.
2. Timing by ear: Gate 1 passed, Idi's confidence moderate ("I think"); rechecked by eye at Gate 3.
3. (Done in 5b.) The first rough render lacked the rewind, globe push, punches, the turn and the hum line.
4. Fonts are still Windows system fonts; the publish render needs free-licensed ones.
5. Counter "107" assumes publishing on 2026-10-15.

## 5. Decisions jep made (overrule any)

1. "Algae" is written in the calendar room: the song leaves 0.05 s between "be" and "Algae", too short for any move; the dive into the pixel runs during its 2.9 s hold.
2. "but never get a turn" is painted across the whole sheet of rooms, so the pull-out on "every page at once" reveals it.
3. Camera eases from rest on every move (a fast start looked like a cut to the detector).
4. Margins and spark are framed whole so the red-pen notes and the neuron stay in view.
5. The raccoon menu is a pop-up under the word, open 2 s.

## 5b. Build-out after Gates 1-2 (same evening)

| Added | Where it shows | Verified |
|---|---|---|
| Beat-slam punches (line after each drop, every "Cut-off!") | 0:09.6, 0:34.5, 0:56.4, 1:26.9, 1:48.6, 2:31.5, 2:53.1 | no cut flags outside the rewind |
| Globe push on every "The world ... spinning" line, globe spins faster | 0:52.6, 1:45.3, 2:49.6 | frame inspected |
| Flap board flips past JUNE to JULY, AUG, SEPT, OCT in the final chorus | 2:34 on | frames inspected |
| Two hum lines (yours, mine) become one gold line on "we both know the tune" | 2:34-2:38.6 | frames inspected |
| Strong hit over the off-beat line: the AI's light reaches the neuron | 2:02.6 | frames inspected |
| "Thank you for telling me" turns from edge-on to face the viewer, camera leans in | 3:07.5 | frames inspected |
| Rewind to frame 1, loop (0.4 s) | 3:12.2-3:12.6 | first vs last frame 54 dB (same picture); the 8 cut flags all sit inside it, by design |

Changed from the scene plan: M3/M7 are a corridor pan past the later doors into the calendar room, in place of a push through one door.

Gate 3 file: `D:\work\AIMVs\ours\video\gate3\knowledge-cutoff-rough-v2.mp4` (1080p, 60 fps, 3:12.6; 483/483 words pass, 0 black frames, bt709 tags).

## 6. Next

Gate 3 is with Idi: watch 3:12, notes by timestamp. Then build-out rounds on his notes, the font licence check, final 1080p60 + 4K renders, Gate 4.
