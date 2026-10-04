---
type: audit
created: 2026-10-04
author: jep
---

# D:\work outside the vault - read-only audit (2026-10-04)

Scope: everything under `D:\work` except `D:\work\vault`. Nothing modified. Receipts: `ls`/`du`, sha1 overlap script (`tmp\overlap.py` -> `tmp\overlap.out`), secret classifier (`tmp\secscan.py` -> `tmp\secscan.out`, types and counts only, no values), `tmp\dups.txt`, vault audit log `.vault-config\audit\edits-pc-2026-09.jsonl`.

## Headline findings

1. Kid Studio: v7 IS LIVE. `index.html` == `index-v6.html` byte-identical, same mtime to 100 ns (2026-09-07 14:24:47.2037754, = `v6-build\v7.css` write time from `build_v7.py`); `index.html` has v7 markers (nunito x3, rainbow). The swap ran (`copy /y` keeps mtime). Nothing lost in the HTML.
2. Kid Studio `archive\` is GONE: deleted 2026-09-25 as manifest row D5 (vault `projects\tutoring-salvage\delete-manifest-2026-09-25.md`). Collateral: v5 and v6 backups (`archive\2026-09-07\index-v5.html`, `index-v6.html`) and `archive\server.v3.py` gone. `swap-v6.bat` undo path dead; `v6-build\build_v7.py` reads `archive\2026-09-07\index-v6.html` -> BROKEN, cannot rebuild v7. README line 36 + vault report `kidstudio-v6-build-2026-09-07.md` point at dead paths.
3. Kid data RE-ACCUMULATED after D5: `out\` recreated 09-28, then 2026-10-01 09:19-09:26 = 6 songs (D 5, K 1), 9 new allow words, `log\K.txt` + `log\D.txt` written. K/D chapter closed 09-25. Kid creations on the HQ PC again.
4. Laptop corpus: 291 MB of 424 MB is derived or re-downloadable (Linux llama.cpp binaries 104.6, Obsidian vector-index embeddings 105.5, plugin code 80.8). Real authored content ~100 MB, single disk, zero backup.
5. `Vaults BACKUPS\Curtains` holds NO notes: 53 MB = `.obsidian` (52 MB plugins) + 4 harness files. All Curtains content = `NEXUS BACKUP\projects\Curtains` (171 files, 0.6 MB). laptop-archive README pointer "(Obsidian version)" misleads.
6. Secrets: no `.env` file anywhere outside the vault (only `.env.example`, placeholder-shaped). Real-looking secrets in 5 files (paths below). README "embedded secrets" list incomplete.
7. `laptop-archive\README.md` stale: `home/` row says 1,507 files / 331 M with `game3d`; now 34 files / 365 K (game3d deleted by Idi 09-25, D6). `tutoring-kit\games-tools-report.md` also cites the dead `laptop-archive\home\game3d\` path; `tutoring-kit` now holds the only Word World source.

## Root loose files

| path | what | size | state | action | reason |
|---|---|---|---|---|---|
| `XCOM-archive-2026-09-11.zip` | 187 files removed from vault `projects\XCOM` 09-11 (character pools, csv sources), md5-verified entries | 5.6 MB | orphan-ish, SOLE COPY (source folder untracked by git, deletion permanent per `xcom-sitrep-2026-09-10.md` l.136-158) | MOVE `D:\work\archive\xcom\` (with manifest) | only recovery copy; root clutter for an agent reader |
| `XCOM-archive-2026-09-11_MANIFEST.txt` | md5 + size + path per zipped file | 20 KB | live companion | MOVE with zip | keeps the pair together |
| `XCOM-archive-2026-09-11_delete.py` | one-shot delete script, executed by Idi 09-11 (192 removed, 0 skipped) | 1 KB | spent | DELETE-CANDIDATE | logic + result recorded in `xcom-sitrep-2026-09-10.md`; rerun would no-op |
| `aml-settings-2026-09-28.json` | AML launcher settings snapshot, jep `cp` 09-28 14:04 (session d60d4ae0) | 3.8 MB | stale snapshot, unique (differs from live `settings.json` at char 1121420; size matches none of the 4 snapshots in `C:\XCOM2 AML 1.6.0-beta\`) | MOVE `D:\work\archive\xcom\` | no vault file cites it; snapshots belong together; live dir already has `.bak`, `.bak-2026-09-17-1405`, `.jep-2026-09-14`, `.BACKUP!!!!` |

## studio\kidstudio (live kids app, port 8787)

| path | what | size | state | action | reason |
|---|---|---|---|---|---|
| `venv\` | uv venv, CPython 3.12: torch 2.14, transformers 5.16, kokoro 0.9.4, misaki, spacy, imageio-ffmpeg | 1052 MB | live (start.bat runs `venv\Scripts\python.exe server.py`) | KEEP; write `requirements.lock` (uv pip freeze) first | NO requirements file exists (searched depth 2); README names only imageio-ffmpeg; not rebuildable from a recipe today; delete only if Studio retires |
| `index.html` | live page = v7 (Idi's 8 notes) | 0.12 MB | live | KEEP | sole v7 copy besides its twin |
| `index-v6.html` | byte-identical twin, served at `/v6` | 0.12 MB | superseded name | DELETE-CANDIDATE | twin = `index.html` (dups.txt + identical mtime); name says v6, content is v7 |
| `swap-v6.bat` | v5->v6 swap + backup to `archive\` | <1 KB | broken (undo target deleted) | DELETE-CANDIDATE | swap done; archive gone |
| `v6-build\build_v6.py`, `build_v7.py`, `v6.css`, `v7.css`, `fluid*.js`, `confetti`, `zzfx`, fonts | build scaffolding | 0.2 MB | broken (`build_v7.py` input deleted), v6.css superseded | RENAME `build\`; KEEP scripts as reference | only record of how v7 was assembled |
| `v6-build\shots\` | v3/v4/v7 screenshots incl. `s3-D-*`, `s4-K-*` | 8 MB | stale | ASK-IDI (with D5 question) | may show the girls' typed words |
| `static\` | baloo2, titanone, nunito, fluid licence | 0.09 MB | live | KEEP | baloo2/titanone/licence twins in `v6-build\` are the dups |
| `out\K`, `out\D`, `out\_tts` | girls' songs + json, TTS cache, written 10-01 | 15 MB | live, re-accumulated after D5 | ASK-IDI | D5 ruling said delete; contradiction with 10-01 use |
| `log\K.txt`, `log\D.txt`, `build.txt` | per-girl word logs, build log | 15 KB | live | ASK-IDI (same) | word logs = kid data |
| `log\*.png`, `server-test.out` | 09-06 dev screenshots | 3.1 MB | stale | DELETE-CANDIDATE | superseded by v7 shots; dev residue |
| `__pycache__\` | pyc (cp312 + cp314) | 16 KB | rebuildable | DELETE-CANDIDATE | regenerated on import |
| `pin.txt` | PIN for live word adds | 6 B | live, secret-ish | KEEP | path only; README says default `2468`, change it |
| `allow.txt` | allowed word list, edited 10-01 | 2 KB | live | KEEP | vault copy (`projects\kidstudio\allow.txt`, 1.9 KB) older |
| `README.md`, `server.py`, `gate.py`, `movie.py`, `start.bat`, `reset.bat`, `test_gate.py`, `workflows\` | app source | 0.06 MB | live; README cites dead `archive\` paths | KEEP; fix README | vault `projects\kidstudio\` mirror is a 09-07 10:45 snapshot (index 48 KB = pre-v6, server.py 35588 vs 36168 B) = SUPERSEDED mirror, refresh or mark stale |

## laptop-archive (sole copy, single disk, no backup)

| path | what | size | state | action | reason |
|---|---|---|---|---|---|
| `README.md` | wave-1 manifest | 3 KB | stale (home row, Curtains pointer, secrets list) | KEEP; fix 3 rows | agent readers trust it |
| `config\` | crontab + telegram unit dumps | 5 KB | reference | KEEP | tiny, laptop cron record |
| `home\` | laptop CLAUDE.md, DESIGN.md, run-agent.sh, render-tools, Vervaeke transcript | 0.37 MB | reference | KEEP | unique (overlap 0) |
| `kitchen-nexus-extras\` | Nexus files absent from NEXUS BACKUP; `.claude.archived` 1.6 MB is content-identical to `NEXUS BACKUP\.claude` | 2.5 MB | reference | KEEP; `.claude.archived` DELETE-CANDIDATE | sha1 twin in NEXUS BACKUP; `projects\voice-input-stt` 0.4 MB unique |
| `CORPUS-June-2026\_CORPUS-MAP\` | June map: REDUNDANCY-MANIFEST, canonical-set, echoes, forks list, strata | 0.4 MB | reference, unique | KEEP | names Vaults BACKUPS\Idiverse canonical, 8 forks |
| `NEXUS BACKUP\.bin\llama-b7519\` | Linux llama.cpp build b7519 | 104.6 MB | disposable | DELETE-CANDIDATE | Linux binaries, useless on Windows; ungated re-download ggml-org/llama.cpp releases |
| all `.obsidian\plugins\*\vector-index\` | ObsidianPrivateAI embeddings | 105.5 MB | derived | DELETE-CANDIDATE | regenerable from the notes |
| all plugin `main.js` / `styles.css` / `manifest.json` | Obsidian community plugin code | 80.8 MB | re-downloadable | DELETE-CANDIDATE | community store / GitHub releases; keep each `data.json` (settings) |
| `NEXUS BACKUP\projects\Idiverse\` (after strip) | Jan copy of Idiverse vault | 41.3 MB | echo | ASK-IDI (forks) then DELETE-CANDIDATE | 83.7 of 83.8 MB sha1-present in `Vaults BACKUPS\Idiverse`; unique = 8 forks + 5 obsidian state files |
| `NEXUS BACKUP\data\inbox\` | images (MacriumReflect, CLONEZILLA, AQAL, DONE.png x3 internal), LOG 7.8 MB, transcripts 7 MB, MadVR | 33.1 MB | reference, 29 MB unique | KEEP | authored/collected material |
| `NEXUS BACKUP` rest (`data\` other, `kernel`, `nexus`, `docs`, `scripts`, `vault\TELOS`, `vault\atomic_notes`, `projects\Curtains`, `I4`, `XCOM`, `investment-research-system`) | Sovereign Nexus repo, Jan 2026 | ~15 MB | reference, unique | KEEP | Curtains + I4 + Nexus-original live only here |
| `Vaults BACKUPS\Idiverse` | Idiverse vault, canonical per June map | 83.9 MB (~42 after strip) | reference | KEEP | canonical source |
| `Vaults BACKUPS\Curtains` | `.obsidian` + `.harness` + `.claude\settings.local.json` only, zero notes | 54.6 MB (0.4 after strip) | config shell | KEEP stripped | harness rules unique; notes live in NEXUS copy |
| `Vaults BACKUPS\TemporarilyTitleless`, `Espionage Inc` | Midjourney persona / humor business | 7.3 MB | reference, 6.1 MB unique | KEEP | only copy |
| `Vaults BACKUPS\XCOM` | old XCOM vault (pools, VIPs, name mods) | 6.9 MB | reference, 6.5 MB unique | KEEP | one file twins `vault\projects\XCOM\XCOM VAULT\Name Mods\XComGame.txt` |
| `Vaults BACKUPS\jep`, `Music` | jep notes layer, 1 mp3 + 2 lyric txt | 2.5 MB | reference | KEEP | mostly unique |
| `.pytest_cache`, `.docker_cleaned`, `.vscode` | residue | ~0 | disposable | DELETE-CANDIDATE | regenerable |

### Overlap: NEXUS BACKUP vs Vaults BACKUPS (sha1, per subfolder)

| subfolder | NEXUS MB (unique) | Vaults MB (unique) | keep | unique to the other copy |
|---|---|---|---|---|
| Idiverse | 83.8 (0.2) | 83.9 (0.1) | `Vaults BACKUPS\Idiverse` | NEXUS: 8 forked notes (GOALS, jep, PC Formatting Guide, Pillars 1, Prompts, Current Active Video Game, Video Game Backlog, The Telescope The Sun And The Flame) + 5 obsidian state files. Vaults: same 8 in other versions + ADR-003, DLEKG_Analysis_Table, Modern Robin Hood Film Trilogy Idea, PERMISSIONS |
| `.obsidian` (NEXUS root) vs vault plugins | 40.4 (23.7) | n/a | strip both to `data.json` | plugin code 16.7 MB shared |
| Curtains | 0.6 notes (0.6) | 54.6 config (38.1) | BOTH, Vaults one stripped | NEXUS = all notes; Vaults = harness + plugin settings |
| XCOM | 4.8 (4.4) | 6.9 (6.5) | BOTH | different eras, 0.4 MB shared |
| TemporarilyTitleless | none | 7.2 (6.0) | Vaults | 1.2 MB echoed in NEXUS `data\` |
| data\inbox, data\archive | 37.7 (31.5) | n/a | NEXUS | 6.2 MB shared with Vaults images |
| I4, investment-research-system, kernel, nexus, TELOS, atomic_notes | all unique | none | NEXUS | atomic_notes = derived re-mining of Idiverse (June map) |
| totals | 280.0 (171.5) | 155.2 (52.8) | | distinct content across laptop-archive 306.9 of 438.2 MB |

### Secrets (paths only, no values printed)

| path | type | note |
|---|---|---|
| `NEXUS BACKUP\config\google-service-account.json` | PRIVATE KEY block | NOT in README list; revoke in Google Cloud (R4) |
| `NEXUS BACKUP\projects\investment-research-system\specs\2025-12-28-system-configuration\tasks.md` | JWT (207 chars) | NOT in README list; likely the n8n JWT |
| `NEXUS BACKUP\docker-compose.yml` | `API_KEY=sk-...` | in README list |
| `NEXUS BACKUP\projects\Idiverse\.obsidian\plugins\obsidian-local-rest-api\data.json` + Vaults twin | private key + API key of local REST plugin | low risk (localhost self-signed), still a key |
| `NEXUS BACKUP\config\searxng\settings.yml` | `secret_key` + passwords | unverified whether default placeholder |
| `NEXUS BACKUP\nexus\services\heartbeat\config.py` | token assignment | unverified real vs placeholder |
| `NEXUS BACKUP\data\process\handoff-vault-processor-phase4-2026-01-15.md` | README says JWT; scan found only `TOKEN=x...` placeholder shapes | README claim unconfirmed |
| `.env` | none found anywhere outside vault | `.env.example` only, placeholder-shaped |
| false positives | `kernel\cache.json`, `kernel\graph.json`, `_CORPUS-MAP\canonical-set.txt` (`sk-conv...` = filename), `autounattend.xml` (`PublicKeyToken`), plugin `main.js` | ignore |

Slack `xox` tokens: 0 hits. Telegram bot tokens: 0 hits. GitHub/AWS/Google API keys: 0 hits.

## screens\ (Idi's drop/reference folder)

| path | what | size | state | action | reason |
|---|---|---|---|---|---|
| `DASHBOARD.mp4` | Fuselab Dribbble motion reference for Cash Console v2 | 18.6 MB | stale (v2/v3/v4 shipped) | ASK-IDI | third-party clip, no further vault use after `console-v2-2026-09-11.md` |
| `9GAG\` | 87 memes (`media\`, index.csv), export html, `fetch_counts.js`, GhostOfTsushima.png | 24 MB | live W evidence (wins-jar row 3, telos creations) | KEEP; RENAME `D:\work\exports\9gag\` | sole local copy; "screens" misnames an export |
| `Poker\` | WhatsApp group export 3 MB txt + 6 jpg + `poker_recaps_index.md` | 4 MB | live W evidence (94 recaps) | KEEP; RENAME `D:\work\exports\poker\` | holds other people's messages: private, never into vault git |
| `BIOS\` | empty since 09-21 | 0 | orphan | DELETE-CANDIDATE | BIOS photos live in vault `projects\pc-bios\` |
| `XCOM\`, `one-zero\` | empty, created today 10:18 | 0 | fresh drop targets | KEEP | likely staged this morning |

## Other areas

| path | what | size | state | action | reason |
|---|---|---|---|---|---|
| `captures\` | git repo `IdanDalal/vault-captures`, phone GitSync; root has `2026-09-19.md`, README | 136 KB | live, quiet: last commit 09-19 11:38, clean, = origin/main as last fetched | KEEP | no phone capture in 15 days; daily-note skill pulls before each run |
| `tutoring-kit\` | Word World + Game Lab templates (html+png), patch, 3 generic tools, PIPELINE.md, report | 2.9 MB | live salvage, NO BACKUP (outside git) | MOVE text files into vault `projects\tutoring-salvage\kit\`; MERGE `tools\PIPELINE.md` with vault `projects\tutoring-salvage\PIPELINE.md` (dups.txt twins) | game3d source gone (D6), template = only Word World copy; fix report's dead game3d path |
| `drop\reddit\` | empty, created 09-27 | 0 | drop target (Reddit saved-page route) | KEEP | Reddit 403s anonymously; this is the planned intake |

## No backup today

- `laptop-archive\` whole (~100 MB authored: Curtains, I4, Nexus, Idiverse, TemporarilyTitleless, XCOM vault): one disk, not git, not restic.
- `tutoring-kit\` (only Word World template).
- `XCOM-archive-2026-09-11.zip` (only copy of 187 pool files).
- `screens\9GAG`, `screens\Poker` (W evidence; 9GAG media also on 9GAG CDN).
- Kid Studio v7 (`index.html` + twin, same disk), `allow.txt`, v6-build scripts.
- `captures\` is backed by GitHub.

## Questions for Idi

1. Kid Studio ran on 2026-10-01 (6 songs, 9 new words for K and D) after the 09-25 D5 delete. Keep the girls' new creations, or delete them again (A keep, B delete; jep recommends B if K/D chapter stays closed, A if the Studio continues at home)?
2. The 8 forked Idiverse notes (list above): keep the Vaults BACKUPS versions as canonical and drop the NEXUS copy, or keep both versions side by side (jep recommends both side by side in a `_forks\` folder, then drop the NEXUS Idiverse copy, 41 MB)?
3. Strip the laptop corpus of derived files (Linux llama binaries, embeddings, plugin code, 291 MB), then back up the remaining ~100 MB to a private GitHub repo or a second disk (jep recommends strip + private repo)?
4. `DASHBOARD.mp4` (Cash Console motion reference, 18.6 MB): delete, or keep for a v5 skin?
5. Kid Studio: retire it (frees the 1 GB venv) or keep it running for home use?

## Totals

- Safe now (disposable or proven twin): 291 MB corpus derived (104.6 + 105.5 + 80.8) + 3.1 log pngs + 1.6 `.claude.archived` + 0.13 `index-v6.html` + pycache/delete.py/swap bat ~0 = **~296 MB**.
- Needs ruling: venv 1052 MB (Q5, after requirements.lock) + NEXUS Idiverse copy 41.3 MB (Q2) + DASHBOARD.mp4 18.6 MB (Q4) + kid `out\` 15 MB + `v6-build\shots` 8 MB (Q1) + aml snapshot 3.8 MB = **~1139 MB**.
- Area sizes: studio 1.1 GB (venv 96 %), laptop-archive 425 MB, screens 46 MB, root files 9.4 MB, tutoring-kit 2.9 MB, captures 0.1 MB, drop 0.
