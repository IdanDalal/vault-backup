---
type: research
created: 2026-09-27
author: jep
---

# Weapons research: items 1, 2, 8, 9 (read-only, nothing edited)

Path shorthand: `WS` = `C:\Program Files (x86)\Steam\steamapps\workshop\content\268500`, `SDK` = `...\XCOM 2 War of the Chosen SDK\Development\SrcOrig`, `JF` = `...\XComGame\Mods\jepFixes\Config`, `LOG` = `D:\work\vault\projects\XCOM\Launch.log`.
Note: No Missable Alien Hunter Upgrades is **3326247546** (the brief said 3326547546). Active, added 2025-07-06.

---

## ITEM 1: Alien Hunters tier 1 (Bolt Caster, Hunter Axe, Shadowkeeper, Frost Bomb)

### Verdict
Tier 1 was not removed. In this setup the four tier-1 weapons can only come from two places, and the player has hit neither:
1. **The Hunter Weapons POI** (a one-time scan site: "Locator Beacon" rumor, then "BigSky crash site"). Always possible.
2. **Proving Ground projects** after the Lab research **Experimental Weapons**. Possible only if the campaign was started with *Integrated DLC* enabled.

The Engineering build path for tier 1 is switched off by Alternative DLC Integration. The tier-2 Ionic Axe is buildable anyway because two mods together strip its "own the tier-1 axe" gate. That explains what the player sees: tier 2 appears, tier 1 never does.

### Mechanism, with receipts
- Alternative DLC Integration (3208771302) sets `SpecialRequirementsFn = AlwaysFalse` on all four tier-1 schematics (`HunterRifle_CV_Schematic`, `HunterPistol_CV_Schematic`, `HunterAxe_CV_Schematic`, `Frostbomb_Schematic`), so none of them can be built in Engineering. It sets `AlwaysTrue` on every MG/BM schematic. Author comment: "the weapons are now always obtained with resistance rumor". `WS\3208771302\Src\AlternativeDLCIntegration\Classes\X2DownloadableContentInfo_AlternativeDLCIntegration.uc:34-132`. High confidence (source read).
- The same mod re-adds the Hunter Weapons POI spawn in `OnPreMission`. Conditions: `RulerMgr.bContentActivated`, the mission already carries a POI (`POIToSpawn != 0`), **and** objectives `T0_M10_IntroToBlacksite` **and** `T2_M1_L0_LookAtBlacksite` are complete. It then swaps that mission's POI for `POI_HunterWeapons` if that POI has never spawned (`NumSpawns < 1`). Same file:209-233. POI name: `...\XComGame\DLC\DLC_2\Config\XComGame.ini:54`. High confidence.
- Covert Infiltration (2567230730) gives a mission a POI only for Intelligence, Datatap and Informant activities (`bNeedsPOI = true`, `WS\2567230730\Src\CovertInfiltration\Classes\X2StrategyElement_DefaultActivities.uc:79,101,120,145,441`). The POI spawns only if that mission **succeeds**; on failure it is deactivated (`X2Helper_Infiltration.uc:1277-1305`). So the swap needs a successful Intelligence/Datatap/Informant mission after the Blacksite has been looked at. High confidence on the code; the frequency in a real campaign is my inference.
- Proving Ground route: `ExperimentalWeapons` (Lab, needs `T0_M1_WelcomeToLabs` plus Integrated DLC) unlocks PG projects `BoltCaster`, `HuntersAxe`, `Shadowkeeper`, `Frostbomb`. They grant the CV schematic through `GiveItems`, which bypasses the schematic's AlwaysFalse. `SDK\DLC_2\Classes\X2StrategyElement_DLC_Day60Techs.uc:243-363`, gate `X2Helpers_DLC_Day60.uc:807-813`. No active mod disables these techs (grep over all active mods: only LAByrinth UI tag, Cosmo Dragoon check, Zelfana tech colours). High confidence.
- Why the Ionic Axe is buildable: vanilla `HunterAxe_MG_Schematic` needs `RequiredEquipment AlienHunterAxe_CV` plus the narrative-complete check, or alternatively `HunterAxe_CV_Schematic` plus the CV axe (`SDK\DLC_2\Classes\X2Item_DLC_Day60Schematics.uc:320-356`). No Missable (3326247546) removes `AlienHunterAxe_CV` from the main requirement (`WS\3326247546\Src\...\X2DownloadableContentInfo_NoMissableDLCWeaponsAndArmor.uc:90-115`). ADI turns the narrative check into AlwaysTrue. What remains is `AutopsyAdventStunLancer` + engineering 10, the "tier 2 melee research" the player did. Same logic for Bolt Caster MG (`MagnetizedWeapons`) and Shadowkeeper MG (`MagnetizedWeapons`). High confidence.
- SO Bridge: Alien Hunters (3328607898) only re-prices the schematics (`Config\XComStrategyTuning.ini`), so no access change. Crossbow boltcaster mod 1711144528 adds its own crossbows, unrelated. Dark Event Manager: no hunter-weapon references. Five Tier Weapon Overhaul: no hunter-axe references (grep).

### Log (LOG)
- ADI listeners registered: lines 5716-5720 ("Created Locator Beacon Detected Template", "Hunter Weapons Retrieved/UI Popup/Viewed").
- No "Created Hunter Weapons Tracker !" line (ADI logs it on retrieval) and no `POI_HunterWeapons` string. This log is one session, so this is only weak evidence that the POI has not been completed. It cannot show whether the POI already spawned and expired.
- Lines 277755/280566 `DLC2_S_King_Lives_Escapees_Remain` are tactical-start preloads next to `DLC3_S_Julian_Lives`. Noise; they say nothing about the Nest.

### What the player does now
1. Check the Research list for **Experimental Weapons**. If it is there: research it, then run PG projects Bolt Caster / Hunter's Axe / Shadowkeeper / Frost Bomb. That covers all four.
2. If it is absent (non-integrated campaign): have the Blacksite revealed and viewed, then succeed at a CI Intelligence, Datatap or Informant mission. The Hunter Weapons scan site should replace that mission's POI. Scan it. Hangar or Squad Select shows the weapons.
3. Risk: if `POI_HunterWeapons` already spawned once and expired, `NumSpawns >= 1` means it never returns (ADI and the DLC2 Highlander both skip it). There is no config lever for that case.

### Config lever
**None in ini.** Both blocks are code delegates set in OnPostTemplatesCreated; jepFixes cannot reach them. Fallback: the console (needs `-allowconsole`), `GiveItem AlienHunterAxe_CV`, `GiveItem AlienHunterRifle_CV`, `GiveItem AlienHunterPistol_CV`, `GiveItem Frostbomb`. Medium confidence that these give usable infinite items. The Hunter's Lodge trophy and upgrade checks look for the schematics (`HasItemByName('HunterAxe_CV_Schematic')`, `SDK\DLC_2\Classes\XComGameState_HuntersLodgeManager.uc:154`), so `GiveItem HunterAxe_CV_Schematic` etc. may also be needed for the Lodge display. Low-medium confidence, untested.

---

## ITEM 2: Shield Attachments (2197927839)

### Verdict
Shield Attachments adds **no upgrade slots of its own**. It creates 18 upgrades (`DraktenAlloy/Bullseye/Bigboom/Fold/Knock/Siphon` x `_Bsc/_Adv/_Sup`) that fit any weapon whose WeaponCat is in `AllowedTypes`. Slots come from the shield mod itself. Ballistic Shields Redux already gives slots: CV 1, MG 2, BM 2, SPARK the same (`WS\3750594110\Config\XComShields.ini`, keys `SHIELD_*_NUM_UPGRADE_SLOTS`). No active mod or jepFixes overrides those keys (grep over all workshop inis + JF). The most likely reason the player "sees no slot" is the UI: the Armory **Weapon Upgrade** button only ever opens the **primary** weapon. Secondary weapons such as shields are upgraded only by clicking the empty upgrade icons under the shield on **robojumper's Squad Select** screen. Medium-high confidence.

### Receipts
- Attachment gate: `CanApplyToShield` requires `WeaponCat` in `AllowedTypes` (`WS\2197927839\Src\ShieldUpgrades\Classes\X2Item_ShieldUpgrades.uc:251-259`). `AllowedTypes = shield` (`Config\XComShieldAttachmentsSetup.ini`). BSR adds `spark_shield` (`WS\3750594110\Config\XComShieldAttachmentsSetup.ini`).
- `NewAttachmentsSetups ... MatchWeaponTemplate = BallisticShield_CV/MG/BM, SparkBallisticShield_CV/MG/BM` (`WS\2197927839\Config\XComGame.ini`) sets icons and visuals only (`X2DownloadableContentInfo_ShieldUpgrades.uc:82-106`). Applicability does not depend on it, so the MGSV riot shields (`MD_WOTC_MGSV_MEL_*SHIELD*_T1-3`, cat `shield`, 1/2/2 slots in their own ini) and the MW4 riot shield are covered too.
- BSR templates: `BallisticShield_CV` (StartingItem, infinite, `NumUpgradeSlots = SHIELD_CV_NUM_UPGRADE_SLOTS`), `BallisticShield_MG/BM` built in Engineering (`WS\3750594110\Src\WotCBallisticShields\Classes\X2Item_Shield.uc:80-179`). Shield Rework (2310533632) changes armor/dodge/shield points only and has no slot keys. Nero's Custodian tower shields fail to create (`LOG:4673-4674` RDLC import failure), so they are not a factor.
- Armory button is primary-only: `WS\1796402257\Src\XComGame\Classes\UIArmory_WeaponUpgrade.uc:130,189` (`eInvSlot_PrimaryWeapon`). Squad Select icon path: `WS\1122974240\Src\robojumperSquadSelect\Classes\robojumper_UISquadSelect_EquipItem.uc:233-255,357-372` (needs `XComHQ.bModularWeapons`). The player's saved setting shows secondary icons: `C:\Users\Idi\Documents\My Games\XCOM2 War of the Chosen\XComGame\Config\XComrobojumperSquadSelect_NullConfig.ini`: `bShowWeaponUpgradeIcons=True`, `bSkipSecondaryUpgradeIconsAvailable=False`.
- Loaded: `LOG:227665` X2Item_ShieldUpgrades, `228130` X2Item_Shield.

### Loot and buying
- No schematics, `CanBeBuilt = false`, sell values 10/20/30 (black market **sell** only, no buy path). `X2Item_ShieldUpgrades.uc:49-76`.
- Loot is added in OnPostTemplatesCreated via `LootEntry` (`X2DownloadableContentInfo_ShieldUpgrades.uc:109-127`) into existing tables. Shipped odds (`WS\2197927839\Config\XComGame.ini:19-34`):
  - Early and Mid ADVENT weapon-upgrade tables: **1% + 1% (+1%)**, near zero. These tables are the ones rolled by early timed loot and vultures (vanilla `DefaultGameCore.ini:393,432,456`).
  - Late ADVENT 20/5, Early/Mid Alien 20-25, Late Alien 25.
  - Corpse base loot 50%: Priests M1-3, Shieldbearer M2/M3, Destroyer (not vanilla), Muton Elite / Centurion Elite, Bio Assault Trooper M2/M3; Biotic 30/15.
  - Early campaign drops are therefore very rare unless Priests or Shieldbearers are killed. Medium-high confidence.

### Drafted levers (for jepFixes; NOT written)
A. Slots. Only needed if a live check shows 0 slots on Squad Select. Plain keys, jepFixes loads last. File `JF\XComShields.ini`:
```
[WotCBallisticShields.X2Item_Shield]
SHIELD_CV_NUM_UPGRADE_SLOTS=2
SHIELD_MG_NUM_UPGRADE_SLOTS=2
SHIELD_BM_NUM_UPGRADE_SLOTS=3
```
Or through Configure Upgrade Slots (1171964288, active; absolute set in OPTC, `X2DownloadableContentInfo_ConfigureUpgradeSlots.uc:36-47`). This also covers the riot shields. File `JF\XComUpgradeSlots.ini`:
```
[ConfigureUpgradeSlots.X2DownloadableContentInfo_ConfigureUpgradeSlots]
+SlotConfig = (TemplateName=BallisticShield_CV, NumUpgradeSlots=1)
+SlotConfig = (TemplateName=BallisticShield_MG, NumUpgradeSlots=2)
+SlotConfig = (TemplateName=BallisticShield_BM, NumUpgradeSlots=2)
+SlotConfig = (TemplateName=SparkBallisticShield_CV, NumUpgradeSlots=1)
+SlotConfig = (TemplateName=SparkBallisticShield_MG, NumUpgradeSlots=2)
+SlotConfig = (TemplateName=SparkBallisticShield_BM, NumUpgradeSlots=2)
```
B. Loot. Raise early drops with `-` byte-exact removal plus new `+` lines. The originals are LF, no trailing spaces. File `JF\XComGame.ini`:
```
[ShieldUpgrades.X2DownloadableContentInfo_ShieldUpgrades]
-LootEntry = ( TableName = "EarlyADVENTWeaponUpgrades",Loots[0]=(Chance=1,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropBsc",RollGroup=2),Loots[1]=(Chance=1,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropAdv",RollGroup=2) )
-LootEntry = ( TableName = "MidADVENTWeaponUpgrades",Loots[0]=(Chance=1,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropBsc",RollGroup=2),Loots[1]=(Chance=1,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropAdv",RollGroup=2), Loots[2]=(Chance=1,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropSup",RollGroup=2) )
+LootEntry = ( TableName = "EarlyADVENTWeaponUpgrades",Loots[0]=(Chance=20,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropBsc",RollGroup=2),Loots[1]=(Chance=5,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropAdv",RollGroup=2) )
+LootEntry = ( TableName = "MidADVENTWeaponUpgrades",Loots[0]=(Chance=15,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropBsc",RollGroup=2),Loots[1]=(Chance=10,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropAdv",RollGroup=2),Loots[2]=(Chance=5,MinCount=1,MaxCount=1,TableRef="ShieldUpgradeDropSup",RollGroup=2) )
```
(The 20/5 and 15/10/5 values are the author's own commented-out defaults in the same file, lines 17-18.) Takes effect at next launch, including in the current campaign (tables rebuild each launch). High confidence on the mechanism, medium on the exact in-game rate.

---

## ITEMS 8 and 9: Total Advent Weaponry (1136349656) and Avengers Endgame Weapon Pack (1838499827)

### (a) What each adds and how it is obtained
**Total Advent Weaponry (TAW)**
- 26 weapons: `{AssaultRifle, Pistol, SniperRifle, Shotgun, Cannon, Sword, PsiAmp, SMG}_Advent_{CV,MG,BM}`, `GrenadeLauncher_Advent_{CV,MG}` (no BM). Also 3 gremlins `Gremlin_Advent_{CV,MG,BM}`, with cosmetic character templates `GremlinMk1/2/3Advent`, plus a schematic for each (`..._Schematic`). `WS\1136349656\Src\TotalAdventWeaponryWotC\Classes\X2Item_AdventWeaponry.uc`, `X2Item_Schematics.uc`, `X2Character_AdventGremlins.uc:18,80,142`.
- The player's MCM file (`C:\Users\Idi\Documents\My Games\...\Config\XComTotalAdventWeaponryWotC.ini`) has all tiers on, schematics on, `START_WITH_CONVENTIONAL_WEAPONS=True`. Because schematics are on, the CV items are **not** starting items (`X2Item_AdventWeaponry.uc:153-168`). The paths are:
  - CV: Engineering schematic, 5 supplies, requires the matching vanilla CV weapon owned (`X2Item_Schematics.uc:89-106`).
  - MG: schematic, `MagnetizedWeapons` + owning the vanilla MG.
  - BM: the plasma-tier equivalent.
- The existing-save insert (`X2DownloadableContentInfo_TotalAdventWeaponry.uc:19-28`) only runs when schematics are off.
- No loot, black market or reward path. The Grimy Loot config inside TAW is inert (Grimy not active). High confidence.
- **jepFixes already hides 18 TAW templates** (`JF\XComWeaponSkinReplacer.ini:132-150`: AR, Cannon, Pistol, Shotgun, Sniper, Sword, all tiers). Still live: `SMG_Advent_*` (3), `PsiAmp_Advent_*` (3), `GrenadeLauncher_Advent_CV/MG` (2), `Gremlin_Advent_*` (3). That is 11.

**Avengers Endgame (Endgame)**
- 15 melee secondaries, cat `sword`: `{Mjolnir, Stormbreaker, ThanosBlade, WidowBaton, RoninBlade}_{CV,MG,BM}`, plus a schematic for each. `WS\1838499827\Src\EndgameWeapons\Classes\X2Item_EndgameWeapons.uc`.
- CV: **StartingItem + infinite** (e.g. :246-248). The player owns all five CV now; they were also inserted on first load of an older save (`X2DownloadableContentInfo_EndgameWeapons.uc:24-89`).
- MG/BM: Engineering upgrade schematics gated on `AutopsyAdventStunLancer` / `AutopsyArchon` (`X2Item_EndgameWeapons_Schematics.uc:139-198`).
- No loot or black market.
- Stats are well above vanilla. Mjolnir CV: 5 dmg / +25 aim / stun + disorient / +mobility, against vanilla sword CV 4 dmg / +20 aim (`Config\XComEndgameWeapons.ini`, vanilla `DefaultGameData_WeaponData.ini:493,751`).
- None hidden in jepFixes today. The 09-15 audit counted 15 items / 0 skins (`vault\projects\XCOM\weapon-skin-audit.md:35`).

### (b) Dependencies
- AML `settings.json`: **no mod lists either as a dependency**. Both have `Dependencies: []` (python read of all 1120 entries). High confidence.
- Template-name grep over all active mods:
  - XSkin 2337161588 excludes TAW MG/BM and gremlins as skins (`Config\XComExcludedSkins.ini:482-498,591-593`).
  - Appearance Manager 2664422411 excludes them from pool loadouts.
  - Advent Purge Unit 2824985371 name-compares `Gremlin_Advent_*` in a `case` statement.
  - WSR Shotgun Animation Addon 2895282660 animsets `Shotgun_Advent_*`.
  - jepFixes WSR list.
  - All of these are name lists; a missing template only produces a skipped entry or log line. Endgame: referenced by nothing else. High confidence.

### (c) Removal mid-campaign
- Items in HQ storage or equipped become item states with no template. The Highlander (and vanilla) treats them as "bad items due to outdated saves": `CanRemoveItemFromInventory` returns true for a none template (`WS\1796402257\Src\XComGame\Classes\XComGameState_Unit.uc:8683`). Loadout validation then strips them and refills the slot with a default. That is survivable in most reports, but it is the classic source of red screens, empty-slot soldiers and squad-select crashes. The riskiest case is an **equipped TAW gremlin**: its cosmetic unit `GremlinMk*Advent` spawns at tactical start and its character template would be gone. Medium confidence (community pattern plus code, not tested here).
- Safe removal order, if chosen: unequip every TAW item (especially Advent gremlins) and sell or leave nothing equipped, save in the Avenger, disable in AML, load, go to the Armory once, save. The jepFixes hide lines for TAW then log "could not find" and are otherwise harmless (`WS\1517938486\Src\zzzWeaponSkinReplacer\Classes\X2DownloadableContentInfo_WeaponSkinReplacer.uc:690-694`).
- Removing TAW also deletes its CV skins from XSkin (MG/BM and gremlins are already excluded there).

### (d) Levers compared
- **WSR `WEAPONS_TO_HIDE`** (WSR Core 1517938486 + Config 1709345052, both active): per template it sets `StartingItem=false`, `CanBeBuilt=false`, `HideInInventory`, `HideInLootRecovered`, clears `BaseItem`, and sets the schematic `CanBeBuilt=false` (`X2DownloadableContentInfo_WeaponSkinReplacer.uc:679-718`). XSkin then offers the template as a skin. This is exactly the player's standing standard (`JF\XComWeaponSkinReplacer.ini:1-3`).
- Limitation: copies **already owned** stay in HQ storage and remain equippable. `HideInInventory` is honoured only in `XComGameState_HeadquartersXCom.uc:4268` (acquire popups), and the loadout locker does not check it. That matters for Endgame, whose five CV weapons the player owns. Medium-high confidence.
- The config route (bCanBeBuilt / StartingItem via Template Master, `-` lines) gives nothing extra over WSR here. Neither mod has loot, black market or `+` ini lines to remove; everything is set in code.

### Recommendation
- **TAW: hide the remaining 11, do not remove.** This gives the same result as removal with zero save risk, and the CV looks stay in XSkin. Removal only after the unequip procedure above, and there is no gain. Append to `JF\XComWeaponSkinReplacer.ini` under the existing TAW comment (line 132):
```
+WEAPONS_TO_HIDE=SMG_Advent_CV
+WEAPONS_TO_HIDE=SMG_Advent_MG
+WEAPONS_TO_HIDE=SMG_Advent_BM
+WEAPONS_TO_HIDE=PsiAmp_Advent_CV
+WEAPONS_TO_HIDE=PsiAmp_Advent_MG
+WEAPONS_TO_HIDE=PsiAmp_Advent_BM
+WEAPONS_TO_HIDE=GrenadeLauncher_Advent_CV
+WEAPONS_TO_HIDE=GrenadeLauncher_Advent_MG
+WEAPONS_TO_HIDE=Gremlin_Advent_CV
+WEAPONS_TO_HIDE=Gremlin_Advent_MG
+WEAPONS_TO_HIDE=Gremlin_Advent_BM
```
  Caveat: the 09-15 audit kept 6 TAW templates as "items" (distinct stats: SMG and others). Hiding them overrides that audit on the player's new word, which is his call.
- **Endgame: WSR hide all 15** (new block in the same file). This stops start, build and upgrade in new and current campaigns. The five owned CV copies stay equippable. To make them cosmetic in effect too, optionally flatten their stats to vanilla sword values in `JF\XComEndgameWeapons.ini`. These are plain keys (last loaded wins). Medium confidence that the plain-key override applies; verify in the Armory.
```
; ---- WSR block (JF\XComWeaponSkinReplacer.ini)
+WEAPONS_TO_HIDE=Mjolnir_CV
+WEAPONS_TO_HIDE=Mjolnir_MG
+WEAPONS_TO_HIDE=Mjolnir_BM
+WEAPONS_TO_HIDE=Stormbreaker_CV
+WEAPONS_TO_HIDE=Stormbreaker_MG
+WEAPONS_TO_HIDE=Stormbreaker_BM
+WEAPONS_TO_HIDE=ThanosBlade_CV
+WEAPONS_TO_HIDE=ThanosBlade_MG
+WEAPONS_TO_HIDE=ThanosBlade_BM
+WEAPONS_TO_HIDE=WidowBaton_CV
+WEAPONS_TO_HIDE=WidowBaton_MG
+WEAPONS_TO_HIDE=WidowBaton_BM
+WEAPONS_TO_HIDE=RoninBlade_CV
+WEAPONS_TO_HIDE=RoninBlade_MG
+WEAPONS_TO_HIDE=RoninBlade_BM

; ---- optional stat flatten, CV only (owned copies), pattern repeats for Stormbreaker/ThanosBlade/WidowBaton/RoninBlade
[EndgameWeapons.X2Item_EndgameWeapons]
Mjolnir_CONVENTIONAL_BASEDAMAGE=(Damage=4, Spread=1, PlusOne=0, Crit=2, Pierce=0, Shred=0, Tag="", DamageType="Melee")
Mjolnir_CONVENTIONAL_AIM = 20
Mjolnir_CONVENTIONAL_CRITCHANCE = 10
Mjolnir_CONVENTIONAL_DISORIENT = false
Mjolnir_CONVENTIONAL_PANICCHANCE = 0
Mjolnir_STUN = false
[EndgameWeapons.X2Ability_AveWeapons]
MJOLNIR_CV_MOBILITY_BONUS = 0
```
  Note: ThanosBlade CV also has Pierce 1 / Shred 1 in its BASEDAMAGE; set both to 0. Check `Config\XComEndgameWeapons.ini:1-197` for each weapon's own keys (one typo in the mod: `Stormbreaker_MAGNETIC_ISOUNDRAGNE`).
- Simpler alternative for the owned copies: the player unequips them and leaves them in storage. With the hide list in place there is no other way to get them.

### Side note
TAW ships its own `ModConfigMenuAPI.u` (42,488 bytes). That is the most common size, 15 copies across the workshop, so it adds nothing to the crash "mixed package sizes" suspicion. Low relevance.
