---
type: reference
created: 2026-08-21
author: jep
project: tutoring
status: done
---

# Claude × three.js collaborations — research pass 2026-08-21

Companion to [[tutoring-game-3d-brief]]. Three agents: seed-link deep-dive, community sweep, open-source technique donors. All sources anonymously accessible; licenses verified where code reuse is on the table. Unverified claims labeled.

## The three seeds, resolved

- **Tank game = "Claude of Tanks"** (Kevin B. Liu, r/ClaudeCode 2026-08-20, 275↑). WoT-Blitz-style, 111 procedural vehicles, 16 maps, WebSocket multiplayer, MIT, open source. Play: https://cot.kevinliu.studio/ · repo: https://github.com/Kevin-Liu-01/Claude-of-Tanks. Workflow (author's own words): 3 weeks, Fable at Max/Ultracode + a Codex perf week; AGENTS.md + per-subsystem rule files with hard invariants (meters/seconds/radians, fixed 60 Hz, deterministic server logic); one agent per vehicle family in isolated git worktrees; a critic agent reviews rendered screenshots before an orchestrator commits. Stated lesson: text-only review misses visual defects; the loop that worked was change → render → screenshot → critique. Has full mobile touch controls.
- **LinkedIn pixel-art demo** (Tural Dzhalilov, "built with Claude Opus 5"). Post text public, video login-gated, no demo, no source; effectively an ad for quadcode.ai. Technique described: render at 1/3 res, depth+normal edge-detection outline pass, quantized shading, nearest-neighbor upscale. Matches three.js's stock RenderPixelatedPass (my inference; post doesn't name it). Cheap mobile version: low-res render + `image-rendering: pixelated`.
- **YouTube racer = "Claude Kart"** (Digital Digest Live, 2026-08-16, 77s, ~23 views). ONE 58KB index.html, Mario-Kart-style, player "Claude" vs GPT-Bot/Gemini/Llama, procedural everything incl. Web Audio sound. Play: https://atiqur-rahman-pro.github.io/claude-kart/ · repo MIT. **Claude authorship UNVERIFIED** ("Claude" is the character name; nothing in repo/video mentions Claude as a tool). Two lessons anyway: (1) its "single file" still CDN-loads three.js via import map, so it dies offline — confirms the brief's inline-IIFE decision; (2) touch buttons write the same `keys` object the keyboard writes, one input path, zero duplicated logic.

## Best of the wider wave (community sweep, ranked for our target)

1. **JanneCraft** — dad + 8-year-old, Minecraft clone in under a day, Claude Code wrote everything incl. binary WebSocket protocol; NPCs, crafting, day/night. Closest verified voxel-feel match (server-based though). https://broddin.be/creating-a-minecraft-clone-in-under-a-day/
2. **Procedural Desert Explorer / SNOWFLOW** — visual ceiling of the wave: GPU clipmap dunes with persistent footsteps, cloth sim, zero meshes/textures, all shader. Claude Code + Opus 5, ~14h, ~5M tokens. Babylon.js/WebGPU. https://desert-dusky.vercel.app/
3. **Claude of Duty** (Matt Shumer) — 55k-line procedural three.js FPS, sub-agent-per-subsystem + critic loop + screenshot/imagediff pipeline; the template others genre-swapped. https://github.com/mshumer/Claude-of-Duty
4. **Super Mario Galaxy movie game** — 76K LOC TS, spherical gravity, 53 days, Claude wrote ~95%, runs on mobile; lesson: have Claude build its own review/debug tools. https://supertommy.com/games/super-mario-galaxy-movie-game/
5. **Red Panda Vibes** — three.js pastel platformer, Claude Sonnet 3.7, open source, touch + desktop input. https://collidingscopes.github.io/red-panda-vibes/
6. **Rocket Arena** — Rocket League clone, Opus 5; agent plays 20s verification matches after each feature. https://rl-opus5.vercel.app/
7. **The Long Silence** — Outer-Wilds-like in 24h; playability-first then optimization, 17 automated validation checks. https://github.com/achimala/TheLongSilence
8. **cooked.house** — dad + 12-year-old Roblox-refusal FPS; honest failure notes: Claude strong on architecture, weak on UI design and map layout.
9. **VIBE_WEAVERS** — single self-contained HTML file, three.js + Rapier, MIT; the best single-file specimen found (Claude specifically: unverified). https://leoawen.itch.io/vibe-weavers
10. **Laser Nuke** (DesignCourse video) — key trick: in-game slider editor so feel-tuning skips prompt round-trips. https://www.youtube.com/watch?v=VG_HKh-zfOs

Also: SANDLOX (itch, Claude-disclosed block sandbox), Vibe Safari, FutureCop-style arena (12h pure prompting), MarsInterloper (real NASA MOLA data), Doors (.vox portal rooms), 2025 Vibe Coding Game Jam (jam.pieter.com, ~1,170 entries, richest further pool, per-entry AI attribution unverified).

## Technique donors (licenses verified, ordered by relevance)

1. **three.js manual "Voxel Geometry"** (MIT, self-contained example pages) — sparse cell map `{cellId: Uint8Array}`, culled-face merged BufferGeometry, atlas UV math with per-face rows, Amanatides–Woo DDA grid raycast for place/break (skip THREE.Raycaster), edit rebuilds cell + 6 neighbors. Core engine blueprint. https://threejs.org/manual/en/voxel-geometry
2. **dgreenheck/minecraft-threejs-clone** (NO license → re-implement, don't copy) — the save-string answer: **seed + edit-delta serialization**; regenerate terrain from seed, replay deltas. Our world code = {seed, deltas} → RLE → base64. Also `requestIdleCallback` chunk builds. 10-part YouTube tutorial series.
3. **0kzh/minicraft** (MIT, liftable) — same architecture with safe license: chunked world, physics/collision module, orientation-based face shading (cheap Minecraft look without AO), worker chunk-gen that degrades to sync for file://. https://github.com/0kzh/minicraft
4. **joe-shenouda/infinite-minecraft-html** — existence proof: whole game in one 12.8KB index.html (`world["x,y,z"]` map, per-chunk merged geometry, atlas per-face UVs). Fix its sins: CDN three.js, hotlinked wiki texture atlas, no touch. MIT in README only.
5. **nipplejs** (MIT, one dep-free file) — virtual stick: dynamic stick under first touch (Minecraft-PE feel), left zone move / right zone look, per-touch identifier bookkeeping. Worth inlining or imitating.
6. **0fps.net meshing + AO articles** + mikolalysenko/greedy-mesher (MIT) — ~60-line greedy mesher; vertex-AO formula `side1&&side2 ? 0 : 3-(side1+side2+corner)` into vertex colors; quad-diagonal flip rule kills AO seams. Vertex AO = cheapest "real" look on weak GPUs; greedy merge must include AO in merge criteria.
7. **vyse12138/minecraft-threejs** (MIT) — six-ray directional collision for solid movement without a physics lib; block-highlight wireframe. WARNING: README claims mobile-friendly; agent read the control source, found no touch path.
8. **Context-loss + pixelRatio hardening** — `webglcontextlost` preventDefault + `restored` handler that re-runs the mesher (voxel array is source of truth, recovery is free); cap pixelRatio ≤2, drop toward 1 on rolling frame-time overage. Matches the brief's rescue ladder.
9. **Digital Bricks devlogs** (read-only) — sizing evidence: RLE took a chunk 361KB→5KB; binary+RLE ~1KB/chunk. Our 96×96×32 island lands low-KB, WhatsApp-safe, esp. column-major RLE (vertical runs dominate islands).
10. **three-spritetext** (MIT) — bot name tags: text → offscreen canvas → Sprite; auto camera-facing, scale from `measureText`, zero assets. ~30 lines to imitate.
11. **ordoghl/vibe-doom** (MIT, explicit Claude Code attribution, index.html + one game.js) — seed-based deterministic level gen; Web Audio oscillator/noise SFX (the only offline sound option for one file).
12. **Lallassu/VoxLords** (MIT) — voxel explosion/debris particles for satisfying block-break; heightmap-from-PNG world encoding.

## Cross-cutting verdicts

- Meshing: culled-face merged geometry per chunk is right at our scale; greedy meshing only if measured triangle count demands it.
- Save string: {seed + RLE'd deltas + base64} beats full-grid encoding on every axis.
- Renderer: plain WebGLRenderer; Claude Kart's WebGPU-with-fallback evidence says WebGL is the safe file://-Android read. Confirms brief.
- Textures: every Minecraft atlas seen in the wild is CC-BY-NC-SA or wiki-scraped; canvas-generated atlas sidesteps all of it. Confirms brief.
- **The gap = our opening:** no found project combines touch voxel gameplay in a single offline file. Donors 1+5+8 compose it; nobody has shipped the composition.

## Workflow patterns to adopt for the build sessions

- Nobody one-shots the good ones: dense written brief up front (~20% of final result per the desert-explorer builder), then hours of increments.
- Close the eyes-on-the-game loop: render + screenshot + critique each iteration (we have `~/render-tools` Playwright for exactly this). The single most repeated differentiator.
- Executable invariants in a persistent rules file (units, fixed timestep) keep fresh sessions honest.
- Touch-as-keyboard aliasing: touch UI mutates the same key-state object as keyboard.
- In-game slider editor for feel-tuning beats prompt round-trips.
- Verification-by-play: timed self-play sessions / automated validation checks after each feature.
- Kids as product managers worked twice (JanneCraft, cooked.house); K & D can fill that role.
