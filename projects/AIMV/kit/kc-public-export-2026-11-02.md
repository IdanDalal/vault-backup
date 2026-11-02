---
type: report
created: 2026-11-02
author: Agent kc-export
---

# kc-engine public export: `knowledge-cutoff` (2026-11-02)

## Verdict

- DONE, local only. `D:\work\aimv-lab\knowledge-cutoff-public` holds one commit `d76d979` (author and committer `Chorus of Minds <chorusofminds@users.noreply.github.com>`), 204 tracked files, 13,293,513 bytes, no remote, nothing pushed.
- Source `D:\work\aimv-lab\kc-engine` untouched: HEAD `9be094d` before and after; `git status --porcelain --ignored` byte-identical before and after (`cmp`).
- Path grep `git grep -n -i -E 'C:/Users|D:/work|/c/Users|jep@|@gmail'` returns nothing. Secrets grep returns nothing.
- Stills render from the export (june1 36.0, spinning1 54.5, spinning2 107.5, kit-fx 41.0, all real frames, zero scene errors). `tools/new-video.sh` births a repo that installs, typechecks and renders its stub plate.

## 1. Rulings applied

| ruling | applied as | path |
|---|---|---|
| mp3 ships | `audio/kc.mp3` tracked (`!audio/kc.mp3` exception in `.gitignore`); `audio/LICENSE.md` = rights file section 6 text, `<HOLDER>` and `<CHANNEL>` = Chorus of Minds | `audio/` |
| D1 option A | `data/lyrics.json`, `audio.json`, `pitch.json`, `asides.json` ship under `audio/LICENSE.md`; `data/audio.v1.json` dropped | `data/` |
| MIT holder | `LICENSE` = MIT, "Copyright (c) 2026 Chorus of Minds"; `LICENSE-pdoom-engine.txt` unchanged (equals the source blob; equals upstream `refcode/pdoom-video/LICENSE` modulo CRLF) | root |
| D2 | option 1 (keeps the scene rendering): `data/globe-series.json` replaced by hand-entered rounded month-end values (Jun 30, Jul 31, Aug 31, Sep 30, latest) for the 6 series `spinning.ts` reads, each with a source line; raw Yahoo/EIA/BLS/Open-Meteo series, CPI, NYC temperature, EUR/USD and the `source_url` API links gone. Same JSON shape, so `spinning.ts` is unchanged apart from one comment. Effect: the visit-1 ticker rolls through 5 values instead of about 100 daily closes, so `spinning` frames differ slightly from the published video (README says so) | `data/globe-series.json`, `app/src/scenes/spinning.ts:9` |
| D3 | `app/src/scenes/pages-plates/` (54 jpg, 13.6 MB) dropped; `kitfx.ts` paints 24 stand-in tiles at boot (`standInTiles()`) when the glob finds no jpg | `app/src/scenes/kitfx.ts` |
| D4 | "Idi" / "jep" attributions kept; `docs/ENGINE.md` says who they are | code comments |
| D5 | quoted text kept; README line "Not affiliated with or endorsed by Anthropic, MiniMax or any company named." | `README.md` |
| D6 | `compare.sh`, `detail.sh` dropped; `refcheck.sh` kept, parametrised (`[dir]` arg, default `out/ref`; `FFMPEG`); `tools/qwen.py` URL from `KC_LLM_URL`; `tools/leap.py` ffmpeg from `FFMPEG`, usage line generic | root, `tools/` |
| name | `knowledge-cutoff`, folder `knowledge-cutoff-public` (did not exist before the run) | |

## 2. What changed (export vs source tree at `9be094d`)

| step | change |
|---|---|
| strip | removed `reports/` (132), `tools/__pycache__/` (4 pyc), `compare.sh`, `detail.sh`, `data/audio.v1.json`, `app/src/scenes/pages-plates/` |
| fonts | `tools/OFL-Anybody.txt` (copy of the Anybody OFL, `tools/Anybody-VF.ttf` kept as `make_fonts.py` input); `app/public/fonts/licenses/ems/OFL.txt` (each EMS file's metadata credits quoted + full OFL 1.1 text); `app/public/fonts/licenses/hershey/NOTICE.txt` (font list, Oskay/McGuire provenance, the use restriction quoted verbatim; checked identical in all 3 Hershey SVGs) |
| browser | `browserPath()` added to `app/scripts/server.ts`: `KC_BROWSER`, else Edge (x86, x64), Chrome (x64, x86, per-user) on Windows, Edge/Chrome app bundles on macOS, `/usr/bin` Edge/Chrome/Chromium on Linux, else playwright's own Chromium. Used by the 10 scripts with the hardcoded Edge path (`check`, `clarity`, `detail`, `errors`, `flips`, `inventory`, `lifecycle`, `q0-glass`, `render`, `shutter-audit`) and `tools/type_probe.ts` |
| root scripts | `kc.sh`, `lock.sh`, `gates-full.sh`, `probe-full.sh`, `render-full.sh`, `render-4k.sh`, `refcheck.sh`, `tools/strip-stills.sh`: root from `$(dirname "$0")`; bun from PATH (`BUN_INSTALL` optional); ffmpeg from PATH or `FFMPEG`; Python from `KC_PYTHON`; `out/` created if missing; `kc.sh` prints usage on an unknown verb; the `^D:` output filter in `kc.sh stills` removed |
| ffmpeg in TS | `app/scripts/detail.ts` `FF = process.env.FFMPEG ?? 'ffmpeg'` |
| Python tools | `avsync.py` (engine root from `__file__`; `FFMPEG`, `KC_TMP` default OS temp, `KC_STEMS`, `KC_REFS`, `KC_MP4`, `KC_AVSYNC_OUT`), `build_data.py` (argv: timing json, drums json, drum stem, vocal stem, [mp3], [out dir]), `build_pitch.py` (argv: vocal stem, [lyrics], [out]), `make_fonts.py` (argv: out dir, [source font dir]), `camflow.py`, `leap.py`, `qstrip.py`, `strip.py`, `type_stills.py` (`FFMPEG`), `qwen.py` (`KC_LLM_URL`), usage lines in `pixeq*.py` |
| comments | private-path pointers fixed: `timeline.ts:1` (named a vault path), `palette.ts:3`, `_kc.ts:1`, `post.ts:61`, `build_data.py` headers; `docs/TREATMENT.md` pointers now point at `docs/ENGINE.md`, which explains `TREATMENT n.n`, `reports/...`, handoff and agent-name citations as unshipped production notes |
| .gitignore | audit section 7 lines added (`app/dist/`, `.vite/`, `app/public/plates/`, `__pycache__/`, `*.pyc`, media, `.env*`, editor files); `audio/*.mp3` ignored with `!audio/kc.mp3` |
| package | `app/package.json` `"license": "MIT"`; `@types/bun` pinned `1.4.2` (installed version, from the source's `node_modules/@types/bun/package.json` and `bun.lock`); `bun.lock` workspace line updated to match |
| new files | `LICENSE`, `README.md`, `LINEAGE.md`, `docs/ENGINE.md`, `audio/LICENSE.md`, `tools/new-video.sh`, the 3 font licence files |

## 3. New docs

| file | holds |
|---|---|
| `README.md` | what it is, video link, requirements table, quick start (`kc.sh` verbs, whole-song renders), environment variables, layout, new-video step, "How it was made" (Idi: premise, lyric selection and edits, every ruling, final calls; Claude Code agents: engine, scenes, gates, render scripts via briefs, blind panels, gates, fix rounds), machine-generated music statement + "Credit: MiniMax-Music3", credit chain (P(Doom) code + video + its song credits; all 10 other references with URLs from `kit-references.md`), font credits, ticker data note, licence section. No private paths, no email |
| `LINEAGE.md` | table row: parent `mexicat/pdoom-video` `fa164b7` -> `knowledge-cutoff` = export of kc-engine `9be094d` (full sha), 2026-11-02; section "Changes in knowledge-cutoff" with 10 bullets from `kit-engine-components.md` |
| `docs/ENGINE.md` | `kit-engine-components.md` sections (a) and (f), private receipts removed, pointers relative; plus the comment-citation key |

## 4. `tools/new-video.sh <name> <dest>`

| does | detail |
|---|---|
| copy | `git ls-files --cached --others --exclude-standard` piped through tar, so ignored `out/`, `node_modules/` never travel |
| strip | `audio/*.mp3`, `*.wav`, `audio/LICENSE.md`, `data/lyrics.json`, `audio.json`, `pitch.json`, `asides.json`, `globe-series.json`; `data/*-allowed.json` reset to `[]` |
| lyric-bound scenes | modules named in `timeline.ts` plan rows (18) plus `<module>-*.ts`, minus the transitive import closure of every kept scene (bash fixpoint over `from './x'`); KC run removes 44 files, keeps the `_kc-*` kits, `kit*` demos, `placeholder`, `letter-shared`, `open-grains`, `verse-a-kit`, `verse-b-kit`, `hook-aside` |
| stubs | `lyrics.json` (no lines), `audio.json` (30 s, 120 BPM grid, one section), `pitch.json`, `asides.json`, `notes.json` `[]`; `timeline.ts` with an empty plan that falls back to one `blank` placeholder entry over the song (render.ts refuses a boot with zero loaded entries, so a fully empty edit cannot render a frame) |
| renames | `audio/kc.mp3` -> `audio/song.mp3` in `render.ts` and `main.ts`; `.gitignore` drops the mp3 exception (no audio ships until its rights are ruled) |
| docs | README (status, 5 next steps incl. the song constants to edit), PROCESS (phase headings + rulings table), LINEAGE (parent table + new row naming this repo and its commit + empty "Changes in <name>"), `cards/README.md` (line-card field layers) |
| git | `git init -b main`, no commit |

Test (into `C:\Users\jep\.claude\jobs\99182c36\tmp\newvideo-test\`, re-run after the commit): `bash tools/new-video.sh test-video <dir>` -> "parent knowledge-cutoff @ d76d979; removed 44 lyric-bound scene files"; LINEAGE row `| knowledge-cutoff | d76d979 | test-video ... |`; `bun install` exit 0; `bunx tsc --noEmit -p tsconfig.json` exit 0 (first run); `BUN_INSTALL=... bash kc.sh stills blank 1.0 first-look` -> `out/first-look/f_0001.00.png` (2,089,584 B), the placeholder plate "BLANK", window 0.00-31.50 s, viewed.

## 5. Verification (audit step 13)

| check | command | result |
|---|---|---|
| source untouched | `git -C kc-engine status --porcelain=v1 --ignored` before/after, `cmp` | identical; HEAD `9be094d` both times |
| private paths | `git grep -n -i -E 'C:/Users\|D:/work\|/c/Users\|jep@\|@gmail'` | 0 hits (exit 1) |
| wider names/paths | `git grep -i -E 'idan\|dalal\|/d/work\|aimv-lab\|AIMVs\|vault'` | 0 hits |
| secrets | `git grep -i -E 'api[_-]?key\|secret\|password\|bearer\|token=\|sk-...\|ghp_\|AKIA\|BEGIN ... KEY'` (data excluded) | 0 hits; `token(s)` hits are lyric/LLM-token content in 11 scene files, as in the audit |
| mp3 metadata | ID3 tag (8,251 B) scanned for jep, Users, drive paths, Idi, email | none; it holds the ComfyUI workflow (`minimax_music3_dit_fp16.safetensors`, prompt, `filename_prefix audio/kc_3327`). 5 case-insensitive "jep" byte runs sit in audio frames (offsets 1.46 M to 4.39 M), random data |
| size | `git ls-files -z \| xargs -0 du -cb` | 13,293,513 B (204 files), near the 13 MB plan figure |
| install | `bun install` in `app/` | exit 0, 32 packages, `bun.lock` unchanged apart from the pin |
| typecheck | `bunx tsc --noEmit -p tsconfig.json` | exit 0 |
| typecheck scripts | `bunx tsc --noEmit -p tsconfig.scripts.json` | 2 errors, `scripts/check.ts:178` strict-null, inherited (line untouched) |
| still (render.ts) | `bun scripts/render.ts stills --only june1,spinning1 --t 36,54.5`; `--only spinning2 --t 107.5`; `--only kit-fx --t 41` | exit 0, RENDERER ANGLE Vulkan RTX 4090, 0 scene errors; frames viewed: JUNE split-flap board, KEPT + engraved globe, KEEPS + globe, mosaic BE from 281 stand-in tiles |
| still (driver) | `BUN_INSTALL=... bash kc.sh stills june1 36.0 kcsh-test` | `out/kcsh-test/f_0036.00.png` written |
| shell syntax | `bash -n` on 9 scripts | all pass |
| Python syntax | `ast.parse` on 19 `tools/*.py` | all parse |
| GPU idle before renders | `nvidia-smi` | 0-7 % utilisation; no `llama-server`, no `ffmpeg` running |
| commit | `git log` | 1 commit `d76d979`, author = committer = Chorus of Minds noreply; `git remote -v` empty |

Logs: `C:\Users\jep\.claude\jobs\99182c36\tmp\export\` (`still*.log`, `tsc*.log`, `nv-*.log`, `src-status-*.txt`, the two edit scripts).

## 6. Not done

| item | why |
|---|---|
| push, remote, GitHub org | out of scope (plan steps 5, 7, 8) |
| `bash kc.sh tsc` through the driver | the session's command checker refused `bash kc.sh tsc` with redirects; the same `bunx tsc` ran directly |
| whole-video render, gates, `probe-full.sh`, `gates-full.sh`, avsync | not asked; ffmpeg is not on this machine's PATH, so ffmpeg-dependent paths were not exercised (`FFMPEG` env not tested end to end) |
| Python tools run | parsed only; their inputs (stems, timing json, reference videos) are not shipped |
| clean-clone render on a second machine | audit step 13 suggestion; this machine only (export folder, fresh `bun install`) |
| Linux/macOS browser fallbacks | written, untested (Windows only) |
| optional curated reports (audit step 12) | not requested |

## 7. Open issues

1. Commit message ends with the `Co-Authored-By: Claude Opus 5.5` and `Claude-Session: https://claude.ai/code/session_...` lines (session attribution rule). The session link is a private claude.ai URL; if it should not be public, amend before the first push (one-command amend; the repo has one commit).
2. Every boot logs one `404 (Not Found)` console error. Pre-existing: the source's `out/full7b/render.log` and `out/final4k/render.log` show the same line. A response probe saw no failed request from the page (likely the browser's favicon fetch). Harmless to renders.
3. The brief's still example `--t 44 --only june1` lands outside june1's window (34.35-37.35 s, read from `__pdoom.timeline`) and renders the red not-loaded plate; 36.0 is the correct june1 time. The same example sits in audit step 13 and `kit-engine-components.md` (e) `kc.sh` row.
4. D2 values are my rounding of the series already on disk (fetched 2026-10-18), month-end picks: S&P 7499/7490/7686/7652/7659, Brent 72.9/90.1/90.5/103.5/109.9, gold 4040/4110/4480/4190/4180, UST10Y 4.42/4.75/4.76/5.29/5.10, BTC 58,600/62,800/78,500/83,600/82,000, gas 3.83/4.10/4.07/4.47/4.33. Not re-checked against the live sources. Yahoo's terms still unread (audit D2); five rounded points per series is a small factual table, not the series.
5. `new-video.sh` removes kit files named after a plate (`paced-kit`, `younger-kit`, `tune-cam`, `tune-data`, `cutoff-cam`, `cutoff-heap`, `session-chat`, `session-space`, `letter-desk`) that `kit-engine-components.md` marks REUSE/ADAPT; they stay in the parent and can be copied back by hand. Kit demos stay but do not load in a child (stub timeline has no demo block; the demos read KC lyric lines).
6. Song constants survive into a child (161.5 BPM in `_kc.ts`/`_kc-rhythm.ts`, KC section names, ruled quiet windows, `STRESS_OVERRIDES`, `194.1` in the root scripts); the child README lists them as next step 3.
7. Comments still cite unshipped notes: 50 files mention `reports/`, 21 lines `TREATMENT n.n`, several "handoff" and agent names. No private paths among them; `docs/ENGINE.md` explains the citations. A scrub to plain wording is optional.
8. README credit chain carries the `kit-references.md` pre-publish checks forward: re-open each URL logged out, channel names can change (Regenerate), Count Me In's creator is medium confidence.
9. `scripts/check.ts:178` strict-null typecheck errors (inherited); listed in `docs/ENGINE.md` (f).
