---
type: note
created: 2026-11-13
author: jep
status: active
project: DECADEnts
---

# DECADEnts T4: other models on the September assignment (2026-11-13, completed 11-14)

Idi, 2026-11-13, on the T1 sheet: "nothing looks good, so I still think we should try other models." His correction of "low quality": "it's more like 'not following instructions' or 'not understanding the assignment' - faces/heads mostly."

Done-state: both models he named installed and run on this PC; his own September prompts rendered on them; every picture scored blind on his criterion; fit on the 4090 measured. Review surface: `projects/decadents/t4-models-2026-11-13.html` (100 pictures, tap answers, one line to paste).

## Verdict

1. **HunyuanImage 3.0 understands the assignment.** Head instruction followed fully in 26 of 32 pictures, against 17 (H3-Image) and 9 (Z-Image-Turbo), same prompts, blind critics. Clear failures: 0, 1, 5.
2. **Strict rule, nothing human visible anywhere:** 19, 7 and 1 of 32.
3. **Idi's own taps agree** (section 8): understood in 5 of 5 HunyuanImage pairs, 7 of 16 H3-Image pairs, 3 of 16 Z-Image-Turbo pairs.
4. **Both new models run on this PC.** H3-Image: about 10 s per new prompt at 4 MP. HunyuanImage: median 54.5 s at 0.8 MP, with two ComfyUI flags and the browser closed.
5. **Look is unsolved.** His mean look scores: 1.9, 2.1, 2.2. No model reaches 5 anywhere.
6. Three corrections to the 11-12 file, section 6 below.

## Receipts

| What | How verified | Where |
|---|---|---|
| Installs | ComfyUI v0.45.0 portable in `C:\Users\jep\comfy2` (port 8190); the v0.39.0 copy used by AIMV untouched; `/object_info` confirmed all 12 node classes | `C:\Users\jep\comfy2-tools\check_nodes.py` |
| Downloads | anonymous, sizes match the repositories' listings: H3-Image 20.98 + 15.69 + 1.17 GB; HunyuanImage 46.91 + 2.52 GB | `get_comfy2.log` |
| HunyuanImage node code | pattern search of 14 runtime files, 4,212 lines: no process, network, pickle or dynamic-execution calls; one read of its own config | clone in the job folder |
| 34 + 34 pictures | all viewed by jep as thumbnails; all read blind at 1024 px | `C:\Users\jep\comfy2-tools\t4-out\` |
| Blind scoring | 100 pictures resized to one size, shuffled, neutral names; three critic agents; keys joined afterwards by script; 0 unmatched rows; 14 control pictures re-scored by the third critic, same verdict on 12 | `blind-key.json`, `blind2-key.json`, `blind-out\` |
| Times and RAM | logged per picture by the runner from ComfyUI's own `/system_stats` | `manifest-h3.json`, `manifest-hy3.json` |
| Sheet | headless Edge at 1876 and 492 px: 0 overflow, 0 script errors, 101 images, scripted taps gave the expected line; findings and ruling block looked at | the sheet |

## 1. Blind result

Prompts: the 16 round-2 prompts of 2026-09-14, word for word, plus one 2000s pixel-cube prompt in jep's wording. Seeds 3 and 4. Scale per picture: yes = the head is what the brief says in every stated detail; partly = right object, a stated detail missed; no = a human head or the wrong object.

| Model | Pictures | Yes | Partly | No | Nothing human visible | Look, 1 to 5 |
|---|---|---|---|---|---|---|
| Z-Image-Turbo (September renders) | 32 | 9 | 18 | 5 | 1 | 3.38 |
| MiniMax H3-Image, same 16 prompts | 32 | 17 | 14 | 1 | 7 | 3.59 |
| HunyuanImage 3.0, same 16 prompts | 32 | 26 | 6 | 0 | 19 | 3.19 |
| MiniMax H3-Image, all 17 prompts | 34 | 19 | 14 | 1 | 7 | 3.50 |
| HunyuanImage 3.0, all 17 prompts | 34 | 27 | 7 | 0 | 20 | 3.12 |

Limits: two seeds per prompt; one critic per picture; the 1024 px blind size can hide small leaks; the third critic scored look 0.36 higher than round one on the 14 controls; "look" is the critics' taste, and Idi's eye is the judge.

## 2. Per prompt

| Prompt | Head instruction | Z-Image-Turbo | H3-Image | HunyuanImage |
|---|---|---|---|---|
| 1920s-A | porcelain mask, no mouth | partly, partly | partly, partly | partly, yes |
| 1920s-B | same, one figure | partly, partly (2 and 3 figures) | partly, partly | yes, partly |
| 1930s-A | gas mask, dark lenses, nothing behind | no, no (eyes show) | yes, yes | yes, yes |
| 1930s-B | gas mask, mirrored lenses | partly, partly | yes, yes | yes, yes |
| 1940s-A | helmet, black shadow under the brim | partly, partly | yes, yes | yes, yes |
| 1940s-B | backlit, brim shadow over the whole face | partly, partly | partly, no (profile shows) | yes, yes |
| 1950s-A | chrome toaster with a fedora | yes, yes | yes, yes | yes, yes |
| 1950s-B | chrome toaster | yes, yes | yes, yes | partly, yes |
| 1960s-A | lava lamp mounted on the shoulders | partly, partly | yes, partly | yes, yes |
| 1960s-B | same, kaftan | partly, partly | yes, partly | yes, yes (chest and forearms of the dummy show) |
| 1970s-A | disco ball, covered body | yes, partly | partly, yes | partly, yes |
| 1970s-B | disco ball on a turtleneck collar | yes, yes | yes, yes | yes, yes |
| 1980s-A | Memphis shapes above an empty collar | no, no (chin, neck, hair) | partly, partly | partly, partly (neck, jaw) |
| 1980s-B | same, blazer | partly, no | yes, yes | yes, yes |
| 2000s-A | pixelated cube | parked in September | yes, yes (reads as a Minecraft block) | partly, yes (skin-toned mosaic) |
| 2010s-A | emoji ball with sunglasses | yes, yes | partly, partly (flat sticker, neck) | yes, yes |
| 2010s-B | same, mirror selfie | partly, partly | partly, partly | yes, yes |

Readings (jep's):
- HunyuanImage builds the head as an object where the others paste it on: the emoji is a glossy ball, the lava lamp is head-sized with its base as the neck, the backlit helmet holds a solid void.
- H3-Image's gains over Z-Image-Turbo sit where the brief names a physical arrangement: lenses with nothing behind, a collar with nothing in it.
- HunyuanImage reads literally: "brick cellphone" is a brick with a keypad in four pictures; its 1940s helmets are French or British types.
- No model solved 1980s-A; the brief itself ("floating cluster... above an empty collar" plus a shirt with an open collar) leaves room for a neck.
- Borrowed designs: Minecraft-like blocks, Rubik's-style cubes, Apple-style emoji and phones on H3-Image; Rubik's-style cubes in one HunyuanImage picture. The blind critics named them when asked to note real-company designs.

## 3. Fit on this PC (measured)

| Model | Files | Time per picture | Lowest free RAM | Notes |
|---|---|---|---|---|
| Z-Image-Turbo | 12 GB | 4 s at 1 MP | not logged | current |
| H3-Image (8-bit image network, 4-bit text encoder) | 38 GB | 10 to 12 s new prompt, 4 to 5 s next seed, at 4 MP; 16.5 s cold | 14.7 GB | no flags needed |
| HunyuanImage 3.0 (4-bit) | 49 GB | median 54.5 s (52.9 to 66.1) at 0.8 MP; about 5.6 s per step, 8 steps | 12.4 to 14.6 GB, browser closed; 9.0 to 10.5 GB, browser open; 1.7 GB with pinned memory on | needs `--fast-disk --disable-pinned-memory`; model on C: (NVMe) |

HunyuanImage, what happened:
1. First run, default pinned memory (ComfyUI locked 13 GB): picture 1 fine in 58.6 s, picture 2 failed with Windows error 1450, "insufficient system resources", on a 56 MB read at 32.7 GB into the file.
2. Second run, `--fast-disk --disable-pinned-memory`: 7 pictures, 0 errors. Then the session's own low-memory guard stopped the runner; jep shut ComfyUI down and waited for Idi's word.
3. Third run, 11-13 on his word with his browser closed: the remaining 26 pictures, 0 errors, 0 retries.
4. The Reddit thread's "about 30 s" is the author's 188 GB machine. Here: about 55 s.

## 4. H3-Image licence, corrected reading

- Clause V.4, verbatim: "You may not use, reproduce, modify, distribute, or display the MiniMax-H3-Image Works or any of their Outputs or results outside the Applicable Territory."
- Excluded Territories, verbatim: "the European Union, the United Kingdom, the Republic of Korea and the United States of America."
- MiniMax's own Q&A (for the H3 family, `docs/QA-about-License.md` in the MiniMax-H3 repository): the limit applies to the open weights; "API: Globally available with built-in safeguards"; the stated concern is "the ability to control compliance after open weights leave our infrastructure"; organisations in those regions can apply for a licence.
- Why YouTube is full of it: hosted and API use is global; some creators run the weights regardless; viewers are never mentioned in the Q&A.
- jep's read, no lawyer: Idi renders in Israel, inside the territory. Risk for publishing: low, untested. The literal text of V.4 remains.
- HunyuanImage 3.0: Tencent's community licence excludes the EU, UK and South Korea, with the same kind of clause on outputs (the 11-12 research agent read it; jep did not re-read it).

## 5. Where things live

- `C:\Users\jep\comfy2\` : ComfyUI v0.45.0 with both models and the HunyuanImage node. Start: `bash /c/Users/jep/comfy2-tools/comfy2_up.sh` (add `--fast-disk --disable-pinned-memory` for HunyuanImage). Stop: `comfy2_down.ps1`.
- `C:\Users\jep\comfy2-tools\` : `t4_run.py` (runner, logs time and RAM, retries on the memory error), `t4_prompts.json`, `blind_set.py`, `blind_set2.py`, `aggregate.py`, `make_sheet4.py`, `t4-out\` (pictures and manifests).
- Full PNGs: `C:\Users\jep\comfy2\ComfyUI_windows_portable\ComfyUI\output\t4\`.
- Disk: C: 165 GB free after 89 GB of downloads.

## 6. Corrections to `decadents-restart-2026-11-12.md`

1. "HunyuanImage 3.0 (80B): no" was wrong. It runs here, and on Idi's criterion it is the best of the three.
2. "Licence bars displaying outputs in the USA..." was stated as a flat bar. Section 4 above is the accurate version.
3. "Design was the bigger lever, the model the smaller one" was drawn from Z-Image-Turbo alone. On Idi's criterion the model moves full compliance from 9 to 26 of 32. Both levers are real.

## 7. Not done

- HunyuanImage's prompt rewriting and its edit mode with reference images: untested (rewriting adds minutes per picture by the node author's figures).
- H3-Image's prompt expander and edit mode: untested.
- Negation-free rewrites of the prompts (all 17 end in "no face, no skin").
- MOSS-Image, Krea 2, Z-Image base: not installed.
- No second critic per picture; no full-resolution blind read.
- What drives Idi's low look scores: unknown.

## 8. Idi's answers on the T4 sheet (2026-11-13)

His pasted line, verbatim:

> DECADEnts T4 answers | 1920s-A: zit partly 2/5; h3 no 1/5; hy3 yes 3/5 | 1920s-B: zit partly 1/5; h3 no 1/5; hy3 yes 2/5 | 1930s-A: zit no 2/5; h3 yes 3/5; hy3 yes 2/5 | 1930s-B: zit partly 2/5; h3 yes 3/5; hy3 yes 3/5 | 1940s-A: zit no 1/5; h3 partly 1/5 | 1940s-B: zit no 1/5; h3 no 1/5 | 1950s-A: zit yes 2/5; h3 yes 3/5; hy3 yes 1/5 | 1950s-B: zit yes 2/5; h3 yes 3/5 | 1960s-A: zit no 1/5; h3 partly 2/5 | 1960s-B: zit no 2/5; h3 no 2/5 | 1970s-A: zit partly 3/5; h3 yes 3/5 | 1970s-B: zit yes 4/5; h3 yes 4/5 | 1980s-A: zit no 2/5; h3 no 1/5 | 1980s-B: zit no 1/5; h3 yes 3/5 | 2010s-A: zit partly 3/5; h3 no 2/5 | 2010s-B: zit no 1/5; h3 no 1/5

Key: zit = Z-Image-Turbo, h3 = H3-Image, hy3 = HunyuanImage 3.0. One answer per pair of pictures. 2000s-A and the model ruling were left untapped. With it he said: "Excellent work!", closed his browser so the remaining 26 HunyuanImage pictures could run, and asked for research on `github.com/JustAResearcher/gpu-unlock-ada` and similar developments.

Tally (jep's count of his line):

| Model | Pairs answered | Understood: yes | Partly | No | Look, mean of his scores |
|---|---|---|---|---|---|
| Z-Image-Turbo | 16 | 3 | 5 | 8 | 1.9 |
| H3-Image | 16 | 7 | 2 | 7 | 2.1 |
| HunyuanImage 3.0 | 5 | 5 | 0 | 0 | 2.2 |

Readings (jep's):
1. His eye agrees with the blind critics on direction and is stricter: H3-Image 7 of 16 pairs fully understood against 3 for Z-Image-Turbo; both H3-Image 1920s masks are a "no" for him where the critics said "partly".
2. HunyuanImage 3.0 understood the assignment in every pair he saw (5 of 5). Sample still small; the full set was started on his word the same day.
3. Look is a separate problem that no model solved: his highest score anywhere is 4 of 5 (1970s-B, both Z-Image-Turbo and H3-Image); the HunyuanImage toaster he marked "yes" got 1 of 5. What drives his look score is unstated.

## Sources

- Blind critiques: `projects/decadents/research-2026-11-13/critic-1.md`, `critic-2.md`, `critic-3.md`; raw verdicts `critic-1.json`, `critic-2.json`, `critic-3.json`; joined counts `aggregate.json`.
- Prompts and run logs: `t4_prompts.json`, `manifest-h3.json`, `manifest-hy3.json` in the same folder.
- Idi's paste of the Reddit thread: `projects/decadents/HunyuanImage 3.0 Reddit Thread.md`.
- MiniMax licence: https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE ; Q&A: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/QA-about-License.md
- Models: https://huggingface.co/Comfy-Org/MiniMax-H3-Image ; https://huggingface.co/PedroMarinhoDev/HunyuanImage-3.0-Instruct-Distil-ComfyUI ; node https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3
- Yesterday's file: `projects/decadents/decadents-restart-2026-11-12.md`.

## Log

- 2026-11-13 created. Installs, 42 renders, blind scoring, sheet.
- 2026-11-13 Idi's answers pasted (section 8); remaining 26 HunyuanImage pictures rendered on his word.
- 2026-11-14 third blind critic; tables, verdict and sheet updated with the full HunyuanImage set. Waiting on Idi: taps on the HunyuanImage columns and the model ruling.
