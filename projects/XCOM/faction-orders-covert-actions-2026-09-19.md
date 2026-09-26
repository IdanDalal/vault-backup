---
type: reference
created: 2026-09-19
author: jep
project: XCOM 2 WotC campaign
status: active
---

# Faction orders, covert actions, campaign preferences (2026-09-19)

Scope: the 1,094 mods marked active in AML `settings.json` (vault copy dated 2026-09-11) plus the base game. Enumerated by script over every Config ini, Localization int and Src uc of those mods. Receipts: workshop ids in brackets, file:line where a claim rests on code.

## Levers (all config, all in jepFixes)

| Target                                                     | File in jepFixes    | Section                                                                               | Line shape                                                                      | Mechanism                                                                                                                                                                                |
| ---------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Faction order (either form: order card or continent bonus) | `XComGameData.ini`  | `[CovertInfiltration.X2Helper_Infiltration_TemplateMod]`                              | `+arrRemoveFactionCard="ResCard_X"`                                             | CI marks the card template `__REMOVED__` (X2Helper_Infiltration_TemplateMod.uc:1361). Expanded Continent Bonuses readme: a card blocked this way also never spawns as a continent bonus. |
| Covert action, random-spawn kind                           | `XComGameBoard.ini` | `[CovertInfiltration.X2EventListener_Infiltration]`                                   | `+CovertActionsPreventRandomSpawn=CovertAction_X`                               | Highlander event `AllowActionToSpawnRandomly` (XComGameState_ResistanceFaction.uc:795), CI answers false for listed names (X2EventListener_Infiltration.uc:535).                         |
| Covert action, chain kind                                  | none found          |                                                                                       |                                                                                 | CI activity chains spawn by work accumulation (XComInfiltration.ini:296-330); no per-chain disable key exists in CI config.                                                              |
| Capture risk                                               | `XComGameBoard.ini` | `[ConfigurablePosthumousRisks.X2DownloadableContentInfo_ConfigurablePosthumousRisks]` | `+ChangeRisk=(RiskName="CovertActionRisk_SoldierCaptured", Behavior=alwaysOff)` | availability function returns false; Highlander never attaches the risk (XComGameState_CovertAction.uc:969). Ambush untouched.                                                           |

Campaign note: card decks are dealt at campaign start. Removal is certain for a new campaign, medium confidence mid-campaign (cards already dealt may persist).

## 1. Faction orders (52 cards, all base game; no active mod adds cards)

Columns: Continent = the card also spawns as a continent bonus (base = vanilla continent card; ECB = made one by Expanded Continent Bonuses [2797864304]). Status = already blocked on this stack.


### Reapers

| Template                     | Order                | Effect                                                                                    | Continent | Status        |
| ---------------------------- | -------------------- | ----------------------------------------------------------------------------------------- | --------- | ------------- |
| `ResCard_BallisticsModeling` | Ballistics Modeling  | The speed of all weapons research is increased by X%.                                     |           |               |
| `ResCard_BetweenTheEyes`     | Between the Eyes     | Any XCOM shot that hits the Lost is an instant headshot kill.                             | ECB       |               |
| `ResCard_GuardianAngels`     | Guardian Angels      | Covert Actions will not be ambushed.                                                      | ECB       | removed by CI |
| `ResCard_HeavyEquipment`     | Heavy Equipment      | Excavation speed increased by X%.                                                         |           |               |
| `ResCard_RunSilentRunDeep`   | Infiltrate           | On timed missions, the timer does not begin until the squad has lost concealment.         | ECB       |               |
| `ResCard_LightningStrike`    | Lightning Strike     | Units gain +X mobility for the first X turns of battle while the squad remains concealed. | ECB       | removed by CI |
| `ResCard_LiveFireTraining`   | Live Fire Training   | Any recruits training in the GTS will achieve the rank of Sergeant.                       | base      |               |
| `ResCard_MunitionsExperts`   | Munitions Experts    | Experimental Ammo projects in the Proving Grounds are completed instantly.                | base      |               |
| `ResCard_PopularSupportI`    | Popular Support I    | Supplies collected from each Supply Drop are increased by X%.                             |           |               |
| `ResCard_PopularSupportII`   | Popular Support II   | Supplies collected from each Supply Drop are increased by X%.                             |           |               |
| `ResCard_RapidCollection`    | Rapid Collection     | Resistance supply drops are collected instantly.                                          | base      |               |
| `ResCard_RecruitingCenters`  | Recruiting Centers   | New recruits cost only X Supplies.                                                        | ECB       |               |
| `ResCard_ResistanceNetwork`  | Resistance Network   | Contact with new regions is made instantly.                                               | base      |               |
| `ResCard_ResistanceRisingI`  | Resistance Rising I  | +1 Resistance Contact.                                                                    |           |               |
| `ResCard_ResistanceRisingII` | Resistance Rising II | +2 Resistance Contacts.                                                                   |           |               |
| `ResCard_Scavengers`         | Scavengers           | All resource rewards from scanned Rumors are doubled.                                     | ECB       |               |
| `ResCard_VolunteerArmy`      | Volunteer Army       | On every mission, there is a chance that a Resistance soldier will join the XCOM squad.   | base      | removed by CI |

### Skirmishers

| Template                      | Order                 | Effect                                                                                         | Continent | Status        |
| ----------------------------- | --------------------- | ---------------------------------------------------------------------------------------------- | --------- | ------------- |
| `ResCard_BombSquad`           | Bomb Squad            | Experimental Grenade and Heavy Weapon projects are completed instantly in the Proving Grounds. | base      |               |
| `ResCard_DecoysAndDeceptions` | Decoys and Deceptions | All knowledge gained by the Chosen is reduced by X%.                                           | ECB       |               |
| `ResCard_DoubleAgent`         | Double Agent          | On every mission, there is a chance that an ADVENT unit will join the XCOM squad.              | base      |               |
| `ResCard_ImpactModeling`      | Impact Modeling       | The speed of all armor research is increased by X%.                                            |           |               |
| `ResCard_InformationWar`      | Information War       | The Tech Defense of all enemies and hack targets is lowered by X.                              | ECB       | removed by CI |
| `ResCard_InsideJobI`          | Inside Job I          | All Intel rewards increased by X%.                                                             |           |               |
| `ResCard_InsideJobII`         | Inside Job II         | All Intel rewards increased by X%.                                                             |           |               |
| `ResCard_InsideKnowledge`     | Inside Knowledge      | The effect of all weapon modifications is increased.                                           | base      |               |
| `ResCard_IntegratedWarfare`   | Integrated Warfare    | All PCS effects are increased.                                                                 | base      |               |
| `ResCard_ModularConstruction` | Modular Construction  | Facility construction speed is increased by X%.                                                |           |               |
| `ResCard_PrivateChannel`      | Private Channel       | All mission timers are increased by X turns.                                                   | ECB       |               |
| `ResCard_QuidProQuo`          | Quid Pro Quo          | All Black Market costs reduced by X%.                                                          | ECB       |               |
| `ResCard_Sabotage`            | Sabotage              | Remove one block of Avatar Progress at the end of every month.                                 | ECB       |               |
| `ResCard_TacticalAnalysis`    | Tactical Analysis     | Enemy units lose one action on their next turn if discovered on the XCOM turn.                 | base      | removed by CI |
| `ResCard_UnderTheTableI`      | Under the Table I     | The Black Market pays a X% Supply Premium for goods.                                           |           |               |
| `ResCard_UnderTheTableII`     | Under the Table II    | The Black Market pays a X% Supply Premium for goods.                                           |           |               |
| `ResCard_Vulture`             | Vulture               | Enemies drop additional loot items.                                                            | ECB       | removed by CI |
| `ResCard_WeakPoints`          | Weak Points           | Any shredding attack from XCOM does an additional +X shred to the target.                      | ECB       |               |

### Templars

| Template                     | Order                | Effect                                                                                   | Continent | Status        |
| ---------------------------- | -------------------- | ---------------------------------------------------------------------------------------- | --------- | ------------- |
| `ResCard_ArtOfWar`           | Art of War           | Ability Points gained by promotion are increased by X%.                                  | ECB       |               |
| `ResCard_BondsOfWar`         | Bonds of War         | Soldier bonds grow X% faster.                                                            | ECB       |               |
| `ResCard_DeeperLearningI`    | Deeper Learning I    | Soldiers' XP gains are increased by X%.                                                  |           |               |
| `ResCard_DeeperLearningII`   | Deeper Learning II   | Soldiers' XP gains are increased by X%.                                                  |           |               |
| `ResCard_Feedback`           | Feedback             | Psionic attacks on XCOM units will cause damage to the caster.                           | ECB       |               |
| `ResCard_GreaterResolve`     | Greater Resolve      | Lightly wounded soldiers can be sent into combat.                                        | base      | removed by CI |
| `ResCard_HiddenReservesI`    | Hidden Reserves I    | Gain an additional +X power on the Avenger.                                              |           |               |
| `ResCard_HiddenReservesII`   | Hidden Reserves II   | Gain an additional +X power on the Avenger.                                              |           |               |
| `ResCard_MachineLearning`    | Machine Learning     | Research breakthroughs are twice as likely to occur.                                     | base      |               |
| `ResCard_MentalFortitude`    | Mental Fortitude     | All battle madness (panic, obsession, berserk, shattered) only lasts one turn.           | base      |               |
| `ResCard_NobleCause`         | Noble Cause          | Will recovery in all soldiers is X% faster.                                              | ECB       |               |
| `ResCard_PursuitOfKnowledge` | Pursuit of Knowledge | Laboratory facilities provide an additional X% boost to research times.                  | base      |               |
| `ResCard_StayWithMe`         | Stay With Me         | Soldiers are much more likely to bleed out rather than die when their health drops to 0. | ECB       |               |
| `ResCard_SuitUp`             | Suit Up              | All armor and vest projects in the Proving Ground are completed instantly.               | base      |               |
| `ResCard_Tithe`              | Tithe                | Resource rewards on all missions are increased by X%.                                    | ECB       |               |
| `ResCard_TrialByFire`        | Trial by Fire        | Double the Ability Points gained in combat.                                              | ECB       |               |
| `ResCard_Vengeance`          | Vengeance            | When a squadmate dies, the entire squad receives random bonuses for two turns.           | ECB       |               |

Counts: 17 Reapers, 18 Skirmishers, 17 Templars. Continent forms: 15 base, 21 ECB. Already removed by CI (7): Lightning Strike, Volunteer Army, Guardian Angels, Vulture, Information War, Tactical Analysis, Greater Resolve (CI XComGameData.ini:4-16). Bonds of War = 25% on every difficulty (base DefaultGameData.ini:4228-4231).

## 2. Covert actions (46 templates that can reach the Covert Actions screen)

Spawn path: random = offered by a faction at random (lever: CI prevent list); chain = spawned by a Covert Infiltration or mod activity chain (no config lever found); story = golden path (keep). Screen name = the narrative ActionName from localization.

| Template                                  | Screen name                          | Source                       | Spawn path  | Status / lever                                                                                |
| ----------------------------------------- | ------------------------------------ | ---------------------------- | ----------- | --------------------------------------------------------------------------------------------- |
| `CovertAction_AlienLoot`                  | Scavenge Alien Loot                  | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_BreakthroughTech`           | Technical Advances                   | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_CancelChosenActivity`       | Counterintelligence                  | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_FacilityLead`               | Facility Lead                        | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_FindFaction`                | Find the Reapers                     | base game                    | story       | keep                                                                                          |
| `CovertAction_FindFarthestFaction`        | Find the (faction), shared narrative | base game                    | story       | keep                                                                                          |
| `CovertAction_FormSoldierBond`            | Teamwork Training                    | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_GatherIntel`                | Intel Collection                     | base game                    | random      | CI: late game, 3 slots, capture+ambush risks (X2Helper_Infiltration_TemplateMod.uc:1252-1275) |
| `CovertAction_GatherSupplies`             | Supply Run                           | base game                    | random      | CI: late game, 3 slots, capture+ambush risks (X2Helper_Infiltration_TemplateMod.uc:1252-1275) |
| `CovertAction_ImproveComInt`              | Tactical Education                   | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_IncreaseIncome`             | Helping Hand                         | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_RecruitEngineer`            | Tech Support                         | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_RecruitExtraFactionSoldier` | A Hero's Welcome, shared narrative   | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_RecruitFactionSoldier`      | A Hero's Welcome                     | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_RecruitScientist`           | Higher Learning                      | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_RemoveDoom`                 | Sabotage                             | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_RescueSoldier`              | Personnel Extraction                 | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_ResistanceCard`             | New Orders                           | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_ResistanceContact`          | Signal Boost                         | base game                    | random      | already blocked by CI                                                                         |
| `CovertAction_RevealChosenMovements`      | Behind Enemy Lines                   | base game                    | story       | keep                                                                                          |
| `CovertAction_RevealChosenStrengths`      | Find the Stronghold                  | base game                    | story       | keep                                                                                          |
| `CovertAction_RevealChosenStronghold`     | Into the Fire                        | base game                    | story       | keep                                                                                          |
| `CovertAction_SharedAbilityPoints`        | Combat Preparedness                  | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_SuperiorPCS`                | Fabricate PCS                        | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_SuperiorWeaponUpgrade`      | Manufacture Upgrade                  | base game                    | random      | CI prevent list                                                                               |
| `CovertAction_RMStartUnlockRegion`        | Contact New Resistance Cell          | Activity Chain Unlock Region | chain (mod) | no config lever                                                                               |
| `CovertAction_AlienCorpses`               | Scavenge Alien Loot                  | Covert Infiltration          | random      | CI prevent list                                                                               |
| `CovertAction_BlackMarket`                | Help the Smugglers                   | Covert Infiltration          | random      | CI prevent list                                                                               |
| `CovertAction_ExhaustiveTraining`         | Inter-Resistance Exercises           | Covert Infiltration          | random      | already blocked by Odd S9                                                                     |
| `CovertAction_ExperimentalItem`           | Our Experiment Now                   | Covert Infiltration          | random      | CI prevent list                                                                               |
| `CovertAction_PatrolWilderness`           | Patrol Wilderness                    | Covert Infiltration          | random      | CI prevent list                                                                               |
| `CovertAction_PrepareCounterDE`           | (counter dark event)                 | Covert Infiltration          | chain (CI)  | no config lever                                                                               |
| `CovertAction_PrepareFacility`            | Identify Avatar Coordinators         | Covert Infiltration          | chain (CI)  | no config lever                                                                               |
| `CovertAction_PrepareFactionJB`           | Consult the Faction                  | Covert Infiltration          | chain (CI)  | no config lever                                                                               |
| `CovertAction_PreparePersonnel`           | Investigate Reports of Treason       | Covert Infiltration          | chain (CI)  | no config lever                                                                               |
| `CovertAction_PrepareUFO`                 | Force the UFO to Ground              | Covert Infiltration          | chain (CI)  | no config lever                                                                               |
| `CovertAction_UtilityItems`               | Factory Reactivation                 | Covert Infiltration          | random      | CI prevent list                                                                               |
| `CovertAction_WeakChosenActivity`         | Expose Weakness                      | Expose Chosen Weakness       | random      | CI prevent list                                                                               |
| `CovertAction_MOCXAssault`                | Prepare Attack on MOCX HQ            | MOCX Initiative              | chain (mod) | no config lever                                                                               |
| `CovertAction_MOCXCancelProject`          | Stop MOCX Project                    | MOCX Initiative              | chain (mod) | no config lever                                                                               |
| `CovertAction_MOCXOffsite`                | Recon Offsite Facility               | MOCX Initiative              | chain (mod) | no config lever                                                                               |
| `CovertAction_MOCXTraining`               | Recon Training Exercise              | MOCX Initiative              | chain (mod) | no config lever                                                                               |
| `CovertAction_GatherMELD`                 | Meld Collection                      | Psionics Ex Machina          | random      | CI prevent list                                                                               |
| `CovertAction_IRI_Nuke`                   | Refined Elerium                      | Rocket Launchers             | random      | already blocked by Odd S9                                                                     |
| `TRCovertAction_HeistSpark`               | SPARK Heist                          | Steal Spark                  | chain (mod) | no config lever                                                                               |
| `TRCovertAction_InvestigateSpark`         | Investigate ADVENT's SPARK           | Steal Spark                  | chain (mod) | no config lever                                                                               |

Counts: 42 static templates + 4 CI chain templates built at runtime (X2StrategyElement_DefaultActivities.uc:805) + PrepareCounterDE. CI infiltration missions (Hack ADVENT Datavault, Rescue Resistance Informant, Distract ADVENT Garrison, Sabotage ADVENT Infrastructure, Rescue XCOM Personnel, Capture ADVENT Collaborator) are chain missions, not covert actions, and have no disable key either. "Recover corpses" = `CovertAction_AlienCorpses`, screen name Scavenge Alien Loot, Covert Infiltration's replacement for the base `CovertAction_AlienLoot` (which CI already blocks).

## 3. Idi's campaign preferences (his words, 2026-09-19 captures)

### Second Wave, the only ones he activates (8 of 8 verified present on the stack)

| # | Option | ID | Provided by | Text in game |
|---|---|---|---|---|
| 1 | Beta Strike | `BetaStrike` | base (DefaultUI.ini:240) | Greatly increase HP of most units for longer tactical engagements |
| 2 | Skirmisher Ally | `SkirmisherStart` | base (DefaultUI.ini:242) | Start at Skirmisher HQ |
| 3 | Lengthy Scheme | `ExtendedAvatarProject` | base (DefaultUI.ini:245) | Double the length of the Avatar Project |
| 4 | Not Created Equal | `PBNCE` | Point-Based Not Created Equal [1144463583] | Randomize base stats for all soldiers, balanced around a point pool |
| 5 | Macrophagial Transgenesis | `GM_SWO_MutagenicGrowth` | Gene Modding [1877861493] | Soldiers can be Gene Modded even while wounded |
| 6 | Scamper Exhaustion | `ARFMNoPostScamperReactions` | A Harder War: Absurd Aliens [2867288932] | Supremacy and Dominance reaction mechanics disabled for one turn after scampering |
| 7 | Impermanent Injury | `ARFMRequiemTraits` | A Requiem For Man: Dark Events [2795578857] | Wound and Requiem traits can be removed in the Infirmary |
| 8 | Busy Skies | `CI_NoUfoGate` | Covert Infiltration [2567230730] | UFO raid chains can appear before an Avenger-hunting UFO is encountered |
| 9 | Embraced Endings | `ARFMRequiemBeginning` | A Requiem For Man: Dark Events [2795578857] | Enable special Trait mechanics (added on his word 2026-09-19; section 4) |

Everything else stays off. Second Wave picks are a checkbox screen at campaign start, outside config; WOTC Second Wave Defaults [3740606425] saves the ticked set to the user config (Documents), so ticking the nine once and pressing its Save Defaults button makes them the default. WOTC Second Wave Defaults [3740606425] is on the stack and can store this set as the default selection.

### Continent bonuses, all disabled except these 6 (6 of 6 verified in the pool)

| # | Bonus | Template | Pool membership |
|---|---|---|---|
| 1 | Between the Eyes | `ResCard_BetweenTheEyes` | ECB |
| 2 | Resistance Network | `ResCard_ResistanceNetwork` | base |
| 3 | Integrated Warfare | `ResCard_IntegratedWarfare` | base |
| 4 | Inside Knowledge | `ResCard_InsideKnowledge` | base |
| 5 | Trial By Fire | `ResCard_TrialByFire` | ECB |
| 6 | Machine Learning | `ResCard_MachineLearning` | base |

Reason, his words: "so that the options are constant, and I only ever get these, instead of drawing randomly from a pool." Pool on this stack: 15 base + 21 ECB, minus 7 CI-removed = 29 possible; he keeps 6. Mechanism: Modify Continent Bonus WOTC [1145436332] in-game checkbox screen (UIOptions_ContinentBonus.uc); its saved state lives in the user config, outside this vault.

## 4. Embraced Endings, exactly what it does

Source: A Requiem For Man: Dark Events [2795578857]. Second Wave ID `ARFMRequiemBeginning` (X2DownloadableContentInfo_ARFMDarkEvents.uc:1208). In-game text (ARFMDarkEvents.int:14-15): "Enable special Trait mechanics. All Trait mechanics are modified and unique Trait mechanics are enabled."

The ID is checked in exactly three places in the mod's source (grep over all .uc, .ini, .int of the mod). Nothing else reads it. Off means none of the three fire.

| # | Gate | File:line | What the option unlocks |
|---|---|---|---|
| 1 | `ProcessRequiemTraits` | ARFM_Traits_GameplayMutators.uc:905 | Wound traits acquired in combat. Trigger: an XCOM unit with the Will system takes damage, cumulative damage from that enemy's character group reaches 70% of max HP (`AcquireRequiemWoundDamageThreshold=0.7`, XComARFM_DETA_Config.ini:2), current Will is below half of max, and a 1-in-12 roll picks the family. Damage that is not melee, explosion or ADVENT mag projectile rolls the psionic families (Knock, Moth, Sky, Soul, Resonance/PsiWeak, Blood); damage that is not psi or mental rolls the bodily families (Decrepitude, Decay/Wither, Splintering, Heart, Dawn, Winter). Each family: Wound I, Wound II, then a Requiem "Scar" (36 trait templates, file lines 6-46). |
| 2 | `CanActivateLastingTrauma` | ARFM_DE_DarkEvents.uc:2911-2916 | The dark event Lasting Trauma can activate at all (also needs force level 6+ and `CANACTIVATE_REQUIEMDARKEVENT_LASTINGTRAUMA=true`, XComARFM_DE_Config.ini:174). On activation every injured or shaken crew member rolls 1-in-13 per family for a permanent Requiem Scar (ARFM_DE_DarkEvents.uc:1418-1490). In-game text: "All Injured or Shaken Soldiers will Acquire a Requiem. A Permanent, Unremovable, Harmful Trait." |
| 3 | `ARFM_DE_Condition_LWOTC` | ARFM_DE_Condition_LWOTC.uc:7 | Shooter condition on the 26 trait abilities in ARFM_TA_Abilities.uc (ScarBlood, SoulHack, MothLight, SkyEyes, KnockNullLance, ScarDawnReckoning, WinterExtender and the rest). With the option off the abilities never validate, so a trait that somehow exists does nothing. |

Not modified by the option: vanilla traits (Fear of X, Obsessive Reloader and the rest). The word "modified" in the tooltip has no code behind it; the mod adds, it does not alter vanilla trait acquisition. Related switch: `ARFMDETA_HARD_DISABLE_REQUIEMTRAITS=false` (XComARFM_DETA_Config.ini:5) hard-disables the same system regardless of the option. Related option: Impermanent Injury (`ARFMRequiemTraits`, on Idi's list) makes Wound and Requiem traits removable in the Infirmary; with Embraced Endings off there is nothing for it to remove, so it is inert until he turns Embraced Endings on.

Confidence: high on the three gates and their effects (read in source). Medium on the exact accounting inside the 70% damage helper (`HasUnitTakenThresholdDamageFromCharacterGroup` lives in the base game, not on disk; vanilla uses it for fear traits and sums damage from that enemy group within the mission).

## Sources

- Covert Infiltration [2567230730]: Config/XComGameData.ini, Config/XComGameBoard.ini, Src/CovertInfiltration/Classes/X2Helper_Infiltration_TemplateMod.uc, X2EventListener_Infiltration.uc, X2StrategyElement_DefaultActivities.uc
- X2WOTCCommunityHighlander [1796402257]: Src/XComGame/Classes/XComGameState_CovertAction.uc, XComGameState_ResistanceFaction.uc
- Configurable Posthumous Risks [2823200756]: Config/XComGameBoard.ini, Src/.../X2DownloadableContentInfo_ConfigurablePosthumousRisks.uc
- Expanded Continent Bonuses [2797864304]: Config/XComGameData.ini, ReadMe.txt
- A Requiem For Man: Dark Events [2795578857]: files cited inline
- Base game: XComGame/Config/DefaultGameData.ini, DefaultUI.ini, Localization/INT/XComGame.int
- Active mod list: `projects/XCOM/XCOM2 AML 1.6.0-beta/settings.json` (1,094 active; the 09-14 inventory counted 1,111, a later snapshot)

## 5. Applied 2026-09-19 (jepFixes, on his word)

- `jepFixes/Config/XComGameBoard.ini`: capture risk alwaysOff; 9 names on the prevent list = his 8 covert actions (Scavenge Alien Loot covers both `CovertAction_AlienLoot` and `CovertAction_AlienCorpses`).
- `jepFixes/Config/XComGameData.ini`: 31 of his 37 orders on `arrRemoveFactionCard` (the 7 CI already lists restated on his word).
- Held, 6 of 37, ruled A by Idi 2026-09-19 (keep out of the removal list, they survive only as his continent bonuses): Between the Eyes, Resistance Network, Integrated Warfare, Inside Knowledge, Trial by Fire, Machine Learning. Same six he keeps as continent bonuses; this lever deletes both forms. Continent-flagged cards stay out of faction decks anyway (Expanded Continent Bonuses readme; medium confidence, deck code is in the base game, not on disk).
- Installed copy at `XComGame\Mods\jepFixes\Config` byte-identical to the vault copy (diff -rq, 2026-09-19 16:16). In-game check pending: no Soldier Captured risk, none of the 8 actions, none of the 31 orders.
