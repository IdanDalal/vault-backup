---
type: research
created: 2026-10-22
author: jep
scope: local models on one RTX 4090 (24 GB) for the AIMV pipeline (plate agents, critic agents, gate runners, fact-check, summaries)
---

# Local models on the 4090: research, 2026-10-22

Confidence tags: [H] high (primary source or replicated), [M] medium (one credible source or vendor-only), [L] low (single blog/anecdote, or my inference).
"Vendor" = number from the model maker's own card. "Indep" = third-party measurement.

## 0. Verdict lines

- Coding/agentic pick: **Qwen3.8-27B** (dense, Apache-2.0, ungated, released 2026-08-05 on HF). Top small open model on every independent board found. [H]
- Vision/critic pick: **the same Qwen3.8-27B** (native image+video input, mmproj in GGUF repos). One model, two roles, no swap cost. [M]
- Runtime pick: **llama.cpp llama-server**, Windows CUDA build, router mode, `/v1/messages` + `/v1/chat/completions`. [H]
- Fast/parallel fallback: **Qwen3.6-35B-A3B** (MoE, 3B active) or Gemma 4 26B-A4B. Weaker, much faster per token. [M]
- Honest gap: local = one serial worker at ~45 to 110 tok/s; independent SWE-bench Verified 86% vs Opus 5 97% (Vals.ai, 2026-09-01); SWE-rebench gap ~33 pts (Qwen3.6-27B vs frontier, May to Jul 2026 window). Long multi-file edits, long-style-bible adherence and aesthetic judgment remain cloud work. [H on numbers, M on interpretation]
- VLM-as-judge: frontier and open VLMs alike are weak at comparative aesthetic picks (best model 26.5% vs human experts 68.9%, VAB, May 2026) and at subtle low-level diffs (best 40.7% recall, DiffSpot). Use local VLM for legibility/defect triage with rubrics, never as the final aesthetic gate. [H]

## 1. Coding / agentic text models that fit 24 GB

### 1a. Candidate table

| Model | Released (HF) | Params / active | Quant that fits 24 GB + context | 4090 tok/s (indep unless noted) | Agentic benchmarks | Gate status |
|---|---|---|---|---|---|---|
| **Qwen3.8-27B** | 2026-08-05 | 27B dense, hybrid Gated DeltaNet + Gated Attention, vision encoder, 262K native ctx | UD-Q4_K_XL 17.6 GB or Q4_K_M ~16.5 to 17 GB; 64K ctx f16 KV = 20.6 GiB; 131K needs q8_0 KV (21.3 GiB); 262K needs q4_0 KV (22.2 GiB) | llama.cpp b11200, no MTP: 47 tok/s decode at 8K to 262K, prefill 2,600 to 3,000 tok/s; with MTP (8K): 102.8 / 109.4 / 113.2 tok/s, 69% draft acceptance; Ollama Q4_K_M + MTP 95 to 104 tok/s up to 64K (computingforgeeks, 2026-09-27) [H] | Vendor: Terminal-Bench 2.1 73.0, SWE-bench Pro 61.7, SWE-Multilingual 73.8, Toolathlon Verified 67.1, IFBench 79.5, LiveCodeBench v6 90.3. Indep: Vals.ai SWE-bench Verified (mini-SWE-agent) 86.0% rank 15, updated 2026-09-01; Quesma replicated vendor Terminal-Bench 2.1 at BF16 and at Q4_K_M (2026-08-26); AA Intelligence Index v4.3.2: 34 (xhigh), #1 small open | Ungated, Apache-2.0 [H] |
| Qwen3.6-27B | 2026-04-21 | 27B dense | Q4_K_M 16 GB; 64K ctx ~19.8 GB | 47.7 tok/s baseline, 115 to 133 tok/s with MTP at 16K (pedroalonso.net, 2026-06-09) [M] | Vendor: SWE-bench Verified 77.2, Pro 53.5, Terminal-Bench 2.0 59.3. Indep: Vals.ai 70.0%; SWE-rebench 31.2% (window 2026-05-15 to 07-01) | Ungated, Apache-2.0 |
| Qwen3.6-35B-A3B | 2026-04-15 | 35B MoE, 3B active | Q4_K_M ~20 GB; 64K needs `--n-cpu-moe 12` | L4 GPU (slower than 4090): 65.6 tok/s at 8K (localllm.in, updated 2026-05-12); no clean 4090 figure found | Vendor: SWE-V 73.4, Terminal-Bench 2.0 51.5, TAU3 67.2. Indep: SWE-rebench 24.7%; AA index 18 | Ungated, Apache-2.0 |
| Gemma 4 31B | card 2026-03-11, tech report 2026-07-02 | 30.7B dense, vision | Q4 fits; llama.cpp OOM at 16K+ on a 24 GB L4 in localllm.in tests | no 4090 figure found | Vendor: LiveCodeBench v6 80.0, Tau2 76.9. Qwen's table: SWE-V 52.0. AA index 15 | **Ungated now** (google/gemma-4-31B-it: gated=false, Apache-2.0) |
| Gemma 4 26B-A4B | 2026-04 | 25.2B MoE, 3.8B active | Q4_K_M 18.7 GB at 64K | L4: 47 tok/s at 8K | Qwen's table: SWE-V 17.4; AA index 17 | Ungated, Apache-2.0 |
| Nemotron 3.5 Bolt 74B-A9B-24GB | 2026-10-07 | 74B MoE, 9B active, Mamba-2/Transformer, native 2-bit, vision | single 22.0 GB GGUF built for 24 GB | no figure published | Vendor (IQ2): Terminal-Bench 2.1 50.98, MCP-Atlas 52.2; AA index 21 | Ungated, OpenMDW-1.1 |
| Nemotron 3.5 Lightning 30B-A3B | 2026-08 | 30B MoE, 3B active | fits at Q4 | none found | Indep: Vals.ai SWE-V 52.8% | OpenMDW-1.1 |
| Devstral Small 2 24B | 2025-12-09 | 24B dense | ~15 GB Q4 | none found | Vendor: SWE-V 68.0. Successor line folded into Mistral Medium 3.5 (128B, too big) | Ungated, Apache-2.0 |
| GLM-4.7-Flash | 2026-01-19 | 30B MoE, ~3B active | Q4_K_M ~17 GB | none found | Vendor: SWE-V 59.2, tau2 79.5. Newer GLM-5.3-Flash (2026-08-25) is 321B, does not fit | Ungated, MIT |
| gpt-oss-20b | 2025-08-04 | 21B MoE, 3.6B active, MXFP4 | fits in 16 GB | none recent | Vendor model card: SWE-V 60.7. No new OpenAI open model since (HF org listing) | Ungated, Apache-2.0 |
| Qwen3.8-Flash-Next | 2026-08-24 | 125B MoE, 6B active (+51B n-gram embeddings) | does NOT fit 24 GB | n/a | Vendor: SWE-Pro 62.5, Toolathlon 73.5 | qwen-community-1.0 license |

Not found / not current: Qwen3.7 (no open weights, codersera), Qwen3-Coder small (superseded by 3.6/3.8 general models on the same benchmarks), Seed-OSS and Kimi/DeepSeek small variants (no 24 GB-class release surfaced in Jun to Oct 2026 searches; DeepSeek V4 Flash/Pro are server-class). [M]

### 1b. Top pick detail: Qwen3.8-27B

- Weights: `Qwen/Qwen3.8-27B` (ungated). GGUF: `unsloth/Qwen3.8-27B-GGUF` (gated=false; mmproj-BF16/F16; `MTP/mtp-Qwen3.8-27B-Q4_0.gguf` sidecar 1.37 GB) and `ggml-org/Qwen3.8-27B-GGUF` (Q4_K_M, Q8_0, mmproj, mtp, dflash drafts). Ollama tag `qwen3.8:27b`. [H]
- Quant: Q4_K_M / UD-Q4_K_XL. Quesma (2026-08-26): Q4_K_M shows no measurable loss vs BF16 on GPQA, IFBench, Terminal-Bench 2.1; Q2 drops on Terminal-Bench; 1-bit collapses. Q5_K_XL fits only at 8K ctx (22.8 GiB with MTP); Q6 does not load. [H]
- MTP: in mainline llama.cpp (`--spec-type draft-mtp`, Qwen3.8 needs `--spec-draft-model mtp-...gguf`). Doubles decode at short context. Breaks at >=64K ctx ("failed to create MTP context", computingforgeeks). Qwen3.6 MTP card reports vision + MTP crashes llama.cpp; unverified for 3.8. Practical rule: MTP on for text plate/fact-check jobs at <=32K; MTP off for critic (vision) jobs. [M]
- KV cache conflict: one gist (BeeLlama fork, 2026-08-28) claims mainline llama.cpp falls back to CPU for non-q4 KV on Qwen3.x; computingforgeeks measured q8_0 KV at 131K on mainline b11200 at 46.6 tok/s with no slowdown. Treat the fork claim as unconfirmed. Also: HN user girvo reports quantized K cache causes loops; F16 K + Q8 V fixed it. [L]
- Thinking: on by default; `reasoning_effort` xhigh (default) / medium / low; xhigh overthinks (Quesma). Sampling thinking: temp 1.0, top_p 0.95, top_k 20. Non-thinking: temp 0.7, top_p 0.8, presence_penalty 1.5. [H, vendor]
- Tool calling: one tester, multi-hour Hermes session, zero failed tool calls, "clear step up from 3.6" (MindStudio, 2026-08-15, A100/vLLM, not a 4090) [L]. Ollama-specific hangs on `qwen3.8:27b` tool calls (issues #17839, #17825, fixed v0.33.0 / v0.32.15; open #18913, #18872 on empty arguments), runtime bug, not model (BetterClaw, updated 2026-10-13) [M]. No BFCL or Aider Polyglot score for 3.8 found anywhere. [H that it is missing]
- Parallel capacity: dense 27B on one card = effectively one stream. `-np 2` splits the KV budget (e.g. 2 x 32K). Expect 1 local worker, not N. [M, inference from VRAM numbers]
- VRAM contention: the AIMV render engine (Vulkan/WebGL, 4K frames) and games share the same 24 GB. A 20 GB resident model plus a 4K render will fight. Schedule local jobs outside render windows, or unload via router. [L, inference]

## 2. Vision-language models for judging rendered frames

### 2a. Candidates

| Model | Fit on 24 GB | Vision evidence (vendor unless marked) | Notes |
|---|---|---|---|
| **Qwen3.8-27B** | Q4 + mmproj BF16 (~1 GB) | OmniDocBench 1.5 91.1, CharXiv RQ 83.7 (no CI), RealWorldQA 85.9, Vision2Web 62.9, ERQA 65.5 | Same weights as coding pick. llama.cpp needs `--mmproj`; cap per-image tokens with `--image-max-tokens`. BF16 mmproj recommended over low-precision (MindStudio guide) [M] |
| Qwen3.6-27B | Q4 + mmproj | MMMU 82.9, OCRBench 89.4, V* 94.7 | Older, otherwise similar role |
| MiniCPM-V 4.7 35B-A3B | int4/GGUF fits | Vendor claims beats Qwen3.6-35B-A3B in Instruct mode; charts are images, no text numbers | Released 2026-10-06; Apache-2.0; ungated per card; very new, no indep evals found [L] |
| Gemma 4 31B | Q4 tight | MMMU-Pro 76.9, MATH-Vision 85.6; image token budgets 70 to 1120 | Mixed text/images in any order; multi-image not explicitly confirmed on card |
| Nemotron 3.5 Bolt 74B-A9B-24GB | 22 GB GGUF + mmproj | WebArena (vision) 50.86 | 2-bit native; no image-judging evals |
| GLM-4.6V-Flash (9B) | easy fit | VAB: big brother GLM-4.6V scored 11.5% TB-1 pass^3 (near random 5.3) | Dated (2025-12) |
| InternVL3.5 | 8B/14B/38B fit | none newer than 2025-09 on HF | Stale line, skip |

### 2b. Can VLMs reliably compare two images? Evidence

- **Visual Aesthetic Benchmark** (arXiv 2605.12684, 2026-05-12): 400 tasks, 1,195 images, 10 expert judges per task. Pick best and worst among matched candidates, correct across 3 orderings (TB-1 pass^3): best model Claude Sonnet 4.6 26.5%, human experts 68.9%, random 5.3%. Open: Qwen3.5-397B 17.2%, Qwen3-VL-235B 14.0%, GLM-4.6V 11.5%. Order sensitivity: models keep only 34 to 65% of accuracy when required to be consistent across permutations. LoRA on 2,000 expert examples lifted Qwen3.5-35B-A3B 15.8 to 17.5 (TB-1 pass^3). Score-derived rankings align poorly with the same experts' direct comparisons. [H]
- **DiffSpot** (arXiv 2605.29615, 2026-05-28): spot-the-difference on rendered web UIs, 4,400 pairs. Best of 13 frontier VLMs finds 40.7% of true changes; all models <23% on Hard tier; pixel magnitude does not predict recall. [H]
- **VDiff-Bench** (arXiv 2609.06245, 2026-09-05): 1,756 four-way pair questions, 10 change categories. 7 to 8B open models: 52.5 to 70.6% on semantic changes, 8.7 to 33.3% on low-level (noise, texture); models often claim "no change" when one exists. [H]
- **Aesthetic critique** (arXiv 2606.29689 v2, 2026-08-31): r/photocritique, 1,227 posts. Models (incl. Gemma-4-31B, Qwen3.5-397B, GPT-5.5) cover every aspect (composition >97%) where humans are selective; correct image beats no image by only +0.03 SBERT-cos, i.e. weak image grounding; small models stay positive and reframe flaws as intentional. [H]
- **MLLM-as-a-Judge** (arXiv 2402.04788, 2024): pair comparison is the most human-aligned mode; scoring and batch ranking diverge from humans; position and verbosity bias. [H, older]
- Implication for critic agents: local VLM is fit for objective checks (is text legible, is a region empty/noisy, count of elements, OCR of on-frame text, gross artifacts) under a written rubric with position-swapped double runs. It is unfit as the "matches reference level" aesthetic gate; frontier models are only modestly better there, so keep human eye (Idi) as final. [M, inference from above]
- Resolution: 4K frames exceed sane token budgets for a 27B on 24 GB; feed crops (roughly 1 to 2 MP each) or crop sheets downscaled per tile, set `--image-max-tokens`. [L, inference]

## 3. Runtime on Windows

| Runtime | Windows status | OpenAI tools | Anthropic `/v1/messages` | Multi-model | Throughput notes |
|---|---|---|---|---|---|
| **llama.cpp llama-server** | Native CUDA Windows release builds | Yes, `--jinja` (default on); `--chat-template-file` override when parser fails | **Verified**: PR #17570, HF blog 2026-01-19; streaming SSE, tool_use/tool_result, image blocks, `thinking`, `/v1/messages/count_tokens`; `ANTHROPIC_BASE_URL=http://127.0.0.1:8080` | **Router mode**: start without `-m`; `--models-dir`, `--models-preset` (INI), `--models-max N` (default 4, LRU evict), `--models-autoload`/`--no-models-autoload`; load/unload endpoint names vary by build, check `--help` | Best raw numbers on 4090 (47 / ~110 tok/s with MTP); MTP, DFlash, EAGLE3 spec decode in mainline; `-np` slots + continuous batching |
| Ollama | Native Windows | Yes | Yes since v0.14.0 (2026-01-16); token required but ignored; recommends >=32K ctx | Auto load/unload | MTP works (95 to 104 tok/s, Linux test). Qwen3.8 tool-call hang bugs Aug 2026 (fixed 0.33.0, some open); on an L4, Qwen3.6-27B at 64K fell to 2.6 tok/s vs 12.0 in llama.cpp (localllm.in) |
| LM Studio | Native Windows, GUI + headless | Yes | Yes since 0.4.1; custom tools + streaming; no context-length param on that endpoint | JIT model loading | llama.cpp backend, so similar speed; less control over spec-decode flags [M] |
| vLLM | **No native Windows** per official docs; WSL2 or community forks (SystemPanic, aivrar 0.27.1/0.29.0) | Yes, best-in-class parsers | Yes | One model per server | Strong batching, but WSL2 on the Standard user `jep` likely needs admin to enable; forks lag upstream 0.31.0 [M] |

Recommendation: llama-server router mode, one preset for Qwen3.8-27B text (MTP on, 32K, `-np 1`) and one for Qwen3.8-27B vision (mmproj, MTP off). Both presets share the same GGUF. Claude Code subagents or a thin script can hit `/v1/messages` directly. [M]

Claude Code against a local server: users report needing `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_MODEL` alongside `ANTHROPIC_BASE_URL`; Claude Code sends Claude model IDs, local servers may reject unknown names (alias the model). Billing note for this machine: these vars point Claude Code at localhost, never set `ANTHROPIC_API_KEY`. [M]

## 4. Honest capability gap (local vs frontier) for this pipeline

| Area | Evidence | Read |
|---|---|---|
| Repo-level coding, contamination-resistant | SWE-rebench (2026-05-15 to 07-01): Qwen3.6-27B 31.2% vs Fable 5 64.5%, Opus 5 63.4% (Qwen3.8 not yet listed) | ~2x gap on fresh tasks [H] |
| SWE-bench Verified, same harness | Vals.ai (2026-09-01, mini-SWE-agent): Qwen3.8-27B 86.0% vs Opus 5 97.0%, GPT-5.6 Sol 96.2% | 11 pts on a saturated board; failure rate ~4.7x [H] |
| Harness sensitivity | arXiv 2608.26218 (2026-08-26): same model, harness tweak raised tight-window complete solutions 43 to 72 of 169; Qwen3.6-27B-FP8: 90.0% custom stack vs 67.8% mini-swe-agent (GitHub discussion #1846) | Local results depend on harness more than model; budget for tuning [H] |
| Long multi-file edits, loops | HN "replaced Claude with local?" thread (2026): loops, wrong edit tool calls ("5 or 6 attempts at editing a 5-line function"), ignoring scope ("fixing a bug when told only to find it"), local = "a junior" vs Opus "a senior"; dev.to (Oct 2026): local ~70% of cloud on routine single-file, gap widens on agentic | Anecdotal but consistent [M] |
| Following a long style bible | Qwen3.8 IFBench 79.5 (vendor) beats Opus 4.6 62.5 on short constraints; HN practitioners report weaker attention to precise instructions buried in long context; quality drops before advertised window (several blogs) | Short rules fine, 10K+ token bible with many constraints risky [M] |
| GLSL / shader code | No benchmark compares open vs frontier on GLSL (searched Oct 2026). Startrise self-published 12-model UI test had a WebGL shader brief won by Fable 5 [L] | Unknown; your own gate scripts are the only real test [H that no benchmark exists] |
| Aesthetic / "reference level" judgment | VAB above: even frontier 26.5% vs human 68.9% | Neither tier is reliable; local is worse [H] |
| Throughput / parallelism | One 4090 = one dense-27B stream ~47 tok/s (110 with MTP, short ctx); cloud subagents run many in parallel | Local adds one worker, it does not multiply capacity [M] |

Where local fits in AIMV (my mapping, [L]):
- (c) run/read gate scripts and logs: good fit. Deterministic, short context, cheap retries.
- (d) fact-check short headlines: poor fit without web tools; local model knowledge cutoff + hallucination; pair with a search tool or keep in cloud.
- (e) summarise reports: good fit (Qwen3.8 long-context passphrase test at 197K passed, computingforgeeks).
- (b) critic agents: rubric-based objective checks only (legibility, emptiness, artifacts), double-run with swapped order; final aesthetic verdict stays cloud + Idi's eye.
- (a) plate agents: first-draft or single-module tweaks with the gate scripts as judge; multi-module work and style-bible-heavy plates stay cloud.

## 5. Gating and mirrors (checked via HF API, 2026-10-22)

| Repo | gated | Ungated mirror |
|---|---|---|
| Qwen/Qwen3.8-27B | false | unsloth/Qwen3.8-27B-GGUF (false), ggml-org/Qwen3.8-27B-GGUF (false), Ollama `qwen3.8:27b` |
| google/gemma-4-31B-it | **false** (Apache-2.0; changed from Gemma 3) | unsloth / ggml-org GGUF, Ollama `gemma4:31b` |
| google/gemma-3-27b-it | **"manual"** (Gemma license click + approval) | unsloth/gemma-3-27b-it-GGUF, ggml-org, bartowski, Ollama `gemma3:27b` [M on mirror names] |
| zai-org/GLM-5.3-Flash | false (MIT) | n/a, too big |
| nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF | false (OpenMDW-1.1) | itself is a GGUF |
| openbmb/MiniCPM-V-4.7-35B-A3B | no gate notice on card | openbmb/MiniCPM-V-4.7-35B-A3B-gguf (official) |
| Mistral, Qwen, OpenAI gpt-oss org listings | no gated field returned in org listings | Ollama registry for all |

Rule: check `https://huggingface.co/api/models/<repo>` field `gated` before any download; `false` = anonymous, `"auto"`/`"manual"` = gated.

## 6. Divergent option (one)

Skip local LLM agents for plates and critics entirely; use the 4090 for deterministic checks (image metrics like SSIM/LPIPS against reference crops, OCR via the VLM only for text legibility, shader compile/lint), and keep all judgment in cloud. Cheaper to verify, zero harness tuning, and the evidence above says VLM comparative judgment is the weakest link anyway. [L, proposal]

## Sources (accessed 2026-10-22)

Models and cards
- Qwen HF org listing (dates): https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=40
- Qwen3.8-27B card: https://huggingface.co/Qwen/Qwen3.8-27B ; API gate check: https://huggingface.co/api/models/Qwen/Qwen3.8-27B
- Qwen3.8-Flash-Next card (comparison table incl. 27B): https://huggingface.co/Qwen/Qwen3.8-Flash-Next
- Qwen3.6-27B card: https://huggingface.co/Qwen/Qwen3.6-27B
- Qwen3.6-35B-A3B card: https://huggingface.co/Qwen/Qwen3.6-35B-A3B
- unsloth Qwen3.8 GGUF: https://huggingface.co/unsloth/Qwen3.8-27B-GGUF ; files: https://huggingface.co/api/models/unsloth/Qwen3.8-27B-GGUF
- ggml-org Qwen3.8 GGUF files: https://huggingface.co/api/models/ggml-org/Qwen3.8-27B-GGUF
- Gemma 4 31B card: https://huggingface.co/google/gemma-4-31B-it ; gate: https://huggingface.co/api/models/google/gemma-4-31B-it
- Gemma 3 27B gate: https://huggingface.co/api/models/google/gemma-3-27b-it
- Nemotron 3.5 Bolt 24GB: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB ; GGUF: https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF
- Nemotron listing: https://huggingface.co/api/models?author=nvidia&search=Nemotron&sort=createdAt&direction=-1&limit=30
- zai-org listing: https://huggingface.co/api/models?author=zai-org&sort=createdAt&direction=-1&limit=25 ; GLM-4.7-Flash: https://huggingface.co/zai-org/GLM-4.7-Flash ; GLM-5.3-Flash: https://huggingface.co/api/models/zai-org/GLM-5.3-Flash
- Mistral listing: https://huggingface.co/api/models?author=mistralai&sort=createdAt&direction=-1&limit=25 ; Devstral 2: https://mistral.ai/news/devstral-2-vibe-cli/
- OpenAI listing: https://huggingface.co/api/models?author=openai&sort=createdAt&direction=-1&limit=15 ; gpt-oss model card: https://arxiv.org/abs/2508.10925
- MiniCPM-V 4.7: https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B ; listing: https://huggingface.co/api/models?author=openbmb&sort=createdAt&direction=-1&limit=15
- InternVL listing: https://huggingface.co/api/models?author=OpenGVLab&sort=createdAt&direction=-1&limit=15
- Qwen3.7 status: https://codersera.com/blog/how-to-run-qwen-3-7-locally-2026/

Independent measurements
- computingforgeeks, Qwen3.8-27B on RTX 4090 (2026-09-27): https://computingforgeeks.com/run-qwen3-8-27b-locally/
- Quesma, Qwen3.8 quantization benchmarks (2026-08-26): https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/
- ryan4yin gist, 4090 config (2026-08-28): https://gist.github.com/ryan4yin/19db9fa44972c5735c1d181e8888d4fe
- Pedro Alonso, MTP on 4090 (2026-06-09, upd. 08-24): https://www.pedroalonso.net/blog/qwen-mtp-speculative-decoding-4090/
- localllm.in, 24 GB tests on L4 (upd. 2026-05-12): https://localllm.in/blog/best-local-llms-24gb-vram
- Vals.ai SWE-bench Verified (upd. 2026-09-01): https://www.vals.ai/benchmarks/swebench
- SWE-rebench: https://swe-rebench.com/
- Artificial Analysis small open models: https://artificialanalysis.ai/models/open-source/small ; medium: https://artificialanalysis.ai/models/open-source/medium
- Qwen3.6-27B-FP8 custom stack 90.0 vs 67.8: https://github.com/QwenLM/Qwen3/discussions/1846
- Same Model, Different Harness (2026-08-26): https://arxiv.org/abs/2608.26218

Practitioner reports
- MindStudio Qwen3.8 agentic test (2026-08-15): https://www.mindstudio.ai/blog/qwen3-8-27b-agentic-coding-test
- BetterClaw Ollama tool-call hang (upd. 2026-10-13): https://www.betterclaw.io/blog/qwen-3-8-27b-tool-calling-fails-agents-fix
- HN "replaced Claude/GPT with a local model": https://news.ycombinator.com/item?id=48542100
- dev.to "benchmark everyone quotes is the wrong one" (Oct 2026): https://dev.to/rudratosh/can-a-local-llm-replace-claude-code-the-benchmark-everyone-quotes-is-the-wrong-one-2kna
- Startrise frontend/WebGL test (self-published): https://www.startrise.io/blog/llm-frontend-benchmark/

VLM judging
- Visual Aesthetic Benchmark (2026-05-12): https://arxiv.org/abs/2605.12684 (tables: https://arxiv.org/html/2605.12684)
- DiffSpot (2026-05-28): https://arxiv.org/abs/2605.29615
- VDiff-Bench (2026-09-05): https://arxiv.org/abs/2609.06245
- Can MLLMs Critique Like Humans (v2 2026-08-31): https://arxiv.org/html/2606.29689
- MLLM-as-a-Judge (2024): https://arxiv.org/abs/2402.04788

Runtimes
- llama.cpp Anthropic Messages API (2026-01-19): https://huggingface.co/blog/ggml-org/anthropic-messages-api-in-llamacpp ; PR: https://github.com/ggml-org/llama.cpp/pull/17570
- llama-server README (router flags, spec decode, mmproj): https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
- llama.cpp speculative docs: https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md
- Router mode unload notes: https://glukhov.org/llm-hosting/llama-cpp/unload-llama-cpp-router-models/
- llama.cpp multimodal flags (`--image-max-tokens`): https://docs.liquid.ai/deployment/on-device/llama-cpp/multimodal ; Qwen3.6 MTP+vision crash note: https://gitcode.com/hf_mirrors/froggeric/Qwen3.6-27B-MTP-GGUF/blob/main/README.md
- Ollama Anthropic compatibility: https://docs.ollama.com/api/anthropic-compatibility ; https://registry.ollama.ai/blog/claude
- LM Studio Anthropic compat: https://lmstudio.ai/docs/developer/anthropic-compat ; changelog: https://lmstudio.ai/docs/developer/api-changelog
- vLLM GPU install (no native Windows): https://docs.vllm.ai/en/stable/getting_started/installation/gpu/ ; fork: https://github.com/aivrar/vllm-windows-build
- KDnuggets Claude Code + local models: https://kdnuggets.com/pairing-claude-code-with-local-models
