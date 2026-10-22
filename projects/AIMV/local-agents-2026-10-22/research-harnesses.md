---
type: research
created: 2026-10-22
author: jep
topic: local-model workers under a subscription-billed Claude Code orchestrator
---

# Local workers for a Claude Code orchestrator (Windows, RTX 4090, Max plan)

Researched 2026-10-22. Confidence tags: [H] high (primary doc read), [M] medium (one good secondary or partial primary), [L] low (single blog, inference, or unverified). Source numbers in brackets point to the list at the end.

## 0. Bottom line

- Start harness: **`codex exec` (already installed) pointed at a local endpoint**, called by Claude Code from Bash in the foreground, with `--output-schema` + `-o` for a machine-readable return and `--sandbox workspace-write` for containment. Zero Claude billing contact. [M]
- For non-agentic one-shot jobs (log summaries, single-file drafts, frame triage): **plain HTTP call to a llama-server on 127.0.0.1:8080 (not installed yet, jep probe 2026-10-22)** from a script, or a thin MCP wrapper. No tool calls, so no tool-call breakage. [M]
- Billing risk exists in exactly one family: proxies that sit in front of the orchestrator's own traffic (claude-code-router, LiteLLM mixed routing). Avoid them. [H]
- Second-tier risk: a separate `claude -p` pointed at a local model is fine billing-wise only when it carries its own dummy `ANTHROPIC_AUTH_TOKEN`; without it, the saved claude.ai OAuth login is the active credential and travels to the base URL. Anthropic calls non-Claude routing unsupported. [H]

## 1. Dispatch routes, one by one

### 1a. MCP servers wrapping a local OpenAI-compatible endpoint

| Server | What it does | Status | Conf |
|---|---|---|---|
| PAL MCP (ex zen-mcp-server), BeehiveInnovations | multi-provider abstraction; `CUSTOM_API_URL` for Ollama/vLLM/LM Studio; `clink` bridges Codex/Gemini/Claude CLIs | **last commit 2025-12-15 (v9.8.2)**, ~10 months dormant; Windows doc points to WSL, has .ps1 scripts | [H] dormancy, [M] features [1][2][3] |
| houtini-lm | delegates bounded tasks (review, test stubs, commit msgs), tracks offload totals | repo fork 404 on fetch; claims unverified | [L] [4] |
| hlgr360/local-llm-mcp | llama.cpp / OpenAI-compatible, `session_stats` token counter, Claude Code plugin | not deeply verified | [L] [4] |
| koyakimu/local-llm-mcp | Claude Code + Codex plugin, bulk/private text to llama.cpp, llama-swap, vLLM, LM Studio, Ollama | not deeply verified | [L] [4] |
| aplaceforallmystuff/mcp-local-llm | Ollama; "Claude does the thinking, local does grunt work"; Claude reviews results | not deeply verified | [L] [4] |
| Emasoft/llm-externalizer-plugin | Claude Code plugin, profiles, ensemble mode, local + OpenRouter | not deeply verified | [L] [4] |
| ccebelenski/localagents | MCP `run_agent` spawns a **headless `claude`** whose `ANTHROPIC_BASE_URL` points at a shim in front of llama-server/vLLM `/v1/messages`; worktree isolation option | "early", v0.1.5, 13 stars, POSIX install, no Windows mention; author: needs native tool calling + **128k+ context per slot**, 64k "works but thrashes", first turn ~20k prompt tokens | [H] from README [5] |

- Mechanism: MCP tool call is a normal Claude Code tool; the worker's tokens never touch Anthropic. Billing impact zero. [H]
- Weakness: most of these are small single-author repos; read the code before install (vault rule: verify). [M]

### 1b. Claude Code calls a local CLI agent through Bash

| Harness | Headless form | Local endpoint | Native Windows | Notes | Conf |
|---|---|---|---|---|---|
| **Codex CLI** | `codex exec --oss --local-provider ollama -m <model> "..."`; `--json` JSONL events; `-o` last message to file; `--output-schema schema.json`; `--sandbox read-only/workspace-write` | `--oss` = Ollama or LM Studio; custom `model_providers` with `base_url` for others (llama-server) | yes, native sandbox (elevated/unelevated) shipped with Windows app 2026-03-04 | `codex exec` errors if no provider chosen (no prompt); **`wire_api="chat"` removed**, custom providers must speak Responses API; Codex needs >=64k context | [H] docs [6][7][8][9][10] |
| Codex via MCP (`mcp__codex__codex`, already in this session) | tool params: prompt, model, sandbox, approval-policy, cwd, `config` overrides | `config` object can override provider (untested) | yes | one secondary source says `codex mcp-server` is deprecated upstream | [H] schema seen locally, [L] deprecation [11] |
| OpenCode | `opencode run --model ...` | `@ai-sdk/openai-compatible` provider in opencode.json (Ollama :11434, LM Studio :1234, llama-server :8080) | yes (Windows guides exist) | XDA July 2026 supervisor pattern used it with Qwen3-Coder-30B-A3B on llama.cpp | [M] [12][13][14] |
| Crush (Charm) | `crush run -m provider/model -q` | `openai-compat` provider in crush.json | yes, winget/Scoop | no Windows+local example found | [M] [15] |
| Qwen Code | `-p` prompt flag, output + approval-mode flags | OpenAI env vars or `~/.qwen/settings.json` | guides say tested on Windows | Qwen OAuth discontinued 2026-04-15; small models (8B) chat but fail tools | [M]/[L] [16][17] |
| Aider | `--message` / `--message-file`, `--yes`, `--no-auto-commits`, `--dry-run` | OpenAI-compatible / Ollama | Windows usage mostly via WSL in guides | no exit-code semantics documented; architect mode = plan model + edit model | [H] flags [18], [L] Windows |
| Goose (AAIF / Linux Foundation) | recipes `goose recipe run x.yaml` | Ollama; `GOOSE_TOOLSHIM=true` for models that narrate tools | native Windows build since ~Aug 2025 | v1.52.0 2026-09-23 per secondary | [L] [19] |
| OpenHands | `--headless` CLI (uv tool) | env vars with `--override-with-envs` | Windows without WSL documented for GUI + local runtime, **no sandbox**; CLI Windows support disputed | heavy for this use | [M] [20] |

- Billing impact for all rows: zero Claude contact; Codex rows on `--oss` also zero ChatGPT-plan use. [H]
- Fallback built in: the same `codex exec` call without `--oss` runs on the ChatGPT plan, a second flat-rate tier for escalation. [M]

### 1c. claude-code-router / ANTHROPIC_BASE_URL tricks

Facts from Anthropic docs (read 2026-10-22):
- `ANTHROPIC_BASE_URL` changes where requests go, "not which model answers them". [H] [21]
- "Anthropic ... doesn't support routing Claude Code to non-Claude models through any gateway." Unsupported, no prohibition sentence found. [H] [22]
- **Credential variable (`ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_API_KEY`, `apiKeyHelper`) replaces the subscription** for those requests; subscription limits do not apply; billing goes to whoever owns the forwarded credential. Against a local server nobody bills. [H] [22][23]
- **`ANTHROPIC_BASE_URL` alone does not replace the subscription**: "a saved claude.ai login remains the active credential, so its usage limits and billing apply" and the OAuth token is sent to that base URL. [H] [22]
- `ANTHROPIC_AUTH_TOKEN` takes precedence immediately; `ANTHROPIC_API_KEY` prompts once. Use AUTH_TOKEN for a worker (also keeps the HQ rule "no ANTHROPIC_API_KEY in env"). [H] [23]
- Shell exports reach only that process and children; settings.json `env` applies everywhere, including the orchestrator. Worker config must live in the worker's own process env, never in `~/.claude/settings.json`. [H] [23]
- Telemetry still goes to Anthropic without the gateway credential unless `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`. [H] [23]

Separate worker process (`claude -p` with base URL = local):
- Works: Ollama v0.14+ speaks Anthropic Messages (messages, streaming, tools, thinking, vision); docs show `ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 claude --model qwen3-coder`. LM Studio 0.4.1 adds `/v1/messages`; llama.cpp has Anthropic API support. [H] Ollama [24][25], [M] others [26]
- Cost on a 4090: Claude Code's system prompt + tools ~20k tokens first turn; 128k context advised; a 27B Q4 model with 128k KV on 24 GB is tight. [M] [5][14]
- Terms: the Consumer Terms govern Claude Code for Max users; legal page restricts OAuth use by third-party tools and the Agent SDK, nothing found that bans pointing the unmodified binary at a local model with a non-Anthropic credential. Status: unsupported, not documented as prohibited. [M] [27]

Subagent to local while orchestrator stays on Claude:
- Subagent `model` accepts `sonnet`/`opus`/`haiku`/`fable`, a full Claude model ID, or `inherit`. No per-subagent base URL or provider. [H] [28]
- So one Claude Code process can split models only through a proxy that routes by model name: e.g. LiteLLM forwards the Max OAuth token (`sk-ant-oat...`, adds `anthropic-beta: oauth-2025-04-20`) to Anthropic for `anthropic/*` and could send `haiku` to llama-server. Anthropic documents subscription traffic through a gateway ("must forward the OAuth capability"). [H] LiteLLM [29], [H] Anthropic [22]
- Risks of that route: orchestrator traffic now depends on a proxy you maintain; any misconfigured `api_key` fallback bills per token (LiteLLM's own warning); built-in Explore subagent and background tasks that resolve to Haiku would silently go to the weak local model; terms gray zone (one vendor warns account risk). **Do not use.** [H] mechanics, [L] enforcement [29][30]
- claude-code-router v3.1.3 now ships a Windows x64 app; README no longer documents OAuth passthrough or the old `<CCR-SUBAGENT-MODEL>` tag. [M] [31]
- Historical enforcement: 2026-01-09 server-side block of third-party OAuth use; 2026-02-19 terms section "Authentication and credential use"; possible further step 2026-04-04 (single source). These target Claude credentials inside third-party harnesses, irrelevant to local-only workers. [H] Jan/Feb [32][33], [L] April [34]

### 1d. Claude Code native features

| Feature | Non-Anthropic model support | Use here | Conf |
|---|---|---|---|
| Subagent `model` | Claude aliases/IDs only | cheap Claude tier (Haiku 5.5) costs plan quota, not zero | [H] [28] |
| `CLAUDE_CODE_SUBAGENT_MODEL` | same set | none | [H] [28] |
| Advisor tool | Claude only, server-side, reverse pattern (cheap executor, strong advisor) | none for local | [H] [35] |
| Hooks | run any command; a PostToolUse/Stop hook can run gates or call a local model | gate runner, cheap validator | [H] (hooks doc not re-read; general) |
| Agent SDK | spawns Claude Code binary; env passthrough supports base URL + token | could script local `claude` workers; SDK docs say third-party products must use API keys, personal subscription use of SDK sits in the "ordinary individual usage" clause | [H] [36][27] |
| Gateway model discovery | `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` lists gateway models in `/model` | only inside a worker process | [H] [23] |

No official Anthropic feature dispatches to a non-Claude model. [H]

## 2. Native Windows matrix (no WSL)

| Component | Native Windows | Conf |
|---|---|---|
| Claude Code | yes; Git Bash optional; **sandboxing not supported natively** | [H] [37] |
| Codex CLI + `codex exec` | yes, native sandbox (restricted token + ACL + firewall in elevated mode) | [H]/[M] [10] |
| llama-server (llama.cpp) | yes (planned for :8080; not installed, jep probe 2026-10-22) | [H] |
| Ollama | yes; `ollama launch claude/codex/opencode` | [H] [9][38] |
| LM Studio | yes | [M] |
| OpenCode, Crush, Goose | yes (native builds) | [M] |
| Qwen Code | yes (npm) | [M] |
| Aider | runs, most guides use WSL | [L] |
| OpenHands | GUI/local runtime without WSL, no sandbox; CLI disputed | [M] |
| PAL MCP | docs steer to WSL | [M] |
| localagents | POSIX install, untested on Windows | [M] |

## 3. Documented orchestrator-worker evidence

### Measured (peer-reviewed or first-party measurement)

| Study | Setup | Result | Caveat | Conf |
|---|---|---|---|---|
| Minions, Hazy Research, ICML 2025 (arXiv 2502.15964) | frontier remote + small local; MinionS = remote decomposes into chunked subtasks, local runs them in parallel | **5.7x cost reduction, 97.9% of remote-only quality**; naive chat protocol: 30.4x cheaper but only 87% quality | document QA/reasoning, not coding; one group; not independently replicated | [H] [39][40] |
| Anthropic multi-agent research (2025-06-13) | Opus lead + Sonnet workers | +90.2% vs single Opus on internal eval; multi-agent ~15x chat tokens; tokens explain ~80% of variance | internal eval, research tasks, Claude-only workers | [H] [41] |
| AgentFloor (arXiv 2605.00334), via dev.to digest | 16 open models 0.27B-32B vs GPT-5, 16,542 trials | gemma4:26b: single tool 96%, two-tool chain 72%, conditional 59%, multi-source 32%, **long-horizon 0%**; ~15x cheaper per passed task at matched ~60% | secondary digest of a preprint | [M] [14] |
| Reward hacking in autonomous research agents (Sept 2026, arXiv 2609.28614 per index) | 17 LLMs, 38 tasks | spontaneous hacking **30.5% on open-ended tasks vs 2.9% on task-specific kernels**; LLM review panel missed 6.5% of confirmed hacks | preprint | [M] [42] |
| SWE-bench Verified, vendor-reported | open models | Devstral Small 2 (24B) 68.0%, Qwen3-Coder-Next 70.6-71.3%, Opus 4.5 80.9% | vendor numbers, scaffold-dependent | [L] [14] |

Pattern in the measured data: **workers succeed when the orchestrator cuts the task small and checkable** (MinionS vs naive Minion; kernels 2.9% vs open-ended 30.5%; AgentFloor collapse past two-step chains).

### Anecdotes and vendor claims (no controlled measurement)

- XDA 2026-07-28: GPT-5.6 supervisor writes SUPERVISOR.md + reviews diff, OpenCode + Qwen3-Coder-30B-A3B Q4 on llama.cpp does the edits; "roughly half the time", "far fewer cloud tokens"; no pass rates; stop rules: repeated failure, architectural change, drift. [M as report, L as evidence] [13]
- XDA: routing edit-retry loops to local Qwen3-Coder/Gemma 4 stopped 5-hour limit burn. [L] [43]
- Dev.to: six-person startup claims 88-92% quality retained on local Qwen3-Coder. [L] [44]
- localagents author: prefix-cache-friendly prompts cut per-turn latency from 21-47 s to 2.5-14 s on a 27B. [M] [5]
- No source found that measures Claude-subscription quota saved per delegated task. Gap. [H]

### Known failure modes

| Failure | Evidence | Conf |
|---|---|---|
| Worker reports success it did not achieve | llama.cpp issue #30773: `/v1/responses` marks **truncated tool calls as completed**; chat-completions path handles truncation correctly; relevant because Codex now requires Responses | [H] [45][46] |
| Tool call narrated in prose, no `tool_calls` array | dev.to digest; Goose ships a tool shim for it | [M] [14][19] |
| Silent context truncation | Ollama auto context: <24 GiB VRAM = 4,096, 24-48 GiB = 32k; a 4090 sits on the boundary, so set `OLLAMA_CONTEXT_LENGTH` / `num_ctx` explicitly; truncation makes agents invent file contents | [M] [14] |
| KV-cache quantization hurts tools | `-ctk q4_0` "can substantially degrade" tool calling | [M] [14] |
| Small models cannot use tools | qwen3:8b chats but fails tools; 14B+ needed | [L] [17] |
| Test tampering / evaluator rewriting | Countdown-Code (1% contaminated SFT is enough), rebound study, 30.5% open-ended rate | [M] [42] |
| Over-spawning, duplicated work, vague briefs | Anthropic: 50 subagents for simple queries; fix = objective, output format, tools, boundaries | [H] [41] |
| Verification cost eats savings | Minions naive protocol lost 13 points of quality; no study prices orchestrator review tokens against worker savings for coding | [M] inference [39] |

## 4. Task contract for a weak worker

Hand it over only when every line holds:
- **One deliverable, one file or one function**; file allowlist stated; everything else read-only.
- **Machine-checkable done-state**: a command that exits 0 (typecheck, unit test, headless render, shader compile, frame probe). The worker gets the command; the orchestrator re-runs it.
- **Small context**: brief + the files it needs, under ~16-32k tokens on this card; no "explore the repo".
- **At most two tool steps deep** (AgentFloor cliff); multi-step plans stay with Claude.
- **Structured return**: JSON matching a schema (`codex exec --output-schema`), fields like `status`, `files_changed`, `command_run`, `exit_code`, `notes`.
- **Stop rules**: N failed attempts, needs a file outside the allowlist, needs an architectural change: return `blocked`, never improvise.
- **Tests and gates are read-only to the worker** (tamper risk).

Orchestrator verification, cheapest first:
1. Re-run the gate command itself; trust the exit code, never the worker's text.
2. `git diff --name-only` against the allowlist; reject on any outside file, including test/gate files.
3. Diff size sanity (empty diff with "done" = fail; huge diff = scope creep).
4. Schema-validate the JSON return.
5. Read the diff only for tasks that passed 1-4, and only sampled when volume is high.
- Rule of thumb [M, inference]: when Claude must read more than half of what the worker wrote to trust it, the task should not have been delegated.
- Log per task: delegated, gate pass first try, retries, Claude review needed (y/n). That yields the missing "quota saved" number for this project after ~20 tasks.

AIMV task fit (TS/GLSL engine):

| Task | Fit | Why | Conf |
|---|---|---|---|
| Summarize render/gate logs | best | long input, short output; MinionS-shaped; no tools needed | [M] |
| Run checks | needs no LLM | a script is the worker; LLM only summarizes failures | [H] |
| Scene module from a spec + existing module as template | good if gated | one file, typecheck + headless render + probe as done-state | [M] |
| Shader tweak to a numeric target | good if gated | compile + pixel/probe metric | [M] |
| Judge frames | triage only | local VLM can flag blank/broken/off-palette frames; taste verdict stays with Claude and Idi's eye | [L] |
| Cross-module refactor, timing/beat sync design | keep on Claude | long-horizon, multi-source (AgentFloor tiers D/E) | [M] |

## 5. Ranked recommendation for this machine

1. **Codex CLI `codex exec` on a local provider** [M]
   - Already installed, native Windows sandbox, headless, `--output-schema` + `-o` give machine-checkable returns, `--json` gives an event log; one flag removed from the call escalates to the ChatGPT plan.
   - Endpoint choice: Ollama (`--oss --local-provider ollama`, 64k context set explicitly) is the documented path; a llama-server would work through a custom `model_providers` entry with `wire_api="responses"` but carries the #30773 truncation bug, so test it first.
   - Model candidates for 24 GB: Qwen3.6-27B Q4 (~18 GB), Qwen3-Coder-30B-A3B Q4 (~19 GB), Devstral Small 2 24B; pick by a 10-task bake-off on AIMV modules. [L] model ranking [47][14]
2. **Direct HTTP to llama-server :8080 once installed (script or thin MCP)** for non-agentic jobs: log summaries, single-file drafts, frame triage. The script form needs only llama-server; chat-completions path avoids the Responses truncation bug. [M]
3. **Headless `claude -p` worker with per-process `ANTHROPIC_BASE_URL` + dummy `ANTHROPIC_AUTH_TOKEN`** when a worker must use Claude Code skills/hooks. Unsupported by Anthropic, ~20k-token system prompt, 128k context wanted; never put these variables in settings.json. [H] mechanics, [M] fitness
4. OpenCode or Crush as a second local harness if Codex's Responses-only requirement keeps biting. [M]
5. Avoid: PAL MCP (dormant since 2025-12-15), claude-code-router / LiteLLM mixed routing (puts the orchestrator's OAuth traffic through a proxy, silent per-token fallback risk), OpenHands (heavy, unsandboxed on Windows). [H]/[M]

Divergent option: skip local workers for coding and use Claude Haiku 5.5 subagents for bounded work (plan quota, near-zero setup, strong tool use), keeping the 4090 for log summarization and frame triage only. [M]

## Sources (accessed 2026-10-22 unless dated)

1. PAL MCP server repo: https://github.com/BeehiveInnovations/pal-mcp-server
2. PAL commit history (last 2025-12-15, v9.8.2): https://github.com/BeehiveInnovations/pal-mcp-server/commits/main
3. PAL custom models doc: https://github.com/BeehiveInnovations/pal-mcp-server/blob/main/docs/custom_models.md
4. MCP offload servers (search results): https://github.com/Emasoft/llm-externalizer-plugin , https://github.com/hlgr360/local-llm-mcp , https://github.com/koyakimu/local-llm-mcp , https://github.com/aplaceforallmystuff/mcp-local-llm , https://github.com/suppressio/local-llm-offload , https://github.com/Kerstin59718/houtini-lm (404 on fetch)
5. localagents README: https://github.com/ccebelenski/localagents
6. Codex advanced config (oss_provider, model_providers, profiles): https://learn.chatgpt.com/docs/config-file/config-advanced
7. Codex non-interactive mode: https://developers.openai.com/codex/noninteractive.md
8. Codex `wire_api=chat` deprecation, discussion #7782 (Dec 2025): https://github.com/openai/codex/discussions/7782
9. Ollama Codex integration: https://docs.ollama.com/integrations/codex
10. Codex on Windows, native sandbox (2026-04-01): https://codex.danielvaughan.com/2026/04/01/codex-cli-windows-native-sandbox-wsl/ ; SD Times: https://sdtimes.com/sdt_dev/openai-releases-codex-for-windows/
11. Codex MCP tool schema and deprecation note (third-party): https://glama.ai/mcp/servers/hxkuc2tvi9
12. OpenCode + llama.cpp guide: https://medium.com/@anish.rai3737/run-a-local-llm-for-coding-with-llama-cpp-opencode-8eaa5b0db73b
13. XDA, cloud supervisor + local model (2026-07-28): https://www.xda-developers.com/ditched-claude-code-local-model-cloud-supervisor-twice-fast/
14. dev.to, Running AI coding agents locally in 2026 (2026-07-28; AgentFloor, context tiers, SWE-bench figures): https://dev.to/dublecc/running-ai-coding-agents-locally-in-2026-what-actually-works-4ogl
15. Crush run + local models: https://next-docs.charm.land/crush/cli/run.html , https://mintlify.com/charmbracelet/crush/advanced/local-models
16. Qwen Code headless: https://www.mintlify.com/QwenLM/qwen-code/features/headless-mode ; OAuth end 2026-04-15: https://www.morphllm.com/qwen-cli
17. Qwen local tool-calling caveat: https://docs.conduction.nl/nl/claude/local-llm/
18. Aider scripting: https://aider.chat/docs/scripting.html
19. Goose + Ollama: https://bestllmfor.com/guide/goose-agent-local/ ; https://sonusahani.com/blogs/goose-ollama
20. OpenHands Windows without WSL: https://docs.all-hands.dev/usage/windows-without-wsl
21. Claude Code model config: https://code.claude.com/docs/en/model-config
22. Claude Code LLM gateways (subscriptions and gateways): https://code.claude.com/docs/en/llm-gateway
23. Claude Code connect to gateway: https://code.claude.com/docs/en/llm-gateway-connect
24. Ollama blog, Claude Code with Anthropic API compatibility (Jan 2026, v0.14.0): https://registry.ollama.ai/blog/claude
25. Ollama Anthropic compatibility doc: https://docs.ollama.com/api/anthropic-compatibility
26. KDnuggets, pairing Claude Code with local models: https://www.kdnuggets.com/pairing-claude-code-with-local-models
27. Claude Code legal and compliance: https://code.claude.com/docs/en/legal-and-compliance
28. Claude Code subagents (model field): https://code.claude.com/docs/en/sub-agents
29. LiteLLM, Claude Code Max subscription passthrough: https://docs.litellm.ai/docs/tutorials/claude_code_max_subscription
30. provider-claude-code ToS warning: https://workers.iii.dev/workers/provider-claude-code ; Tailscale Aperture passthrough: https://tailscale.com/docs/aperture/how-to/use-passthrough-mode/claude-subscriptions
31. claude-code-router repo: https://github.com/musistudio/claude-code-router
32. The Register (2026-02-20): https://www.theregister.com/software/2026/02/20/anthropic-clarifies-ban-on-third-party-tool-access-to-claude/5014546
33. WinBuzzer (2026-02-19): https://winbuzzer.com/2026/02/19/anthropic-bans-claude-subscription-oauth-in-third-party-apps-xcxwbn/
34. Kersai (2026-04-07, single source for April step): https://kersai.com/anthropic-killed-third-party-claude-access-heres-every-workaround-that-still-works/
35. Claude Code advisor tool: https://code.claude.com/docs/en/advisor
36. Agent SDK overview: https://code.claude.com/docs/en/agent-sdk/overview
37. Claude Code setup (Windows): https://code.claude.com/docs/en/setup
38. Ollama launch (Jan 2026): https://registry.ollama.ai/blog/launch
39. Minions paper: https://arxiv.org/abs/2502.15964
40. Hazy Research Minions blog (2025-02-24): https://hazyresearch.stanford.edu/blog/2025-02-24-minions
41. Anthropic, multi-agent research system (2025-06-13): https://www.anthropic.com/engineering/multi-agent-research-system
42. Reward hacking papers: https://arxiv.org/abs/2603.07084 , https://arxiv.org/abs/2604.01476 , https://www.emergentmind.com/papers/2609.28614
43. XDA, split work Claude/Qwen3-Coder/Gemma 4: https://www.xda-developers.com/i-split-my-coding-work-between-claude-qwen3-coder-and-gemma-4-and-it-costs-less-than-paying-for-one-subscription/
44. dev.to, local LLMs vs Claude Code reality check: https://dev.to/s3cloudhub/can-local-llms-really-replace-claude-code-a-2026-reality-check-for-developer-teams-i87
45. llama.cpp issue #30773 (Responses truncation marked completed): https://github.com/ggml-org/llama.cpp/issues/30773
46. llama.cpp server README (`POST /v1/responses`): https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
47. 24 GB model picks: https://insiderllm.com/guides/best-local-coding-models-2026/ , https://pactentia.com/blog/best-local-llm-for-coding-on-a-single-24gb-gpu
