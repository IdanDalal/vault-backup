---
type: project
created: 2026-10-17
author: jep
status: active
---

# Knowledge Cutoff: phase 0 of the full video (2026-10-17)

Verdict: **phase 0 is done: the detail kit, the reference library, the full 32-entry timeline (the whole song renders end to end, placeholders for the 13 unbuilt modules), 4K checks and crop sheets, the bible's "Detail at 4K" section, and the engine under git. Wave A (the four chorus agents) is briefed and ready; it is not launched.** Follows [[handoff-2026-10-17-full-video]], [[knowledge-cutoff-treatment-2026-10-17]] (section 12 is new).

## 1. What changed

| item | state | where (engine root `D:\work\aimv-lab\kc-engine\`) |
|---|---|---|
| 1 detail kit | `PaperPlate`, `InkPlate` (paper fibre, print gain, rough edge, ink mottle, signal printed as an offset transparent plate; ink scan texture, phosphor rows), `kcFormHatch`, `kcContourHatch`, `kcSphereST`, `kcRim`, `kcHalo`, `Defocus`; 2D: `LW` (4 weights), `rule`, `node`, `tick`, `cropMarks`, `regMark`, `annot` (micro-type, 10 px), `hatchForm2D`, `hatchFlat2D`, `text`, `settle`, `overshoot`, `flutter` | `app\src\scenes\_kc-glsl.ts`, `_kc.ts`; worked example `kitdemo.ts` |
| 2 reference library | see section 3 | `refs\` (gitignored: frames of other videos never enter a repo) |
| 3 timeline | all 32 bible entries in song order, cuts anchored to lyric lines, set-up anchors and plate (paper/ink) per set-up, ends at 194.1 s (song + 1.5 s tail); a missing module renders `placeholder.ts` | `app\src\timeline.ts` |
| 4 checks at 4K | `check.ts`: `--scale 2`, `--only`, type scale per set-up, micro-type kept off the lyric. `detail.ts`: per set-up, full frame + busiest and flattest 960x540 windows at 1:1 + a reference crop. `errors.ts`: render-error probe | `app\scripts\` |
| 5 bible | section 12 "Detail at 4K": the 8 standards, the kit call for each, the done-state per set-up | vault `projects/AIMV/knowledge-cutoff-treatment-2026-10-17.md` |
| 6 git | `kc-engine` is its own repository: `7ee0515` (proof state), `57eb6b9` (LF endings), `53e477f` (phase 0), `1d8a758` (briefs). The `.git` guard did not block `git init` | `kc-engine\` |
| wave A briefs | shared block + four module blocks + critic block, from handoff section 5 | `reports\wave-a-briefs.md` |

## 2. Verified, and how

| check | result | receipt |
|---|---|---|
| kit renders at 1080p and 4K | at 1:1: paper fibre and print texture visible, highlighted ink prints clean (after one fix), micro-type crisp, engraved sphere follows its parallels, curl hatching follows the curl; viewed by me | `out\kit\1x\`, `out\kit\4k\`, `out\kit\crops2.jpg` |
| whole song renders end to end | 48 frames 0.5-193.5 s, every entry loaded, no scene errors | `out\phase0\full-song-sheet.png` |
| checks unchanged on the proof | chorus 1: 61/61 words lit, negative control 0, 0 edge, 0 title-safe, 0 overlap in 274 frames (the proof's own numbers) | `out\phase0\check-chorus1.json` |
| type-scale check | per set-up: tune 3.5-4.8x, spinning 4.9x, turnedout 5.0x (target 10x); matches the proof report's 3.9-5.7x | same file |
| check at 4K | `turnedout1` at `--scale 2` and at 1x give identical results (9/9 lit, same 2 issues) | `out\phase0\check-turnedout1-4k.json`, `-1x.json` |
| detail sheet | 4 rows for tune1 + cutoff1; flattest windows of the proof are flat ink and flat paper, which is the gap section 12 names | `out\phase0\detail-test\sheet.jpg` |
| renderer per launch | Vulkan, RTX 4090, every run | logs |
| CPU reference (SwiftShader) vs Vulkan, kit shaders | 52.8 dB (paper plate), 54.4 dB (ink plate, hatched sphere, defocus); above 40 dB = no visible difference | `out\kit\swift\`, `out\kit\vk\` |

## 3. Reference library

Built by agent `refs-library` (ffmpeg only), `kc-engine\refs\` (705 MB, gitignored), verified by file count.

| id | video | frames (every 3 s) | heroes | 1:1 crops |
|---|---|---|---|---|
| R1 | I'm Upping My P(Doom) (3840x2160, 60 fps) | 53 | 10 | 10 at 960x540 |
| R2 | LGTM (2560x1440) | 102 | 10 | 10 at 640x360 + 10 upscaled to 960x540 |
| R3 | The Simulation's Ending (1080p, 60 fps) | 83 | 10 | 10 + 10 |
| R4 | Run It Again (1080p, 30 fps) | 96 | 10 | 10 + 10 |
| R5 | Ignore Previous Instructions (1080p, 30 fps) | 61 | 10 | 10 + 10 |

Overview `refs\contact-sheet.jpg` (4 crops per video), per-video `sheet-frames.jpg` and `sheet-crops.jpg`, index with one line per hero `refs\INDEX.md`. Heroes picked by eye from labelled sheets with a sharpness score as a guide; 3 heroes whose crops showed only big lyric type were swapped. What the crops show, the bar in one line: ink-textured stamps, engraved 3D with rim light, mono micro-labels on every instrument, paper documents with footnotes and running heads.

## 4. Found and fixed on the way

1. **Intermittent red frames**: Vite's dependency scan missed the lazily loaded scenes, re-bundled on first use and reloaded the page under the renderer (every entry active, none loaded). Fixed in `vite.config.ts` (scan all scenes up front); `render.ts`, `check.ts`, `detail.ts` now wait out a reload and refuse to render when nothing loaded. With three agents rendering in parallel this would have hit all of them.
2. **Type scale gate**: per set-up (the bible says "every plate"; the references' 9.7-16.6x are whole-video figures), so a frame holding one hook word passes. Per-frame medians are still reported.

## 5. Not done, open

1. **Wave A not launched**: phase 1 is the next step; the briefs are ready.
2. **Proof defects for wave A**: `june` visits 2-3 show garbage flaps ("RF" at 86.7 s, "ZOYB" at 152.4 s); a red hairline on the card at 111.4 s; `june` and `cutoff` draw type outside the box registry, so their type scale is unmeasured until rebuilt.
3. **The 1.5 s tail**: `kc.mp3` is 192.63 s; the engine's duration is the audio's. The final render needs `--to 194.1` and the mux must pad 1.5 s of silence (phase 2).
