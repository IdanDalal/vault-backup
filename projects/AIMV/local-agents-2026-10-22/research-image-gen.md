---
type: research
created: 2026-10-22
author: jep
project: AIMV / Knowledge Cutoff
---

# Local image generation for Knowledge Cutoff (4090, Oct 2026)

Scope: web research only, nothing installed. Confidence per claim: H = primary source (model card, HF API, vendor docs) / M = one credible secondary or community measurement / L = SEO blog, extrapolation, or conflicting sources. "Gated" checked against the HF API `gated` field on 2026-10-22 unless noted.

## 0. Verdict

- Top pick: **Qwen-Image-Edit-2511** (edit targets, micro-type survives) + **Z-Image-Turbo** (textures, boards; already used on this PC). Both Apache 2.0, both ungated. [H license/gating]
- Fast alternate: **FLUX.2 [klein] 4B** (Apache 2.0, ungated, ~1 s/1024px on a 4090, gen + edit in one model). [H license, M speed]
- Strongest open-weights quality now: FLUX 3 Image Klein (Elo #1 open, 2026-10-15) and Qwen-Image-2.1, both blocked for us: FLUX 3 Klein is HF click-through gated; Qwen-Image-2.1 is a research (non-commercial) license. [H]
- Video models: no use at 4K 60 fps. 720p/24 fps, 5 s clips, ~25-40 s each on a 4090; upscale + interpolation to 4K60 would read worse than the code render. [M]
- Ranked uses: (1) edited "detail target" crops for agents, (2) tileable texture atlas feeding the detail kit, (3) style boards / concept frames per plate before coding. Section 5.

## 1. Image models on a 24 GB 4090

Notes for all rows: NVFP4 files target Blackwell FP4 hardware; on a 4090 use fp8 / int8 / bf16 (NVFP4 loads but can run up to 2x slower than FP8) [M, Comfy blog]. int8 "convrot" builds are native in recent ComfyUI and reported faster than FP8 on 40-series (informal, no numbers) [L].

| Model (release) | Size | VRAM at usable quant | s / 1024px on 4090 | Strengths | License | Weights / gating |
|---|---|---|---|---|---|---|
| **Z-Image-Turbo** (Tongyi, 2025-11-25) | 6B, 8 steps, CFG 1 | bf16 ~12.3 GB file fits 16 GB; fp8 6.15 GB; GGUF Q4 ~5 GB | ~2.3 s (up to 3.4 s) bf16 [M] | photoreal, environments, bilingual text OK; flat low-contrast with default euler; no negative prompt | Apache 2.0 [H] | Comfy-Org/z_image_turbo **ungated** [H]; Tongyi-MAI/Z-Image (base, 2026-01-23) ungated Apache [H] |
| **FLUX.2 [klein] 4B** (BFL, 2026-01-14) | 4B, gen + edit unified | ~8 GB fp8 floor, ~13 GB listed | ~1 s [M, steps unstated] | speed, editing, multi-ref; short English text only; fine detail weaker | Apache 2.0 [H] | black-forest-labs/FLUX.2-klein-4B **ungated** (gated:false) [H]; Comfy-Org/vae-text-encorder-for-flux-klein-4b ungated [H] |
| FLUX.2 [klein] 9B (2026-01) | 9B | ~24-29 GB (L, conflicting) | n/a | better than 4B (Elo 929 vs 837) | FLUX Non-Commercial [M] | skip: NC + tight fit |
| FLUX.2 [dev] (2025-11) | 32B | fp8 ~32 GB; 4090 needs GGUF Q4 (~19 GB) or offload [M] | not measured; FLUX.1-dev fp8 was 6.6-11 s at 20 steps [M] | top open quality class (Elo 1000), multi-ref edit, 4 MP | FLUX Non-Commercial [M] | Comfy-Org/flux2-dev ungated (fp8mixed) [H]; turbo LoRA in repo |
| **Qwen-Image-Edit-2511** (2025-12-17) | 20B MMDiT | GGUF Q4_K_M 13.1 GB (unsloth); fp8 + Lightning fused checkpoint exists | not measured on 4090; Lightning 4-step claims ~10x vs 40 steps [M] | instruction edits that preserve layout and text; best Apache editor for typography | Apache 2.0 [H] | Qwen/Qwen-Image-Edit-2511 **ungated** [H]; Comfy-Org/Qwen-Image-Edit_ComfyUI; unsloth GGUF; lightx2v/Qwen-Image-Edit-2511-Lightning |
| Qwen-Image-2512 (2025-12-30) | 20B | GGUF 7.8-16.9 GB + 5.1 GB text encoder [H byteshape] | n/a | strong text rendering, Elo 903 for original Qwen-Image | Apache 2.0 [M] | Comfy-Org/Qwen-Image_ComfyUI; unsloth / byteshape GGUF |
| **Qwen-Image-Layered** (2025-12-17) | 20B | not stated | n/a | splits an image into N RGBA layers (3/4/8 in examples), 640 px recommended | Apache 2.0 [H] | Qwen/Qwen-Image-Layered, no gate shown [M] |
| Qwen-Image-2.1 (+Turbo 2026-10-09) (2026-09-14) | 7B DiT, pipeline 16.2B | int8 Turbo ~17-18.6 GB peak on 4090 [M] | Turbo int8 ~4 s at 1024x1536; base ~20 s [M] | #2 open T2I (Elo 1042, 2026-10-20); native RGBA transparency; up to 10 refs; masks; 2K+ | **Qwen Research License = non-commercial** [H name, M terms] | Comfy-Org/Qwen-Image-2.1 ungated [H]; blocked by license if the video monetizes |
| FLUX 3 Image Klein (BFL, 2026-10-15) | 5.6B gen | bf16 11.2 GB, fp8 5.6 GB, int8 runs on 8 GB [H] | ~4 s on 5090 int8, <9 s on 4070 (16 steps) [H vendor] | #1 open T2I (Elo 1117); native 4K; 10 refs; bounding-box edits | FLUX Kommunity: free commercial under $5M revenue [H] | **gated** (HF `gated: auto`, accept license; also flux-3-image-klein-comfy gated) [H]; only unofficial mirrors (Rin247, 2 downloads, created 2026-10-21) [H]; needs ComfyUI >= 0.41 [H] |
| Krea 2 Turbo (2026-06-22) | 12.9B, 8 steps | fp8 ~12.8-13 GB weights, 16 GB floor [M] | not measured on 4090 (4060 Ti: fp8 19.5 s, int8 12.4 s) [M] | photoreal, style fidelity, 9 style LoRAs incl. `style_reference`, `dotmatrix`, `vintagetarot` | Krea 2 Community: commercial free under $1M revenue and 50 seats; mandatory content filtering [M] | krea/Krea-2-Turbo **gated** [H]; Comfy-Org/Krea-2 **ungated** mirror (fp8/int8/bf16 + LoRAs) [H] |
| Ideogram 4.0 (2026-06-03) | 9.3B | nf4 ~10 GB, fp8 ~13 GB (L, conflicting) | n/a | strongest open typography, JSON layout, hex palette conditioning | **non-commercial** agreement [H] | Comfy-Org/Ideogram-4 ungated [H]; official repo gated [M] |
| HiDream-O1-Image (2026-05-08) | ~8B pixel-level | fp8 ~10 GB (community) [L] | n/a | Elo 975; full (50 steps) + Dev (28 steps) | MIT [H] | Comfy-Org/HiDream-O1-Image ungated [H] |
| ERNIE-Image (Baidu, 2026-04-15) | 8B DiT (15.8B pipeline) | bf16 on 24 GB recommended [M] | n/a | text in images; Turbo 8-step (Elo 914) | Apache 2.0 [H] | Comfy-Org/ERNIE-Image ungated [H] |
| Bria Fibo 2.0 (2026-10-20) | 8B gen + edit | n/a | n/a | #1 open edit (Elo 1087 claimed), trained only on licensed data (Bria's claim) | non-commercial (CC BY-NC per one source) [M] | briaai auto-gate [M] |
| HunyuanImage 3.0 (2025-09) | 80B MoE (13B active) | ~80 GB int8 [L] | n/a | Elo 989, long prompts | Tencent community | does not fit 24 GB |
| SD3.5 Large (2024-10) | 8.1B | ~12 GB fp8 | n/a | superseded | Stability Community | skip |

Leaderboard (Artificial Analysis arena, open weights, snapshot 2026-10-20 via theopenweights.com): FLUX 3 Image 1117, Qwen-Image-2.1 1042, FLUX.2 dev 1000, Qwen Image 2.0 990 (API only), HunyuanImage 3.0 989, HiDream-O1 975, FLUX.2 klein 9B 929, ERNIE Turbo 914, Qwen Image 903, FLUX.2 klein 4B 837. [M; arena Elo scales differ between snapshots]

License filter for this project: MiniMax-Music3 track + YouTube upload. If the channel monetizes, treat it as commercial use: keep to Apache / MIT (Z-Image, Klein 4B, Qwen-Image-Edit-2511, Qwen-Image-Layered, ERNIE, HiDream-O1) or small-business tiers (Krea 2 under $1M, LTX under $10M). [H for license texts; the "monetized YouTube = commercial" reading is jep's, not legal advice]

## 2. Ways image generation can feed the procedural engine

### 2a. Tileable textures as shader inputs (sampler2D)
- Targets: paper fibre field, cut-paper edge fray, ink bleed / pooling, scan dust and hair, foxing / age stains, cardstock tooth, newsprint show-through. Keep halftone, registration offset and print gain procedural: they are exact, resolution-free and animatable in GLSL; a raster version adds nothing. [jep judgment]
- Tiling on DiT models: classic circular-padding nodes patch U-Net Conv2d only; on DiTs (Flux, Z-Image) they "produce no tiling at all". [M, ComfyUI-Universal-Seamless-Tiles README]
- Working routes: (1) latent rolling during sampling + circular VAE decode (OliverCrosby/ComfyUI-Universal-Seamless-Tiles, lists Flux, Wan) [M]; (2) per-step latent circular padding (mikemojen/ComfyUI-seamless_latent_tiling, lists z-image-turbo) [M]; (3) post-pass offset + inpaint seams (SparknightLLC/ComfyUI-MakeSeamlessTexture) [M]. Seams and uneven lighting still occur; plan a high-pass / flatten step. [M]
- Pipeline sketch: Z-Image-Turbo 1024-2048 px tile → seam fix → luminance flatten (high-pass, normalize mean) → SeedVR2 or 2x upscale to 4096 → pack channels (R fibre, G stain, B edge noise, A dust) → one RGBA texture, sampled at 2-3 scales with rotation per instance to kill repetition. 4096^2 RGBA8 = 64 MB GPU each; 4-6 textures fine on 24 GB. [jep design; arithmetic H]
- Material maps: Marigold v2 (Comfy-Org/marigold-v2-0, 2026-09-10, ungated listing) or Lotus via ComfyUI-TextureAlchemy / QFX-PBRGenerator give normal + height from the colour tile, so paper relief can catch the scene light in the shader. [M]
- Divergence worth testing first: real CC0 scans. ambientCG: 1,300+ CC0 seamless materials, most at 8K, no sign-up per third party [M]; texturecan.com has PBR paper sets [M]. A real scan carries true multi-scale paper statistics with zero AI provenance. Generate only what scans lack (specific stains, cut edges, ink behaviour).
- Real precedents (no WebGL-specific published example found; adjacent pipelines): Dream Textures, Stable Diffusion seamless textures inside Blender's shader editor, plus DeepBump normals (2022-2023) [H]; ComfyTextures, ComfyUI texturing for Unreal [M]; StableGen, Blender + ComfyUI projection texturing [M]; StreamDiffusionTD, diffusion driven live by audio inside TouchDesigner shader networks [M]; three.js ShaderTexture (fragment shader → diffuse/roughness/normal maps) shows the receiving side [M].

### 2b. Style-reference boards and concept frames before coding a plate
- Bulk boards: Z-Image-Turbo at ~2-3 s/image = ~100 variants in ~5 min per plate (calendar leaf, hourglass, globe, letter). [M speed]
- Reference-conditioned: FLUX.2 klein 4B multi-ref, or Krea 2 `style_reference` LoRA (Comfy-Org/Krea-2), to push toward the 5 reference videos' look without copying frames. [H files, L quality]
- Use: the coding agent gets a picture of the target density (layers, line-weight hierarchy, fill breakup) instead of prose. Matches the AIMV rule "foundation before art, reference-level ceiling".

### 2c. Edit rendered frames to show agents a target ("paint-over")
- Input: a 1:1 1024 crop of our 4K frame (the documented "vector-flat" region). Edit prompt: add fibre, uneven ink, overprint, secondary hatching, micro-type wear; keep layout. Output: a target crop. Agent diffs ours vs target and writes shader code to close the gap.
- Model: Qwen-Image-Edit-2511 (layout and text preservation, Apache, ungated; Lightning 4-step fp8 fused checkpoint) [H files, M speed]; FLUX.2 klein 4B edit as the ~1 s draft. Qwen-Image-2.1 masks/circles would be better but NC. [H]
- Nothing generated ships in the final frames, so no new provenance or disclosure question.
- Qwen-Image-Layered can split a target crop into RGBA layers: tells the agent how many paper layers the target implies. [H capability, L usefulness]

### 2d. Upscalers for stills
- SeedVR2 (ByteDance, Apache 2.0): Comfy-Org/SeedVR2 ungated, 3B and 7B, fp16/fp8/int8, native ComfyUI image template since 2026-06 [H]. On a 4090: batch 1 max, 3B needs >= 18 GB, 7B fp8 has quality issues (use 7B fp16 + BlockSwap) [M]. Measured: 3B fp8, 5 frames 512x768 → 1080x1620 in 14.66 s on a 24 GB card [M].
- Use for texture tiles (2a) and board stills. Avoid on final video: 11,640 frames at 4K, extrapolated ~10-15 s/frame from the figure above = 30-50 h, and hallucinated texture would shimmer on micro-type. [L, jep extrapolation]

### 2e. Copyright and disclosure
- YouTube altered/synthetic policy: disclosure required for realistic content and for "AI generated music" that is "the main focus of the video"; exempt: clearly unrealistic/animated content, VFX and filters, backgrounds, production help (scripts, thumbnails, infographics). [H, YouTube Help 14328491]
- Consequence: the track is AI music (MiniMax-Music3) and is the main focus, so the upload needs the AI label already. Generated textures inside a stylized animated video add no new disclosure trigger. [H policy, jep application]
- US Copyright Office Part 2 (2025-01-29): prompts alone do not make a user the author; selection, arrangement and creative modification of outputs, and human inputs perceptible in outputs, can be protected. Generated tiles themselves are likely unprotectable by anyone; low risk as background texture. [H]
- Training-data risk: only Bria claims licensed-only training data, and its weights are non-commercial. [M]
- Krea 2 license obliges deployers to run content filtering. [M]

## 3. Local video models on 24 GB

| Model | Open? | Realistic 4090 output | Time | License | Gating |
|---|---|---|---|---|---|
| LTX-2.5 (Lightricks, 2026-08-11) | yes, 22B, video + audio, Gemma 4 12B encoder | 720p / 24 fps / 5 s clips; 10 s stalls at VAE decode; 22.67 GiB resident int8 [M] | ~24.6 s per 720p clip in ComfyUI 0.38.2 int8 distilled; 39 s in WanGP [M] | LTX-2 Community, free under $10M revenue [H] | Lightricks repo gated (contact info) [M]; unsloth/LTX-2.5-GGUF **ungated** [H] |
| LTX-2.3 (2026-03) | yes, 22B | 720p fp8 on 12-24 GB [L]; 4K claims conflict (3-12 min per clip, "48 GB+ native 4K") [L] | see left | same | Comfy-Org/ltx-2.3 ungated (LoRAs only) [H] |
| Wan 2.2 14B / 5B (2025-07-28) | yes, Apache 2.0 | 720p 81 frames (~5 s at 16 fps) with Lightning 4-step LoRAs; 5B undistilled crashed at final decode after ~9 min on a 4090 (2026-09) [M] | Blackwell nvfp4 card: 22-27 s per 720p clip; 4090 slower, unmeasured [M] | Apache 2.0 | ungated |
| Wan 2.5 / 2.6 / 2.7 / 3.0 | **no weights** (API only); Wan-Dancer-14B (music-to-dance) and Wan-Animate-2 are the only newer open Wan models [M, 2026-09-06] | | | | |
| HunyuanVideo 1.5 | yes | 720p 5 s at ~22 GB; 10 s 720p OOM [L] | ~3:50 per 720p 5 s [L] | Tencent community | |

Verdict for Knowledge Cutoff:
- 4K 60 fps from these = 720p/24 generation + 3x spatial upscale + 2.5x frame interpolation. Each step softens or invents detail; the result would fail the same 1:1 crop test the code render fails, and break the paper-cut style continuity. Not worth it. [jep judgment on M data]
- Narrow uses that could pay: (a) reference motion for a plate, e.g. how a page-a-day leaf tears and flutters, generated at 720p as a timing/arc study the agent re-implements in code; (b) LTX-2.5 IC-LoRA Alpha-Gen (2026-09-28) for an alpha-matted element, only if an insert is ever wanted. Both optional, low priority. [H existence, L value]

## 4. Automation

- ComfyUI HTTP API (docs.comfy.org): POST /prompt (API-format JSON, returns prompt_id), GET /history/{id}, GET /view?filename=..., POST /upload/image, GET/POST /queue, POST /interrupt, POST /free, GET /system_stats; WebSocket /ws messages: status, execution_start, execution_cached, executing, progress, executed. [H]
- Pattern: keep workflow JSON templates in the repo (export "API format"), patch node inputs (seed, prompt, image name) by node id, POST, wait on /ws `executing` with node null for that prompt_id (or poll /history), pull outputs via /view, write a sidecar JSON per output (model, seed, prompt, workflow hash) for receipts. [H API, jep pattern]
- Batch: queue many prompts back to back with the same model so weights stay loaded; group by model to avoid swaps; seeds fixed for reproducibility. [jep]
- MCP servers usable from Claude Code: artokun/comfyui-mcp (MIT, 855 stars, `npx -y comfyui-mcp` or plugin, queue tool, `clear_vram` via /free, `/comfy:batch` sweeps, Windows supported; maintainer says "limited maintenance"; its `download_model` pulls HF/CivitAI, so keep downloads manual to enforce the ungated rule) [H]; jcd315/comfyui-mcp-muse (enqueue_workflow / get_job_status / get_queue) [M]; hybridindie/comfyui_mcp (path sanitization, rate limits, audit log) [M]. A 60-line Python client over the raw API does the same with fewer moving parts. [jep]
- VRAM sharing with llama-server (127.0.0.1:8080): ComfyUI flags `--reserve-vram N` (GB kept free for other apps), `--lowvram`, `--highvram`, `--disable-smart-memory` [H]. POST /free `{"unload_models": true, "free_memory": true}` drops weights and cache; reported more reliable than in-graph cleanup nodes [M]. llama.cpp router `--sleep-idle-seconds` unloads but each dormant child process kept ~600 MiB [M]; llama-swap TTL kills the process and frees all VRAM, has `/unload` [M].
- Swap cost: reload = file size / disk speed: ~13 GB fp8 from NVMe ~3-6 s, plus first-run compile; a bf16 20B model ~40 GB will spill to system RAM on 24 GB. [L, jep arithmetic]
- Rule for this card: one big resident at a time. Sequence: stop or /unload the LLM → ComfyUI batch → POST /free → restart LLM. Z-Image-Turbo (~12 GB) + a ~7-8 GB LLM can co-reside with `--reserve-vram`; Qwen-Image-Edit-2511 cannot. [M]
- Version check: FLUX 3 Klein templates need ComfyUI >= 0.41; int8 convrot loading needs >= 0.27 per one card. Check the portable's version before planning. [H/M]

## 5. Ranked recommendation for this project

1. **Edit-target crops for the coding agents** (2c). Take 6-10 1:1 4K crops of the flattest plates, produce 3-4 painted-over targets each with Qwen-Image-Edit-2511 (Klein 4B for drafts), hand target + original to the agent as the acceptance picture.
   - Payoff: attacks the documented gap directly; turns "layered detail" from words into a picture the agent can match; zero generated pixels in the final video. High.
   - Cost: ~25-30 GB download (fp8 Lightning + text encoder + VAE); ~1-2 h setup; seconds to a minute per edit (unmeasured on 4090). Risk: the model invents detail the engine cannot express; mitigate by asking for print-process detail only (fibre, ink, overprint, hatching).
2. **Texture atlas for the detail kit** (2a + 2d). Test CC0 scans (ambientCG) against Z-Image-Turbo tiles with a DiT-aware seamless node; flatten, SeedVR2 to 4K, pack RGBA, sample multi-scale in the existing paper/scan shaders; Marigold normals for relief.
   - Payoff: breaks uniform fills at 1:1 with real multi-scale stochastic structure no hand noise reproduces cheaply. Medium-high.
   - Cost: ~1 day; Z-Image already known here (~12 GB); textures add ~64 MB GPU each. Risk: visible repetition, seams; mitigated by multi-scale rotated sampling.
3. **Plate boards before coding** (2b). 50-100 Z-Image-Turbo variants per plate, ref-conditioned with Klein 4B multi-ref or the Krea 2 `style_reference` LoRA; jep picks direction, then codes.
   - Payoff: cuts wasted shader iterations on a wrong direction. Medium.
   - Cost: minutes per plate once the API client exists.

Not recommended: video models for inserts (Section 3); SeedVR2 over the final 4K video (30-50 h estimate, shimmer on micro-type, and it abandons the "every frame is code" premise); Qwen-Image-2.1 / FLUX 3 Klein / Ideogram 4 / Fibo 2.0 until licensing or gating changes (best quality, but NC license or HF gate).

Open questions for Idi (rulings, not HOW): will the video be monetized (decides NC models)? Is AI-made texture inside frames acceptable given the "every frame is code" framing?

## Sources (accessed 2026-10-22)

Models and gating
- HF API Comfy-Org listing: https://huggingface.co/api/models?author=Comfy-Org&sort=lastModified&direction=-1&limit=40
- Comfy-Org/z_image_turbo (gated false, Apache): https://huggingface.co/api/models/Comfy-Org/z_image_turbo
- Tongyi-MAI/Z-Image (gated false, Apache): https://huggingface.co/api/models/Tongyi-MAI/Z-Image
- Z-Image release (2025-11-27): https://comfyui-wiki.com/en/news/2025-11-27-alibaba-z-image-turbo-release
- Z-Image-Turbo vs Klein timings (2026-08-26): https://runaihome.com/blog/z-image-turbo-16gb-vram-home-lab-image-gen-2026/
- FLUX.2 klein 4B (gated false, Apache): https://huggingface.co/api/models/black-forest-labs/FLUX.2-klein-4B
- FLUX.2 klein blog: https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence
- Comfy-Org/flux2-dev: https://huggingface.co/api/models/Comfy-Org/flux2-dev
- FLUX 3 Image Klein blog (2026-10-15): https://bfl.ai/blog/flux-3-image-klein
- FLUX 3 Klein HF (gated auto): https://huggingface.co/api/models/black-forest-labs/flux-3-image-klein
- FLUX 3 Klein ComfyUI docs (gated comfy repo, ComfyUI 0.41): https://docs.comfy.org/tutorials/flux/flux-3-klein
- FLUX 3 Klein license coverage: https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses
- Unofficial FLUX 3 mirror: https://huggingface.co/api/models/Rin247/flux-3-image-klein-INT8
- Qwen model list: https://huggingface.co/api/models?author=Qwen&search=Qwen-Image&sort=createdAt&direction=-1&limit=20
- Qwen-Image-Edit-2511 (gated false, Apache): https://huggingface.co/api/models/Qwen/Qwen-Image-Edit-2511
- Qwen-Image-Edit-2511 Lightning: https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning
- Unsloth Qwen GGUF guide: https://unsloth.ai/docs/models/qwen-image-2512
- ByteShape Qwen-Image-2512 GGUF: https://huggingface.co/byteshape/Qwen-Image-2512-GGUF
- Qwen-Image-Layered: https://huggingface.co/Qwen/Qwen-Image-Layered
- Qwen-Image-2.1 card: https://huggingface.co/Qwen/Qwen-Image-2.1
- Comfy-Org/Qwen-Image-2.1 (qwen-research license): https://huggingface.co/api/models/Comfy-Org/Qwen-Image-2.1
- Qwen-Image-2.1 Turbo 4090 test: https://promptowy.com/qwen-image-2-1-turbo/
- Qwen-Image-2.1 Turbo VRAM: https://dev.to/alanwest/qwen-image-21-turbo-isnt-7b-the-vram-you-actually-need-to-run-it-locally-3ikp
- Krea 2 Turbo (gated): https://huggingface.co/krea/Krea-2-Turbo
- Comfy-Org/Krea-2 (gated false): https://huggingface.co/api/models/Comfy-Org/Krea-2
- Krea 2 local guide (2026-07-20): https://localaimaster.com/blog/krea-2-local-guide
- Krea 2 formats / 4060 Ti timings: https://www.instasd.com/post/krea-2-turbo-checkpoint-formats-vram-guide
- Comfy-Org/Ideogram-4 (NC): https://huggingface.co/api/models/Comfy-Org/Ideogram-4
- Ideogram 4 coverage: https://www.buildfastwithai.com/blogs/ideogram-4-open-weight-image-model
- Comfy-Org/HiDream-O1-Image (MIT): https://huggingface.co/api/models/Comfy-Org/HiDream-O1-Image
- HiDream-O1 ComfyUI: https://docs.comfy.org/tutorials/image/hidream/hidream-o1
- Comfy-Org/ERNIE-Image (Apache): https://huggingface.co/api/models/Comfy-Org/ERNIE-Image
- Bria Fibo 2.0: https://huggingface.co/briaai/Fibo-2.0-dev ; https://docs.bria.ai/whats-new/fibo-2
- Model roundup (2026-07-08): https://www.earngenix.com/blog/best-local-image-generation-models-2026
- Open-weights T2I leaderboard snapshot (2026-10-20): https://theopenweights.com/leaderboards/text-to-image
- AA leaderboard: https://artificialanalysis.ai/image/leaderboard/text-to-image?open-weights=true
- NVFP4 is Blackwell-targeted: https://blog.comfy.org/p/new-comfyui-optimizations-for-nvidia
- FLUX.1 dev 4090 timings: https://github.com/Comfy-Org/ComfyUI/discussions/9002

Textures, maps, upscalers
- DiT tiling caveat + latent rolling: https://github.com/OliverCrosby/ComfyUI-Universal-Seamless-Tiles
- seamless_latent_tiling: https://comfy.icu/extension/mikemojen__ComfyUI-seamless_latent_tiling
- MakeSeamlessTexture: https://comfy.icu/extension/SparknightLLC__ComfyUI-MakeSeamlessTexture
- spinagon seamless tiling: https://github.com/spinagon/ComfyUI-seamless-tiling
- TextureAlchemy (Marigold PBR): https://github.com/amtarr/ComfyUI-TextureAlchemy
- QFX PBR generator: https://comfy.icu/extension/qornflex__ComfyUI-QFX-PBRGenerator
- Dream Textures: https://github.com/carson-katri/dream-textures/blob/main/docs/TEXTURE_PROJECTION.md ; https://www.cgchannel.com/2023/02/these-free-ai-add-ons-create-pbr-materials-inside-blender
- ComfyTextures (Unreal): https://github.com/AlexanderDzhoganov/ComfyTextures
- StreamDiffusionTD: https://blog.livepeer.org/builder-story-dotsimulate-x-daydream
- three.js ShaderTexture example: https://clicktorelease.com/code/codevember-2016/4
- ambientCG CC0 summary: https://creativebloq.com/3d-tips/find-high-res-textures-1232646
- Comfy-Org/SeedVR2 (Apache): https://huggingface.co/api/models/Comfy-Org/SeedVR2
- SeedVR2 4090 notes: https://huggingface.co/numz/SeedVR2_comfyUI/blob/b77d5dd95dba3f25e3a28064b76e6028a5152368/README.md
- SeedVR2 Comfy docs: https://docs.comfy.org/tutorials/utility/seedvr2.md

Video
- LTX-2.5 release (2026-08-11): https://comfyui-wiki.com/en/news/2026-08-11-ltx-2-5-open-weights-release
- LTX-2.5 4090 VRAM (2026-08-19): https://runaihome.com/blog/ltx-2-5-local-ai-video-hardware-guide-2026/
- LTX-2.5 HF search: https://huggingface.co/api/models?search=ltx-2.5&sort=downloads&direction=-1&limit=15
- unsloth/LTX-2.5-GGUF (gated false): https://huggingface.co/api/models/unsloth/LTX-2.5-GGUF
- LTX-2.3 card: https://huggingface.co/Lightricks/LTX-2.3
- LTX license $10M: https://ltx.io/model/license
- Wan open weights stop at 2.2 (2026-09-06): https://howaiworks.ai/blog/alibaba-wan-open-weights-stopped-at-2-2
- LightWan2.2 timings: https://huggingface.co/lightx2v/LightWan2.2-A14B
- HunyuanVideo 1.5 on 4090: https://dev.to/thurmon_demich/rtx-5090-vs-4090-for-video-gen-in-2026-32gb-matters-k3i
- LTX/Wan/Hunyuan VRAM guide: https://www.spheron.network/blog/ai-video-generation-gpu-guide/

Automation
- ComfyUI server routes: https://docs.comfy.org/development/comfyui-server/comms_routes
- ComfyUI memory flags: https://mintlify.wiki/Comfy-Org/ComfyUI/advanced/memory-management
- /free behaviour: https://docs.runcomfy.com/serverless/instance-proxy-endpoints
- artokun/comfyui-mcp: https://github.com/artokun/comfyui-mcp
- comfyui-mcp-muse: https://github.com/jcd315/comfyui-mcp-muse
- hybridindie/comfyui_mcp: https://github.com/hybridindie/comfyui_mcp
- llama-swap: https://betterstack.com/community/guides/ai/llama-swap/
- llama.cpp sleep-idle issue: https://github.com/ggml-org/llama.cpp/issues/19379

Policy
- YouTube altered/synthetic disclosure: https://support.google.com/youtube/answer/14328491
- USCO Part 2 copyrightability (2025-01-29): https://datamatters.sidley.com/2025/02/07/u-s-copyright-office-issues-report-on-artificial-intelligence-and-copyrightability/
