---
type: project
created: 2026-10-17
author: jep
status: active
---

# Handoff 2026-10-17: Knowledge Cutoff, route B, engine probe first

START HERE in a fresh session. Read this file, then [[knowledge-cutoff-v6-2026-10-17]] (the audit), then `D:\work\aimv-lab\kc-video\critique\v6\refs-build.md` (P(Doom)'s engine, read from its source).

## 1. Where things stand

- v6 is the last video of the old approach and the baseline to beat: `D:\work\AIMVs\ours\video\gate3\knowledge-cutoff-v6.mp4` (3:14.1).
- Idi's ruling, 2026-10-17, in his words: "we must choose B and rebuild on P(Doom)'s engine. We must start over based on your valuable report, and 'forget' my constraining/conflicting rules." "you try to match (and ideally EXCEED) the inspirations [...] instead of relying on me for arbitrary rules and instructions." "aiming for heaven by making sure we at least have ~150 lines per second as a technical foundation before artistically judging/analyzing anything." Next step: "option B's first domino (the 5s WebGL probe) in a new session starting from a handoff."
- The new contract: jep owns the creative and technical direction toward reference level and beyond; Idi judges results by eye. Only paths with a reference-level ceiling. The 116 rules in `critique\v6\rules-ledger.md` are void as rules and stay as a record of what was tried.
- Lines per second is a proxy for depth (P(Doom) 149, Ignore Previous Instructions 129, v6 about 11). The foundation it stands for is the engine's capability (GPU shaders, layers, one module per set-up) plus craft per set-up; code volume follows from those.

## 2. What still binds

1. The song: v8B, seed 3327, `D:\work\aimv-lab\kc\final\v8B-3327.mp3` (192.6 s), plus Idi's 1.5 s silent tail (ruling A, "fits perfectly"). No audio edits. Timing of record: `D:\work\aimv-lab\kc-video\sync\kc-timing-v2.json` (483 words, forced-aligned); drum hits: `kc-video\sync\drums.json`.
2. The lyric and the story: an AI frozen at its June 30, 2026 cutoff and told what happened since; chat bookends; the forgetting in the tail. Facts on screen stay true (receipts: `D:\work\aimv-lab\after-cutoff-world.md`, `after-cutoff-tech.md`).
3. Legal: P(Doom)'s code is MIT (keep its copyright notice in anything copied); its song, lyrics and plates are not ours (its README). Fonts OFL. The Harry line uses the name only, no film crests, fonts or imagery. At publish: YouTube AI disclosure and the "MiniMax-Music3" credit.
4. Machine: anonymous downloads only; plan-only billing (no API keys; never drive gemini.google.com); downloaded code runs only after Idi's okay; ffmpeg and git lines go in `.sh` files (worktree guard); one heavy job at a time (BSOD history 09-21).

## 3. Idi's taste (his words and notes, v2 to v6)

| likes | dislikes |
|---|---|
| chorus letters that change colour and hop when sung ("looks great") | "baby's-first" drawings: people, doors, suns, raccoon, flags, neuron, cat |
| text written by an invisible hand, or stamped like type | clipping, see-through bodies, lazy repetition |
| spectacle, WOW, jokes | props cut off by the frame edge; stamps over text |
| facts you can see | long captions; "June" five times on one screen; day numbers on timelines |
| the triple "Cut-off!", each one cut | empty or confusing elements (the WHO? box); dead space |
| the forgetting beat after the song | spoilers; frame grabs where thumbnails belong; every view count (only the million matters) |

Evidence: his 8 screenshots `D:\work\screens\AIMVs\`; 403 flaws `critique\v6\flaws-F1.md` .. `F6.md`; the measured gap `critique\v6\refs-approach.md`; `critique\v6\gap-sheet.jpg`.

## 4. The first domino: the engine probe

Question: can this PC render WebGL (the browser's GPU drawing system, which P(Doom)'s shaders need) headlessly, correctly and fast enough, under the jep account?

History:
- 10-13: headless Edge with the GPU on returned a blank canvas; `--disable-gpu` (software) fixed it for 2D drawing ([[knowledge-cutoff-2026-10-13]]:24).
- 10-15 probe (`D:\work\aimv-lab\research-video-tech-plan.md`:45-49): default flags and `--use-angle=d3d11` gave no WebGL; `--in-process-gpu --use-angle=d3d11` ran WebGL on the RTX 4090 for one frame; `--use-angle=vulkan` also reached the 4090. Inference then, untested: Edge's separate GPU process cannot start under the Standard user jep.
- 10-15 build: the full render with those flags gave black frames with 1 and 4 workers; never diagnosed ([[knowledge-cutoff-video-build-2026-10-15]]:43).
- Suspects: our `render.js` copies each frame with `canvas.toDataURL`, and a WebGL canvas made without `preserveDrawingBuffer` is wiped after display (a classic cause of black captures); P(Doom) reads its own render target through GPU pixel-pack buffers with fences (`app/src/engine/engine.ts`:648-682). Also the GPU sandbox under jep.
- P(Doom)'s export (`app/scripts/render.ts`:51-54): playwright-core, `channel: 'chrome'`, `--use-angle=metal --enable-gpu-rasterization --ignore-gpu-blocklist` plus anti-throttling flags; a `--headed` option renders in a visible window. Bun runtime and a Vite dev server. Mac-tuned: 4K took about 57 min on an M5 Pro.
- This PC, checked 2026-10-17: Node 26.8.1, npm 11.19.0, Edge 155.0.4283.45; no Chrome, no Bun. Clone: `D:\work\aimv-lab\refcode\pdoom-video\` (commit `fa164b74`), read only so far.

Steps:
1. **P1, no installs.** A minimal WebGL page: one fullscreen shader, a bloom-style blur, a line of text, driven by `?t=`. Render 300 frames (5 s at 60 fps) in headless Edge with `--in-process-gpu --use-angle=d3d11` (then vulkan), reading frames with `gl.readPixels` and `preserveDrawingBuffer: true`. Pass = no black frame, two runs md5-identical, equal by eye to the same page in a visible Edge window, at least 10 frames/s. If headless fails: try a visible window and the GPU-sandbox flags; log every attempt with its result.
2. **P2, after Idi's okay (one ask, listing exactly what gets installed).** Install Bun (or run the TypeScript under Node) and the repo's npm packages; point its renderer at Edge with Windows flags; render 5 s of P(Doom) itself. Pass = its own plates render here and match its YouTube frames by eye; speed noted.
3. Report both with receipts (frame sheets, md5s, flags, timings) in `projects/AIMV/`.

## 5. After the probe

If it passes:
1. Write Knowledge Cutoff's own treatment (a style bible) modelled on P(Doom)'s `docs/TREATMENT.md`: idea, tone, palette with one signal colour, type roles, karaoke rules (the chorus hop on every line), motifs, a plate table of 33-75 set-ups, one paragraph per plate.
2. Build plate by plate as engine modules under `docs/ENGINE.md`'s contract, each checked on contact sheets; Idi watches proofs.
3. Keep the checks: per-word sync, nothing over the lyric zone, nothing across the frame edge, reading time, the loop.

If it fails: report why, with receipts; then Idi chooses among a fix, rendering in a visible window, or porting the looks into the Canvas2D engine (route A).

## 6. Files

| what | where |
|---|---|
| the audit report | [[knowledge-cutoff-v6-2026-10-17]] |
| P(Doom) engine anatomy | `D:\work\aimv-lab\kc-video\critique\v6\refs-build.md` |
| measured gap, gap sheet | `critique\v6\refs-approach.md`, `critique\v6\gap-sheet.jpg` |
| flaws to avoid | `critique\v6\flaws-F1.md` .. `F6.md` |
| old rules (void, history) | `critique\v6\rules-ledger.md` |
| Gemini research | `critique\v6\staff-gemini.md` |
| reference dissections | `critique\v5\ref-1.md` .. `ref-5.md` |
| v6 code (old engine) | `D:\work\aimv-lab\kc-video\world6.html`, `world6-*.js`, `render.js` (has `--apad`), `tests\` |
| status, two staged intent-log rows | `D:\work\aimv-lab\kc-video\critique\v5\STATUS.md` |
| reference videos | `D:\work\AIMVs\*.mp4` |

Git: branch `worktree-kc-video-v5` holds the v5 and v6 reports (commits `96cac01`, `bc4a7ac`), unpushed because the permission checker blocked the push; the same files sit in the vault.
