---
type: report
created: 2026-09-14
author: jep
project: XCOM 2 WotC campaign
status: active
---

# XCOM 2: Season 10 mod additions, four questions answered (2026-09-14)

Sources: live launcher database `C:\XCOM2 AML 1.6.0-beta\settings.json` (mtime 2026-09-14 15:04, 1,109 mods), workshop folders on disk (1,109), launcher exe strings, three agent reads of the Steam pages (anonymous, curl where WebFetch hit 429). Agent reports kept at `C:\Users\jep\.claude\jobs\4807d975\tmp\report-*.md` for this job only.

## Launcher delta since the 09-10 sitrep

- 1,094 → 1,109 mods. 21 added since 09-01 (9 on 09-11 incl. local `jepFixes`, 3 on 09-13, 9 on 09-14). All active.
- Unresolved dependency flags across all 1,109: exactly one, No Civilian Walk (item 1).
- Highlander in use: `[BETA] X2WOTCCommunityHighlander v1.31.2` (id 1796402257) + `[WOTC][BETA] Alien Hunters Community Highlander v1.31.2` (id 2635921321). Stable ids 1134256495 and 2534737016 are not on disk.
- 249 mods list the stable Highlander 1134256495 as a Steam requirement; 248 have it in `IgnoredDependencies`. Same pattern will repeat for every new Highlander-dependent mod.

## 1. No Civilian Walk: false-positive dependency

- Folder 3800744283, internal name `CiviliansRun`, author tac, created 2026-09-13, compiled script (`Script/CiviliansRun.u`) + own config `XComCiviliansRun.ini` (panic triggers: concealment break, mission start if unconcealed, scary action; panic uncleansable by default).
- Launcher entry: `Dependencies: [1134256495]`, `IgnoredDependencies: []`. Steam's "required items" box on the mod page names the stable Highlander; the launcher checks by workshop id, so the beta (1796402257) does not satisfy it. Nothing is missing.
- Fix, same click as the other 248: in AML select the mod → Mod Info → `Dependencies` tab → select the missing X2WOTCCommunityHighlander row → `Ignore`. Labels verified from the launcher exe strings ("Mod Info -> Dependency Tab", "&Ignore", "Ignored"). Writes `IgnoredDependencies: [1134256495]` to settings.json.
- Alternative: jep edits settings.json while AML is closed. Not recommended; AML rewrites that file on exit and a race loses the edit.
- Confidence high on cause and fix. Beta 1.31.2 is newer than the stable 1.31.x the mod was built against; medium confidence it exposes everything the mod calls (no way to test short of a mission).

## 2. Steam item 2820842366: "How to Preserve Mods' Configurations in a Local Mod"

- A Steam guide, by TeslaRage, 2022-06-13, updated 2022-07-18, comments live through 2026-09-09. Nothing to subscribe to.
- Method: a local mod folder under `XComGame\Mods\` (AML mod directory below the workshop one), `ZZZLocalTweaks.XComMod` with `publishedFileId=0`, a `Config\` holding ini files named exactly as the target mods' ini files, only the changed lines under the exact `[Section]` header. Workshop updates never touch it. `Localization\` overrides work the same way (2026-09-09 comment).
- Verdict: useful, and already in practice here. `XComGame\Mods\jepFixes` (built 2026-09-11, `XComContent.ini`, 8 corrected BodyPartTemplateConfig lines for Mandalorians of the Old Republic and Mass Effect Multiplayer Armour) is this exact pattern. Every future ini tweak (WSR skin-only list, Amalgamation exclusions from Next Campaign Notes) belongs there.
- Caveats: local mod must load after the workshop mods; `+` appends, bare `Key=` replaces, wrong prefix duplicates; a renamed variable upstream makes the override silently dead.
- Confidence high (two consistent fetches, comments read).

## 3. Steam item 3641533905: "Odd SX Gameplay Tweaks"

- By FearTheBunnies, posted 2026-01-07, updated 2026-05-25, 15.99 MB, 3,761 subscribers, 89 change notes. Season X (10) balance layer of OddCom, sitting on the 583-mod S10 collection (id 3693365875 gameplay 422, cosmetics 171). Requires both stable Highlanders v1.31.0 (ids 1134256495, 2534737016) and all DLC.
- Content: per-mod overrides for about 30 mods (squad sizes, MOCX as Dark VIPs, Covert Infiltration chains, research smoothing, enemy buffs incl. Avatars and Lost, Chosen strengths removed, Lost swarm cap 5, "local copy of Universal Enemy Compatibility Patch group definitions", weapon/item/cost rebalance) + one character pool + three AML profile txt files.
- Relationship to item 2: none stated; zero hits for the guide, TeslaRage or "local mod" in the page. It is the guide's method published as a workshop item.
- Can jep do this: yes for the ini layer, today. The S9 predecessor you already run (`Odd S9: Season 9 Campaign Tweaks`, id 3314720537, active, updated 2026-04-24) is 61 ini files + 8 UnrealScript classes + 1 compiled `.u` (EU Berserker patch, Spark shield patcher, Expose Weakness patcher, Pitcher fix). The ini part is text; jep reads every workshop `Config\` folder and writes overrides into `jepFixes`. The compiled part needs the free "XCOM 2 War of the Chosen SDK" Steam tool (not installed) plus an in-game test cycle.
- Do not stack SX tweaks on top of S9 tweaks: both override the same ini files (Amalgamation, class data, encounters, missions, weapons); last loader wins and neither author tested the pair. Subscribing to SX for reading only is fine: the folder lands on disk, jep diffs it against S9, and you rule per change.
- Confidence: high on identity and content; medium on "config-only" for SX (16 MB is large for text; folder not on disk to verify).

## 4. Universal Enemy Compatibility Patch (UECP) and Enemy Mod Balance Changes

Both by Rather Incoherent. Neither requires the other; designed as a pair; no conflict; no load-order instructions. No ChristopherOdd mention on any page, but the SX tweaks description (item 3) says Season 10 ships a local copy of UECP's group definitions, so Odd's S10 runs on UECP logic.

Enemy Mod Balance Changes (id 3013744547, 49 KB, updated 2023-09-23, 6,561 subscribers)
- Config-only. No dependencies. Absent mods: no effect.
- Legend-tier nerfs, mostly Defense: Venators (LEB's), Hive Guards (Hive More) deflect 25→1, Adv Priest Revamp, Purge Priests Archbishops 30→15 def / 50→40 HP / 6→4 armor, Warlocks, Muton Hunter def 10→0, Muton Enemy Pack (Honor Guards 25→10), Frost Legion (Bruisers 40→25, Shield Droids 50→25), Bio Division (Assaults lose Shield Deflect, +5 HP).
- All 9 target mods are installed and active here. S9 tweaks' `XComGameData_CharacterStats.ini` (91 sections) touches the Priest templates only to add followers, no Defense/HP lines, so no collision. Beta Strike doubles HP by game setting after the nerf; Defense edits unaffected.
- Verdict: install. Confidence high.

UECP (id 3034030070, 410 KB, updated 2025-01-27, 7,583 subscribers)
- Hard dependency: Encounter List Replacer WOTC by H4ilst0rm. NOT installed here. ELR replaces encounter lists by script and skips enemies whose mod is absent, which is what makes a universal patch possible.
- Mechanism: rebuilds every ADVENT leader/follower list with hand-set weights for 72 listed mods (+ Muton Centurion Standalone, G-Virus). Untouched: Lost, faction mods, mod-added SITREPs, new mission types. Pathfinders restricted to theme pods; trooper variants 1/5 Faceless imitator; Bio Assaults +2 FL; vanilla Muton/Sectoid/Viper fall off at FL 21. No stat changes.
- The catch: any enemy-adding mod not on the list silently never spawns in normal pods (author's statement; confirmed by EvilBob22 and ice_castle_cmdr 2026-06-17, Stukov's Thin Men vanished). Author replies stopped 2024-07-10; list last edited 2025-02-06. Users maintain extensions: Captain Lost's Drive folder (2026-05-17, Requiem ADVENT units), RambelZambel's ini update (2026-06-15, in the mod's Discussions, not fetched).
- Coverage diff against this launcher (77 mods tagged Alien/Enemy, name-matched, medium confidence): 44 matched the list. Of the 33 unmatched, 23 are not spawn-list mods (Not Created Equal ×4, MOCX classes ×2, Choose Your Aliens (author: fully compatible), skins/colors/icons/SFX/corpse ×6, Zelfana fixes ×2, AI Patcher, Lost mods ×3 untouched by design, mission mods ×2, CreativeXenos revamps ×3 which replace vanilla units in place). Real gaps, enemies that would go silent: Muton Adolescent (3507107993, requested 2025-12, unsupported), A Requiem For Man: ADVENT Pack (3512490242, unsupported, Captain Lost's extension covers it), Stukov's War Enhanced Enemies: Purifiers, Spooky Scary Sectopods. Unknown interaction: All Followers Supported! (3022561023) and Synthoids (author: script-inserts itself into lists). Overridden by UECP: Diverse Aliens By Force Level (ini edits to lists that UECP replaces) and S9 tweaks' own EU Berserker encounter edits (UECP handles EU Berserker itself).
- Verdict: install UECP + ELR for the new campaign, then jep writes a local UECP ini extension for the 4 gap mods into `jepFixes` using UECP's shipped Readme and Captain Lost's entries. Without the extension those 4 mods are dead weight. Mid-campaign install untested by the author; start-of-campaign is the safe moment. Confidence medium: coverage is by name match, not template-level; the 2026 comment reports are the strongest evidence for both the value and the cost.
- Skip UECP if you would rather keep Diverse Aliens By Force Level and the S9 encounter edits as the spawn logic; then the 88 enemy mods compete on their own ini weights, which is the "some show up far too often, others almost never" state the patch exists for.

## Not done

- No settings.json write. No mod subscribed. No ini written. SX tweaks folder not read (not on disk). RambelZambel's UECP ini thread not fetched (429).
- DABFL: S9 tweaks ship `XComDABFL.ini` but no DABFL mod is in the launcher. Unasked; flagging once.

## Receipts

- Launcher DB parse: `Mods.Entries.{Unsorted,Big}.Entries`, 1,109 rows; No Civilian Walk row index 1100.
- Exe strings: `XCOM2 Launcher.exe`, UTF-16 scan for depend|ignor.
- S9 tweaks: `workshop\content\268500\3314720537`, 7.4 MB, 61 ini / 8 uc / 1 u / 5 bin.
- jepFixes: `XCom2-WarOfTheChosen\XComGame\Mods\jepFixes`, 3 files.
- Steam pages: 3034030070, discussion 3825300455707242332 (27 replies, both pages), 3013744547, 2820842366, 3641533905; fetched 2026-09-14.

## 5. Same day, after Idi's corrections: UECP extension built into jepFixes

Idi's corrections: jepFixes was known; the TeslaRage guide was sent for refinements to it; ELR, UECP, EMBC and Odd SX Tweaks subscribed. All four landed on disk (ELR = folder 2337729548).

What the code says (ELR source read): each `+Overrides=(List=...)` entry deletes and rebuilds that whole list; `FindGroup` returns the first group with a given name. So a partial add-on ini cannot extend UECP; the extension must be full replacement copies of UECP's groups and overrides files, loaded after UECP. Odd SX does exactly this (`Config/UECP/` in its folder, `!Groups=()` at the top).

Gap scan, template level, case-insensitive: every workshop `XComEncounterLists.ini` (98 mods add to lists) against UECP's 741 covered templates and the 76 lists it rebuilds. Result: 33 units in 9 mods would never spawn in normal pods; 150 more uncovered units sit only on Lost, SITREP or mission-only lists and are unaffected. Earlier name-match estimate (4 gap mods) was wrong in both directions: Stukov's Purifiers and Spooky Scary Sectopods add no units; Synthoids are in UECP; Frost Legion, Requiem Legion, Custodian Pack, Children of the King, ABA and the LWOTC Standalone pack each have 1 to 4 units UECP missed.

Built (in `XComGame\Mods\jepFixes\Config\`, mirrored to `projects/XCOM/jepFixes/`): `XComELR_groups.ini` (UECP copy + 39 unit entries + FrostPudding_M2 trimmed to FL14), `XComELR_overrides.ini` (UECP copy + 5 Extras), `XComAGData.ini` (18 Requiem ADVENT units on the General buff whitelist, lifted from Odd SX), `XComELR.ini` (logs TerrorLeaders/Followers). Numbers: Odd SX's for the 18 Requiem ADVENT units, scaled to UECP's base; jep's for the other 15, each justified in the README table. Skipped: MutonLegionEarlyBoss115 (UECP replaced that mission's Muton bosses with generals by design).

Verified: both generated files parse (127 groups, 76 lists, contiguous indices except UECP's own pre-existing ArchonFollowers gap, every line carries the continuation marker, CRLF and no BOM preserved to match the source), md5 of live and mirror copies identical, ban grep zero. Not verified: in-game. Recipe in the README (ELR prints the rebuilt lists into Launch.log).

jepFixes refinements taken from the guide: load position (jepFixes must be last; it sits at index 1094 of 1271 and the new mods import after that), README rewritten with the real defect per source line (missing comma, doubled quote) instead of truncated identical before/after strings, verification recipe, maintenance rule (re-diff if UECP updates). Not taken: `<STEAMID>_<MODNAME>` subfolders (unverified by jep; flat files carry zero risk).

Conflicts found: All Followers Supported rewrites SupportedFollowers in the same hook ELR uses (disable); Diverse Aliens By Force Level is inert under UECP; Odd SX Tweaks must stay disabled or its own ELR copies fight jepFixes for last place. Odd's S10 profile runs ELR + UECP + EMBC and none of those three.

No Civilian Walk: nothing for jepFixes to do. The launcher flag is the "Ignored" checkbox in the mod's Dependencies tab (AML wiki, Basic usage). Its panic settings can go into jepFixes only if non-default values are wanted.

## 6. First launch: extension not live, cause found, two corrections owned

Idi's log (`projects/XCOM/Launch.log`, 53,540 lines, 16:34): the game checked `Mods\jepFixes` 6th, right after the five DLCs and before all 1,114 workshop folders (ascending folder name). UECP's `!Groups=()` ran later and wiped jepFixes' groups: the ELR "Lists after" dump holds none of the 33 added units and FrostPudding_M2 still shows Max FL 99. The rule I stated (AML index = load order) was wrong. The real rule: directory order from AML's Settings > Mod Directories (`ModPaths` in `settings.json`), then folder name inside a directory. TeslaRage's step 2 ("add the local path below the workshop directory") is exactly this, and I filed it under cosmetic. Fixed 2026-09-14 16:4x by swapping `ModPaths` in `settings.json` (AML closed, backup `settings.json.jep-2026-09-14`). Pass criterion for the next log: jepFixes is the last `Checking DLC installation` line, and the six ELR "Lists after" blocks contain ARFMAdvOutriderM1, MutonAdolescent, ViperFrostling, SectoidTrooperM4.

Dependency exceptions: the August 31 database (vault copy, 1,094 mods) has 0 ignored dependencies; the live one had 248 by today. A jep session set them between those dates by editing `settings.json`; no memory note recorded it, so I defaulted to the click path. Done now the same way: `[WOTC] No Civilian Walk` ignores 1134256495; `Odd SX Gameplay Tweaks` ignores 1134256495 and 2534737016 (it is disabled; the red mark goes away). Verified by reloading the file.

Also in the log: `ELR: No group defined with name: NemesisLeaders` (UECP references a group it never defines; harmless), 2,997 `Unit template does not exist` lines (ELR skipping units of mods not installed; expected), 60 `Missing Leader template` lines (same cause, follower patching). All Followers Supported disabled by Idi.

Enemy checklist: `projects/XCOM/enemy-checklist.md`. 549 units from 44 sources: the 520 units in the six logged pod lists (real pool) plus the 29 pending jepFixes units, each with display name from the mods' localization, template, force-level window, leader/follower role. Grouped per source mod, sorted by first appearance, Obsidian checkboxes. Out of scope on purpose: Lost, Chosen, rulers, SITREP-only, mission-only, raider factions.

## 7. Second launch: extension live

Log 17:00 (`projects/XCOM/Launch.log`, 53,616 lines). Load order: jepFixes is check 1,119 of 1,120 (the 1,120th is the launcher's workshop-root placeholder path, not a mod). ELR "Lists after": all 29 pod units present with the intended numbers (MutonAdolescent FL1-5 w1.5 on Default/Terror leaders and followers, ARFMAdvOutriderM1 FL3-7 w0.5 on Default/Advent/Terror leaders, SectoidTrooperM4 FL13+ w2 on TerrorLeaders, FrostPudding_M2 now FL9-14). The 4 remaining additions sit on boss and field-commander lists that ELR does not log, unverifiable from this log by design. Pod pool grew from 520 to 549 units. Same harmless noise as before (one dangling UECP group reference, 2,997 skipped absent-mod templates).

Checklist rebuilt from the live lists: `projects/XCOM/enemy-checklist.md`, 549 units, 44 sources, no pending lines.

## 8. Mod configuration inventory

Idi's ask: which mods can be configured, to decide which to configure. Built `projects/XCOM/mod-config-inventory.md`: 1,111 active mods scanned; 610 ship their own options ini (listed with key counts, sample keys, and whether Odd S9 or SX tweaks already override them), 403 carry only base-game overrides. Worked cases in the same file: Choose My Class set to 30 in jepFixes (done); sitrep removal via Multiple Sitreps REDUX's `+BlockedSitReps` (any sitrep, base game included; Lightning Strike is Covert Infiltration's `LightningStrike`); PCS loot via the untouched `PCSDropsEarly/Mid` mix tables, option A drops the Common tier only. Also surfaced: Multiple Sitreps REDUX guarantees 3 sitreps per mission by default.
