---
type: project-brief
created: 2026-08-21
author: jep
project: tutoring
status: todo
---

# 3D Game Brief ("the Roblox/Minecraft answer") — start in a fresh conversation

Goal: a 3D blocky world for K & D, same delivery constraints as GAME LAB: ONE self-contained HTML file, opens from file:// (WhatsApp → phone Chrome + old Linux laptop), zero network/assets, kid-editable CHANGE ME block, touch + keyboard, English mechanics woven in. Real networked multiplayer is out of scope, permanently.

## Verdict from the 2026-08-21 feasibility research

- **Feasible, and worth doing.** Recommended stack: **three.js embedded inline as a pre-bundled IIFE** (~670KB min, MIT license, total file ~1MB). WebGL from file:// works fine when the page fetches nothing; the one killer is ES module imports (CORS-blocked from file://) — three.js dropped its global build in r160, so run esbuild ONCE: `esbuild --bundle --format=iife --global-name=THREE` and paste the bundle in.
- Raw-WebGL mini-engine saves 600KB nobody will notice, costs ~2,000 extra LOC + Mali shader debugging. Canvas raycaster reads as a 1992 maze game to Minecraft kids. CSS 3D caps at toy scale. All three rejected.
- **Scope for v1:** seeded voxel island ~96×96×32, first-person walk/jump, place/break 4–6 block types, canvas-generated texture atlas, vertex AO + fog (never shadow maps, never antialias on phones), name-tagged wandering bots with chat bubbles (put real friends' names in CHANGE ME — the Roblox social feel), typed word gates + billboard English labels, world saved as a copyable "world code" string (localStorage is unreliable under content:// origins — and codes shared over WhatsApp ARE the multiplayer).
- **What carries the Roblox/Minecraft feel:** avatar identity, building agency, named social presence, blocky aesthetic. All four survive the constraints.
- **Controls:** left half = dynamic virtual stick, right half = look-drag, tap = place, long-press = break, jump button. Touch listeners MUST be `{passive:false}`; `touch-action:none`; track touches by identifier; pointer-lock is desktop-only.
- **Perf:** target WebGL1 surface; handle `webglcontextlost`/`restored` (~40 LOC, the top on-device failure); auto-rescue ladder = pixelRatio 1.0→0.55, then draw distance, then clouds/particles.
- **Estimate:** 2 long sessions + 0.5 contingency. Session 1 = island + physics + controls + rescue (the risky one). **Day-1 first step: WhatsApp a 20-line WebGL smoke-test HTML to the girls' phones to confirm the content://→Chrome→WebGL path and baseline fps BEFORE building.**

## Design rules carried over from D's observed profile (session 4)

- Death→control-return under ~1s, always; the recovery act must itself be input (typing the word = agency, per the competence-thwarting literature). No timers, no forced waiting, ever — the Brainrot-jail minute is the documented anti-pattern.
- Stakes as ratchets: collections/bases that grow or pause but never regress; streaks that risk breaking are fine, calendar streaks are not.
- Drop the "instead of an ad" fiction; the gate word is a "power word" she performs.
- Expectation management with the girls: they may be imagining full Roblox. Frame v1 as "I built you a 3D world of our own" and let bots + world codes carry the social illusion.
