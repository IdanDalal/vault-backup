---
type: report
created: 2026-10-29
author: jep
---

# Basic Immolator x200+: cause analysis

Read-only. No files edited except this one. Shell was blocked by a worktree guard mid-run; all evidence below comes from Grep/Read on the mod source and config. Game not run, save not read.

## Verdict

Top cause, confidence ~80%: a config chain makes the Basic Immolator a FINITE item, while 5 Amalgamation chemthrower specs use it as their squaddie weapon. The Highlander's loadout code treats the squaddie weapon as an always-available default and creates a fresh copy from thin air whenever a chemthrower soldier's primary slot gets emptied or "upgraded". With a finite template, every fresh copy is a real extra item that lands in HQ stock on the next swap or restore. Net +1 Basic Immolator per chemthrower soldier per strip/unequip cycle.

Plain locker swaps in the Armory are zero-sum. The duplication comes from actions that EMPTY the primary slot (Make Weapons Available, Unequip Squad/Barracks, wounded unequip, covert action / infiltration unequip, training slots, class pick).

## 1. Item identity (confidence 99%)

- Display name "Basic Immolator" = template `MZImmolator_CV`
  - rename: `268500/3315142674/Localization/XComGame.int:133-135` (Chemthrower Addon Redux)
- Template defined in Immolator + Chemthrower Abilities (1918448514)
  - `268500/1918448514/Src/ImmolatorChemthrower/Classes/X2Weapon_Immolator.uc:71` CREATE `MZImmolator_CV`, Tier 0 (line 78), WeaponCat chemthrower (74)
  - shipped as `CanBeBuilt=false`, `bInfiniteItem=true`, `StartingItem=true` (lines 110-112)
- Squaddie weapon for chemthrower specs (all active):
  - Desolator `268500/2837085224/Config/XComAmalgamation.ini:13`
  - Salamander `268500/2889808819/Config/XComAmalgamation.ini:13`
  - Toxicologist `268500/3318678864/Config/XComAmalgamation.ini:13`
  - Pioneer / Paramedic `268500/3311953486/Config/XComAmalgamation.ini:23` and `:249`
  - Amalgamation turns that into the class `SquaddieLoadout`: `268500/2428993550/Src/AmalgamationClassesWOTC/Classes/X2SoldierClass_Amalgamation.uc:158-159`, `MakeSquaddieLoadout` 295-320

## 2. How it became finite (confidence 80%)

- Immolator Overhaul (2237137501) ships a Prototype Armoury compat file:
  - `268500/2237137501/Config/Compatibility/XComStrategyTuning.ini:1-3` `[PrototypeArmoury.PATemplateMods] +arrMakeItemBuildable=(ItemName="MZImmolator_CV")`, trading value 6
  - line 6 kills the Flametorch->Immolator schematic `IRI_Flamethrower_TLE_Schematic`
- Prototype Armoury (2567230602) is ACTIVE (settings.json ~line 680)
  - `268500/2567230602/Src/PrototypeArmoury/Classes/PATemplateMods.uc:111-113` sets `CanBeBuilt=true`, `bInfiniteItem=false`, `CreatorTemplateName=''`
  - called every launch from `X2DownloadableContentInfo_PrototypeArmoury.uc:31`; empty DLC field always passes (`PAHelpers.uc:10-11`)
- Same treatment for tiers 2/3: `268500/1918448514/Config/XComStrategyTuning.ini:14-15` (MZImmolator_MG/BM finite)
- Template Master edit also drops StartingItem: `268500/2237137501/Config/XComTemplateEditor.ini:15`
- Gap: the compat file sits in a Config SUBFOLDER. I could not prove from source that the engine loads subfolders. Supporting evidence: Five Tier Weapon Overhaul (3350314521, active) keeps its live gameplay edits in subfolders (`Config/Shotgun/XComTemplateEditor.ini:108-112` etc.), and the player sees a COUNT of 200+, which only a finite stack produces. Infinite items never show a quantity.
- The only infinite chemthrower left in HQ is the Flametorch `IRI_Flamethrower_TLE` (tier -1): `268500/2237137501/Config/XComFlamerTLE.ini:49-53`

## 3. The minting mechanism (code-level confidence 95%)

All in the active Highlander, `268500/1796402257/Src/XComGame/Classes/`:

- `XComGameState_Unit.uc:12847-12882` `GetCompleteDefaultLoadout` puts the class SQUADDIE loadout first, with no finite check
- `XComGameState_Unit.uc:12448-12503` `GetBestPrimaryWeaponTemplates` seeds the list with that default (MZImmolator_CV), then adds only INFINITE HQ weapons of equal or higher tier. Nothing infinite beats tier 0 for a chemthrower class, so MZImmolator_CV stays at index 0.
- `XComGameState_Unit.uc:12300-12315` `GetBestPrimaryWeapon` = `CreateInstanceFromTemplate` (new item, nothing taken from HQ)
- `XComGameState_Unit.uc:12116-12122` `ValidateLoadout`: empty primary -> GetBestPrimaryWeapon -> equip
- `XComGameState_Unit.uc:11983-12053` `UpgradeEquipment`: empty slot -> CreateInstanceFromTemplate (12014); lower tier same WeaponCat (Flametorch -1 < Immolator 0) -> old item to HQ, new instance created (12046-12052)
- `XComGameState_Unit.uc:11851-11907` `ApplyBestGearLoadout` runs UpgradeEquipment on primary, then ValidateLoadout
- `XComGameState_Unit.uc:12769-12844` `MakeItemsAvailable`: removed items -> `PutItemInInventory`, then ApplyBestGearLoadout (12842)
- `XComGameState_HeadquartersXCom.uc:4232-4259` `PutItemInInventory`: finite unmodified item -> HQ stack Quantity += 1; infinite unmodified -> destroyed (4261-4265). This branch is the whole difference: with the template infinite, the fresh copy would vanish harmlessly.
- `XComGameState_Unit.uc:12920-13028` `EquipOldItems`: takes the stored item back from HQ, puts the minted one into HQ (13027) -> net +1

Cycle per chemthrower soldier: strip (old Immolator -> HQ +1) -> best-gear fills slot with a NEW Immolator -> restore (old one back, new one -> HQ). HQ +1, every time.

## 4. Ranked triggers (all feed cause #3; confidence that each mints when it fires: 90%; share of the 200: unknown without the save)

1. Armory "Make weapons available" (strip weapons/gear/items) then leaving the screen. Strips EVERY other eligible soldier, then restores. +N per use, N = chemthrower soldiers stripped.
   - `UIArmory_Loadout.uc:445-483` (strip weapons, MakeItemsAvailable bStoreOld=true), `:485-511` ResetAvailableEquipment -> EquipOldItems; target list `:529-559`
   - Vanilla Squad Select equivalents: `UISquadSelect.uc:814, 1110, 1155, 1204`, restore `:1588`
   - Best fit for "equip/unequip duplicates them"
2. robojumper Squad Select "Unequip Squad" / "Unequip Barracks": `268500/1122974240/Src/robojumperSquadSelect/Classes/robojumper_UISquadSelect.uc:1087` and `:1148` (MakeItemsAvailable, bStoreOld=false). Barracks button = +1 per chemthrower soldier in the whole barracks per click.
3. Post-mission wounded unequip: `XComGameStateContext_StrategyGameRule.uc:1537-1539`. +1 per wounded chemthrower soldier. Shut off THIS WEEK by Dont Unequip.
4. Covert actions / CI infiltrations: `XComGameState_CovertAction.uc:371-374`. Also shut off this week by Dont Unequip.
5. Training / facility slots: `X2StrategyElement_DefaultStaffSlots.uc:765, 1043`; CI academy `268500/2567230730/Src/CovertInfiltration/Classes/X2Helper_Infiltration_TemplateMod.uc:1114`, squaddie + best gear `XComGameState_HeadquartersProjectTrainAcademy.uc:84-85`
6. Squaddie promotion / Choose My Class: `XComGameState_Unit.uc:11790` (ApplySquaddieLoadout always creates the item); Choose My Class `268500/1467643380/Src/WOTC_ChooseMyClass/Classes/UIChooseClass_WOTC_ChooseMyClass.uc:510-513` (strip + squaddie loadout + best gear; rank-0 only, so about one per soldier). Bounded by soldier count (40 start), small share.

Scale check: 10 chemthrower soldiers x 20 strip cycles = 200. Plausible over a campaign with 40 starting soldiers.

## 5. Week-added mods

- Dont Unequip (1539496987): config only, two Highlander flags. `268500/1539496987/Config/XComGame.ini:4-6` (`bDontUnequipWhenWounded`, `bDontUnequipCovertOps`). Source file is an empty class. It REMOVES triggers 3 and 4. Cause: no, confidence 90%.
- Automated Loadout Manager - Fixed (3822286199): possible amplifier, confidence 30%.
  - Never calls CreateInstanceFromTemplate, so it cannot mint by itself.
  - Flaw: on an unlocked loadout it "looks for a better version" via `FindBestReplacementItemForUnit`, which only accepts INFINITE items of the same WeaponCat (`XComGameState_ALS.uc:837-846`, chosen at 479-491). The only infinite chemthrower is the tier -1 Flametorch, so it can swap a soldier DOWN to a Flametorch and drop the Immolator into HQ (+1 visible). The next best-gear pass then upgrades the Flametorch to a freshly minted Immolator (UpgradeEquipment, above). Fires on Squad Select init/focus when the squad grows (`UIScreenListener_ALS.uc:33-50, 74-88, 117-128`) and only when the saved item ID differs from the equipped one, which strip/restore cycles cause.
  - Its trim pass (`XComGameState_ALS.uc:338-385`) submits removals before the equip step; a failed equip could leave the primary empty for the next ValidateLoadout. Edge case.
- Reusable Hunter Axe, Build items menu sorting fix, Fast Save/Load List, Commands UI: zero item add/remove/create calls in their Src (grep of MakeItemsAvailable / ValidateLoadout / ApplyBestGearLoadout / CreateInstanceFromTemplate / PutItemInInventory / RemoveItemFromInventory). Cause: no, confidence 90%.
- Iridar's Loadout Manager disabled: irrelevant to the mint path.

## 6. Ruled down

- XSkin (2337161588) attaches a component to reskinned weapons, which makes `HasBeenModified` true (`XComGameState_Item.uc:807-809`), so reskinned infinite Immolators would be stored as SEPARATE rows. Only matters if the 200 are 200 rows instead of one counted stack. Confidence 10%.
- Chemthrower Addon Redux console cheat `RustyFix_ToolBox_Alchemists_Addons` adds 5 each (`X2DownloadableContentInfo_WOTC_Rusty_Alchemist_AddonRedux.uc:651-715`). Only if someone typed it.
- Zelf Class Requirements Begone `AddMissingStartingItems` only adds missing INFINITE starting items (`X2DLCInfo_ZelfClassRequirementsBegone.uc:363`). No.
- jepFixes: no Immolator, chemthrower or SquaddieWeapon lines (grep). No.

## 7. Fixes, safest first

A. Root fix, recommended: make MZImmolator_CV infinite again by cancelling the PA entry.
   - jepFixes, new `Config/XComStrategyTuning.ini`:
     ```
     [PrototypeArmoury.PATemplateMods]
     -arrMakeItemBuildable=(ItemName="MZImmolator_CV")
     -arrTradingPostModifiers=(ItemName="MZImmolator_CV", NewValue=6)
     ```
   - Risk: a `-` line only removes an entry already merged, so jepFixes must load after 2237137501. Load order unverified. Fallback: comment lines 2-3 of `268500/2237137501/Config/Compatibility/XComStrategyTuning.ini` (a workshop update would revert it).
   - Effect: the existing HQ stack turns into the infinite entry (count display disappears); future mints get destroyed on return. ALM then prefers the Immolator (tier 0) over the Flametorch.
   - Cost: the tier-1 Immolator stops costing supplies, the same as vanilla conventional weapons. In a NEW campaign there is no way to get one (StartingItem=false per Template Master line 15, schematic killed by compat line 6). The current save already holds the item.
   - Do NOT use a Template Master `bInfiniteItem` edit instead: both run at template creation, and their order relative to PA is unknown.
B. Keep the PA economy: switch the 5 chemthrower specs' `SquaddieWeapon` to the infinite Flametorch `IRI_Flamethrower_TLE`. Five struct entries in four addon inis, each needs exact `-`/`+` struct replacement. More edits, more ways to break. The ALM downgrade quirk stays.
C. Behaviour only, no config: stop using Make Weapons Available and the robojumper Unequip buttons; keep Dont Unequip on. Promotions and training slots still mint, slowly.
- Surplus already in stock: under A it becomes moot. If it stays finite, selling 200 on the Black Market (value 6 each) is an exploit; that ruling belongs to the player.

## 8. In-game confirmation (use a throwaway save)

1. Engineering > Inventory or the primary locker: Basic Immolator shows ONE row with a quantity -> finite stack (supports the verdict). 200 separate rows -> modified copies (points at XSkin/upgrades instead).
2. Engineering > Build Items lists Basic Immolator with a supply cost -> PA made it finite.
3. Repro: note count X. Count chemthrower-primary soldiers who are idle in the barracks: N. Open a NON-chemthrower soldier's loadout, primary slot, "Make weapons available", accept, then leave the loadout screen. Expect X + N. Repeat: +N again.
4. Repro 2: robojumper Squad Select with one chemthrower soldier in squad, "Unequip Squad": +1.
5. Control after fix A: repeat step 3, no growth, count display gone.

## Gaps

- Subfolder config loading inferred from evidence, not proven (the reason the verdict is 80%).
- Save not read: the split of the 200 across triggers is unknown.
- jepFixes vs workshop load order for the `-` lines unverified.
