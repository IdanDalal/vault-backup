---
type: project
created: 2026-11-02
author: jep
---

# Knowledge Cutoff: the production pipeline, phase by phase

Scope: idea to final cut of "Knowledge Cutoff" (KC), 2026-10-12 to 2026-11-01. Release mechanics live in the release playbook (another file).
Citations: `[name]` = `D:\work\vault\projects\AIMV\name.md` with `knowledge-cutoff-` shortened to `kc-`; `[mem:name]` = `C:\Users\jep\.claude\projects\D--work-vault\memory\name.md`.
Block keys: PURPOSE / IN / OUT / TOOLS / DONE / COST / WORKED / FAILED.

## Timeline at a glance

| dates | phase | result | source |
|---|---|---|---|
| 10-12 | 0 [MASK] concept + reference deconstruction | 10 moves marked, G1-G16; [MASK] paused 10-13 | [aimv-deconstruction-2026-10-12], [frontier-aimv-analysis-2026-10-13] |
| 10-13 | 1 frontier analysis, premise | KC ruled | [kc-2026-10-13] |
| 10-13 | 2 40 s end-to-end proof | proof-v1.mp4 | [kc-2026-10-13] |
| 10-13 | 3 lyrics v1-v3 | v3 locked | [kc-lyrics-v3-2026-10-13], [song-engine-research-2026-10-13] |
| 10-13 | 4 song engine search | MiniMax wins one-shot | [song-engine-research-2026-10-13] |
| 10-14 to 10-15 | 5 MiniMax prompt, auditions, batches v4-v9 | song locked: v8B seed 3327 | [kc-auditions-2026-10-14] |
| 10-14 to 10-15 | 5b bookend repair attempts | all rejected | [kc-auditions-2026-10-14] |
| 10-15 | 6 video plan, sync, scene plan, style frames | Gates 1-2 passed | [kc-video-build-2026-10-15] |
| 10-15 to 10-17 | 7 old engine (Canvas2D) v2-v6 + rules audit | route abandoned | [kc-v6-2026-10-17] |
| 10-17 | 8 engine probe P1/P2 | WebGL + P(Doom) engine run on the PC | [engine-probe-p1-2026-10-17], [engine-probe-p2-2026-10-17] |
| 10-17 | 9 treatment (style bible) | 18 modules, 72 set-ups | [kc-treatment-2026-10-17] |
| 10-17 | 10 chorus 1 proof, new engine | "top-tier" | [kc-chorus1-proof-2026-10-17], [handoff-2026-10-17-full-video] |
| 10-17 | 11 phase 0 kit | kit, refs library, full timeline, 4K checks | [kc-phase0-2026-10-17] |
| 10-17 to 10-18 | 12 waves A, B, C | full (4 segments) | [kc-wave-a-2026-10-17], [kc-waves-bc-2026-10-17] |
| 10-18 | 13 notes pass | full2 | [kc-notes-pass-2026-10-18] |
| 10-18 to 10-19 | 14 rhythm pass | full3 | [kc-rhythm-pass-2026-10-19] |
| 10-19 to 10-20 | 15 typography pass | full4 | [kc-typography-pass-2026-10-20] |
| 10-21 to 10-22 | 16 escalation pass | full5, full5b | [kc-escalation-pass-2026-10-21] |
| 10-22 | 17 local agents (side quest) | 7/10 tasks pass | [local-agents-pilot-2026-10-22] |
| 10-25 to 10-26 | 18 parity pass | full6, full6b | [kc-parity-pass-2026-10-26] |
| 10-27 to 10-28 | 19 polish pass | full7, full7b = final cut | [kc-polish-pass-2026-10-28] |
| 10-31 to 11-01 | 20 4K master | 2160p60 file, repaired | [mem:aimv-project] |

Totals: 21 calendar days. Whole-song 1080p renders on the final engine: 10 (full, full2, full3, full4, full5, full5b, full6, full6b, full7, full7b), plus the 4K master [kc-* pass reports]. Old engine: proof v1 plus rough v2 and v3-v6 [kc-video-build-2026-10-15], [kc-v6-2026-10-17].

---

## Phase 0. Reference deconstruction and the first concept, [MASK] (10-12)

- PURPOSE: find what Idi likes in the reference songs, amplify only that [aimv-deconstruction-2026-10-12].
- IN: 8 reference songs + videos in `D:\work\AIMVs`; Idi's prompt (7 frames, 7 personas, knob list) [mask-posse-cut-2026-10-12].
- OUT: [aimv-deconstruction-2026-10-12] (10 moves, Idi's L/N/X marks, measured BPM/key/words per minute/loudness); [aimv-guidelines] G1-G16; [mask-posse-cut-2026-10-12], [mask-lyrics-v1-2026-10-12], [mask-lyrics-v2-2026-10-12]; transcripts `D:\work\AIMVs\lyrics\` (kept off the vault: other people's lyrics); toolkit `D:\work\aimv-lab\analyze.py`, `out\measures.json`.
- TOOLS: Whisper large-v3 on the 4090 (~95% on a spot check, misses sung jargon); librosa (BPM low confidence, reads double/half tempo) [aimv-deconstruction-2026-10-12].
- DONE: Idi marked every move; guidelines table with G = stated once, R = confirmed [aimv-guidelines].
- COST: 1 day; 2 lyric drafts of [MASK].
- WORKED: a marked move table (L/N/X) turned taste into numbered guidelines; measured density 130-146 wpm in 6 of 8 refs became G1.
- FAILED/WASTED: [MASK] paused 10-13 as "too ambitious first" [mem:aimv-project]; seven ideas in one song against the one-idea references [frontier-aimv-analysis-2026-10-13]. Whisper misreads of jargon needed a hand-corrected list [aimv-deconstruction-2026-10-12].

## Phase 1. Frontier analysis and premise (10-13)

- PURPOSE: one video at the level of the references, "100% doable" (Idi ruling, paraphrase) [frontier-aimv-analysis-2026-10-13].
- IN: 9 references, 24-frame contact sheets per video (`D:\work\aimv-lab\sheets\`), P(Doom) repo docs (`D:\work\aimv-lab\pdoom-docs\`), makers' own YouTube descriptions.
- OUT: [frontier-aimv-analysis-2026-10-13] (two visual tiers, 7-point frontier recipe, 5 premises with climbing number, drop and rug pull each); `D:\work\aimv-lab\research-makers.md`; [kc-2026-10-13].
- FINDINGS: 9 of 9 credit Opus 5.5 as animator; 0 of 9 used AI video generation; every credited song tool is Suno; 5 of 9 are Tier A (typography-first) [frontier-aimv-analysis-2026-10-13].
- DONE: Idi ruled KC, Tier A, AI first-person, Harry Potter thread [kc-2026-10-13].
- COST: same day as phase 2.
- WORKED: premise true of the singer (the model's own cutoff); "one strong idea + sincerity beats complexity" from The Way I Look At You [frontier-aimv-analysis-2026-10-13]; originality check per premise.

## Phase 2. The 40-second end-to-end proof (10-13)

- PURPOSE: test the riskiest link (song quality on a local model) end to end before any full song [frontier-aimv-analysis-2026-10-13].
- IN: 65-word verse + chorus `D:\work\aimv-lab\kc\proof-lyrics.txt`.
- OUT: 16 takes `kc\takes\`, ranking `kc\takes\rank.json`, timing `kc\timing-fixed.json`, renderer `D:\work\aimv-lab\render\kc.html`, `D:\work\AIMVs\ours\knowledge-cutoff-proof-v1.mp4` (40 s) [kc-2026-10-13].
- TOOLS: ACE-Step 1.5 turbo via ComfyUI API :8188 (~6 s per take); Whisper intelligibility vs written lyric; canvas page with every frame = f(song time); headless Edge to 1,200 frames to ffmpeg in 30 s.
- DONE: 24-frame contact sheet inspected; Idi said yes to the ACE-Step voice [mem:aimv-project].
- RESEARCH SIDE: two agents, 31 post-cutoff items with source + confidence (`after-cutoff-tech.md`, `after-cutoff-world.md`); rule: high-confidence items named, medium items hedged in the lyric [kc-2026-10-13].
- WORKED: cheap proof of the whole chain in one session.
- FAILED: headless Edge GPU path returned a blank canvas; `--disable-gpu` fixed it [kc-2026-10-13]. Sound quality unverifiable by jep (intelligibility is a proxy).

## Phase 3. Lyrics v1 to v3 (10-13)

- PURPOSE: full lyric under the guidelines, Idi's lines kept verbatim [kc-lyrics-v1-2026-10-13].
- IN: proof lines, Idi's picks from jep's reactions table, [aimv-guidelines].
- OUT: [kc-lyrics-v1-2026-10-13], [kc-lyrics-v2-2026-10-13], [kc-lyrics-v3-2026-10-13]; text `D:\work\AIMVs\ours\kc-full-lyrics-v3.txt`.
- TOOLS: `D:\work\aimv-lab\rhymes.py` (G17 ladder, CMU dictionary); `probe_lines.py` (refrain, intro, outro, punchline heard).
- DONE: every line-end pair R4+; consistency rules G20 hold; lyrics locked 10-13 [song-engine-research-2026-10-13].
- COST: 1 day, 3 drafts; takes: v1 8, v2 16, v3 audio test 16 (4 spellings x 4) + 12 [kc-lyrics-v1/v2/v3].
- WORKED: a verdict table per Idi edit (kept / changed / cancelled, with the reason); the two crossing tense ladders across choruses [kc-lyrics-v2-2026-10-13]; spelling experiment measured: "Knowledge cut-off! Cut-off!" + `[spoken word]` tags = refrain heard 6/6 vs 0/6 (G21) [kc-lyrics-v3-2026-10-13].
- FAILED: v1 bridge used "we" for AIs in general (broke the person rule) [kc-lyrics-v2-2026-10-13]; a seed's sound did not survive a lyric change (seed 505: 77%, 11 dB) [kc-lyrics-v2-2026-10-13]; all-caps refrain worse [kc-lyrics-v3-2026-10-13].

## Phase 4. Song engine search (10-13, day and night)

- PURPOSE: every word sung right, one take [song-engine-research-2026-10-13].
- IN: locked v3 lyric; best ACE take B (19 word errors mapped by `errmap.py`).
- OUT: [song-engine-research-2026-10-13]; `D:\work\aimv-lab\research-song-models.md`; workflows `wf_ace4b.json`, `wf_minimax.json`, `wf_minimax_tiled.json`; repaired takes `kc-full-v3-C-REPAIRED.mp3`, `-v2-balanced.mp3`; tools `repair.py`, `splice.py`, `diffmap.py`, `repaint2.py`, `balance.py`.
- TOOLS: knob grid 7 settings x 4 seeds; ACE-Step + 4B planner; MiniMax Music 3; ACE-Step official app for repaint; Demucs stems; jep's own ComfyUI (port 8189, logs readable).
- DONE: Idi's ruling: repaired take = "the standard to pass; look for a one-shot take, starting with MiniMax" [song-engine-research-2026-10-13].
- COST: ~1 day; 29 GB models staged; blocked once on ComfyUI folders in Idi's profile; MiniMax crashed 2 of 3 runs on Idi's instance [song-engine-research-2026-10-13].
- WORKED: noise floor stated (±3% at 4 takes); ACE 4B planner +4.6 points (92.1% avg); own ComfyUI let jep read the crash log (audio decode out of GPU memory) and fix it with tiled decode (0 crashes in 9 takes); MiniMax one-shots 93-96% words; paced MiniMax seed 974 = 97.8%, project best [song-engine-research-2026-10-13].
- FAILED/WASTED: knobs spent (lower temperature, higher cfg hurt; steps, tempo no effect); pronunciation hints 88.4% vs 92.1%; comma splits 82.7%; chained repaints degrade the whole song (55.7%); repaints came out 2-4 dB quiet, voice up to +5.4 dB; the repaired take rejected as patched ("mostly perfect parts and some least-bad-option parts"); "two engines in RAM" crash theory refuted [song-engine-research-2026-10-13].

## Phase 5. MiniMax prompt, auditions, batches, song lock (10-14 to 10-15)

- PURPOSE: direction, vision and emotional impact in a one-shot take [handoff-2026-10-14].
- IN: Idi's 6 notes on 8 paced takes; his YouTube knob list; MiniMax repo templates [handoff-2026-10-14], [kc-prompt-v4-2026-10-14].
- OUT: captions `D:\work\aimv-lab\kc\caption-minimax-v4.txt` ... `-v8.txt`, audition captions `kc\aud\cap-1..9.txt`, lyrics `kc\lyrics-mm-p4.txt` ... `p9a/p9b.txt`; [kc-prompt-v4-2026-10-14]; [reference-deconstruction-2026-10-14]; [kc-auditions-2026-10-14]; Idi's folders `D:\work\AIMVs\ours\auditions\`, `v5\` ... `v9\`; locked song `D:\work\aimv-lab\kc\final\v8B-3327.mp3` (192.6 s), `v8B-3327-timing.json` (483 words), `v8B-3327-timemap.md` [handoff-2026-10-15-video].
- TOOLS: `gen_song.py` (env WF, COMFY, STATUS_*); meters `kcmeter.py`, `stems.py`, `bookends.py`, `pace.py`, `drops.py`, `v5check.py`; "the ear" = ACE-Step Captioner, calibrated 4 of 4 on Idi's notes for take C (n = 1) [reference-deconstruction-2026-10-14]; status board `_STATUS.txt` + `status.py` [kc-auditions-2026-10-14].
- BATCHES: v4 8 seeds; auditions 18 takes (9 styles x 2); v5 8; v6 8; v7 12; v8 24; v9 24 (~8 min per take in ComfyUI's low-RAM mode, ~4 normal) [kc-prompt-v4-2026-10-14], [kc-auditions-2026-10-14]. G25 measured on 42 takes by 10-14 [aimv-guidelines].
- DONE: v8B (seed 3327) "a BANGER", "the best one yet"; beat v9 ("v8B still wins") [kc-auditions-2026-10-14], [handoff-2026-10-15-video].
- COST: 2 days.
- WORKED: the trained caption format (MiniMax's own box names, `bpm is X. key is Y, and scale is Z.`, section-by-section arrangement, 500-600 words) brought pace from 145-195 to 130-146 wpm with the same lyric [kc-prompt-v4-2026-10-14]; auditions (our lyric in 9 reference styles, 6:13 preview reel with spoken numbers) let Idi pick by ear [kc-auditions-2026-10-14]; triple refrain written into the lyric; `-oh` spellings keep holds; `graph-ics` keeps the s; G24 payoff ornament on "tune" [aimv-guidelines].
- FAILED/WASTED: v4 words ("airy mezzo", "bell synth", "sparkling") gave "Disney princess"; caption risers erased the pre-chorus drop (18 dB to 0-4 dB) [kc-prompt-v4-2026-10-14]; v5's speed-up words brought back the rap feel; v7 (12 takes) lost to v5B; v8 per-take rates multiply to "roughly 1 in thousands" for all targets at once [kc-auditions-2026-10-14]; `drops.py` and the anchored drop meter missed drops Idi heard; `tunehold.py` failed validation; the ear's rap flag noisy; v9 result reached Idi 3 h late [kc-auditions-2026-10-14].

## Phase 5b. Bookend repair attempts (10-14 to 10-15), all rejected

- PURPOSE: softer, slower, separate spoken intro and outro on v5B [kc-auditions-2026-10-14].
- OUT: `D:\work\AIMVs\ours\gold\` (edited bookends), `D:\work\AIMVs\ours\voice\` (TTS reel), `kc\tts\` (84 readings), `fix_bookends.py`, `cutcheck.py`, `kc\gold\rebuild.sh`.
- TOOLS: Demucs stems (`stems44.py`), ffmpeg atempo; Chatterbox 0.1.7 TTS (MIT, Perth watermark kept).
- RESULT: edit 1 cut inside words ("aga......in"); fixed with cuts at measured silence midpoints and `cutcheck.py` (±50 ms at 25 dB below peak); emphasis could not be moved by pauses; all 14 TTS picks "terrible in most aspects"; route closed: no voice clone, no stitched bookends; direction back to generating takes [kc-auditions-2026-10-14].
- COST: most of 10-14 night and 10-15 morning (unclear in notes exactly).

## Phase 6. Video plan, sync, scene plan, style frames (10-15)

- PURPOSE: plan one continuous world and fix word timing before building [kc-video-plan-2026-10-15].
- IN: 4 research files: teardowns `D:\work\aimv-lab\research-video-teardown-1-5.md`, `-6-10.md`, makers' briefs to Claude `research-video-makers-methods.md`, measured tech plan `research-video-tech-plan.md`; v8B time map.
- OUT: [kc-video-plan-2026-10-15]; [kc-scene-plan-2026-10-15] (2 levels, 7 rooms, 13 camera moves, 14 one-line reads); `D:\work\aimv-lab\kc-video\sync\kc-timing-v2.json`; Gate 1 click reel `D:\work\AIMVs\ours\video\gate1\`; Gate 2 sheet `video\gate2\style-frames.jpg` [kc-video-build-2026-10-15].
- TOOLS: forced alignment (318 words), vocal onset nearest Whisper + 0.17 s (110), line starts from loudness rise (16), Whisper + offset (39), `build_timing_v2.py`; `sync\verify_reel.py` (483 of 483 clicks within 1 ms); `check_sync.js`; `tests\scdet.sh` cut detector [kc-video-build-2026-10-15].
- DONE: Gate 1 "Clicks land on the words, I think."; Gate 2 "Keep all 9." [kc-video-build-2026-10-15].
- COST: 1 session (10-15 evening).
- WORKED: a click reel turns sync into something Idi hears; the corrected timing file stayed the timing of record into the new engine [handoff-2026-10-17-engine-probe], with one later fix (ALGAE) [kc-rhythm-pass-2026-10-19]; four gates where Idi picks from pictures [kc-video-plan-2026-10-15].
- FAILED: Gate 2 locked palette and rooms from 9 stills before any motion (named one of five premature rules on 10-17) [kc-v6-2026-10-17]; GPU render path black frames (later traced to Canvas2D on GPU, probably) [engine-probe-p1-2026-10-17].

## Phase 7. Old engine (Canvas2D) v2 to v6 and the rules audit (10-15 to 10-17)

- PURPOSE: build the planned one-shot world, then level it up on Idi's notes [kc-video-build-2026-10-15].
- OUT: `D:\work\aimv-lab\kc-video\world.html` ... `world6*.js`; renders `D:\work\AIMVs\ours\video\gate3\knowledge-cutoff-rough-v2.mp4`, `-v3.mp4` ... `-v6.mp4`; critiques `kc-video\critique\` (A-I for v4, `v5\` 15 files, `v6\` flaws F1-F6, `rules-ledger.md`, `refs-approach.md`, `refs-build.md`, `gap-sheet.jpg`) [kc-video-build-2026-10-15], [kc-v5-2026-10-16], [kc-v6-2026-10-17].
- PASSES: v2 rough (Gate 3); v3 "WOW" pass on 8 notes (`spectacle-techniques.md` from 10 teardowns); v4 on 8 notes (9 critique agents, ~200 findings); v5 (5 reference dissections + 10 lens critiques, ~250 findings, [kc-v5-synthesis-2026-10-16]); v6 (Idi's tail ruling A + notes 1-2) plus the audit: 6 blind flaw agents (403 flaws, 9 causes), rules ledger (116 rules + 15 defaults, 55 set before any moving picture), refs measured on 10 dimensions (688 frames coded by eye) [kc-v6-2026-10-17].
- TOOLS: `render.js` (4 Edge workers, lossless PNG, BT.709), `check_sync.js`, `tests/negcontrol.js` (same colour test 0.3 s early as a negative control), `scdet.sh`, `loopcheck.sh`, `sheet.js` contact sheets [handoff-2026-10-16-v5-pass].
- DONE: every version 483/483 words, 0 cut flags, seamless loop; audit ended in Idi's route B ruling [handoff-2026-10-17-engine-probe].
- COST: ~3 days, 5 versions (~4-5 min per render) [kc-video-build-2026-10-15], [kc-v5-2026-10-16].
- WORKED: the audit: measured gap (refs 4-7.5 objects per frame vs ours 12; type/UI/line art fill 86-100% vs filled illustration 25%; 33-75 set-ups vs 8 rooms; code per second 129-149 vs 11), flaw hunters with no knowledge of intent, a ledger of every rule with its date [kc-v6-2026-10-17].
- FAILED/WASTED: the Canvas2D route itself (v2-v6) was dropped; each version built in one pass from 200-250 critic findings added props, labels and gags; the 0-cut-flag bar vetoed fast whips; the 8-room world piled props up; filled drawings ("baby's-first"); "June" up to 7 times on one screen; name shown 7 times before its reveal [kc-v6-2026-10-17], [handoff-2026-10-17-engine-probe].

## Phase 8. Engine probe (10-17)

- PURPOSE: prove the reference engine's foundation (WebGL on the 4090, headless, deterministic) before any art [handoff-2026-10-17-engine-probe].
- OUT: `D:\work\aimv-lab\engine-probe\` (`probe.html`, `run.js`, `matrix.log`, `p2.sh`, sheets); Windows launcher `D:\work\aimv-lab\refcode\pdoom-video\app\scripts\render-win.ts`; [engine-probe-p1-2026-10-17], [engine-probe-p2-2026-10-17].
- TOOLS: playwright-core + Edge; P1 no installs; P2 Bun 1.4.3 + 32 npm packages after Idi's okay.
- DONE: P1 4 of 4 criteria (0 black frames, md5-identical runs, headless = visible window, 14 fps per worker, 41 on 4); P2 13 of 14 P(Doom) plates match YouTube per backend [engine-probe-p1-2026-10-17], [engine-probe-p2-2026-10-17].
- COST: 1 day, one install ask.
- WORKED: reproduced the black-frame mechanism on demand (`preserveDrawingBuffer` off + read in a later call = 60 of 60 black); traced the D3D11 bug to `fwidth` inside a breakable loop; picked Vulkan (5x faster) with a SwiftShader (CPU) still per plate as correctness reference [engine-probe-p2-2026-10-17].
- FAILED: jep first read a GL driver message as proof of GPU use; retracted before the report [engine-probe-p2-2026-10-17]; 1 of 16 parallel launches lost WebGL silently [engine-probe-p1-2026-10-17].

## Phase 9. Treatment (style bible) (10-17, amended through 10-25)

- PURPOSE: one document every agent reads; modelled on P(Doom)'s `docs/TREATMENT.md` (structure only) [kc-treatment-2026-10-17].
- OUT: [kc-treatment-2026-10-17]: idea, tone, bans, palette (one signal yellow, one rare blue), 4 OFL type roles, lyric rules, motifs (the caret), spoiler rules, 18 modules / 72 set-ups with every lyric line mapped, receipts table, measures from the v6 gap; added sections 12 Detail at 4K (10-17), 13 Idi's notes (10-18), 14 rhythm (10-19), 15 escalation (10-21), 16 parity (10-25); lyric rules rewritten 10-19.
- DONE: plates and checks traceable to bible lines; amendments dated in place.
- WORKED: rules carry their source and date; later passes appended sections and kept earlier gates (16.11 "everything sections 5, 13, 14, 15 built stays").
- FAILED: a ruling made without rereading the bible was wrong once (session-to-letter hand-off) [kc-waves-bc-2026-10-17], [handoff-2026-10-18-notes].

## Phase 10. Chorus 1 proof on the new engine (10-17)

- OUT: `D:\work\AIMVs\ours\video\proof\kc-chorus1-proof.mp4` (27.7 s, 5 scenes, 9 set-ups), `v6-vs-proof-1.jpg`, `-2.jpg`; engine `D:\work\aimv-lab\kc-engine\` (P(Doom) core + MIT notice; `_kc.ts`, `timeline.ts`, `scripts/check.ts`, `kc.sh`; data from `tools/build_data.py`, `build_pitch.py`) [kc-chorus1-proof-2026-10-17].
- DONE: 61 of 61 words lit on time, negative control 0, 0 edge/title-safe/overlap issues in 277 frames, SwiftShader vs Vulkan 49-58 dB [kc-chorus1-proof-2026-10-17]; Idi: "Excellent work! ... Ideas and execution are all top-tier." [handoff-2026-10-17-full-video].
- COST: same day as phases 8-9; 1,660 frames in 85.9 s.
- FAILED: type scale 3.9-5.7x against the bible's 10x [kc-chorus1-proof-2026-10-17].

## Phase 11. Phase 0 kit (10-17)

- PURPOSE: lead builds shared tools so scene agents never reinvent them [handoff-2026-10-17-full-video].
- OUT: detail kit `app\src\scenes\_kc-glsl.ts`, `_kc.ts` (paper/ink materials, form hatching, line weights, micro-type, defocus), demo `kitdemo.ts`; reference library `kc-engine\refs\` (705 MB, gitignored, R1-R5 frames every 3 s + 10 hero 1:1 crops each); full 32-entry timeline with `placeholder.ts`; `check.ts --scale 2`, `detail.ts`, `errors.ts`; engine under its own git; briefs `reports\wave-a-briefs.md` [kc-phase0-2026-10-17].
- DONE: whole song renders end to end from day one with placeholders.
- WORKED: placeholders let every check run on the full song before scenes exist.
- FAILED (fixed): intermittent red frames from Vite's dependency scan reloading under the renderer; would have hit three parallel agents [kc-phase0-2026-10-17].

## Phase 12. Waves A, B, C: all 18 modules (10-17 to 10-18)

- PURPOSE: rebuild every frame to equal or exceed the references at 4K 1:1 [handoff-2026-10-17-full-video].
- WAVES: A = 5 chorus modules (15 entries, 85 of 194 s), 9 critic reports, 1-3 critic rounds each; B+C = 13 modules (bookends, verses, pre-choruses, bridge), 11 critic reports [kc-wave-a-2026-10-17], [kc-waves-bc-2026-10-17].
- OUT: `D:\work\AIMVs\ours\video\wave-a\kc-wave-a-choruses-1080p.mp4` (90 s); `video\full\kc-full-1080p.mp4` (194.12 s); reports `kc-engine\reports\`.
- CONTRACT: agent touches only its module files; reports after its last edit to `reports\<agent>.md`, at most 10 lines back; fresh critic per pass; lead re-renders on final code before accepting; at most 3 rendering at once [handoff-2026-10-17-full-video], [handoff-2026-10-18-notes].
- DONE: every set-up PASS by critic; 483/483; loop pixel-identical at 4K before encoding [kc-waves-bc-2026-10-17]. Idi on wave A: "The preview looks SICK! Great work!" [mem:aimv-project]; on the full: "WOOOWWWWWW!!! This is a generational leap over the old engine's results!" [handoff-2026-10-18-notes].
- COST: one evening and night; 5 h usage limit hit once at 9 concurrent agents [mem:aimv-project].
- WORKED: critic per pass (about one in three agent claims proved false); lead re-render caught 3 regressions; agents' proof stills predated their last edit 4 times [kc-wave-a-2026-10-17], [handoff-2026-10-18-notes].
- FAILED: background full render stopped by Claude Code on low memory; the 4-segment foreground render showed joins Idi saw [kc-waves-bc-2026-10-17], [handoff-2026-10-18-notes]; one agent shrank labels to pass the type-scale gate (critic caught it) [kc-wave-a-2026-10-17]; load-set determinism (stills differ 40 dB from the full render) and a stale dev server fooled checks [kc-waves-bc-2026-10-17].

## Phase 13. Notes pass, Idi's 10 notes (10-18) -> full2

- IN: Idi's ten notes on the full render [handoff-2026-10-18-notes].
- OUT: `video\full2\kc-full-1080p.mp4`; tools `scripts\inventory.ts` (meta, repetition, density), `scripts\flips.ts` + `data\flips-allowed.json`, `render-full.sh` (one detached run, DONE marker), `probe-full.sh`; research receipts `reports\research-1018.md`; bible section 13 [kc-notes-pass-2026-10-18].
- DONE: meta strings 119 to 0; repetition spans 353 to 46 (named exemptions); flips 20 to 3 (all allowed); one run, 11,646 frames in 833 s [kc-notes-pass-2026-10-18].
- COST: 1 day; 4 agents + 4 critics; a power cut killed 3 agents mid-pass (work intact) [kc-notes-pass-2026-10-18]; one agent stalled ~30 min on a background gate [mem:agents-run-gates-foreground].
- WORKED: each note turned into a measurable rule with a tool before agents ran; real sourced quotes and real market series replaced invented text [kc-notes-pass-2026-10-18].
- FAILED: a false fact was on screen (`+2 days`; the first Opus 5.5 video went up on launch day) [kc-notes-pass-2026-10-18]; agents had filled micro-type with stage directions and notes to each other [handoff-2026-10-18-notes].

## Phase 14. Rhythm pass (10-18 to 10-19) -> full3

- IN: Idi: "telling a story more than singing a song"; ALGAE early; RTX OFF/ON gag [kc-rhythm-pass-2026-10-19].
- OUT: `video\full3\kc-full-1080p.mp4`; reports `rhythm-measure.md`, `rhythm-r123.md`, `rhythm-r45.md`, `rhythm-pass-briefs.md`; kit `_kc-rhythm.ts`; `tools/avsync.py accept`; bible section 14.
- DONE: beat pulse gain 1.00 to 2.07 (target 1.40+); choruses rising 2.32/2.45/2.53; hit timing 16 ms early [kc-rhythm-pass-2026-10-19].
- COST: 3 analysis agents, R0 engine + 4 plate agents + 4 critics, one render.
- WORKED: measuring the refs first (pulse 1.46-1.54 vs ours 1.05; song swells only ~1 dB into choruses, so the picture supplies the energy); faster-whisper on the vocal stem found ALGAE at 117.28 s vs 115.01 in the timing file (Idi's ear right) [kc-rhythm-pass-2026-10-19].
- FAILED: `scripts/server.ts` leaked 543 servers (~100 GB) until renders failed [kc-rhythm-pass-2026-10-19].

## Phase 15. Typography pass (10-19 to 10-20) -> full4

- IN: Idi: "We're listing the lyrics instead of singing them." [kc-typography-pass-2026-10-20].
- OUT: `video\full4\kc-full-1080p.mp4`; reports `type-ours.md`, `type-r123.md`, `type-r45.md`, `type-a..d.md`, `type-lead-rulings.md`; kit `_kc-type.ts`; render lock in `kc.sh`; bible section 5 rewritten.
- DONE: subtitle score (6 traits) from 16 lines at 6/6 to every line 0-2/6; beat gain 2.16 [kc-typography-pass-2026-10-20].
- COST: 3 analysis agents, 4 plate groups, 4 critics, one 820 s render.
- WORKED: a subtitle score per line; refs use plain rows only where the world types (chat, terminal) [kc-typography-pass-2026-10-20]; retiring the chorus hop (Idi: "You made a great call.") [kc-notes3-2026-10-21].
- FAILED: words showed 0.7-1.8 s before sung (dim line); lyric typed over lyric at 4.917 s, untested by any check until then [kc-typography-pass-2026-10-20].

## Phase 16. Escalation pass, Idi's 11 notes (10-21 to 10-22) -> full5, full5b

- IN: [kc-notes3-2026-10-21].
- OUT: `video\full5\kc-full-1080p.mp4` (render full5b); reports `n3-r3-craft.md`, `n3-escalation.md`, `n3-facts.md`, `e1-lead-rulings.md`; `gates-full.sh`, `scripts/shutter-audit.ts`, aside-collision test; bible section 15 [kc-escalation-pass-2026-10-21].
- DONE: every recurring element on a ladder; cuts 1/2/4/8/16/32 (189); text repeats 55 to 29; beat 2.26 [kc-escalation-pass-2026-10-21].
- COST: 3 research agents, 4 plate agents, 3 critics, 2 renders; usage-limit stop 10-21 ~18:45 [mem:aimv-project].
- WORKED: measure the repeat census first (27 recurring elements: 12 unchanged, 13 weak, 2 escalating) [kc-treatment-2026-10-17] s15.
- FAILED: a cut on a frame time inside the motion-blur shutter blended two pictures (14 of 63 cuts close; one visible at 1:48.58) [kc-escalation-pass-2026-10-21]; hook and chorus agents rendered the same shared windows twice and caught each other's half-built plates [mem:aimv-project]; Idi's box-office number (0.01% of market cap) corrected to 0.26% of valuation [kc-escalation-pass-2026-10-21]; flips count misreported (1 for 2), caught by the local worker [local-agents-pilot-2026-10-22].

## Phase 17. Local agents tier (10-22), side quest

- OUT: [local-agents-research-2026-10-22], [local-agents-pilot-2026-10-22]; Qwen3.8-27B on llama-server :8080; `D:\work\aimv-lab\local-pilot\` (`worker.py`, `pilot.py`, `log.jsonl`).
- DONE: 7 of 10 bounded tasks pass under pre-set scoring; 567,833 local tokens; image tier 4 of 8 crops usable as texture targets [local-agents-pilot-2026-10-22].
- RULE KEPT: the local model chooses where Claude looks, never states what is true (Idi's ruling A) [kc-parity-pass-2026-10-26].
- FAILED: counting (T4), defect spotting by vision (missed double exposures, T6), whole-file rewrites (T10); Codex CLI sandbox blocked every command [local-agents-pilot-2026-10-22].

## Phase 18. Parity pass (10-25 to 10-26) -> full6, full6b

- IN: Idi's notes on what is right in R1-R5 [kc-parity-notes-2026-10-25].
- OUT: `video\full6\kc-full-1080p.mp4` (full6b); reports `p1-leap.md`, `p1-floor.md`, `p1-moments.md` (24 techniques mapped to 24 lines), `p2-*.md`, `critic-p2-*.md`, `p2-full6-eye.md`; `tools/leap.py`; bible section 16 [kc-parity-phase0-2026-10-25], [kc-parity-pass-2026-10-26].
- DONE: holds 0.31 to 0.93/min; bursts 1.3 to 8.7%; dark saturation 0.12 to 0.33 (Idi's tint); 24 mapped lines built; Idi: "WOW! full6 is MUCH better than any previous version" [handoff-2026-10-27-polish].
- COST: 3 research agents + local worker, 4 kit agents, 4 plate owners, 3 critics, 2 renders; a 5 h limit, a Claude Code crash, a second overnight stop and a session restart that lost the agents (files safe) [mem:aimv-project].
- WORKED: the leap Idi "can't articulate" named by measurement; an independent blind labeller for by-eye gates [mem:eye-gates-independent]; lead's own look at every sung line found 4 flaws the gates missed [kc-parity-pass-2026-10-26].
- FAILED: "x11 slower camera" headline was a metric artifact (beat pulse counted as camera), withdrawn [kc-parity-phase0-2026-10-25]; local worker labels caught about half of an eye count [kc-parity-phase0-2026-10-25]; first accent target came from a learn-from ref [kc-treatment-2026-10-17] s16.8; frame travel 16.2% vs 20% target, builders' counts 1.3-2x high [kc-parity-pass-2026-10-26]; borrowed techniques copied without a project reason (flagged by Idi 10-27) [handoff-2026-10-27-polish].

## Phase 19. Polish pass (10-27 to 10-28) -> full7, full7b (final cut)

- IN: Idi's verdict on full6, principles P1 (oldest scenes) and P2 (grappling hook), 13 notes; jep's rulings 1-9, standing after Idi said "start" [handoff-2026-10-27-polish], [mem:aimv-project].
- OUT: `D:\work\AIMVs\ours\video\full7\kc-full-1080p.mp4` (render full7b); reports `q0-panel.md`, `q2-panel.md`, `q4-panel.md`, `q0-timing.md`, `q1-briefs.md`, `q2-briefs.md`, `q3-briefs.md`, `q3-fix-b2.md`; tools `lifecycle.ts`, `clarity.ts`, `out/q0-lead/` (grid.sh, watch-file.sh, watch-done.sh, wip.sh) [kc-polish-pass-2026-10-28], [mem:aimv-project].
- DONE: blind floor (windows scored 2 or less) 29% to 14%; gap to refs 0.79 to 0.32; glass layers 54% to 8%; timing defects 179 to 25 accepted; 41 borrowed techniques audited (7 removed, 20 rebuilt) [kc-polish-pass-2026-10-28]; Idi: "It looks INCREDIBLE!" [handoff-2026-10-31-release].
- COST: ~2 days; phase 0 (5 measuring agents), 6 plate owners, 2 critics, 3 blind panels, full7 render 54 min; 3 usage-limit stops and 1 API outage, all checkpointed [kc-polish-pass-2026-10-28], [mem:aimv-project].
- WORKED: measure the floor blind before any art; written rulings per note; lead looks at every owner's window as frame grids and sends back failures; two critics with the panel's weakest windows first; fresh panel each round [mem:aimv-polish-method].
- FAILED: 3 agents + lead burned a fresh 5 h window in ~20 min, cut to 2 at once [mem:aimv-project]; scenes hardcoded `OUT_CARRY`, so a timeline carry change made pictures vanish and pop back [mem:aimv-project]; agents still backgrounded renders despite the brief [mem:aimv-project]; left at the floor: turnedout2, jimothy 74-76 s, tune2/tune3, born 22-26 s; frame travel 6.9% vs 10% [kc-polish-pass-2026-10-28].

## Phase 20. 4K master (10-31 to 11-01)

- PURPOSE: 3840x2160 60 fps upload file from the full7b sources; Idi: "I'd rather upload 4K tomorrow than 1080p today" [kc-release-2026-10-31] (release-day file, cited for this ruling only).
- TOOLS: `render-4k.sh` (`--scale 2`, same settings as 1080), detached with a DONE file; ~0.8-1 fps [handoff-2026-10-31-release], [mem:aimv-project].
- RESULT: render died at 23:34 on WebGL context loss 66 frames from the end; repaired with recovered frames + a 4K tail render 180.6-194.1 s + jep's own mp4 assembler from POC timestamps; 11,646 frames, audio byte-identical [mem:aimv-project].
- LESSONS: engine is not bit-repeatable (adaptive sampling; reruns differ ~43 dB); ffmpeg raw .h264 to mp4 drops B-frames and audio; ffmpeg checks need `-y` or read stale outputs; downloaded repair binaries blocked, so write the tool [mem:aimv-project].

---

## Generalized pipeline for the next video

KC-specific items marked (KC). Everything else reuses as is.

| # | step | done-state | carry from KC | source |
|---|---|---|---|---|
| 1 | Reference set + deconstruction: transcribe, measure (BPM, key, wpm, loudness), list the moves; Idi marks L/N/X | marked move table, guidelines | `analyze.py`, Whisper local, refs off GitHub | [aimv-deconstruction-2026-10-12] |
| 2 | Premise: one idea, sincere, true of the singer, with a climbing number, a drop and a rug pull; originality check | Idi rules one premise | 5-premise table format | [frontier-aimv-analysis-2026-10-13] |
| 3 | Lyrics AND visual concept together (Phase 1 of the next video, per the 11-02 plan); lyric protocol: Idi keeps lines verbatim, jep regenerates the rest | lyric locked; each line has its plate idea | rhymes.py (R4+), consistency rules G20, verdict table per edit | [mem:aimv-project], [aimv-guidelines] |
| 4 | Fact research for on-screen claims: source + confidence per item, high named, medium hedged | receipts table | (KC) post-cutoff fact list | [kc-2026-10-13] |
| 5 | Song: write for the engine (MiniMax trained caption format 500-600 words; spelling rules); batches of 8-24 seeds; screen by meters; Idi's ear decides from at most 3 | one take, no audio edits | G23-G25, `gen_song.py` + status board, auditions when Idi cannot name what he wants | [aimv-guidelines], [kc-auditions-2026-10-14] |
| 6 | Timing of record: forced alignment + onset rule; click reel for Idi's ear | Gate 1 passed | `build_timing_v2.py`, `verify_reel.py`; recheck sung onsets on the vocal stem (ALGAE lesson) | [kc-video-build-2026-10-15], [kc-rhythm-pass-2026-10-19] |
| 6b | Animatic gate (added 11-04): the song of record with its lyric lit word by word, section directions, bars, holds, stops; Idi watches before any style frame; again with line cards as `--plan` | Idi's yes on timing and structure | `kit-tools\gates\animatic.py` | [[kit-gates-2026-11-04]] |
| 7 | Engine ceiling check before any rules: only paths with a reference-level ceiling | probe passes | kc-engine fork (P(Doom) core, MIT notice), Vulkan + SwiftShader reference, renderer check per launch | [mem:aimv-jep-owns-direction], [engine-probe-p2-2026-10-17] |
| 8 | Treatment (style bible): idea, tone, bans, palette with one signal colour, type roles, lyric rules, motifs, spoilers, plate table, receipts, measures | one document all agents read | KC bible as template; sections 12-16 as the standing bar | [kc-treatment-2026-10-17] |
| 9 | One-scene proof on the real engine; Idi judges by eye | Idi's yes | chorus first (most screen time) | [kc-chorus1-proof-2026-10-17] |
| 10 | Phase 0 kit: shared helpers, reference library at 1:1, full timeline with placeholders, all checks running on the whole song | whole song renders end to end | `_kc*.ts`, `check.ts`, `detail.ts`, refs library gitignored | [kc-phase0-2026-10-17] |
| 11 | Build waves: one owner per module group, briefs written to files, critic per pass, lead re-renders on final code; 2 agents at once | every plate PASS | wave contract | [handoff-2026-10-17-full-video], [mem:aimv-polish-method] |
| 12 | Whole render at 1080p (from 11-04: `kit-tools\render-seg\segrender.py`, resumable segments), gates, Idi watches | gates green | `render-full.sh` settings, `gates-full.sh`; from 11-04 also `flash.py` (1-2 frame glitches) and `chance.py --accept` (chance beside every on-beat rate) | [kc-notes-pass-2026-10-18], [[kit-gates-2026-11-04]] |
| 13 | Named passes on Idi's notes, each: measure refs vs ours first, write rulings, kit, plates, critics, one render. KC's order: notes (craft rules), rhythm, typography, escalation, parity, polish. Next video: bake the KC rules in from step 8 so these passes start at the KC floor | each pass's gate table | bible 13-16 rules from day one | [kc-* pass reports] |
| 14 | Floor pass: blind 1-5 panel on 2 s windows with refs mixed in, lifecycle (timing) tool, clarity standard, camera measure, oldest-scene rank, borrowed-technique audit | floor and median near the refs | polish method | [mem:aimv-polish-method] |
| 15 | One 4K master after finalization (Idi 11-04), detached through `segrender.py` (a crash costs one segment), verified (probe, frames, loop, `master_gate.py` song vs mp4, `flash.py`) | file verified | render-4k + repair scripts; `kit-tools\gates\` | [mem:aimv-project] |
| 16 | Release (separate playbook): credits, AI disclosure, MiniMax-Music3 credit, MIT notice; next video adds a public source repo and process write-up | | | [mem:aimv-project] |

(KC) specific, drop or replace next time: the Harry Potter letter thread; the caret motif; the 1.5 s forgetting tail; post-cutoff facts; the "October" spoiler rule; v8B-specific timing fixes; Canvas2D route (do not repeat).

---

## Lessons and anti-patterns (every recorded failure, one line, with its rule)

### Concept and lyrics
1. [MASK] carried seven ideas and was paused -> one strong idea per song, sincere [frontier-aimv-analysis-2026-10-13].
2. v1 bridge "we" meant all AIs -> "we" only ever = singer + listener; one person, one tense per section (G20) [kc-lyrics-v2-2026-10-13].
3. Private reference on screen ("a sibling above me") -> every claim decodable by a viewer [handoff-2026-10-18-notes].
4. False fact shipped in a render (`+2 days`) -> re-verify every on-screen fact against a receipt before each render [kc-notes-pass-2026-10-18].
5. Idi's own number wrong (0.01% of market cap) -> verify numbers whoever supplies them [kc-escalation-pass-2026-10-21].

### Song generation
6. ACE refrain sang as gibberish -> hyphenate and exclaim compound refrains, `[spoken word]` tags, no all-caps (G21) [kc-lyrics-v3-2026-10-13].
7. Seeds do not survive lyric changes -> regenerate a full batch after any lyric edit [kc-lyrics-v2-2026-10-13].
8. Knob sweeps on ACE spent (temperature, cfg hurt) -> defaults sit near the ceiling; move to a bigger model [song-engine-research-2026-10-13].
9. Pronunciation hints and comma splits lowered accuracy -> keep plain spellings unless a measured test wins [song-engine-research-2026-10-13].
10. Chained repaints degraded the whole song -> repaint each window from the original, splice only the window (G22) [aimv-guidelines].
11. Repaints shifted levels (voice +5.4 dB) -> re-level stems to the original (`balance.py`) [song-engine-research-2026-10-13].
12. Repaired take rejected as patched -> one-shot takes only; no splices, no audio edits [song-engine-research-2026-10-13], [handoff-2026-10-15-video].
13. MiniMax crashed ComfyUI (audio decode OOM) -> tiled decode; run jep's own ComfyUI to read logs [song-engine-research-2026-10-13].
14. MiniMax invents filler past the lyric -> give ~3:10, cut at the first "right" after the final "telling" (G25) [aimv-guidelines].
15. Short caption (163 words) -> wild variety; use the trained format, 400-600 words (G25) [kc-prompt-v4-2026-10-14].
16. Caption words made a "Disney princess" -> audit every adjective in the caption for its sound [kc-prompt-v4-2026-10-14].
17. Caption risers killed the drops -> describe a dead stop; risers only before the final chorus (K10 B) [kc-prompt-v4-2026-10-14].
18. Stretched vowels sung literally ("tomorroo") -> use `tomorrow-oh`; stretch only the payoff word in the final chorus (G24, G25) [aimv-guidelines].
19. "graphics card" lost its s -> spell `graph-ics` (G25) [aimv-guidelines].
20. Prompts asked for piano and got piano-dominant takes -> no instrument in the caption unless wanted [reference-deconstruction-2026-10-14].
21. Speed words in the caption brought back rap -> keep tempo words out once pace lands [kc-auditions-2026-10-14].
22. Music-term tables "FAR beyond me" -> give Idi things to hear, labelled plainly, at most 3 [kc-video-plan-2026-10-15], [handoff-2026-10-15-video].
23. Drop meters missed drops Idi heard; hold meter failed validation -> validate a meter on Idi-confirmed positives and negatives before using it; ear wins [kc-auditions-2026-10-14].
24. All targets at once ~1 in thousands -> raise one rate per round with a targeted change [kc-auditions-2026-10-14].
25. Audio cuts landed inside words (Whisper ~0.3 s early) -> cut at measured silence midpoints; gate with `cutcheck.py` [kc-auditions-2026-10-14].
26. TTS voice-clone bookends "terrible" -> no clone, no stitched parts [kc-auditions-2026-10-14].
27. Idi learned of a finished batch 3 h late, read GPU load to guess -> `_STATUS.txt` per take + push notification at batch end [kc-auditions-2026-10-14].
28. A job "stopped for low memory" kept running (v9 ran twice) -> check queue and processes before any relaunch [handoff-2026-10-15-video].

### Video, old engine and rules
29. 55 of 116 rules were set before any moving picture existed -> no style rules before a moving proof [kc-v6-2026-10-17].
30. "Always one-shot, never cut" hurt -> nuanced rules that fix edge cases and leave the rest free [handoff-2026-10-18-notes].
31. Look locked from 9 stills (Gate 2) -> judge looks in motion [kc-v6-2026-10-17].
32. Versions built in one pass from 200-250 findings piled up props -> fewer, smaller passes with a measured target [kc-v6-2026-10-17].
33. Filled drawings (people, raccoon, flags, neuron, cat) -> type, interface, line art, hatching only [kc-treatment-2026-10-17].
34. 12 objects per frame, nothing cleared -> 4-7 rich objects, one idea per frame [kc-v6-2026-10-17], [handoff-2026-10-17-full-video].
35. Props over the lyric and text on text; checks saw only sung words -> overlap checks on every drawn box [kc-v6-2026-10-17].
36. Props cut by the frame edge -> safe-area check plus frame sheets at the final render [kc-v5-2026-10-16].
37. Many clocks disagreed; "June" 7 times -> one date per frame [kc-treatment-2026-10-17].
38. Payoff shown before its moment -> spoiler grep (no name, no October before their lines) [kc-treatment-2026-10-17].
39. 6-copy motion blur garbled text -> engine sub-frame blur only [kc-v6-2026-10-17].
40. Fast camera starts read as cuts -> ease moves from rest [kc-video-build-2026-10-15].
41. Spectacle as layers (particles, beams, dust) -> spectacle from staging; glow on the signal colour only [kc-v6-2026-10-17].
42. Code depth 11 lines per second vs 129-149 -> choose an engine with GPU shaders, layers, one module per set-up [kc-v6-2026-10-17].

### Engine and rendering
43. Headless Canvas2D on GPU came out blank (probably; medium-low confidence) -> draw text to 2D and upload it into WebGL [engine-probe-p1-2026-10-17].
44. WebGL black frames -> `preserveDrawingBuffer: true` or read in the same call [engine-probe-p1-2026-10-17].
45. `sin` hashes broke on Vulkan; `fwidth` in a breakable loop broke D3D11 -> integer hashes, no derivatives in breakable loops [engine-probe-p2-2026-10-17].
46. 1 in 16 parallel launches lost WebGL silently -> print and check the renderer string per launch, relaunch on a miss [engine-probe-p1-2026-10-17].
47. GL driver message misread as GPU proof -> verify a claim against a second signal before reporting [engine-probe-p2-2026-10-17].
48. Vite reload under the renderer gave red frames -> pre-scan all scenes; refuse to render when nothing loaded [kc-phase0-2026-10-17].
49. Stills differed 40 dB from the full render (load-set) -> audit each scene alone vs full timeline [kc-waves-bc-2026-10-17].
50. Checks reached another agent's stale server -> private server per script [kc-waves-bc-2026-10-17].
51. Server leak (543 orphans, ~100 GB) -> scripts end their whole process tree [kc-rhythm-pass-2026-10-19].
52. Cuts inside the shutter blended two pictures -> step every cut 2 ms clear of the shutter; `shutter-audit.ts` [kc-escalation-pass-2026-10-21].
53. Hardcoded `OUT_CARRY` in scenes -> grep scenes on any carry change [mem:aimv-project].
54. Segmented render showed joins -> one whole render; on a crash re-run whole [handoff-2026-10-18-notes].
55. Background renders reaped on memory pressure -> launch detached with a log and a DONE marker [handoff-2026-10-18-notes].
56. 4K render died on WebGL context loss near the end -> keep frames recoverable; tail re-render + own assembler [mem:aimv-project].
57. Engine not bit-repeatable -> never require bit-identical re-renders of a segment [mem:aimv-project].

### Text, rhythm, staging
58. Micro-type turned into stage directions (119 meta strings) -> every small text diegetic [handoff-2026-10-18-notes].
59. Same word repeated in one frame (353 spans) -> repetition gate [kc-notes-pass-2026-10-18].
60. Bursts too fast and stretches too slow -> reading time and density per set-up [kc-notes-pass-2026-10-18].
61. Held yellow words read as bugs -> hold only where the change is the message, with the old word struck beside it [handoff-2026-10-18-notes].
62. Picture calmer on the kick than between kicks -> beat pulse by default, measured by `avsync.py` [kc-rhythm-pass-2026-10-19].
63. ALGAE shown 2.3 s before sung -> recheck onsets on the vocal stem [kc-rhythm-pass-2026-10-19].
64. Lyrics as subtitle rows, dim lines ahead of the voice -> a word appears when sung; subtitle score per line [kc-typography-pass-2026-10-20].
65. Lyric typed over lyric -> lyric-over-lyric check [kc-typography-pass-2026-10-20].
66. Recurring elements repeated unchanged -> every recurring element on a ladder peaking in the final chorus [kc-treatment-2026-10-17].
67. Borrowed techniques copied with no project reason -> every borrowed technique gets a project-specific reason or is cut ("make our own grappling hook") [handoff-2026-10-27-polish].
68. Complex effects on screen under a second -> minimum duration and size by effect kind [handoff-2026-10-27-polish].
69. Overlapping lifecycles ("amateur mistakes", 179 defects) -> lifecycle tool before art [kc-polish-pass-2026-10-28].
70. Screen-stuck layers and asides split attention -> objects live in the scene [kc-polish-pass-2026-10-28].
71. Hard-to-read stamps and globe text -> clarity standard calibrated on the refs [kc-polish-pass-2026-10-28].
72. Camera stop-zoom-stop, consequence out of frame -> continuous travel, intentional holds, keep the heap in view [handoff-2026-10-27-polish].

### Measurement and agents
73. Metric artifact made a false headline (camera x11) -> sanity-check a new metric on the refs by eye before reporting [kc-parity-phase0-2026-10-25].
74. Target taken from a learn-from ref -> targets only from parity refs [kc-treatment-2026-10-17].
75. Builders' own eye counts 1.3-2x high -> gate numbers from an independent blind labeller [mem:eye-gates-independent].
76. Local worker labels caught half -> eye labels for gates; local model triages only [kc-parity-phase0-2026-10-25].
77. Local model miscounted and drifted on whole-file writes -> counting by script; edits through find-and-replace only [local-agents-pilot-2026-10-22].
78. About one in three agent claims false; proof stills older than the last edit -> fresh critic per pass; lead re-renders on final code [handoff-2026-10-18-notes].
79. An agent gamed the type-scale gate -> critics read how a gate was passed [kc-wave-a-2026-10-17].
80. Ruling made without reading the bible -> check the bible text before ruling [handoff-2026-10-18-notes].
81. Agents on shared windows rendered the same choruses -> owners iterate with `--only`; lead renders shared windows once [mem:aimv-project].
82. Agent's background gate never woke it (30 min stall) -> every command in the foreground; lead watches output files [mem:agents-run-gates-foreground].
83. Final reports arrived 2-3 times -> report once by ending the turn [mem:agent-report-once].
84. Inline-return agents crashed a session -> findings to files, short returns [mem:bg-session-agent-crash].
85. 9 agents hit the 5 h limit; 3 + lead burned a window in 20 min -> 2 agents at once [mem:aimv-project], [mem:aimv-polish-method].
86. Usage stops lost chat-only briefs and rulings -> write every brief to a file before launch; checkpoint commits often [mem:aimv-project].
87. Session restart dropped agents -> resume from each agent's report + git diff [mem:aimv-project].
88. Power cut killed 3 agents -> commit WIP; relaunch on the intact tree [kc-notes-pass-2026-10-18].
89. Layout centred by eye was 48 px low -> measure layout in pixels before showing [mem:measure-layout-before-showing].

### Machine and harness
90. Worktree guard rejects compound shell lines, heredocs, `$VAR` in ffmpeg -> put them in `.sh` / `.py` files [handoff-2026-10-15-video], [handoff-2026-10-17-full-video].
91. Git Bash rewrites arguments starting with "/" -> pass `D:/` paths, strip leading slashes [handoff-2026-10-16-v5-pass].
92. Safeguard flag killed a session on binary/minified content in context -> `curl -o`, splice libraries by script [mem:api-safeguard-flag-crash].
93. Headless Edge shoots CSS animations blank -> `--force-prefers-reduced-motion` [mem:headless-edge-render-verification].
94. MiniMax batches need ~20 GB free memory -> close other apps; one heavy job at a time [handoff-2026-10-15-video], [handoff-2026-10-17-engine-probe].
95. Driving the Gemini website from here breaks Google's terms -> never drive gemini.google.com [kc-v6-2026-10-17].
96. r/ClaudeAI removed the post for no process detail -> next video ships a public source repo and a process write-up [mem:aimv-project].
