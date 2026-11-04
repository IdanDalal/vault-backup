---
type: research
created: 2026-11-04
author: jep
---

# Repo scout 2026-11-04: kinetograph, reanimate, video-director, earshot

Verdict: install none, borrow ~20 methods. The 4 repos sell agents eyes and ears plus gates. Our renderer and word sync lead all four. They lead on standard measurements (loudness, true peak, chance baselines), render fault tolerance ideas, and honest public write-ups.

Source caveat: all 4 read through WebFetch (raw files, GitHub API); the clones were blocked by this session's worktree isolation (jep's sequencing error). Line numbers approximate. Per-repo reports: `repo-scout-2026-11-04/`. Claims about our engine checked against `kit-engine-components.md` (receipts below).

## The 4 repos

| repo | what | age, signal | license | verdict |
|---|---|---|---|---|
| 0xS4N4TG/kinetograph | browserless video engine for agents, Remotion API, Rust GPU compositor | 2026-10-23, 1,581 commits in 12 days, 452 stars, v0.3 beta | PolyForm Small Business (source-available) | ideas only; engine swap impossible: "Three.js is not drawn", no WebGL readPixels |
| NiazMorshed2007/reanimate | Claude skill: clone a web UI animation, verify by frame diff | 2026-10-29..31, 20 commits, 1.1k stars | MIT | borrow 3 measuring functions |
| win4r/video-director | Claude skill: 8-phase video workflow, timeline.json, 2 Python QA scripts, critic rubric | 2026-10-28..30, 8 commits, 299 stars; evals n=1, author: "a direction, not a measurement" | MIT | best fit; 4 gates we lack |
| Leonxlnx/earshot | CPU audio ears for agents: sync, sheets, critics, SFX bank (CLAP + AST models, ungated) | 2026-10-16..22, 40 commits, 3.8k stars, alpha | MIT | borrow methods; SFX bank needs a ruling |

| heygen-com/hyperframes (added same day, Idi's 5th link) | HTML-to-MP4 renderer for agents: Puppeteer seek-and-capture, FFmpeg | 2026-03-10, 78,586 stars, v0.9.10, HeyGen-backed, telemetry on by default | Apache-2.0 | borrow 5 render-reliability methods (B below); capture path poor for our 4K on Windows |

Pattern: the first four are under 3 weeks old and agent-built; star counts track the showcase more than tested use (inference, medium).

## A. Release gates (cheap, gap confirmed)

1. Final-MP4 audio gate: integrated LUFS, true peak, clipped samples, measured after AAC. Targets -14 LUFS +-1, TP <= -1 dBTP. 3 of 4 repos ship it (video-director `qa_video.py analyse_audio`, kinetograph `audio analyze`, earshot master gate). Ours: LUFS + LRA on song takes only (`pa_screen.py`), no true peak, no final-file check. -14 = YouTube playback convention (turns loud uploads down, never quiet ones up), no measured optimum. Effort: one ffmpeg `ebur128=peak=true` call.
2. Post-mux sync check: pull audio from the final MP4, refit the beat grid, compare with cut times; <=1.5 frames ideal, >3 fix; uniform offset = AAC priming, fix with one constant (video-director `sound.md` s12). Ours: 483/483 word sync measured before encode.
3. Chance baseline beside every sync rate: what random times would score (earshot `timeline.py _chance`; their dense refs scored 67-80 % vs chance 46-71 %). Ours: "hits on beat 61 %" printed bare in `avsync.py`, `verify_reel.py`.
4. Single-frame flash detector: frame differs from both neighbours by > max(2, 4x median step) while neighbours match (video-director `qa_video.py frame_stats`). Catches red failed-scene frames, half-shutter doubles, splice frames in repaired renders. Ours: `flips.ts` catches only >=60/255 brightness jumps.
5. `render.json` per render (scale, samples, shutter, tol, ANGLE renderer string, commit, fps); comparisons refuse on mismatch (reanimate `compare.ts`). Catches the silent SwiftShader fallback (receipt: `kit-engine-components.md:224`).

## B. Render reliability

6. Segmented 4K render: ~600-frame segments + manifest, browser restart per segment, or requeue only the failed worker's chunk. Neither repo implements it (kinetograph scout's spark, video-director's one line "retry failed chunks"). Fixes: any failure kills the whole render (`render.ts:173-184`); KC 4K died at frame 11,580/11,646 after 8 h 26 min (`kit-engine-components.md:214`). Effort medium; context-loss cause still unproven.
7. Frame reuse on declared holds: reuse the last buffer where `_kc-rhythm.ts` declares a hold; key on the declaration, since adaptive sampling is not bit-repeatable (kinetograph `reuse.rs`). Saves render hours; held-frame share in KC unknown.
6b. hyperframes turns item 6 into working code (`repo-scout-2026-11-04/hyperframes.md`): 3,000-frame segments with a hashed manifest and resume (reuse only when hash, bytes and probed frame count all match); browser restart every 3 segments ("keeps a session under the 10k-frame band", verified verbatim; KC died at 11,580 in one session); failure classes, retry only browser-loss errors; retry only missing frames; release WebGL contexts when a clip ends (our context-loss prior = GPU memory pressure). Their segment mode is still opt-in pending a soak test.
6c. Cut-continuity gate (hyperframes seam gate): per cut, the carrying object stays within 12 px / 5 % size across the cut, exits still moving, entry speed near exit speed; rects from `window.__kc.boxes`. No other repo covers cuts.
8. Determinism guard: `Math.random`, `Date.now`, `performance.now` throw in render mode with the scene id; plus `tsc --noEmit` in the pre-render gate (kinetograph: "a misspelled prop draws at full opacity without an error"). Known debt: `check.ts:178` strict-null error (`kc-public-export-2026-11-02.md:79`).

## C. Motion and picture QA

9. Onion skin: one image blending a frame range = the motion path of a camera move or word entrance (kinetograph `onion`). For camera audits and blind panels scoring motion from one still. ffmpeg `tmix` or numpy.
10. Easing fit on the refs' camera tracks: 25 named easings, RMSE rank, overshoot >2 % = spring (reanimate `easing.ts`, Python port ~60 lines). Puts numbers on the camera parity gap: KC 2.2 % of time in 3 s+ moves vs R1 20.5 %.
11. Blurred + sharp mismatch in `pixeq.py`: separates grain moved from layout moved (reanimate `compare.ts`, `--blur 4`).
12. Golden stills per REUSE module, tolerance 3-4 levels (our GPU noise 2-3/255): video 2 edits cannot silently break KC-proven modules (kinetograph `snapshot`).
13. Phone-size sheet (360 px, 1 fps) + first-3-s sheet (every 0.5 s); our clarity gate measures only 4K (video-director `qa_video.py sheet`).

## D. Process

14. Animatic gate: timed boxes + lyric words on the click reel, reviewed before any style frame (kinetograph skill: "never animate against an unapproved storyboard"). Mirrors KC Gate 2 locking the look from 9 stills. Pay Attention reaches this step next.
15. Fix card: DIAGNOSIS / SCOPE / KEEP / FAILURE NOW / TARGET / PROOF; worst 3 per take; pixel-diff every frame outside SCOPE; replace a version only after a side-by-side win (video-director `briefs.md` s9, `quality.md`). Guards against the v4-v6 pile-up (one pass from 200-250 findings).
16. Critic upgrades: restate the video's message in one sentence from frames alone (video-director); per round CHANGED and FIXED lists, `weakest_3s`, every taste claim carries a measurement, fixes tested on a variant with before/after numbers (earshot `critic_*.md`).
17. Line-card validator: every term sung (`lyrics.json`) and shown (`inventory.ts` log); error if neither, warning if one (video-director `check_timeline.py`).
18. AI-tells checklist per card, 3 already hit KC: signs repeat the picture ("June" up to 7x), camera pumping on every beat (`_kc-rhythm` pulse default), generic crossfades (engine default) (video-director `quality.md`).
19. Validate the dynmap thresholds (LRA >= 7, valleys >= 8 %, escalation >= +1.5 dB): leave-one-out over the 9 bar songs (baseline 1 - 2/9 = 78 %) + damage mixes with flags written before the run, KC v8B as flat control (earshot `eval/launch/RESULTS.md`: 13/14 caught).

## E. Public repo (Pay Attention)

20. README receipts table (each claim with its measured number), LIMITS page with numbers, "thresholds tuned on the data they report" caveat block, THIRD-PARTY-NOTICES, failure ledger (all 4 repos; earshot and video-director strongest). Fits R13 visual README.
21. Kit as a Claude skill: short SKILL.md + per-stage `references/` loaded when needed + `scripts/`. All three skill repos use this shape. Our kit reads 1,196 lines up front; a skill makes the public repo installable.

## F. Rulings for Idi (WHAT)

22. SFX layer: earshot renders 252 sounds from code, no models; kc-engine already knows every pop and slam frame. Against: earshot's own docs say synthesized SFX sound amateur next to real recordings (their score 0.33 vs 0.94); a layer on the "no audio edits" song is new ground. Rec: a 20 s A/B on one KC chorus, his ear decides.
23. Scout round 2: 8 repos listed in video-director `references/sources.md`; most promising `Vincentwei1021/video-shotcraft` (music-led cut fitting) and `yihui-dev/awesome-opus5-5-videos` (real iteration data).

## Rejected

- Installing any of the 4 (each duplicates or trails kc-engine).
- kinetograph engine swap (no three.js, no readPixels, untested Windows GPU, PolyForm terms on copied code).
- earshot `llm` extra (Gemini per-token API key).
- Virtual clocks (reanimate, kinetograph): kc-engine is already a pure function of t.
- CLAP tagging for take triage (their own limits: tags right ~25-50 % in busy mixes).

## Gaps none of the 4 cover

- Whisper mishearing sung words ("without one" heard "with that one" in 10/12 takes).
- Lyric-to-picture design (line cards stay ours).
- Root cause of WebGL context loss.

## Unverified

- ITU-R BT.1359 / EBU R37 sync tolerances quoted by earshot (+45/-125 ms, +40/-60 ms): check before citing publicly.
- All repo line numbers (WebFetch condenses files).
