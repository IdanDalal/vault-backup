---
type: inventory
created: 2026-09-25
author: jep
---

# PC inventory (HQ, Windows 11), 2026-09-25

Read-only scan as user `jep`. Sizes from `du -sh` (Git Bash), file counts from `find -type f`. "denied" = `jep` has no read access, so size and contents are unknown to this scan.

## FLAGS (read first)

1. **POLICY VIOLATION, probable raw tutoring data: `C:\tutoring-bakeoff` (6.4G).** Its name is not `tutoring-data`, so it escaped the literal check. Top level holds 4 phone photos (`PXL_20260817_*.RAW-01.COVER.jpg`, ~31 MB, dated 2026-08-17), `lesson\` (57M, 1 file), `lesson-transcripts\` (1.3G, 19 files), `clips\` (6.8M, 5 files). File types across clips/lesson/lesson-transcripts: 9 .wav, 6 .m4a, 9 .md, 1 .txt. That is audio plus transcripts, and CLAUDE.md forbids both on this machine. Nothing was opened, moved or deleted. Rest: `venv\` 4.9G (47,091 files), `results\` 35M, `results-vad\` 35M, `bakeoff.py`, `lesson-transcribe.py`, `README.md`. Looks like the Whisper transcription bakeoff, run on real lesson audio.
2. `tutoring-data` itself: **not found** under D:\, C:\Users (readable parts), or C:\ root.
3. `C:\Users\Idi` = **denied** to jep. The owner's own profile (Desktop, Documents, Downloads, any laptop copies, probably ComfyUI Desktop) is invisible to this scan. It needs a second pass as Idi.
4. D:\ root user folders are all **denied** to jep (18 folders, sizes read 0). Only D:\work is readable. Drive-level totals are the only numbers available.
5. ComfyUI: **no folder found** on C:\ (depth 5, outside AppData/Games/Windows), E:\ or F:\ (depth 3), D:\work, C:\Users\jep. The only trace is `C:\ProgramData\NVIDIA Corporation\NVIDIA App\UXD\Log.Comfy Desktop.exe.log`, which points to ComfyUI Desktop, most likely installed inside `C:\Users\Idi` (denied).
6. Staging/backup candidates: `G:\Backup\2026-08-29\` (613M, Desktop/Documents/Pictures, a Windows-profile backup, contains XCOM2 WotC config), `G:\Idi Manual Backup\` (862K, loose txt/pdf/jpg), `E:\4K BACKUP\` (4K film remuxes), `E:\0_TEMP_STORAGE\` (+ `D:\0_TEMP_STORAGE.lnk`), `D:\FileHistory`, `E:\FileHistory` (both denied/unsized). Nothing named laptop, transfer, from-laptop, migration or workspace exists as a folder. No laptop `/workspace` tree found.
7. Vault worktrees: 10 git worktrees under `D:\work\vault\.claude\worktrees` (387M, 3,088 files). They duplicate `projects/` and the identity folder. Expect duplicate hits in any diff.

## 1. Drives

| Drive | Label | Used | Free | Notes |
|---|---|---|---|---|
| C:\ | (none) | 859.2 GB | 71.3 GB | OS, `C:\Games` 424G, `C:\tutoring-bakeoff` 6.4G (FLAG 1) |
| D:\ | D | 585.4 GB | 345.2 GB | user content; only `D:\work` readable by jep |
| E:\ | Games 0-L | 3,644.2 GB | 81.8 GB | game library + `4K BACKUP` + `0_TEMP_STORAGE` |
| F:\ | Games M-Z | 2,779.2 GB | 15.2 GB | game library, nearly full |
| G:\ | Archive | 0.8 GB | 697.9 GB | `Backup\2026-08-29`, `Idi Manual Backup` |

## 2. D:\work (depth 3)

| Path | Size | Files | Notes |
|---|---|---|---|
| D:\work | ~1.8G | | total |
| D:\work\vault | 621M | 3,565 excl. .git | see section 4 |
| D:\work\studio | 1.1G | 28,409 | |
| D:\work\studio\kidstudio | 1.1G | 28,409 | Kid Studio app |
| ...\kidstudio\venv | 1.1G | 28,238 | Python venv, rebuildable |
| ...\kidstudio\archive | 17M | 46 | |
| ...\kidstudio\out | 18M | 68 | generated output |
| ...\kidstudio\v6-build | 8.2M | 23 | |
| ...\kidstudio\log | 3.1M | 13 | |
| ...\kidstudio\static | 92K | 4 | |
| ...\kidstudio\workflows | 8.0K | 2 | |
| ...\kidstudio\__pycache__ | 16K | 3 | |
| D:\work\screens | 50M | 138 | screenshots |
| ...\screens\9GAG (+media) | 24M | 111 | |
| ...\screens\Poker | 4.0M | 8 | |
| ...\screens\one-zero | 1.4M | 8 | Cash bank screenshots |
| ...\screens\XCOM | 440K | 1 | |
| ...\screens\BIOS | 4.0K | 0 | empty |
| ...\screens\DECADEnts.png, XCOM-BLACK.png | | | loose files |
| D:\work\captures | 136K | 66 | phone-capture git clone (vault-captures) |
| ...\captures\.git | 122K | 59 | |
| ...\captures\.obsidian | 12K | 5 | |
| D:\work\XCOM-archive-2026-09-11.zip | 5.4M | 1 | + `_MANIFEST.txt` 20K, `_delete.py` 4K |

## 3. C:\Users

| Path | Size | Files | Notes |
|---|---|---|---|
| C:\Users\Idi | denied | | owner profile, unreadable to jep (FLAG 3) |
| C:\Users\Public, Default | not sized | | system |
| C:\Users\jep\AppData | 3.2G | | internals skipped (`Application Data` 709M and `Local Settings` 2.5G are junctions into it) |
| C:\Users\jep\.claude | 2.1G | 3,418 | |
| ...\.claude\jobs | 1.9G | 2,119 | 27 job dirs, tmp deliverables (XCOM inis, kidstudio/decadents drafts) |
| ...\.claude\projects | 248M | 188 | session transcripts + memory |
| ...\.claude\plugins | 6.5M | 450 | |
| ...\.claude\file-history | 4.6M | 353 | |
| ...\.claude\skills | 4.1M | 209 | |
| ...\.claude (backups, cache, daemon, hooks, teams, others) | <1.5M | | |
| C:\Users\jep\.local | 1.4G | 664 | `bin` 458M, `pwsh7` 247M, `share\claude` 682M |
| C:\Users\jep\.cache\huggingface | 315M | 13 | model cache |
| C:\Users\jep\.pi | 8.0M | 5 | Pi harness leftovers |
| C:\Users\jep\.codex | 1.2M | 81 | |
| C:\Users\jep\.psmux | 228K | 30 | |
| C:\Users\jep\.gemini | 210K | 34 | |
| C:\Users\jep\.ssh | 17K | 10 | |
| C:\Users\jep\Desktop, Documents, Downloads, Pictures, Music, Videos | ~1-5K each | 1 each | effectively empty (desktop.ini) |

## 3b. Other drives, top level

| Path | Size | Notes |
|---|---|---|
| D:\ root folders: 83030_1080p, App Installers, aurel_manea_archive_selection, Drive, eBooks, Fan Theories, FileHistory, Funny Gifts, Funny Videos, KEEP, MEMES, Memories, OLD Music, PKMS, Post, Prompt, RSD, Torrent Downloads | denied | user content, jep cannot read (FLAG 4). `PKMS` and `Prompt` are likely knowledge-system material |
| D:\ root loose files | ~33M+ | ~25 .txt notes, AVATAR*.jpg, ChangeFramework.png, SpaceJam.The#1Draft.pdf (33M), 0_TEMP_STORAGE.lnk |
| C:\Games | 424G | game library (Cyberpunk 2077, Death Stranding 2, Kena, Nioh, Spider-Man 2) |
| C:\XboxGames | 359M | game library |
| C:\XCOM2 AML 1.6.0-beta | 82M | XCOM mod launcher |
| C:\Python314 | 172M | runtime |
| C:\ColorControl | 75M | tool |
| C:\Overstrike | 8.1M | tool |
| C:\tutoring-bakeoff | 6.4G | FLAG 1 |
| E:\ AAA, Cemu, Episodes, Horror, Local/Online Multiplayer, Other, Side Scrollers, Strategy, Walking Simulators, Z-Mods and shit | ~3.6T (drive) | game library, not sized per folder |
| E:\4K BACKUP | not sized | 4K film remuxes (Interstellar, Apocalypse Now, 12 Angry Men...) |
| E:\0_TEMP_STORAGE | not sized | Hamilton remux, 2016 Passengers, Black Mirror, YouTube; staging-like |
| E:\FileHistory | not sized | Windows File History |
| F:\ same genre folders + MSOCache, Z-Lists, Z-Mods+Tools | ~2.8T (drive) | game library |
| G:\Backup | 613M | `2026-08-29\` Desktop 32K (10), Documents 453M (610), Pictures 160M (61) |
| G:\Idi Manual Backup | 862K | Repos.txt, YT.txt, words.txt, Nioh.txt, flow-flywheel.pdf, weekly-archive.bat, PEACE.jpg, others |

## 4. D:\work\vault (top level only)

621M total, 3,565 files excluding .git.

| Folder | Size | Files |
|---|---|---|
| .claude (10 worktrees) | 387M | 3,091 |
| projects | 141M | 299 |
| .git | 61M | 558 |
| inbox | 27M | 29 |
| .vault-config | 1.2M | 21 |
| daily | 488K | 51 |
| .obsidian | 362K | 10 |
| identity folder (TELOS) | 176K | 42 |
| bases | 16K | 4 |
| atomic-notes | 4K | 1 |
| templates | 1K | 1 |
| work | 0 | 2 |
| root loose files | | CLAUDE.md, Idi's Whiteboard.md, wins-jar.md, IMDb_EDA.ipynb, 1-6.png, one Pasted image |

## 5. Project-name hits (top-level hits only; worktree duplicates and .claude job scratch collapsed)

| Name | Path | Size | Files | Notes |
|---|---|---|---|---|
| Curtains | D:\work\vault\projects\Curtains | 12K | 1 | inventory stub only; laptop `/workspace/projects/Curtains` NOT on this PC |
| I4 / Triple Inception | none | | | no hit |
| Sovereign Nexus / sovereign / nexus | none (only Corsair `nexus_images` in AppData, irrelevant) | | | no hit |
| Kid Studio / kidstudio | D:\work\studio\kidstudio | 1.1G | 28,409 | app, 1.1G of it venv |
| | D:\work\vault\projects\kidstudio + 4 `kidstudio-*.md` | 126K | 11 | |
| DECADEnts | D:\work\vault\projects\decadents + 2 `decadents-d1-*.md` | 25M | 21 | |
| | D:\work\screens\DECADEnts.png | | 1 | |
| XCOM | D:\work\vault\projects\XCOM | 113M | 73 | |
| | D:\work\XCOM-archive-2026-09-11.zip (+manifest, delete.py) | 5.4M | 3 | |
| | D:\work\screens\XCOM | 440K | 1 | |
| | C:\XCOM2 AML 1.6.0-beta | 82M | | launcher |
| | G:\Backup\2026-08-29\Documents\my games\XCOM2 War of the Chosen | 35M | 10 | config backup |
| Cash | D:\work\vault\projects\Cash | 1.2M | 80 | |
| vault-agent | none | | | no hit |
| tutoring | C:\tutoring-bakeoff | 6.4G | | FLAG 1 |
| | D:\work\vault\projects\tutoring-bakeoff | 1.3M | 44 | vault-side bakeoff notes |
| | D:\work\vault\projects\tutoring-*.md | | ~35 | distilled notes |
| | D:\work\vault\inbox\TUTORING | 156K | 3 | |
| investment-research | none | | | no hit (identity-folder page was deleted, per git status) |
| voice-input | none | | | no hit |
| workspace | none as a folder | | | only Obsidian/Edge `workspace*.json` state files |
| TELOS | D:\work\vault\(identity folder) | 176K | 42 | + copies in 5 worktrees |
| ComfyUI | none found | | | FLAG 5 |
| vault worktrees | D:\work\vault\.claude\worktrees | 387M | 3,088 | cash-console, -v2, -v3, d1-quest, daily-note-system, decadents-d1-round4, intent-layer, parts-registry-draft-two, session7-generators, xcom-sitrep |

## 6. Not scanned / gaps

- `C:\Users\Idi`, D:\ root folders, `D:\FileHistory`: denied to jep. Rerun as Idi (or an admin shell) to size them.
- E:\ and F:\ game folders not sized per folder (drive totals only).
- Name search ran to depth 12, skipping venv, .git, node_modules, site-packages.
