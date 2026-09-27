---
type: research
created: 2026-09-27
author: jep
---
# Research: bond cluster removal (item 5) + Templar Psi Blade colors (item 6)
Date 2026-09-27. Read-only. W = /c/Program Files (x86)/Steam/steamapps/workshop/content/268500

## ITEM 5: bond cluster

Verdict: all five can go. Remove them together at an Avenger (strategy) save. If removing only some, remove dependents before their parents (order below). No other active mod needs any of the five. Mid-campaign removal: harmless orphans only, no strategy object wired into XComHQ. Confidence ~85%.

### What each one does + declared deps (AML settings.json Dependencies; 1134256495 = WOTC DLC itself, ignored)
| id | mod | does | AML deps | other evidence |
|---|---|---|---|---|
| 3523258775 | Cohesion Matchmaker - Dynamic Relationships | tracks in-mission help/friendly fire, adjusts cohesion after mission, auto-forms romance/friend/rival pairs via Complex Bonds | 3428787645, 3499811007 | description "you need all 3"; code reads XComGameState_RelationshipManager (UISoldierBondAlert_SpecialBondExtension.uc:327-344, UISpecialBondConfirmScreen.uc:193-217) = HARD dep on Complex Bonds; zero code refs to Re-enabler (grep Reenabler/SoldierBondCohesionRestore in src+Config = 0) = SOFT/behavioral dep. MCO UISoldierBondAlert (Config/XComEngine.ini:5) |
| 3468585452 | Love, Kin, Friend or Foe Pack | relationship-driven life events (promotions, AP, gear, stats) for lovers/family/friends/rivals | 3428787645 | description "Complex Soldier Bonds Add-On is required", "base Soldier Life Events is not a requirement"; its XComEngine.ini lists +NonNativePackages=ComplexSoldierBondsAddOn + ModEditPackages (compile+load HARD dep); zero refs to base Life Events classes |
| 3428787645 | Complex Soldier Bonds Add-On | utility: stores romance/family/friend/rival pairs (XComGameState_RelationshipManager), Armory Soldier Bonds screen, console cmd AddRelationshipPair | none | MCO UISoldierBondListItem (XComEngine) |
| 3499811007 | Team Cohesion Re-enabler | UIScreenListener caches then restores a new bondmate pair's cohesion with the rest of the squad (SoldierBondCohesionRestoreListener.uc:14-60) | none | no state classes, no MCO |
| 3422452897 | Soldier Life Events | 40 random Avenger events, 3-choice responses, stat changes | none | standalone |

### Who depends on them (scan of all AML entries' Dependencies + Config/Src/XComMod of 1,113 other active mods)
- 3428787645 <- 3523258775, 3468585452 (only AML hits)
- 3499811007 <- 3523258775 (only AML hit)
- 3523258775, 3468585452, 3422452897 <- nobody
- Only textual hit outside the cluster: XpanD's Console Commands 3113132590, XCCConsoleCommandListData.uc:1611-1625, guarded by IsModActive('SoldierLifeEvents'/'ComplexSoldierBondsAddOn') = optional, harmless when absent.
- No other active mod MCOs UISoldierBondAlert or UISoldierBondListItem (grep of every other active XComEngine.ini = 0 hits), so removing frees those classes and breaks nothing.

### Other active bond mods: need any of the five? NO for all
| id | mod | AML deps | needs cluster |
|---|---|---|---|
| 1124175584 | Color Coded Bonds | none | no |
| 1167567103 | Bondmates With More Benefits | none | no |
| 1176368634 | Avenger Defense Bondmates Fix | none | no |
| 3512173534 | No Drop Down Lists: Bond Slot | 2098062078 No Drop Down Lists | no |
| 3731747818 | Bond To Header 2 | 667104300 Mod Config Menu | no |
| 2011007357 | Cooldown Teamwork | none | no |

### Safe removal order (one sitting is fine; order only matters if partial)
1. 3523258775 Matchmaker (depends on 2 and 3)
2. 3468585452 Love/Kin pack (depends on Complex Bonds; its XComEngine.ini force-loads ComplexSoldierBondsAddOn, so never keep it without Complex Bonds)
3. 3428787645 Complex Soldier Bonds Add-On
4. 3499811007 Team Cohesion Re-enabler
5. 3422452897 Soldier Life Events (independent; any position)

### Mid-campaign save safety
- Life Events: XComGameState_SoldierLifeEvent extends XComGameState_HeadquartersProject, BUT never added to XComHQ.Projects (UIScreenListener_SoldierLifeEvents.uc:230 is commented out). Standalone objects -> orphan "failed to load class" at worst. XComGameState_LastSoldierLifeEvent = BaseObject. Outcomes already applied are vanilla and stay: SetBaseMaxStat, RankUpSoldier, AbilityPoints, vanilla heal project with eStatus_Healing (X2StrategyElement_SoldierLifeEvents.uc:424-432). Confidence high.
- Love/Kin pack: same pattern (UIScreenListener_SoldierLifeEventsExpansion.uc:237 commented; heal project vanilla at X2StrategyElement_SoldierLifeEventsExpansion.uc:438). Confidence high.
- Complex Bonds: XComGameState_RelationshipManager = BaseObject singleton; orphaned; pair labels lost (flavor only). Confidence high.
- Matchmaker: XComGameState_BondInteractionStore, XComBondTrackerHelper, X2SpecialBondPopupHelper = BaseObject; orphaned. Relationship_* ability names appear only in the confirm-screen UI list (UISpecialBondConfirmScreen.uc:81-102), no grant path found. Only vanilla thing it writes: XComHQ.bHasSeenSoldierBondPopup + cohesion via vanilla ModifySoldierCohesion. Confidence medium-high (did not decompile .u, source only).
- Re-enabler: no state objects; cohesion values it restored are vanilla SoldierBond data and stay. Confidence high.
- None of the five calls RegisterForEvent (grep = 0) -> no persistent event listeners left dangling in the save.
- Mid-mission: avoid; Matchmaker's in-mission memory store would just vanish. Remove from a strategy save.
- Log receipt: Launch.log lines 226295, 226311, 226313, 226319 (DLCInfo found for LifeEvents, Expansion, CohesionReenabler, DynamicSpecialSoldierRelationships).

## ITEM 6: [WOTC] Templar Psi Blade & Ability Colors 3788619284

### (a) "Original" deep purple
- Value: W/3788619284/Config/XComTemplarPsiColorMod.ini:49 `OriginalTemplarFallbackColor=(X=0.20,Y=0.10,Z=1.00)` (vector = linear RGB, per ini comment lines 45-48 and :43 "Linear RGB"). Declared TPC_ParticleColorPatcher.uc:23 `var config vector`. Confidence high.
- Floats: R 0.20, G 0.10, B 1.00.
- 0-255 straight scale: (51, 25.5 -> 25/26, 255) = #3319FF / #331AFF.
- 0-255 as sRGB (linear->gamma converted, what a screen color picker would show): (124, 89, 255) = #7C59FF. Computed by me, standard sRGB curve.
- Armory swatch actually drawn: TPC_UICustomize_BladeColor.uc:81-89 -> vanilla LinearColorToFlashHex (UIUtilities_Colors.uc:254-266, truncating int) with UIColorBrightnessAdjust=1.6 (game DefaultUI.ini:69) -> (81, 40, 255) = 0x5128FF.
- Choosing ORIGINAL stores INDEX_NONE; at render the mod substitutes this same fallback so parameterized blades do not go white (TPC_ParticleColorController.uc:341-356). Also used for enemies/Niven sharing the particle templates (ini :45-48).

### (b) Why PSI BLADE COLOR shows only for Templars
- Button gate: TPC_UIScreenListener_CustomizeMenu.uc:88-96 = bEnableArmoryBladePreviewButton && IsBladeColorArmoryCustomizationEligible(Unit, bInArmory, displayed primary).
- Eligibility, X2DownloadableContentInfo_TemplarPsiColorMod.uc:141-157: class template name == 'Templar' (:24-29) -> always yes. Otherwise requires ALL: bEnableAdditionalClassSupport (ini :27, shipped =true), bInArmory (character pool excluded), class name non-empty, rank >= 1, and PRIMARY-slot item template in a HARD-CODED switch.
- The switch, TPC_ParticleColorPatcher.uc:2056-2074: ShardGauntlet_CV/MG/BM, ShardGauntletLeft_CV/MG/BM, CasterGauntlet_CV/MG/BM, CasterGauntletLeft_CV/MG/BM. Nothing else. No weapon category check, no config list. Confidence high.
- Compiled .u matches Src (both 2026-08-29 13:09; .u contains IsAdditionalClassCustomizationEligible). No Documents-side XComTemplarPsiColorMod.ini override exists (C:/Users/Idi/Documents/My Games/.../Config has none).
- Implication: an Amalgamation Psi-Blades soldier (squaddie weapon ShardGauntlet_CV, spec at W/3347798508/Config/XComAmalgamation.ini:9-14, WeaponType gauntlet in primary) at rank >= 1 in the Armory SHOULD already get the button. If it does not, the likely cause is the equipped primary is a non-listed gauntlet template. Active candidates found in configs: PsiShardGauntlet_CV/MG/BM (Psionics Ex Machina 2222545926; True Primary Secondaries 2133399183 config :115-117), LWGauntlet_* (LW2 Secondary Weapons 1140434643), FactionShardGauntlet_* (Additional Mission Types Redux 1133287457), WraithGauntlet*, CultGauntlet_*, RHIGauntlet_*, ExaltedGauntlet. Also rookies (rank 0) and character-pool edits never qualify. Confidence medium (cause not observed in a log; no TPC_UI_ELIGIBILITY line in Launch.log because diagnostics are off).
- Tactical coloring for non-Templars additionally needs a saved color pair (IsAdditionalClassTacticalColorEligible, :162-187).

### jepFixes lines (drafts, NOT written)
Extension to other weapons is impossible by config (hard-coded switch; a code change or a request to the author is the only route). What config CAN do:
```
; jepFixes Config/XComTemplarPsiColorMod.ini  (class is config(TemplarPsiColorMod), TPC_ParticleColorPatcher.uc:9)
[TemplarPsiColorMod.TPC_ParticleColorPatcher]
; one-session diagnostic: logs class, rank, armory, unitPrimary, displayPrimary, eligible per Customize menu open
bEnableCustomizationEligibilityDiagnostics=true
; already default, pin it
bEnableAdditionalClassSupport=true
```
Then grep Launch.log for TPC_UI_ELIGIBILITY after opening a Psi-Blades soldier's customize menu: unitPrimary/displayPrimary tells which template blocks it (log format at TPC_UIScreenListener_CustomizeMenu.uc:160-173). Turn diagnostics off afterwards.
Optional recolor of the "original": override `OriginalTemplarFallbackColor=(X=..,Y=..,Z=..)` in the same section (affects ORIGINAL choice and enemy/Niven shared templates).
