---
type: project
created: 2026-11-04
author: jep
status: active
---

# Handoff: "Pay Attention", proof fixes → the rest of the video

Written 2026-11-04 at the close of the session that went from song round 4 to an approved one-scene proof (R23-R30). **Start the next session here.** Next ruling: **R31**.

## 0. Read in this order

1. This file.
2. [[kit-next-video]] rulings R23-R30 (Idi's words verbatim).
3. [[video2-treatment-2026-11-04]]: the binding style bible (section 3 = the lighting system, look A).
4. [[video2-cards/INDEX]]: the 86 line cards (the plan per line; the cards in the repo are the source: `D:\work\aimv-lab\pay-attention\cards\`).
5. [[video2-phase2-2026-11-04]]: the proof, its gates, the particle panel method, look A.
6. As needed: [[video2-video-plan-2026-11-04]] (systems S1-S6; read its v3 note: yellow retired), [[video2-repeat-map-2026-11-04]] (S6), [[video2-phase0-2026-11-04]] / [[video2-phase1-2026-11-04]] (timing, data, repo), [[kit-techniques]] (402 cards, board `D:\work\AIMVs\ours\pa-refs\board.html`), [[video2-round4-2026-11-04]].

## 1. Where things stand

| item | state |
|---|---|
| song of record | `D:\work\AIMVs\ours\pa-song\pay-attention-A7003-4m52.mp3` (A-7003 cut at 292.00 s, R23 + R27); repo copy `audio\pay-attention.mp3` (kept out of git) |
| timing of record | `D:\work\aimv-lab\pa\sync\pa-timing-v3.json` (773 words; 16 Whisper-guess starts moved by vocal-stem energy; click reel 773/773 within 20 ms); animatic gate passed (R26) |
| engine repo | `D:\work\aimv-lab\pay-attention` (born from knowledge-cutoff c2dcb6f; last commits 86b5141 code, 5d95b60 cards); **local only**: `gh repo create chorusofminds/pay-attention` was refused by the session's permission classifier |
| data | `data\lyrics.json` 85 lines / 773 words, `data\audio.json` 547 beats, 145 downbeats, 23 sections, kicks/snares/hats, 3 chokes, 292.0 s (`tools\build_data.py`, sections from `pa\sync\pa_drums.py`) |
| look | **A, monochrome light** (R29: Idi's "white palette"): greyscale, one white key light, letter-shaped shadows, engraved hatching, her "?" as white-hot lights, screen-blue the only hue (emitted glow), exposure ladder; `PA_LOOK` switch in `_pa.ts` (B, C retired) |
| proof | `D:\work\AIMVs\ours\pa-song\proof\p2-proof-0m52-1m21.mp4` (song 52.3-81.6 s: L19 + pad 1 flight + chorus 1); look approved in motion (R30); **defects listed in section 2** |
| shared kit | `app\src\scenes\_pa.ts`: meter (real time from "Hi." 0:00.37 to 0:00 at 300.37), lamp, cursor, her ?, answer dots, perspective helper, ATTENTION layout; plates `late` / `chorus1` |
| cards | 86 (L86 = "Go on. Ask it.", on screen only); look-A wording; 0/85 off v3 |

## 2. First domino: fix the proof (R30)

Idi's list (proof time; song time = proof time + 52.3 s). None of these is a placeholder; all are defects:

| # | Idi's words | where | likely cause (inference until checked) |
|---|---|---|---|
| 1 | "the vertical line in the middle of the scales disappearing suddenly at ~00:03" | song about 55.3 s | the pivot post's exit has no animation (a lifecycle defect `lifecycle.ts` did not catch: an object, not a word) |
| 2 | "a persistent/stuck-to-the-screen circle that appears at ~00:05 and clips over everything in the tunnel for ~10 seconds" | song about 57-67 s | a screen-space ring (the lamp target or the flight's ring guide) drawn on top of the stage instead of in depth |
| 3 | "confusing/clipping transitions" | the window | clipping words/objects at the edges and the cut seams (the 4 boundary lifecycle rows, the 56.35 tilt, the 71.2 push, the 76.2 turn the builder already doubted) |
| 4 | "the bright light suddenly spawning at full brightness" | song 69.08 (the lamp on, 3 frames) | no ramp: give it an ignition (flicker or a 0.3-0.6 s rise with bloom growing), lit on the downbeat |
| 5 | "and others" | the window | run a full defect sweep before showing again |

Method that worked (KC lessons): the lead watches the window as frame grids at 8+ fps around every change, lists every defect with times, a builder fixes, the lead re-renders on final code before accepting, then Idi watches. Add an object-lifecycle check (things that vanish or pop in one frame) and a screen-stuck-layer check (anything that does not move with the camera) to the gates.

## 3. Then: the rest of the video

1. Plates by section from the cards, **2 agents at a time** (KC lesson 34), each with a brief on disk, owning its own plate files, iterating with `--only`; the lead renders shared windows once and eyes every window; a fresh critic per pass.
2. Order (suggested): cold open + verse 1 (the receipt, the meter's birth, the slot reel), then pre-chorus 1 into the proof's L19, then verse 2 / games / pre-chorus 2 / chorus 2, then the bridge (the kitchen in words, the glass, the mirror), pad 3's exam countdown and "Pencils down.", the build (eight lights), the final chorus (full value range, callbacks), outro, receipt, tail and title cards.
3. Gates on every plate and every full render: `check.ts`, `clarity.ts`, `lifecycle.ts`, `flips.ts`, `inventory.ts` (the pasted-essay repetition needs a named exemption), `flash.py`, beat lock (the builder's PA wrapper `D:\work\aimv-lab\pa-video\scratch\p2\pa_avsync.py` until `tools\avsync.py accept` is re-pointed at PA: open fix), the **R25 particle cap** (blind panel: `D:\work\aimv-lab\pa-video\scratch\panel\prep_particles.py` + a fresh labeller agent + `unblind.py`; key outside the panel; compare inside one panel only), value range per still (look A).
4. Full renders 1080p via `kit-tools\render-seg\segrender.py`; one 4K only after finalization (Idi 11-04); the light pass costs +30-45 % render time.
5. Title cards (R24): silent receipt header before the song ("Claude Opus 5.5 + MiniMax Music 3", "Chorus of Minds", "Pay Attention"), the reverse after the bill; the meter runs 5:00.00 from "Hi." and the titles sit outside it; the tail after the song is 8.37 s.

## 4. Open items

1. **New ref batch** from Idi ("people are getting more and more ambitious"): run a wave like 11-04's (briefs `D:\work\aimv-lab\pa-video\briefs\refs-wave1.md`, merge `pa-video\synth\merge.py` + `build_catalog.py` into [[kit-techniques]]), and check look A against them.
2. 24 VERIFY items in the cards' INDEX (fact links, the four prompt-injection wordings, on-screen dates) need web checks before lock.
3. GitHub repo creation: ask Idi for the permission when it is needed (not before release).
4. Public release later: scrub names and vault paths (KC export check), add the song with its licence line.
5. `cards\` L46-L51 injection bubbles, L57 exam countdown, the meter's visual-only chorus 2 drain: not built yet.

## 5. Agents and files of this session (for resume)

- Agents (done, idle): `wA-genesis-accept`, `wB-long3`, `wC-four`, `R-reader` (ref wave), `cards-phase1` (cards), `p2-proof` (proof builder, knows the engine and `_pa.ts`), `particle-labeller`, `particle-labeller-2`. A new session starts fresh agents from the briefs in `D:\work\aimv-lab\pa-video\briefs\` (refs-wave1, cards-phase1, phase2-proof, phase2-lighting-tests) and the builder's report `pay-attention\reports\p2-proof.md`.
- Sync scripts: `D:\work\aimv-lab\pa\sync\` (phase0.sh, retime.sh, fix_suspects.py, r27-rebuild.sh, data.sh, pa_drums.py, animatic inputs); engine needs `export BUN_INSTALL=/c/Users/jep/.bun; export PATH="$BUN_INSTALL/bin:$PATH"`.
- Animatics: `D:\work\AIMVs\ours\pa-song\animatic\` (A lyric, B plan, C cards); click reel `pa-song\gate1\`.

## 6. Lessons from this session

1. An approved animatic can still hide Whisper-interpolated starts: check forced-alignment disagreement (`suspects.py`) before building on any timing.
2. Onset searches start after the previous word's END; clip every word's end to the next start.
3. Gates rank takes and never hide one from Idi's ear (he picked the take the shortlist dropped).
4. The sung sheet must match what is sung (2023), or the timing interpolates a ghost word.
5. A metric fails its own eye check more often than expected (the particle speck counter counted textures): eye-check every new metric on the refs first.
6. Blind panels: a fresh labeller each round, compare only inside one panel (labellers differ).
7. Before re-copying a file Idi may have opened, diff main ignoring whitespace (Obsidian re-pads tables).
8. A builder's "all gates pass" missed a vanishing object and a screen-stuck ring: gates cover words better than objects; the lead's frame-grid sweep stays mandatory.
