---
type: report
created: 2026-11-12
author: Agent audit-strategy
---
# jepFixes strategy-layer block audit (2026-11-12)

Scope: capture-risk lever, faction-card removal, Chosen trait whitelist, CI sitrep exclude list, dark-event count, Emergency Defense removal, Immolator line, Living Space, Loot Post Mover.
Read-only. Scratch scripts sit beside this file (`active.py`, `cfgscan.py`, `shapes.py`, `cards.py`).

Ground facts used by every block:
- All mods named below are `isActive: true` in `C:\XCOM2 AML 1.6.0-beta\settings.json` (checked by `active.py`). 1128 entries, 1080 active.
- jepFixes loads after every workshop mod: `Checking DLC installation for ...\XComGame\Mods\jepFixes` is line 2376 of each log, after the last workshop line (2258 block). Four other local mods (`jepClassWeights`, `jepGTSFilter`, `jepNoCoverGrabs`, `jepReusePCS`) sit around it; none of them touches a key audited here (cfgscan).
- Logs on disk now: EIGHT, not nine. `Launch-backup-2026.11.09-12.23.56.log` (the campaign-start session) rotated out between my first pass and the resume. Lines quoted from it below were read before it vanished and cannot be re-read. Current set: 11.09-14.46.32, 11.09-16.21.25, 11.09-19.25.31, 11.10-10.53.43, 11.10-13.28.40, 11.11-16.56.21, 11.12-12.07.47, Launch.log (11-12).
- The live campaign was created in the rotated log: one `UIShellDifficultySW` / `UIChooseIronMan` sequence at [0423-0525], none in any later log.
- Highlander `Src` holds only the classes it changes (inferred: `XComGameState_StrategyCard.uc` and `X2StrategyElement_DefaultCovertActions.uc` are absent from it). For untouched classes the running script is `SrcOrig`.
- The engine loads ini files from SUBFOLDERS of a mod's `Config` (proved in section 7: the runtime count of a merged array matches only a recursive merge). A mod's `Config\Compatibility\*.ini` is live.
- Larger listener priority runs first (`CHEventListenerTemplate.uc:10`), so the lower-priority listener has the last word.
- Save used as ground truth: `...\SaveData\save_Save 258_1` (Geoscape, in-game 4/12/2035, written 2026-11-12 13:03, campaign start stamp `2026.11.09-10.10.14` in its header). Method in section 10.

---

## 1. Capture risk off (`XComGameBoard.ini:10-11`)

Intent: `CovertActionRisk_SoldierCaptured` never attaches to any covert action.

Lever: correct.
- Class `X2DownloadableContentInfo_ConfigurablePosthumousRisks ... config(GameBoard)`, `var config array<AbiziRiskBehavior> ChangeRisk` (2823200756 `Src\...\X2DownloadableContentInfo_ConfigurablePosthumousRisks.uc:11,26`). Section, file name, key, enum value `alwaysOff` (line 15) all match.
- `OnPostTemplatesCreated` swaps `IsRiskAvailableFn` for a function returning false (lines 42-52, 63, 81-84).

Bypass check:
- Risk attach at action creation: `XComGameState_CovertAction.uc:969` (Highlander) calls `IsRiskAvailableFn`; false means no `AddRisk`.
- Second gate at action start: line 1249 negates any template risk whose `IsRiskAvailableFn` now returns false, so an action generated before the block would still be cleaned.
- Dark-event risk path (`TriggerAllowDarkEventRisk`, line 1124-1141) also starts from `IsRiskAvailableFn`; the only listener (CI, `X2EventListener_Infiltration.uc:195`) can only turn it further off.
- No other active mod with source sets `IsRiskAvailableFn` on this template (grep of all workshop `.uc`: only CI's own flat-risk templates). `WOTC_MoreEngineeringRepairSlots` 2165999454 line 584-587 changes `FindTargetFn` only.
- CI infiltration actions carry only flat-risk sitrep risks (`X2StrategyElement_InfiltrationActions.uc:176-187`), never Captured.
- Capture in tactical play (Chosen kidnap, soldiers left behind) is a different mechanic and outside this lever.

Log evidence:
- CI logs every risk attached to a non-infiltration action: `CI: Risk modifier for <risk> is ...` (`X2EventListener_Infiltration.uc:237`, fired from `AddRisk` via `CalculateRiskChanceToOccurModifiers`).
- Eight logs: 266 lines `CovertActionRisk_SoldierWounded`, 60 lines `CovertActionRisk_Ambush`, **0 lines `CovertActionRisk_SoldierCaptured`**. Example `Launch-backup-2026.11.09-14.46.32.log:57743-57746`.
- No `UISoldierCaptured` screen, no `CovertActionSoldierCaptured_Central` in any log.
- Gap: the risk lines do not name the action. The 11 action types that finished (BlackMarket, BreakthroughTech, FindFaction, FindFarthestFaction, ImproveComInt, PatrolWilderness, PersonnelRescue, PreparePersonnel, ResistanceCard, SharedAbilityPoints, UtilityItems) carry no Captured risk in their templates anyway. The logs cannot show that an action whose template lists Captured (IncreaseIncome, RemoveDoom, ResistanceContact, FacilityLead, RevealChosenStrengths, CancelChosenActivity, AlienLoot, AlienCorpses, ExperimentalItem, GatherSupplies, GatherIntel, PrepareUFO) was on the board.

Save evidence (method in section 10; save `save_Save 258_1`, Geoscape, written 11-12 13:03):
- Five covert actions on the board whose templates list Wounded, Captured, Ambush: `CovertAction_CancelChosenActivity` (Skirmishers, blob offset 9097606), `CovertAction_RevealChosenStrengths` x3 (Reapers 10108514, Templars 10170241, Skirmishers 10215907), `CovertAction_RemoveDoom` (18777751). Each has `Risks = [SoldierWounded, Ambush]` and `NegatedRisks = [SoldierCaptured]`.
- Vanilla availability (`IsRivalChosenAlive`, `SrcOrig\...\X2StrategyElement_DefaultCovertActionRisks.uc:217-238`) returns true while the rival Chosen is undefeated, and all three Chosen are alive in this save. So the missing risk comes from the swapped function, which is the lever.
- `CovertActionRisk_SoldierCaptured` occurs 10 times in the save: 5 as `NegatedRisks` entries, 5 as the target of a `Reward_DecreaseRisk` slot reward. Zero times inside a `Risks` array.

Verdict: **HOLDING** (high confidence). Five live actions that would carry the risk in vanilla do not.

---

## 2. Faction orders removed (`XComGameData.ini:10-44`, 31 names)

Intent: the listed `ResCard_*` never appear as a Resistance Order or as a continent bonus.

Lever: correct.
- `var config(GameData) array<name> arrRemoveFactionCard` on `X2Helper_Infiltration_TemplateMod` (CI `X2Helper_Infiltration_TemplateMod.uc:16`). Section `[CovertInfiltration.X2Helper_Infiltration_TemplateMod]`, file `XComGameData.ini`, key and quoting identical to CI's own lines (`2567230730\Config\XComGameData.ini:4-16`).
- All 31 names exist as vanilla templates (`cards.py` against `SrcOrig\...\X2StrategyElement_XpackResistanceActions.uc`), so `CardTemplate.Category = "__REMOVED__"` (line 1364) never hits None.
- Only `+` lines, so no byte-match question.

Bypass check:
- Card state objects are created once, at campaign start, only for `Category == "ResistanceCard"` (`SrcOrig\...\XComGameState_StrategyCard.uc:66-79`, called from Highlander `XComGameStateContext_StrategyGameRule.uc:192`). A removed card has no state object.
- Every draw iterates existing card states (`XComGameState_ResistanceFaction.uc:1134,1162,1185-1189`), so a card with no state cannot be drawn by faction meeting, influence gain or the Resistance Card covert action.
- Continent bonus assignment: vanilla (`XComGameState_StrategyCard.uc:75-91`) and Modify Continent Bonuses 1145436332 (`X2DownloadableContentInfo_ModifyContinentBonusWOTC.uc:33`) both filter on `Category == "ResistanceCard"`.
- Remaining creators of card states by name: console commands only (1145436332 line 131, XpanD's Console Commands 3113132590 line 632).
- Timing: RemoveFactionCards runs in CI's OnPostTemplatesCreated (`X2DownloadableContentInfo_CovertInfiltration.uc:640`), before any campaign start. The campaign began 11-09, after the 09-19 edit.

Log evidence:
- `CI: Suffocating Faction Cards` once per launch in all logs (e.g. `Launch.log`, CI line 1359): the function runs.
- Rotated campaign-start log `Launch-backup-2026.11.09-12.23.56.log:51585-51599`: Idi opened the continent-bonus toggle screen and disabled exactly 11 (`ResCard_MentalFortitude, SuitUp, NobleCause, DoubleAgent, Sabotage, BombSquad, ResistanceNetwork, RapidCollection, Scavengers, MunitionsExperts, ArtOfWar`), then a `UIDialogueBox_0` init 2.3 s after the 11th, then `Screen closed! Ignore Length: 11`.
- That screen lists templates with `Category == "ResistanceCard" && bContinentBonus` (`UIToggleContinents.uc:80-81`) and refuses a disable that would leave fewer than one spare (`:159`). `cards.py` over base + all active mods: 36 continent-eligible templates; 7 removed by CI alone would leave 29; CI + jepFixes removals leave **17**. 17 - 11 = 6 = the six continents, the kept six being BetweenTheEyes, InsideKnowledge, IntegratedWarfare, MachineLearning, TrialByFire, Tithe. With a pool of 29 he would have needed 23 disables to reach six, and the refusal dialog would not have fired after the 11th. The dialog is the screen's only dialog and fires exactly when the pool is 17.
- So the 12 jepFixes-only continent-eligible names (BondsOfWar, DecoysAndDeceptions, Feedback, LiveFireTraining, PrivateChannel, PursuitOfKnowledge, QuidProQuo, RecruitingCenters, RunSilentRunDeep, StayWithMe, Vengeance, WeakPoints) were already `__REMOVED__` when the campaign was created. The other 19 names ride the same array and loop.
- No log line names any drawn card, so there is no direct card-form evidence in the logs.

Save evidence (`save_Save 258_1`): the whole save holds exactly 20 distinct `ResCard_*` names: ArtOfWar, BetweenTheEyes, BombSquad, DoubleAgent, HeavyEquipment, InsideKnowledge, IntegratedWarfare, MachineLearning, MentalFortitude, ModularConstruction, MunitionsExperts, NobleCause, RapidCollection, ResistanceNetwork, ResistanceRisingI, Sabotage, Scavengers, SuitUp, Tithe, TrialByFire. Vanilla has 52 card templates; 52 minus the 32 on the merged removal list (31 jepFixes + CI's Vulture) = 20. None of the 31 jepFixes names has a card state, so none can be drawn or assigned.

Verdict: **HOLDING** (high confidence). Two independent receipts: the 17-card continent pool at campaign creation, and 20 card states in the 11-12 save.
Consequence worth knowing: only 20 orders exist in this campaign, 17 of them continent-eligible, 6 of those consumed as continent bonuses. That leaves 14 orders for three factions.
Side note for the lead: the header comment in the ini says Idi keeps Resistance Network as a continent bonus; on 11-09 he disabled it and kept Tithe. The comment is stale, the block is unaffected.

---

## 3. Chosen trait whitelist (`XComGameData.ini:52-77`)

Intent: Chosen roll strengths only from 13 names and weaknesses only from 10.

Lever: correct.
- `var config array<name> ChosenStrengths / ChosenWeaknesses` on `XComGameState_AdventChosen` (Highlander `XComGameState_AdventChosen.uc:147-148`), section `[XComGame.XComGameState_AdventChosen]`, file `XComGameData.ini` (same file the base game and six mods use for these keys).
- `!ChosenStrengths=()` then `+` lines. jepFixes loads after every other contributor (base, RestoredChosenTraits 1133896546, ABetterChosen 1762615740, FixedAgile 2211077969, OddS9Tweaks 3314720537, WoTCPathfinders 1229048071, FrostDivision 2481645156; cfgscan), so the wipe lands last.

Bypass check:
- Starting roll and level-up roll both read `default.ChosenStrengths/Weaknesses` (`:209-232`, `:577-595`). `AddTrait` rejects names outside the lists (`:359-366`). Chosen Rechosen 3775981048 reads the same defaults (`X2EventListener_ChosenRechosen.uc:343`).
- Hard-coded exception 1: with Lost and Abandoned on, the Assassin gets `ChosenShadowstep` regardless (`:267-271`). Not triggered in this campaign (the save shows no Shadowstep).
- Hard-coded exception 2: A Requiem For Man: Gameplay Mutators 2795578857 pushes its own strengths straight into `ChosenState.Strengths` (`ARFM_DESW_StrategyActions.uc:1483-1614, 2551-2690`: `ARFMDedication*`, `ARFMAspect*`, `ARFMCapstone*`, `ARFMKeystone*`). These never consult the whitelist. None present in the save yet.
- Level-up fallback list copies other Chosen's strengths (`:561-574`), so it stays inside the whitelist.

Log evidence: none. No log line names a rolled trait.

Save evidence (`save_Save 258_1`, offsets 12652292 / 12655257 / 12658363):
- Hunter: Strengths `[ChosenIncreaseCrit, None]`, Weaknesses `[ChosenReaperAdversary, ChosenGroundling]`.
- Warlock: Strengths `[ChosenWatchful, ChosenHoloTargeting]`, Weaknesses `[ChosenTemplarAdversary, ChosenWeakPsi]`.
- Assassin: Strengths `[ChosenLowProfile, ChosenRevenge, ChosenIncreaseMobility]`, Weaknesses `[ChosenSkirmisherAdversary, ChosenWeakEnviro]`.
- Every name is on the whitelist. No struck name occurs anywhere in the save (23 struck names searched; the single `ChosenBrutal` hit is the mod id `ChosenBrutalFix` in the header).
- The pool ran dry, which only the whitelist explains: `StartingNumStrengths` is 3 (OddS9Tweaks `XComGameData.ini:38-39`), yet Hunter and Warlock hold 2 entries and the Hunter's second entry is the name `None` (array count 2, hex at 12652348). The six real strengths across the three Chosen are six of the thirteen whitelisted names.

Verdict: **HOLDING** (high confidence for the starting roll; level-ups read the same list).
Side effect to rule on (medium confidence on the mechanism): the whitelist is too small for three Chosen at force level 1. Line `:313-314` indexes an empty `AllStrengths` and stores `None`; the Hunter carries a dead strength slot and two Chosen started one strength short.

---

## 4. CI environmental sitrep exclude list (`XComGameData.ini:82-134`, 52 names)

Intent: Covert Infiltration's random environmental sitrep never picks one of the 52.

Lever: correct.
- `var config(GameData) array<name> ENVIROMENTAL_SITREPS_EXCLUDE` on `X2Helper_Infiltration` (CI `X2Helper_Infiltration.uc:55`); section and file match CI's own line (`2567230730\Config\XComGameData.ini:180-181`). Unquoted names, same as CI's.
- Names: 47 of 52 exist as sitreps in active config (`sitnames.py`). Not found: `ARFMDESitrep_MutonGrenades`, `AbiziOTS_Leadership0-3`. Inert if the templates do not exist; harmless.

Bypass check (paths that add a sitrep to a CI mission without reading the list):
- Consumer: `GetAllEnviromentalSitreps` (`:830-879`) subtracts the list; `SelectEnviromentalSitreps` (`:882-956`) draws only from the result. This path is covered.
- Flat-risk sitreps: `X2Helper_Infiltration.uc:786-799` (assault missions) and `XComGameState_MissionSiteInfiltration.uc:190,229`. Not covered.
- Over-infiltration bonus sitreps: `X2Helper_Infiltration.uc:751-781`, `X2StrategyElement_DefaultOverInfiltrationBonuses.uc:93`. Not covered.
- So listed names that are CI risk or bonus sitreps (ShoddyIntel, IntelligenceLeak, UpdatedFirewalls, WellRehearsed, MentalReadiness, ExperimentalStims, OpportuneMoment1/2 and similar) still arrive through their own mechanic. `GetAllEnviromentalSitreps` already removes them from the environmental pool (`:861-876`), so those list entries change nothing.
- Forced sitreps in mission definitions and sitreps added by other mods' listeners are outside this lever.

Evidence:
- Sitreps on missions, from the save (`ActiveSitReps` / `SitReps` arrays, 10 arrays) and from `BeneathSuspicionMission: Tag:` log lines (e.g. `Launch-backup-2026.11.10-13.28.40.log:108300`, `Launch-backup-2026.11.12-12.07.47.log:104694,130341`, `Launch.log:106964`): ARFMDESitrep_ExtraAction, PathfinderSearchTeams, RRHIncursion, ARFMDESitrep_HazmatLoots, ARFMDESitrep_XCOMGrenades, AftermathSitRep, TheLost, TheHorde, AbiziBanRuler, AbiziBanChosen.
- None of the ten is on the list. About six are random draws. With a dead list roughly 30-40% of the pool would be listed names (47 of 116 known sitreps), so six clean draws by luck has a chance of roughly 5-15% (my estimate, rough).

Verdict: **UNPROVEN, leaning holding**. No violation in ten mission sitrep arrays; the support is statistical. Neither logs nor save tell an environmental draw from other sitrep sources.
Probe: after about ten more missions rerun `savescan.py` then `ctx.py "SitReps"` on the newest save; a listed name on a CI mission that is not a CI risk or bonus sitrep = FAILING. The console command `ForceNextEnviromentalSitrep` is no probe: it skips the list by design (`:899-903`).

---

## 5. Dark-event count (`XComMoreDarkEvent.ini`; no other dark-event count key exists in jepFixes)

Intent: 1, 2, 2, 3, then 3 per month; doom adds nothing; never 4.

Lever: correct.
- `class X2EventListener_MoreDarkEvents ... config(MoreDarkEvent)` with `PerMonthDarkEvent`, `PerDoomFormulaSlope`, `PerDoomFormulaConstantTerm`, `MaxDarkEvents` (3078247580 `X2EventListener_MoreDarkEvents.uc:1-11`). Section, file name and `Key[n] = v` syntax equal the mod's own ini.
- Competing writers: the mod itself and OddS9Tweaks 3314720537 (`XComMoreDarkEvent.ini:15-30`: third month 3, slope 0.33, constant term 1, cap 6). OddS9Tweaks is ACTIVE, so without jepFixes every month gets at least +1. jepFixes loads after both and sets all seven indices.
- Listener order: CI also listens to `OverrideDarkEventCount` at priority 99 (`X2EventListener_Infiltration.uc:88, 828-857`), this mod at 50 (`:28`). Larger runs first, so this mod's number is final.

Bypass check:
- **Leak, by the mod's own code**: after `Min(..., MaxDarkEvents)` the listener adds 1 when a Chosen played its Dark Event action (`:69-75`; flag set at Highlander `X2StrategyElement_XpackChosenActions.uc:380`). A capped month of 3 becomes 4 in that case. No config key in this mod prevents it. CI's source does not remove `ChosenAction_DarkEvent`.
- `NumEvents -= ChosenDarkEvents.Length` afterwards only lowers the number (`XComGameState_HeadquartersAlien.uc:1810`).

Evidence:
- Logs: no line reports the count.
- Save: `NumMonths = 1` (one monthly roll done). Exactly one dark-event state has `TimesPlayed` set, value 1 (`ARFMDE_SupremeArmor`, offset 10827251); AlienHQ `ChosenDarkEvents` count = 1; no `ActiveDarkEvents`. So the only roll so far produced 1 event.
- jepFixes predicts 1 for month index 0. OddS9Tweaks' values, which would rule if jepFixes were dead, predict at least 2 (1 + constant term 1). The observed 1 fits jepFixes only.

Verdict: **HOLDING for the per-month number and the zeroed doom term** (one roll observed; medium-high confidence). **"Never 4" is not guaranteed**: the Chosen +1 sits outside the cap.
Probe for the later months: at the third monthly report the screen shows 2 new dark events (OddS9 values would show 4 or more); rerun `prop.py TimesPlayed` and `prop.py ChosenDarkEvents` on a save made right after it.

---

## 6. Emergency Defense removed (`XComMissionDefs.ini`, three `-arrMissions`)

Intent: `EmergencyDefense_Reapers/Templars/Skirmishers` never spawn.

Lever: correct.
- Section `[XComGame.XComTacticalMissionManager]`, file `XComMissionDefs.ini`, as in the source mod.
- Byte check (`bytecmp.py`, raw bytes including CRLF, tabs and the `\\` continuations): all three `-` entries are an EXACT byte match of `+` entries in Additional Mission Types Redux 1133287457 `Config\XComMissionDefs.ini` (active).

Bypass check: a mission type is generated from an `arrMissions` entry; with the entries gone the family `Extract` resolves to the remaining definitions. No other active mod re-adds the three names (they are absent at runtime, below).

Log evidence:
- Mission Beneath Suspicion 3000011407 prints every `arrMissions[i].sType` at startup (`X2DownloadableContentInfo_MissionBeneathSuspicion.uc:49`). `Launch.log` has 115 such lines.
- `Current mission sType is  EmergencyDefense` count: 0 in all eight logs. Sibling entries from the same source file are present (e.g. `MRExtract`, `MRSupplyExtraction`, `Launch-backup-2026.11.09-14.46.32.log:19471-19473`).

Verdict: **HOLDING** (high confidence). The runtime array lacks the three definitions.

---

## 7. Immolator no longer finite (`XComStrategyTuning.ini:6-7`)

Intent: remove `MZImmolator_CV` from Prototype Armoury's make-buildable list so the weapon stays infinite and stops duplicating.

Lever: correct, with a twist.
- `class PATemplateMods ... config(StrategyTuning)`, `var config array<ItemFromDLC> arrMakeItemBuildable` (2567230602 `PATemplateMods.uc:1,4`); section `[PrototypeArmoury.PATemplateMods]` matches.
- The `+` line lives at `2237137501\Config\Compatibility\XComStrategyTuning.ini:2`, a subfolder. Its text equals the jepFixes `-` line.

Bypass check: `MakeItemBuildable` (`:59-65, 111-113`) is the only place this mod sets `bInfiniteItem = false`; ImmolatorChemthrower 1918448514 lists only `_MG` and `_BM`.

Log evidence:
- `PrototypeArmoury: Making 156 items buildable` in all eight logs (e.g. `Launch-backup-2026.11.09-14.46.32.log:19223`, source `PATemplateMods.uc:57`).
- `pacount.py` replays the merge over active mods in load order: top-level `Config` only gives 100 entries; with subfolders it gives 157 before the jepFixes line and **156 after it**. The logged 156 matches only "subfolders are loaded and the removal applied".
- Save: 3 `MZImmolator_CV` name occurrences in total; no pile of copies.

Verdict: **HOLDING** (high confidence).

---

## 8. Living Space numbers (`XComLivingSpace.ini`)

Intent: start limit 50, upgrade 1 +20, upgrade 2 +30.

Lever: correct. `LSHelpers ... config(LivingSpace)` `STARTING_CREW_LIMIT` (3309295545 `LSHelpers.uc:1,12`); `X2StrategyElement_LSFacilityUpgrades ... config(LivingSpace)` `CrewSizeUpgrades` (`:1,17`). Mod defaults are 30, +10, +20 (`3309295545\Config\XComLivingSpace.ini:19-30,44`). `!CrewSizeUpgrades=()` then two `+` lines; jepFixes loads after the mod. The mod's MCM page holds only a display toggle.

Bypass check: the limit is stored in campaign state at campaign start (`XComGameState_LivingSpaceData.uc:56,62`) and raised by `ADDCREW` when an upgrade completes (`X2StrategyElement_LSFacilityUpgrades.uc:66,79`). Otherwise only the mod's console commands change it.

Evidence: no log lines. Save: `CurrentCrewLimit = 50` in an older history frame (offset 10035099) and `= 70` in the current one (19587596). 50 is the jepFixes start value (mod default 30); 70 = 50 + 20 is upgrade 1 at the jepFixes size (mod default +10).

Verdict: **HOLDING** for the start limit and upgrade 1 (high confidence). Upgrade 2 (+30) rides the same array; unobserved.

---

## 9. Loot expiry (`XComLootPostMover.ini`)

Intent: all field loot expires after 3 turns; psi loot raised from 2 to 3.

Lever: correct since the 09-28 section fix. `class XComGameState_LootDropSplitter ... config (LootPostMover)`, `bLootExpirationEnabled(_Psi)`, `iLootExpirationMaxTurns(_Psi)` (2043070900 `XComGameState_LootDropSplitter.uc:12,24-25`); consumed at `:273-281`. The class is live only through a class override of `XComGameState_LootDrop` (`2043070900\Config\XComEngine.ini:5`); no other active mod overrides that class (cfgscan).

Bypass check: only the psi value differs from the mod's defaults (3 and 2). Non-psi loot reads 3 either way.

Evidence:
- Logs: none; the mod's logging is off (`bEnableLogging = false`).
- Tactical save `save_AUTOSAVE- Campaign 35, Mission 8, Turn 9` (`tacloot.py`): the loot-drop state is of class `XComGameState_LootDropSplitter` (override live) with `LootExpirationTurnsRemaining = 3`, dropped by an ADVENT Pathfinder. I did not establish whether that drop counts as psi loot; if it is non-psi, 3 is also the mod default.

Verdict: **UNPROVEN** for the one value this block changes (psi 2 to 3). The class and a 3-turn timer are confirmed live.
Probe (one config line): add `bEnableLogging = true` under `[WOTCLootPostMover.X2DownloadableContentInfo_WOTCLootPostMover]` in jepFixes `XComLootPostMover.ini`; the next psi drop logs `Loot Drop was PsiLoot - Timer set at 3` (2 = FAILING). Alternative: `tacloot.py` on an autosave taken the turn a psi loot drop appears.

---

## 10. Save-file probe (method, so it can be rerun)

- `savescan.py "<save name>" dump` reads a save from `...\XComGame\SaveData\` read-only, walks the UE3 compressed chunks (magic `C1832A9E`, 131072-byte blocks), inflates them with a pure-Python LZO1X decoder (no packages installed) and writes `audit\save_blob.bin` (about 25 MB, scratch). 351 chunks, every block length checked against its header.
- `names.py <regex>` tallies names; `ctx.py <needle>` prints neighbouring strings; `prop.py <Property>` decodes serialized Int/Bool/Name/Array-count values; `tacloot.py <save...>` scans tactical saves for loot timers.
- Limits: a strategy save holds current state plus recent history frames, so it shows what exists now. It cannot show an event that left no state. Property decoding was checked on values with visible answers (array counts that match the listed entries).

---

## Summary

| Block | Verdict | One-line reason | Probe if unproven |
|---|---|---|---|
| Capture risk off (`XComGameBoard.ini`) | HOLDING | Save: 5 live actions with Captured in their template carry Wounded + Ambush only, Captured sits in NegatedRisks; logs: 0 of 326 attached risks is Captured | - |
| Faction orders removed (`XComGameData.ini`) | HOLDING | Save holds 20 card states = 52 vanilla minus 32 removed; continent pool at campaign creation was 17 = merged pool minus removals | - |
| Chosen trait whitelist (`XComGameData.ini`) | HOLDING, with a side effect | All 6 strengths and 6 weaknesses in the save are whitelisted; pool ran dry, Hunter holds a `None` strength, two Chosen started one short. ARFM mutator strengths bypass the list by code (none present yet) | - |
| CI sitrep exclude list (`XComGameData.ini`) | UNPROVEN, leaning holding | 10 mission sitrep arrays, 0 listed names; statistical only. Risk/bonus sitreps on the list arrive by other paths regardless | Rerun the save scan after about 10 more missions |
| Dark-event count (`XComMoreDarkEvent.ini`) | HOLDING (count), LEAK ("never 4") | First roll gave 1 event; the active OddS9 values would give 2+. Chosen Dark Event action adds +1 after the cap, by the mod's code | Third monthly report shows 2 new events |
| Emergency Defense removed (`XComMissionDefs.ini`) | HOLDING | Byte-exact removals; startup dump of all 115 mission types has no EmergencyDefense in 8 logs | - |
| Immolator buildable line (`XComStrategyTuning.ini`) | HOLDING | Logged "Making 156 items buildable" equals the replayed merge only with the removal applied (157 without) | - |
| Living Space (`XComLivingSpace.ini`) | HOLDING | Save: crew limit 50 at start, 70 after upgrade 1 (mod defaults 30 and +10) | - |
| Loot expiry (`XComLootPostMover.ini`) | UNPROVEN (psi value) | Class override live and a 3-turn timer seen, which does not separate 3 from the mod default; no confirmed psi drop | Set `bEnableLogging = true` in the mod's DLCInfo section; next psi drop logs the timer |

Not done: the game was not launched; nothing outside this audit folder was written; the covert spawn list was skipped as instructed; `jepCovertBlock` and `XComIsmsRogue.ini` were not read.

