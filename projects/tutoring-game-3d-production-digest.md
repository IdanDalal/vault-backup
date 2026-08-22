---
type: research-digest
created: 2026-08-23
author: jep
project: tutoring
status: active
---

# 3D game production-quality digests (overnight fleet, Sat→Sun 2026-08-23)

Four research agents on presentation upgrades; full digests in session transcript, keepers here. APPLIED = shipped in the overnight build; QUEUE = ranked leftovers for later passes.

## 1 · Visuals (voxel-cozy, three.js Lambert+vertex-color stack)

APPLIED: golden-hour keyframes (warm key `#FFB36B` + cool ambient + pink horizon at low sun) · fog = horizon color lightened 8%, never darker than sky (A Short Hike rule) · foam contour lines marching shoreward (Alisavakis `sin((d - t·speed)·k)` gated by noise) · sequin sparkle field on water (thresholded twinkle noise × specular lobe, HDR ×2.6) · fake caustics on shallow floor (`pow(noise,4)·shallowMask·sunHeight`) · poor-man's bloom in the post pass (`c += 0.18·smoothstep(1,3,luma)·c` pre-ACES) · baked top-rim catch-light ×1.13 + wall-base contact shadow ×0.82 in the mesher (the Townscaper "model kit" read) · grass: wider blades, darker roots (0.4) brighter tips (1.28), denser.

QUEUE (ranked): Quilez sun-scattered height fog via fog-chunk override (~50 LOC, all materials share uniforms; iquilezles.org/articles/fog) · altitude saturation/hue ramp per biome in mesher (shore cool-green → hilltop warm `#A8C256`) · fresnel rim tint on props (`pow(1-NdotV,3)·0.25`, rim color from dusk keyframes) · dual-Kawase real bloom at ¼ res ONLY if screenshots still lack glow (Intel blur study; avoid UnrealBloomPass) · flower clump-scatter by low-freq noise > 0.6, 2 colors max per patch · weenie composition: S-path occlude-reveal of the lighthouse twice, bench at each reveal point (leveldesignbook massing).

DO-NOT: SSAO (baked AO is right), Reflector water, volumetric shafts on iGPU.

## 2 · Audio (all-synth WebAudio)

APPLIED: convolver reverb from generated decaying-noise IR (2.1 s, independent noise per channel = stereo width, one-pole darkening tail 0.5→0.08; sends sfx .25 / amb .12 / mus .10, predelay 30 ms) · mix numbers (glue −18/20/2.5/.01/.25, limiter −3/0/20, highshelf −5 dB@6.5 k + peak −3 dB@3 k on sfx+mus, highpass 100–110 Hz on amb+mus) · calm music composed: root+fifth detuned drone → lowpass, I–vi–IV–V pad (2 s crossfades, ~13 s/chord), sprinkles 70% chord-tones no-repeats, night = density 0.45 + top octave dropped · wind gusts (cutoff+gain rise together on 2–5 s random walk) · two overlapping surf wave-voices + foam-hiss layer after crest · FM birdsong (3 species: swoop-up 1740→3400, fall 2500→1850, trill LFO 42 Hz depth 260) · footsteps grass/sand/stone/snow from noise bursts, material read from block under feet · premium UI tick (2200 Hz sine + quiet octave) · splash (bandpass sweep 3 k→600 + droplet chirps) on water entry.

QUEUE: pad voice-leading to nearest tone (current pads re-attack) · echo-feedback darkening at night · phone "knock" layer (180 Hz) under the party kick · Haas widening for one-shots · FDN reverb only if convolver costs on weak machines (Signalsmith recipe).

## 3 · UI juice (kid-calm rules)

APPLIED: settleIn squash-settle on all panels/cards (0.42 s cubic-bezier(.22,1,.36,1)) · button press physics (:active scale .95 translateY 2px) · tilePop on typed letter slots (Wordle pattern) · sticker die-cut emoji (stacked drop-shadows) · title screen: gradient storybook logo + soft-light god rays (8–16 s breathing) + drifting motes + vignette — calm periods ≥8 s, opacity ≤.36 · hand-rolled canvas confetti (100 caps, gone ≤2.4 s) fired ONLY on achievements: set complete, story told, character made.

CALM LAWS (from Duolingo ABC/Khan Kids/Teach Your Monster evidence): escalation reserved for rarity; no motion within 200 px of active letter slots; everything decays to stillness; screen shake + hitstop deliberately NOT shipped (revisit only on observed reaction).

QUEUE: sparkle-to-journal flight on catch (Khan Kids collector pattern) · stat-cards slide-up on set completion · badge starburst (repeating-conic-gradient) · panel transform-origin from the trigger point.

## 4 · Rigless animation

APPLIED: hip-pivot leg swing via `geometry.translate` re-origin, trot phase (diagonal pairs), amplitude 0.55, ease-home on stop · body roll 0.05·sin(phase) · blink system (2–8 s, close-fast-open-slow, 18% doubles) on tagged dot-eyes · tail wag (happy 15 Hz amp 0.5 when following/petted; lazy sway idle) · asymmetric wingbeat `sin(u + 0.5·sin(u))` on birds + dragon + tagged prop wings · doll arms/legs in shoulder/hip pivot groups, opposite-phase swing, walking bounce kept.

QUEUE (all with numbers in transcript source: Yakudoo rabbit mirror the-ramenator.github.io/experiments/rabbit-run.html + Rosen GDC 2014): head look-at clamp ±0.6 yaw λ=8 smoothing → snap-then-settle · pupil saccades (quantize target 0.4–1.2 s) · notice-the-player script (freeze 0.5 s → head turn → blink 300 ms later) · serpentine chain for snake/fish (slither k=2π·1.75/N uniform amp vs swim k=2π·0.7/N tail-envelope amp²) · damped-spring helper (ryanjuckett) for tails/ears/landing overshoot · hop anticipation squash 120 ms → stretch → land 0.85 spring back · wave-hello (raise Back.easeOut → 2.5 Hz oscillate ×3 → lower).
