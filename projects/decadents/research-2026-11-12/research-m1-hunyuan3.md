---
type: research
created: 2026-11-12
author: Agent m1
---

# HunyuanImage 3.0 (80B) via ComfyUI-HunyuanImage3 as a Z-Image-Turbo replacement

Read date for every web fact: 2026-11-12. Confidence tags: [H] high, [M] medium, [L] low.

## 0. Verdict

- **Fit: runs with pain. Replace Z-Image-Turbo: no.** [M]
- Choke point: 31.8 GB RAM against a ~50 GB working set (node README). It runs only by streaming weights from disk on every step.
- Evidence for 32 GB: 3 Reddit anecdotes say it works, 0 give a timed run on a 4090 + 32 GB. Speed on this PC is unmeasured.
- Expected speed on this PC: 1 to 3 min per image (my inference from the reports in section 5) [L]. Z-Image-Turbo on a 4090: about 2.3 s per 1024x1024 image (widely repeated secondary figure) [M-L].
- One capability Z-Image-Turbo lacks and this model has: instruction editing with 1 to 3 reference images.
- Licence is weaker than Z-Image-Turbo's Apache-2.0 for a global YouTube channel (section 4).
- Recommendation: keep Z-Image-Turbo for generation. Treat HunyuanImage 3.0 as an optional second-stage editor, and test Qwen-Image-2.1 for that role first (it outranks HunyuanImage 3.0 Instruct on both editing boards, section 6).

## 1. The Reddit thread

Source: Arctic Shift archive of post `1wzclz5` (reddit.com not read directly). 166 comments retrieved.

| Item | Value | Conf |
|---|---|---|
| Title | "...on a single 12-24 GB GPU..." The archive holds an en dash (U+2013) between 12 and 24. "1224 GB" = lost dash | H |
| Posted | 2026-10-06, r/StableDiffusion, u/LatentSpacer, score 777, 159 comments | H |
| Claim: speed | Instruct-Distil, ~1 MP: 4090 = 22-26 s (W4A8), 47-49 s (int8). 3090 = 29 s / 54 s. 4090 capped to 16 GB / 12 GB = ~30 s / ~32 s | H (that it is claimed) |
| Claim: RAM | "ComfyUI held about 50 GB with the 4-bit file loaded. This is the real requirement" | H |
| Claim: features | text-to-image, editing, fusion of up to 3 input images, optional prompt rewriting (~1 s per token), Spectrum speed-up (3.4x on 50-step models) | H |
| Claim: test size | 60 prompts x 2 formats, 60 edits, 14 styles, one seed each. "Most of the edits worked; a few didn't" | H |

W4A8 = weights stored in 4 bits, activations computed in 8 bits. int8 = 8-bit weights. Both shrink the model at some cost in fidelity.

Sceptical and critical comments:

| Theme | Comment (user) | 
|---|---|
| Speed dispute | "How on earth are you getting to 26s per image? On my 4090 with 64gb system ram, 4-bit W4A8 takes about 130s and int8 takes about 240 seconds" (Netsuko). 5x slower than the claim |
| Speed | 4070 Ti Super 16 GB + 64 GB RAM: ~2 min (PerAngusta-AdAugusta). 3060 12 GB, two input images: 2 min 17 s (Lucaspittol). Unstated GPU: 135 s, 72 s with Spectrum (CutLongjumping8) |
| RAM | "It takes 100Gb of system RAM on my side" (CutLongjumping8). "4-bit W4A8 takes about 54GB of RAM" (Lucaspittol). "excludes 90% of potential users as most have just 32GB" (bitzpua) |
| 32 GB | "It works on 32 gb ram .. with lot of disk activity" (SRWindMill). "It will work on 32gb ram easily for the W4A8 model... 7gb ram and 22gb vram in use" (cosmicr). 4060 8 GB + 32 GB: "under 3 mins per image" (luciferianism666). Author: "No idea... I never tested it" |
| Page file | "Using virtual memory is going to cause a lot of wear on your SSD" (alwaysbeblepping), who points to ComfyUI's `--fast-disk` |
| OOM | "how tf, i cannot get this to not OOM" (knoll_gallagher, hardware unstated) |
| Artefacts | "heavy horizontal stripes/line artifacts on most images" (AltruisticList6000). "That banding" (PATATAJEC). Banding in hair on an RTX 6000 Pro with int8 (roculus) |
| Text | "really bad at long form text" (Winougan). "80B training and doesn't know alphabet" (cadissimus). Author: "might struggle with text and complex layouts" |
| Quality | "much worse in every respect than the Krea 2 Turbo" (Odd_Fix2, contested in replies). "images that I would believe to be lucky gens from sdxl" (MobileCA). Author: "Krea 2 might have better quality but not as creative" |
| Hands | Wrong thumb / extra index finger in a gallery image (2 users) |
| Install | `ValueError: orig_shape must be 2D` fixed by updating ComfyUI (tehorhay). Thinking mode tensor-size error (OracleofEpirus). Prompt rewriting fails off 1024x1024 (jah-selassie). "batching is broken", no sampling preview (Kooky-Mode3047) |
| Rewriting | 1-2 s per token, 1,000-2,000 tokens for think mode. Author: "I think the prompt rewrite is what makes it score high on the benchmarks" |

Supportive counterpoints: "dramatically better at t2i and prompt following... compared to the full-fat Flux.2" (DelinquentTuna). "very good prompt adherence and good subject likeness preservation" with two inputs (Lucaspittol). "not a Qwen 2.1/Krea 2/Ideogram 4 killer, but a great model to have alongside them" (Hoodfu). All anecdotes, no shared test set. [H that they were said, L as evidence]

## 2. The node repo: PedroMarinhoDev/ComfyUI-HunyuanImage3

| Item | Value | Conf |
|---|---|---|
| What | Native ComfyUI nodes: stock KSampler (ComfyUI's sampling node), stock VAE Decode, ComfyUI's own memory manager. No wrapper around Tencent's pipeline | H |
| Age | Created 2026-09-23 (50 days). 7 commits, 1 author, last push 2026-10-25 | H |
| Traction | 44 stars, 5 forks, 1 open issue (a macOS patch), 3 closed. Comfy Registry: 12 downloads | H |
| Licence | Code GPL-3.0. Ported model code and weights stay under the Tencent Hunyuan Community License | H |
| Install | `git clone` into `ComfyUI/custom_nodes`, restart. `requirements.txt` is empty: nothing to pip install. Also in ComfyUI-Manager / Registry as `hunyuanimage3-native` | H |
| Registry flag | Version 0.1.0 has status `NodeVersionStatusFlagged`. The 6 automated findings: env-variable reads, one `subprocess.run` in the optional `tools/convert_all.py`, one false match in a JS file. Manager install may be blocked or warned; git clone is unaffected | H findings, L Manager behaviour |
| Needs | ComfyUI core from 2026-09-24 or later (node `__init__.py`). W4A8 at full speed needs core v0.38.0+ (released 2026-09-29) per PR #2 | H |
| Quantisation | W4A8 with ConvRot (a rotation applied before quantising) and per-expert codebooks; int8 ConvRot; bf16 (unquantised 16-bit). No GGUF, no NF4, no block swap. Streaming is ComfyUI Dynamic VRAM (`comfy-aimdo`, an allocator that loads weights to the GPU on demand) plus one-layer lookahead | H |
| Fidelity cost | W4A8: 7.3% weight error, image SSIM 0.738 vs bf16. int8: 1.0%, SSIM 0.844 (SSIM = pixel similarity, 1 = identical). Author: SSIM here measures "same picture", and says nothing about quality | H (author-measured) |
| VRAM | 24 GB tested. Peak 15.9 GB and 11.6 GB when capped to 16 / 12 GB | H (author-measured) |
| RAM | ~50 GB held with W4A8, tested on a 188 GB machine. "a smaller card still needs the same ~50 GB of free RAM" | H (author-measured) |
| Disk | 45 GB for W4A8 "on a fast SSD" | H |
| Speed, 4090 | Author's rig: PCIe 4.0 x8, 188 GB RAM, 1024x1024. Table below | H (author-measured, unreplicated) |
| Remote code | Static read of the 14 runtime `.py` files on `main`: no `trust_remote_code` (a flag that runs Python shipped inside a model repo), no `torch.load`, no pickle (a file format that can execute code on load), no network or subprocess calls. Weights load as safetensors (a data-only tensor format) | H for files read |
| Negative prompt | None. "The encoders make the negative prompt themselves... there's no second text box to fill" | H |
| LoRA | No LoRA code in `nodes.py`. A third-party trainer fork exists (envy-ai/ai-toolkit-envy-optimized); its author says 64 GB RAM minimum for the 4-bit model | H / M |

Speed on the author's 4090 (188 GB RAM):

| Model | Format | Cold first image | Warm image |
|---|---|---|---|
| Instruct-Distil, 8 steps | W4A8 | 39 s | 26 s |
| Instruct-Distil, 8 steps | int8 | 1 min 10 s | 49 s |
| Instruct, 50 steps | W4A8 | 5 min 23 s | 5 min 08 s (1 min 30 s with Spectrum) |
| Base, 50 steps | W4A8 | 5 min 14 s | 4 min 58 s (1 min 27 s with Spectrum) |
| Prompt rewriting | any | +4 to 5 min for ~300 tokens (0.8-0.9 s per token) | same |

Known issues in the README: an edit that reuses the input image's seed comes out overbaked or as colour noise; above 2048x2048 the output is noise; the large-image nodes are experimental.

## 3. The HuggingFace repos

Three repos, same layout: `PedroMarinhoDev/HunyuanImage-3.0-Instruct-Distil-ComfyUI`, `-Instruct-ComfyUI`, `-Base-ComfyUI`.

| File (Distil repo) | Size | Needed for |
|---|---|---|
| `hunyuan_image_3_instruct_distil_w4a8.safetensors` | 46.91 GB | everything (recommended) |
| `..._int8_convrot.safetensors` | 81.85 GB | higher fidelity; too large for this PC's RAM |
| `..._bf16.safetensors` | 161.62 GB | reference only |
| `..._cot_head.safetensors` | 1.09 GB | prompt rewriting only |
| `vae/hunyuan_image_3_vae_fp16.safetensors` | 2.52 GB | always |
| `vae/..._fp32.safetensors` | 5.04 GB | optional |
| `clip_vision/..._siglip2_so400m_naflex.safetensors` | 0.90 GB | editing only |

- Minimum set for generation + editing: 46.91 + 2.52 + 0.90 = 50.3 GB. With rewriting: 51.4 GB. Fits C: (257 GB free) and D: (75 GB free). [H]
- Gating: `gated: false` on all 3 repos (HF API). Anonymous test: unauthenticated request for the W4A8 file returned HTTP 302 to the CDN with `user_id=public`. No login, no licence click. [H]
- Upstream `tencent/HunyuanImage-3.0`, `-Instruct`, `-Instruct-Distil`: also `gated: false`. [H]
- Licence tag: `tencent-hunyuan-community`. Pure safetensors, no pickle files. [H]
- No W6A8 file as of today, although the author wrote on 2026-10-09 that one was in progress. HF repos last modified 2026-09-24. [H]

## 4. Upstream: Tencent HunyuanImage-3.0

| Item | Value | Conf |
|---|---|---|
| Architecture, one sentence | A large language model (64-expert mixture-of-experts, where a router sends each token to 8 of 64 sub-networks) that produces images inside the same network that reads the prompt, so it has no separate text encoder | H |
| Parameters | 80B total, 13B active per token | H |
| Released | Base 2025-09-28. Instruct and Instruct-Distil 2026-01-26. Repo: 3,300 stars, 56 open issues, last push 2026-06-23 | H |
| Official hardware | Base: 3 x 80 GB VRAM. Instruct and Instruct-Distil: 8 x 80 GB VRAM | H |
| Variants | Base (text-to-image, 50 steps). Instruct (adds editing, up to 3 input images, self-rewrite, chain-of-thought "think" mode, 50 steps). Instruct-Distil (same features, 8 steps). No separate "edit" checkpoint; editing lives in Instruct | H |
| Upstream loader | Uses `trust_remote_code=True`. The ComfyUI node avoids it | H |
| Newer sibling | HunyuanImage 3.5 (Preview), Sep 2026: API only, no weights on Tencent's HF listing | H |
| Vendor evals | GSB (good/same/bad human pairwise rating, 1,000 prompts, 100+ raters) and SSAE (a vision-language model scores 3,500 key points). Vendor-run; I found no independent replication | H / M |

Licence (Tencent Hunyuan Community License, node copy byte-identical to upstream by SHA-256):

| Question | Answer | Clause | Conf |
|---|---|---|---|
| Commercial use | Allowed. Above 100 million monthly active users a separate licence is required | 2, 4 | H |
| Territory | Worldwide minus the European Union, United Kingdom, South Korea | 1(l) | H |
| Israel | Inside the Territory | 1(l) | H |
| Output ownership | "Tencent claims no rights in Outputs You generate" | 6(d) | H |
| Output display | "You must not use, reproduce, modify, distribute, or display the Tencent Hunyuan Works, Output or results... outside the Territory" | 5(c) | H |
| YouTube | No YouTube clause. A public upload is viewable in the EU, UK and South Korea, which a literal reading of 5(c) forbids. Untested legally; I am no lawyer | 5(c) | M |
| AI labelling | Public posting must "expressly and conspicuously" identify the content as machine generated | Exhibit A, item 12 | H |
| Training on outputs | Outputs may not be used to improve any non-Hunyuan AI model (rules out LoRAs for Z-Image trained on its outputs) | 5(b) | H |
| Governing law | Hong Kong | 9 | H |

Z-Image-Turbo and Z-Image for contrast: `license:apache-2.0`, ungated (HF API). [H]

## 5. Fit for this machine

| Resource | Have | Need | Result |
|---|---|---|---|
| VRAM | 24 GB | 12 GB+ (22 GB used in one report) | passes |
| Disk | C: 257 GB, D: 75 GB | 50.3 GB | passes; the drive must be NVMe for `fast_disk` |
| RAM | 31.8 GB | ~50 GB (README), 54 GB (one user) | 18 GB short; disk streaming required |
| ComfyUI | Desktop, version unknown | core v0.38.0+ | check. The legacy "ComfyUI Desktop" repo is archived at core 0.22.3 (May 2026). The successor "Comfy Desktop" is at v1.1.9 (2026-11-06) |

How 32 GB can work:
- `fast_disk` = ComfyUI mode that maps the weight file from an NVMe drive and streams it to the GPU, with no pinned copy in RAM. Auto-detected since core v0.37.0; all loaders since v0.38.0; flag `--fast-disk` forces it. Windows detection goes through `comfy_aimdo.storage.fast_disk`. [H]
- The node adopted it on 2026-10-09 (commit `db6a293`). Measured by a third party on a 96 GB-VRAM card: ComfyUI's RAM fell from ~50 GB to 7 GB. Author on his 4090: "same speed, 10-16 GB less RAM". [H that reported, M for transfer to this PC]
- With fast_disk off, ComfyUI builds a pinned 44 GB RAM copy. On 31.8 GB that lands in the page file (disk space Windows uses as overflow RAM): heavy SSD writes, or an out-of-memory stop. [M]
- With fast_disk on, about 45 GB of weights move per step and roughly 20 GB can stay in VRAM. The rest re-reads from disk or the file cache every step. Reads cause no SSD write wear. [M, inference]

Evidence for and against at 32 GB:

| Direction | Evidence | Weight |
|---|---|---|
| For | 3 thread users report 32 GB runs (one "lot of disk activity", one "7gb ram and 22gb vram in use", one 4060 8 GB at "under 3 mins") | anecdote, no 4090 timing |
| For | PR #2 numbers: 7 GB process RAM with fast_disk | measured, different hardware |
| Against | README and HF card: ~50 GB of free RAM needed | author-measured, written before the fast_disk commit |
| Against | 64 GB + 4090 user got 130 s per image, 5x the claim | anecdote, ComfyUI version unstated |
| Against | One OOM report, hardware unstated | anecdote |

Unknowns on this PC that decide the speed: installed ComfyUI core version, whether the model drive is NVMe, the 4090's PCIe link width (author's is 4.0 x8), free RAM after Windows and Edge.

Other costs: the local Qwen `llama-server` cannot share the GPU with it (22 GB VRAM in use). 50-step Instruct or Base at ~5 min per image on a 188 GB machine is impractical here. Prompt rewriting adds 4-5 min per image.

## 6. Quality evidence

What the two arenas measure: blind pairwise human preference votes on arena-chosen prompts, run against hosted API versions at full precision, aggregated to an Elo score (a rating where a 100-point gap means the higher model wins about 64% of pairings). What they leave unmeasured: the local W4A8 8-step build without rewriting, long-prompt adherence, style range, cross-shot consistency.

Text-to-image:

| Model | LMArena (mirror scraped 2026-11-10, 84 models) | Artificial Analysis (read direct 2026-11-12) |
|---|---|---|
| HunyuanImage 3.0 | 1151.6, rank 35 | 994 ±15 rank 58 (Tencent Cloud); 935 ±16 rank 78 (other host) |
| HunyuanImage 3.0 Instruct | not listed separately | 987 ±12, rank 64 |
| Z-Image-Turbo | 1081.9, rank 61 | 937 ±11, rank 77 |
| Z-Image Base | not listed | 896 ±16, rank 92 |
| Qwen-Image-2.1 (open weights) | 1226.8, rank 21 | 1047 ±12, rank 26 |
| FLUX.2 [dev] | 1145.1, rank 40 | 1000 (anchor), rank 52 |
| Qwen-Image (2512) | 1123.9, rank 47 | Qwen Image: ~903 |
| Krea 2 Turbo / Medium | 1115.6 / 1128.1 | Krea 2 Medium Turbo 1021 |
| Top open-weights (AA's own line) | n/a | H3-Image 1067, Qwen-Image-2.1 1047, FLUX 3 Image Klein 1044 |

Image editing:

| Model | LMArena Image Edit (mirror, 2026-11-10, 63 models) | Artificial Analysis editing (2026-11-12) |
|---|---|---|
| HunyuanImage 3.0 Instruct | 1301.4, rank 32 | 1064 ±13, rank 36 |
| Qwen-Image-2.1 | 1362.9, rank 22 | 1084 ±13, rank 29 |
| FLUX.2 [dev] | 1224.2, rank 47 | 1000 (anchor), rank 54 |
| FLUX.2 [klein] 9B | 1224.5, rank 45 | 1014 ±12, rank 49 |
| Qwen-Image-Edit (2511) | 1233.1, rank 43 | 996 ±16, rank 57 |
| Z-Image-Turbo | absent (no editing) | absent |

Reading these:
- Measured: hosted HunyuanImage 3.0 beats hosted Z-Image-Turbo by 70 Elo on LMArena and by 57 on Artificial Analysis in its Tencent Cloud hosting; on the other AA hosting the two tie (935 vs 937). [H]
- The same model scores 994 and 935 on two hosts, a 59-point spread from hosting configuration alone. The local W4A8 8-step build has no arena score. [H / inference]
- Popular claim "tops the leaderboard, beats Nano Banana" (SCMP, Oct 2025): true for a preliminary LMArena snapshot on 2025-10-03; rank 35 of 84 today. [H]
- lmarena.ai returned HTTP 403 to automated fetch; LMArena numbers come from the benchmarklist.com mirror. [H]
- Independent head-to-head against Z-Image-Turbo with shared prompts and seeds: none found. BudgetPixel (2025-12-29) calls Hunyuan "premium polish", Z-Image-Turbo "speed + cost king", Qwen-Image best at text; a vendor blog with no scoring method. [L]

## 7. Capabilities for the character project

| Need | Finding | Conf |
|---|---|---|
| Long prompts | Vendor: "thousand-character level complex semantic understanding". The text reader is the 80B LLM itself. No independent long-prompt test found | L |
| Object-for-head, faceless characters | No evidence either way. One user: "smart with complex artistic concepts". Needs a direct test | L |
| Style range (comics, cel, film stocks) | Author ran 14 style transfers with a photo + style reference image; Tencent showcases 3D plush and poster styles. No test of period film stocks or cel animation found | L |
| Legible text | Vendor claims precise text. Local W4A8 users and the node author report weak long text and layouts. Qwen-Image family is the stronger text model per BudgetPixel | M |
| Editing | Instruction edits ("turn this photo into a watercolor"). Author's run: most of 60 edits worked, a few failed | M |
| Reference input for one character across shots | Up to 3 input images, addressed as "the first image", "the second image". `vit_strength` and `latent_strength` set how hard the inputs steer. One user reports good likeness preservation with two inputs. Each extra image slows every step. Multi-turn interaction is unchecked on Tencent's roadmap | M |
| Negative prompts | Absent in this node. Distil runs a single pass at cfg 1.0 (cfg = strength of the pull toward the prompt). Instruct and Base use the model's own empty prompt as the negative | H |
| LoRA for a fixed character | Trainer fork needs 64 GB RAM for the 4-bit model: out of reach on this PC | M |
| Resolution | ~1 MP native in 37 aspect shapes; up to 2048x2048 with drift; 2x upscale pass documented | H |
| Batch and preview | One user reports batching broken and no step preview | L |

## 8. Not verified

- Any run on this PC. Nothing was installed or downloaded.
- The installed ComfyUI core version, the drive type, the PCIe link width.
- reddit.com itself (archive copy, comment scores as of ~2026-10-16).
- Whether ComfyUI-Manager refuses a registry version with the Flagged status.
- H3-Image (Artificial Analysis's top open-weights entry): outside this brief; it and Qwen-Image-2.1 both outrank HunyuanImage 3.0 on both boards.

## Sources

- Thread (archive): https://arctic-shift.photon-reddit.com/api/posts/ids?ids=1wzclz5
- Thread comments (archive): https://arctic-shift.photon-reddit.com/api/comments/search?link_id=1wzclz5&limit=100
- Thread (original, not fetched): https://www.reddit.com/r/StableDiffusion/comments/1wzclz5/hunyuanimage_30_80b_running_natively_in_comfyui/
- Node repo: https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3
- Node repo metadata: https://api.github.com/repos/PedroMarinhoDev/ComfyUI-HunyuanImage3
- Node PR #2 (fast_disk, v0.38.0 note): https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3/pull/2
- Node PR #3 (grouped MoE, 4090 timings): https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3/pull/3
- Node issue #1 (codebook error): https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3/issues/1
- Node comparison page: https://pedromarinhodev.github.io/ComfyUI-HunyuanImage3/
- Comfy Registry entry and scan findings: https://api.comfy.org/nodes/hunyuanimage3-native/versions?include_status_reason=true
- HF author: https://huggingface.co/PedroMarinhoDev
- HF weights (Distil): https://huggingface.co/PedroMarinhoDev/HunyuanImage-3.0-Instruct-Distil-ComfyUI
- HF weights (Instruct): https://huggingface.co/PedroMarinhoDev/HunyuanImage-3.0-Instruct-ComfyUI
- HF weights (Base): https://huggingface.co/PedroMarinhoDev/HunyuanImage-3.0-Base-ComfyUI
- HF file tree API (sizes): https://huggingface.co/api/models/PedroMarinhoDev/HunyuanImage-3.0-Instruct-Distil-ComfyUI/tree/main?recursive=true
- Tencent repo: https://github.com/Tencent-Hunyuan/HunyuanImage-3.0
- Tencent HF: https://huggingface.co/tencent/HunyuanImage-3.0 , https://huggingface.co/tencent/HunyuanImage-3.0-Instruct , https://huggingface.co/tencent/HunyuanImage-3.0-Instruct-Distil
- Tencent licence: https://huggingface.co/tencent/HunyuanImage-3.0/blob/main/LICENSE
- Technical report: https://arxiv.org/abs/2509.23951
- ComfyUI flags (`--fast-disk`): https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/cli_args.py
- ComfyUI fast-disk detection: https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/storage.py
- ComfyUI releases (v0.37.0, v0.38.0 notes): https://github.com/Comfy-Org/ComfyUI/releases
- Dynamic VRAM blog: https://blog.comfy.org/p/dynamic-vram-in-comfyui-saving-local
- Legacy Desktop repo (archived): https://github.com/Comfy-Org/desktop
- Comfy Desktop (successor): https://github.com/Comfy-Org/Comfy-Desktop
- Artificial Analysis text-to-image: https://artificialanalysis.ai/image/leaderboard/text-to-image
- Artificial Analysis editing: https://artificialanalysis.ai/image/leaderboard/editing
- LMArena text-to-image mirror: https://benchmarklist.com/arenas/arena_ai_text_to_image/
- LMArena image-edit mirror: https://benchmarklist.com/arenas/arena_ai_image_edit/
- Artificial Analysis mirror: https://benchmarklist.com/arenas/artificial_analysis_text_to_image/
- LMArena (HTTP 403 to automated fetch): https://lmarena.ai/leaderboard/text-to-image
- SCMP launch coverage: https://www.scmp.com/tech/big-tech/article/3328003/tencents-ai-model-hunyuan-image-30-tops-leaderboard-beating-googles-nano-banana
- BudgetPixel comparison: https://budgetpixel.com/blog/best-open-source-image-models-right-now-hunyuan-image-3-vs-qwen-image-vs-z-image-turbo
- Scenario overview (vendor claims restated): https://help.scenario.com/articles/8571674678-hunyuan-image-3-0-the-essentials
- Z-Image-Turbo HF (licence tag): https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
- Z-Image HF: https://huggingface.co/Tongyi-MAI/Z-Image
- Z-Image-Turbo 2.3 s figure: https://comfyui-wiki.com/en/news/2025-11-27-alibaba-z-image-turbo-release
- LoRA trainer fork: https://github.com/envy-ai/ai-toolkit-envy-optimized
