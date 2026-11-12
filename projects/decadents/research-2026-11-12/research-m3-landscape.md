---
type: research
created: 2026-11-12
author: Agent m3-landscape
---

# Local open-weight image models for a 24 GB RTX 4090 - landscape, 2026-11-12

Scope: web research only. Nothing installed. Fetched: web pages, HuggingFace metadata JSON, model cards, licence texts, ComfyUI workflow templates (text). All reads dated 2026-11-12.

## 0. Verdict

1. Shortlist: **Krea 2** (design and style range), **FLUX 3 Image Klein** (edit model for the locked character), **MOSS-Image** (Apache-2.0 base with working negative prompts and cheap LoRA training). Reasons in section 3.
2. Highest blind-vote score among models that fit 24 GB: Qwen-Image-2.1 (Elo 1047 text-to-image, 1084 editing). Its licence allows research and evaluation only, so it is off the shortlist for anything published for money.
3. Z-Image base fixes the control complaints (guidance, negative prompts, seed variety) and scores lower than Z-Image-Turbo in blind votes (896 vs 937). Cheap control arm, weak upgrade.
4. Z-Image-Edit: unreleased. The official repo name returns "no such repo" today.
5. No model on this list has published evidence on object-headed, skinless characters. Section 6 is the test that decides.

## 1. Terms and confidence marks

- Open-weight: the trained model file can be downloaded and run locally.
- Distilled: retrained to finish in 4 to 16 steps; guidance is baked in, so the negative prompt box does nothing.
- CFG: classifier-free guidance, the mechanism that steers away from named things; costs 2 model passes per step.
- LoRA: a small add-on file (0.3 to 2 GB) that teaches a base model one character or style.
- Text encoder: the language model that reads the prompt for the image model.
- Prompt upsampler: a small language model that rewrites a short prompt into a long caption before generation.
- INT8 ConvRot, FP8, W4A8, GGUF Q8: compressed weight formats; all run on a 4090. NVFP4 needs an RTX 50-series card (source: BFL card).
- Elo: a rating fitted from pairwise wins; 100 points = about 64% expected win rate.
- DINOv2 similarity: a 0 to 1 score of how alike two image crops look to a vision model.
- (H) read in a primary source today. (M) one independent source, or my reading of a licence. (L) derived, estimated, or seen only in a search summary.
- Parameter counts marked "≈" are derived from the 16-bit file size (bytes / 2).

## 2. Candidate tables

One row per candidate, split in two tables with the same row numbers. Unkeyed cells in Table A come from the HuggingFace API record and model card of the repo named in the row [HF]. Source keys are resolved in section 7.

### Table A - identity, licence, access

| # | Model | Maker | Released | Params (image model) | Licence → paid YouTube use of outputs | Gated? Anonymous source | Best weights for 24 GB (file size) | ComfyUI |
|---|---|---|---|---|---|---|---|---|
| 0 | Z-Image-Turbo (current) | Alibaba Tongyi-MAI | 2025-11-25 | ≈6.2B | Apache-2.0 → yes | open | bf16 12.3 GB | native |
| 1 | Z-Image (base) | Alibaba Tongyi-MAI | 2026-01-27 | ≈6.2B | Apache-2.0 → yes | open, `Comfy-Org/z_image` | bf16 12.3 GB; reuses the Turbo text encoder and VAE | native [TPL] |
| 2 | Z-Image-Edit | Alibaba Tongyi-MAI | unreleased | - | - | `Tongyi-MAI/Z-Image-Edit` returns 401 (no repo) (H); "to be released" as of 2026-08 [ZE] (L) | - | - |
| 3 | Qwen-Image-2.1 (+ Turbo 8-step) | Alibaba Qwen | 2026-09-20; Turbo 2026-10-09 [GQ] | 7B [GQ] | Qwen Research License: "research or evaluation purposes only" [LQ] → no (M) | open, `Comfy-Org/Qwen-Image-2.1`, `unsloth/Qwen-Image-2.1-GGUF` | bf16 14.2 GB or INT8 7.3 GB + encoder INT8 9.4 GB | native, day 0 [GQ] |
| 4 | Qwen-Image-Edit-2511 | Alibaba Qwen | 2025-12-17 | ≈20B | Apache-2.0 → yes | open, `Comfy-Org/Qwen-Image-Edit_ComfyUI` | INT8 20.5 GB or GGUF Q6 18.0 GB; tight with 31.8 GB RAM | native [TPL] |
| 5 | FLUX 3 Image Klein (distilled + Base) | Black Forest Labs | 2026-10-15 [VF] (L) | 5.6B [CF] | FLUX Kommunity License: commercial use of outputs allowed under US$5M revenue, with content review and AI disclosure where law requires [LF] → yes, conditional (H) | gated (`auto`); mirrors `ml-resources/flux-3-image-klein-comfy`, `unsloth/flux-3-image-klein-FP8`, `unsloth/flux-3-image-klein-GGUF` (H) | bf16 11.1 GB or INT8 5.8 GB + encoder 4.9 GB + upsampler 6.7 GB | native, needs ComfyUI ≥ 0.41.0 [DF] |
| 6 | FLUX.2 [dev] | Black Forest Labs | 2025-11-22 | ≈32B | FLUX Non-Commercial; §2(d) "may use Output for any purpose (including for commercial purposes)" [LN] → outputs yes (M) | gated; mirrors `Comfy-Org/flux2-dev`, `city96/FLUX.2-dev-gguf` | GGUF Q4 20.0 GB + encoder 12.3 GB; poor fit for 31.8 GB RAM | native |
| 7 | FLUX.2 [klein] 9B | Black Forest Labs | 2026-01-14 | ≈9.1B | FLUX Non-Commercial, outputs clause as row 6 [LN] → outputs yes (M) | gated; mirrors `unsloth/FLUX.2-klein-9B`, `unsloth/FLUX.2-klein-9B-GGUF` | bf16 18.2 GB or Q8 10.3 GB | native [TPL] |
| 8 | FLUX.2 [klein] 4B | Black Forest Labs | 2026-01-14 | 4B | Apache-2.0 → yes | open | bf16 7.8 GB | native [TPL] |
| 9 | Krea 2 (Raw + Turbo) | Krea | 2026-06-22/23 [VK] (L); repos 2026-06-18 | 12.9B [KE] | Krea 2 Community License: commercial use of model and outputs allowed under US$1M company revenue [LK] → yes, conditional (H) | gated (`auto`); mirrors `Comfy-Org/Krea-2`, `unsloth/Krea-2-Turbo` (H) | FP8 13.1 GB each + encoder 5.2 GB | native [TPL] |
| 10 | MOSS-Image (Base, SFT; Kromoss fine-tune) | OpenMOSS; Kromoss by lodestones | 2026-10-16 [RV] | 5B [CM] | Apache-2.0 → yes | open, `Comfy-Org/MOSS-Image` (6.3M downloads) | bf16 10.2 GB + encoder INT8 9.8 GB | native since v0.42.0 [HI] (M) |
| 11 | HiDream-O1-Image (full + Dev) | HiDream.ai | 2026-05-08 | 8B, pixel-space, no VAE | MIT → yes | open, `Comfy-Org/HiDream-O1-Image` | bf16 16.4 GB or FP8 8.1 GB | native [TPL] |
| 12 | ERNIE-Image (+ Turbo) | Baidu | 2026-04 | 8B | Apache-2.0 → yes | open, `Comfy-Org/ERNIE-Image` | 16.1 GB + encoder 7.7 GB | native [TPL] |
| 13 | Ideogram 4.0 | Ideogram | 2026-06 [S1] | ≈9.3B | Ideogram 4 Non-Commercial (licence text not readable anonymously) → no (L) | gated; mirrors `Comfy-Org/Ideogram-4`, `stduhpf/ideogram-4-gguf` | FP8 9.3 GB × 2 (conditional + unconditional model) | native [TPL] |
| 14 | Fibo 2.0 (dev + edit-turbo) | Bria | 2026-10-20 [VB] (L) | ≈8.2B | CC BY-NC 4.0 → no | gated; mirror `Comfy-Org/Fibo-2.0` | bf16 16.5 GB or INT8 8.4 GB | native edit templates [TPL] |
| 15 | Ming-Image-0.1-Design | Ant Group (inclusionAI) | 2026-09-17 | 6B | MIT → yes | open, `Comfy-Org/Ming-Image` | 12.3 GB + encoder W4A8 12.8 GB (INT8 19.5 GB) | native [TPL] |
| 16 | Boogu-Image 0.1 (Base, Turbo, Edit) | Boogu | 2026-06-16 | 10B | Apache-2.0 → yes | open, `Comfy-Org/Boogu-Image` | FP8 10.3 GB + encoder 10.6 GB | native [TPL] |
| 17 | Chroma1-HD | lodestones | 2025-08-08 | 8.9B | Apache-2.0 → yes | open | 17.8 GB or FP8 9.2 GB | native [TPL] |
| 18 | HunyuanImage 2.1 | Tencent | 2025-09-05 | 17B | Tencent Hunyuan Community (licence text unread today; territory limits reported) → unverified (L) | open | FP8 17.4 GB + refiner 15.0 GB | native |
| 19 | Kandinsky 5.0 Image Lite | Kandinsky Lab | 2025-11-19 | 6B | MIT → yes | open | 12.0 GB | native [TPL] |
| 20 | Ovis-Image | Alibaba AIDC | 2025-11-28 | 7B | Apache-2.0 → yes | open, `Comfy-Org/Ovis-Image` | 14.7 GB | native [TPL] |
| 21 | LongCat-Image (+ Edit) | Meituan | 2025-12-04 | 6B | Apache-2.0 → yes | open, `Comfy-Org/LongCat-Image` | 12.5 GB | native [TPL] |
| 22 | GLM-Image | Z.ai | 2026-01-08 | ≈7B diffusion + language-model front end | MIT → yes | open | ≈14 GB + 11 GB | no native template found [TPL] (M) |
| 23 | Lumina-Image 2.0 (+ NetaYume anime tune) | Alpha-VLLM | 2025-01-22 | ≈2.6B | Apache-2.0 → yes | open | 5.2 GB | native [TPL] |
| 24 | HiDream-I1 | HiDream.ai | 2025-04-06 | ≈17B | MIT → yes | open | FP8 17.1 GB | native; superseded by row 11 |
| 25 | Cosmos3-Super-Text2Image | NVIDIA | 2026-05-28 | 32B to 64B depending on stored precision (27 shards, ≈128 GB) (L) | OpenMDW 1.1 (unread) | open | none fits 24 GB (H) | - |
| 26 | HunyuanImage 3.0 (80B) | Tencent | 2025-09 [S1] | 80B | other researcher | other researcher | other researcher | - |
| 27 | MiniMax H3-Image | MiniMax | 2026-11-10 [LX] | 33.1B [CX] | MiniMax community licence; excludes EU and UK among "Excluded Territories" [LX] (H) | open, `Comfy-Org/MiniMax-H3-Image` | W4A8 12.6 GB + encoder 15.7 GB; other researcher | native [TPL] |

Also seen, outside the brief: Anima (2B anime model, non-commercial licence), Krea 3 and Qwen-Image-3.0 (API only), Kandinsky 6.0 (video), P-H3-Image (Pruna's 8-step H3 variant).

### Table B - behaviour

| # | Model | s per 1 MP on a 4090 | True CFG, negative prompt | Seed variety | Reference / edit input | Style range beyond photo | Known weaknesses | Artificial Analysis rank, read 2026-11-12 |
|---|---|---|---|---|---|---|---|---|
| 0 | Z-Image-Turbo | ≈4 (owner's number) | no; 8 steps, cfg 1 [ZC] | Low [ZC] | none | - | the owner's list | open #19, Elo 937 ±11 [S1] |
| 1 | Z-Image base | ≈25 at 25 steps cfg 4, derived from row 0 (L) | yes; cfg 3 to 5, 28 to 50 steps; "robust negative control" [ZC] (vendor) | High [ZC] (vendor) | none | anime and illustration claimed [ZC] | visual quality rated below Turbo by its own maker [ZC] | all-models #92, Elo 896 ±16 [S2] |
| 3 | Qwen-Image-2.1 | 10 (one ComfyUI user, settings unstated) [NK] (L); 45 at 40 steps via diffusers with CPU offload, 65 at 20 steps with CFG 4 [MR] (H); Turbo ≈2 (L) | optional; template default cfg 1 [TPL]; cfg 3 to 4 "far better", time ×2 [DD] (M) | no measurement found; one high-score post cites "lack of style diversity" [R11] (L) | up to 10 reference images in the same model [GQ] | papercraft and anime restyles shown [R12]; "polished although overbaked" [R7] | research-only licence; pink vertical line from tiled VAE decode; reusing the reference's seed copies it oversaturated; 10 references took ≈10 min and one person changed identity [MR] | open #2 T2I, 1047 ±12; open #3 edit, 1084 ±13 [S1][S3] |
| 4 | Qwen-Image-Edit-2511 | not found | yes; `true_cfg_scale` 4, 40 steps [HF] | n/a | multi-image edit | - | 20B, slow, RAM-tight here | open #10 edit, 996 ±16 [S3] |
| 5 | FLUX 3 Image Klein | distilled 16 steps: ≈4 on a 5090, under 9 on a 4070 (BFL) [WF] → ≈5 to 6 (L); Base ≈4× slower [GF] | Base: yes, 50 steps, cfg 3.5, negative prompt slot [DF]; distilled: no | not found | up to 10 references; bounding boxes on a 0 to 1000 grid [CF] | style transfer praised [R13]; own T2I look called "AI images circa 2023" [R7] | T2I rated weak, anatomy errors [R5][R6]; BFL re-described it as primarily for editing on 2026-11-03 [R14]; short prompts give generic output without the upsampler [CF]; edits can change content outside the target [CF] | open #3 T2I, 1044 ±11; open #4 edit, 1069 ±13 [S1][S3] |
| 6 | FLUX.2 [dev] | not found | guidance-distilled; no (L) | not found | multi-reference | - | too large for this RAM | open #8 T2I (anchor 1000); #9 edit [S1][S3] |
| 7 | FLUX.2 klein 9B | 1.2 distilled, ≈11 base [WF] (L) | base only (L) | identity drifts per seed in edits [R8] | multi-reference | style transfer compared in [R13] | softer output; needs a consistency LoRA [R8] | open #21 T2I, 933; #6 edit, 1014 [S1][S3] |
| 8 | FLUX.2 klein 4B | ≈1 (L) | base only (L) | not found | multi-reference [HF] | - | lowest quality of the family | open #29 T2I, 840; #13 edit, 942 [S1][S3] |
| 9 | Krea 2 | Turbo: ≈4 on a 5090 (blog) → ≈5 to 7 (L); Raw 52 steps with CFG: ≈60+ (L) | Raw: yes, 52 steps, cfg 3.5, up to 1K [KE]; Turbo: no, exactly 8 steps at cfg 1 [DD] | Raw "diverse" (vendor) [KE]; no measurement | no identity input; style reference with 1 to 2 images [MU]; community identity-edit LoRA needs custom nodes and a separate non-commercial licence [KI] | strongest evidence here: 1,255-style sheet, score 1130 [R9]; 9 official style LoRAs incl. retro anime, stippling, ink wash [HF]; "innately knows a lot of styles" [R7] | 512-token prompt limit, drifts from long prompts [DD]; pattern artefacts with grain prompts [R7]; "can look too artistic" [DD]; Turbo shares Z-Image-Turbo's negative-prompt limit | API "Krea 2 Medium" 1015, "Medium Turbo" 1021 [S2]; link to the open files unverified (L); absent from the open-weights filter |
| 10 | MOSS-Image | 37 on a 5090 at 50 steps, cfg 3 [AM] → ≈45 to 50 (L); ≈25 at 25 steps (L); 8-step DMD LoRA ≈8× faster, cfg 1 [R15] | yes; default cfg 3, negative prompt supported [CM]; the 8-step LoRA removes it [KR] | praised: "variety in images... faces, ethnicities, body types" [R10] (M) | none in the release [MU]; community edit LoRA [R16] | 4-panel comic via layout JSON worked [R4]; anime verdicts conflict [HI][MU] | "no cars" in the prompt still drew cars [R4]; most anomalies of three models in one test [DD]; divided reception: score 627 "cannot get decent results" [R2] vs score 439 "best base model" [R1] | not listed |
| 11 | HiDream-O1-Image | not found | yes; 40 steps, cfg 5 in the template [TPL] | not found | edit + multi-reference subject input [HF] | not found | Dev (distilled) variant scores far lower (812) | open #16 T2I, 979; #12 edit, 952 [S1][S3] |
| 12 | ERNIE-Image | not found | yes; 50 steps, cfg 4 [HF] | not found | none | "stylized aesthetics" claimed [HF] | T2I only | open #23, 910 [S1] |
| 13 | Ideogram 4.0 | not found | guidance through a second unconditional model [TPL]; negative text unverified (L) | not found | none found | design and typography focus | non-commercial; two 9.3 GB models | open #5 (Quality) 1026; #6, 1003 [S1] |
| 14 | Fibo 2.0 | not found | not checked | not found | edit model | JSON prompts | non-commercial | open #4 T2I, 1038; #2 edit, 1085 [S1][S3] |
| 15 | Ming-Image-0.1-Design | not found | no; 12 steps, cfg 1 [HF] | not found | edit template exists [TPL] | UI, posters, infographics | 37 GB encoder at full size; maker validated on 80 GB | open #7, 1002 [S1] |
| 16 | Boogu-Image 0.1 | not found | Base: yes, cfg 2 to 5; Turbo: no [HF] | Base "strong diversity" (vendor) | Edit: 1 reference [HF] | anime, 3D, gilded styles claimed | ranks only on its own vendor arena | not listed |
| 17 | Chroma1-HD | not found | yes; 40 steps, cfg 3, negative prompt in the card example [HF] | not found | none | broad, community-tuned | older FLUX.1-class detail | not listed |
| 18-24 | HunyuanImage 2.1, Kandinsky 5 Lite, Ovis-Image, LongCat-Image, GLM-Image, Lumina 2.0, HiDream-I1 | not found | all undistilled with CFG in card examples (cfg 3.5, 3.5, 5, 4, 1.5, 4) [HF] | not found | LongCat-Edit and GLM-Image take images | Lumina has anime tunes | all rank below row 0 or are unranked | Qwen-Image (2025) 907; GLM-Image 893; LongCat 860; others not listed [S1] |
| 26 | HunyuanImage 3.0 | other researcher | - | - | Instruct variant edits | - | - | open #20 T2I, 935; Instruct #13 T2I, 987, #5 edit, 1064 [S1][S3] |
| 27 | MiniMax H3-Image | other researcher | no; 6 steps, no CFG [CX] | - | up to 16 references [XS] (L) | - | 33B | open #1 T2I, 1067 ±15; #1 edit, 1138 ±16 [S1][S3] |

## 3. Ranked shortlist for this project and this machine

1. **Krea 2** - Turbo for drafts, Raw for the guided pass and LoRA training.
   - Style range has the strongest evidence in this survey (Table B, row 9). The project needs 11 period looks plus comics and cel.
   - Raw gives true CFG and negative prompts; Turbo gives ≈5 to 7 s drafts. Maker's rule: train LoRAs on Raw, run them on Turbo [KE].
   - Licence covers paid publishing under US$1M revenue [LK]. FP8 files fit 24 GB with room.
   - Risks: 512-token prompts; Raw tops out at 1K and takes 104 model passes; no identity input.
   - Confidence that it beats Z-Image-Turbo on the owner's eye: medium. Evidence is community preference, no blind test on this subject matter.
2. **FLUX 3 Image Klein** - the edit and consistency tool; Base as a second guided text-to-image arm.
   - Edit Elo 1069 ±13, statistically tied with Qwen-Image-2.1 (1084 ±13) [S3]; an independent 12-task test put it 1 point behind Qwen [R8].
   - Up to 10 references, bounding-box placement, 5.6B, bf16 fits in 24 GB.
   - Licence allows commercial outputs under US$5M [LF]; Qwen-Image-2.1's does not [LQ].
   - Risks: weak as a from-scratch generator [R5][R6][R7]; needs the 6.7 to 9.8 GB upsampler; official repo gated, mirrors are third-party copies.
3. **MOSS-Image** (SFT, with Kromoss as a variant) - the Apache-2.0 base.
   - Undistilled by default: cfg 3, negative prompts, seed variety. That answers the seed and negative-prompt complaints directly; eyes, skin and extra figures become things a negative prompt can name.
   - LoRA training reported under 6 to 8 GB VRAM [R17]; character LoRA settings published [R10].
   - Risks: ≈45 to 50 s per image at maker settings; divided reception on raw quality [R2]; anomalies more frequent [DD].
- Control arm at near-zero cost: **Z-Image base** (12.3 GB, same encoder and VAE as today).
- If nothing will ever be monetised: add **Qwen-Image-2.1** (INT8 7.3 GB); it leads both boards among 24 GB fits.
- Disk: Krea 2 ≈32 GB, FLUX 3 Klein ≈24 to 35 GB, MOSS ≈20 to 30 GB, Z-Image base 12 GB, Qwen-Image-2.1 ≈17 GB. Total ≈115 GB; C: has 257 GB.

## 4. Character consistency across shots - strongest local approach today

1. **Edit models with reference images** hold the best-measured position.
   - Blind votes: 5 open edit models now score above 1060, with FLUX.2 [dev] fixed at 1000 (rows 27, 14, 3, 5, 26) [S3].
   - Measured test, Qwen-Image-2.1 [MR]: 1 reference preserved people and products (product DINOv2 similarity 0.88 to 0.94 vs ≤0.16 for different products). 3 references: people held, shoe stripes changed. 10 references: 6 preserved, 4 partial, one man became another person (face similarity 0.17 to 0.31).
   - Independent character-sheet task [R8]: FLUX 3 Klein 3/5, Qwen-Image-2.1 3/5, FLUX.2 klein 9B 2/5 ("a slightly different person with each seed").
   - Rules that come out of those tests: 1 to 3 references; describe each item's colour, material and shape in words; never reuse the seed that made the reference [MR].
2. **Character LoRA** has anecdotes and no measurement.
   - Musetta's comparison states nobody has measured identity retention across Krea 2, MOSS and Qwen [MU].
   - Reports: MOSS character LoRAs from 50 to 100 captioned images, done before 5k steps [R10]; a second user "finally nailed Moss char loras" [R18]; Krea 2 "takes a lot more effort to train" [R19].
   - Guides claim reference workflows drift around image 10 to 15 and LoRAs hold longer [BL] (L, marketing blogs).
3. **For this cast specifically** (my inference, untested): an object head behaves like a product, and the product numbers above are the relevant ones. Face-similarity tools do not apply.
4. Recommended order: lock one hero image per character → use the edit model to make a 15 to 30 image sheet (angles, poses, distances) → curate → train a LoRA on Krea 2 Raw or MOSS Base → shots use LoRA first, edit model for repairs and restyles (comic, cel).

## 5. Leaderboards - what each measures

1. **Artificial Analysis, AA-Image-T2I v2.1 and AA-Image-Editing v2.1** [S4] (H)
   - Votes: blind pairwise choices by a recruited, validated panel, plus older public votes that legacy models still carry.
   - Prompts: written by the company against a grid of 10 use cases × 9 capabilities, English, refreshed monthly; "Animation & Gaming" (character design, comics) is 1 of the 10.
   - Generation: 1 image per prompt, seed 42, 1024×1024, each model's default steps and guidance, negative prompt left empty, hosted endpoints at full precision.
   - Score: Bradley-Terry fit shown as Elo, FLUX.2 [dev] fixed at 1000.
   - Editing board: each prompt paired with one curated reference image; 7 edit actions × 10 use cases [AS] (L).
   - Does not measure: seed variety, negative prompts, identity across many shots, compressed local builds, speed on a 4090.
2. **LMArena / arena.ai Text-to-Image Arena** (L)
   - Votes: public visitors type their own prompts, see two anonymous outputs, pick one; Bradley-Terry scores [SR].
   - The site refused automated reads today (HTTP 403), so no rank was read. Last third-party snapshot: 2026-05-12, 5.17M votes, 60 models, open models near the bottom [SR].
3. **Claims vs measurements**
   - "Open weights" on a board says nothing about 24 GB: the top open row is 33B, another ships ≈128 GB of weights, another is 80B.
   - Krea's "#1 from an independent lab" refers to its hosted model (Krea 2 Large, 1036) [KE][S2]; the downloadable Raw and Turbo files have no row under the open-weights filter.
   - MOSS-Image's "second only to GPT Image 2" is the maker's own arena [SM] (vendor). Same for Boogu Arena [HF].
   - FLUX 3 Klein ties Qwen-Image-2.1 on the board (1044 vs 1047) while hands-on users rate its text-to-image well below [R5][R6][R7]. Board runs use maker defaults with the upsampler and one seed; community runs vary. Unresolved; the head-to-head settles it for this project.
   - Z-Image base at 896 vs Turbo at 937: the non-distilled model is the less preferred single image.

## 6. Head-to-head test plan

Arms: Z-Image-Turbo (baseline), Z-Image base (cfg 4), Krea 2 Turbo, Krea 2 Raw (cfg 3.5), MOSS-Image SFT (cfg 3), FLUX 3 Klein Base (cfg 3.5). Edit arms for P8: FLUX 3 Klein, plus Qwen-Image-2.1 if non-commercial testing is acceptable.
Fixed: 1 MP, 8 seeds per prompt per arm (16 for P4), maker-default sampler, the same wording for all arms. Labelling by someone who cannot see model names.
Prompt rule for every arm: no negations in the positive prompt. Banned things go in the negative prompt; coverage is written positively ("high starched collar", "leather gloves", "head fully enclosed").

| # | Prompt (from the cast) | Failure it exposes | Measure |
|---|---|---|---|
| P1 | 1920s: figure whose whole head is a smooth glazed porcelain mask, high collar, gloves, silver-gelatin studio portrait. Negative: eyes, eye holes, skin, neck, hands | eyes through the mask, skin, neck | images of 8 with zero visible eye, skin or neck |
| P2 | 1940s: steel helmet with pure black shadow inside the opening, greatcoat, press-photo grain. Negative: face, eyes, mouth | a face forming inside the void | images of 8 with a featureless opening |
| P3 | 1950s: chrome toaster head in a kitchen, Kodachrome look. Run twice: (a) "no dinosaurs" written in the prompt, (b) "dinosaur" only in the negative prompt | negated words leaking | leak count per variant; (a) leaked on MOSS in [R4] and is expected to leak on every arm, (b) should be 0 on guided arms |
| P4 | 1970s: disco-ball head, full body, empty dance floor. 16 seeds | seeds barely changing the image | mean pairwise DINOv2 distance across the 16, plus a count of distinct compositions by eye, vs baseline |
| P5 | 1930s: burlap-sack head, dust-bowl farmer, alone on an empty road, full body. Negative: second person, crowd | extra figures | images of 8 with exactly one figure |
| P6 | 1980s: head made of floating Memphis-style geometric shapes, power suit, direct-flash magazine photo | concept binding plus period look | shapes float with no head underneath (count of 8); blind guess of the decade |
| P7 | 1960s lava-lamp head as a four-colour halftone comic panel; 2000s pixelated-cube head as a hand-painted cel animation frame | style range beyond photo | images of 8 that read as the medium (flat colour, line, dots) with the head design intact |
| P8 | Edit: approved hero image of the 1990s CRT-monitor head; instruction: seated, three-quarter back view, new room. 8 seeds, none equal to the hero's seed | re-posing a locked character | DINOv2 similarity of the head crop to the hero; costume checklist items kept; new pose achieved (count of 8); skin leaks |

Readout per arm: pass counts for P1, P2, P3b, P5; variety score for P4; medium counts for P6, P7; then a blind pairwise preference vote against the Z-Image-Turbo set on the passing images. Time per image logged from ComfyUI for the speed column this report could only estimate.

## 7. Sources

Leaderboards and method
- [S1] https://artificialanalysis.ai/image/leaderboard/text-to-image/open-weights
- [S2] https://artificialanalysis.ai/image/leaderboard/text-to-image
- [S3] https://artificialanalysis.ai/image/leaderboard/editing/open-weights
- [S4] https://artificialanalysis.ai/text-to-image/methodology
- [AS] https://alphasignal.ai/news/artificial-analysis-rebuilds-its-image-editing-arena-across-17-specialized (search summary)
- [SR] https://arena.ai/leaderboard/text-to-image (403 to automated read; figures from search summaries of this page)

HuggingFace metadata and cards [HF] - `https://huggingface.co/api/models/<repo>` and `https://huggingface.co/<repo>` for:
- Tongyi-MAI/Z-Image, Tongyi-MAI/Z-Image-Turbo, Comfy-Org/z_image, Comfy-Org/z_image_turbo [ZC = https://huggingface.co/Tongyi-MAI/Z-Image]
- Qwen/Qwen-Image-2.1, Qwen/Qwen-Image-2.1-Turbo, Comfy-Org/Qwen-Image-2.1, unsloth/Qwen-Image-2.1-GGUF, Qwen/Qwen-Image-Edit-2511, Comfy-Org/Qwen-Image-Edit_ComfyUI, unsloth/Qwen-Image-Edit-2511-GGUF
- black-forest-labs/flux-3-image-klein, -base, -comfy, -pup; ml-resources/flux-3-image-klein-comfy [CF]; unsloth/flux-3-image-klein-FP8, unsloth/flux-3-image-klein-GGUF
- black-forest-labs/FLUX.2-dev, FLUX.2-klein-9B, FLUX.2-klein-4B; Comfy-Org/flux2-dev; city96/FLUX.2-dev-gguf; unsloth/FLUX.2-klein-9B, unsloth/FLUX.2-klein-9B-GGUF
- krea/Krea-2-Raw, krea/Krea-2-Turbo, Comfy-Org/Krea-2, unsloth/Krea-2-Turbo; [KI] https://huggingface.co/conradlocke/krea2-identity-edit
- OpenMOSS-Team/MOSS-Image-SFT [CM], OpenMOSS-Team/MOSS-Image-Base, Comfy-Org/MOSS-Image, unsloth/MOSS-Image-SFT-GGUF; [KR] https://huggingface.co/lodestones/Kromoss
- HiDream-ai/HiDream-O1-Image, Comfy-Org/HiDream-O1-Image; baidu/ERNIE-Image, Comfy-Org/ERNIE-Image; ideogram-ai/ideogram-4-fp8, Comfy-Org/Ideogram-4, stduhpf/ideogram-4-gguf; briaai/Fibo-2.0-dev, Comfy-Org/Fibo-2.0; inclusionAI/Ming-Image-0.1-Design, Comfy-Org/Ming-Image; Boogu/Boogu-Image-0.1-Base, Boogu/Boogu-Image-0.1-Edit, Comfy-Org/Boogu-Image; lodestones/Chroma1-HD; tencent/HunyuanImage-2.1; kandinskylab/Kandinsky-5.0-T2I-Lite-sft-Diffusers; ATH-MaaS/Ovis-Image-7B; meituan-longcat/LongCat-Image; zai-org/GLM-Image; Alpha-VLLM/Lumina-Image-2.0; HiDream-ai/HiDream-I1-Full; nvidia/Cosmos3-Super-Text2Image; MiniMaxAI/MiniMax-H3-Image [CX], Comfy-Org/MiniMax-H3-Image; circlestone-labs/Anima

Licences
- [LQ] https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE
- [LF] https://huggingface.co/ml-resources/flux-3-image-klein-comfy/blob/main/LICENSE.md (copy of the FLUX Kommunity License v1.0)
- [LN] https://huggingface.co/unsloth/FLUX.2-klein-9B/blob/main/LICENSE.md (copy of the FLUX Non-Commercial License)
- [LK] https://www.krea.ai/krea-2-licensing
- [LX] https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE

Maker repos and docs
- [GQ] https://github.com/QwenLM/Qwen-Image-2.1
- [GF] https://github.com/black-forest-labs/flux-3-image-klein
- [DF] https://docs.comfy.org/tutorials/flux/flux-3-klein
- [KE] https://github.com/krea-ai/krea-2 ; https://www.krea.ai/blog/krea-2-technical-report
- [TPL] https://github.com/Comfy-Org/workflow_templates (templates/index.json and the per-model workflow JSON files)
- [SM] https://arxiv.org/abs/2610.23374 (MOSS-Image Technical Report; figures via search summary)

Independent tests and reviews
- [MR] https://github.com/MindrLabs/image-generation-qwen-image-2.1
- [DD] https://diffusiondoodles.substack.com/p/small-model-overload-krea-2-qwen (2026-11-05)
- [MU] https://musetta.ai/blog/moss-image-vs-krea-2-vs-qwen-image-2-1-recurring-face
- [HI] https://note.com/hirorohi03/n/n085c66f9f7fc
- [WF] https://willitrunai.com/blog/flux-3-klein-vram-requirements
- [AM] https://ai-muninn.com/en/blog/moss-image-traditional-chinese-comic-cards (search summary)
- [NK] https://note.com/kongo_jun/n/n6b7f4d51944d (search summary)
- [ZE] https://localaimaster.com/blog/z-image-base-edit-guide (search summary)
- [BL] https://rangy.ai/blog/ai-character-consistency/ ; https://aiofm.info/en/guides/consistent-ai-character (search summaries)
- News, search summaries only: [VF] https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses ; [VK] https://venturebeat.com/technology/enterprise-grade-ai-image-generation-in-2-seconds-is-here-krea-2-raw-and-turbo-available-as-open-weights-under-custom-license ; [VB] https://comfyui-wiki.com/en/news/2026-10-20-fibo-2-0 ; [RV] https://elma.sh/blog/moss-image-review ; [XS] https://technode.com/2026/11/11/minimax-releases-h3-image-weights-says-model-can-generate-4k-images-in-under-10-seconds/

Reddit r/StableDiffusion, read through the Arctic Shift archive (https://arctic-shift.photon-reddit.com/api/posts/search); post = https://www.reddit.com/r/StableDiffusion/comments/<id>/
- [R1] 1x8ixsy "Moss is the best base model we've gotten yet" (score 439)
- [R2] 1xj7sk5 "How I feel about the current open source image models" (627)
- [R4] 1x7kc3o "MOSS-Image ... 35 hard prompts, one seed, no cherry-picking" (152)
- [R5] 1x7a0qu "FLUX 3 Klein vs FLUX.2 Klein 9B vs Qwen Image 2.1 vs Krea2" (213)
- [R6] 1x7fx0m "FLUX.3 Klein is disappointing for image generation, but AMAZING for consistent photo editing" (163)
- [R7] 1x9oi6x "Basic Workflow Simple Prompt Testing: Krea2 vs MOSS vs Qwen2.1 vs Flux3" (90)
- [R8] 1x9qq05 "How good is FLUX.3 Klein at editing? A 12-task comparison" (158)
- [R9] 1xfeonr "Krea 2 king of styles!" (1130)
- [R10] 1xeunzs "My MOSS Character Lora Training Results" (234)
- [R11] 1xfek2n "...tired of Qwen/Klein's lack of style diversity and realism" (249)
- [R12] 1xmg8au "I textured an entire street in Blender with Qwen Image 2.1, then made cyberpunk, anime and papercraft versions" (422)
- [R13] 1xcr36a "Flux3 style transfer mastery" (168); 1x8koa8 "Flux3 vs Flux2 9B for style transfer" (119)
- [R14] 1xmqbyu "Black Forest Labs updated Flux.3 Image Klein documentation to clarify that its primarily designed for image editing" (108)
- [R15] 1xfe5qy "Moss vs Kromoss vs Krea 2, 192 images for each" (126)
- [R16] 1xclgg2 "MOSS-Image-Edit LoRA" (253)
- [R17] 1x8ch9k "MOSS-Image LoRA training ... under 6 GB VRAM" (147); 1xarw4c "How to train MOSS-Image LoRAs locally (8 GB VRAM)" (180)
- [R18] 1xfu2d6 "I finally nailed Moss char loras" (163)
- [R19] 1xtuqk4 "Krea2 takes a lot more effort to train loras" (1)

Gaps, stated once
- No RTX 4090 timing was found for Krea 2, MOSS-Image, FLUX 3 Klein or Z-Image base; those cells are estimates.
- LMArena ranks unread (site blocks automated reads).
- Ideogram 4 and Tencent Hunyuan Community licence texts unread.
- Reddit title search timed out; coverage is every post from 2026-10-15 to 2026-11-03 plus a 50-post sample from 2026-11-10 to 11-12, filtered by model name.
