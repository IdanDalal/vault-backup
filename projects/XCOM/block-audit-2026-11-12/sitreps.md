---
type: report
created: 2026-11-12
author: Agent audit-sitreps
---
# Sitrep block audit (jepFixes), 2026-11-12

Scope: the 52-name sitrep block list and the per-mission count limit. Read-only. Scratch scripts sit beside this file (`sr_*.py`).

Short paths used below:
- `JEP` = `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\jepFixes\Config`
- `WS` = `C:\Program Files (x86)\Steam\steamapps\workshop\content\268500`
- `MSR` = Multiple Sitreps REDUX, `WS\3739636065` (active)
- `CI` = Covert Infiltration, `WS\2567230730` (active)
- `ARFM` = A Requiem For Man: Gameplay Mutators, `WS\2795578857` (active)
- `CHL` = Community Highlander, `WS\1796402257\Src\XComGame\Classes`
- `LOGS` = `C:\Users\Idi\Documents\My Games\XCOM2 War of the Chosen\XComGame\Logs`

## Bottom line

1. No blocked sitrep ran on any of the 9 tactical missions in the logs. 37 of the 38 blocked names that still exist as templates carry a tactical tag that the logs print at launch, and none of the 37 appears.
2. The count limit was never visibly exceeded: largest tagged count on one mission is 2 (limit 1 + 1 at 50% = 2). This is a lower bound, because sitreps without a tag are invisible in the logs.
3. Nothing is FAILING on the evidence. Most levers stay UNPROVEN, because 9 missions drawing from a pool of a few hundred sitreps cannot prove a filter. Two things are proven by source to be outside every block list: ARFM dark events (5 blocked names) and the count on Covert Infiltration missions.
4. The logs do not record a mission's sitrep list directly. The only per-mission record is the tag dump from the mod Mission Beneath Suspicion (`WS\3000011407\Src\MissionBeneathSuspicion\Classes\X2DownloadableContentInfo_MissionBeneathSuspicion.uc:140-143`), which prints `MissionState.TacticalGameplayTags` at launch.

## Step 1: what jepFixes intends

- Block list: 52 names, `JEP\XCom_Sitrep_Categories_REDUX.ini:11-62`. Mirrored 52 of 52 in `JEP\XComGameData.ini:83-134` (script check: sets equal).
- Count: 1 guaranteed + 1 extra at 50%, `JEP\XCom_Sitrep_Categories_REDUX.ini:5-8` and `JEP\XComMultipleSitreps_REDUX_MCM_Defaults.ini:4-6`.
- CI channels: 15 risk removals + 10 bonus removals, `JEP\XComInfiltration.ini:7-33`.
- Of the 52 names, 14 have no live template, so they cannot spawn whatever the levers do:
  - never declared by any active mod: AdventPatrols, Juggernaut, ARFMDESitrep_MutonGrenades, AbiziOTS_Leadership0-3 (7)
  - removed by another active mod's `-SitReps=`: Surgical, LowProfile (CI), Fireteam, Phalanx (bridge 2608952868), StealthInsertion (`WS\3318172774\Config\XComGameData.ini:5`), ARFMDESitrep_AdvancedEnemies, ARFMDESitrep_RapidReconcealment (Odd S9 Tweaks 3314720537) (7)
- OpportuneMoment1 and OpportuneMoment2 are in both block lists, yet `JEP\XComInfiltration.ini:4` keeps them wired on purpose as CI over-infiltration bonuses (`CI\Config\XComInfiltration.ini:354-355`). The two files contradict each other; the CI wiring wins (step 3, path C). Decide which is intended.

## Step 4: sitreps on every tactical mission in the logs

Method: every `Mission type is X. Tactical tags are:` block (`sr_missions.py tac`), tags mapped back to sitrep templates through each mod's `[Name X2SitRepTemplate]` section (`sr_tagmap.py`). Blocked names and their tags are in the table at the end.

| # | Date | Mission | Log:line | Sitrep tags printed | Sitreps | Blocked? |
|---|---|---|---|---|---|---|
| 1 | 11-09 | GatecrasherCI | `Launch-backup-2026.11.09-12.23.56.log:55506` (rotated out of the folder during this audit; read before it went) | none | 0 | no |
| 2 | 11-09 | RescueVIP | `Launch-backup-2026.11.09-19.25.31.log:72474` | SITREP_TheLost | TheLost | no |
| 3 | 11-10 | ChosenRetaliation | `Launch-backup-2026.11.10-10.53.43.log:84722` | SITREP_ARFMExtraAction | ARFMDESitrep_ExtraAction | no |
| 4 | 11-10 | ChosenRetaliation | `Launch-backup-2026.11.10-13.28.40.log:80216` | SITREP_ARFMExtraAction, SITREP_RRHIncursion | ARFMDESitrep_ExtraAction, RRHIncursion | no |
| 5 | 11-10 | HIVECovertEscape | `Launch-backup-2026.11.10-13.28.40.log:98047` | none | 0 | no |
| 6 | 11-10 | SupplyExtraction | `Launch-backup-2026.11.10-13.28.40.log:113067` | SITREP_ARFMHazmatLoots, SITREP_TheLost | ARFMDESitrep_HazmatLoots, TheLost | no |
| 7 | 11-11 | MRRescueAdventCell | `Launch-backup-2026.11.11-16.56.21.log:134414` | none | 0 | no |
| 8 | 11-11 | RecoverExpedition | `Launch-backup-2026.11.12-12.07.47.log:110237` | SITREP_TheHorde | TheHorde, plus AbiziBanRuler forced by Beneath Suspicion (no tag; `Launch.log:19319, 19550`) | no |
| 9 | 11-11 | SabotageTransmitter | `Launch-backup-2026.11.12-12.07.47.log:133699` | SITREP_ARFMExtraAction, SITREP_PathfinderSearchTeams | ARFMDESitrep_ExtraAction, a Pathfinders sitrep | no |
| - | 11-12 | (no new launch) | `Launch.log:56427` loads a tactical save, mission 9 continues (`:96540` Obj_DestroyTransmitter) | - | - | - |

Extra evidence from the same logs:
- Strategy-side tag dumps (missions generated on the map, launched or not, `sr_missions.py strat`): 26 dumps in the 8 files on disk, zero blocked tags. The complete set of sitrep tags printed anywhere in those files is 7: ARFMExtraAction, ARFMHazmatLoots, ARFMXCOMGrenades, PathfinderSearchTeams, RRHIncursion, TheHorde, TheLost. Newest: `Launch.log:106964`, RM_Sabotage_Neutralize with SITREP_ARFMXCOMGrenades (not blocked).
- Diverse Aliens By Force Level prints the sitrep modifiers per enemy pod. All 49 pod lines read `UnitCap: 99 ... UnitCountOffset: 0`, so Fireteam (cap 2), Surgical (cap 3), Advanced (cap 2) and LowProfile (count -1) were on none of those missions.
- `HazmatLoots` on mission 6 is `ARFMDESitrep_HazmatLoots` (`ARFM\Config\XComGameData.ini:281-282`), a different template from the blocked `ARFMDESitrep_HazmatCleanup` (`:100-101`).
- Redscreens `Unable to find a template with DataName: StealthInsertion` (`Launch.log:106957`) and `AHWSitrep_OrbitalDrop` (`:107251`): a mission definition and a risk row point at templates that no longer exist. Harmless.

Limits of this evidence:
- Largest count seen = 2 (missions 4, 6, 8, 9). Lower bound only.
- Invisible in the logs: `ARFMDESitrep_ForceElevation` (no tag) and anything ARFM dark events push in after launch (step 3, path E).
- Missions 3 and 4 look like the same retaliation launched twice (confidence medium). Its sitrep count went from 1 to 2 between sessions, which matches MSR re-rolling the extra slot on every save load (`MSR\Src\MultipleSitreps_REDUX\Classes\X2DownloadableContentInfo_MultipleSitreps_REDUX.uc:46-49, 229-230`; `bRepairAvailableMissionsOnLoad = true`, `MSR\Config\XCom_Sitrep_Categories_REDUX.ini:29`). The limit of 2 still holds, but the count is not stable across loads.

## Step 2: lever check

L1. `JEP\XCom_Sitrep_Categories_REDUX.ini`, `+BlockedSitReps` and counts
- Class: `X2DownloadableContentInfo_MultipleSitreps_REDUX ... config(_Sitrep_Categories_REDUX)` (`...MultipleSitreps_REDUX.uc:5`), array at `:33`. File name, section `[MultipleSitreps_REDUX.X2DownloadableContentInfo_MultipleSitreps_REDUX]`, key and name syntax all match.
- Consulted at `:440` (roller filter), `:196` and `:501` (repair), `:648` (the test).
- Reach: only the mission sources switched On in `MSR\Config\XCom_Sitrep_Categories_REDUX.ini:44-50` (GuerillaOp, SupplyRaid, Council, ResistanceOp, LandedUFO, Retaliation, AlienNetwork). CI missions use source `MissionSource_ActivityCI`, which `IsMissionSourceEnabled` (`:382-399`) rejects.
- Hijack risk: `XComGameState_MultipleSitreps_REDUX_Settings.uc:365-366` calls `StaticSaveConfig()` on two classes of this same config name (the Seal feature). If Idi ever seals a sitrep in game, the engine writes `XCom_Sitrep_Categories_REDUX.ini` into Documents. No such file exists there today (listing checked), so no hijack yet.
- The counts in this file (`SitrepAmount` etc.) are overwritten at startup by the MCM values (`UIScreenListener_MultipleSitreps_REDUX_MCM.uc:156-160`). They do nothing on their own.

L2. `JEP\XComMultipleSitreps_REDUX_MCM_Defaults.ini`
- The engine does read this name: `class MultipleSitreps_REDUX_MCM_Defaults ... config(MultipleSitreps_REDUX_MCM_Defaults)` (`MultipleSitreps_REDUX_MCM_Defaults.uc:1`), section matches.
- It is not what the game uses. `MCM_CH_GetValue` returns the default only when the saved version is lower than the default version (`MSR\Src\ModConfigMenuAPI\MCM_API_CfgHelpers.uci:3-7, 23-24`). Saved `CONFIG_VERSION=3`, default `VERSION=3` (`MSR\Config\XComMultipleSitreps_REDUX_MCM_Defaults.ini:13`), so the saved file wins.
- Saved file: `C:\Users\Idi\Documents\My Games\XCOM2 War of the Chosen\XComGame\Config\XComMultipleSitreps_REDUX_MCM.ini` (written 09-15) = 1 / 1 / 50, change cost 10, remove 0, seal 0. Identical to what jepFixes intends.
- jepFixes has no file named `XComMultipleSitreps_REDUX_MCM.ini`, so it cannot hijack that save.

L3. `JEP\XComInfiltration.ini`, 25 `-` lines
- Class `X2Helper_Infiltration ... config(Infiltration)` (`CI\...\X2Helper_Infiltration.uc:8`), `FlatRiskSitReps` at `:49`; `SitRepBonuses` section `[CovertInfiltration.X2StrategyElement_DefaultOverInfiltrationBonuses]`.
- Byte check (`sr_tagmap.py`): 25 of 25 `-` lines have a byte-identical `+` line in an active mod (CI `XComInfiltration.ini:50-54, 57, 358, 360, 365, 369, 371`; bridge 2608952868 `:4, 5, 7, 10`; bridge 2608960168 `:5`; ARFM `:3-5, 7-9, 15, 18, 19`).
- Still wired on purpose or by omission (none is a blocked name except the two OpportuneMoments): Congregation, MessyInsertion, ExperimentalRollout, ARFMDESitrep_AlienShields, AHWSitrep_OrbitalDrop (risks); CommsJamming, Foxholes, VolunteerArmy, EquipmentCache, ShadowSquad, ResistanceCell, six ARFM bonuses, four Faction Hero incursions (bonuses).

L4. `JEP\XComGameData.ini`, `+ENVIROMENTAL_SITREPS_EXCLUDE` (52 lines)
- `var config(GameData) array<name> ENVIROMENTAL_SITREPS_EXCLUDE` (`X2Helper_Infiltration.uc:55`), so `XComGameData.ini` is the right file; section `[CovertInfiltration.X2Helper_Infiltration]` matches; CI's own line uses the same bare-name syntax (`CI\Config\XComGameData.ini:181`).
- Consulted at `:856-858`, feeding the environmental pick at `:919-949`.
- On paper this lever has the same shape as the `CovertActionsPreventRandomSpawn` lever that is failing, so paper is worth nothing here.

L5. `JEP\XComMissionDefs.ini` (sitrep-relevant part only)
- Removes the only mission definition in any mod that forces a blocked sitrep: `EmergencyDefense_Skirmishers` with `ForcedSitreps[0] = "ShowOfForce"` (`WS\1133287457\Config\XComMissionDefs.ini:142`).
- Its own probe passes: `Launch.log` holds 0 lines `Current mission sType is  EmergencyDefense`.

## Step 3: every path that puts a sitrep on a mission, and which list it consults

The mission site's list `GeneratedMission.SitReps` is the truth. Tactical copies it at map build: `BattleData.ActiveSitReps = MissionSiteState.GeneratedMission.SitReps` (`CHL\XComTacticalMissionManager.uc:449`, called from `XComParcelManager.uc:1847`).

| Path | Where | Block list consulted |
|---|---|---|
| A. Vanilla mission creation: forced by mission def, source roller, forced by plot type, then every mod's `PostSitRepCreation` | `CHL\XComGameState_MissionSite.uc:480, 498-504, 528-533, 539-542` | MSR list, only if the source is one of MSR's 7 |
| B. MSR roller and repair | `...MultipleSitreps_REDUX.uc:415, 173-201, 203-250` | MSR list; enforces the count |
| C. CI infiltration missions: forced + plot + 1 environmental at 50%, then risks that occurred, then over-infiltration bonuses | `CI\...\XComGameState_MissionSiteInfiltration.uc:68-75, 118-120, 216-232`; `X2StrategyElement_DefaultOverInfiltrationBonuses.uc:81-97` | L4 for the environmental pick; L3 removes the risk and bonus rows; MSR list never; no count limit |
| D. CI assault missions: 50% chance of 1 bonus (milestone SitRep1) + 1 risk, then 1 environmental at 50%, plot-forced, hooks | `X2Helper_Infiltration.uc:727-809`; `X2ActivityTemplate_Assault.uc:122-188`; chances `CI\Config\XComInfiltration.ini:44-48` | same as C |
| E. ARFM dark events add a sitrep straight into `BattleData.ActiveSitReps` inside tactical, after the copy at `:449` | `ARFM\...\ARFM_DE_DarkEvents.uc:1827` MedicalEmbargo, `:1993` HairTrigger, `:2044` ExtraAmmo, `:2234` Fortress, `:2348` ImmortalPursuit; called from `CHL\X2TacticalGameRuleset.uc:2932-2941` | none |
| F. ARFM second-wave option `ARFMPerilousYearning`: Ambush on Covert Escape missions, Fortress on Chosen Strongholds | `ARFM\...\X2DownloadableContentInfo_ARFMDarkEvents.uc:264-269, 158-166` | none (Fortress is added at launch, after every filter) |
| G. Other mods' hooks adding one fixed sitrep: MOCX `MOCX`, LEB `LEBLGSR`, Beneath Suspicion `AbiziBanChosen` / `AbiziBanRuler`, Alternative DLC Integration `RoboticUprising`, Capture Zone `TheLost` | `sr_bypass_hits.txt` lines 1-4, 34, 52-54, 56, 102 | none; none of these names is blocked; each can push a mission past the count |
| H. MSR's launch-time strip of `BattleData.ActiveSitReps` | `...MultipleSitreps_REDUX.uc:52-111` | MSR list, all sources, but the copy at `XComTacticalMissionManager.uc:449` overwrites it in tactical. It is not a safety net. |

Consequences:
- The count limit (1 + 1 at 50%) governs only MSR's 7 sources. In this campaign 6 of the 9 missions were CI activities (5 confirmed by `ALVarietyCI: Difficulty for Activity_*` or CI lines next to the launch; MRRescueAdventCell assumed), where the possible count is forced + plot + 1 environmental + risks + bonuses.
- Five blocked names can still arrive through path E whenever the matching dark event is active: `ARFMDE_MedicalEmbargo`, `ARFMDE_ExtraAmmoII` (HairTrigger), `ARFMDE_ExtraAmmoI` (ExtraAmmo), `ARFMDE_Fortress`, `ARFMDE_ImmortalPursuit` (`ARFM_DE_DarkEvents.uc:1751, 1953, 2004, 2171, 2281`). No jepFixes file removes these dark events. The sixth, WavesAssault, has a typo in the mod (`:2456`, trailing space in the name) and cannot attach.
- Path E leaves no line in any log: the tag dump runs before it.

## Step 5: verdicts

| Lever | Verdict | Reason | Probe if unproven |
|---|---|---|---|
| L1 `+BlockedSitReps` (MSR sources) | UNPROVEN | Wiring right; 0 blocked tags on the 2 retaliation launches and 26 map dumps; too few draws to prove the filter | Set `bVerboseLogging = true` in `JEP\XCom_Sitrep_Categories_REDUX.ini`, load the same geoscape save about 20 times (each load re-rolls), then compare every `[MultipleSitreps] Added sitrep:` line with the 52 names |
| L1/L2 count 1 + 1 at 50% (MSR sources) | HOLDING | Saved MCM file is the live source and reads 1 / 1 / 50; retaliation ran with 1 then 2 tagged sitreps | - |
| L2 `_MCM_Defaults.ini` itself | HOLDING but idle | Engine reads it; the saved file outranks it; values identical | - |
| Count on CI missions | NO LEVER | MSR never touches `MissionSource_ActivityCI`; max seen 2, lower bound | Mission brief screenshot of any CI mission showing 3 or more sitreps would show the gap in practice |
| L3 CI risk and bonus removals (25) | UNPROVEN | 25 of 25 byte-identical; no removed risk or bonus sitrep on 6 CI missions; no log line states the array's content | Game console (needs `-allowconsole`; command availability: medium confidence): `get X2Helper_Infiltration FlatRiskSitReps`. 9 rows left = held, 24 = failed. Or: no infiltration risk panel ever lists Shoddy Intel, Air Patrols, Intelligence Leak, Updated Firewalls, Phalanx, Restricted Airspace |
| L4 `ENVIROMENTAL_SITREPS_EXCLUDE` (52) | UNPROVEN | Wiring right; 0 blocked tags on 6 CI missions; at 50% per mission that is about 3 environmental draws | Console: `get X2Helper_Infiltration ENVIROMENTAL_SITREPS_EXCLUDE` shows 53 names (52 + TheHorde) = held, 1 = failed |
| L5 ShowOfForce via Emergency Defense | HOLDING | 0 `EmergencyDefense` mission-type lines in `Launch.log` | - |
| OpportuneMoment1/2 | CONTRADICTION | Blocked in L1 and L4, kept wired in L3 on purpose; CI will grant them at over-infiltration milestones | Ruling needed: keep or remove |
| ARFM dark-event sitreps (MedicalEmbargo, HairTrigger, ExtraAmmo, Fortress, ImmortalPursuit) | UNPROVEN, not blockable by these levers | Path E consults no list and leaves no log line | In a mission while one of those 5 dark events is active: MSR's tactical sitrep viewer (it reads `BattleData.ActiveSitReps`, `UIScreen_MultipleSitreps_REDUX_TacticalViewer.uc:192`) lists the sitrep or not |
| ARFMDESitrep_Ambush / Fortress via `ARFMPerilousYearning` | UNPROVEN | Applies only if that second-wave option is on in this campaign; not recorded in any ini I can read | Second Wave screen of the campaign: is "Perilous Yearning" ticked |
| `ARFMDESitrep_ForceElevation` | UNPROVEN | Only blocked name with a live template and no tag; `bExcludeFromStrategy`, so no roller can pick it | none needed unless it shows in a mission brief |

Whole-list probe that needs no file change: a screenshot of the mission brief (Enhanced Sitrep UI lists every sitrep) for each new mission. That closes the untagged-sitrep gap for both the block list and the count.

## Blocked names and their log tags (for future greps)

38 live templates. Tag = the string to grep in `LOGS\Launch*.log`.

LightningStrike SITREP_LightningStrike; LocationScout SITREP_LocationScout; ShowOfForce SITREP_ShowOfForce; Ambush SITREP_Ambush; LowVisibility SITREP_LowVisibility; BlackOps SITREP_BlackOps; Advanced SITREP_Advanced; Waves SITREP_Waves; Phalanx_CI SITREP_Phalanx_CI; ExperimentalStims SITREP_ExperimentalStims; UpdatedFirewalls SITREP_UpdatedFirewalls; MentalReadiness SITREP_PhysicalConditioning; ShoddyIntel SITREP_ShoddyIntel; WellRehearsed SITREP_WellRehearsed; IntelligenceLeak SITREP_IntelligenceLeak; TacticalAnalysis SITREP_TacticalAnalysis; AdventAirPatrols SITREP_AdventAirPatrols; OpportuneMoment1 SITREP_OpportuneMoment1; OpportuneMoment2 SITREP_OpportuneMoment2; RestrictedAirspace SITREP_RestrictedAirspace; ARFMDESitrep_Ambush SITREP_ARFMAmbush; _HighGround SITREP_ARFMHighground; _Brittleness SITREP_ARFMBrittleness; _OverwatchWeakness SITREP_ARFMOverwatchWeakness; _AlienArmor SITREP_ARFMAlienArmor; _XCOMDeepCover SITREP_ARFMXCOMDeepCover; _MedicalSurplus SITREP_ARFMMedicalSurplus; _MedicalEmbargo SITREP_ARFMMedicalEmbargo; _ExtraAmmoXCOM SITREP_ARFMFreeReloads; _ExtraAmmo SITREP_ARFMExtraAmmo; _HairTrigger SITREP_ARFMHairTrigger; _WavesAssault SITREP_ARFMWavesAssault; _HazmatCleanup SITREP_ARFMHazmatCleanup; _HighAlert SITREP_ARFMHighAlert; _GnawingDread SITREP_ARFMGnawingDread; _ImmortalPursuit SITREP_ARFMImmortalPursuit; _Fortress SITREP_ARFMDEFortress; _ForceElevation (no tag).

## Not done

- Save files were not parsed (they hold the exact sitrep list per mission; compressed, needs a decompressor).
- Whether the 5 ARFM dark events have been active in this campaign: not established.
- The log count is 8 Launch files on disk today, not 9: the 11-09 12:23 file rotated out mid-audit. Its one mission (Gatecrasher) is row 1.
