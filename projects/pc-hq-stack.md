---
type: reference
created: 2026-08-30
author: jep
status: active
---

# PC HQ Stack - research synthesis 2026-08-30

Supersedes the Pi plan in [[pi-hq-bootstrap]]. Companion checklist: [[pc-base-migration]] (P1 rewritten same day). Four research passes: billing policy, hub integration, personal-software direction, Sovereign Nexus excavation.

## 1. Billing ground truth (decides everything)

1. Since **2026-04-04** Anthropic enforces server-side: any third-party harness (Pi, OpenCode, T3Code, Cline, aider, Crush...) authenticating with a subscription token bills per-token as "extra usage"; with extra usage disabled the requests are **rejected**, never plan-billed. The warning text is served by Anthropic's API, identical in every tool. No partner exemptions exist. ([relayplane](https://relayplane.com/blog/anthropic-extra-usage-third-party-tools), [Pi-specific, Aug 24](https://dev.to/spksoft/using-your-claude-subscription-in-pi-agent-at-your-own-risk-5h1j)) Confidence high.
2. Plan-billed surfaces: claude.ai, Claude Code (CLI / desktop / web / IDE), Cowork, and tools embedding the official Claude Code / Agent SDK (Zed's ACP adapter is the worked example). `claude -p`, Agent SDK apps, subagents, background tasks, scheduled routines all draw plan limits **today** under the paused June-15 credit split ([Anthropic support article](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan), verbatim: "For now, nothing has changed"). Policy-fragile: design so headless pieces are swappable. Confidence high.
3. Guards: keep **extra usage / usage credits OFF** in claude.ai settings (overflow then fails loudly); never let `ANTHROPIC_API_KEY` exist in the PC environment (it silently flips CLI/SDK to per-token API billing).
4. Claude Code on native Windows 11: fully supported, per-user install, no admin, Standard account fine (`winget install Anthropic.ClaudeCode` or `irm https://claude.ai/install.ps1 | iex`). Git for Windows recommended (real Bash tool; PowerShell fallback otherwise). Claude Code's own sandboxing is unavailable on native Windows, so the `jep` account restrictions carry the containment. ([setup docs](https://code.claude.com/docs/en/setup))

## 2. Architecture

Claude Code (resident, plan-billed) is the hub. Delegates outward; each tier spends its own budget.

| Tier | Runs | Budget | Invocation |
|---|---|---|---|
| Hub: Claude Code | judgment, orchestration, multi-file work | Max plan | resident session as `jep` |
| Codex CLI | mechanical straight-line tasks, second opinions, batch | ChatGPT plan | `codex exec "..."` from Bash; native Win11 installer; "Sign in with ChatGPT" = plan-billed ([docs](https://developers.openai.com/codex/cli)) |
| Local: llama-server | bulk generation, extraction, summarization, classification | electricity | OpenAI-compatible `127.0.0.1:8080`, curl or MCP |

Delegation contract, lifted from the Nexus (`spec-progressive-context-architecture.md:209`, `delegation-rules.yaml`): **delegate when the task exceeds ~2K tokens and only the RESULT matters, not the process.** Cloud delegates run parallel; local runs sequential (5–15 s model swap). Judgment never goes local. Delegation context capped ~2K tokens (context-compiler rule).

Optional tool-shaped wiring instead of Bash calls: [zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server) (10.9k stars, Apache-2.0; its Ollama/local path is free, its cloud paths need per-token API keys - skip those). Codex-as-MCP wrappers exist ([codex-as-mcp](https://github.com/kky42/codex-as-mcp)); start with plain `codex exec`, MCP only after the rule of three.

## 3. Local model tier - Nexus lineage, models refreshed

Verdict from the excavation: the Nexus **mechanics** transfer intact (build flags, router mode, VRAM math, delegation rules); its **model picks are Jan-2026 stale** and the Aug-2026 web pass had the fresher ones. The famous Ollama-vs-source table (85% vs 100% optimal, 45 vs 55 t/s) was **projected, never measured** - treat as directional.

Reusable Nexus artifacts (paths under `inbox/CORPUS-June-2026/NEXUS BACKUP/`):

1. `docs/guides/llama-cpp-rtx4090-build.md` - build recipe, still 100% valid: CUDA arch 89, `-DGGML_CUDA=ON -DGGML_CUDA_F16=ON -DGGML_CUDA_FA_ALL_QUANTS=ON`, VS 2022 + CUDA 12.x.
2. `scripts/llama-cpp/start-router.ps1` + root `models.ini` - the canonical run: one port, hot-swap. `llama-server --port 8080 --models-dir ... --models-max 2 --models-preset models.ini -ngl 99 -c 32768 -fa on --embeddings --parallel 1`. Key gotcha: `--parallel N` divides context N ways, so 1 slot = full context. Swap cost 5–15 s (measured, lived).
3. `data/research-output/2026-01-04-local-models/final_analysis.md` - reuse the METHOD: roles (research / reasoning / structured), model-bytes + KV-budget = 24 GB solve-for-context, headroom reserved for future voice (~6 GB).
4. `scripts/deep-research/deep_research.py` - working client layer vs llama-server; includes the Qwen3 `/no_think` suffix and `<think>`-stripping.
5. `scripts/llama-cpp/windows/start-longctx-server.ps1` - KV-quant recipe: `--cache-type-k q8_0 --cache-type-v q8_0` reaches 64K context.

Known Nexus conflict (its own audit flagged it): per-port-per-model scripts vs router mode shipped side by side. **Pick router mode.** Known gap: no speculative decoding anywhere; worth one experiment (30B main + small draft model) after the stack runs.

Model refresh, Aug 2026, slotted into the Nexus roles (GGUF from ungated sources: unsloth/ggml-org HF repos or the anonymous Ollama registry; official Gemma HF repos are gated - avoid):

| Role (Nexus) | Jan-2026 pick | Aug-2026 refresh | Size Q4 |
|---|---|---|---|
| Research / extraction | Qwen3-30B-A3B, Nemotron-3-Nano-30B | **Qwen3-Coder-30B-A3B** (code) / keep Nemotron for 1M-ctx | ~19 GB |
| Reasoning / planning | DeepSeek-R1-Distill-32B | **Qwen3.6-27B** (256K ctx, vision) | ~18 GB |
| Cheap bulk | Gemma-3-27B | **gpt-oss-20B** (~14 GB) or **Gemma4-26B MoE** (~19 GB) | 14–19 GB |

Practical ceiling stays ~27–30B Q4 on 24 GB once KV cache is budgeted; 35B-class Q4 fits on disk but starves context.

## 4. Collaboration layer port (laptop → PC)

| What | From (laptop) | To (PC) | Channel |
|---|---|---|---|
| Vault | GitHub `vault-backup` | `D:\work\vault` | git clone, read-only PAT (P1) |
| Output style | `~/.claude/output-styles/idi.md` | `C:\Users\jep\.claude\output-styles\idi.md` | **scp after P2** |
| Memory | `~/.claude/projects/-home-jep/memory/` | PC project memory dir after first launch | **scp after P2 - NEVER git: files contain full student names** |
| Home CLAUDE.md | `~/CLAUDE.md` | adapted copy at `C:\Users\jep\.claude\CLAUDE.md` | scp + hand-adapt (laptop paths/sandbox notes don't apply) |
| Vault governance | `vault/CLAUDE.md` | loads automatically in the clone | free |

## 5. Obsidian / GUI layer (later, rule of three)

Shortlist from the wild-direction pass, all plan-billed because they wrap Claude Code/SDK: **Claudian** (Agent SDK sidebar chat in Obsidian, subscription auth), [iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp), artifacts-as-apps (dashboards republished at stable URLs by scheduled sessions). Trap: any plugin with an "API key" settings field bills per-token. Dead ends: free Gemini CLI (killed 2026-06-18), Qwen free OAuth tier (closed 2026-04-15).

## 6. Security item (open)

The excavation found cleartext secrets in `inbox/CORPUS-June-2026/NEXUS BACKUP/.env`: Slack bot/app tokens, two n8n JWT keys, SearXNG + WebUI secrets. That file is inside the vault, therefore on GitHub (private repo) since the corpus was committed. Recommended: rotate what is still live, then purge the file (and any siblings) from the repo + history. Owner's call; not yet done.
