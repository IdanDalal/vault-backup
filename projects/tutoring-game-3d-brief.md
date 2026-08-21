---
type: project-brief
created: 2026-08-21
author: jep
project: tutoring
status: todo
---

# 3D Game Brief ("the Roblox/Minecraft answer") — start in a fresh conversation

Design layer: verb thesis v2 + full mechanics research digest now in [[tutoring-game-3d-verbs]] (2026-08-21; Customize/Collect/Combine/Create, catch ritual, word economy, co-op, build-scope ladder).

Goal: a 3D blocky world for K & D, same delivery constraints as GAME LAB: ONE self-contained HTML file, opens from file:// (WhatsApp → phone Chrome + old Linux laptop), zero network/assets, kid-editable CHANGE ME block, touch + keyboard, English mechanics woven in. Real networked multiplayer is out of scope, permanently.

## Verdict from the 2026-08-21 feasibility research

- **Feasible, and worth doing.** Recommended stack: **three.js embedded inline as a pre-bundled IIFE** (~670KB min, MIT license, total file ~1MB). WebGL from file:// works fine when the page fetches nothing; the one killer is ES module imports (CORS-blocked from file://) — three.js dropped its global build in r160, so run esbuild ONCE: `esbuild --bundle --format=iife --global-name=THREE` and paste the bundle in.
- Raw-WebGL mini-engine saves 600KB nobody will notice, costs ~2,000 extra LOC + Mali shader debugging. Canvas raycaster reads as a 1992 maze game to Minecraft kids. CSS 3D caps at toy scale. All three rejected.
- **Scope for v1:** seeded voxel island ~96×96×32, first-person walk/jump, place/break 4–6 block types, canvas-generated texture atlas, vertex AO + fog (never shadow maps, never antialias on phones), name-tagged wandering bots with chat bubbles (put real friends' names in CHANGE ME — the Roblox social feel), typed word gates + billboard English labels, world saved as a copyable "world code" string (localStorage is unreliable under content:// origins — and codes shared over WhatsApp ARE the multiplayer).
- **What carries the Roblox/Minecraft feel:** avatar identity, building agency, named social presence, blocky aesthetic. All four survive the constraints.
- **Controls:** left half = dynamic virtual stick, right half = look-drag, tap = place, long-press = break, jump button. Touch listeners MUST be `{passive:false}`; `touch-action:none`; track touches by identifier; pointer-lock is desktop-only.
- **Perf:** target WebGL1 surface; handle `webglcontextlost`/`restored` (~40 LOC, the top on-device failure); auto-rescue ladder = pixelRatio 1.0→0.55, then draw distance, then clouds/particles.
- **Estimate:** 2 long sessions + 0.5 contingency. Session 1 = island + physics + controls + rescue (the risky one). **Day-1 first step: WhatsApp a 20-line WebGL smoke-test HTML to the girls' phones to confirm the content://→Chrome→WebGL path and baseline fps BEFORE building.**

## Art direction contract (added 2026-08-21 after the visual-excellence research; binding for the build)

Named direction: **"Townscaper light on Minecraft bones."** One desaturated teal field for sky and sea (they nearly merge), with the island carrying all the saturation: warm coral/mustard accents on muted greens. Poster logic — every screenshot should read as a cozy diorama. Calibration screenshots regenerable via `~/render-tools/shoot.mjs` (positive: Townscaper web, The Aviator, Summer Afternoon; negative: stock three.js minecraft demo, raccoon-heist gameplay).

- **Palette, locked before any geometry.** Hue-shifted ramps: each shadow step moves ~20° toward blue and desaturates; each light step moves warm and gains saturation. Base set: sky horizon `#BFD8D2` → zenith `#4E7E8C`; water deep `#3F7480` / shallow `#6FAAAC` with a pale shore-halo ring `#D8E8E2` baked at the coast; grass sage `#7FA36B`; dirt `#8A6D4F`; sand `#E3D3A8`; stone `#9A958C`; wood `#B0623F`; leaves `#5E8A56`; accents coral `#E0574F`, mustard `#E8B94C`, teal `#3FBFB0`. Saturation budget: resting surfaces 10–25%; accents may exceed; mean frame saturation must land 5–25% (below reads plastic, above reads cartoon — measured thresholds from build-world's pixelstats).
- **Atmosphere coupling:** `scene.fog` color = sky horizon color = `scene.background`, FogExp2 tuned so the far coast melts into sky. ACESFilmicToneMapping + SRGBColorSpace (this pair alone separates "game" from "programmer art").
- **Sky dome:** BackSide sphere shader, 3-stop gradient (horizon glow / mid / zenith) + sun disc `pow(d,800) + pow(d,8)*0.25` halo. The 2D game's solid-yellow-circle-with-bloom sun is the documented anti-pattern this replaces.
- **Light rig, count fixed forever:** HemisphereLight cool sky `#9FC2E8` over warm ground `#54463A`, plus one warm DirectionalLight sun. Day/night animates intensity and hue only. Torches/glow use emissive materials and vertex color so the visible-light count never changes (light count is a shader-permutation key; changing it mid-game costs 600–900 ms compile stalls on phones).
- **Canvas atlas:** every tile = base color + 2-octave value noise + per-pixel grain; plus per-face value/hue jitter (a few % value, a few degrees hue, seeded by position). Banned: flat single-color fills, the saturated `#00FF00` grass family.
- **Vertex AO baked into chunk geometry:** `ao(side1,side2,corner) = side1&&side2 ? 0 : 3-(side1+side2+corner)` into vertex colors; flip the quad diagonal when `a00+a11 > a01+a10` to kill seams. Cheapest "real" look available at zero shader cost.
- **Camera:** voxels shown at an angle wherever possible (Crossy Road: "it looked 100 times better"); first-person FOV 60–70 on phones; any title/spectate framing gives the sky at least half the frame.
- **Production-feel layer (DOM/CSS, nearly free on phones).** Gravecrawl evidence, verified by my own screenshots: most of its felt production value lives in this layer. Adopt: a display font with letterspacing/small-caps; a world title card on load ("THE ISLAND OF ..." with the girls' world name); feat/achievement toasts; the power-word gate styled as a glowing ritual card; HUD built from icons, orbs, and meters (banned in HUD: rectangular stat-card grids); an inline CSS loading screen with logo shown before the world finishes meshing.
- **Game-feel constants** (from threejs-game-skills, MIT): screenshake trauma-based, shake = trauma², decay 1.4/s, max offset 0.55 units, max roll 0.1 rad; block-break trauma ~0.2; hitstop reserved for heavy events, 60–90 ms at 0.05 timescale scaling the gameplay delta only (RAF keeps running); squash/stretch 1.15 stretch / 0.9 squash settling ~180 ms; pickup pop scale 1.6→1.0 over 280 ms + HUD counter punch 1.2→1 over 120 ms; impact emissive pulse to 2.4 tweening back over 220 ms; every SFX gets ±6% pitch variance (procedural oscillator synth, AudioContext unlocked on first gesture); all randomness through the seeded world RNG, effects driven by accumulated game time.
- **Verification gauntlet, every visual session:** capture a fixed 8-shot list (establishing, 0.5 m close-up, dawn and noon lighting extremes, underground/enclosed, coastline, FX at peak, UI composite) via `~/render-tools/shoot.mjs`; judge against the calibration anchors before claiming quality. Auto-fail list: flat single-color sky; gray fog; black shadows; saturated-green grass; glow standing in for missing shape; stat-card HUD. Sky/fog/exposure/materials form one coupled system → one sequential owner per polish pass (build-world measured parallel visual agents scoring worse than a single owner, defects 66→26 vs 66→66).
- **Reference material for the build session (re-clone fresh, both anonymous):** github.com/majidmanzarpour/threejs-game-skills (MIT — read `references/shader-cookbook.md`, `game-feel.md`, `visual-scorecard.md`, mobile checklists) and github.com/thrixel/build-world (Apache-2.0 — read `engines/threejs/threejs.md`, `PITFALLS.md`, `PROCESS.md`; skip its commercial asset pipeline). Full research digest: [[tutoring-game-3d-collab-research]].

## Design rules carried over from D's observed profile (session 4)

- Death→control-return under ~1s, always; the recovery act must itself be input (typing the word = agency, per the competence-thwarting literature). No timers, no forced waiting, ever — the Brainrot-jail minute is the documented anti-pattern.
- Stakes as ratchets: collections/bases that grow or pause but never regress; streaks that risk breaking are fine, calendar streaks are not.
- Drop the "instead of an ad" fiction; the gate word is a "power word" she performs.
- Expectation management with the girls: they may be imagining full Roblox. Frame v1 as "I built you a 3D world of our own" and let bots + world codes carry the social illusion.
