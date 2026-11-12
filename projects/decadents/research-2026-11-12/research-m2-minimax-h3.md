---
type: research
created: 2026-11-12
author: Agent m2-minimax-h3
---

# MiniMax H3-Image vs Z-Image-Turbo: research report

Read date for every web fact: 2026-11-12. Method: anonymous web fetches only, nothing installed, no model files downloaded. Reddit read through the Arctic Shift archive API. Confidence tags: high = primary source read directly; medium = one independent source or several anecdotal ones; low = inference or single anecdote.

## Verdict

**Usable locally, ungated, on the 4090. Recommended as a head-to-head trial beside Z-Image-Turbo, with the swap decided by the owner's eye.** The model is 2 days old, RAM at 31.8 GB is the tight spot, and the evidence on art styles and on reference consistency is mixed.

## 1. Does it exist

| Item | Finding | Source | Conf. |
|---|---|---|---|
| Exact name | "MiniMax H3-Image" (blog), "MiniMax-H3-Image" (model card), "MiniMax H3 Image" (site menu) | minimax.io blog, HF card | high |
| Maker | MiniMax (the Hailuo company). Licensor entity in the licence text: Nanonoble Pte. Ltd. | LICENSE | high |
| Release | Licence dated 2026-11-10; blog stamped 2026-11-11; Artificial Analysis lists 2026-11-10; HF repo created 2026-11-03 | LICENSE, blog, AA, HF API | high |
| Official page | https://www.minimax.io/blog/minimax-h3-image | | high |
| Weights | https://huggingface.co/MiniMaxAI/MiniMax-H3-Image | | high |
| Lineage | Built on MiniMax H3, the open-weight video+audio model launched 2026-07-31. Same transformer design minus the audio layers, same text encoder | HF card, H3 blog | high |

Nearest names, to prevent mix-ups:

| Name | What it is | Conf. |
|---|---|---|
| MiniMax-H3-Image-Highspeed | API-only faster tier of the same model | high |
| MiniMax-H3-Image-PE | Official prompt expander (an LLM that rewrites a short prompt into the long caption the model wants), 17.9 GB | high |
| Pruna P-H3-Image | Third-party image model made from the H3 video weights, released 2026-11-03, one week before the official one | high |
| "H3 image" before 2026-11-10 | Community still-image use of the H3 video checkpoints (FL2VA, Ref2VA) | medium |
| image-01 | MiniMax's February 2025 image model, API-only, $0.0035 per image | high |
| "Hailuo Image 3" | No such product name found | medium |

Reddit: r/StableDiffusion had 50+ H3-Image threads between 2026-11-10 and 2026-11-12 (top scores 401, 389, 294). The owner almost certainly saw these.

## 2. Open weights or API

**Both. Weights are public and ungated** (HF API field `gated: false` on MiniMaxAI/MiniMax-H3-Image, Comfy-Org/MiniMax-H3-Image, Comfy-Org/MiniMax-H3). Conf. high.

### Official files (too large for this machine as shipped)

| Part | Size | Note |
|---|---|---|
| Diffusion transformer (DiT, the image-making network) | 66.28 GB, BF16, 33.1 B parameters | 6 sampling steps, guidance fixed at 1, negative prompts rejected |
| Text encoder Qwen3-VL-32B | 66.7 GB | Lives in the MiniMax-H3 repo, shared with the video model |
| Image VAE (the decoder from latents to pixels) | 2.34 GB | |
| Prompt expander PE | 17.9 GB | Optional |

### ComfyUI builds (Comfy-Org mirror repos, ungated)

| File | Size | Fits 24 GB VRAM |
|---|---|---|
| minimax_h3_image_pruned_int8_convrot (stock template DiT) | 20.98 GB | yes, tight at 16 MP |
| minimax_h3_image_pruned_w4a8 (4-bit weights) | 12.55 GB | yes |
| minimax_h3_image_pruned_bf16 | 40.23 GB | no |
| qwen3vl_32b_minimax_h3_int8_convrot (stock template text encoder) | 27.14 GB | no, spills to RAM |
| qwen3vl_32b_minimax_h3_nvfp4_awq (4-bit text encoder) | 15.69 GB | yes |
| qwen3.5_9b_w4a8_gptq (template prompt expander) | 7.34 GB | yes |
| minimax_h3_image_vae_fp16 | 1.17 GB | yes |

- ComfyUI support: native nodes and two templates (text-to-image, image edit). Needs ComfyUI 0.45.0+ and template pack 0.11.104+. No paid API nodes involved. Source: docs.comfy.org tutorial. Conf. high.
- Community GGUF builds exist (Abiray repo: Q4_K_M 11.57 GB, Q5_K_M 14.08 GB, ungated). Conf. high on existence, unknown on quality.
- Disk for a working set: about 37 GB (int8 DiT + 4-bit encoder + VAE) to 57 GB (stock template set with expander).

### Speed and memory reports (all anecdotal, single posters)

| Hardware | Result | Source |
|---|---|---|
| RTX 4090, int8 DiT | about 22 s per 16.6 MP image | r/StableDiffusion 1xtlj1t |
| RTX 4090, stock edit template | about 30 s per edit, 70 s with expander on | comment in 1xtuj87 |
| RTX 5080 16 GB VRAM + 192 GB RAM, int8 DiT + 4-bit encoder | median 23.9 s per 16 MP, 600 images, zero out-of-memory errors | jo-nike bench |
| RTX 4060 Ti + 32 GB RAM | about 60 s per 8 MP | 1xtuj87 |
| RX 9060 XT 16 GB + 64 GB RAM, W4A8 + 4-bit encoder | 35 to 43 s per 8.4 MP | 1xt50cj |

- Fit on 24 GB VRAM + 31.8 GB RAM (my inference, conf. low to medium): the stock template pair (20.98 + 27.14 = 48 GB) leaves about 2 GB of combined memory after Windows, so expect page-file swapping on every prompt change. The pair int8 DiT + 4-bit encoder (36.7 GB) or W4A8 DiT + 4-bit encoder (28.2 GB) is the safer start. No report from an exact 4090 + 32 GB machine was found.
- Resolution: trained around 16 MP, working range 4 to 20 MP. Multiple Reddit users report poor output at 1 MP. Plan on 4 MP minimum.

### API (for completeness; owner rejects paid APIs)

- Token-priced: $2.30 per M input text tokens, $1.50 per M input image tokens, $3.80 per M output image tokens. MiniMax's own examples: $0.0218 per 1K image, $0.0233 per 2K, $0.0688 per 4K (4K is half price until 2026-11-17 16:00 UTC). Conf. high.
- Needs an account, an API key and a prepaid balance. Free tier: not verified.

## 3. Quality evidence

### Artificial Analysis arenas (read 2026-11-12)

| Arena | H3-Image Elo (95% interval) | Rank | Top open-weight? | Z-Image Turbo |
|---|---|---|---|---|
| Text to image (AA-Image-T2I v2.1) | 1067 (1052 to 1082), 3,143 appearances | 23 of 112, rank range 21 to 24 | yes; next are Qwen-Image-2.1 at 1047 and FLUX 3 Image Klein at 1044 | 937, rank 77 of 112 |
| Image editing (AA-Image-Editing v2.1) | 1138 (1122 to 1154), 3,137 appearances | 12 of 83, rank range 8 to 17 | yes; next are Fibo 2.0 at 1085 and Qwen-Image-2.1 at 1084 | not listed |

- What it measured: blind pairwise preference votes by AA's "validated private evaluators" on AA's own prompt set, with the model served through an API. Leader is GPT Image 2.6 Sunburst (max) at 1262 (T2I) and 1210 (editing).
- What the 130-point gap to Z-Image Turbo means (my arithmetic from the Elo formula): H3-Image preferred in about 68% of head-to-head votes.
- What it does not show: the pruned int8 local build (AA tested the hosted full-precision model, probably with hosted prompt enhancement), comics or cel-animation fidelity, or consistency of one character across shots. The sample is 2 days old and about a quarter the size of older entries.
- MOSS-Image, the model Reddit compares it with most, is absent from the AA list.

### LMArena

Direct fetch returned HTTP 403 and search surfaced no H3-Image entry. **Not verified.**

### jo-nike H3-Image Bench (hobbyist, local int8 build, 600 prompts, graded by an AI reviewer against written checklists)

Single author, no replication, AI grader. Treat as a structured first look.

| Slice | Result |
|---|---|
| Round 1, 300 prompts reused from a MOSS benchmark | mean about 4.2 of 5 |
| Art styles set (50 images) | 4.24; 82.4% of 296 checks passed |
| Anime, cartoon, comics (n=13) | 4.38; manga page, 90s cel frame, key visual named as the strongest images; a second 90s-cel prompt came out as modern flat illustration |
| Print and graphic, incl. halftone comic, linocut, engraving (n=8) | 4.63 |
| Dry handmade media: chalk, charcoal, sketch (n=5) | 3.80, rendered too clean |
| Posters and vector design (n=7) | 3.57 |
| Round 2, 300 harder prompts | 3.67; 74% of 2,113 checks passed |
| Anatomy defects | 21 of 300 (round 1), 22 of 300 (round 2) |

### Reddit side-by-sides (opinions on posted galleries)

- "Minimax H3 Image vs Moss Image art styles" (score 51): top comment "Moss SFT wins all" (16 points). Several commenters prefer MOSS for styles.
- "MOSS-Image-SFT vs MiniMax-H3-Image, 10 art mediums, 1K" (48 comments): method rejected by commenters because H3-Image ran at 1 MP.
- VAE thread (score 162), top comment (83 points): the H3 VAE compresses 32x spatially where most image models use 16x; commenters estimate a 16 MP output carries the detail of a 2 to 4 MP image from other models. An estimate, unmeasured.
- "H3 FL2VA vs H3-Image character knowledge" (score 90): 4 test prompts show celebrity and franchise-character knowledge removed from H3-Image. Irrelevant for original characters.
- Recurring complaint: the stock ComfyUI template gives weak results; users switch sampler to LCM or Euler ancestral and render at 8 to 16 MP.

## 4. Capabilities for this project

| Need | Evidence | Conf. |
|---|---|---|
| Long prompts | 4,096 tokens locally; card says the model "expects a detailed English description of the whole image". Bench: captions of 200+ words scored 4.67 (n=3), under 40 words 3.60 (n=5) | high on limit, low on the trend (small n) |
| Object-headed, faceless characters | **No direct test found.** Adjacent: 1930s rubber-hose dancing teapot scored 5 of 5; "boulder for a head" golem scored 4; exclusions written into the prompt and tied to an object were honoured 28 of 30 times; official showcase has surreal scenes (a barber trimming a cloud). No negative prompt exists, so "no face" goes in the positive prompt | low |
| Comics, cel animation | Bench numbers above favour it; Reddit galleries favour MOSS for styles | medium |
| Period film stocks | 1930s film texture "lighter than asked"; lithograph posters come out as clean vector; one user likes its "technicolor" look. Period sets and costumes (1920s club, 1950s diner) scored 4 | low to medium |
| Legible text | Latin text: 23 of 28 images spelled every string right; one Reddit test 4 of 4 on a dense sign. Hebrew 0 of 5, Arabic 4 of 8. Clocks wrong 10 of 11 | medium |
| Character reference across shots | Up to 16 reference images addressed as `<Picture 1>` and up, same checkpoint. AA editing Elo is the best of any open model. Reddit is split: several users report the subject's likeness drifting and say the H3 video Ref2VA model holds it better; others get it to hold with the wording `<Subject 1> is fully preserved`. All reports concern human faces; object heads untested | medium on mechanism, low on outcome |
| LoRA route (a small trained add-on that fixes one character or style) | Fizgig 9.6 trains H3-Image LoRAs: about 23 GB with int8, 13 GB in 4-bit. Its author measured about 15% of a LoRA's effect lost under ComfyUI's default dynamic VRAM loading (fix: start ComfyUI with `--disable-dynamic-vram`). Single source | low to medium |
| Editing | Restyle, repose, relight reported working; repeated small edits degrade the image (one user). API has no masked edits | medium |

## 5. Licence and YouTube

Source: MiniMax-H3-Image Community License Agreement, read in full.

| Clause | Content | Effect here |
|---|---|---|
| Territory (I.3, I.5) | Licence covers the world except the EU, UK, South Korea and USA | Local use is licensed if the owner sits outside those four |
| Outputs (VI.4) | "MiniMax claims no rights over the Outputs you generate" | Owner keeps the images |
| V.4 | No use, distribution or display of the model "or any of their Outputs" outside the licensed territory | **Open question:** a YouTube upload is viewable inside the excluded territories. The text does not address online publication. MiniMax's own Q&A frames the restriction around deploying weights in those regions. Not legal advice |
| Acceptable Use 12 | Public posting needs clear disclosure that the content is machine-generated | YouTube's altered-content label plus a line in the description covers it |
| V.3 | Outputs may not train other AI models | No effect on video use |
| IV | Separate written authorisation if annual revenue exceeds $1 M or if hosting the model for others | No effect at hobby scale |
| Governing law | Hong Kong | |

- A Reddit commenter reports the authorisation form for excluded territories answered within 1 minute. The form sits behind a MiniMax platform account. Unverified.
- API output terms (MiniMax platform terms of service): not read.

## 6. Verdict for this owner

**Usable locally.** Ungated weights, native ComfyUI support, 4090-class speed around 22 to 30 s per image, and the strongest blind-vote score of any open-weight model on Artificial Analysis (130 Elo above Z-Image Turbo in text-to-image).

Three cautions before treating it as a replacement:

1. Memory: pick the int8 or W4A8 DiT with the 4-bit text encoder; the stock template pair overruns 31.8 GB RAM by my estimate.
2. Fit to the project is unproven: no faceless object-head test exists, style opinion is split against MOSS-Image, and reference consistency reports conflict.
3. Licence clause V.4 on outputs and excluded territories is unresolved for YouTube.

Suggested test, about 40 GB of downloads: the 10 existing decade prompts through H3-Image at 8 to 16 MP, then one character re-shot in comics and cel styles from a reference image, judged by eye against the Z-Image-Turbo set.

## Sources

- https://www.minimax.io/blog/minimax-h3-image
- https://minimax.io/blog/minimax-h3
- https://huggingface.co/MiniMaxAI/MiniMax-H3-Image
- https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE
- https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/discussions/3
- https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE
- https://huggingface.co/MiniMaxAI/MiniMax-H3
- https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/QA-about-License.md
- https://huggingface.co/api/models/MiniMaxAI/MiniMax-H3-Image?blobs=true
- https://huggingface.co/Comfy-Org/MiniMax-H3-Image
- https://huggingface.co/Comfy-Org/MiniMax-H3
- https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF
- https://huggingface.co/Woovee/MiniMax-H3-Image-LowVRAM
- https://huggingface.co/PrunaAI/P-H3-Image
- https://huggingface.co/PrunaAI/P-H3-Image-Comfy
- https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image
- https://blog.comfy.org/p/minimax-h3-image-is-now-available
- https://platform.minimax.io/docs/guides/image-generation.md
- https://platform.minimax.io/docs/pricing/overview.md
- https://artificialanalysis.ai/image/leaderboard/text-to-image
- https://artificialanalysis.ai/image/leaderboard/editing
- https://arena.ai/leaderboard/text-to-image (HTTP 403, not read)
- https://jo-nike.github.io/h3-image-bench/
- https://dzfarouk7.github.io/h3imagetest/ (288-style library, text only read)
- https://www.mindstudio.ai/models/minimax-h3-image-open
- https://arctic-shift.photon-reddit.com/api/posts/search (archive used for every Reddit item below)
- https://www.reddit.com/r/StableDiffusion/comments/1xt50cj/amazed_by_the_generation_speed_of_minimax_h3image/
- https://www.reddit.com/r/StableDiffusion/comments/1xtoutk/according_to_ostris_h3_image_has_a_vae_issue/
- https://www.reddit.com/r/StableDiffusion/comments/1xtojdr/minimax_h3_image_vs_moss_image_art_styles/
- https://www.reddit.com/r/StableDiffusion/comments/1xtjm4z/comparison_mossimagesft_vs_minimaxh3imagepruned_a/
- https://www.reddit.com/r/StableDiffusion/comments/1xtiv2z/h3_fl2va_vs_h3image_character_knowledge/
- https://www.reddit.com/r/StableDiffusion/comments/1xt090n/warning_with_h3_image_it_is_illegal_to_use_it/
- https://www.reddit.com/r/StableDiffusion/comments/1xsx45t/minimax_h3_image_is_about_to_clean_the_field_but/
- https://www.reddit.com/r/StableDiffusion/comments/1xszz5f/300_random_prompts_across_styles_on_minimax_h3/
- https://www.reddit.com/r/StableDiffusion/comments/1xsrphc/minimax_h3_image_is_natively_supported_in_comfyui/
- https://www.reddit.com/r/StableDiffusion/comments/1xtlj1t/minimaxh3image_at_16_mp_6_steps_20_s_per_image/
- https://www.reddit.com/r/StableDiffusion/comments/1xstb5n/minimax_h3image_vs_pruna_ai_h3image_quick_test/
- https://www.reddit.com/r/StableDiffusion/comments/1xtmknj/is_the_new_minimax_h3image_better_than_qwen_21/
- https://www.reddit.com/r/StableDiffusion/comments/1xsx9tq/minimax_h3_image_face_consistency_tips/
- https://www.reddit.com/r/StableDiffusion/comments/1xu1bpt/tried_minimax_h3_image_with_some_surreal_prompts/
- https://www.reddit.com/r/StableDiffusion/comments/1xsrnb0/tested_h3image_on_a_textheavy_sign_4_of_4/
- https://www.reddit.com/r/StableDiffusion/comments/1xtkg94/fizgig_96_train_loras_on_minimax_h3_image/
- https://www.reddit.com/r/StableDiffusion/comments/1xt9ocv/minimax_h3_image_20mp_workflow/
- https://www.reddit.com/r/StableDiffusion/comments/1xtuj87/first_testings_with_minimax_h3_image_i_am_happy/
- https://www.reddit.com/r/comfyui/comments/1xmyovx/new_image_model_based_on_minimax_h3_7_smaller_5/
- https://www.reddit.com/r/comfyui/comments/1xsu2rz/minimax_h3_image/
- https://www.reddit.com/r/comfyui/comments/1xtxqh0/h3_minmax_image_styles_library/
