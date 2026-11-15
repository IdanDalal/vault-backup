---
type: report
created: 2026-11-15
author: Agent items-fix
---
# jepFixes V1 + V2 applied (2026-11-15)

Status: both rulings written and replay-verified on the live files. The game was never launched, so nothing here is confirmed in play. Source audit: `block-audit-2026-11-12/items.md` sections 1, 3, 10 to 12.

Paths: `J\` = `...\XComGame\Mods\jepFixes\Config\`, `W\` = `...\steamapps\workshop\content\268500\`, `T\` = `C:\Users\jep\.claude\jobs\0815ca4d\tmp\`.

## 1. Files

| jepFixes file | bytes before | bytes after | sha256 (16) after | line endings | ASCII only |
|---|---|---|---|---|---|
| `XComGameCore.ini` | 9273 | 17108 | e087ab62bf0374df | CRLF | yes |
| `XComGame.ini` | 317 | 1114 | 654527f8e93a45e4 | CRLF | yes |
| `XComCorpseLooting.ini` | new file | 1501 | 2fa965454fbd6049 | CRLF | yes |
| `XComWeaponSkinReplacer.ini` | 21506 | 19234 | 723d6e28cfc40e12 | CRLF | yes |
| `XComContent.ini` | 2584 | 1035 | 43821a68743a70d9 | CRLF | yes |

Backups: `T\<name>.bak-1115` for the four edited files (`XComCorpseLooting.ini` is new, nothing to back up). Full revert = copy the four backups over `J\`, delete `J\XComCorpseLooting.ini`, copy the two moved files back.

| moved to `T\removed-1115\` | bytes | sha256 (16) | in jepFixes now |
|---|---|---|---|
| `XComTemplateEditor.ini` | 880 | 09d3b052472800e7 | gone |
| `XComEndgameWeapons.ini` | 2082 | ba9ec5e3dccb1a72 | gone |

Also in `T\removed-1115\`: `XComWeaponSkinReplacer.removed-lines.txt` (95 lines) and `XComContent.removed-lines.txt` (7 lines), the exact bytes taken out.

## 2. V1, what was written

1. **Route 1, Black Market.** `J\XComGameCore.ini:59-77`, own `[XComGame.X2LootTableManager]` header (the file's last header was `[XComGame.XGTacticalGameCore]`). Six `-LootTables` byte copies: `W\1335226018\Config\XComGameCore.ini:76,77,78` and `W\2164176007\Config\XComGameCore.ini:14,15,16`. Then three `+LootTables`, one per table name. Base game copies: no line needed, LW2 Classes and Perks already removes all three (`W\1335226018\...:72-74`, replay below).
2. **Route 2, More POI Types deck `EpicPCS`.** `J\XComGame.ini:7-15`, section `[RewardDeckBuilder.X2DownloadableContentInfo_RewardDeckBuilder]`, six `-AddItemsToDecks` byte copies of `W\2833889867\Config\XComGame.ini:49,50,52,55,59,60`. Declaring class: `W\2830998888\Src\RewardDeckBuilder\Classes\X2DownloadableContentInfo_RewardDeckBuilder.uc:11,19` (`var config array<ItemToDeck> AddItemsToDecks`, no config name of its own, parent `X2DownloadableContentInfo` is `Config(Game)`), so `XComGame.ini` is the right file.
3. **Route 3, ARFM Scavenger.** New file `J\XComCorpseLooting.ini`, section `[ARFMScavenger.ARFM_GameState_LootCorpse]`, 33 `-` byte copies from `W\3158385565\Config\XComCorpseLooting.ini`: CaptainLoot 9, LancerLoot 7, AdventLoot 7, AlienLoot 7, CorpseLoot 3. Declaring class: `W\3158385565\Src\ARFMScavenger\Classes\ARFM_GameState_LootCorpse.uc:1,4-13` (`config(CorpseLooting)`, ten `array<name>` lists, one entry per line, so no struct line had to be rebuilt). The other five lists (Muton, Andromelid, Berserker, Sectoid, Shieldbearer) are empty in the mod and unread by its code.
4. MOCX proving ground projects: untouched, as ruled.

How the `-` lines were made: `fix_v1_build.py` reads the source file's raw bytes, takes the physical line, swaps the leading `+` for `-`, writes it unchanged otherwise. None was typed.

### Black Market table design (the one judgment call)

Two source copies existed per table and they disagree on totals. Rule used: **entries = union of both copies minus the six types; each roll group's total = the larger of the two source totals**, split evenly among the survivors of that group. That keeps every roll group at or above both originals, whichever copy the game was using.

```
table / roll group | LW2 C&P total | Cut Content Psi total | jep total | jep entries
BlackMarketPCS_01 group 1 |  30 |  40 |  40 | RarePCSSpeed 40
BlackMarketPCS_01 group 2 | 105 |  50 | 105 | HyperReactivePupilsPCS 35, DepthPerceptionPCS 35, SmartMacrophagesPCS 35
BlackMarketPCS_01 group 3 |  15 |  50 |  50 | RarePCSPerception 25, RarePCSPsi 25
BlackMarketPCS_01 whole table | 150 | 140 | 195 |
BlackMarketPCS_01 entries: union of both sources 11, minus the six types 6, in the jep table 6, same set: True
BlackMarketPCS_02 group 1 |  60 |  60 |  60 | RarePCSSpeed 30, EpicPCSSpeed 30
BlackMarketPCS_02 group 2 |  60 |  60 |  60 | RarePCSPsi 30, EpicPCSPsi 30   (moved in from group 3: RarePCSPsi, EpicPCSPsi)
BlackMarketPCS_02 group 3 |  30 |  60 |  60 | RarePCSPerception 30, EpicPCSPerception 30
BlackMarketPCS_02 whole table | 150 | 180 | 180 |
BlackMarketPCS_02 entries: union of both sources 12, minus the six types 6, in the jep table 6, same set: True
BlackMarketPCS_03 group 1 |  30 |  60 |  60 | EpicPCSSpeed 60
BlackMarketPCS_03 group 2 | 105 |  40 | 105 | CombatRushPCS 27, IronSkinPCS 26, ImpactFieldsPCS 26, DamageControlPCS 26
BlackMarketPCS_03 group 3 |  15 |  60 |  60 | EpicPCSPerception 30, EpicPCSPsi 30
BlackMarketPCS_03 whole table | 150 | 160 | 225 |
BlackMarketPCS_03 entries: union of both sources 11, minus the six types 7, in the jep table 7, same set: True
every jep roll group equals the larger source total, no jep table below either source table, no surviving entry dropped: True
```

- `BlackMarketPCS_02` roll group 2 held only Focus and Agility (4 entries, all removed). Rare and Epic Psi moved from group 3 into group 2 so the table still makes three rolls of 60. Without that move the table would have dropped from 150/180 to 120.
- Side effect to know: against the LW2 copy (the first one in the array, the later Cut Content copy is the one the log calls duplicate), some groups rise: `_01` group 3 15 to 50, `_03` group 1 30 to 60, group 3 15 to 60. Effect: more PCS on the Black Market shelf from those groups. Alternative if unwanted: LW2 totals only (30/105/15, 60/60/30, 30/105/15).
- Psionics Ex Machina 2222545926 adds a roll group 4 entry to these three tables by name at run time (`XComPsionicsExMachina.ini:259-261`). It finds one table per name now. Untouched.

## 3. V1 replay (live files: base + 5 DLC + 1081 active mods in engine order + jepFixes)

Replay check on itself: run on the pre-fix files, it puts the duplicate `BlackMarketPCS_01/02/03` at array indexes 359, 360, 361. The game's own log names the same three indexes (`Launch.log:29453-29455`, 11-14 session). Mod order was compared with that log's 1140 "Checking DLC installation" lines: same order for all 1133 settings entries.

Route 1:
```
GameCore files merged: 109
events touching /BlackMarketPCS/:
  ADD     BASE|DefaultGameCore.ini:538  BlackMarketPCS_01
  ADD     BASE|DefaultGameCore.ini:539  BlackMarketPCS_02
  ADD     BASE|DefaultGameCore.ini:540  BlackMarketPCS_03
  REMOVE  by 1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:72  -> entry from BASE|DefaultGameCore.ini:538 (case-exact True)  BlackMarketPCS_01
  REMOVE  by 1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:73  -> entry from BASE|DefaultGameCore.ini:539 (case-exact True)  BlackMarketPCS_02
  REMOVE  by 1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:74  -> entry from BASE|DefaultGameCore.ini:540 (case-exact True)  BlackMarketPCS_03
  ADD     1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:76  BlackMarketPCS_01
  ADD     1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:77  BlackMarketPCS_02
  ADD     1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:78  BlackMarketPCS_03
  NO-MATCH '-' at 2164176007:CutContentPsionicsWOTC|XComGameCore.ini:10  BlackMarketPCS_01
  NO-MATCH '-' at 2164176007:CutContentPsionicsWOTC|XComGameCore.ini:11  BlackMarketPCS_02
  NO-MATCH '-' at 2164176007:CutContentPsionicsWOTC|XComGameCore.ini:12  BlackMarketPCS_03
  ADD     2164176007:CutContentPsionicsWOTC|XComGameCore.ini:14  BlackMarketPCS_01
  ADD     2164176007:CutContentPsionicsWOTC|XComGameCore.ini:15  BlackMarketPCS_02
  ADD     2164176007:CutContentPsionicsWOTC|XComGameCore.ini:16  BlackMarketPCS_03
  REMOVE  by jepFixes:jepFixes|XComGameCore.ini:63  -> entry from 1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:76 (case-exact True)  BlackMarketPCS_01
  REMOVE  by jepFixes:jepFixes|XComGameCore.ini:65  -> entry from 1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:77 (case-exact True)  BlackMarketPCS_02
  REMOVE  by jepFixes:jepFixes|XComGameCore.ini:67  -> entry from 1335226018:LongWar2AbilitiesforWotC|XComGameCore.ini:78 (case-exact True)  BlackMarketPCS_03
  REMOVE  by jepFixes:jepFixes|XComGameCore.ini:69  -> entry from 2164176007:CutContentPsionicsWOTC|XComGameCore.ini:14 (case-exact True)  BlackMarketPCS_01
  REMOVE  by jepFixes:jepFixes|XComGameCore.ini:71  -> entry from 2164176007:CutContentPsionicsWOTC|XComGameCore.ini:15 (case-exact True)  BlackMarketPCS_02
  REMOVE  by jepFixes:jepFixes|XComGameCore.ini:73  -> entry from 2164176007:CutContentPsionicsWOTC|XComGameCore.ini:16 (case-exact True)  BlackMarketPCS_03
  ADD     jepFixes:jepFixes|XComGameCore.ini:75  BlackMarketPCS_01
  ADD     jepFixes:jepFixes|XComGameCore.ini:76  BlackMarketPCS_02
  ADD     jepFixes:jepFixes|XComGameCore.ini:77  BlackMarketPCS_03
final LootTables entries: 658
duplicate table names in final array: {}
tables in the whole final array still holding one of the six types: 0
FINAL tables matching /BlackMarketPCS/:
  [655] BlackMarketPCS_01  from jepFixes:jepFixes|XComGameCore.ini:75  table total=195
      RollGroup 1 total=40: RarePCSSpeed 40
      RollGroup 2 total=105: HyperReactivePupilsPCS 35, DepthPerceptionPCS 35, SmartMacrophagesPCS 35
      RollGroup 3 total=50: RarePCSPerception 25, RarePCSPsi 25
      entries of the six types: 0 []   loose-name hits: 0
  [656] BlackMarketPCS_02  from jepFixes:jepFixes|XComGameCore.ini:76  table total=180
      RollGroup 1 total=60: RarePCSSpeed 30, EpicPCSSpeed 30
      RollGroup 2 total=60: RarePCSPsi 30, EpicPCSPsi 30
      RollGroup 3 total=60: RarePCSPerception 30, EpicPCSPerception 30
      entries of the six types: 0 []   loose-name hits: 0
  [657] BlackMarketPCS_03  from jepFixes:jepFixes|XComGameCore.ini:77  table total=225
      RollGroup 1 total=60: EpicPCSSpeed 60
      RollGroup 2 total=105: CombatRushPCS 27, IronSkinPCS 26, ImpactFieldsPCS 26, DamageControlPCS 26
      RollGroup 3 total=60: EpicPCSPerception 30, EpicPCSPsi 30
      entries of the six types: 0 []   loose-name hits: 0
```

Routes 2 and 3:
```
=== Route 2: [RewardDeckBuilder.X2DownloadableContentInfo_RewardDeckBuilder] AddItemsToDecks (config Game) ===
  Game files merged: 986  final AddItemsToDecks entries: 111
  '-' lines applied: 6 (case-exact 6)   '-' lines with NO match: 0   clears/plain sets: 0
  removals by file owner: {'jepFixes:jepFixes': 6}
  FINAL deck EpicPCS: 13 items: EpicPCSSpeed, EpicPCSPerception, DepthPerceptionPCS, HyperReactivePupilsPCS, CombatRushPCS, DamageControlPCS, ImpactFieldsPCS, IronSkinPCS, SmartMacrophagesPCS, EpicPCSPsi, EpicPCSHacking, LongJumpPCS, MimeticSkinPCS
  contributors: ['2833889867:MorePOITypes']
  entries of the six types in EpicPCS: []  loose-name hits: []
  six-type items in any other deck built by this key: []
=== Route 3: [ARFMScavenger.ARFM_GameState_LootCorpse] loot lists (config CorpseLooting) ===
  CorpseLooting files merged: ['3158385565:ARFMScavenger', 'jepFixes:jepFixes']
  CaptainLoot      final 20 entries | removed 9, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: CommonPCSSpeed, CommonPCSPerception, RarePCSSpeed, RarePCSPerception, EpicPCSSpeed, EpicPCSPerception
  LancerLoot       final 23 entries | removed 7, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: CommonPCSPerception, RarePCSPerception, CommonPCSSpeed, RarePCSSpeed, EpicPCSSpeed
  AdventLoot       final 23 entries | removed 7, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: CommonPCSPerception, RarePCSPerception, CommonPCSSpeed, RarePCSSpeed, EpicPCSSpeed
  AlienLoot        final 23 entries | removed 7, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: CommonPCSPerception, RarePCSPerception, CommonPCSSpeed, RarePCSSpeed, EpicPCSPerception
  CorpseLoot       final 13 entries | removed 3, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: CommonPCSSpeed, CommonPCSPerception
  MutonLoot        final  0 entries | removed 0, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: -
  AndromelidLoot   final  0 entries | removed 0, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: -
  BerserkerLoot    final  0 entries | removed 0, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: -
  SectoidLoot      final  0 entries | removed 0, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: -
  ShieldbearerLoot final  0 entries | removed 0, no-match 0 | six-type left 0 [], loose hits 0 | PCS left: -
```

## 4. V2, what was removed

1. `J\XComWeaponSkinReplacer.ini`: 95 `+WEAPONS_TO_HIDE` lines out (509 to 414). Head comment at line 4; the six emptied group headers and the Resistance Firearms header carry a dated note.
2. `J\XComContent.ini`: the six Mandalorian helmet lines and their `; source:` comment out, one dated comment in. The two Mass Effect lines are byte-identical to before. Line 2 still says "8 entries" (history, left alone).
3. `XComTemplateEditor.ini`, `XComEndgameWeapons.ini`: moved. Checked first: the first holds 2 entries, both the CBR Redux schematic edits; the second holds 30 entries, all in package `EndgameWeapons`. No active mod ships that package, an `XComEndgameWeapons.ini`, or names the two schematics.

### The 95 names, re-derived from the current active set

Method: every hide name against every mod in `settings.json`, whole-token match in `Src\*.uc`, `Config\**\*.ini`, `Localization\**`, plus compiled `Script\*.u` of active mods and every `Launch*.log` line. Run on the pre-fix file.

```
hide-list file: C:\Users\jep\.claude\jobs\0815ca4d\tmp\XComWeaponSkinReplacer.ini.bak-1115
names: 509 | distinct: 509 | odd chars: []
mods in settings.json: 1133 | active: 1081
compiled .u files of active mods scanned: 1016 | logs scanned: 3 | hide names seen in a log: 310 | hide names in an active .u: 113
A dead, inactive-only: 87 (of them named by an inactive mod: 87)
   by first inactive owner: {'1349983893:ValhallaRifles': 26, '2211497852:RE2_Weapons_Test': 14, '1838499827:EndgameWeapons': 15, '1935901704:AlbionPlanetside2NCWeapons': 21, '1773508826:N7Weapons': 10, '1701830636:MercPlasmaHeroWeapons': 1}
B dead, no template (Localization-only mention by active mods): 8: ['TC_WOTC_S79_XM16E1_T1', 'TC_WOTC_S79_XM16E1_T2', 'TC_WOTC_S79_XM16E1_T3', 'TC_WOTC_SKR_MWR_M21_T1', 'TC_WOTC_SKR_MWR_M21_T2', 'TC_WOTC_SKR_MWR_M21_T3', 'TC_WOTC_SKR_S79_XM16E1_T2', 'TC_WOTC_SKR_S79_XM16E1_T3']
   their owners: ['1132835147:ResistanceFirearms_WotC_Data']
C kept and reported (Resistance Firearms config names them, no line creates them, never in a log): 4: ['TC_WOTC_SKR_S79_XM16E1_T1', 'TC_WOTC_TMP_MWR_M9_T1', 'TC_WOTC_TMP_MWR_M9_T2', 'TC_WOTC_TMP_MWR_M9_T3']
kept: 414 | of them seen in a log: 310 | with a .uc or .ini or .u mention in an active mod: 414
```

- A = 87: no active mod names them anywhere, no log line, inactive owner found for each.
- B = 8: the same 8 the audit listed. Resistance Firearms 1132835147 names them in localization only; no `.uc`, no `.ini`, no `.u`, no log line.
- **C = 4, found by this pass, left in the file:** `TC_WOTC_SKR_S79_XM16E1_T1`, `TC_WOTC_TMP_MWR_M9_T1/T2/T3`. Resistance Firearms config refers to them (`NewWeaponToHQ`, upgrade matches, a Grimy Loot list) but no `CVWPdata_T<n>_TemplateName` line creates them (309 of the mod's 321 hide names have one), and no log has them. Probably dead too (medium confidence: the absence test is the same as for B, but config mentions exist). Outside the ruled 95, so kept. Harmless either way.
- Per-name evidence: `T\audit\fix_wsr_scan.tsv`.

## 5. V2 replay (live files)

```
=== WEAPONS_TO_HIDE (config WeaponSkinReplacer) ===
  files merged: ['1584992858:WOTC_TLP_Cannon_Vanilla_Anim', '1701209115:NewShotgunAnimations', '1709345052:zzzWeaponSkinReplacerConfig', '1726550197:WOTC_TLP_V_Weapons', '1745325917:SlagAndMelta', '1750855914:WOTC_TLP_3_Weapons', '1898540490:WOTC_TLP_Fudge', '1948941654:WOTC_Multishot_Plasma_Rifle', '2058741060:WOTC_TLP_V_2_Weapons', '2127166233:WOTCMoreSparkWeapons', '2170720621:ThePatriotWarOfTheChosen', '2224463798:WOTC_MorePsiAmps', '2254206296:NelVlesis_Icon_Overrides', '2310533632:ShieldRework', '2428993550:AmalgamationClassesWOTC', '2608963616:PexMforTemplar', '2681055768:mocxadventarsenal', '2696763989:2022DPReskinMod', '2728208078:StukovWarPerkPack', "2761660432:[WOTC]Stukov'sWarEnhancedEnemies-LostandMore", '2798084598:ZelfanasAssortedFixesConfig', '2811243277:AmalgamationPathfinder', '2864298891:AmalgamationSpecsRichardsClasses', '2876755199:BigThingsDontGetHugs', '2895282660:WSR_NewShotgunAnimation_Addon', '2962703655:Unique-ishVektorCrossbow', "2978459982:[WOTC]Stukov'sWarEnhancedEnemiesPurifiers", '2981314573:randomupgrade', '3246095691:MCFactionAmalgamation', '3284612057:2024MOCXMecTrooper', '3314720537:OddS9Tweaks', '3347699211:StrategyOverhaulBridgeHarbingerRifle', '3350314521:FiveTierWeaponOverhaul', '3350314521:FiveTierWeaponOverhaul', '3444054961:NerosAdventGear', '3444054961:NerosAdventGear', '3444054961:NerosAdventGear', '3583339838:Chosen_Arashi_SFX_Fix', 'jepFixes:jepFixes']
  before: 513 names | after: 418 names | gone: 95 | added: 0
  gone == the 95 dead names: True | dead names still present: 0 | events other than add: ['dup+']
  contributors after: ['3347699211:StrategyOverhaulBridgeHarbingerRifle', 'jepFixes:jepFixes']
  order of the kept names unchanged: True
=== BodyPartTemplateConfig lines owned by jepFixes (config Content) ===
  before: 8 ['ORMandos_Helmet_MercilessSeeker_M', 'ORMandos_Helmet_MercilessSeeker_F', 'ORMandos_Helmet_Shae_M', 'ORMandos_Helmet_ShaeCommander_M', 'ORMandos_Helmet_Shae_F', 'ORMandos_Helmet_ShaeCommander_F', 'HPT_DemolisherLegsDeco', 'HPT_DemolisherLegsDeco_M']
  after : 2 ['HPT_DemolisherLegsDeco', 'HPT_DemolisherLegsDeco_M']
  Mandalorian lines left: 0 | the two Mass Effect lines byte-identical to before: True
=== moved files ===
  XComTemplateEditor.ini     in jepFixes: False | in removed-1115: True  (880 bytes)
  XComEndgameWeapons.ini     in jepFixes: False | in removed-1115: True  (2082 bytes)
  Edit_X2SchematicTemplate entries naming MBR_MJ_* in the merged config (live): 0
  files named XComEndgameWeapons.ini in the merged set: []
```

513 before = 509 jepFixes + 4 from the Harbinger Rifle bridge 3347699211.

## 6. What the next launch log should show (probes, unverified until then)

1. No `LootTable index ... has a duplicate name (BlackMarketPCS_0x) - INVALID` line (6 per launch before).
2. `Reward Deck Rebuilder: EpicPCS  contains  13` (19 before, `Launch.log:57208`).
3. No `TEMPLATE_MASTER: ERROR :: GetTemplates failed ... MBR_MJ_MG_Schematic` / `MBR_MJ_BM_Schematic` (2 per launch before).

## 7. Not done, and limits

1. MOCX `RM_BasicPCS` / `RM_AdvPCS`: untouched by ruling (hard-coded rewards).
2. Running campaign: PCS of the six types already owned, and any already on the Black Market shelf in the save, stay. The shelf re-rolls from the new tables at its next reset. The `EpicPCS` deck shrinks on the first Avenger screen after load (`UISL_DeckBuilder.uc:75-78` removes cards no template claims).
3. Which duplicate table the game used before the fix is native code. The log flags the later (Cut Content) copy as the duplicate, so the LW2 copy was probably the live one (medium confidence). The design above is safe under both readings.
4. The 4 class C names above: a ruling to remove them would make it 99.
5. Scripts: `T\audit\fix_*.py` (`fix_v1_build.py`, `fix_v2_build.py`, `fix_commit.py`, `fix_move.py`, replays `fix_replay_loot.py`, `fix_replay_keys.py`, `fix_replay_v2.py`, scan `fix_wsr_scan.py`).
