---
type: reference
created: 2026-08-22
author: jep
project: tutoring
status: in-progress
---

# MengTo / ThreeUI technique digest — distilled for the island game

Four research agents, 2026-08-22 (Idan's find: threeui.com + 6 GitHub repos). Full agent transcripts are session-lost; THIS note + local sources are the durable record. Local study copies: `~/game3d/ref/mengto/` (49MB: 6 shallow repos stripped of .git, the 4 golden Skills dirs, public single-file demos `landscape.html` / `japanese-tower.html` / `sakura-branch.html`, extracted `sec-*.js` strips). Companion: [[tutoring-game-3d-playtest1]].

## Licensing map (decides how each source may be used)

- **MIT: threeui repo + Skills repo** (+ npm `@designcodeio/threeui`). Fonts SIL OFL. Port freely, keep MIT notice if copying substantially. The Skills repo `agent-skills/web-design/threejs-{weather,landscape,towers}` + `build-threejs-scroll-worlds` dirs are distilled dependency-free versions of the flagship demos (27–38KB, base64-stripped) — THE port sources.
- **No license granted: towers, complete-shelf, sylva, kage standalone repos** (READMEs explicitly reserve code+artwork). Study + reimplement mechanisms only; never copy code or embedded assets.
- threeui.com: Community tier free (source public), Pro $99/yr gated — live demos public, formatted source gated. Scout's verdict: the free `landscape.html` already carries the most valuable systems; Pro marginal for us (Sunset Valley water-ripple params already captured below).

## APPLIED to island.html this session (Sat 2026-08-22)

1. **Adaptive resolution governor** (kage/landscape pattern): raw-frame-time average over 45 frames; >24ms → scale ×0.85 (×0.64 if >50ms), <14ms → +0.08 recovery; pixelRatio × scale + post-RT resize; floor rung sheds post+shadows+70% grass once at scale≤0.43. Replaced the fixed 2-step rescue ladder.
2. **Split-tone grade**: teal shadows `c*vec3(.84,1.02,1.07)` weighted `smoothstep(.5,0,l)*0.3`, warm highs `vec3(1.03,1,.97)*smoothstep(.5,1,l)*0.5`, inserted between contrast and saturation in our post pass.
3. **Lamp glow sprites + decorrelated flicker**: additive radial-gradient sprite per lamp block, opacity `0.22+0.09*sin(t*(2.3+i%5*0.7)+i*2.1)`; rebuilt on lamp edits.
4. **Grass root-AO ramp** (sylva "astroturf" fix): blade vertex colors 0.45 root → 1.15 tip, multiplied under instanceColor.
5. **Butterfly spook** (sylva behavior): proximity 0..1 with asymmetric smoothing (snaps on, calms slowly `1-pow(.25,dt)`), flees up/away, flap rate +9Hz under spook.

## QUEUED (v9 candidates, ranked; source pointers into ref/mengto/)

1. **Time-of-day presets × weather multipliers** (Skills threejs-weather+landscape, MIT): 4 THEMES as flat color/light/fog records + CLEAR/RAIN/STORM/SNOW as multiplier overlays (`fogK,sunK,hemiK,ambK` + lerp targets); crossfade 1.15s, mid-transition freeze so mashing never pops; CSS vars ride the same preset so DOM UI re-skins with the world. Weather button = kid-facing magic; STORM = RAIN with dials pushed. Est. ~250 LOC.
2. **Rain/snow camera-anchored pools** (same source): fixed Points pools (4400/5200) in a small volume carried ahead of the camera, density via setDrawRange; blizzard envelope calm/build/blow/ease; snowPack accumulator whitens terrain + grass tips first. **Sentence hook: "It is raining." / "It is snowing." → weather actually changes = the no-dead-sentences law made spectacular.** ~150 LOC.
3. **Lightning**: dedicated DirectionalLight outside themes; leader + 1–3 return strokes `exp(-t/.085)`; sky brightened multiplicatively; thunder delayed by distance. ~50 LOC.
4. **Water tap-ripples** (Sunset Valley params, captured): `uRip[40]` uniform slots (x,z,start,strength), vertex rings `sin(w*1.15)*exp(-|w|*.4)*exp(-age*1.15)`, w=dist−age*13; fragment tilts normal by ripple gradient. Zero draw calls. ~70 LOC on our water shader.
5. **Scan-pulse island reveal** (sylva): shared `uScanO/uScanR` on every material, discard beyond wobbled front, wireframe cage rides ahead of solids by a lag; disposed after. First-open ceremony. ~80 LOC.
6. **Deterministic inspect transition** (complete-shelf, reimplement): matrixWorld.decompose → move to scene at exact pose → one smootherstep timeline to a fixed camera+object pose; `setViewOffset` shoves subject beside a DOM panel. For a "look at your creature/word" moment. ~120 LOC.
7. **Clip-plane grow-from-ground** (towers, reimplement): one shared `THREE.Plane` in all structure materials + cap disc riding the cut; garden/base buildings could construct themselves. ~60 LOC.
8. **Luminance-gated aerial haze** (sylva): distance haze mix gated by surface luminance (`smoothstep(.003,.075,luma)`) so far shadows keep silhouette while lit surfaces lift. Needs fog-chunk patching across materials. ~40 LOC.
9. **Butterfly full flight stack** (sylva): cruise/approach/land/takeoff state machine, perch scoring `n.y+n.z*.42`, bank from lateral acceleration, wander faded on approach. Upgrade for our birds too.
10. Misc pocketable: contact-shadow blob sprites; sun-elevation-aware shadow extent `ext=13+30*cos(el)`; boot JOBS array with named steps for a charming loading screen ("Raising the lighthouse…"); mip bloom + chromatic aberration + post-encode contrast pivot (kage composite) if we ever want night scenes; WebAudio loop-seam trick `loopStart .05 / loopEnd −.10`; `damp(a,b,λ,dt)=lerp(a,b,1-exp(-λ dt))` as the universal smoothing idiom.

## Cross-cutting confirmations of our existing choices

Static baked shadow maps (`autoUpdate=false`), canvas-everything textures, deterministic mulberry32 seeds, FogExp2-color-as-master-darkness, quality tiers decided at boot, dt clamp 0.05 with raw-dt perf reads, `?q= ?dpr=` style URL debug knobs (worth adding), fill-bound = pixels-are-the-only-knob.
