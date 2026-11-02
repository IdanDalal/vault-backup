---
type: project
created: 2026-11-02
author: jep
---

# kc-engine open-source audit (2026-11-02)

Scope: `D:\work\aimv-lab\kc-engine` at `9be094d` (main, 166 commits, no remote, working tree clean apart from ignored dirs). Read-only audit: nothing was changed, moved or committed.

## Verdict

- Publishable as a public GitHub repo after a clean export: a fresh repository without the current history, with the song audio removed, the song-derived data decided by Idi, internal reports dropped, licence files added.
- Publishing the current repo as-is: no. Blockers B1-B4 below.
- No secrets found: zero tokens, keys or passwords in tracked files (method and hits in section 6).

## 1. Size

| measure | value | receipt |
|---|---|---|
| tracked files | 388 | `git ls-files \| wc -l` |
| tracked bytes | 31,091,524 (31.1 MB) | `git ls-files -z \| xargs -0 du -cb` |
| history pack | 40.14 MiB (+4.50 MiB loose) | `git count-objects -vH` |
| working tree incl. ignored | 117 GB | `du -sh .` |
| ignored `out/` | 115 GB (renders, gates, panels, ref crops) | `du -sh out` |
| ignored `refs/` | 705 MB (frames of the 5 reference videos) | `du -sh refs`, `refs/INDEX.md` |
| ignored `bridge/` | 399 MB (`plates-review` KC stills) | `du -sh bridge` |
| ignored `app/node_modules/` | 128 MB | `du -sh app/node_modules` |
| estimated clean export | about 8.5 MB with song data kept; about 6.0 MB without it | sums below |

Largest tracked files (bytes):

| file | bytes | note |
|---|---|---|
| `audio/kc.mp3` | 4,631,923 | the KC song (MiniMax Music 3 take v8B, seed 3327) |
| `data/audio.json` | 2,280,224 | beat grid, sections, onsets, envelopes of the song |
| `data/audio.v1.json` | 2,269,801 | superseded analysis (rhythm pass 2026-10-18) |
| `app/src/scenes/pages-plates/spinning2_s2.jpg` | 420,209 | 54 jpgs, 13,633,332 bytes total: KC's own rendered frames, used only by `kitfx.ts:24` (mosaic demo) |
| `app/src/scenes/pages-plates/spinning1_s2.jpg` | 409,021 | same set |
| `app/public/fonts/Caveat-500.ttf` | 266,920 | fonts total 3,727,150 |
| `tools/Anybody-VF.ttf` | 201,352 | source variable font for `tools/make_fonts.py` |
| `reports/` (132 files) | 1,768,340 total | internal briefs, critics, rulings |
| `tools/__pycache__/` (4 pyc) | 119,073 total | compiled Python, carries abs paths |

History: only one file was ever deleted (`app/src/scenes/pages-plates/june1_s2.jpg`); no `refs/` or `out/` media ever entered history (largest historical blobs = the current list). History does hold `audio/kc.mp3`, every report, and 166 commit messages full of internal notes and Idi's name; authors `jep <jep@hq>` (107) and `jep <jep@localhost>` (59).

## 2. Blockers (must not publish as-is)

| # | item | why | paths |
|---|---|---|---|
| B1 | KC song audio | MiniMax-Music3 Community License grants rights on the "Software" (weights, code, config, docs); outputs are not defined or granted, output ownership is not addressed; the AUP (Exhibit A item 11) requires a clear machine-generated disclosure for public content. Redistribution of the mp3 as a file is neither granted nor forbidden by the licence text: ownership is unsettled, so it is Idi's ruling. Upstream P(Doom) also excludes its song from MIT. Recommendation: strip | `audio/kc.mp3`; licence notes `D:\work\AIMVs\ours\release\research\rights-rules.md:13-31`; byte identity `:38` |
| B2 | git history | contains B1 and B3 content and 166 commit messages with internal rulings; rewriting is heavier than a fresh export | `.git` (166 commits) |
| B3 | internal reports | 132 working reports: Idi's notes and rulings, abs paths (38 lines with `C:/Users/jep` across reports, tools and scripts), blind-panel results, descriptions of the 5 reference videos | `reports/` |
| B4 | missing licence files for shipped fonts | 5 EMS stroke fonts are OFL per their SVG metadata, with no OFL text shipped; 3 Hershey fonts carry a use restriction that requires acknowledgements distributed with the font data (present only inside the SVG metadata) | `app/public/fonts/stroke/EMS*.svg`, `app/public/fonts/stroke/Hershey*.svg` |

## 3. Decisions for Idi (publishable either way, each needs a ruling)

| # | item | facts | recommendation |
|---|---|---|---|
| D1 | song-derived data | `data/lyrics.json` (36,456 B, the full KC lyric), `data/pitch.json` (103,845 B, pYIN of the vocal stem), `data/audio.json`; the engine cannot boot without `data/audio.json` + `data/lyrics.json` (`app/src/engine/engine.ts:314`, `audio.ts:51`, `lyrics.ts:39`); `video` mode wires `audio/kc.mp3` (`app/scripts/render.ts:129`, `--noaudio` skips it) | A: keep data, licensed separately from MIT (upstream's model), plus the MiniMax-Music3 credit and a machine-generated statement. B: strip and ship a tiny synthetic demo song analysis. Recommend A: the scenes are lyric-bound, and without the data nothing renders |
| D2 | third-party market data | `data/globe-series.json` (42,689 B): series fetched from query2.finance.yahoo.com (S&P 500, Brent, gold, 10-year, BTC, EUR/USD), EIA, BLS, Open-Meteo, statisticstimes; used by `spinning.ts`. Provider terms not checked in this audit | replace with rounded hand-entered values citing sources, or strip and let `spinning.ts` draw placeholders; verify Yahoo terms before shipping the raw series |
| D3 | KC frames | `app/src/scenes/pages-plates/*.jpg` (54, 13.6 MB): KC renders, not third-party; only the `kit-fx` demo reads them | drop (cuts the repo from about 22 MB to 8.5 MB); the demo can render its tiles at boot |
| D4 | names in code comments | "Idi" in 152 lines across 75 files, "jep" in 73 lines across 61 files (design-ruling attributions such as "Idi's note 10") | keep as attribution, or scrub to "director"; recommend keep (no personal data beyond a first name) |
| D5 | quoted third-party text inside scenes | short verbatim social reactions (`app/src/scenes/jimothy.ts:41`), essay title and byline (`paced.ts`), real names (Messi, Torres, Dario Amodei, Deisseroth et al.) in lyric-bound plates | commentary scale; keep, add a "not affiliated" line in README (rights-rules section 6 safeguard) |
| D6 | local-tool scripts | `detail.sh`, `compare.sh`, `refcheck.sh` read local third-party video (`D:/work/AIMVs/I'm Upping My P(Doom).mp4`) or one-off dirs; `tools/qwen.py` targets a local llama-server; `tools/leap.py` runs under a ComfyUI embedded python | drop `compare.sh`, `detail.sh`; keep the rest with paths parametrised |

## 4. Fonts and licences

| asset | licence | shipped licence file | status |
|---|---|---|---|
| Anybody static instances (32 files `app/public/fonts/Anybody-w*-*.ttf`) | SIL OFL 1.1 (Copyright 2020 The Anybody Project Authors) | `app/public/fonts/licenses/anybody/OFL.txt` | OK. Instances are Modified Versions (fontTools instancer, `updateFontNames=False`, `tools/make_fonts.py:25`); no Reserved Font Name declared in the copyright line, so keeping the names is allowed |
| `tools/Anybody-VF.ttf` | OFL 1.1 | none beside it | gap: add `tools/OFL-Anybody.txt` or drop the file (build input only) |
| Caveat-500, JetBrainsMono-400/700, Newsreader o16/o60 400/600 + italic | OFL 1.1 | `app/public/fonts/licenses/{caveat,jetbrainsmono,newsreader}/OFL.txt` | OK |
| EMS Allure, Felix, Osmotron, Readability, Tech (`app/public/fonts/stroke/EMS*.svg`) | OFL per metadata ("Created by Sheldon B. Michaels", "SVG font conversion by Windell H. Oskay"; Allure a derivative of Allura, Rob Leuschke, TypeSETit) | none | B4: add `app/public/fonts/licenses/ems/OFL.txt` with the metadata credits |
| Hershey Sans 1, Script 1, Serif Med (`app/public/fonts/stroke/Hershey*.svg`) | Hershey use restriction: free use providing the acknowledgements (Dr. A. V. Hershey, U.S. National Bureau of Standards; format by James Hurt, Cognition, Inc.) are distributed with the font data, no NTIS format | inside the SVG metadata only | B4: add `app/public/fonts/licenses/hershey/NOTICE.txt` quoting the restriction |
| `app/src/engine/type.ts:5-9` comment | states "all SIL OFL 1.1, licences in public/fonts/licenses/" | - | accurate for the TTFs only |

## 5. MIT notice obligations (P(Doom) fork)

- Upstream: `D:\work\aimv-lab\refcode\pdoom-video` (origin `https://github.com/mexicat/pdoom-video.git`, head `fa164b7`), MIT, "Copyright (c) 2026 Giacomo Magnanini". Video: `https://www.youtube.com/watch?v=5EoO5413dBY` (upstream `README.md:5`).
- Obligation: the copyright notice and permission notice stay in all copies or substantial portions. Present today as `LICENSE-pdoom-engine.txt` (verbatim MIT text, 1,095 B). Keep it unchanged.
- Upstream code still in the fork: `app/src/engine/*` (engine, gl, post, hud `PDoom` class, lines, stroke, type, util), `app/scripts/render.ts` (header and modes, `plates` mode with P(Doom) figure ids `:324-339`), `app/src/main.ts`, `app/vite.config.ts`; comments credit upstream files (`_kc-camera.ts:8`, `_kc-rhythm.ts:4`).
- Upstream's README states its song and lyrics are outside MIT (`refcode/pdoom-video/README.md:98-100`); none of its song, lyrics or plates is in the fork (`audio/` holds only `kc.mp3`; `data/lyrics.json` is KC v8B-3327).
- Idi's own changes: add a top-level `LICENSE` (MIT) with Idi's own copyright line, keeping the upstream file beside it; or license the whole fork MIT with both copyright lines in one file.
- `docs/` is empty, while code points at `docs/TREATMENT.md` (`app/src/timeline.ts:1`, `palette.ts:3`, many scene headers); upstream had `docs/TREATMENT.md` and `docs/ENGINE.md`. Broken pointers only, no licence issue.

## 6. Secrets, paths, personal data

| check | result | method |
|---|---|---|
| key / token / secret / password / api / bearer / `sk-` / `ghp_` / `AKIA` | none. Every "token" hit is lyric or LLM-token content (`algae.ts`, `inferred.ts`, `outro.ts`, `session-chat.ts`, `borrow-chat.ts`); `reports/type-r123.md:131` "passwords" describes a ref frame | `git grep -i -E` over tracked text, pyc and fonts excluded |
| URLs in code | `http://localhost:5173`, `http://localhost:<port>` (`app/scripts/server.ts:22`), `http://127.0.0.1:8080/v1/chat/completions` (`tools/qwen.py:22`) | local only |
| email, phone, address | none (`idan`, `dalal`, `@gmail` zero hits) | `git grep` |
| absolute Windows paths | 83 tracked files (79 text + 4 pyc). Code: Edge path `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe` in 11 scripts (`app/scripts/{render,check,clarity,detail,errors,flips,inventory,lifecycle,q0-glass,shutter-audit}.ts`, `tools/type_probe.ts`); `D:/work/aimv-lab/...` and `/c/Users/jep/.bun/bin` in every root `.sh`; `D:/work/aimv-lab/ffmpeg.exe` in `app/scripts/detail.ts:19`; `tools/*.py` (avsync, build_data, build_pitch, camflow, leap, make_fonts, qstrip, strip, type_stills); 48 reports | `git grep -c -E '[A-Za-z]:[\\/](work\|Users\|Program)\|/c/Users\|/d/work'` |
| username `jep` in paths | 38 lines (`C:/Users/jep/...`, e.g. ComfyUI python in `tools/leap.py`, `tools/qwen.py:16`, bun bin in root scripts) | `git grep -E 'C:/Users/jep\|/c/Users/jep'` |
| tutoring or family data | none (`student`, `tutor`, `mom`, `dad` zero relevant hits) | `git grep` |
| git authorship | `jep <jep@hq>`, `jep <jep@localhost>` | `git log --format='%an <%ae>'` |

## 7. .gitignore gaps

Current `.gitignore`: `app/node_modules/`, `out/`, `refs/`, `*.log`, `bridge/`. `.gitattributes`: `* text=auto eol=lf`, binaries for ttf/mp3/png/jpg.

| gap | evidence | add |
|---|---|---|
| Python bytecode tracked | `tools/__pycache__/*.pyc` (4 files, abs paths inside) | `__pycache__/`, `*.pyc` |
| song audio | `audio/kc.mp3` tracked | `audio/*.mp3`, `audio/*.wav` (keep `audio/README.md`) |
| plates output of `render.ts plates` | writes `app/public/plates/` (`app/scripts/render.ts:328`) | `app/public/plates/` |
| Vite build output and caches | `vite build` writes `dist/`; vite cache under node_modules | `app/dist/`, `.vite/` |
| media anywhere | only extension rules in `.gitattributes`, no ignore | `*.mp4`, `*.mov`, `*.wav`, `*.aac`, `*.h264`, `*.npz` |
| local env and editor files | none tracked today | `.env*`, `.DS_Store`, `Thumbs.db`, `.vscode/` |
| render spool | lives in the OS temp dir (`render.ts:153`) | none needed |

## 8. Step list for a clean public repo (not performed)

1. Rulings from Idi first: D1 (song data), D2 (globe data), D3 (KC frames), D4 (names), the licence holder name for Idi's LICENSE line, the repo name.
2. Export the tree without history into a new folder, for example `D:\work\aimv-lab\kc-engine-public` (`git archive HEAD` from `D:\work\aimv-lab\kc-engine`, or a plain copy of tracked files). New `git init` there. Leave `D:\work\aimv-lab\kc-engine` untouched.
3. Strip from the export: `audio/kc.mp3`; `data/audio.v1.json`; `reports/` (all 132); `tools/__pycache__/`; `compare.sh`; `detail.sh`; `refcheck.sh` (or keep with a parametrised dir); per D2 `data/globe-series.json`; per D3 `app/src/scenes/pages-plates/` (then guard `app/src/scenes/kitfx.ts:24`); per D1 `data/lyrics.json`, `data/pitch.json`, `data/audio.json`, `data/asides.json`.
4. Fix `tools/Anybody-VF.ttf`: drop it, or add `tools/OFL-Anybody.txt` copied from `app/public/fonts/licenses/anybody/OFL.txt`.
5. Add font notices: `app/public/fonts/licenses/ems/OFL.txt` (OFL 1.1 text + EMS metadata credits: Sheldon B. Michaels, Windell H. Oskay, Allura by Rob Leuschke / TypeSETit); `app/public/fonts/licenses/hershey/NOTICE.txt` (the Hershey use restriction and both acknowledgements, quoted from `app/public/fonts/stroke/HersheySans1.svg` metadata).
6. Parametrise machine paths: Edge path via env (`KC_BROWSER`) with a Chrome fallback in the 11 scripts listed in section 6; root scripts use `$(dirname "$0")` for the engine root and `ffmpeg` on PATH in `kc.sh`, `lock.sh`, `render-full.sh`, `render-4k.sh`, `gates-full.sh`, `probe-full.sh`; `tools/*.py` take paths from argv or env (`tools/build_data.py`, `build_pitch.py`, `make_fonts.py`, `avsync.py`, `camflow.py`, `leap.py`, `qstrip.py`, `strip.py`, `type_stills.py`, `tools/strip-stills.sh`); `app/scripts/detail.ts:19`.
7. Remove `jep`-specific paths from comments (`tools/qwen.py:16`, `tools/leap.py` usage line); per D4 scrub or keep "Idi" attributions.
8. Update `.gitignore` with the section 7 lines.
9. Add `LICENSE` (MIT, Idi's copyright line, 2026) and keep `LICENSE-pdoom-engine.txt` unchanged at the root; add `"license": "MIT"` to `app/package.json` and pin `@types/bun` (currently `"latest"`).
10. Per D1 add `data/LICENSE-song-data.md` (or `audio/README.md`): the song "Knowledge Cutoff" and its lyrics and analysis are excluded from MIT, under a rights statement Idi rules (output ownership is unsettled per B1); the music is machine-generated with MiniMax-Music3 (credit text "MiniMax-Music3", rights-rules section 1).
11. Write `README.md`: what the engine is; credit "Engine forked from P(Doom) by Giacomo Magnanini" with `https://github.com/mexicat/pdoom-video` and `https://www.youtube.com/watch?v=5EoO5413dBY`; KC video `https://youtu.be/-g6hYVec1Uo`; inspirations R2-R5 by title (LGTM (Looks Good To Me), The Simulation's Ending, Run It Again, Ignore Previous Instructions) with links Idi supplies (no URLs for them exist on disk); requirements (bun, Edge or Chrome, ffmpeg with libx264, a GPU with Vulkan ANGLE); commands from `kc.sh` and `render-full.sh`; fonts credits; machine-generated music statement; "not affiliated with or endorsed by Anthropic" line.
12. Add `docs/ENGINE.md` from `engine-components.md` sections (a) and (f), or remove the `docs/TREATMENT.md` pointers; optional curated reports (for example `reports/rhythm-engine.md`, `type-engine.md`, `e0-depth.md`, `p2-camera.md`, `p2-look.md`, `p2-type-geo.md`, `p2-type-glyph.md`) after a path scrub.
13. Verify the export before the first push: `git grep -i -E 'key|token|secret|password|api'` reviewed; `git grep -E 'C:/Users|D:/work'` returns nothing; `bun install && bun scripts/render.ts stills --t 44 --only june1` renders on a second machine or a clean clone; `git ls-files -z | xargs -0 du -cb` near the 6.0-8.5 MB estimate.
14. Create the GitHub repo private first, push, review the file list in the web UI, then flip public.

Size sums used: 31,091,524 minus `audio/kc.mp3` 4,631,923, `data/audio.v1.json` 2,269,801, `pages-plates` 13,633,332, `reports` 1,768,340, `__pycache__` 119,073, `Anybody-VF.ttf` 201,352 = 8,467,703 B; minus `data/audio.json` 2,280,224, `lyrics.json` 36,456, `pitch.json` 103,845, `globe-series.json` 42,689 = 6,004,489 B.
