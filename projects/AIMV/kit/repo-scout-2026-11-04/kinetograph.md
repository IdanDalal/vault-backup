---
type: research
created: 2026-11-04
author: jep
---

Verdict: real, very active, poor engine swap (does not draw three.js, no WebGL readPixels). Borrow ideas only, copy no code (PolyForm Small Business 1.0.0, source-available). Source: WebFetch only (clone blocked); file + section cites, no line numbers.

Facts: "programmatic video engine, made for agents"; Remotion-API TS or HTML without a browser; Node + Rust N-API (Blitz/Stylo/taffy/Parley DOM, wgpu + Skia compositing, naga GLSL, ThorVG Lottie, ffmpeg-next encode, offline Web Audio). Created 2026-10-23, last push 2026-11-03, 1,581 commits in ~12 days, 452 stars, v0.3.0 beta. GPU tests only on Apple M4 (Windows GPU path least tested). npm install anonymous, Windows x64 prebuilt, no API keys found (docs only, source unchecked). Blockers (kinetograph.dev/docs/compat): "Three.js is not drawn"; readPixels, MSAA renderbuffers, cube textures, sampler2DShadow not drawn; empty canvas each frame. kc-engine port = full rewrite.

1. Onion skin (AUTHORING.md s9, SKILL.md step 2): blend a frame range into one image = motion path trace. We have contact sheets, no single-image trace. Use: camera audits (_kc-camera.ts), word paths (onPath, dropLine, bounceWord), blind panels scoring motion from one still. Build: ffmpeg tmix/tblend or numpy max/mean. Value high, effort low, conf high.
2. Release loudness gate (audio analyze; AUTHORING.md s9): integrated LUFS, true peak, clipped samples, silences, per scene. Targets ~-14 LUFS, TP < -1 dBTP, 0 clipped. Gap: kit-audio-pipeline has stem meters, no master LUFS/TP. Add ffmpeg -af ebur128=peak=true on take + final mux as receipt. -14 = playback convention (YouTube turns loud down, never quiet up), not a measured optimum. Value med-high, effort low, conf high.
3. Frame reuse for held windows (INTERNALS.md "Frame reuse", crates/core/src/reuse.rs): skip provably identical frames, report "repeated". Our holds declared (_kc-rhythm.ts heldT 224, declareFps 238); reuse last rgb24 buffer in render.ts; 4K ran 8 h 26 min before dying. Key on declared hold, never pixel compare (adaptive sampling not bit-repeatable). Value med, effort med, conf medium (share of held frames unknown).
4. Determinism guard (INTERNALS.md step 2): shim ties Date, Math.random, timers, rAF to frame number. Our pure-f(t) rule is convention only. Add: Math.random/Date.now/performance.now warn or throw with scene id in render mode + grep gate over app/src/scenes/. Value med, effort low, conf high.
5. Typecheck before render: "Rendering never type-checks, so a misspelled prop ... draws at full opacity without an error." Confirm kc-engine scripts/check.ts runs tsc --noEmit; if not, add to pre-render gate. Value med, effort trivial.
6. Look-without-pixels loop (SKILL.md, AUTHORING.md s9): strip -> still -> onion -> inspect --frame N (layer bounds, effects, text lines) -> lint (overflow, off-canvas, overlapping text, missing fonts, frame + layer id); all --json; MCP returns PNGs. We have window.__kc.boxes (_kc.ts 42); gap = text dump per sampled frame (lit word, boxes, overlaps) -> lyric timing checkable as text by a blind critic or the local model. Value med, effort med.
7. Golden stills with tolerance (snapshot, max channel diff 2): our GPU noise 2-3/255 -> tolerance 3-4 + pixel-count cap; one frozen still per REUSE module via ?only=kit-* (timeline.ts 187-198) so video 2 edits cannot silently break KC-proven modules. Value med, effort low-med, conf high.
8. Animatic gate: brief -> script -> storyboard -> look; review animatic before animating, again after hook and reveal. "Never animate against an unapproved storyboard without saying so." Mirrors KC Gate 2 locking look from 9 stills (kit-process phase 6). For Pay Attention: timed-box + lyric animatic on click reel between song lock and style frames. Value med, effort low.
9. Public-repo doc shape: AGENTS.md (ask-before list), CLAUDE.md, SKILL.md + references, compat "known gaps" page, THIRD-PARTY-NOTICES.md, COMMERCIAL.md. For knowledge-cutoff: THIRD-PARTY-NOTICES (P(Doom) MIT, OFL fonts, ffmpeg) + failure-ledger page. Value low-med.
10. Engine swap: rejected (three.js, readPixels, untested Windows GPU). Revisit only for a pure 2D/CSS/SVG video.
11. Spark (scout's own idea, not in kinetograph): render 4K in ~600-frame segments to intermediate files + manifest, restart browser per segment, concat. Context loss costs one segment; moov-less repair no longer needed. Value high, effort med, conf medium (context-loss cause unproven).
12. Minor: --draft preset; bench --range per-frame stage timing; layer cache ignoring opacity/blend; track (Blender tracker) only for live footage.

Not checked: source crates/ packages/, examples, SCENE.md, ENGINE.md, telemetry.
