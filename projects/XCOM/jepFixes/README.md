---
type: reference
created: 2026-09-11
updated: 2026-09-14
author: jep
---

# jepFixes: local config mod (fixes + UECP extension)

Purpose: hand-edited ini overrides that Workshop updates cannot wipe (TeslaRage's local-mod pattern, Steam guide 2820842366). Config only, no script. `publishedFileId=0`.

## Install and load order

- Path: `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\jepFixes\`
- AML: the `...\XComGame\Mods\` path is listed under Settings > Mod Directories (both paths present in `settings.json` ModPaths as of 2026-09-14).
- Load order, required: Encounter List Replacer WOTC (2337729548) < Universal Enemy Compatibility Patch (3034030070) < jepFixes. Rule, proved from Launch.log 2026-09-14: the game walks mod directories in the order of AML's Settings > Mod Directories list (`ModPaths` in `settings.json`, written to the game's `ModRootDirs` under `[Engine.DownloadableContentEnumerator]`), and inside one directory by folder name ascending. AML's Index/Order column plays no part in config merge order. With `XComGame\Mods` listed first, jepFixes was checked 6th, before all 1,114 workshop mods, and UECP's `!Groups=()` wiped it (the ELR list dump held none of the 33 units). Fix applied 2026-09-14 by jep: `ModPaths` swapped so the workshop directory comes first and `XComGame\Mods` second. Pass criterion in the next Launch.log: the line `Checking DLC installation for ...\Mods\jepFixes` is the LAST of the `Checking DLC installation` lines. If it is not, re-add the Mods path in AML Settings > Mod Directories so it sits below the workshop path.
- Odd SX Gameplay Tweaks (3641533905) ships its own full ELR copies; keep it DISABLED (subscribed for reading only) or it fights this file for last place.
- All Followers Supported (3022561023): disable. It rewrites every unit's SupportedFollowers in OnPostTemplatesCreated, the same hook ELR uses; whichever runs last wins, so either UECP's follower tables die or the mod is inert. Odd's S10 profile does not run it.
- Diverse Aliens By Force Level (1969247728): inert under UECP (its ini list edits are wiped by ELR). Harmless; disable for tidiness.

## Files

| File | Kind | What |
|---|---|---|
| `Config\XComContent.ini` | additive | 8 BodyPartTemplateConfig lines, corrected copies of broken source lines (below) |
| `Config\XComELR_groups.ini` | FULL REPLACEMENT | UECP groups (127) + 39 jep unit entries + 1 edited line |
| `Config\XComELR_overrides.ini` | FULL REPLACEMENT | UECP overrides (76 lists) + 5 jep Extras |
| `Config\XComAGData.ini` | additive | Advent General Revamp buff whitelist, 18 Requiem ADVENT units (from Odd SX) |
| `Config\XComELR.ini` | additive | ELR logs TerrorLeaders + TerrorFollowers to Launch.log for verification |

Full-replacement files are byte copies of UECP's (mod updated 2025-01-27, copied 2026-09-14) plus the jep lines. If UECP ever updates, re-diff: `fc` the workshop file against this one, re-apply the jep lines (all marked in the header comment and listed below).

## XComContent.ini: broken source lines, fixed

Source defect, Mandalorians of the Old Republic 2376020557 (6 helmets): missing comma between `Gender=eGender_Male` (or `_Female`) and `bCanUseOnCivilian=false`. Fixed: comma inserted.
Source defect, Mass Effect Multiplayer Armour Pack 2010492838 (2 leg decos): doubled quote `ArmorTemplate="HeavyPlatedArmor""`. Fixed: single quote.
Templates: ORMandos_Helmet_MercilessSeeker_M/F, ORMandos_Helmet_Shae_M/F, ORMandos_Helmet_ShaeCommander_M/F, HPT_DemolisherLegsDeco, HPT_DemolisherLegsDeco_M. The engine discards the broken originals at load, so these adds do not duplicate.
Verify: the six helmets and two leg decos appear in the customizer. The source mods' broken lines still redscreen on every launch (1,206 lines in the 2026-09-14 17:00 log); the engine parses the originals regardless, so the redscreen count is not a test of this fix.

## UECP extension: 33 units from 9 mods that UECP never listed

Method (2026-09-14): every workshop `XComEncounterLists.ini` scanned; each `Template=` added to a list UECP rebuilds (76 lists) and absent from UECP's groups/Extras (case-insensitive) = a unit that would never spawn in normal pods. Lost-list, SITREP-list and mission-only units excluded by that rule (150 such, untouched). Weights on UECP's scale (base 1, brackets 1x/2x/4x by entry FL; captain 1.5/3/6, trooper 1/2/4, priest 1.5/3/6, purifier 2/4/6).

| Unit | Mod | Group or list | FL | Max | Weight | Number source |
|---|---|---|---|---|---|---|
| ARFMAdvOutriderM1/M2/M3 | Requiem ADVENT Pack 3512490242 | ADVENTCaptains | 3-7 / 8-13 / 14+ | 1 | 0.5 / 1 / 3 | Odd SX 0.75/1.5/3 scaled to UECP captain base |
| ARFMAdvRunnerM1/M2/M3 | same | ADVENTTroops | 2-6 / 7-12 / 13+ | 1 | 0.25 / 1.25 / 2 | Odd SX 0.5/2.5/3 x trooper ratio 0.5/0.5/0.67 |
| ARFMAdvArtilleryM1/M2/M3 | same | ADVENTTroops | 4-7 / 8-13 / 14+ | 1 | 0.25 / 1.25 / 2 | same |
| ARFMAdvKriegsmarineM1/M2/M3 | same | ADVENTTroops | 5-6 / 7-12 / 13+ | 1 | 0.25 / 1.25 / 2 | same |
| ARFMAdvTorcherM1/M2/M3 | same | ADVENTPurifiers | 5-7 / 8-14 / 15+ | 2 | 2 / 4 / 6 | Odd SX = purifier weight; UECP purifier 2/4/6 |
| ARFMAdvKnightM1/M2/M3 | same | ADVENTPriests | 5-7 / 8-12 / 13+ | 1 | 1 / 2 / 3 | Odd SX SXPriests (priest base identical in both) |
| MutonAdolescent | Muton Adolescent 3507107993 | MutonLeaders / MutonFollowers | 1-5 | 1 / 2 | 1.5 / 1.5 | jep: bracket-1 main-unit base; mod's own ini puts it on Default/Terror/NoHardCC lists FL1-5 |
| AHWServitor | Requiem Legion 2867288932 | RequieumLeaders | 10-14, 15+ | 2 | 2, 4 | jep: mirrors UECP AHWFloater curve (own weight = Floater's) |
| AHWServitor | same | RequieumFollowers | 13+ | 2 | 4 | jep |
| AHWGunshipT2, AHWNavigatorT2 | same | RequieumLeaders / Followers | 18+ | 2 | 3 / 2 | jep: T1 stays as UECP set; T2 enters late at half T1 weight |
| AHWChryssalidMagnaM2 | same | RequieumLeaders / Followers | 18+ | 4 | 4 / 2 | jep, same rule |
| AdventCustodianMaster | Custodian Pack 2094672450 | AssaultLeaders | 16+ | 1 | 1.6 | jep: half a Custodian (UECP 3.2); own ini leaders-only |
| ViperFrostling | Children of the King 2205934483 | ViperFollowers | 9-21 | 4 | 1 | same line as UECP's ViperHatchling |
| FrostCaptain_M2 / M3 | Frost Legion 2481645156 | FrostLeaders | 12-17 / 18+ | 1 | 1.5 / 3 | UECP FrostBruiser bracket structure; own ratio M1:M2:M3 = 4:8:16 |
| FrostPudding_M3 | same | FrostFollowers + TheFaceless | 15+ | 3 | 2 | same as UECP FrostPudding_M2; M2 trimmed to FL 9-14 (was 9-99) |
| SectoidTrooperM4 | A Better ADVENT 1126623381 | Extras on TerrorLeaders | 13+ | 1 | 2 | ABA restricts it to terror; own ratio to SectoidTrooper 20:15, UECP trooper 1 |
| FrostAbomination | Frost Legion | Extras on ForcedBossLeader / _PsionicStorm | 20+ / 18+ | 1 | 1 / 10 | jep: a third of the AHW bosses (3); PsionicStorm list runs x10 to x30 |
| AdvGeneralM1_LW, AdvGeneralM2_LW | Standalone LWOTC Alien Pack 3005345170 | Extras on NeutralizeFieldCommander_FieldLeader | 8-13 / 14+ | 1 | 20 / 40 | half of UECP's generals there (ADVENTGenerals x20 = 40/80) |

Skipped on purpose: MutonLegionEarlyBoss115 (Muton Enemy Pack) sits only on the field-commander list, where UECP replaced all six Muton-pack bosses with ADVENT generals by design; one early boss alone would change that mission's FL1-3 pool. Say the word to add it (FL1-3, weight 20).

Not gaps, verified: Synthoids (in UECP), Spooky Scary Sectopods (ability mod, no units), Stukov's Purifiers (weapon/ability mod, no units), AdvMec_M3_LW (in UECP as AdvMEC_M3_LW; names are case-insensitive), Derelict MECs / Neonate Vipers / Advent Hunter Revamp (UECP `UnitRequiredMods` switches them on when the mod is loaded), all Lost units (Lost lists untouched).

## Verify after the next launch

Launch.log (`C:\Users\Idi\Documents\my games\XCOM2 War of the Chosen\XComGame\Logs\Launch.log`): first check the load order (jepFixes must be the last `Checking DLC installation` line), then the ELR blocks `Lists after:` per logged list. Expect in DefaultLeaders: ARFMAdvOutriderM1, MutonAdolescent; in DefaultFollowers: ARFMAdvRunnerM1, ViperFrostling; in TerrorLeaders: SectoidTrooperM4. Lines `Unit template does not exist:` name any entry whose mod is missing (harmless, ELR skips it). Lines `No group defined with name:` mean a broken group reference (should be zero). Drop the log into `projects/XCOM/` or grant read access; jep greps it.

## Campaign levers (2026-09-19)

| File | Kind | What |
|---|---|---|
| `Config\XComGameBoard.ini` | additive | capture risk off (Configurable Posthumous Risks `+ChangeRisk` alwaysOff); 9 covert action names on Covert Infiltration's `CovertActionsPreventRandomSpawn` |
| `Config\XComGameData.ini` | additive | 31 faction orders on Covert Infiltration's `arrRemoveFactionCard` (kills order and continent-bonus forms); 6 of Idi's 37 held because they are his kept continent bonuses |

Spec and receipts: `projects/XCOM/faction-orders-covert-actions-2026-09-19.md`. Verify in game: Covert Actions screen shows no Soldier Captured risk and none of Teamwork Training, Intel Collection, Supply Run, Combat Preparedness, Scavenge Alien Loot, Our Experiment Now, Patrol Wilderness, Factory Reactivation; Resistance Orders never offer a listed card.

## Log

- 2026-09-11 created: 8 BodyPartTemplateConfig fixes.
- 2026-09-14 UECP extension: 4 files added, README rewritten (real defect per source line, verification recipe).
- 2026-09-14 second launch 17:00: extension LIVE, jepFixes check 1119/1120, all 29 pod units in the ELR dumps.
- 2026-09-14 first launch: extension NOT live, jepFixes loaded 6th. Cause: mod directory order. ModPaths swapped in settings.json; README load-order rule corrected. ELR also logs `No group defined with name: NemesisLeaders`, a UECP-side dangling reference (Nemesis group never defined), harmless.
- 2026-09-19 campaign levers: XComGameBoard.ini + XComGameData.ini added (capture risk off, 9 covert actions blocked, 31 orders removed); installed copy byte-identical to vault copy.
