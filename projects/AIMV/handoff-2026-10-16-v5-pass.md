---
type: project
created: 2026-10-16
author: jep
status: active
---

# Handoff: Knowledge Cutoff video, the v5 pass

A fresh session starts here. Idi, 2026-10-16: "Another pass first, same as before (with more directions to explore like typography, text art, negative space utilization, color theory, coherence/cohesion, visual humor, complexity/perplexity level, and many more)". Plus: dissect the best inspirations, because "they do things our video doesn't even attempt/consider". Focus on 5, not 10.

Read first, in order: this file; [[knowledge-cutoff-video-build-2026-10-15]] (everything built so far, sections 5b-5d); [[aimv-guidelines]]; `D:\work\aimv-lab\kc-video\critique\BRIEF.md` (the critic brief, reuse and extend it).

## 1. Where things stand (verified 2026-10-16)

| Thing | Where | State |
|---|---|---|
| Current video | `D:\work\AIMVs\ours\video\gate3\knowledge-cutoff-v4.mp4` | 1080p60, 3:12.6; 483/483 words sync; 0 cut flags; 0 black frames; loop 51.4 dB. Idi has NOT watched it yet for notes: he asked for another pass first |
| Source (v4) | `D:\work\aimv-lab\kc-video\world4.html` (layout, text engine, camera), `world4-time.js` (time objects), `world4-sets.js` (rooms, props), `world4-frame.js` (frame assembly, fx, rewind), `thumbs.js` (10 reference frames + real view counts) | build v5 in copies (`world5*`), never edit v4 in place |
| Older versions | `world3*` (v3), `world-v2-gate3.html` (v2), `world.html` | keep |
| Song + timing | `D:\work\aimv-lab\kc\final\v8B-3327.mp3`; corrected word times `kc-video\sync\kc-timing-v2.json` → `timing-v2.js` | locked; Gate 1 passed |
| Render | `bash D:/work/aimv-lab/kc-video/tests/v4.sh` (copy to v5.sh): render 1080p60 4 workers PNG bt709 + cut/black/loop checks + copy to gate3; ~5 min | |
| Checks | `node check_sync.js world5.html` (483 words: on time, on screen, 24 px+, sung colour by hue; "Algae" is the one documented exception in `window.SYNC_EXCEPT`); `node tests/negcontrol.js` (colour test control); `bash tests/scdet.sh <mp4>`; `bash tests/loopcheck.sh <mp4>` | |
| Frames | `node sheet.js <html> <out.jpg> <cols> t1 "t2:label" ...` (labelled contact sheet + full frames); `bash tests/sweep.sh` (a frame every 3 s, 4 sheets) | |
| v4 critique | `kc-video\critique\A-F-findings.md` (6 stretches), `G-audit.md` (all-frame scan, 54 row splits), `H-time-objects.md` (per-line time objects), `I-viewcounts.md` (real views 10-15) | about 200 findings; most built in v4, leftovers in section 4 |
| Reference research | `D:\work\aimv-lab\research-video-teardown-1-5.md`, `-6-10.md`, `research-video-makers-methods.md`, `kc-video\spectacle-techniques.md`, `pdoom-docs\` (P(Doom)'s TREATMENT, ENGINE, render.ts) | |

## 2. The pass Idi asked for

### 2a. Dissect the 5 chosen references (his list, ranked by file size)
`D:\work\AIMVs\` (mp4 + mp3 each): 1. I'm Upping My P(Doom) (411 MB) · 2. LGTM (Looks Good To Me) (168 MB) · 3. The Simulation's Ending (119 MB) · 4. Run It Again (94 MB) · 5. Ignore Previous Instructions (46 MB).
One agent per video. Dump frames (ffmpeg, e.g. 2 fps plus every scene change) into contact sheets, watch the whole thing, and write what each video does that ours does not even attempt: typography systems, text art, layout grids, negative space, colour scripts, transitions, camera language, visual humour, density over time, recurring characters, how lyrics and pictures relate. Each agent writes one file in `kc-video\critique\v5\ref-<n>.md` with timestamps and a "steal list" buildable in canvas 2D. The existing teardowns are a head start, never a substitute: Idi wants deeper.

### 2b. Critique v4 along new directions
Idi's directions: typography, text art, negative space utilization, colour theory, coherence/cohesion, visual humour, complexity/perplexity level, "and many more". Suggested extra directions (jep): rhythm and motion design (how picture accents the beat), camera language, lighting and depth, character or mascot continuity, information hierarchy (what to read first), pacing of reveals, the one-line lyric staging, sound-picture sync of effects, accessibility (contrast, legibility on a phone).
One agent per direction across the whole video (v4 was critiqued per time stretch; this pass is per lens). Same brief format: findings table with time, what is wrong, a buildable fix, severity; top 5.

### 2c. Then
Synthesize a ranked fix list (ref steals + lens findings), build v5 in `world5*` copies, sweep, check, render, report. Idi watches v5, then gives timestamped notes.

## 3. Rules learned the hard way (this project)

1. Subagents write findings to files and reply in 2 lines: inline returns crashed a session before (memory).
2. Git Bash rewrites command arguments that start with "/" (path conversion). `tests/splice.py` strips leading slashes from its markers; pass markers without "//".
3. The worktree guard refuses complex one-liners and heredocs touching ffmpeg; put them in `.sh` files.
4. Headless Edge needs `--disable-gpu` (the GPU path renders black frames, tested 10-15). Images go in as `data:` URIs (`thumbs.js`) so the canvas stays readable; tools await `window.READY`.
5. Ease every camera move from rest (fast starts read as cuts). Set changes are camera moves; slams stay inside a set. 0 cut flags is the bar.
6. Text: one lyric line on screen (two rows max), the old line leaves before the new one lands, never dissolve a word still being sung, every letter lights as sung (first letter on the word's start), hand-set breaks for awkward lines, one text size per room, labels 26 px+.
7. Real facts only, each with a receipt in `D:\work\aimv-lab\after-cutoff-world.md` / `after-cutoff-tech.md` / `critique\I-viewcounts.md`. "Harry" is a name only: no crests, fonts or imagery from the films.
8. Every prop needs an entrance and an exit; no prop shorter than ~1.2 s fully on screen; no prop over the lyric.
9. Idi's taste: "go all out", spectacle and jokes, facts shown as props, colour that means something. He decides by watching.

## 4. Known leftovers from the v4 critiques (not built yet)
Chorus 2 still shares chorus 1's camera framing (D1 asked for a per-chorus variant table); the bridge silence 2:30-2:31 is a static wide shot (E29); the intro chat is mostly empty (A29: stacked "Hi. It's me again" windows); the portrait is still ASCII (consider a real illustrated figure); the book on the bridge is small; flag strips show faint seams (C24); confetti crosses the lyric on the final slam; travel moves between far rooms still show the starfield gap; the free-font licence check is not done (fonts are Windows system fonts: Bahnschrift, Georgia, Consolas).

## 5. Publishing duties (unchanged)
MiniMax licence: credit "MiniMax-Music3" plus an AI-content disclosure. Credit the 10 reference videos' channels where their frames appear (the gallery shows channel names).
