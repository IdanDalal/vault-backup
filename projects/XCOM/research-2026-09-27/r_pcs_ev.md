---
type: research
created: 2026-09-27
author: jep
---
# PCS drops, reusable PCS, Ever Vigilant (read-only research, 2026-09-27)

Receipts use short paths. W = workshop/content/268500, G = XCom2-WarOfTheChosen/XComGame, SDK = WOTC SDK SrcOrig/XComGame/Classes, HL = W/1796402257/Src/XComGame/Classes, LOG = D:/work/vault/projects/XCOM/Launch.log (09-27).

## Item 3a: PCS drop chances

### Verdict
- One tactical PCS so far: plausible bad luck for ~10 missions, suspicious past ~15. Config is NOT cutting the rate today; the jepFixes six-type removal is NOT in effect at all (new finding, high-medium confidence).

### Finding 1: jepFixes PCS removal failed; Cut Content Psionics table is the live one
- LOG 0192.35 / 0640.70: `LootTable index 641/642/643 has a duplicate name (PCSDropsBasic/Rare/Epic) - INVALID` and again at 666/667/668. Three copies of each table survive; engine keeps the first, flags later ones INVALID (same pattern as the BehaviorTable dupes in the same log block).
- Why: jepFixes `-` lines are not byte-exact. Script check (tmp/pcs_cmp.py): every jep `-` line matches its target only whitespace-insensitive, never exact.
  - jep writes `-LootTables=(TableName = "PCSDropsBasic",...`; Cut Content (W/2164176007) has `LootTables = ( TableName = "PCSDropsBasic",...` (space after `(`).
  - LW2 (W/1335226018) and Odd S9 (W/3314720537) tables are multi-line `\\` blocks with tabs; jep flattened them to one line with single spaces.
- Simulation, load order LW2 < CC < OddS9 < jepFixes (exact-match rule): LW2 `-` removes vanilla (exact, verified) and adds L; CC adds C; Odd S9 `-` removes L (exact copy, verified) and adds O; jep removes nothing and adds J. Survivors C, O, J = 3 copies, matching the log count. Every other removal outcome gives 1, 2 or 4 copies.
- Live tables = Cut Content Psionics (first survivor). Sums 100 each, so every PCS roll yields a PCS:
  - Basic: Speed 21, Conditioning 21, Focus 21, Perception 8, Agility 21, Psi 8 (ChanceModPerExistingItem 0.75)
  - Rare / Epic: same shape (21/21/21/8/21/8).
  - So Conditioning, Focus, Agility (63% of each roll) still drop. Combat Awareness, ELS, Body Shield never drop tactically (absent from CC tables). Depth Perception, Hyper-Reactive Pupils, Iron Skin, Macrophages, Combat Rush, Impact Fields, Damage Control, Hacking also absent.
- Psionics Ex Machina (W/2222545926, AddLootTables via HL AddEntryStatic onto the first table by name) adds RollGroup 4 to each PCSDrops table: 30% pexmPCS0 (PexM psi chips) / 70% pexmMELD (Inert Meld). Sum 100, so each PCS roll also gives one PexM item.
- Side note: LOG `X2EquipmentTemplate RarePCSPsi is invalid: references an invalid ability: PCSPsiOffenseBoostRare`. RarePCSPsi is 8% of CC Rare rolls: that drop is a dud item.
- Also the jep table J, if it ever wins, sums Basic 50 / Rare 56 / Epic 66. HL doc (HL/X2LootTable.uc lines 30-60): sum x<100 means (100-x)% chance of nothing. J as written would halve Basic PCS drops.

### Drop mechanics (vanilla, unchanged by mods except count)
- Carriers: `TimedLootPerMission` (SDK XComGameState_HeadquartersXCom.uc:382), vanilla 1 (G/Config/DefaultGameData.ini:650), Covert Infiltration sets 2 (W/2567230730/Config/XComGameData.ini:126). No other active mod or jepFixes touches it (LW2 line commented out).
- ADVENT carriers roll ADVENTEarly/Mid/LateTimedLoot (G/Config/DefaultGameCore.ini:393-395): RollGroup 3 = Chance 50, MinCount 0, MaxCount 1, TableRef PCSDropsEarly/Mid/Late. No active mod redefines these tables; mod enemies (Medic, Pathfinders, Spectrum, drones at 80%) point to them.
- Alien carriers (Sectoid_TimedLoot, Viper_TimedLoot etc., lines 398-400) have NO PCS entry.
- PCSDropsEarly: Basic 75 / Rare 20 / Epic 10 (sum 105, Epic effectively 5%). Mid: 20/60/20. Late: Rare 50 / Epic 50.
- Vulture loot (continent bonus) 50% PCSDrops per vulture roll; only with Vulture.
- Loot expires 3 turns (jepFixes XComLootPostMover.ini); a carrier you never kill or never loot yields nothing.

### Numbers
- P(PCS | ADVENT carrier killed and looted) = 0.50 x P(count 1). MinCount 0 / MaxCount 1: if count is uniform 0..1 (HL doc wording "between MinCount and MaxCount"), 25%; if MinCount 0 is ignored, 50%. Native code not visible; medium confidence on 25%.
- Per mission: 2 carriers x ~0.65 ADVENT share x 0.25..0.50 x ~0.7 killed-and-looted = ~0.23 to ~0.46 PCS per mission. Per kill: ~2 carriers among ~8-12 enemies, so roughly 2-5% per ADVENT kill.
- P(at most 1 PCS), Poisson:
  - 10 missions: 33% (low rate) / 6% (high rate)
  - 15 missions: 14% / 0.8%
  - 20 missions: 5% / <0.1%
- Log has no loot-roll lines (rolls are native, unlogged). Mission count unknown: that number decides the verdict.

### Levers (not applied)
- Fix removal: replace jep `-` lines with byte-exact copies (CC single line verbatim; Odd S9 multi-line block verbatim with tabs and `\\`, the way Odd S9 itself removes LW2). Then rescale J to sum 100 per table or accept 50/56/66% fill.
- Rate: jepFixes XComGameData.ini `[XComGame.XComGameState_HeadquartersXCom] TimedLootPerMission=3`; or raise the PCS entry (MinCount 1 / Chance 75) in ADVENT*TimedLoot via exact `-`/`+`.

## Item 3b: PCS behave like weapon upgrades

### How removal works now
- SDK/UIInventory_Implants.uc:323-355 (HL copy lines 383-390 identical): RemoveImplant: if `XComHQ.bReusePCS` then `PutItemInInventory` (returned); else `RemoveStateObject` (destroyed, comment "Combat sims cannot be reused"). Replacing a PCS without bReusePCS destroys the old one.
- bReusePCS is set only by breakthrough tech `BreakthroughReusePCS` (SDK X2StrategyElement_XpackTechs.uc:1247-1263). With it, the swap popups are also skipped (UIInventory_Implants.uc:248). No continent bonus or resistance order sets it (Lock and Load = bReuseUpgrades only, X2StrategyElement_DefaultContinentBonuses.uc:592).
- Active PCS mods: Remove All PCS Button (W/2782908294) shows its button only when bReusePCS is true (RemoveAllPCSButton.uc:20): inert today. Show Current PCS (2989400002) and Coloured PCS Icons (2425682362) are UI only.
- No "Reusable PCS" style mod exists in the local workshop folder (grep bReusePCS across all 268500 subfolders: only Highlander + Remove All PCS Button). Any such mod name is memory-only, unverified.

### Smallest lever: config only, via Iridar's Template Master (active, W/2363075446)
- Template Master TechTemplate.uc supports bBreakthrough, Requirements, PointsToComplete, Cost and patches all difficulty variants (Help.uc:307 FindDataTemplateAllDifficulties). Syntax proven by active mods (W/2728408174, W/3360388191 XComTemplateEditor.ini).
- Vanilla hides breakthrough-flagged techs from the normal Labs list (SDK XComGameState_HeadquartersXCom.uc:6157-6158). Clearing the flag turns it into a normal research gated by Requirements.
- Draft, new file jepFixes/Config/XComTemplateEditor.ini:
```
[WOTCIridarTemplateMaster.X2DLCInfo_Last]
+Edit_X2TechTemplate = (T = "BreakthroughReusePCS", P = "bBreakthrough", V = "false")
+Edit_X2TechTemplate = (T = "BreakthroughReusePCS", P = "Requirements", Requirements = (RequiredTechs[0] = "ModularWeapons"))
+Edit_X2TechTemplate = (T = "BreakthroughReusePCS", P = "PointsToComplete", V = "600")
```
- Effect: a Labs project "Reuse PCS" appears once Modular Weapons is done (likely at once in this campaign); on completion vanilla ResearchCompletedFn sets bReusePCS; from then on removal returns the PCS, swaps are free, Remove All PCS Button turns on. Legend breakthrough cost is 1200 points (G/Config/DefaultStrategyTuning.ini:569); 600 is a proposal.
- Risks, medium confidence: name/description keep breakthrough wording; a campaign where it was already offered as a breakthrough may list it twice until done; untested in game.
- Instant fallback for this campaign only: console `GiveTech BreakthroughReusePCS` (needs -allowconsole) runs the same ResearchCompletedFn (SDK XComHeadquartersCheatManager.uc:2860-2887).
- Script-mod alternative (if Template Master route misbehaves): X2DLCInfo with OnPostTemplatesCreated wrapping ModularWeapons ResearchCompletedFn (call ModularWeaponsResearchCompleted, then set bReusePCS) plus OnLoadedSavedGameToStrategy retrofit (if ModularWeapons researched and !bReusePCS, set it). ~30 lines. Needed only for "gated on an already-researched tech" in a running campaign.

## Item 4: Ever Vigilant, Reliable EV Redux (3546124299) + Maybe Vigilant (3657133353)

### What each does
- Reliable EV Redux: OnPostTemplatesCreated on 'EverVigilant' removes AdditionalAbilities EverVigilantTrigger / NewEverVigilantTrigger, adds its own M31_ReliableEverVigilant_Trigger (X2DownloadableContentInfo_MeristReliableEverVigilant.uc). Effect listens AbilityActivated (counts invalidating abilities into unit value M31_ReliableEverVigilant_Counter; ignores movement and a long EverVigilantIgnore list: loot, interact, hack starts, toggles) and PlayerTurnEnded (priority 55): if counter 0 and no reserve AP, fires the highest-priority available overwatch from a 25-entry list (Overwatch, PistolOverwatch, Longwatch variants, Reaperwatch, SnapShot, glaive/bow/Rider etc.), adding the needed action point type. No ModClassOverrides.
- Maybe Vigilant: adds per-soldier Enable/Disable toggle abilities + a Pending buff to 'EverVigilant' (AdditionalAbilities AddItem only, removes nothing). It never fires overwatch itself. Blocking: PlayerTurnEnded listener at priority 100 (runs before REVR's 55) increments REVR's own counter for toggled-off units, so REVR skips them. Detects REVR by IsModActive('MeristReliableEverVigilant'). Adds its toggles and a few SJ abilities to REVR's EverVigilantIgnore (Config/Base/XComGame.ini). No ModClassOverrides.
- Third mod on the trigger: Pre-Scamper Ability Stopper (2943434088) adds an unscampered-enemy condition to EverVigilantTrigger and Overwatch; XCOM units always pass. No conflict.

### Interaction
- Complementary layers: REVR = engine (when EV fires, which overwatch), MV = switch (per-soldier opt-out plus UI). Different templates, different listeners, no override collision, no double-fire (MV spawns no overwatch). MV's author recommends REVR (its ini NOTE3).
- LOG: MV patch success at 0181.28; ~30 harmless `Failed to load 'WOTC_ReliableEverVigilant...'` warnings: MV references the older original REV mod (not installed); those code paths are gated by IsREVActive() = false.
- Open check, medium confidence: MV's REVR ignore lines live in Config/Base/. Log evidence suggests Base/ inis are read (MV package loads; the missing-package load attempts match Base/XComEngine.ini). If they were not read, using the toggle would count as an invalidating action for REVR.

### Recommendation
- Keep both. Neither is redundant. Confidence high on no conflict, medium on the Base/ load point.
- Test in game: toggle Disable then Enable on one soldier, move only, end turn: EV should fire. Toggle Disable, move, end turn: no overwatch.
