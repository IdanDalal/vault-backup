---
type: research
created: 2026-11-05
author: jep
---

# Camera balance and render scans: pa-wip-0m00-1m21.mp4

Verdict: our camera sits still far more than his three films (60 % against 30-40 %), moves slightly less often, and lands too often; the late plate's flight carries 35 of the 51 reversals. The cut scan found zero real cuts. The flicker scan fails by its number, and the frames show most of its top events are designed type changes and sliding objects; one of six sampled is a probable real 1-frame dropout (19.37 s, "INK'S" to "INK").

Bands are his taste (kit level-up 4.2): this report informs Idi and blocks nothing.

## Terms (defined once)

- fw/s: frame widths per second, how far the picture travels on screen per second (balance.md, Imaginative Prompting).
- still: picture speed under 0.04 fw/s (his threshold).
- move: a burst at or above 0.12 fw/s lasting 4+ frames (our threshold; his text gives none; sensitivity table below).
- hold: 10+ consecutive still frames. A move lands when a hold starts within 12 frames of its end.
- whip: a move peaking at 1.5 fw/s or more; fast: 0.5 fw/s or more.
- reversal: a camera parameter (pan x, pan y, zoom, roll) changes sign with no hold in between, including a turn through a momentary stop (his rule: no reversal).
- jitter window: a 1 s span where the picture shift travels 14+ px at 640x360 but ends under 35 % of that path from where it started (his rule: wander and return).
- flicker: a 1-3 frame change that undoes itself, measured in CIELAB dE (dE = perceptual colour difference; seeds 12, grow 6 at 720 lines, his thresholds).
- inlier share: fraction of tracked points that agree with one camera transform (1.0 = the whole picture moves as one).

## Receipts

- Source `D:\work\AIMVs\ours\pa-song\proof\pa-wip-0m00-1m21.mp4` (60 fps, 81.6 s, file time 2026-11-05 05:43).
- camprobe: 4896 frames decoded of 4896 expected, 4895 frame pairs, 177 pairs with no camera estimate (165 of them blank frames, read as still; 12 interpolated).
- scans: 4896 of 4896 frames at 1280x720; 4892 flicker reference frames tested of 4892 possible (121 cleared by the prune); 4895 pairs for cuts and jitter; 635 s.
- Tools: `D:\work\aimv-lab\pa-video\tools\camprobe.py`, `scans.py`, `vlib.py`. Raw tables: `D:\work\aimv-lab\pa-video\scratch\t-probe\camprobe.md`, `scans.md`; data `camprobe.json`, `scans.json`; flicker sheets `sheets-0m00-1m21\` (600 saved, cap reached at ~69 s).
- Re-analysis without a second decode: `python camprobe.py scratch/t-probe/camprobe.json --out <md> --sections plates=plates.tsv --sections song=song.tsv` (1.6 s; output identical to the decode run before today's new rows).

## Self-tests (planted known-bad clips, made with `D:/work/aimv-lab/ffmpeg.exe`)

| check | plant | expected | measured | result |
|---|---|---|---|---|
| camprobe, known camera | still 1 s, eased 400 px move, still 1.5 s, whip 900 px, drift, still with a slammed box; 360 frames | 2 moves, 1 whip, 1 landed, 0 reversals, 0 jitter, ~67 % still | 360/360 frames; 2 moves, 1 whip, 1 landed, 0 reversals, 0 jitter, 67.1 % still | read correctly |
| camprobe reversal | 300 px sine swing, turns at 0.50 and 1.50 s; 180 frames | reversal check FAILS | 180/180 frames; reversals at 0.52 s and 1.52 s | FAILED (good) |
| camprobe jitter | 3 Hz wander and return, 1.00-3.00 s; 240 frames | jitter check FAILS | 240/240 frames; 1 window | FAILED (good) |
| scans flicker | 2-frame white box at frames 100-101 during a pan; 240 frames | flicker scan FAILS | 240/240; found at 100-101, strength 1064, 0 other events | FAILED (good) |
| scans flicker control | same pan, a box that appears and stays | clean | 0 failing events | clean |
| scans cut | hard cut at frame 120 plus a whip at frames 30-45; 240 frames | cut at 120 only | cut at 120, whip clean | FAILED (good) |
| scans jitter | camera wander 1.00-3.00 s; 240 frames | jitter scan FAILS | 1 window 0.15-3.85 s | FAILED (good) |
| scans tile jitter | textured patch wanders while the camera holds | tile scan FAILS, global clean | 0 global, 1 tile window | FAILED (good) |

The reversal plant first PASSED (instrument broken: a turn through a 3-frame stop split the segment). Fixed today: reversals now count between holds. Logs: `scratch\t-probe\camprobe-plant.log` (18:51), `scans-plant.log` (17:11, after the last `scans.py` edit at 17:08).

## Balance against his bands (0:00-1:21)

| measure | ours | his 3 films | verdict |
|---|---|---|---|
| still share | 59.6 % | 30-40 % | high |
| median picture speed | 0.021 fw/s | 0.06-0.11 | low |
| moves per 10 s | 4.54 (37 moves) | 4.9-6.9 | low |
| fast moves and whips | 68 % (9 whips) | 66-82 % | in |
| moves that land and hold | 54 % | 18-35 % | high |
| holds mean / longest | 1.02 / 10.82 s | 0.9-2.6 / 7.2-33 s | in / in |
| reversals | 51 | 0 | high |
| jitter windows | 9 | 0 | high |
| peak image speed, all | 13,601 px/s at 1080p | ~3,600 px/s except blurred whips | whip peak |
| peak image speed outside whips | 5,952 px/s (51.87 s) | ~3,600 px/s | high |
| time over 3,600 px/s outside whips | 0.5 % (5 runs: 2.07, 40.00, 40.12, 45.28, 51.87 s) | 0 % | high |
| median inlier share | 0.98 | (no band) | motion reads as whole-frame |

His rejected drafts sat at 17-18 % still and 8-14 % landing (balance.md S1). Ours misses on the opposite side.

Move threshold sensitivity: 0.08 fw/s → 4.17 moves/10 s, 68 % land; 0.12 → 4.54, 54 %; 0.20 → 4.78, 38 %. Landing stays above his band and moves stay under it at every threshold tried.

## Per plate

| plate | song s | still % | median fw/s | moves/10 s | land % | holds mean / max s | reversals | jitter |
|---|---|---|---|---|---|---|---|---|
| open | 0.00-9.14 | 70 | 0.002 | 6.6 | 83 | 0.9 / 2.6 | 4 | 2 |
| verse1 | 9.14-27.87 | 81 | 0.010 | 4.3 | 50 | 1.7 / 10.8 | 3 | 1 |
| class | 27.87-52.72 | 57 | 0.025 | 4.0 | 80 | 0.8 / 2.8 | 7 | 1 |
| late | 52.72-69.58 | 28 | 0.191 | 5.9 | 20 | 0.6 / 1.4 | 35 | 4 |
| chorus1 | 69.58-81.33 | 70 | 0.015 | 1.7 | 50 | 1.3 / 2.8 | 2 | 1 |

## Per song section

| section | song s | still % | median fw/s | moves/10 s | land % | holds mean / max s | reversals | jitter |
|---|---|---|---|---|---|---|---|---|
| spoken1 | 0.00-6.52 | 74 | 0.001 | 6.1 | 100 | 0.9 / 2.6 | 4 | 1 |
| pad1 | 6.52-9.47 | 60 | 0.018 | 6.8 | 50 | 5.9 / 10.8 | 0 | 1 |
| verse1 | 9.47-40.91 | 67 | 0.014 | 4.1 | 54 | 0.7 / 2.8 | 9 | 1 |
| spoken2 | 40.91-43.25 | 42 | 0.051 | 4.3 | 100 | 0.9 / 2.0 | 1 | 0 |
| pre1 | 43.25-56.00 | 75 | 0.017 | 4.7 | 83 | 0.6 / 1.4 | 5 | 2 |
| solo1 | 56.00-69.75 | 18 | 0.230 | 5.8 | 12 | 0.8 / 1.4 | 30 | 3 |
| chorus1 | 69.75-81.37 | 69 | 0.016 | 2.6 | 33 | 1.3 / 2.8 | 2 | 1 |

Against his section shape (quiet verses about half still with 3-7 s holds; energy saved for pre-chorus and chorus):
1. verse1 is quiet (67 % still) and its still time is chopped: longest hold 2.8 s, under his 3-7 s.
2. pre1 and chorus1 are stiller than the verse (75 %, 69 %) and chorus1 moves least of all (2.6/10 s). His shape puts the camera energy there; ours spends it in solo1. The chorus energy may come from type slams, which this probe counts as local change (see limits); medium confidence.
3. solo1 (the late plate's flight) is 18 % still, the level of his rejected drafts (17-18 %), with 7 near-identical ~0.9 s fast moves at 58.7-64.2 s, none landing, and roll reversals every ~0.5 s. Reads as a banking weave; his rule bans reversals; whether the weave stays is Idi's taste.
4. 9 jitter windows (also found by scans.py from the same phase-correlation input, so the two tools agree without being independent): 2.03-3.30, 6.55-8.65, 23.53-24.75, 50.05-51.08, 53.82-54.88, 57.82-59.15, 61.02-62.18, 68.68-70.87, 76.07-77.52 s. Frames not yet stepped; candidates.

## Scans

| scan | result | frames read by eye | reading |
|---|---|---|---|
| flicker | 439 events, 114 at strength 8+ (FAIL by number) | top 6 sheets | 1 probable real defect, 4 false, 1 unclear |
| cut | 2 flagged, 0 allowed (FAIL by number) | both, 5-6 frame strips | 0 real cuts |
| light jumps | 31 histogram jumps with structure kept | none | many sit within 1 frame of a beat: designed light hits, likely |
| global jitter | 9 windows | none | see item 4 above |
| tile jitter | 75 windows (advisory) | none | designed wobbles flag here too |

Flicker events read by eye:
1. 19.37 s (frame 1162): "INK'S" vanishes for exactly one frame, then "INK" appears (strip `scratch\t-probe\drop19.png`, sheet `flk_01162_3.png`). Probable real 1-frame dropout in the verse1 word swap. Builder check.
2. 43.18 s: a panel slides away as "THEY" slams in. Local motion plus type slam: false.
3. 3.15 s: the blue highlight sweep across "INTELLIGENCE" and its exit: designed type change, false.
4. 33.53 s: rolling counter digit 3 to 2 with blur: local motion, false.
5. 48.43 s: sliding panels: local motion, false.
6. 8.68 s: a soft blob on the dark lamp-lit gradient, peak dE 15: unclear; could be a glow pulse. Eye check.

Cuts read by eye: 44.35 s is "BOARD" slamming onto a near-black frame (a type slam drops the grey correlation, so the structure test cannot save it); 81.58 s is the last frame of the clip inside a blurred push into "If you never asked," (the isolation test has no frames after it). Both false.

Calibration finding: the flicker fail bar (strength 8) was set on synthetic plants and does not transfer to this footage. Recommendation: in `gates-window.sh post`, the flicker scan reports its top 25 with sheets for a lead eye pass and blocks nothing until the bar is recalibrated on accepted plates.

## What the tools cannot see

1. The probe reads pixels. His numbers come from his films' camera values at every frame; ours from the picture. Typographic slams, fades, glows and particles move pixels too: a whole-frame type push reads as a camera move, a slam on black reads as a cut, a glow pulse reads as flicker.
2. One 2D transform per frame (shift, zoom, roll). Depth parallax collapses onto the dominant plane; turn rate in degrees per second and acceleration in m/s² (his smoothness numbers) cannot be measured without focal length and depth, so only px/s is compared.
3. Blank or near-blank frames carry no estimate; 165 such pairs are counted as still, which pushes the still share up (165 of 4895 pairs = 3.4 points at most).
4. The move threshold (0.12 fw/s) and landing gap (12 frames) are ours; his text gives none. The sensitivity table bounds that choice.
5. Flicker alignment uses dense flow with a global fallback; sliding objects that the flow loses score as flicker (items 2, 4, 5 above).
6. No scan judges intent: a reversal or jitter window may be designed. Every flag is a frame to step before anyone rules on it.
7. Coverage: 0:00-1:21 only. Waves 2-4 plates are unmeasured until the full render.

Credit: definitions, thresholds and bands from Imaginative Prompting, claude-video-skills (MIT), `skills/shot-design/balance.md` and `skills/render-checks/SKILL.md`; their code was read for reference and run nowhere. Our code and our departures are stated in each tool's header.
