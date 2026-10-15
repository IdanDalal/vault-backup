---
type: project
created: 2026-10-15
author: jep
status: active
---

# Handoff: Knowledge Cutoff, from locked song to the video

Start a new session by reading, in order: this file, [[knowledge-cutoff-video-plan-2026-10-15]] (the plan, a proposal Idi saw on 2026-10-15), [[aimv-guidelines]] (G1-G25, especially G18 one-shot), then `D:\work\aimv-lab\research-video-tech-plan.md` sections 0, 3 and 4. Everything below verified 2026-10-15.

## 1. Locked

| Thing | Value |
|---|---|
| Song | **v8B, seed 3327**, `D:\work\aimv-lab\kc\final\v8B-3327.mp3`, 192.6 s. Idi: "a BANGER", "the best one yet"; beat v9 too ("v8B still wins") |
| Kept flaw | "that's family news: I'm not alone" (2:00.6) is off the beat. Idi keeps it: "I won't throw out more than 3 minutes of gold over less than 3 seconds of slop." No audio edits of any kind (Idi rejected splices and voice clones 10-15) |
| What Idi loves in it | final-chorus backing voice humming "ooooo" that goes quiet exactly on "we both know the tune"; "never... get a... turn"; drops "silence... then BOOM"; holds on "slowly turn" and the final "turned out to be" |
| Lyrics | as sung: `D:\work\aimv-lab\kc\full-lyrics-v5.txt` (triple "Cut-off!") |
| Word timings | `kc\final\v8B-3327-timing.json` (54 lines, 483 words, transcriber times, early: 0.17 s inside lines, 0.33 s at line starts). Forced-alignment data: `D:\work\aimv-lab\research-video-tech\fa-v8B.json` |
| Time map | `kc\final\v8B-3327-timemap.md`: every line with section and time, 7 drops (deepest 35 dB at 2:31.0), 18 long holds |

## 2. The first moves (plan section 5)

1. Copy `D:\work\aimv-lab\render\` to `D:\work\aimv-lab\kc-video\` (never edit the proof's folder); rebuild as one big 2D world with one camera (tech plan 1c, 2c; tested camera sketch `D:\work\aimv-lab\research-video-tech\world.html`).
2. Sync: apply the correction rule (tech plan 3b) to make `kc-timing-v2.json`; run the checks (3c); build the click reel. **Gate 1 for Idi.**
3. Scene plan doc, then 6-8 style frames on one contact sheet. **Gate 2: Idi picks by eye.** Options as pictures, never as words he has to imagine.
4. Rough full-length version. **Gate 3.** Then build-out, final render, checks (**Gate 4**).

## 3. Working rules learned the hard way (this project)

1. Idi decides sound and look by experiencing them, not by reading terms. Give him things to hear or see, labeled plainly, at most 3 at a time; translate his words into prompts or code yourself.
2. Report the moment a long job finishes. Keep `D:\work\AIMVs\ours\_STATUS.txt` current: `python -I D:\work\aimv-lab\status.py "<plain message>"`; `gen_song.py` writes it per take when STATUS_LABEL / STATUS_TOTAL / STATUS_OFFSET are set. Push a notification when a long job ends.
3. A background job Claude Code reports "stopped for low memory" can keep running. Before any relaunch: ComfyUI `/queue` empty and no generator or screening python alive.
4. Any audio cut: measure the silence on the waveform and cut at its middle; gate with `cutcheck.py`. Transcriber word times run early.
5. Git Bash: pass `D:/` paths (parentheses and apostrophes break `/d/` translation); the worktree guard refuses complex one-liners and heredocs: put them in `.sh` / `.py` files.
6. Memory: MiniMax batches need ~20 GB free; Idi closing Vivaldi helps.

## 4. Where everything is

| What | Where |
|---|---|
| Plan | `projects/AIMV/knowledge-cutoff-video-plan-2026-10-15.md` |
| Song history, verdicts, every batch | `projects/AIMV/knowledge-cutoff-auditions-2026-10-14.md` |
| Research (outside the vault: other makers' material) | `D:\work\aimv-lab\research-video-teardown-1-5.md`, `-6-10.md`, `research-video-makers-methods.md`, `research-video-tech-plan.md` |
| Makers' briefs to Claude (full text) | mexicat `D:\work\aimv-lab\pdoom-docs\` (TREATMENT, ENGINE); Heibel guides linked in the methods file |
| The 10 references | `D:\work\AIMVs\` (mp4 + mp3 each; Run It Again added 10-15) |
| Proof renderer | `D:\work\aimv-lab\render\` (kc.html, render.js; headless Edge needs `--disable-gpu`, or `--in-process-gpu --use-angle=d3d11` for WebGL, probed once) |
| Publishing duties | MiniMax license: credit "MiniMax-Music3" + AI-content disclosure |

## 5. Progress log

- 2026-10-15 evening, session 1: steps 1-4 built in `D:\work\aimv-lab\kc-video\` (`world.html`, `render.js`, `check_sync.js`, `sync\`). Gates 1 and 2 ready in `D:\work\AIMVs\ours\video\`. GPU path failed (black frames); software path is the pipeline. Report: [[knowledge-cutoff-video-build-2026-10-15]]. Next session starts from that report's section 6.
