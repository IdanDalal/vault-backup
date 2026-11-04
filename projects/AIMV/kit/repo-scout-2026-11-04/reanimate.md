---
type: research
created: 2026-11-04
author: jep
---

Verdict: borrow 3-4 measuring functions, never a dependency. MIT Claude Code skill that clones web UI animations and verifies by frame comparison. 6 days old, 20 commits (2026-10-29 to 10-31), 1.1k stars. No API keys, anonymous downloads. Capture half redundant (kc-engine deterministic). Nothing for 4K context loss or sound. Source: WebFetch only (clone blocked); mechanisms high confidence, line ranges medium.

1. Easing fit (scripts/easing.ts ~L66-127): 25 cubic-bezier easings, duration-multiplier grid 1.0-2.0 step 0.05, RMSE rank, good <0.03 / approx <0.08, overshoot >2 % = spring/back; accepts raw [[t_ms,v]] series. Use: run on tools/camflow.py pan/zoom/roll tracks of R1/R3/R4 per move; targets known gap (KC 2.2 % of time in 3 s+ moves vs R1 20.5 %); feeds _kc-camera.ts defaults. Python port ~60 lines. Value high, effort low, conf medium (10 Hz camflow noise).
2. Same fit as entrance audit on window.__kc.boxes (_kc.ts:42): flags linear entrances, overshoot %, stagger shape. Row in lifecycle.ts/check.ts. Value med, effort low-med.
3. Activity curve + motion window (compare.ts ~L117-129): per-frame mismatch vs previous frame; first/last >0.002 + peak; timing pass <=0.08 s. Use: crop ref moment vs KC counterpart, compare curve shapes; numbers for parity moments judged by eye. Value med, effort med.
4. Blurred + sharp mismatch (compare.ts ~L81-104, --blur 4): add to pixeq.py/pixeq_any.py; separates grain moved vs layout moved. Value med, effort low, conf high.
5. Settings-mismatch warning before compare (compare.ts ~L47-56, capture.json): write render.json per render (scale, samples, shutter, tol, ANGLE RENDERER string, commit, fps); pixeq/compare.sh/detail.sh/refcheck.sh warn or refuse on mismatch; catches silent SwiftShader fallback (render.ts:55,74). Value med-high, effort low, conf high.
6. Noise floor first (verify.md: ref vs itself before judging). We do it with pixeq_any; make mandatory in kit-process. Value low.
7. Leftover reporting (verify.md): "never relax thresholds silently"; stop after 5 no-progress rounds per row; each residual = row + last numbers + reason; "## Verification (round N of M)" block. Fits pass reports. Value med, effort low.
8. Spec table with source column + rows for things that must stay still (analysis.md s2). Use: per-word motion row on line cards + anchor rows (R5 coherence). Value med-low.
9. Pattern library numbers (analysis.md s5): web UI speeds too slow for KC (161.5 BPM 16th = 93 ms). Names only. Value low.
10. Ref/copy/diff sheets with % caption (sheet.ts ~98 lines). We have engine sheet mode + strip.py; borrow the 3-column row for notes-pass sheets. Value low-med.
11. Spring from overshoot (references/implementation.md): overshoot = exp(-pi z / sqrt(1-z^2)); 10 % ~ z 0.59, 5 % ~ 0.69, 20 % ~ 0.46; settle = 4/(z w). Lets _kc.ts overshoot take "overshoot %, settle ms". Value low.
12. Virtual clock (inpage/clock.js): kc-engine already pure f(t) + mulberry32. No value.
13. --gl tracing (gl.ts): classifier on our per-frame post params = inventory of what animates how per plate. Value low, effort med, conf low.
14. README pattern: one-line promise, 5-verb workflow, examples table with measured receipts, honest Limits, "No API keys", one-line install. Use with visual README (R13): table of gate numbers per pass. Value med.
15. Kit as a skill: SKILL.md ~140 lines + references/ loaded per stage + scripts/. Our kit = 1,196 lines read up front. Cuts context, makes public repo installable. Value med, effort med.

Pain-point coverage: 4K context loss none; lyric timing indirect (2,3,7); sound none; by-eye gates items 1,3,4,5; public write-up 14,15.
Next: port items 1 and 5 first (each < 1 day). MIT attribution, never install or run the skill.
