---
type: research
created: 2026-10-22
author: jep
project: AIMV / Knowledge Cutoff
status: active
---

# Local agents for Knowledge Cutoff: research verdict (2026-10-22)

Idi's ask: use the PC as a token source for every modality, text included, with jep as the expensive orchestrator and local models as workers. Four questions: what to delegate, which models, which harness, does image generation help.

Three web-research agents, ~10,000 words of findings, attached as receipts in `local-agents-2026-10-22/`. Confidence: [H] primary source or replicated, [M] one credible source, [L] anecdote or jep inference.

## Verdict lines

- Delegable: summaries, log/gate reading, objective frame checks, single-file code tweaks with a numeric gate. Stays with jep: direction, multi-module plates, style-bible work, beat design, the "reference level" verdict, fact-checks. [M]
- Model: **Qwen3.8-27B** at Q4_K_M, one model for text and vision. [H on existence and gating, verified by jep via HF API 2026-10-22]
- Harness: **llama.cpp `llama-server`** as the engine; `codex exec` (already installed) for agentic jobs; a plain script for one-shot jobs. [M]
- Images: yes, and higher payoff than text for this project: painted-over target crops attack the documented "vector-flat" gap directly. [M]
- Correction to the premise: one 4090 = **one serial worker**, weaker than the cloud. The cloud spawns many in parallel. The PC adds one free worker for checkable bulk work and frees Claude quota for judgment. [M]

## 1. What the PC has today (probed 2026-10-22)

| item | state |
|---|---|
| GPU | RTX 4090, 24,564 MiB, 4,535 used at idle |
| local text model | **none**: no `llama-server`, Ollama or LM Studio installed; nothing answers on 127.0.0.1:8080 (the HQ CLAUDE.md line about :8080 describes a planned stack that was never installed) |
| ComfyUI | portable at `C:\Users\jep\comfy\`, holds only MiniMax-Music3 (4.9 + 9.2 + 0.2 GB); no image model on disk |
| Codex CLI | installed, ChatGPT plan |
| KC pipeline size | 51 scene files, 19,358 lines TS/GLSL; 115 engine commits; 86 agent reports, 33 of them critic verdicts |

## 2. What to delegate (KC workflow, step by step)

| KC step today | who does it now | delegate to | why | conf |
|---|---|---|---|---|
| run gates (`gates-full.sh`, check.ts, avsync) | scripts | stays a script | no LLM needed | H |
| read gate logs, summarise reports, diff two reports | Claude agents | **local text** | long input, short output, no tools; best measured fit (Minions, ICML 2025: 5.7x cheaper at 97.9% quality when the strong model cuts the task into chunks) | M |
| critic: objective checks (text legible, region empty or noisy, on-frame text = lyric, element count, gross artifacts) | Claude critics | **local vision**, rubric + order-swapped double run | VLMs handle rubric checks; a script then verifies counts | M |
| critic: "equal or better than reference" | Claude critics + Idi's eye | stays Claude + Idi | every VLM is weak at comparative taste: best model 26.5% vs human experts 68.9% (Visual Aesthetic Benchmark, May 2026); best of 13 finds 40.7% of real differences (DiffSpot) | H |
| plate code: one file, numeric target (shader to a gate metric, param sweep) | Claude plate agents | **local worker** via `codex exec`, gate as judge | bounded, machine-checkable; small open models hold up to two tool steps (AgentFloor preprint: 96% single tool, 72% two-tool chain, 0% long-horizon) | M |
| plate code: multi-module, style bible, timing design | Claude | stays Claude | long-horizon; fresh-task gap ~2x (SWE-rebench: Qwen3.6-27B 31.2% vs Opus 5 63.4%) | H |
| headline fact-checks | Claude + web | stays Claude | local model has no web and its own cutoff | M |
| lead rulings, direction, briefs | jep | stays jep | judgment never goes local (pc-hq-stack rule) | H |

Task contract for any local job: one file, file allowlist, a done-state command that exits 0, context under ~32K tokens, JSON return, gates read-only to the worker, stop after N failures. jep re-runs the gate and checks the diff against the allowlist; the worker's "done" counts for nothing. Rule of thumb: if jep must read more than half of what a worker wrote to trust it, the task should not have gone local. [M]

## 3. Which model

| role | pick | numbers | conf |
|---|---|---|---|
| text + code + vision | **Qwen3.8-27B**, Q4_K_M (~17 GB), Apache-2.0, ungated (`unsloth/` and `ggml-org/Qwen3.8-27B-GGUF`) | SWE-bench Verified 86.0% vs Opus 5 97.0% (Vals.ai, 2026-09-01, same harness); 47 tok/s on a 4090, ~110 with MTP (multi-token prediction, a draft-ahead speed-up) at short context; 64K context fits (computingforgeeks, 2026-09-27); Q4 shows no measurable loss vs full precision (Quesma, 2026-08-26) | H |
| fast fallback | Qwen3.6-35B-A3B (MoE, 3B active) | weaker (SWE-rebench 24.7%), faster per token | M |
| gated, skip | Gemma 3 (license click); Gemma 4 is now ungated | | H |

Qwen3.8-27B's gate status and creation dates were checked by jep against the HF API: `Qwen/Qwen3.8-27B` gated=false, created 2026-08-05; both GGUF mirrors gated=false.

## 4. Which harness

| rank | route | use | billing | conf |
|---|---|---|---|---|
| 1 | `codex exec` pointed at a local server, called from jep's Bash, `--output-schema` JSON return, native Windows sandbox | agentic one-file jobs | zero Claude, zero ChatGPT; drop the local flag and the same job escalates to the ChatGPT plan | M |
| 2 | plain HTTP script to `llama-server` | summaries, frame triage, one-shot drafts | zero | M |
| 3 | headless `claude -p` worker aimed at the local server | only if a worker needs Claude Code skills | needs its own dummy `ANTHROPIC_AUTH_TOKEN` in that process only; Anthropic calls non-Claude routing unsupported; ~20K-token system prompt wants 128K context, tight on 24 GB | H |
| avoid | claude-code-router, LiteLLM mixed routing | | puts jep's own subscription traffic through a proxy; a misconfigured fallback bills per token | H |
| avoid | PAL MCP (ex zen-mcp-server) | | no commits since 2025-12-15 | H |

Runtime: `llama-server` native CUDA build, router mode (one port, hot-swap models). It speaks OpenAI and Anthropic APIs (PR #17570). vLLM has no native Windows build. [H]

Known trap, verified by jep: llama.cpp issue #30773 (open since 2026-10-18): the Responses endpoint, which Codex requires, reports a tool call cut off by the output limit as "completed". A worker can look successful when it failed. Mitigation: generous output cap, jep re-runs the gate on every result, or route Codex through Ollama instead. [H]

Hard constraint on this card: the 4K render, ComfyUI and a 17 GB text model cannot all sit in 24 GB, and the BSOD history (2026-09-21) already set "one heavy job at a time". Local jobs run between renders; unload before a render. [H]

## 5. Image generation: yes, three uses

| rank | use | model | payoff | cost | conf |
|---|---|---|---|---|---|
| 1 | **painted-over target crops**: 6-10 flat 1:1 4K crops, an edit model adds fibre, ink, overprint, hatching, layout kept; agents get a picture to match; no generated pixels reach the video | Qwen-Image-Edit-2511 (Apache, ungated, keeps micro-type); FLUX.2 klein 4B for ~1 s drafts | high: turns "layered detail" from words into an acceptance picture | ~25 GB download, 1-2 h setup | M |
| 2 | tileable texture atlas for the detail kit (paper fibre, stains, cut-edge fray, scan dust) packed into RGBA textures the shaders sample | test free CC0 scans (ambientCG) first, then Z-Image-Turbo (~2.3 s/image, Apache) with a seamless node that works on these newer models; SeedVR2 upscale | medium-high | ~1 day | M |
| 3 | mood boards per plate before coding | Z-Image-Turbo, 50-100 variants per plate in ~5 min | medium: fewer shader iterations in a wrong direction | minutes per plate | M |
| no | video models | LTX-2.5 = 720p/24 fps/5 s clips; upscaling to 4K60 fails the same 1:1 test | | | M |

Halftone, registration and print gain stay procedural (exact, resolution-free, animatable). Disclosure: the track is AI music, so the YouTube AI label applies already; textures inside a stylised video add no new trigger (YouTube Help 14328491). [H]

Stronger image models exist but break house rules: FLUX 3 Image Klein (top open model, 2026-10-15) is behind a HF license click; Qwen-Image-2.1 is non-commercial. A monetization ruling would only matter for the non-commercial ones; the Apache picks cover all three uses. [H]

## 6. Options

- **A. One pilot on the next KC pass, both tiers.** Install `llama-server` + Qwen3.8-27B (~18 GB) and Qwen-Image-Edit-2511 (~25 GB), both from ungated repos. Wire the summary/triage script and one `codex exec` worker. Run 10 bounded tasks, logging per task: gate pass on first try, retries, jep review needed. Produce painted-over targets for the 6-10 flattest crops. Cost ~half a day of setup, nothing changes in the video until targets are used. Payoff: the first real number for Claude quota saved per delegated task (no published source measures it).
- **B. Images only.** Targets and textures, no local text tier. Smallest step, attacks the documented gap.
- **C. Text only.** Local summaries, triage and one-file workers, no image work.

**Recommendation: A.** The image tier carries the higher payoff for KC; the text tier only proves itself with the per-task log, and both share the same GPU schedule. Risk: setup eats a session before any frame improves; the #30773 bug can fake worker success until the gate re-run catches it.

## Sources

Full source lists with links: the three attached reports.
- `local-agents-2026-10-22/research-local-models.md` (models, runtimes, VLM-judge evidence)
- `local-agents-2026-10-22/research-harnesses.md` (dispatch routes, billing, task contract)
- `local-agents-2026-10-22/research-image-gen.md` (image models, texture pipeline, ComfyUI automation)

Key primary sources: Vals.ai SWE-bench (https://www.vals.ai/benchmarks/swebench); SWE-rebench (https://swe-rebench.com/); Minions (https://arxiv.org/abs/2502.15964); Visual Aesthetic Benchmark (https://arxiv.org/abs/2605.12684); DiffSpot (https://arxiv.org/abs/2605.29615); llama.cpp issue #30773 (https://github.com/ggml-org/llama.cpp/issues/30773); Claude Code gateway docs (https://code.claude.com/docs/en/llm-gateway); YouTube disclosure (https://support.google.com/youtube/answer/14328491).

Related: [[knowledge-cutoff-escalation-pass-2026-10-21]], [[handoff-2026-10-17-full-video]], [[pc-hq-stack]].
