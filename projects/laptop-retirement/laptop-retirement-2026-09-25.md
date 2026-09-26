---
type: project
created: 2026-09-25
author: jep
status: active
---

# Laptop retirement: map + diff (2026-09-25)

Verdict: the laptop holds ~1 GB worth keeping. Most of it sits in ONE gitignored folder (`~/vault/inbox/CORPUS-June-2026`, 446 MB) that exists nowhere else jep can see. Everything else is disposable, a running service to switch over, or tutoring data that must not come here.

Method: 3 read-only agents. Laptop via `ssh laptop` (key `~/.ssh/laptop_ed25519`, user jep, `10.100.102.6` wired / `.11` Wi-Fi, same host key). Nothing written, moved or deleted on either machine. Full maps in this folder: [[laptop-inventory]] (live laptop), [[laptop-expected]] (what vault docs said it should hold, 77 rows), [[pc-inventory]] (this PC).

Blind spots: `D:\KEEP` and the other 17 D:\ root folders, plus `C:\Users\Idi`, deny jep. `D:\KEEP\NEXUS BACKUP` may already duplicate the laptop's Nexus copy. Unverified.

## 1. Diff: laptop vs PC

| item | laptop path | size | on PC? | action |
|---|---|---|---|---|
| Curtains (Nexus copy, most complete, 171 files) | `~/vault/inbox/CORPUS-June-2026/NEXUS BACKUP/projects/Curtains` | 1.2 M | no (vault has a 12 K stub; maybe in `D:\KEEP`) | copy, wave 1 |
| Curtains (Obsidian version, 162 files) | `CORPUS-June-2026/Vaults BACKUPS/Curtains` | 53 M | no / maybe `D:\KEEP` | copy, wave 1 |
| Curtains (older Nexus copy, 160 files) | `~/kitchen/_intake/raw/Sovereign-Nexus/projects/Curtains` | 1.2 M | no | subset of the 171-file copy; skip after diff |
| I4 "Triple Inception Theory" (21 files, 2 identical copies) | `NEXUS BACKUP/projects/I4` + `Sovereign-Nexus/projects/I4`, `data/i4-cycles` | 316 K | no | copy, wave 1 |
| Rest of Nexus repo (Idiverse, XCOM notes, ADRs 002-009, llama.cpp scripts, handoffs, docs) | `CORPUS-June-2026/NEXUS BACKUP` | 293 M | no / maybe `D:\KEEP` | copy, wave 1, **minus `.env`** |
| Old Obsidian vault backups (Idiverse, XCOM, DECADEnts 1-3) | `CORPUS-June-2026/Vaults BACKUPS` | 152 M | maybe `D:\KEEP\Vaults BACKUPS` | copy, wave 1 |
| Corpus maps | `CORPUS-June-2026/_CORPUS-MAP` | 824 K | no | copy, wave 1 |
| Sovereign-Nexus kitchen copy | `~/kitchen/_intake/raw/Sovereign-Nexus` | 7.8 G (5.9 G venvs, 2.2 K `.env`) | no | copy only files the CORPUS copy lacks; drop venvs + `.env` |
| Vault git history | `~/vault` main @ `1e8b4b5` (09-12) | 36 M `.git` | yes via GitHub | nothing; 0 unpushed commits |
| Vault untracked extras (SELF-MAX 15 M, SUPPLIES.jpg, K-GAMEPLAY/K-MENU png, MAGNA MOBSTA, Studio Preflight.html, P4C-research, parts-registry-draft) | `~/vault/inbox/` | ~26 M | check per file | copy, wave 1 (K-* screenshots: check for faces first) |
| Word World 3D workbench | `~/game3d` | 389 M (277 M screenshots, 57 M node_modules) | no | copy src + tools + island.html; screenshots after a face check |
| Render/probe scripts (Playwright) | `~/render-tools` | 19 M | no (PC uses headless Edge) | copy scripts only |
| Cron runner + crontab + settings | `~/bin/run-agent.sh`, `crontab -l`, `~/.claude/settings.json`, `settings.local.json` | <10 K | no | dump to text, wave 1 |
| Home CLAUDE.md, DESIGN.md, Vervaeke transcript .txt | `~/` | <1 M | CLAUDE.md adapted; others no | copy, wave 1 |
| Laptop memory (15 files) | `~/.claude/projects/-home-jep/memory/` | ~150 K | all 15 names exist on PC | diff by content; contains full student names, so diff in place, never commit |
| Session transcripts + jobs | `~/.claude/projects`, `~/.claude/jobs` | 540 M | no | leave; may hold student names |
| Tutoring data (sessions, drop, send, per-girl game copies, pre-purge bundle, blocklist) | `~/tutoring-data` | 291 M | no, **must stay no** | Idi's ruling (R1) |
| Name-guard pre-commit hook | `~/tutoring-data/tools/hooks/pre-commit` | small | no; PC commits run unguarded | Idi's ruling (R2) |
| Nexus secrets `.env` (Slack, n8n, SearXNG) ×2 copies | `NEXUS BACKUP/.env`, `Sovereign-Nexus/.env` | 2.2 K | no | never copy; revoke Slack tokens (R4) |
| Downloads: 2 voice memos (16 Jul), 2 phone photos (07-07, 08-13) | `~/Downloads` | small | no | Idi looks (R3) |
| Pixel rooting (factory zip, extracted image, Magisk) | `~/Downloads`, `~/root-work` | 8.5 G | no | discard |
| clonezilla.iso, Morphe zips, platform-tools | `~/Downloads`, `~/platform-tools` | 750 M | no | discard (re-downloadable) |
| snap, caches, npm, Docker hello-world, venvs | various | ~3 G | no | discard |

## 2. Services that die with the laptop

| service | schedule | PC replacement | switch order |
|---|---|---|---|
| autocommit + push to main | every 30 min | none yet (P3 write flip) | laptop OFF first, then PC on (two writers collide) |
| nightly snapshot tag | 00:00 | none yet | with autocommit |
| backup-health | every 6 h | none; its Syncthing check is broken (wrong unit) | retire or rewrite |
| morning digest | 09:00 daily | `daily/Today.md` replaced it 09-13 | retire on purpose |
| Sunday loop review | Sun 09:17 | none | Idi's call: port or retire |
| Telegram bridge `kitchen-telegram` | always on | GitSync captures already live at `D:\work\captures` | single-instance: laptop off before any PC bot |
| Syncthing | running, zero peers | n/a | nothing depends on it |
| restic | never ran (no env) | n/a | nothing |

The laptop was off 09-12 17:02 → 09-25 11:39, so these all paused for 13 days. They resumed at boot today.
 
## 3. Rulings for Idi

| #            | ruling                                                                                              | options                                                                                                                                                                                                                                         | jep recommends                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| R0 (DONE, A) | how to copy wave 1                                                                                  | A: copy CORPUS-June-2026 (minus `.env`) + small items (~500 MB) to `D:\work\laptop-archive\` now, dedupe vs `D:\KEEP` later. B: first give jep read on `D:\KEEP`, diff, copy only the missing. C: rsync the whole home minus exclusions (~2 GB) | **A**: under 1 GB, ends the single-disk risk today, touches nothing on the laptop |
| R1           | `~/tutoring-data` when the laptop goes                                                              | delete pass by Idi / new consent-gated home off this PC (USB drive) / laptop stays on as a data box                                                                                                                                             | ask after wave 1                                                                  |
| R2           | name-guard hook on the PC                                                                           | port hook code + blocklist to `C:\Users\jep\tutoring-data\` with locked permissions / retype names / no guard                                                                                                                                   | ask after wave 1                                                                  |
| R3           | `C:\tutoring-bakeoff` on THIS PC                                                                    | holds 4 phone photos (08-17), 1.3 G `lesson-transcripts`, `.wav`/`.m4a` audio, 4.9 G venv. Set up on purpose by the bakeoff README before the 08-30 no-raw-data rule                                                                            | Idi's delete call; jep has not opened it                                          |
| R4           | Nexus `.env` secrets + 2 embedded values (docker-compose `API_KEY=sk-...`, a JWT in a handoff note) | revoke Slack tokens and the `sk-` key, then delete the laptop `.env` copies                                                                                                                                                                     | revoke first                                                                      |

## 4. Wave 1 log

R0 ruled A by Idi 2026-09-25. Copied to `D:\work\laptop-archive\` (757 M), manifest `D:\work\laptop-archive\README.md`.

| copied | files | verified |
|---|---|---|
| `CORPUS-June-2026` (Curtains 171, I4 21) | 3,812 | count match with laptop, 0 `.env` |
| kitchen Nexus files absent from CORPUS (archived `.claude` config, voice-input-stt code) | 292 | count match |
| `game3d`, `render-tools`, `run-agent.sh`, CLAUDE.md, DESIGN.md, Vervaeke transcript | 1,507 | count match |
| crontab + kitchen-telegram unit | 2 | text dumps |

Secret scan (pattern grep, values masked): clean except 2 embedded old Nexus values, `NEXUS BACKUP/docker-compose.yml` (`API_KEY=sk-...`) and a JWT in `data/process/handoff-vault-processor-phase4-2026-01-15.md`. Added to R4.
Not copied: laptop `~/.claude/settings*.json` (PC write guard blocks commands naming that path). Laptop inbox has no other untracked files; the rest is on GitHub.
Laptop untouched: nothing deleted there.

Wave 1 excludes by rule: `.env`, `keyfile`, ssh keys, `.credentials.json`, `~/.config/kitchen/env`, telegram `.env`, anything under `tutoring-data`.

- 2026-09-26 17:30 HQ takeover step 6 receipt: first scheduled PC autocommit `4dd3923` pushed (log `ok`). Takeover `d80dce6`, merge `e539977`, manual proof `d3a8b28`. Tasks switched to Password logon by Idi 17:10 (Interactive never fired, S4U denied). Step 7 check due 2026-09-28 17:30: >= 90 ok lines, 2 tags, 0 laptop commits.
