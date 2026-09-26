---
type: report
created: 2026-09-10
author: jep
project: XCOM 2 WotC campaign
status: active
---

# XCOM 2 WotC campaign: situation report, 2026-09-10

Scope: `projects/XCOM/` (108 MB, 361 files) plus the master Google Sheet (link-readable, exported anonymously as xlsx, 15 tabs). Four read-only sweeps (mods, soldiers, plans, duplicates) plus direct sheet parsing. Nothing modified.

## 1. Verdict

- Roster: DONE. `Character Pool/CharacterPool/DefaultCharacterPool.bin` (2026-03-30) holds 200 named characters with full appearance data: 180 soldiers + 20 VIPs (Mr. Black to Ms. Yellow). 187/200 names match the sheet exactly; 13 spelling drifts, listed in §6.
- Mods: DONE, one editing pass behind. Launcher database `XCOM2 AML 1.6.0-beta/settings.json` (2026-03-31): 1,054 enabled, 0 conflicts, 0 duplicates, 53.8 GB. Sheet Mods tab: 1,036 names, 1,035 match the launcher. 287 marked Confirmed, all present in the launcher.
- Game: INSTALLED ON THIS PC. `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2` exists; 1,095 workshop folders under `steamapps\workshop\content\268500` (51 GB). Last logged successful launch 2026-03-31 20:18, closed 20:28.
- Open: no difficulty or ironman decision anywhere (grep-verified). Outfit backlog of about 48 named outfits in `Next Campaign Notes.md`, status unknown (medium confidence; the bin has torso data for all 200 but that does not prove the licensed outfits were built).
- Blind spot: the live launcher database and live character pool sit under `C:\Users\Idi\AppData\Local\AML` and `C:\Users\Idi\Documents\my games\XCOM2 War of the Chosen\XComGame\CharacterPool`. Both exist, both are permission-denied to jep. The consolidated copies come from a `C:\Users\Idan` profile (laptop era) and may be older than what the PC runs now.

## 2. Signal / stale / noise map

| Path | Verdict | Why |
|---|---|---|
| Google Sheet (15 tabs) | SIGNAL, live spec | 180 soldiers + 20 VIPs + 1,036 mods + 124 outfits + name/voice options, dropdown-validated |
| `XCOM2 AML 1.6.0-beta/settings.json` | SIGNAL | launcher DB, 1,054 mods, enabled state, add dates 2025-04-04 to 2026-03-16 |
| `XCOM2 AML 1.6.0-beta/AML.log*` | SIGNAL | 723 launches, 2025-04-04 to 2026-03-31, missing-mod history |
| `Character Pool/CharacterPool/DefaultCharacterPool.bin` | SIGNAL | the finished 200 roster, 454 records incl. 254 uniform templates |
| `XCOM VAULT/Next Campaign Notes.md` | SIGNAL | rules, skin-only weapon list, manual-config mods, outfit backlog |
| `XCOM VAULT/Name Mods/XComGame.txt` | SIGNAL | hand-edited, 927 `+RandomNickNames` across 9 classes |
| `specs/standards/naming_rules.md`, `Voices & Nationalities.md`, `Outfits.md` | SIGNAL | design rules, 56 voice packs mapped, one outfit per soldier |
| `screenshots/*.jpg` (2025-12-17) | SIGNAL | AML 1062/1062, 265 missing dependencies, 0 conflicts; pool menu "Character Pool Only" |
| `XCOM VAULT/Soldiers - 100/`, `VIPs & Crew - 20/` | STALE | 2025 markdown; 58/100 survive in bin unchanged, 36 renamed, 6 dropped; 28 files half-blank |
| `XCOM VAULT/Mods/Mod List*.md` | STALE | May 2025 hand list, 1,187 IDs, 275 entries absent from sheet |
| `data/csv_source/*.csv` + `*proposals*.md` | STALE | Dec 2025 snapshot of the sheet; 18 names since revised; proposals = naming pass for 60 slots, absorbed |
| `product/*`, `specs/mods/manifest.md`, `scripts/*.py` | STALE | Dec 2025 agent layer; gap report numbers wrong (counted index files, missed the bin); scripts hardcode dead paths; roadmap 2/6 executed |
| `Character Pool/CharacterPool/Importable/*.bin` | STALE | 19 third-party pools + 2 own snapshots (Apr/May 2025) |
| `data/orphans/`, `data/pool/` | NOISE | byte-identical copies of XCOM VAULT files (126 md5 groups); `Soldiers - 180` holds 100 |
| `Mod List 2.md`, `settings.json.bak`, `_AppearanceManagerBackup.bin` | NOISE | md5 twins of their siblings |
| `XCOM2 AML 1.6.0-beta/*.dll, *.exe, *.pdb` (72 MB) | NOISE | program binaries; only the json, txt and logs carry data |

## 3. Mod counts over time

| Source | Date | Mods |
|---|---|---|
| `Mod List 1.md` | 2025-05-17 | 550 |
| `Mod List.md` | 2025-05-19 | 1,187 |
| `AML.txt` export, screenshot | 2025-12-22 | 1,062 |
| `manifest.md` | 2025-12-22 | 1,061 |
| `ModList.txt` = `WAR.txt` | 2026-02-28 | 1,095 |
| `settings.json` | 2026-03-31 | 1,054 enabled |
| Sheet Mods tab | live | 1,036 |
| Workshop folders on disk | 2026-09-10 | 1,095 |

Disk vs launcher DB: 1,034 shared, 20 in DB without folder, 61 folders not in DB. Sheet vs DB: 1 sheet-only (`Civilians Scream - WotC`, hidden by AML 2026-03-16 after its folder vanished), 19 DB-only (robojumper's Squad Select, Holo Begone, Codex Begone, Effect Durations, Friendlier Tactical Analysis, Fancy Spark Poses, Narrative Control, Shield Attachments, Merist's + Styr's Perk Packs + 2 GTS bridges, Re: Death From Above, One More Thing, Traversal Changer + Example, Avatar Psi Amp, Show Me The AP + bridge).

Sheet categories: Cosmetic 194, Fix 154, UI 100, Amalgamation 92, Enemy 88, Weapon 74, System 63, Geoscape 51, Map 46, Class/Perk 36, Voice 29, Bridge 28, Item 21, Spark 20, Animation 11, MOCX 8, Weapon Attachment 8, Armor 7, Graphics 4. Confirmed by category: Cosmetic 170, Weapon 36, Voice 26, UI 17, System 11, Fix 10, Geoscape 10, Enemy 5, Armor 1. Confirmation column values: Confirmed 287, Null 640, XSkin 25, config notes 9.

Log warnings: 118 distinct mods logged "no longer available" over the history, 40 hits on AmalgamationRonin (3256627073); OOM crash of AML 1.6.0 on 2025-06-30; 48 cosmetic contentimage parse warnings on mod 1132838346.

## 4. Roster facts

- Sheet Soldiers tab: 180 rows, 90 M / 90 F, 8 per nation (US, UK, IL, CA, FR, ES, DE, IT, and more), 4 each XCOM/Reaper/Skirmisher/Templar. Identity columns 180/180 filled. Appearance columns partly Null: Hair 84, Facial Hair 148, Shoulders 151, Tattoos 143 (Null = none chosen; the bin has full records regardless).
- Two colored rows: row 119 Essa Evangelista (blue), row 161 Guadalupe 'Lupe' Gortada (pink). Meaning unrecorded.
- VIPs tab: 20, generic black suits, Reservoir Dogs names in the bin.
- Outfit tabs: Male 12+32+1+10+6 = 61, Female 7+40+0+10+6 = 63, total 124. HiTec tier nearly empty (1 male, 0 female).
- Name Options 30, Voice Options 55.
- Design rules: alliteration on first/nick/last; three hero exceptions (Kazimir 'The 11th' Pavlovich, Jane 'The Eternal' Kelly, Dancis 'Knightfather' Joyeuse); `(N)` suffix = callsign syllables, 1 to 2; soldiers are originals in licensed outfits; Skirmishers primordial with tech words blacklisted, Reapers stealth, Templars religious.

## 5. Decisions already on record (`Next Campaign Notes.md`)

Promote ASAP; spend AP and buy gear only pre-mission; avoid captures; prioritize bonds; bestiary after every mission; disable Lightning Strike-type sitreps and junk PCS loot; console sanctioned for Denmother after Knightfather rescue and AP refunds when MECing. 20 weapon packs to convert to skin-only. Amalgamation and WSR configured through the Odd Season 9 Tweaks ini files. Launch args `-allowConsole -USEALLAVAILABLECORES -malloc=system`.

## 6. Spelling drift, bin vs sheet (13)

Bin-Marzawi/Bin-Marwazi, Belissa/Bellisa, Cervouis/Cervoius, Corrington/Corringsworth, Dacnis/Dancis, Figuira/Figueira, Gabriella/Gabriela, Hilderbrand/Hildebrand, Lindholm/Lidnholm, Najafri/Najafi, Nashiwado/Nagiwado, Waverly/Waverley, Guilotine/Guillotine (Gaspard Gilbert nickname). Drift runs both ways; neither source is strictly newer. Typos to reconcile by hand.

## 7. Risks

1. `projects/XCOM/` is untracked and unignored. The next autocommit would push 72 MB of DLLs and an exe plus 24 MB of bins to GitHub. Recommend ignoring `XCOM2 AML 1.6.0-beta/*.dll|exe|pdb` and `Character Pool/**/*.bin`, or moving the AML program folder out of the vault.
2. The consolidated launcher DB and pool may lag the PC's live copies (§1 blind spot). Verify by comparing `settings.json` mtime and the live bin's md5 from the Idi account.
3. 265 missing dependencies in the Dec 2025 screenshot; not re-checked since. Confidence low that it is resolved.
4. Nothing about XCOM in `daily/`, the Whiteboard, or the wins jar; TELOS item 5 names the manual outfit assembly in the character creator as the blocker (Jan 2026 interview).

## 8. Sources and receipts

- Sheet export: `https://docs.google.com/spreadsheets/d/13z-2u18M5AlJcf4q_63Zjzii7l058ipl2C0z17XnYUQ/export?format=xlsx`, HTTP 200, 160,150 bytes, parsed with openpyxl.
- Duplicate check: md5sum over 321 non-AML files, 126 identical groups.
- Bin parse: Unreal property stream, 454 `CharacterPool` elements, `nmTorso` present in all 200 named records.
- Workshop count: `ls C:\Program Files (x86)\Steam\steamapps\workshop\content\268500 | wc -l` = 1095.
- Live-path probe: `ls` on the two `C:\Users\Idi\...` paths returned Permission denied (exists, unreadable).

## 9. Update, same day: live copies compared, duplicates deleted

Idi overwrote the consolidated launcher database and pool bin with the PC's live copies (both dated 2026-08-31). The March 31 database survives as `settings.json.bak`; the March bin is gone (parsed names were cached, bytes were not).

Launcher database, March 31 vs August 31:

| Measure | March | August |
|---|---|---|
| Mods | 1,054 | 1,094 |
| Active | 1,054 | 1,094 |
| Last DateAdded | 2026-03-16 | 2026-08-30 |
| Size | 53.8 GB | 54.2 GB |
| ModPaths | local Mods folder + workshop | workshop only |

60 added, 20 removed, 0 enabled-state changes, 0 notes, 0 tags. Adds are mostly UI, QoL and strategy tools (Ability Shortcuts, Covert Editor, Equipment Manager, Pool Walker, Second Wave Defaults, Campaign Notes Mod, Data Center facility, Small Maps Removal, Virtual Range 2026). Removals are superseded versions (Ballistic Shields, Tactical Armory UI, Extended Information, Filtered Menus, Bond To Header, Remove Missing Mods) plus Faction Flags, GrimStyle Armor, Military Style Torso Decos, Set HQ Location, Auto-Set Second Wave.

Disk: 1,095 workshop folders, 1,094 in the database, one folder unimported (3723136195).

Sheet vs August database: 1,004 of 1,036 sheet names match. 32 sheet rows are gone or renamed (about 11 are renames: Highlander v1.31.0 to v1.31.1, Ghost Templates packs to Weapon Skins, Legacy of Chosen 1.5 to 1.6, MOCX as EXALT 1.4 to 1.5, Classic XCOM Armor 2023 to Redux). 90 database mods have no sheet row. Of 287 Confirmed rows, 274 still resolve; 13 point at removed or renamed mods.

Pool bin, March vs August: identical 200 names (180 soldiers + 20 VIPs), 454 pool elements, full appearance data. File 80 bytes smaller; the changed bytes are outside the name fields. Sheet match unchanged: 187 of 200, same 13 spellings.

Deleted (each guarded by a byte-compare against its twin before removal, 128 files, plus 2 by content proof):

- `data/pool/` entire tree, 122 md files identical to `XCOM VAULT/Soldiers - 100/` and `VIPs & Crew - 20/`, plus 3 empty folders
- `data/orphans/`: `Mod List.md`, `Mod List 1.md`, `Mod List 2.md`, `Outfits.md`, `Voices & Nationalities.md` (identical to XCOM VAULT copies); `Next Campaign Notes.md` (Jan 2026 restyle of Idi's raw file, same lines, ini separator comments dropped; the raw original kept)
- `XCOM VAULT/Mods/Mod List 2.md`, identical to `Mod List.md`
- `Character Pool/CharacterPool/DefaultCharacterPool_AppearanceManagerBackup.bin`, same 200 records as the main bin, differs only in 3 KB of header metadata

Kept on purpose: `settings.json.bak` (the only surviving March 31 database), `data/csv_source/` (December snapshot of the sheet, not a duplicate of any local file), `Importable/*.bin` (third-party pools), the AML program binaries (72 MB, program files rather than data; Idi's call).

Folder after cleanup: 231 files, 102 MB (the 72 MB AML program folder dominates).

## 10. Update, same day: AML program files moved out

Idi runs the launcher from `C:\XCOM2 AML 1.6.0-beta`. That folder already held every program file, so the move was a verified delete: 26 files (22 dll, exe, pdb, 2 config) removed from the vault copy, each md5-identical to its twin in the live folder. Kept in the vault: `settings.json`, `settings.json.bak` (March 31 database; the live `.bak` is an August 31 same-day save, so the vault's is the only March copy), `AML.txt`, `ModList.txt`, `WAR.txt`, `steam_appid.txt`, `AML.log` through `AML.log.5`, `debug.log`, `error.log`.

`AML.log` refreshed from the live folder: the live file continued the vault copy byte for byte, adding 3,836 lines from launcher sessions on 2026-08-30 and 2026-08-31 (43 warnings, all "no longer available" notices for the 20 removed mods). Every other data file matched by md5.

Folder after the move: 205 files, 94 MB. The AML folder is still 64 MB because five rotated 10 MB logs plus the current 6 MB log make 58 MB; the program files were only 8 MB. Pruning the rotated logs is a separate call.

## 11. 2026-09-11: prune to current data (archive built, delete pending)

Idi's order: delete the rotated logs and keep only relevant, useful, up-to-date data. The folder is untracked by git, so deletion there is permanent. Safety net: every file slated for removal was zipped first to `D:\work\XCOM-archive-2026-09-11.zip` (187 files, 26 MB raw, 5.5 MB zipped, each entry md5-verified inside the zip; manifest beside it as `XCOM-archive-2026-09-11_MANIFEST.txt`). The five rotated logs are md5-identical to the live copies in `C:\XCOM2 AML 1.6.0-beta` and are deleted without archiving.

Keep list, 13 files:

| File | Why it stays |
|---|---|
| `Character Pool\CharacterPool\DefaultCharacterPool.bin` | the 200 roster, live copy 2026-08-31 |
| `Character Pool\Path.txt` | where the bin lives on the game side |
| `XCOM2 AML 1.6.0-beta\settings.json` | launcher DB, 1,094 mods, live 2026-08-31 |
| `XCOM2 AML 1.6.0-beta\AML.log` | current log through 2026-08-31 |
| `XCOM2 AML 1.6.0-beta\steam_appid.txt` | launcher needs it |
| `XCOM VAULT\Next Campaign Notes.md` | Idi's rules, skin-only list, config list, outfit backlog |
| `XCOM VAULT\Voices & Nationalities.md` | 56 voice packs mapped to nationality |
| `XCOM VAULT\Name Mods\XComGame.txt` | hand-edited nickname tables, 927 entries |
| `XCOM VAULT\XCOM Character Pool - Soldier Pool.txt` | the master sheet URL |
| `specs\standards\naming_rules.md` | the naming rules |
| `screenshots\Jane_The_Eternal_Kelly.jpg`, `...Kelly2.jpg`, `Sutton_Shade_Stillbrow.jpg` | character reference portraits |

Archived and slated for deletion, 187 files: the 2025 markdown soldiers and VIPs (122), May 2025 mod lists (2), December 2025 CSV snapshot and naming proposals (20), the December agent layer (`product/` 5, `specs/` 4 except naming rules, `scripts/` 2), `Outfits.md` (superseded by the sheet's Outfit Name column), the Dec 2025 soldier-pool CSV, three unmodified name-mod payloads, `settings.json.bak` (March DB; the diff is in §9), the three launcher exports `AML.txt`, `ModList.txt`, `WAR.txt` (superseded by the live DB), `debug.log`, `error.log`, 21 importable third-party pool bins (already absorbed into the main bin as its 254 uniform templates, medium confidence), and 2 launcher screenshots.

The delete step was refused twice by the Claude Code safety classifier as bulk irreversible deletion. The script `delete_archived.py` removes a file only if its md5 matches the archive manifest or its live twin, then drops empty folders. Idi runs it by hand, or rules to keep any group above.

Delete executed by Idi's hand 2026-09-11: 192 removed, 0 skipped, 13 remain. Folder is now the 13 keep files, about 17.5 MB, 15 MB of it the pool bin, launcher database and current log. Recovery for anything removed: `D:\work\XCOM-archive-2026-09-11.zip`.
