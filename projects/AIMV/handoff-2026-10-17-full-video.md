---
type: project
created: 2026-10-17
author: jep
status: active
---

# Handoff 2026-10-17: Knowledge Cutoff, full video at 4K 60 fps with parallel agents

START HERE in a fresh session. Read this file, then [[knowledge-cutoff-treatment-2026-10-17]] (the style bible), then [[knowledge-cutoff-chorus1-proof-2026-10-17]] (the proof and its engine), then P(Doom)'s `docs/ENGINE.md` (`D:\work\aimv-lab\refcode\pdoom-video\docs\ENGINE.md`, the scene-author contract our fork keeps).

## 1. Idi's ruling, 2026-10-17 (his words)

- On the proof: "Excellent work! This looks like a high-ceiling path with MASSIVE potential. Ideas and execution are all top-tier."
- The task: "a handoff to a new session with parallel agents where this proof turns into a full video in the promising new engine."
- The bar: "not a single frame of the proof can stay the way it is now. They must all be equal to (ideally exceed) the inspirations based on this engine in every aspect."
- The format: "a 4K 60FPS output, equal to 'I'm Upping My P(Doom)'", so the question for every frame is "what's the maximum amount of detail a frame SHOULD hold?" rather than "what's the maximum amount of detail a frame CAN hold?" at "compressed, low-bitrate, YouTube-level 1080p on a phone screen".
- Standing contract (10-17): jep owns creative and technical direction toward reference level and beyond; Idi judges by eye. "Parallel agents" in his request is his opt-in to multi-agent work for this session.

## 2. Where things stand

| item | state | where |
|---|---|---|
| song of record | v8B seed 3327, 192.6 s + Idi's 1.5 s silent tail; no audio edits | `D:\work\aimv-lab\kc-engine\audio\kc.mp3` |
| style bible | 18 modules, 72 set-ups, every lyric line mapped, receipts table, spoiler rules | vault `projects/AIMV/knowledge-cutoff-treatment-2026-10-17.md` |
| engine | P(Doom)'s core (MIT notice kept), our palette, fonts, data, helpers, checks; Vulkan default | `D:\work\aimv-lab\kc-engine\` |
| proof | chorus 1, 27.7 s, 1080p, all checks green; the baseline to beat (not to keep) | `D:\work\AIMVs\ours\video\proof\kc-chorus1-proof.mp4` |
| 4K | the fork renders true 3840x2160 (`--scale 2`): 4 stills in 5.8 s incl. browser start | `kc-engine\detail.sh`, `out\detail\` |
| reference | P(Doom)'s upload is 3840x2160, 60 fps, AV1, ~21 Mb/s (LGTM: 2560x1440) | `D:\work\AIMVs\` |

## 3. The detail standard (the "SHOULD hold" question, answered from evidence)

Measured today: 1:1 crops (960x540 of a 3840x2160 frame, a quarter of its width) of P(Doom) beside our proof rendered at 4K: `D:\work\aimv-lab\kc-engine\out\detail-1to1.jpg`. At 1:1 every P(Doom) crop carries layered detail; ours is vector-flat (uniform fills, one line weight, empty areas). The standard every frame meets, at 1:1 on a 4K screen:

1. **Few objects, rich objects.** Keep 4-7 objects per frame and one idea per frame (v6 failed with 12; Idi's "dead space" and "clutter" notes both stand). Detail lives inside objects and surfaces; the object count stays where it is.
2. **Every surface has a material.** Paper: fibre, print gain (ink spread at edges), density variation, registration marks. Screens and dark plates: a fine scan or phosphor texture, faint at 1080p, legible at 1:1. No flat fill anywhere at 1:1.
3. **Hatching follows form.** Shading in line art runs along the surface (parametric or contour coordinates on 3D, `engrave()` / `hatchD()`); one screen-space diagonal over everything (the proof's globe) is the failure case.
4. **A line hierarchy.** At least three weights (hairline, rule, stroke); nodes, ticks and end caps on lines; registration and crop marks where a document is shown.
5. **A micro-type layer.** Small mono annotations (values, coordinates, units, probabilities, footnotes) readable at 1:1 in 4K and invisible as noise at 1080p: rewards pausing, never competes with the lyric. Every annotation is either a true fact with a receipt or plainly the model's own voice.
6. **Depth and light.** Foreground and background separation (defocus, atmospheric falloff), rim light on 3D, glow cores with halos on signal only, halation, grain.
7. **Type scale at least 10x** in every frame (the proof reached 3.9-5.7x).
8. **Motion detail.** Secondary motion on every hit (settle, overshoot, flutter), motion blur from the engine's sub-frames (stacked copies stay banned).

Done-state for each frame: a 4K 1:1 crop sheet of the set-up, beside the matching P(Doom) crop, that a critic agent judges equal or better on items 2-6, plus the checks in section 6.

## 4. The plan

### Phase 0: the lead (this session's main agent), before any scene agent starts

1. **Detail kit** in `src/scenes/_kc.ts` and a new `src/scenes/_kc-glsl.ts`: paper material pass (fibre, print gain, registration), dark-plate material (scan texture), form-following hatch helpers, a micro-type helper (mono annotation with leader line and node), line-weight constants, a defocus layer helper. Scene agents use these; nobody re-invents them.
2. **Reference library**: P(Doom) 4K frames every 3 s plus 1:1 crops of 10 hero moments, and the same for the other four references at their native resolution, into `kc-engine\refs\` with a contact sheet. Agents compare against these.
3. **Timeline**: every entry of the bible's plate table in `src/timeline.ts`, with params for each visit; a placeholder scene so the full song renders end to end from day one.
4. **Checks at 4K**: `scripts/check.ts` gains `--scale 2`; add `scripts/detail.ts` (1:1 crop sheets of every set-up at 4K beside reference crops) and a type-scale check (largest and smallest drawn font size per frame from the box registry).
5. **Bible**: add section "Detail at 4K" (this section 3) to the treatment, so every agent reads one document.
6. Commit the engine to its own git repository (`git init` in `kc-engine`, first commit) so agents' work is diffable and revertible. Risk: the vault write guard blocked a shell line that mentioned `.git` on 10-17; if it blocks `git init` there, keep dated copies of `src\scenes\` per wave instead.

### Phase 1: scene agents in parallel

One agent per module group, at most 3 rendering at once (one heavy job at a time on this PC: BSOD history 2026-09-21; stills only, the lead renders every video):

| wave | agent | modules | window |
|---|---|---|---|
| A | chorus-board | `june` ×3 | 34.5, 86.9, 150.0 s |
| A | chorus-tune | `tune` ×3 | 37.5-50.2, 89.9-102.9, 154.0-167.4 s |
| A | chorus-hook | `cutoff` ×6, `spinning` ×3 | each "Knowledge cut-off", each "spinning" line |
| A | chorus-card | `turnedout` ×3 | 59.2, 111.2, 175.7-184.5 s |
| B | bookends | `session`, `outro` (one agent: the loop must close) | 0-9.5, 184.5-194.1 s |
| B | verse-1 | `letter`, `inferred`, `born` | 9.5-27.7 s |
| B | pre | `borrow` ×2 | 27.7-34.5, 80.5-86.9 s |
| B | verse-2 | `paced`, `extratime`, `jimothy` | 62.1-80.5 s |
| C | verse-3 | `algae`, `dlss` | 115.0-133.3 s |
| C | bridge | `younger`, `pages` | 133.3-150.0 s |
| every wave | critic (one per module, fresh context) | judges 4K crop sheets against references and the bible; lists defects; no code | |

Wave A first: the chorus modules fill 44% of the runtime (85 of 194 s) and the proof exists for them. Each wave ends with a contact sheet and a 1080p preview render for Idi (the gate); Idi's notes feed the next wave.

### Phase 2: the lead integrates

Transitions between plates (hard cuts on downbeats by default; carried moves where the bible names them), the full 4K 60 fps render (`--scale 2 --samples auto --shutter 0.2`, P(Doom)'s export settings), every check on the full song, colour tags, loop, the publish package (YouTube AI disclosure, "MiniMax-Music3" credit, MIT notice for the engine).

## 5. The agent brief (template; the lead fills in the module)

1. Read: the bible (whole), your plate paragraphs, section 3 of this handoff, `ENGINE.md`, `_kc.ts`, the proof's version of your module if one exists (`src/scenes/<id>.ts`: rebuild it, keep nothing by default), the reference crops.
2. Write only `src/scenes/<id>.ts` and `src/scenes/<id>-*.ts`. Engine or `_kc` changes: write the request into your report; the lead makes them.
3. Iterate with stills (`bash kc.sh stills <ids> <times> <dir>`), LOOK at them, then 4K 1:1 crops of every set-up.
4. Done when: `check.ts` green for your windows (sync, edge, title-safe, overlap, type scale), the critic's verdict on the 4K crops is "equal or better" on detail items 2-6, the bible's rules hold (one signal colour, "June" once per frame, no October before 184.5 s, no name before 175.7 s, facts only from the receipts table).
5. Report to `kc-engine\reports\<agent>.md`; return at most 10 lines to the lead (findings in files: three inline-return agents crashed a background session on 2026-09-06).

## 6. Checks (every render)

`check.ts`: per-word sync with negative control, frame edge, title-safe 96 px (logical), nothing over the lyric, type scale. Plus: SwiftShader vs Vulkan stills per module (PSNR > 40 dB), renderer string per launch, colour tags `yuv420p(tv, bt709)`, the loop (first and last frame the same picture), the spoiler grep, reading time for non-lyric text.

## 7. Known gotchas (each cost time on 10-17)

1. Shaders: no `fwidth`/`dFdx`/`dFdy` inside loops that can `break` (D3D11 breaks); `hatch()` leaves a half-coverage hairline at darkness 0 (gate it); integer hashes only (`sin` hashes break on Vulkan).
2. 2D layers are sRGB and top out at 1.0: glow goes on a second layer composited additively; set the glow layer's font explicitly (a `restore()` reverts the main one).
3. Bloom threshold is 1.0 so paper never glows: push signal above 1 for glow.
4. The beat grid's bar phase drifts: downbeats restart per section (`tools/build_data.py`).
5. Bun 1.4.3 recursive `mkdir` throws on existing relative paths (patched in `render.ts`); never edit `kc.sh` while it runs.
6. The worktree guard rejects compound shell lines and `$VAR` in ffmpeg commands: use `.sh` files; Git Bash paths in ffmpeg concat lists need `pwd -W`.
7. The vault write guard blocks shell lines that mention `.git` (even a `find -prune`); list files with Glob.

## 8. Files

| what | where |
|---|---|
| style bible | vault `projects/AIMV/knowledge-cutoff-treatment-2026-10-17.md` |
| proof report | vault `projects/AIMV/knowledge-cutoff-chorus1-proof-2026-10-17.md` |
| engine probes | vault `projects/AIMV/engine-probe-p1-2026-10-17.md`, `engine-probe-p2-2026-10-17.md` |
| engine | `D:\work\aimv-lab\kc-engine\` (`kc.sh`, `app\src\scenes\`, `app\scripts\check.ts`, `tools\`) |
| 1:1 detail evidence | `kc-engine\out\detail-1to1.jpg`, `out\detail\pd\` (P(Doom) 4K frames), `out\detail\kc\` (ours at 4K) |
| P(Doom) source (reference, read-only) | `D:\work\aimv-lab\refcode\pdoom-video\` (Windows launcher `app\scripts\render-win.ts`) |
| audit, flaws, rules ledger, reference dissections | `D:\work\aimv-lab\kc-video\critique\v5\`, `critique\v6\` |
| facts receipts | `D:\work\aimv-lab\after-cutoff-world.md`, `after-cutoff-tech.md` |
| timing | `kc-engine\data\lyrics.json`, `audio.json`, `pitch.json` |

## 9. First domino

Phase 0, items 1-3 (detail kit, reference library, full timeline with placeholders), then launch wave A. Report to Idi when wave A's contact sheets and 1080p preview of the three choruses exist.
