---
type: note
created: 2026-11-13
author: jep
status: active
project: DECADEnts
---

# DECADEnts T4: other models on the September assignment (2026-11-13)

Idi, 2026-11-13, on the T1 sheet: "nothing looks good, so I still think we should try other models." His correction of "low quality": "it's more like 'not following instructions' or 'not understanding the assignment' - faces/heads mostly."

Done-state: both models he named installed and run on this PC; his own September prompts rendered on them; every picture scored blind on his criterion; fit on the 4090 measured. Review surface: `projects/decadents/t4-models-2026-11-13.html` (74 pictures, tap answers, one line to paste).

## Verdict

1. **H3-Image follows the head instruction about twice as often as Z-Image-Turbo**: 17 of 32 pictures against 9, same prompts, blind critics. Clear failures: 1 against 5.
2. **No model solves the strict rule.** Nothing human visible anywhere: 7 of 32 (H3-Image) against 1 of 32 (Z-Image-Turbo).
3. **HunyuanImage 3.0 runs on this 4090 with 32 GB RAM.** About 55 s per picture, memory nearly full. 8 of 34 pictures exist; a low-memory guard stopped the rest. 6 of those 8 followed fully.
4. **H3-Image fits comfortably.** About 10 s per new prompt at 4 MP.
5. Two corrections to the 11-12 file, section 6 below.

## Receipts

| What | How verified | Where |
|---|---|---|
| Installs | ComfyUI v0.45.0 portable in `C:\Users\jep\comfy2` (port 8190); the v0.39.0 copy used by AIMV untouched; `/object_info` confirmed all 12 node classes | `C:\Users\jep\comfy2-tools\check_nodes.py` |
| Downloads | anonymous, sizes match the repositories' listings: H3-Image 20.98 + 15.69 + 1.17 GB; HunyuanImage 46.91 + 2.52 GB | `get_comfy2.log` |
| HunyuanImage node code | pattern search of 14 runtime files, 4,212 lines: no process, network, pickle or dynamic-execution calls; one read of its own config | clone in the job folder |
| 34 H3-Image pictures | all viewed by jep as thumbnails; all 34 read blind at 1024 px | `C:\Users\jep\comfy2-tools\t4-out\` |
| 8 HunyuanImage pictures | same | same |
| Blind scoring | 74 pictures resized to one size, shuffled, neutral names; two critic agents; key joined afterwards by script; 0 unmatched rows | `blind-key.json`, `blind-out\` |
| Times and RAM | logged per picture by the runner from ComfyUI's own `/system_stats` | `manifest-h3.json`, `manifest-hy3.json` |
| Sheet | headless Edge at 1876, 1076, 492 px: 0 overflow, 0 script errors, 75 images, scripted taps gave the expected line; top of page looked at | the sheet |

## 1. Blind result

Prompts: the 16 round-2 prompts of 2026-09-14, word for word, plus one 2000s pixel-cube prompt in jep's wording. Seeds 3 and 4. Scale per picture: yes = the head is what the brief says in every stated detail; partly = right object, a stated detail missed; no = a human head or the wrong object.

| Model | Pictures | Yes | Partly | No | Nothing human visible | Look, 1 to 5 |
|---|---|---|---|---|---|---|
| Z-Image-Turbo (September renders) | 32 | 9 | 18 | 5 | 1 | 3.38 |
| MiniMax H3-Image, same 16 prompts | 32 | 17 | 14 | 1 | 7 | 3.59 |
| MiniMax H3-Image, all 17 prompts | 34 | 19 | 14 | 1 | 7 | 3.50 |
| HunyuanImage 3.0 | 8 | 6 | 2 | 0 | 3 | 3.12 |

On the 5 prompts all three share: Z-Image-Turbo 2 of 10 yes, H3-Image 6 of 10, HunyuanImage 6 of 8.

Limits: two seeds per prompt; one critic per picture; the 1024 px blind size can hide small leaks; HunyuanImage's sample is 8 pictures; "look" is the critic's taste, and Idi's eye is the judge.

## 2. Per prompt

| Prompt | Head instruction | Z-Image-Turbo | H3-Image | HunyuanImage |
|---|---|---|---|---|
| 1920s-A | porcelain mask, no mouth | partly, partly | partly, partly | partly, yes |
| 1920s-B | same, one figure | partly, partly (2 and 3 figures) | partly, partly | yes, partly |
| 1930s-A | gas mask, dark lenses, nothing behind | no, no (eyes show) | yes, yes | yes, yes |
| 1930s-B | gas mask, mirrored lenses | partly, partly | yes, yes | yes (1 picture) |
| 1940s-A | helmet, black shadow under the brim | partly, partly | yes, yes | not run |
| 1940s-B | backlit, brim shadow over the whole face | partly, partly | partly, no (profile shows) | not run |
| 1950s-A | chrome toaster with a fedora | yes, yes | yes, yes | yes (1 picture) |
| 1950s-B | chrome toaster | yes, yes | yes, yes | not run |
| 1960s-A | lava lamp mounted on the shoulders | partly, partly | yes, partly | not run |
| 1960s-B | same, kaftan | partly, partly | yes, partly | not run |
| 1970s-A | disco ball, covered body | yes, partly | partly, yes | not run |
| 1970s-B | disco ball on a turtleneck collar | yes, yes | yes, yes | not run |
| 1980s-A | Memphis shapes above an empty collar | no, no (chin, neck, hair) | partly, partly | not run |
| 1980s-B | same, blazer | partly, no | yes, yes | not run |
| 2000s-A | pixelated cube | parked in September | yes, yes (reads as a Minecraft block) | not run |
| 2010s-A | emoji ball with sunglasses | yes, yes | partly, partly (flat sticker, neck) | not run |
| 2010s-B | same, mirror selfie | partly, partly | partly, partly | not run |

Readings (jep's):
- H3-Image's gains sit where the brief names a physical arrangement: lenses with nothing behind, a collar with nothing in it, a helmet over a void.
- HunyuanImage alone drew the mask with no mouth in all four 1920s pictures (thumbnail read by jep; the critics marked two of four fully right, citing a sculpted nose and ear).
- H3-Image lost ground on the 2010s emoji: it pastes a flat sticker over a real head.
- Borrowed designs appear on H3-Image: Minecraft-like blocks, Rubik's-style cubes, Apple-style emoji and phones. The blind critics named them when asked to note real-company designs.

## 3. Fit on this PC (measured)

| Model | Files | Time per picture | Lowest free RAM | Notes |
|---|---|---|---|---|
| Z-Image-Turbo | 12 GB | 4 s at 1 MP | not logged | current |
| H3-Image (8-bit image network, 4-bit text encoder) | 38 GB | 10 to 12 s new prompt, 4 to 5 s next seed, at 4 MP; 16.5 s cold | 14.7 GB | no flags needed |
| HunyuanImage 3.0 (4-bit) | 49 GB | 54 to 61 s at 0.8 MP; about 5.6 s per step, 8 steps | 9.0 to 10.5 GB with `--disable-pinned-memory`; 1.7 GB without | needs `--fast-disk`; model on C: (NVMe) |

HunyuanImage, what happened:
1. First run, default pinned memory (ComfyUI locked 13 GB): picture 1 fine in 58.6 s, picture 2 failed with Windows error 1450, "insufficient system resources", on a 56 MB read at 32.7 GB into the file.
2. Second run, `--fast-disk --disable-pinned-memory`: 7 pictures, 0 errors, 9 to 10.5 GB free.
3. Then the session's own low-memory guard stopped the runner. jep shut ComfyUI down and did not restart it. Other programs on the PC hold about 10 GB.
4. The Reddit thread's "about 30 s" is the author's 188 GB machine. Here: about 55 s.

## 4. H3-Image licence, corrected reading

- Clause V.4, verbatim: "You may not use, reproduce, modify, distribute, or display the MiniMax-H3-Image Works or any of their Outputs or results outside the Applicable Territory."
- Excluded Territories, verbatim: "the European Union, the United Kingdom, the Republic of Korea and the United States of America."
- MiniMax's own Q&A (for the H3 family, `docs/QA-about-License.md` in the MiniMax-H3 repository): the limit applies to the open weights; "API: Globally available with built-in safeguards"; the stated concern is "the ability to control compliance after open weights leave our infrastructure"; organisations in those regions can apply for a licence.
- Why YouTube is full of it: hosted and API use is global; some creators run the weights regardless; viewers are never mentioned in the Q&A.
- jep's read, no lawyer: Idi renders in Israel, inside the territory. Risk for publishing: low, untested. The literal text of V.4 remains.

## 5. Where things live

- `C:\Users\jep\comfy2\` : ComfyUI v0.45.0 with both models and the HunyuanImage node. Start: `bash /c/Users/jep/comfy2-tools/comfy2_up.sh` (add `--fast-disk --disable-pinned-memory` for HunyuanImage). Stop: `comfy2_down.ps1`.
- `C:\Users\jep\comfy2-tools\` : `t4_run.py` (runner, logs time and RAM, retries on the memory error), `t4_prompts.json`, `blind_set.py`, `aggregate.py`, `make_sheet4.py`, `t4-out\` (pictures and manifests).
- Full PNGs: `C:\Users\jep\comfy2\ComfyUI_windows_portable\ComfyUI\output\t4\`.
- Disk: C: 165 GB free after 89 GB of downloads.

## 6. Corrections to `decadents-restart-2026-11-12.md`

1. "HunyuanImage 3.0 (80B): no" was wrong on feasibility. It runs here. What stands: it is slow and memory-tight on 32 GB.
2. "Licence bars displaying outputs in the USA..." was stated as a flat bar. Section 4 above is the accurate version.
3. "Design was the bigger lever, the model the smaller one" was drawn from Z-Image-Turbo alone. On Idi's criterion a better model about doubles full compliance. Both levers are real.

## 7. Not done

- 26 of 34 HunyuanImage pictures (stopped by the memory guard; restart is Idi's call).
- H3-Image's own prompt expander and its edit mode with reference images: untested.
- Negation-free rewrites of the prompts for H3-Image (its card asks for long positive descriptions; these prompts end in "no face, no skin").
- MOSS-Image, Krea 2, Z-Image base: not installed.
- No second critic per picture; no full-resolution blind read.

## Sources

- Blind critiques: `projects/decadents/research-2026-11-13/critic-1.md`, `critic-2.md`; raw verdicts `critic-1.json`, `critic-2.json`; joined counts `aggregate.json`.
- Prompts and run logs: `t4_prompts.json`, `manifest-h3.json`, `manifest-hy3.json` in the same folder.
- Idi's paste of the Reddit thread: `projects/decadents/HunyuanImage 3.0 Reddit Thread.md`.
- MiniMax licence: https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE ; Q&A: https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/QA-about-License.md
- Models: https://huggingface.co/Comfy-Org/MiniMax-H3-Image ; https://huggingface.co/PedroMarinhoDev/HunyuanImage-3.0-Instruct-Distil-ComfyUI ; node https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3
- Yesterday's file: `projects/decadents/decadents-restart-2026-11-12.md`.

## Log

- 2026-11-13 created. Installs, 42 renders, blind scoring, sheet. Waiting on Idi: taps on the T4 sheet, and the word on finishing the HunyuanImage set.
