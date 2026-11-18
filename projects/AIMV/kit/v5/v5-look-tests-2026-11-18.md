---
type: project
created: 2026-11-18
author: jep
status: active
---

# Pay Attention v5: three look tests (2026-11-18 evening)

Ruling: Idi's A ("A, go ahead"), type-first restart. Proposal [[../v5-restart-proposal-2026-11-18]]. Grammar [[look-guide]], film plan [[section-map]].

## Method

- Look guide: 240 reference stills measured (6 videos), 12 rules, field and type catalogues, a 40-still reference pool.
- Blind panel (`lab scratch\lead\v5\tools\mkpanel.py`): our stills shuffled among the 40 reference stills under neutral names; one judge agent scores all 1-10 and names same-production groups; key file kept outside the panel folder.
- Calibration (v4 stills Idi already judged): v4 proof hand 5, title over hand 5, fractal 5, fractal-8 heads 4; references median 7. The panel grouped all four as "one weaker production". Panel agrees with Idi's rejection.
- Pass bar: stills at 7 or more (reference median) and not grouped as a weaker production.
- Caution: the panel ranked What Counts (Idi's favourite reference) as its weakest group. It checks finish, never taste; Idi's eye rules.

## Results

| test | window | panel 1 | panel 2 (after fixes) | state |
|---|---|---|---|---|
| T1 chorus 1 | 69.5-79.5 | extruded lit slabs: 3, 3, 2, 3, weakest of 52 ("2005 WordArt title template") | rebuilt as a transformer attention diagram: 9, 8, 8, 7, strongest group of 52 | pass |
| T2 Socrates and the ink | 9.3-21.7 | 5, 5, 5, 4 | after 2 rounds: 7, 8, 7, 6 | pass |
| T3 the cheat code | 103.7-113.7 | 7, 7, 6, 5 | after 1 round: 7, 7, 6, 5 (EVERY wall letters malformed) | at the bar |

References: median 7 in both panels.

## The finding that matters

"Pay attention" is the transformer's attention mechanism, and the song's "Eight heads, and every head was looking somewhere new" is multi-head attention (the 2017 paper "Attention Is All You Need" used 8 heads). The attention diagram (tokens, weighted arcs, mono HUD: `CAUSAL SELF-ATTENTION · LAYER 12 · HEAD 0 / 8`, `a = softmax(q·kT / sqrt(d_k))`) is the film's natural field family, and it scored above every reference group.

Dead end, recorded: extruded beige 3D type with lightning and blue halo reads as a stock title template.

## Files

- Clips `D:\work\AIMVs\ours\pa-song\v5\chorus1.mp4`, `ink.mp4`, `games.mp4`; stills `<name>-1..4.png`.
- Engine scenes `app\src\scenes\v5-chorus1.ts`, `v5-ink.ts`, `v5-games.ts` (demo switch `VITE_PA_DEMO=<file>`); reports `reports\v5-chorus1.md`, `v5-ink.md`, `v5-games.md`.
- Briefs `lab pa-video\briefs\v5\` (common, t1-t3, t1b-attention). Panels `lab scratch\lead\v5\panel-cal|1|2` with scores and keys.
- Decision page version 6, tab "v5 look tests": https://claude.ai/artifact/5hyoV9n9kAUw1W65f9j7Bb (each question: v3 / v5 test / neither, nearest reference frame beside it).

## Open

- The sync check reads only pure white as lit, which forces a one-frame white flash on landing words; fix the check before the full build.
- T3 letterform pass on voxel type; T1b raised arm reads as stacked brackets.
- The engine's countdown clock (bottom right) sits in every test; panel 1 named it a mark of our weaker frames. Keep or drop is open.

## Next

Idi taps the three questions. On "this direction": write the section map into 13 plate briefs in the v5 grammar, attention diagram as the chorus family, then build in waves with the panel as the gate.
