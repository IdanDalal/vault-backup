---
type: report
created: 2026-09-26
author: jep
---
# XCOM seven asks, 2026-09-26

Idi's seven items (Chosen traits whitelist, ambush rescue mission, parry, tongue grab, covert capture slot, Chosen intro, reveal text). Live mod: `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\jepFixes`, mirrored in `projects/XCOM/jepFixes/`.

## Status

| # | Ask | Status | Lever |
|---|---|---|---|
| 1 | Chosen trait whitelist | INSTALLED 09-26 (13 S / 10 W kept) | jepFixes `XComGameData.ini` reset + whitelist; Chosen Rechosen for traits already rolled |
| 2 | Never spawn the ambush rescue | INSTALLED | jepFixes `XComMissionDefs.ini`, 3 byte-exact removals |
| 3 | Parry with no focus | WORKING AS DESIGNED | Parry costs Momentum, never Focus |
| 4 | No tongue grab from full cover | BUILT + INSTALLED 09-26 (ruling A) | own script mod `jepNoCoverGrabs` |
| 5 | Capture slot on covert actions | NO LEVER, harmless, ages out | none (UnrealScript code) |
| 6 | Assassin intro skipped | NO LEVER, vanilla skip gates | none |
| 7 | Reveal screen text wraps | INSTALLED | jepFixes `XComGame.ini` `bWordWrapDesc=false` |

## 1. Chosen trait whitelist

- Pool today: 32 strengths, 13 weaknesses, after all active mods (Odd S9 removed Kinetic Plating, added 5 stat traits and Achilles; Restored Chosen Traits, A Better Chosen, Pathfinders, Frost Legion add the rest). Computed by script from vanilla `DefaultGameData.ini:3494-3560` plus every active mod's `[XComGame.XComGameState_AdventChosen]` lines.
- Install: jepFixes loads last (proved 09-14), so `!ChosenStrengths=()` and `!ChosenWeaknesses=()` wipe every mod's list, then `+` lines add back only his picks.
- Reach: the pool feeds every future roll (level-ups, 1 strength per level, 4 levels; favored Chosen +2 strengths, +1 weakness). All three Chosen rolled their starting traits at campaign start; the pool change does not touch those.
- Traits already rolled: Chosen Rechosen (3775981048, active since 08-30). Geoscape, Chosen icon left of the doom timer, green EDIT button: Erase, Add, Seal per Chosen. Legend default = intel cost, Erase 1 use per Chosen. jep's proposal: set `bFreeUses=true` and `bUnlimitedUses=true` in jepFixes so he can bring all three Chosen onto the whitelist once, free. Source: `3775981048/Src/.../CRSJ_UIChosenTraitInterference.uc:27,687,705`.
- Sizing: keep at least 9 strengths and 3 weaknesses (3 start + 4 level-ups + 2 favored = 9). Below that a Chosen may end up with fewer traits than the rules call for. Medium confidence: vanilla roll code is not on disk.
- Traits added by code (outside config) cannot be seen by this scan. Rechosen's Add list shows the full live pool; check it after install.
- Frost Legion traits (S30-S32) require Frost Legion units; Adversary weaknesses (W3-W5) name a faction.
- Exact effect of each Odd S9 stat trait (numbers) not read yet.

Mark each row keep or strike.

**Ruled 09-26 (Idi):** strike S2, S4-S7, S9-S11, S18-S23, S26-S28, S31-S32 / W10-W12. Kept S1 S3 S8 S12-S17 S24 S25 S29 S30 / W1-W9 W13. Written to jepFixes `XComGameData.ini` (appended block, `!` reset then 23 `+` lines, LF endings like the rest of the file; prior content byte-identical, backup `XComGameData.ini.bak-0926` in the job tmp). Rechosen costs left at default (no ruling on free edits). Probe: Rechosen Add list offers only the kept names.

### Strengths (32)

| # | In game | What it does | From |
|---|---|---|---|
| S1 | Revenge (`ChosenRevenge`) | Chance to return fire against missed shots. | vanilla |
| S2 | All Seeing (`ChosenAllSeeing`) | Reveals concealed units. | vanilla |
| S3 | Watchful (`ChosenWatchful`) | Can enter Overwatch upon ending their turn. | vanilla |
| S4 | Brutal (`ChosenBrutal`) | Attacks decrease the Will of any soldiers within sight. | vanilla |
| S5 | Blast Shield (`BlastShield`) | Immune to Explosions. | vanilla |
| S6 | Immune to Melee (`ChosenImmuneMelee`) | Immune to Melee Damage. | vanilla |
| S7 | Shadowstep (`ChosenShadowstep`) | This Chosen does not trigger overwatch or reaction fire. | vanilla |
| S8 | Low Profile (`ChosenLowProfile`) | Defense increased after the first attack of every turn. | vanilla |
| S9 | Planewalker (`ChosenDamagedTeleport`) | Chosen will teleport after taking damage. | vanilla |
| S10 | Regeneration (`ChosenRegenerate`) | Regenerates lost health. | vanilla |
| S11 | Soulstealer (`ChosenSoulstealer`) | Gains health when nearby enemies take damage. | vanilla |
| S12 | Beastmaster (`Beastmaster`) | Can summon savage allies. | vanilla |
| S13 | Prelate (`Prelate`) | Can summon ADVENT Priests. | vanilla |
| S14 | Mechlord (`Mechlord`) | Can summon robotic allies. | vanilla |
| S15 | General (`General`) | Can summon ADVENT Troopers. | vanilla |
| S16 | Shogun (`Shogun`) | Can summon ADVENT Stun Lancers. | vanilla |
| S17 | Mark (`ChosenHoloTargeting`) | Attacks can mark their target, reducing defense. | Restored Chosen Traits |
| S18 | Beyond Earth (`ChosenImmuneEnvironmental`) | Immune to Environmental Damage. | Restored Chosen Traits |
| S19 | Mentally Sound (`ChosenImmunePsi`) | Immune to Psionic Damage. | Restored Chosen Traits |
| S20 | Agile (`ChosenAgile`) | Can move to new cover after being attacked. | Restored Chosen Traits |
| S21 | Bloodlust (`TraitBloodlust`) | This Chosen shoots to kill. No automatic bleedout. | A Better Chosen |
| S22 | Resilience (`TraitResilience`) | This Chosen is near immune to critical strikes. | A Better Chosen |
| S23 | Evasive (`TraitEvasive`) | This Chosen has a significant bonus to Dodge. | A Better Chosen |
| S24 | Precise (`ChosenIncreaseCrit`) | Increased Critical Hit chance. | Odd S9 |
| S25 | Fast (`ChosenIncreaseMobility`) | Increased Mobility. | Odd S9 |
| S26 | Armored (`ChosenIncreaseArmor`) | Increased Armor. | Odd S9 |
| S27 | Strong (`ChosenIncreaseHP`) | Increased HP (the mod's own text wrongly says crit chance) | Odd S9 |
| S28 | Bullet Time (`ChosenIncreaseDodge`) | Increased Dodge chance. | Odd S9 |
| S29 | Pack Hunter (`PackHunter`) | Can summon hunting allies. | [WoTC] Pathfinders |
| S30 | Frost Legion Director (`ChosenSummonFrostLegion`) | Chosen can summon Frost Legion troops. | Frost Legion |
| S31 | Ice Shielded (`MZ_FDChosenIceShield`) | Immunity to Cold. Ice Shields reduce damage by 50% while they hold. Vulnerable to Fire or Psionic damage. | Frost Legion |
| S32 | Icy Demeanor (`ChosenFrostPersonality`) | Chosen attacks inflict bitterfrost. | Frost Legion |

### Weaknesses (13)

| # | In game | What it does | From |
|---|---|---|---|
| W1 | Brittle (`ChosenBrittle`) | Takes increased damage from close range attacks. | vanilla |
| W2 | Shell-shocked (`ChosenWeakExplosion`) | This Chosen takes increased damage from explosions. | vanilla |
| W3 | Adversary: Reapers (`ChosenReaperAdversary`) | Takes increased damage from Reapers. | vanilla |
| W4 | Adversary: Templars (`ChosenTemplarAdversary`) | Takes increased damage from Templars. | vanilla |
| W5 | Adversary: Skirmishers (`ChosenSkirmisherAdversary`) | Takes increased damage from Skirmishers. | vanilla |
| W6 | Groundling (`ChosenGroundling`) | Easy to target from high ground. | vanilla |
| W7 | Bewildered (`ChosenBewildered`) | Takes additional damage from 3+ attacks in a single turn. | vanilla |
| W8 | Environment Sensitive (`ChosenWeakEnviro`) | Takes increased damage from hazardous effects such as fire, poison, and acid. | Restored Chosen Traits |
| W9 | Vulnerable: Psionics (`ChosenWeakPsi`) | Takes increased damage from Psionic attacks. | Restored Chosen Traits |
| W10 | Oblivious (`ChosenOblivious`) | Takes increased damage from concealed attacks. | Restored Chosen Traits |
| W11 | Impatient (`ChosenImpatient`) | Takes increased damage from overwatch attacks. | Restored Chosen Traits |
| W12 | Nearsighted (`ChosenNearsighted`) | Takes increased damage from squadsight attacks. | Restored Chosen Traits |
| W13 | Achilles (`ChosenAchilles`) | Takes increased damage from attacks with high chance to hit. | Odd S9 |

## 2. Ambush rescue: INSTALLED

- Mission = "Emergency Defense" (display "Recover <Faction>-Affiliated Operative") from Additional Mission Types Redux 1133287457. Three types: `EmergencyDefense_Reapers`, `_Templars`, `_Skirmishers` (`Config/XComMissionDefs.ini:65,94,123`). Hold time 4 on Legend (`XComMissions.ini [EmergencyDefense] DurationOfAssault_Legend=4`). Bradford line = vanilla swarm-ambush VO reused (`X2MissionNarrative_AMT.uc:140`). High.
- Entry path: it sits in the vanilla Extract family, so Covert Infiltration's Personnel Rescue and Informant activities roll it by chance. His 09-24 session played `EmergencyDefense_Reapers` (Idi's `Launch-backup-2026.09.25-16.50.45.log:323347`).
- Written: `jepFixes/Config/XComMissionDefs.ini`, three `-arrMissions` blocks copied byte for byte from the source (script check: 3 of 3 match). Extract family keeps vanilla ExtractVIP and Even More Robots' MRExtract, so no deck goes empty. High.
- SO Bridge 2371821987 only blacklists two sitreps on these types; nothing else calls them. High.
- Risk: an Emergency Defense mission already sitting on the map would break on launch. None rolled in the 09-25 session log. Medium (the save itself was not read).
- Probe, next launch: `Launch.log` loses the three `BeneathSuspicionMission: Current mission sType is  EmergencyDefense_*` lines. If they stay, the removal did not match.

## 3. Parry with no Focus: working as designed

- Parry never costs Focus, in vanilla or in any active mod. It costs 1 action point of the Momentum type, which Rend grants. Deflect and Reflect read the Focus level but never spend it. High (Highlander source `X2Ability_TemplarAbilitySet.uc:554-590,779,804-806`).
- Stronger Templar Parry 1746871334 changes only the result: grazes get parried, parries stack, a primed Parry stops Deflect/Reflect from rolling. No cost change. High.
- Other free Parry sources: any Momentum point pays for it. Mitzruti, Immolator, Hare Wacky Skills and AWC Cost Fix grant Momentum; the Amalgamation Psi-Blades spec gives Parry plus Momentum to non-Templars. Medium.
- Config lever: only Ability Editor could add a Focus cost, and it wipes the Momentum cost first, so Parry would then fire on a normal action. jep recommends no change.

## 4. Tongue grab through full cover: no config lever

- Subject Gamma = the vanilla Alien Hunters Viper King. High.
- Both grabs (`KingGetOverHere`, regular `GetOverHere`) roll plain aim with a visibility check only. Firaxis wrote "not in high cover" in a comment and never coded it (`X2Ability_Viper.uc:802-805`). The Viper King's Bind does block full cover (`X2Ability_DLC_Day60ViperKing.uc:181-186`). High.
- Numbers: Viper King aim 75 on every difficulty, about 35% per grab against full cover before height and other modifiers. Rulers act several times per turn, so over a turn it lands often.
- No active or subscribed mod blocks it. High for this install; the Workshop at large was not searched.
- Config reaches only cooldown and range (`KING_GET_OVER_HERE_*`, cooldown 4): fewer grabs overall, cover or not.
- Real fix = a small script mod that copies Bind's full-cover condition onto both grabs. Needs the XCOM 2 WOTC SDK (not installed; free on Steam, no signup wall).
- Idi's find, 09-26: No Full Cover Grabs 880396912 (RealityMachina, 2017-03-09, base XCOM 2). Does exactly this for unflanked full cover, Low Profile included. Steam page: "removed from the community because it violates Steam Community & Content Guidelines" plus "incompatible with XCOM 2" banner; pre-WOTC build; description names the Viper grab only, so the Viper King's separate `KingGetOverHere` is likely untouched (medium, source unread); comments 2020-2024 report it misses mod Viper variants, one WOTC vanilla-Viper success (2020). Not on disk.

### 4b. jepNoCoverGrabs (ruling A, built 09-26)

- What: at template load, adds the Viper King Bind's rule (`X2Condition_Visibility`, `bRequireNotMatchCoverType=true`, `TargetCover=CT_Standing`) to every grab in `Config/XComjepNoCoverGrabs.ini`. Cover is judged from the Viper's position, so a flanked target stays grabbable (same behavior as No Full Cover Grabs 880396912). Medium-high: the check itself is native code.
- Patched: `GetOverHere` (Viper), `KingGetOverHere` (Subject Gamma), `BoaGetOverHere`, `PrimeGetOverHere` (A Better ADVENT), `GetOverHereElite` (Alien Elite Pack).
- Not patched on purpose: player pulls (Skirmisher Justice, Denmother, perk packs) and non-Viper enemy pulls (Advent Commandos `DestroyerPull`, AHW `AHWMagnaPull`). The mod logs every unpatched ability that carries the grab effect.
- Build: WOTC SDK `XComGame.com make -nopause -mods jepNoCoverGrabs <staging>`: 0 errors, `jepNoCoverGrabs.u` 7,964 bytes. Gotchas found: `SrcOrig` copied to `Src` must be backdated (else the base packages rebuild); the staging path needs no spaces; the mod needs `XComEditor.ini +ModPackages` and `XComEngine.ini +NonNativePackages` or `-mods` silently compiles nothing.
- Installed: `...\XComGame\Mods\jepNoCoverGrabs` (Config, Script, Src, .XComMod). AML `settings.json` entry added, active (backup `settings.json.bak-0926` in the job tmp; diff = only the new entry). Source mirror + `build.sh`: `projects/XCOM/jepNoCoverGrabs/`.
- Probe, next launch, in `Launch.log`: five lines `jepNoCoverGrabs: patched: <name> templates N`, zero `not found:`, plus a list of `unpatched GetOverHere-effect ability:` names. In game: a unit in full cover (unflanked) shows no grab target line to the Viper. Removal is safe any time (template patch only, nothing saved).

## 5. Capture-removal slot: no lever, harmless

- Owner correction: the capture-off line in jepFixes `XComGameBoard.ini` works through Configurable Posthumous Risks 2823200756, not Covert Infiltration. High.
- Each paid "reduce risk" slot targets one risk, fixed when the action spawns. Actions spawned before 09-19 still carry a slot aimed at the (now dead) capture risk. Vanilla hides that slot; Covert Infiltration's squad-select screen draws every slot anyway. Medium-high.
- Effect: paying does nothing. Actions created after 09-19 never roll the capture risk, so the button disappears as the old actions are used up.
- Config lever: none. `OptionalCosts` is UnrealScript, not config. The only related key, `ReduceRiskRewardName`, would also break the ambush and wounded slots. High.

## 6. Assassin intro skipped: no lever

- The teleport-in and the freeze-frame are one cutscene (`X2Action_RevealAIBegin`); the radio line runs on a separate path, so it plays even when the cutscene is skipped. High.
- Base game skips the cutscene when: she spawned from a cinematic spawn; she is immobilized; she was revealed in the same chain as a reinforcement drop (mod reinforcements count); or a never-before-seen enemy type revealed in her group takes the camera. The last one fits "sometimes yes, sometimes no": after that enemy type is seen once, later reveals play. Medium on code (Highlander source `X2Action_RevealAIBegin.uc:50-66,404-477`), low on which gate fired, since this path writes nothing to the log.
- Ruled out: Chosen Traits UI Redux, Manual Reveal+, Drone Reveal, A Better Chosen, Covert Infiltration, Commander HUD, Enhanced action camera.
- Weak suspect: Speed Up Aliens Turn 3594012056 (auto 2x speed on the alien turn, no source shipped). Test: CapsLock toggles it off before a Chosen turn. Low.

## 7. Reveal screen wraps: INSTALLED

- Cause: Chosen Traits UI Redux 3775978160, added 2026-08-30 with Chosen Rechosen. It replaces the vanilla 6+3 cards with scrollable, word-wrapped lists. High.
- Written: `jepFixes/Config/XComGame.ini`, `[WOTCChosenTraitsUIRedux.CTURSJ_Watcher_UIChosenReveal] bWordWrapDesc=false`. Effect: one line per trait, long text slides sideways by itself. The list still scrolls if traits outnumber the panel. Font size has no config lever. Medium.
- Probe: tactical, click the Chosen icon in the Commander HUD; it opens the same screen on demand.
- Full revert to vanilla cards: disable 3775978160 (author: safe to remove any time). Cost: vanilla cards cap at 6 strengths and 3 weaknesses, so a leveled Chosen hides traits.
