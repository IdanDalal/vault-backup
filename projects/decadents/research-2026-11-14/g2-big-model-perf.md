---
type: research
created: 2026-11-14
author: Agent g2b-big-model-perf
---

# Big-model performance options: H3-Image (A) and HunyuanImage 3.0 Distil (B) on a 4090 with 32 GB RAM

Method: web pages fetched 2026-11-13 and 2026-11-14 (GitHub API, Hugging Face raw files, Arctic Shift Reddit archive, vendor blogs, Tom's Hardware, TweakTown). Two read-only local queries (memory modules, GPU link) answered the DDR4/DDR5 unknown. Nothing installed, no page code run. "Measured" = a number the source reports from its own run. "Estimate" = my arithmetic from those numbers, untested on this PC.

## 0. Verdict

- Model B is disk-bound on this PC. The 46.91 GB file cannot stay in 12 to 14 GB of free RAM, so most of it is re-read from the NVMe on every step. RAM is the only change that closes the 54 s vs 22 to 26 s gap. Confidence: medium (inference from the node README plus two pull-request measurements; nobody published a 32 GB vs 64 GB run).
- Model A is already near what a 4090 does (Reddit: 4090 + 64 GB, "8 MP around 6-8 seconds"; 16.6 MP in about 22 s with int8). The only large lever left is the 2-step LoRA.
- Software is current: ComfyUI v0.45.0 (2026-11-10) is the newest release, comfy-aimdo 0.6.0 the newest tag.
- The board takes DDR5 (local query): Gigabyte Z790 AORUS ELITE AX, 2 x 16 GB Kingston KF560C36-16 running at 4800, 4 slots, 2 free.
- The GPU-unlock projects give almost nothing for these two models: both run INT8 math, and the one ComfyUI report says "INT8 barely moved".

## 1. System RAM

Why RAM governs Model B (sources: node README, PR #2, PR #3)

- README: "Only a slice fits on the GPU at any time, so the rest streams from system RAM over PCIe on every step." W4A8 "moves ~45 GB" per step. "With the W4A8 file loaded, ComfyUI held about 50 GB (tested on a 188 GB machine)."
- README, smaller-GPU section: "The weights stream from system RAM, not from disk: the disk is read once."
- README speed table (RTX 4090, PCIe 4.0 x8, 188 GB): W4A8 Distil 39 s cold, 26 s warm, 3.1 s/step; re-measured later at 2.5 to 2.6 s/step.
- PR #2 comment (second machine, RTX PRO 6000 96 GB, 128 GB RAM): with fast_disk on, ComfyUI's own RAM fell from about 50 GB to 7 GB; warm render 25.7 s before, 25.0 s after. Author's merge note: "same speed, 10-16 GB less RAM" on the 4090.
- PR #16333 (ComfyUI core): fast-disk weights are "taken straight from disk ... so OS disk cache buffering at most". Reading: in fast-disk mode the Windows file cache (free RAM that holds recently read file data) is what makes repeat reads fast. The author's machine has room to cache all 47 GB. This PC has room for about a quarter.
- This PC: 5.6 s/step vs 2.5 to 3.1 s/step, a 1.8x to 2.2x gap, plus about 10 s of non-step time per picture vs about 1 s on the author's machine.

Expected gain by RAM size (estimates; budget = 46.91 GB file + 2.5 GB decoder + about 7 GB ComfyUI process + 7 to 10 GB other programs = 63 to 66 GB)

| Total RAM | Model B | Model A | Confidence |
|---|---|---|---|
| 32 GB (now) | 54.5 s median, measured here | 10 to 12 s new prompt, 4 to 5 s new seed, measured here | measured |
| 64 GB | 22 to 30 s if other programs stay under about 8 GB; partial gain otherwise (budget is at the edge) | new prompt maybe 2 to 4 s faster (encoder and image network both stay cached, 36.7 GB) | medium for B, low for A |
| 96 GB | 22 to 26 s (author's range), with margin; pinned memory can return | same as 64 GB | medium |
| 128 GB | same as 96 GB for W4A8; also the minimum class for the int8 file (81.85 GB) | same | medium |

- Pinned memory (page-locked RAM that makes RAM-to-GPU copies faster): Comfy blog measured "10-50%" faster sampling with async offload plus pinned memory vs both off, on RTX 3070 / 4070 Ti / 5070 Ti, PCIe 4.0 x16. Vendor-measured; no independent reproduction found. At 32 GB it must stay off (your error 1450 matches issues #15337 and #15255, same `GetOverlappedResult failed error=1450` line).
- This PC's GPU link: x16 wide, Gen 4 capable (nvidia-smi, local). It read Gen 1 at idle, which is likely idle power saving; re-read during a render. The author's card sits on x8, and the Comfy blog says x8 gave "less impressive" offload gains, so this PC could beat 22 s once RAM stops being the limit. Unmeasured.

Prices (Tom's Hardware RAM price index, "last updated 11 November 2026", lowest US price per kit)

| Kit | Price | Note |
|---|---|---|
| DDR5-6000 32 GB | $438 | a second 2 x 16 kit fills the 2 free slots, total 64 GB |
| DDR5-6000 64 GB | $949 | replace the pair with 2 x 32, total 64 GB (or 96 GB if the old pair stays) |
| DDR5-6000 96 GB | $2,049 | 2 x 48 |
| DDR5-6400 128 GB | $3,799 | |
| DDR4-3200 32 GB / 64 GB | $197 / $449 | moot: the board is DDR5 |

- Trend, same page: DDR5 "triple and, in some cases, quadruple increases"; a 32 GB kit was "$100 to $200 in October 2025". Israeli prices not checked.
- How the type was read: `Get-CimInstance Win32_PhysicalMemory` shows `SMBIOSMemoryType 34` (34 = DDR5, 26 = DDR4) and slot names `DDR5-A2`, `DDR5-B2`. Task Manager, Performance, Memory shows the same without a command.
- Risk for this PC: four DDR5 modules train less reliably than two, and two separate kits are not a vendor-validated set. The current 4800 setting (the profile speed is 6000) is the safer one; keep it. A memory test after fitting is the gate. With a suspect 13900K, an unstable result can come from the CPU as well as from the modules.

## 2. ComfyUI and comfy-aimdo: flags, settings, versions

Release notes, September to November 2026 (GitHub releases API, fetched 2026-11-14)

| Version | Date | Relevant line |
|---|---|---|
| v0.45.0 | 11-10 | MiniMax-H3-Image support (#17655); newest release |
| v0.44.0 | 11-04 | fix: fp8 fast path fell back to bf16 under dynamic VRAM (#16941) |
| v0.43.0 | 10-27 | comfy-aimdo 0.6.0: "Writeback VBARs", cuMemSetAccess retry fix (#17274); "Sync offload streams before stealing a pin" (#17297) |
| v0.38.0 | 09-29 | W6A8 format support (#16483); fast-disk detection in all loaders (#16425); the fix that made W4A8 expert banks sample at full speed (PR #2 cites #16637) |
| v0.37.0 | 09-21 | aimdo 0.5.5, auto-enable fast-disk on fast NVMe (#16333); "Always put text encoder on GPU when dynamic vram on" (#16374); `--disable-fast-disk` added |

Flags (from `comfy/cli_args.py`, fetched 2026-11-13)

| Flag | What it does | Use here |
|---|---|---|
| `--fast-disk` | "Force disk-backed dynamic loading and offload over unpinned RAM" | keep at 32 GB; auto-detected since v0.37.0, so the flag only forces it |
| `--disable-pinned-memory` | no page-locked RAM | keep at 32 GB; drop it only after a RAM upgrade, then test |
| `--cache-ram [GB] [GB]` | default result cache; first value = free-RAM headroom to keep (default 10% of RAM, 2 to 10 GB) | `--cache-ram 6` keeps more RAM free for the file cache; untested, low confidence |
| `--cache-none` | re-runs every node each time | bad for A: the 6 s text encode would repeat on every seed |
| `--vram-headroom GB`, `--reserve-vram GB` | keep VRAM free | no speed gain; raise only if the screen stutters |
| `--high-ram` | "Can improve performance slightly on high RAM" | only after 96 GB+ |
| `--disable-fast-disk` | hold weights in RAM | test after a RAM upgrade if B stays slow |
| `--use-ck-attention` | Comfy Kitchen int8 attention | no gain for B (author: 2.5 to 2.6 s/step under every backend); see risk below |
| `--disable-async-offload` | single-stream weight copies | crash workaround only |

- Node version: the fast_disk pass-through and grouped routing landed in commit db6a293 (2026-10-09); newest commit a60958b (2026-10-25). Older installs build "a second, pinned, retained RAM copy of the whole 44 GB checkpoint" (PR #2). Confirm the node is at db6a293 or later.
- Page file: Comfy blog (2026-03-25): cached weights "will never be pushed to your page file"; aimdo maintainer in #15255: it "will still dynamically avoid swap/pagefile use". One #15255 report crashed with 75.7 GB free and a page-file peak of 42 MB. Reading: a larger page file buys no speed. Leave it system-managed on the NVMe so Windows never runs out of commit (the promise of memory it has handed out). Confidence: medium.
- Stability risk tied to these code paths: issue #15488 collects "GPU is lost" black screens during int8 and quantized-attention runs on H3, Wan and LTX, including one RTX 4090 with 64 GB (fixed there with a gentler voltage curve at "like 3 seconds per step"). On a PC with a suspect CPU, stay on default attention and treat any black screen as a stop sign.

## 3. File formats

Model B (Hugging Face file list, fetched 2026-11-14: w4a8 46.91 GB, int8 81.85 GB, bf16 161.62 GB)

| Format | Published? | Measured by node author (4090, 188 GB) | On 32 GB |
|---|---|---|---|
| W4A8 | yes | 26 s warm, 3.1 s/step; weight error 7.3%, image SSIM 0.738 vs bf16 | what you run |
| W6A8 (6-bit weights) | no file found for this model; core support exists since v0.38.0 | none | would be larger than W4A8 (about 60 to 65 GB by bit count, estimate), so slower here |
| int8 ConvRot | yes | 49 s warm, 5.9 s/step, "~1.9x slower per step"; weight error 1.0%, SSIM 0.844 | 82 GB re-read per step: not usable; needs the 128 GB class |

- The grouped-expert kernel (PR #3) is no help on a 24 GB card: author measured W4A8 2.58 s/step before, 3.2 to 3.4 s/step with it. Not merged.

Model A (Comfy-Org/MiniMax-H3-Image file list: int8 image network 20.98 GB, W4A8 12.55 GB, bf16 40.23 GB; encoder NVFP4 15.69 GB, int8 27.14 GB; decoder 1.17 GB)

| Choice | Evidence | Verdict for a 4090 with 32 GB |
|---|---|---|
| int8 image network | fits the card alone; "~22 s on a 4090 with the int8 weights" at 16.6 MP (Reddit 1xtlj1t) | keep |
| W4A8 image network | Reddit: on RTX 30 "not faster and often slower" than int8 (4-bit weights are expanded to 8-bit on the fly); on a 16 GB AMD card W4A8 35 s vs int8 39 s at 8 MP. No 4090 number found | steps likely equal or slower; prompt switches may be quicker because 12.55 + 15.69 GB is closer to 24 GB. Test only if new-prompt time matters more than quality. Low confidence |
| NVFP4 encoder on RTX 40 | comfy-kitchen README lists a CUDA `scaled_mm_nvfp4` kernel; hardware NVFP4 layout needs "SM >= 10.0 (Blackwell)". One model card (6block): on a 4090 "a cu130 torch build enables the comfy_kitchen FP4 kernels (otherwise emulated and ~2.3x slower)". Comfy blog: without cu130, NVFP4 "may actually be up to 2x slower than fp8". One Reddit user on a 3060: "the speed difference is minimal". No independent timing | keep; check the startup log line `Native ops: ... emulated ops: ...`. If `nvfp4` sits under emulated, the encode runs on the slow path. Medium confidence |
| int8 encoder (27.14 GB) | larger than the card's VRAM | worse here: more to read per new prompt, more eviction of the image network |
| GGUF builds (Abiray: Q4_K_M 11.6 GB, Q5_K_M 14.1 GB; encoder Q4_K_M 14.6 GB) | sizes only; no speed numbers; needs the third-party ComfyUI-GGUF loader | no reason on a card that fits int8. Low confidence |

Fastest combination found for this PC: int8 image network + NVFP4 encoder (what you run), plus the 2-step LoRA in section 4.

## 4. Step and compute reducers (measured gains only)

| Reducer | Model | Measured | By whom, hardware | Reproduced? | Cost, risk |
|---|---|---|---|---|---|
| Spectrum node (skips the heavy core on some steps and predicts its output) | B | Distil 8 steps: 26 s to 20 s, 1.3x, SSIM 0.959 (lowest 0.945) vs off. 50-step models: 3.4x | node author, 4090, 188 GB | no | free; already in the workflow, switched off. Estimate here: 54.5 s to about 42 s if the ratio holds |
| pDMD 2-step LoRA (a 2 GB add-on that finishes an image in 2 model passes; stock needs 6) | A | 16 MP bf16: 25.1 s to 17.4 s, 1.4x. Card claims "2-3x faster per render" at 2 to 4 MP. Demo: 2048x2048 in about 4.6 s with detail pass vs about 7 s for the official 6-step demo | card author (akhaliq), H200 and an RTX PRO 6000 slice | no; Reddit thread 1xu7gs2 (48 points) has no benchmark, one commenter says check skin for a waxy look | free, Apache-2.0 LoRA; works with int8 and W4A8 files through the LoRA path; softer output, fixable with the card's half-size draft + 3-step detail pass. Estimate here: new seed 4 to 5 s to 2 to 3 s |
| HAP node (experimental, above 1024x1024) | B | "about 12% faster per step at 2x" | node author | no | free; experimental |
| Attention backends (SDPA, xformers, Kitchen, Flash, Sage) | B | 2.5 to 2.6 s/step under every one | node author, 4090 | no | none; no gain |
| Comfy Compiler (aimdo memory planner + CUDA graphs) | A | on by default for H3 since v0.35.0; PR shows a stalled 5060 run fixed, no seconds for a 4090 | Comfy | n/a | already active |
| torch.compile, fp16 accumulation script, turbo add-ons for H3-Image | A | no measurement found for H3-Image; the fp16 script moved to `./advanced` in v0.45.0 without numbers | | | skip |

## 5. Text encoding for Model A

- Caching: ComfyUI reuses the encode when the prompt text is unchanged; your 4 to 5 s "another seed" time shows it works. A changed prompt always pays the encode.
- Why about 6 s: since v0.37.0 the encoder always runs on the GPU under dynamic VRAM (#16374), so a new prompt pushes part of the 20.98 GB image network out and pulls 15.69 GB in, then swaps back. At 32 GB both moves come from the NVMe. More RAM turns them into RAM copies (estimate, section 1).
- Smaller encoder: P-H3-Image (Pruna's sibling model, core support since v0.44.0) uses its own smaller text encoder with the H3 video network and runs 8 steps at 8 MP, "about 21 GB of VRAM" (Comfy docs). It is a different model with a different look; no encode timing published. ClipProj (a community adapter that feeds H3 from a 4B encoder) exists for H3 video; H3-Image support unverified. Low confidence on both.
- Official prompt expander: Comfy recommends `qwen3.5_9b_w4a8_gptq` (7.34 GB) with the Generate Text node. Reddit 1xt42b3: "25 mins to generate 8k tokens" with one 16 MP reference on a 5060; a commenter reports about a minute on a 3060 after cutting max length to 1024 and feeding images at 1 MP or less; several users got better pictures with the expander off. On this PC a third 7 GB model also adds one more disk swap per prompt. Cheaper: write the expanded prompt outside ComfyUI (MiniMax publishes a prompt-writing guide) and paste it in.

## 6. Windows settings

| Setting | Evidence | Advice |
|---|---|---|
| Page file | section 2: aimdo avoids it; one crash report with 42 MB page-file use | leave system-managed on the NVMe; no speed expected. Medium confidence |
| NVIDIA "CUDA - Sysmem Fallback Policy" (lets VRAM overflow spill into slow shared RAM; added as a switch in driver 546.01, per search summaries, NVIDIA page not opened) | aimdo README: its allocator "behaves a lot better on Windows systems with System Memory fallback"; no timing for these models | watch "Shared GPU memory" in Task Manager during a render; if it climbs, set "Prefer No Sysmem Fallback" for ComfyUI's python.exe only. Low confidence |
| Defender exclusion for the models folder | no benchmark found for model streaming; issue #15337's reporter suspects security filter drivers in the error-1450 read path (the reporter's guess, unconfirmed) | free, reversible, needs an admin account; time one picture before and after. Low confidence |
| Power plan, hardware-accelerated GPU scheduling | no source found with numbers for these workloads | leave at defaults; a high-performance plan adds heat on a suspect CPU |
| GPU power limit | #15488: 90% limit "does help but not by much"; one 4090 fixed black screens with a voltage curve | stability tool; no speed gain |

## 7. Projects that change drivers, firmware or boot-time state on RTX 40 cards

Source: TweakTown, 2026-10-25, plus search-result titles. Source code and setup pages not opened.

| Project | One line | Reported numbers | Works below the driver? | For this PC |
|---|---|---|---|---|
| GPU Unlock Ada (RTX 40) | Linux kernel module that lifts the FP16/BF16 tensor-rate cap by running an old firmware loader ahead of the driver (per search summaries) | RTX 4090 FP16 165.6 to 331.6 TFLOPS | yes | HIGH RISK. Linux-first. Expected gain for A and B near zero: both compute in INT8 |
| GPU Unlock (RTX 30, by Zagitta) | "change low-level GPU registers before the NVIDIA driver loads"; clears at power-off | 3090 Ti FP16 +35%, BF16 +80%, TF32 +94%; ComfyUI BF16 image models +56 to 59%, "INT8 barely moved"; LLM prompt processing +14 to 36% | yes | HIGH RISK. Wrong card generation |
| KohakUnlock (RTX 20) | same technique for Turing | 2080 Ti 59.9 to 111.0 TFLOPS | yes | HIGH RISK. Wrong card generation |
| Experimental Windows build of the unlock | Windows port | "82.5% BF16 gain on an RTX 3090" | yes | HIGH RISK. TweakTown: "unsupported setups may fail to boot", "voids the warranty" |
| Unofficial DLSS 5 / Multi Frame Generation patches for RTX 40 | game-side file swaps that enable RTX 50-only frame generation | game frame rates only | no | irrelevant to image models |

## 8. Ranked top five

| # | Change | Gain A | Gain B | Cost | Risk | First step |
|---|---|---|---|---|---|---|
| 1 | Turn on Spectrum for B | none | 26 to 20 s measured by the author (1.3x, SSIM 0.959); about 54 to 42 s here if it scales | free, one toggle | none; small image drift | set `enabled` true on the HunyuanImage-3.0 Spectrum node, render one seed both ways |
| 2 | pDMD 2-step LoRA for A | 1.4x at 16 MP measured on H200; claimed 2 to 3x at 2 to 4 MP; about 4 to 5 s to 2 to 3 s per seed here (estimate) | none | free, 2 GB download, 2 nodes | none for the PC; softer skin and detail | load the card's `minimax-h3-image-pdmd-2step-lora-t2i.json` workflow, LoRA at 1.0, shift 12, 2 steps |
| 3 | Free checks: node at db6a293 or later; log line `Native ops / emulated ops` (is `nvfp4` emulated?); close RAM-heavy programs before B; GPU link reads Gen 4 x16 under load | up to the emulation penalty on the 6 s encode if `nvfp4` is emulated (one card claims 2.3x) | every GB freed is a GB of the 47 GB file that stops being re-read each step | free, 10 minutes | none | read the first 40 lines of the ComfyUI startup log |
| 4 | RAM to 64 GB (second 2 x 16 DDR5 kit, $438 US on 2026-11-11) or 96 GB (2 x 48, $2,049) | new prompt maybe 2 to 4 s faster | 54.5 s to 22 to 30 s at 64 GB with little else running; 22 to 26 s at 96 GB | $438 to $2,049 | medium: 4-module DDR5 training on a suspect CPU; stay at 4800 and run a memory test | get a local price for a second Kingston KF560C36-16 pair |
| 5 | Windows hygiene: Defender exclusion for the models folder, page file left system-managed, keep `--disable-pinned-memory` and default attention at 32 GB | unmeasured, small | unmeasured, small; fewer error-1450 failures is the real value | free, needs admin for Defender | low | add the exclusion, time one picture before and after |

Skip list: GPU-unlock projects (below the driver, INT8 unaffected), int8 file for B, int8 encoder for A, GGUF builds, `--use-ck-attention`, `--cache-none`.

Open measurements nobody has published: B at 32 vs 64 GB; W4A8 vs int8 H3-Image step time on a 4090; NVFP4 vs int8 encode time on a 4090; Spectrum's gain when weights stream from disk.

## Sources

- https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3 (README: speed, format, Spectrum and smaller-GPU tables)
- https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3/pull/2 (fast_disk, RAM 50 GB to 7 GB, second-machine confirmation)
- https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3/pull/3 (grouped kernel slower on a 4090)
- https://huggingface.co/PedroMarinhoDev/HunyuanImage-3.0-Instruct-Distil-ComfyUI (file sizes, formats)
- https://github.com/Comfy-Org/ComfyUI/releases (v0.31.0 to v0.45.0 notes)
- https://github.com/Comfy-Org/ComfyUI/pull/16333 (auto fast-disk, aimdo 0.5.5)
- https://github.com/Comfy-Org/ComfyUI/pull/16374 (text encoder always on GPU)
- https://github.com/Comfy-Org/ComfyUI/pull/16483 (W6A8 support)
- https://github.com/Comfy-Org/ComfyUI/pull/17274 (aimdo 0.6.0)
- https://github.com/Comfy-Org/ComfyUI/pull/17655 (MiniMax-H3-Image support)
- https://github.com/Comfy-Org/ComfyUI/pull/15861 (Comfy Compiler)
- https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/cli_args.py (flag help text)
- https://github.com/Comfy-Org/ComfyUI/issues/15255 (read_file_slice failures, pinned memory, page-file data point)
- https://github.com/Comfy-Org/ComfyUI/issues/15337 (error 1450 with pinned memory)
- https://github.com/Comfy-Org/ComfyUI/issues/15488 ("GPU is lost" reports, incl. a 4090)
- https://github.com/Comfy-Org/comfy-aimdo (README, tags up to v0.6.0)
- https://github.com/Comfy-Org/comfy-kitchen (README: NVFP4 kernels and hardware floor)
- https://blog.comfy.org/p/dynamic-vram-in-comfyui-saving-local (2026-03-25)
- https://blog.comfy.org/p/new-comfyui-optimizations-for-nvidia (2026-01-09)
- https://huggingface.co/Comfy-Org/MiniMax-H3-Image (file sizes, prompt enhancer recommendation)
- https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF (GGUF sizes)
- https://huggingface.co/akhaliq/minimax-h3-image-pdmd-2step (2-step LoRA, timings)
- https://huggingface.co/6block/MiniMax-H3-Qwen3-VL-NVFP4 (NVFP4 on a 4090, 2.3x claim)
- https://docs.comfy.org/tutorials/image/pruna/p-h3-image (P-H3-Image)
- https://www.tomshardware.com/pc-components/ram/ram-price-index-2026-lowest-price-on-ddr5-and-ddr4-memory-of-all-capacities (updated 2026-11-11)
- https://www.tweaktown.com/news/114288/modders-unlock-nvidia-geforce-rtx-20-30-and-40-series-compute-limits-nearly-doubling-some-tensor-core-throughput/index.html (2026-10-25)
- https://explainx.ai/blog/rtx-4090-tensor-unlock-gpu-unlock-ada-fp16-331-tflops-linux-2026 (search summary only, page not opened)
- https://discuss.pytorch.org/t/documented-fix-slow-execution-pytorch-using-gpu-shared-memory/218909 (search summary only, page not opened)
- Reddit via https://arctic-shift.photon-reddit.com : https://www.reddit.com/r/StableDiffusion/comments/1xt50cj/ (speed reports), https://www.reddit.com/r/StableDiffusion/comments/1xtlj1t/ (16 MP in 22 s on a 4090), https://www.reddit.com/r/StableDiffusion/comments/1xu7gs2/ (2-step LoRA), https://www.reddit.com/r/StableDiffusion/comments/1xt42b3/ (prompt expander speed), https://www.reddit.com/r/StableDiffusion/comments/1xsqz2h/ (W4A8 vs int8 on older cards), https://www.reddit.com/r/StableDiffusion/comments/1xsp46n/ (NVFP4 encoder on a 3060)
- Local read-only queries, 2026-11-14: `Get-CimInstance Win32_PhysicalMemory`, `Win32_BaseBoard`, `nvidia-smi --query-gpu=pcie.link...`
