---
type: project
created: 2026-10-22
author: jep
project: AIMV / Knowledge Cutoff
status: active
---

# Local agents pilot (option A): results, 2026-10-22

Follows [[local-agents-research-2026-10-22]] (Idi ruled A). Done-state: both tiers installed from ungated sources, 10 bounded KC tasks run on the local model with pass/fail fixed before each run, painted-over targets for the flattest crops. Every number below was re-checked by jep with a script; the worker's own claims counted for nothing.

## Verdict lines

- Local text tier: **7 of 10 tasks passed** under strict scoring. 567,833 tokens on the PC in 28 min of GPU time, zero Claude or ChatGPT quota.
- The worker caught an error in jep's 10-21 report (full4 had 2 allowed flips, the table said 1).
- Never delegate: counting, defect spotting by vision, whole-file rewrites.
- Codex CLI cannot run commands on this PC (its Windows sandbox blocks every process). jep's 3-tool worker loop replaced it and worked.
- Image tier: 16 edits at ~10 s each; **4 of 8 crops** gave usable detail targets, all from prompt A. Z-Image-Turbo runs at 4 s per 1024 px image.

## 1. What is installed (all ungated, sizes byte-checked against the HF API)

| item | path | size |
|---|---|---|
| llama.cpp b11819, CUDA 12.4 build | `C:\Users\jep\llm\llama.cpp\` | 0.66 GB zips |
| Qwen3.8-27B Q4_K_M + vision projector + MTP draft | `C:\Users\jep\llm\models\` | 19.0 + 0.9 + 1.7 GB |
| launcher (64K context, 8-bit KV cache, port 8080) | `C:\Users\jep\llm\serve.sh` | |
| patched chat template (allows a later system message; Codex sends two) | `C:\Users\jep\llm\qwen38-template.jinja` | |
| Qwen-Image-Edit-2511 Lightning 4-step fp8 + encoder + VAE | jep's ComfyUI `models\` | 20.4 + 9.4 + 0.3 GB |
| Z-Image-Turbo bf16 + encoder + VAE (own copy; Idi's lives in his ComfyUI Desktop) | jep's ComfyUI `models\` | 12.3 + 8.0 + 0.3 GB |

Start the text worker: `bash C:/Users/jep/llm/serve.sh --chat-template-file C:/Users/jep/llm/qwen38-template.jinja`. It fills 23.6 of 24.6 GB, so it runs alone: stop it before a render or a ComfyUI batch.

Measured speed: 40.3 tokens/s writing, 112 tokens/s reading (published: 47; the desktop shares the card).

## 2. The bake-off (10 tasks, pass/fail fixed before running)

| # | task | kind | result | time | why |
|---|---|---|---|---|---|
| T1 | gate table from full5b logs | text | **pass** 14/14 | 25 s | |
| T2 | full4 vs full5b gates | text | **pass** 28/28 | 39 s | first scored 27/28; the miss was jep's report, the worker read the log right |
| T3 | fix list from a critic report | text | **pass** 7/7 + 3 watch | 70 s | |
| T4 | group 286 check issues | text | fail | 212 + 17 s | groups and times right, every count wrong (31 for 38); attempt 1 spent its 8,192-token budget counting |
| T5 | read on-frame text, 8 frames | vision | **pass** 44/44 words | 51 s | truth hand-curated by jep from the 4K stills |
| T6 | planted defects, 8 frames x 2 runs | vision | fail 12/16 | 251 s | 0 false alarms; caught cut-off and blur; missed double exposure (the 1:48.58 defect type) and blank |
| T7 | rank 11 crops by fine detail | vision | **pass** rank corr. 0.74 | 133 s | |
| T8 | new tool `gate_table.py` | code | **pass** | 216 s | 3 gate runs; only the allowed file added |
| T9 | new TS function to a spec + test | code | **pass** | 391 s | first gate run; test 9/9, typecheck 0 |
| T10 | fix 2 planted bugs in `smart()` | code | fail | 274 s | fix correct, gate green; but it rewrote the whole file: line endings + 3 comments outside `smart()` changed (caught by jep's diff) |

Receipts: `D:\work\aimv-lab\local-pilot\log.jsonl`, `runs\t8|t9|t10.worker.json`, `scope-*.json` (file-hash snapshots), harness `pilot.py`, worker `worker.py`.

## 3. Rules from the pilot (delegation card)

| work | → | why (task) |
|---|---|---|
| extract numbers or items from logs and reports | local | T1, T2, T3 exact |
| read text off frames | local | T5 44/44 |
| rank crops by detail | local, as triage | T7 0.74 |
| new single file to a spec with a test | local, 3-tool worker | T8, T9 |
| counting, grouping with counts | script | T4: model guesses counts |
| catch rendering defects (stacked frames, blanks) | script (4K check) | T6 missed both double exposures |
| edit inside an existing file | local only with a find-and-replace tool | T10: whole-file writes drift |
| taste, direction, "reference level" | jep + Idi's eye | research: VLMs 26.5% vs experts 68.9% |

## 4. Harness findings

1. Codex CLI 0.153.4 on a local provider: requests reach `llama-server` (no cloud contact, verified in the server log). Two blockers: Qwen3.8's template rejected Codex's second system message (fixed by the patched template), and the Windows sandbox killed every command (workspace-write: "blocked by policy"; unelevated: exit 0xC0000142). The elevated sandbox needs administrator setup. The worker reported "blocked" honestly both times.
2. `worker.py` (jep, ~110 lines): chat-completions tool calls, three tools (read files, write allowlisted files, run the task's gate). The worker cannot run any other command, so it needs no sandbox; it also avoids the Responses-API bug (llama.cpp #30773).
3. Next fix for the worker: a find-and-replace edit tool, and a refusal when a write changes lines outside the named function.

## 5. Painted-over targets (image tier)

8 environment crops picked by jep from 12 flat-looking 4K stills (hero lyrics left out), 2 prompts each, seed 4. Scores by script: detail gain = fine-detail energy vs the original; layout = structure correlation (1.0 = same).

| crop | prompt A | prompt B | eye verdict |
|---|---|---|---|
| 116 blue light cone | x1.91, 0.96 | x1.06, 0.89 | **A usable**: scanline texture in the bars, fine grid |
| 156 perspective field | x4.19, 0.81 | x1.71, 0.28 | **A usable**: grid fills dead black |
| 064 essay page | x1.44, 0.97 | x0.85, 0.92 | **A usable**: letterpress feel, paper tooth |
| 184 ON FILE card | x2.24, 0.89 | x0.74, 0.36 | **A usable**: crisper halftone and stamp |
| 096 claims ledger | x2.17, 0.97 | x1.03, 0.80 | contrast only, no texture |
| 008 terminal panel | x2.23, 0.92 | x1.76, 0.89 | contrast and glow only |
| 148 page stack | x1.35, 0.91 | x0.80, 0.65 | spiky ink blobs, reject |
| 012 letter | x2.84, 0.54 | x0.92, 0.74 | invented blots and grid, reject |

- Prompt B (layered artefact) restyles into aged sepia cards or adds gibberish labels: reject.
- The detail score partly counts added contrast; agents take the texture idea and keep the bible's values.
- Sheet: `D:\work\aimv-lab\local-pilot\out\targets\targets-sheet.jpg`; prompts, seeds, scores: `targets.json` beside it.
- Not done: no plate agent has used a target yet. That waits for Idi's eye on full5.

Z-Image-Turbo smoke test: 4 tiles in `out\textures\` (4 s each after load). Cut-edge tiles carry real fray; fibre tiles come out faint and need contrast flattening before shader use.

## 6. Quota saved: what the pilot can and cannot say

- Measured: 567,833 local tokens, 0 Claude tokens for the work itself; jep's verification was one script run per task.
- Not measured: how many Claude tokens the same 10 tasks would have cost as cloud subagents. Cloud agents read less (T8 re-read a 450 KB JSON). An honest estimate needs the same tasks run once in the cloud.
- Setup cost was one session of jep's time; it does not repeat.

## Corrections

- `knowledge-cutoff-escalation-pass-2026-10-21.md`, whole-render gates table: full4 light/dark flips = **2 allowed** (150.17 and 184.35, `out\full4\gates\flips.log`), not 1. Found by the local worker in T2.
- [[local-agents-research-2026-10-22]] said no image model existed on the PC: Idi's ComfyUI Desktop holds Z-Image (Idi's correction, 2026-10-22); jep's probe only covered jep's own copy.

Related: [[knowledge-cutoff-escalation-pass-2026-10-21]], [[pc-hq-stack]].
