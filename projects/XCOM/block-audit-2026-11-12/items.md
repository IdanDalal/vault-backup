---
type: report
created: 2026-11-12
author: Agent audit-items
---
# jepFixes block audit - items, loot, weapons, enemies, class screen

Audit date 2026-11-12. Read-only. Scope: the jepFixes files named in the brief, `XComAmalgamation.ini` excluded.

Ground facts used by every block:
- Active set read from `C:\XCOM2 AML 1.6.0-beta\settings.json`: 1132 entries, 1080 active. jepFixes is active (entry Index 1094).
- Logs on disk now: 8 files, `Launch-backup-2026.11.09-14.46.32.log` through `Launch.log` (11-12 13:04). The 11-09 12:23 backup has rotated out since the first pass. Short names below: `LB-11.09-14.46.32` = `Launch-backup-2026.11.09-14.46.32.log`; `Launch.log` = the 11-12 session.
- The engine scans mod folders in this order: workshop ids ascending, then the game `Mods\` folder (`Launch.log:2360`, jepFixes is entry 1134 of 1139). jepFixes merges after every workshop mod.
- `-` lines were tested with a script that copies the engine's line reader (joins `\\` line breaks the way `ParseLineExtended` does, trims around key and value as `FConfigFile::Combine` does) and then compares values as raw text.
- Paths: `W\` = `C:\Program Files (x86)\Steam\steamapps\workshop\content\268500\`, `J\` = the jepFixes `Config\` folder, `SDK\` = `...\XCOM 2 War of the Chosen SDK\Development\SrcOrig\XComGame\Classes\`.

---

## 1. PCS loot tables (`J\XComGameCore.ini:6-50`)

**Intent.** Remove six PCS types at every tier (Agility, Conditioning, Focus, Combat Awareness, Emergency Life Support, Body Shield): delete the Cut Content Psionics and Odd S9 `PCSDropsBasic/Rare/Epic` tables, add one jep table per tier without the six.

**Lever.** `[XComGame.X2LootTableManager]`, key `LootTables`, class `X2LootTableManager extends X2LootTable ... config(GameCore)` (`SDK\X2LootTableManager.uc:1-3`); file name `XComGameCore.ini` matches. All six `-` lines match a `+` line in an active mod, case-exact:
- `J:8,10,12` = `W\2164176007\Config\XComGameCore.ini:6,7,8` (Cut Content Psionics, active)
- `J:14,26,37` = `W\3314720537\Config\XComGameCore.ini:75,86,96` (Odd S9, active)
- No `-` line without a match. Merge replay (base, LW2 Classes and Perks 1335226018, Cut Content Psionics, Odd S9, jepFixes) ends with exactly one `PCSDropsBasic`, one `PCSDropsRare`, one `PCSDropsEpic`, all three from `J:48-50`, each summing to 100, none holding any of the six.

**Log evidence for the tables.** The game's own loot table check runs every launch and reports duplicate table names. It reports `BlackMarketPCS_01/02/03` as duplicates (`Launch.log:29281-29283`, same three lines in all 8 logs) and reports no `PCSDrops*` duplicate in any log (0 hits for `PCSDrops` across 8 logs). The replay predicts exactly that pattern: without the jep `-` lines there would be three copies of each `PCSDrops*` table and the check would name them, as it did before the 09-27 fix. So the six removal lines apply in the live game.

**Bypass.** Four routes hand out the six types without reading `PCSDrops*`:
1. **Black Market.** `RollForBlackMarketLoot` rolls carrier `BlackMarket` (`SDK\XComGameState_BlackMarket.uc:362-380`), which reaches `BlackMarketPCS_01/02/03` (`DefaultGameCore.ini:542-544`). Two live copies of each exist: LW2 Classes and Perks `W\1335226018\Config\XComGameCore.ini:76-78` and Cut Content Psionics `W\2164176007\Config\XComGameCore.ini:14-16`. Both copies contain Rare/Epic Conditioning, Focus, Agility; the LW2 copy also has Emergency Life Support, Combat Awareness (`_01`) and Body Shield (`_03`). jepFixes has no line touching them. The Black Market screen was opened in the live campaign (`LB-11.10-13.28.40:97985-97987`, `Launch.log:104499`).
2. **More POI Types 2833889867, reward deck `EpicPCS`.** `W\2833889867\Config\XComGame.ini:48-66` puts 19 items in the deck, all six removed types among them (`:49,50,52,55,59,60`). The log confirms the deck is built with 19 entries: `Launch.log:101505` "Reward Deck Rebuilder: EpicPCS contains 19" (same line in all 8 logs). The deck feeds `Reward_MZSPCS` (`:14`) through `POI_SPCS` (`:33`). The POI had not spawned as of `LB-11.10-13.28.40:96047` (`OriginalNumSpawns 0`).
3. **ARFM Scavenger 3158385565.** `W\3158385565\Config\XComCorpseLooting.ini:13-27` (`CaptainLoot`) and `:64-70` onward (`LancerLoot`) list Common/Rare/Epic Focus, Agility, Conditioning as direct drops of the "Mark For Equipment Salvage" ability. The ability exists in the running game (`Launch.log:38673`).
4. **MOCX (Dark XCOM Redux 1129661000) proving ground projects** `RM_BasicPCS` / `RM_AdvPCS`: hard-coded rewards Conditioning, Agility, Focus (`W\1129661000\Src\DarkXCOMRedux\Classes\X2StrategyElement_MOCXTechs.uc:158-162,188-192`). No log line shows either project run.

No log line names a PCS template when one is awarded, so the logs cannot show a removed type landing in inventory by any route.

**Verdict.**
- `PCSDrops*` tables (mission loot, `Reward_SuperiorPCS`, anything using `PCSDropsEpic`): **HOLDING**. Positive evidence: the duplicate check is silent on `PCSDrops*` while flagging its neighbours.
- The ruling "remove at every tier": **FAILING as a whole**. Routes 1 and 2 are live in the running game by log evidence (duplicate `BlackMarketPCS` tables loaded, `EpicPCS` deck = 19). Routes 3 and 4 are open on source and config.
- Probe to see an actual leak: open the Black Market and read the PCS stock; the `EpicPCS` deck needs no probe, its logged count of 19 already matches the 19 config lines.

---

## 2. Starting roster (`J\XComGameCore.ini:55-57`)

**Intent.** 40 starting soldiers (base 12, Covert Infiltration 16).

**Lever.** `[XComGame.XGTacticalGameCore]`, `var config int NUM_STARTING_SOLDIERS` (`SDK\XGTacticalGameCoreNativeBase.uc:650`, GameCore). Covert Infiltration writes `-NUM_STARTING_SOLDIERS = 12` / `+NUM_STARTING_SOLDIERS = 16` (`W\2567230730\Config\XComGameCore.ini:28-29`); after trimming, its value is `16`, which `J:56` removes, then `J:57` adds `40`. Only three files set the key (base, CI, jepFixes).

**Bypass.** One consumer: the start-of-campaign loop `XComGameState_HeadquartersXCom.uc:1574`. Runs once, at campaign creation.

**Log evidence.** None possible: the campaign began 11-08 and the oldest log left is 11-09 14:46. No log line prints roster size.

**Verdict. UNPROVEN** from logs. Probe: count the soldiers recruited on day one in the Armory list (40 expected); Idi has seen that screen.

---

## 3. Weapon hide list (`J\XComWeaponSkinReplacer.ini`, 509 lines)

**Intent.** Turn 509 weapon templates into skins only: never a starting item, never buildable, never in the locker, still wearable as a look through XSkin.

**Lever.** Section `[zzzWeaponSkinReplacer.X2DownloadableContentInfo_WeaponSkinReplacer]`, key `WEAPONS_TO_HIDE`, declared `var config(WeaponSkinReplacer) array<name> WEAPONS_TO_HIDE` (`W\1517938486\Src\zzzWeaponSkinReplacer\Classes\X2DownloadableContentInfo_WeaponSkinReplacer.uc:314`). File name, section, key all match; mod 1517938486 active. 509 `+` lines, 509 distinct names, no stray characters. No `-` lines.
- 414 names are mentioned by at least one active mod. 311 of them are confirmed live templates by the log (`ESP: Weapon calls for difficulty templates adjustment : <name>`, e.g. `LB-11.09-14.46.32:42721`).
- **87 names belong only to inactive mods** (CBR Redux 26, Planetside 2 NC 21, Avengers Endgame 15, RE2 Weapons 14, N7 Weapons 10, Merc Plasma 2): dead lines, harmless.
- **8 names match no template anywhere** (`TC_WOTC_S79_XM16E1_T1/T2/T3`, `TC_WOTC_SKR_MWR_M21_T1/T2/T3`, `TC_WOTC_SKR_S79_XM16E1_T2/T3`): no mod source has them and the log's weapon dump has no XM16 at all. Dead lines.

**What the code does.** `HideWeapons` (`...WeaponSkinReplacer.uc:679-718`) runs when the main menu opens (`UIScreenListener_WSR.uc:19-27`), after every other mod's template edits. Per name it sets `StartingItem=false`, `CanBeBuilt=false`, `HideInInventory`, `HideInLootRecovered`, clears `BaseItem` and `CreatorTemplateName`, and switches the schematic off. In the campaign, `UpdateStorage` (`:1760-1824`) deletes every listed weapon from HQ storage on the first strategy screen of a session and on every load into strategy (`:434-436`, `UIScreenListener_WSR.uc:53-57`).

**Bypass, two open gaps.**
1. **One copy of five gets edited.** `HideWeapons` fetches each weapon with `FindItemTemplate` (`:690`), which returns one difficulty copy. The log shows the hidden weapons have five copies each: `LB-11.09-14.46.32:42721-42722` "TC_WOTC_S79_AK47_T1 ... Number of templates : 5". The same mod uses `FindDataTemplateAllDifficulties` elsewhere (`:1013-1016`), so its author treats the copies as separate. Which copy the main menu returns is native code I cannot read. If it is not the Legend copy, the Legend campaign keeps `StartingItem`, `CanBeBuilt` and the schematic link, and only the in-campaign storage sweep protects the list.
2. **Resistance Firearms re-adds its guns on load.** `UpdateStorageOnEveryLoad` (`W\1132835147\Src\00_ResFirm_Master_Data\Classes\X2DownloadableContentInfo_RFData_WotC.uc:125-158`) creates every `NewWeaponToHQ` item in HQ on each load into strategy, ignoring all template flags. 307 hidden names are on that list. It ran in the live campaign: `LB-11.10-13.28.40:79059` "CVWP: Starting OnLoadedSavedGameToStrategy". The hide mod's sweep answers it on the same event; the order of the two is not logged.

**Log evidence.**
- The hide mod prints nothing about hiding: `ENABLE_LOGGING = false` (`W\1709345052\Config\XComWeaponSkinReplacer.ini:33`). 0 hits for `WEAPONS_TO_HIDE` in 8 logs.
- For: Ability To Slot Reassignment lists the weapons soldiers carry into missions, 226 lines, 28 distinct templates across 6 logs (e.g. `LB-11.11-16.56.21:137194`). None of the 509 hidden names is among them.
- For the skin half: `LB-11.10-10.53.43:84432` "SniperRifle_CV TLP_F_Sniper_BM", XSkin applying a hidden weapon as a look.
- No hidden name appears in any loot, reward or inventory line; the only other hits are the template dump above and 80 "Could not find Fanfire anim" warnings.

**Verdict. UNPROVEN.** The evidence leans to holding (zero hidden weapons carried in 226 samples), but nothing in the logs shows the locker or the build list, and gap 1 is exactly the kind of failure that looks right in config. Probe: Armory, any rifle soldier, primary weapon list: an entry named "AK-47 Type 1" (or any Resistance Firearms gun) means the list is failing; none means holding. Second look: Engineering build list for the same names.

---

## 4. Enemy lists (`J\XComELR.ini`, `J\XComELR_groups.ini`, `J\XComELR_overrides.ini`)

**Intent.** Replace the Universal Enemy Compatibility Patch (UECP 3034030070) groups and overrides with a full copy plus jep additions, and print two extra lists to the log.

**Lever.** One section for all three files: `[EncounterListReplacerWOTC.X2DownloadableContentInfo_EncounterListReplacerWOTC]`. Declarations in `W\2337729548\Src\EncounterListReplacerWOTC\Classes\X2DownloadableContentInfo_EncounterListReplacerWOTC.uc`: `var config(ELR_groups) array<GroupStruct> Groups` (`:50`), `var config(ELR_overrides) array<OverrideStruct> Overrides` (`:53`), `var config(ELR) array<name> ListsToLog` (`:56`). The three jep file names match the three config names. Both mods active. No `-` lines; the files use `!Groups=()` and `!Overrides=()` (wipe by key, no text match needed) then `+` lines.
- Parsed diff against UECP: 127 groups in both, 76 overrides in both, same names. jep adds **35 unit entries = 28 distinct units** in 13 groups, plus 4 distinct units as override Extras (`SectoidTrooperM4` on `TerrorLeaders` `J\XComELR_overrides.ini:179`; `FrostAbomination` on `ForcedBossLeader` `:333` and `ForcedBossLeader_PsionicStorm` `:501`; `AdvGeneralM1_LW`, `AdvGeneralM2_LW` on `NeutralizeFieldCommander_FieldLeader` `:422`). That is 32 distinct units; the brief says 33, I could not find a 33rd.

**Bypass.** `OverrideLists` runs once in `OnPostTemplatesCreated` (`:60-73`); a list with no override keeps its vanilla content. That is by design and the same as UECP.

**Log evidence (`Launch.log`, same counts in all 8 logs).**
- All 32 unit templates exist: each is in the mod's own unit dump (`Launch.log:10159` onward, 1063 names). 0 "Unit template does not exist" and 0 "Missing Leader template" lines for any jep unit.
- "Lists after:" starts `Launch.log:16844`; six lists are printed, the two jep ones included (`TerrorLeaders` `:17933`, `TerrorFollowers` `:18277`), so `XComELR.ini` applies.
- 34 of the 35 added entries appear in every printed list their group feeds, e.g. `ARFMAdvOutriderM3` `Launch.log:16849`, `ARFMAdvRunnerM1` `:17206`, `ARFMAdvKnightM1` `:17286`, `MutonAdolescent` `:17136`, `AHWChryssalidMagnaM2` `:17101`, `FrostPudding_M3` `:18549`. The 35th (`FrostPudding_M3` in `FrostFollowers`) sits in a group that none of the six printed lists uses.
- `SectoidTrooperM4` is in the printed `TerrorLeaders` list.
- In play: the spawner picked a jep unit as pod leader and follower (`LB-11.09-19.25.31:71860` "DiverseAliensByFL: Leader - MutonAdolescent", `:71826`), and it died in missions (`LB-11.09-14.46.32:56787` "WOTC_Equal_XP: Dead enemy: MutonAdolescent", `LB-11.10-10.53.43:58240`). `ARFMAdvRunnerM1` is weighed as a candidate (`LB-11.10-10.53.43:81955`).
- One inherited fault, not jep's: `ELR: No group defined with name: NemesisLeaders` once per launch (`LB-11.09-14.46.32:14763`); UECP's own file has the same reference and no such group.

**Verdict.**
- Groups (35 entries) + `TerrorLeaders` extra + `ListsToLog`: **HOLDING**, on list dumps and on a jep unit spawning and dying in the campaign.
- `FrostAbomination` (2 boss lists) and `AdvGeneralM1_LW/M2_LW` (field commander list): **UNPROVEN**. Templates exist, lever identical to the proven lines, but those three lists are not printed. Probe: add `+ListsToLog="ForcedBossLeader"`, `+ListsToLog="ForcedBossLeader_PsionicStorm"`, `+ListsToLog="NeutralizeFieldCommander_FieldLeader"` to `J\XComELR.ini` and read the next launch's "Lists after:" block.

---

## 5. Basic Immolator made infinite again (`J\XComStrategyTuning.ini:6-7`)

**Intent.** Remove the Immolator Overhaul line that makes `MZImmolator_CV` buildable and finite, so strips stop minting copies.

**Lever.** `[PrototypeArmoury.PATemplateMods]`, `class PATemplateMods ... config(StrategyTuning)` with `var config array<ItemFromDLC> arrMakeItemBuildable` (`W\2567230602\Src\PrototypeArmoury\Classes\PATemplateMods.uc:1,4`). File name matches. The `-` line `J:7` equals `+arrMakeItemBuildable=(ItemName="MZImmolator_CV")` at `W\2237137501\Config\Compatibility\XComStrategyTuning.ini:2` (active), raw text identical. It is the only `+` line for that item in any active mod.

**Bypass.** The consumer is one loop (`PATemplateMods.uc:57-65`; it sets `CanBeBuilt=true`, `bInfiniteItem=false` at `:111-112`, on all difficulty copies). No other active config or script makes `MZImmolator_CV` finite.

**Log evidence.** Prototype Armoury prints the array length on every launch: `PrototypeArmoury: Making 156 items buildable` (`LB-11.09-14.46.32:19223`, same in all 8 logs). A replay of every active `arrMakeItemBuildable` line gives **156 with jepFixes, 157 without**. The live count equals the count with the removal applied. The weapon is in use (`LB-11.12-12.07.47:138111`).

**Verdict. HOLDING.**

---

## 6. Class choice count (`J\XComChooseMyClass.ini:3-4`)

**Intent.** Show 100 class cards at rookie promotion (mod default 3, Odd S9 5).

**Lever.** `[WOTC_ChooseMyClass.UIChooseClass_WOTC_ChooseMyClass]`, `class UIChooseClass_WOTC_ChooseMyClass ... config(ChooseMyClass)`, `var config int NumClassChoices` (`W\1467643380\Src\WOTC_ChooseMyClass\Classes\UIChooseClass_WOTC_ChooseMyClass.uc:1,7`). File name matches. Plain key, last file read wins: mod `=3` (`W\1467643380\Config\XComChooseMyClass.ini:10`), Odd S9 `=5` (`W\3314720537\Config\XComChooseMyClass.ini:4`), jepFixes `=100` read last. No `XComChooseMyClass.ini` exists in `Documents\...\XComGame\Config`, so no saved user copy overrides it.

**Bypass.** None found: the roll uses `Max(default.NumClassChoices, 1)` (`:383`). The Amalgamation Promotion Assistant has a separate `NumClassChoices = -1` in a different class (`W\3313946064\Config\XComUI.ini:7`), which does not touch this screen.

**Log evidence.** The screen is the one in use: 88 opens (`LB-11.09-14.46.32:59243`) and classes picked through it (`LB-11.09-14.46.32:59286` "Chosen Class is: XenoZoologist_Gunslinger_SkvScout"). The number of cards is logged only under the debug flag of the mod, which is off: 0 "Number of choice options" lines.

**Verdict. UNPROVEN** on the number. Probe: at the next rookie promotion, scroll the list; more than 5 cards proves jepFixes won over Odd S9, about 100 proves the value.

---

## 7. Nimble Hands weapon set (`J\XComAbilityToSlotReassignment.ini:5-6`)

**Intent.** Stop Ability To Slot Reassignment deleting Nimble Hands from rifle users by listing it under every main weapon.

**Lever.** `[AbilityToSlotReassignment.AbilityToSlotReassignmentLib]`, `class AbilityToSlotReassignmentLib ... config (AbilityToSlotReassignment)` (`W\2133397762\Src\AbilityToSlotReassignment\Classes\AbilityToSlotReassignmentLib.uc:6`). File name matches; the line has the same shape as the lines the mod ships (`W\2133397762\Config\XComAbilityToSlotReassignment.ini:49`); the set `AllMainWeapons` exists (`:7`: rifle, shotgun, cannon, sniper_rifle, bullpup, vektor_rifle, sparkrifle and two psi rifles). The competing entry is `SparkRifles` from Better Barracks (`W\3087936115\Config\XComAbilityToSlotReassignment.ini:15`).

**Bypass.** The fix depends on the Musashi Mods Fixes function merging both sets, as the jep comment says; I did not re-read that function. A Nimble Hands owner whose primary is outside `AllMainWeapons` (SMG, chemthrower) would still lose it.

**Log evidence.** 0 lines contain `NimbleHands` in 8 logs, although the mod logs each ability it moves (`LB-11.12-12.07.47:138112` for other abilities). No Nimble Hands owner has been seen in a mission.

**Verdict. UNPROVEN.** Probe: take a Rook (rifle) on a mission and look for Nimble Hands on the ability bar; or search the next log for `NimbleHands`.

---

## 8. Chosen reveal word wrap (`J\XComGame.ini:4-5`)

**Lever.** `[WOTCChosenTraitsUIRedux.CTURSJ_Watcher_UIChosenReveal]`, `class CTURSJ_Watcher_UIChosenReveal extends UIPanel config(Game)`, `var config bool bWordWrapDesc` (`W\3775978160\Src\WOTCChosenTraitsUIRedux\Classes\CTURSJ_Watcher_UIChosenReveal.uc:10,18`). File name matches; mod default `true` at `W\3775978160\Config\Base\XComGame.ini:27`; jepFixes read last. Consumer `:96-97`, no second path.

**Log evidence.** The reveal screen ran (`LB-11.10-13.28.40:59377` "Init UIChosenReveal"); nothing logs the wrap setting.

**Verdict. UNPROVEN** (cosmetic). Probe: the next Chosen reveal, by eye: one line per trait = holding.

---

## 9. ADVENT General buff whitelist (`J\XComAGData.ini:3-21`)

**Lever.** `[AdventGeneralRevamp.X2Ability_AdvGeneral]`, `class X2Ability_AdvGeneral ... config(AGData)`, `var config array <string> GENERAL_BUFF_ADVENT_BONUS` (`W\1241956143\Src\AdventGeneralRevamp\Classes\X2Ability_AdvGeneral.uc:1,24`). File name matches, mod active, 18 `+` lines, all 18 unit templates exist (same units as block 4, in the unit dump).

**Log evidence.** None: the mod prints nothing when the buff is applied.

**Verdict. UNPROVEN** (additive, low stakes). Probe: a mission with an ADVENT General and any Requiem ADVENT unit; the unit should show the buff icon of the General.

---

## 10. Body part repairs (`J\XComContent.ini`)

**Lever.** `[XComGame.X2BodyPartTemplateManager]`, key `BodyPartTemplateConfig`, the section and key every cosmetic mod uses; `XComContent.ini` matches.
- **Mass Effect pack, 2 lines (`J:13-14`), mod 2010492838 active.** The premise holds in the log: the two original lines fail to import on every load (`Launch.log:2464-2465` "Missing closing parenthesis", caused by `"HeavyPlatedArmor""` at `W\2010492838\Config\Demolisher\XComContent.ini:438,466`). The jep copies throw no import error. Nothing logs a body part being registered. **UNPROVEN.** Probe: a female soldier in Heavy Plated armour, Thighs list shows the Demolisher legs piece.
- **Mandalorians, 6 lines (`J:6-11`), mod 2376020557 INACTIVE.** The lines register six helmets whose meshes are not installed. **MOOT, with a possible side effect**: six helmet entries that render as nothing. No log line mentions them. Recommend removing the six lines while the mod is off.

---

## 11. CBR Redux schematics re-enabled (`J\XComTemplateEditor.ini:7-9`)

**Lever.** `[WOTCIridarTemplateMaster.X2DLCInfo_Last]`, key `Edit_X2SchematicTemplate`; Template Master 2363075446 active. The lines are read: Template Master answers them by name.

**Log evidence.** `TEMPLATE_MASTER: ERROR :: GetTemplates failed to find any templates for Template Name: MBR_MJ_MG_Schematic` and `..._BM_Schematic`, once each per launch in all 8 logs (`LB-11.09-14.46.32:28341-28342`).

**Verdict. MOOT / dead lines.** CBR Redux 1349983893 is inactive in this campaign, so the schematics do not exist. Two error lines per launch; remove the block or leave it for the day the mod returns.

---

## 12. Avengers Endgame weapons flattened (`J\XComEndgameWeapons.ini`)

**Verdict. MOOT.** Avengers Endgame Weapon Pack 1838499827 is inactive; no loaded class reads these keys, 0 log lines mention the mod or its weapons. The block neither holds nor fails. Its 15 names in the weapon hide list are dead lines too.

---

## Summary

| Block | Verdict | Reason | Probe if unproven |
|---|---|---|---|
| 1a. PCS `PCSDrops*` tables | HOLDING | All 6 `-` lines byte-match; the loot check flags no `PCSDrops` duplicate while flagging `BlackMarketPCS` ones, exactly as the replay predicts | - |
| 1b. PCS "six types gone at every tier" | **FAILING** | Four routes skip `PCSDrops*`: Black Market tables (two live copies, both with removed types), More POI Types `EpicPCS` deck (log: 19 entries, all six types inside), ARFM Scavenger salvage lists, MOCX proving ground projects | Open the Black Market, read the PCS stock |
| 2. Starting roster 40 | UNPROVEN | Lever correct; campaign start predates every log | Count day-one soldiers in the Armory |
| 3. Weapon hide list (509) | UNPROVEN | No hidden weapon in 226 logged mission loadouts; but the hide mod logs nothing, edits one of five difficulty copies per weapon, and Resistance Firearms re-adds 307 of them on load | Armory primary-weapon list: any "AK-47 Type 1" = failing |
| 3. dead lines in the hide list | n/a | 87 names from inactive mods, 8 names that match no template | - |
| 4a. Enemy groups + TerrorLeaders extra + ListsToLog | HOLDING | 34/35 entries in the live "Lists after" dump; MutonAdolescent spawned and died in missions | - |
| 4b. FrostAbomination, AdvGeneral LW extras | UNPROVEN | Three target lists are not printed | Add the three `+ListsToLog` lines |
| 5. Immolator `-arrMakeItemBuildable` | HOLDING | Log count 156 = replay with the removal (157 without) | - |
| 6. Class choices 100 | UNPROVEN | Screen in use, count not logged | Count cards at next promotion |
| 7. Nimble Hands set | UNPROVEN | 0 log lines for the ability | Rook on a mission |
| 8. Chosen reveal wrap | UNPROVEN | Cosmetic, nothing logged | Next Chosen reveal |
| 9. General buff whitelist | UNPROVEN | Additive, nothing logged | Mission with a General |
| 10a. Mass Effect leg parts | UNPROVEN | Originals fail in log, jep copies load without error, no registration line | Thighs list in Heavy Plated armour |
| 10b. Mandalorian helmets | MOOT | Target mod inactive; six meshless helmets possible | Remove the six lines |
| 11. CBR schematics | MOOT | Target mod inactive; Template Master logs 2 errors per launch | Remove or keep for later |
| 12. Endgame weapons | MOOT | Target mod inactive | - |

Scratch scripts (replays and scans) are in the same folder, prefix `items_`.
