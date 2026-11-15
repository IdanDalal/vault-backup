---
type: report
created: 2026-11-15
author: Agent sitreps-fix
---
# Sitrep rulings of 2026-11-15: ARFM dark events, Opportune Moment

Short paths:
- `JEP` = `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\jepFixes\Config`
- `WS` = `C:\Program Files (x86)\Steam\steamapps\workshop\content\268500`
- `ARFM` = `WS\2795578857`, `CI` = `WS\2567230730`, `MSR` = `WS\3739636065` (Multiple Sitreps REDUX), `MMS` = `WS\1365805339` (More Mission SITREPs, active), `ODD` = `WS\3314720537` (Odd S9 Tweaks), `CHL` = `WS\1796402257\Src\XComGame\Classes`
- `DE.uc` = `ARFM\Src\ARFMDarkEvents\Classes\ARFM_DE_DarkEvents.uc`
- Scratch scripts: `C:\Users\jep\.claude\jobs\0815ca4d\tmp\audit\sr\` (`de.py`, `omscan.py`, `mk_arfm.py`, `replay_arfm.py`, `hdr.py`)

## Bottom line

1. Ruling 1: APPLIED. One new file, `JEP\XComARFM_DE_Config.ini`, switches off Medical Embargo, Extra Ammo I, Fortress and Immortal Pursuit with ARFM's own per-event switch. Extra Ammo II (Hair Trigger) has no switch and dies with Extra Ammo I. Templates stay. None of the five is active or pending in the newest strategy save. Proof is on paper (source, merge replay, save); the game was not launched.
2. Ruling 2: NOTHING CHANGED. Opportune Moment 1 and 2 are ordinary strategy sitreps, so the random rollers can draw them. The Multiple Sitreps block entry is the only thing that keeps them bonus-only. The over-infiltration bonus is already wired and live, and neither block list touches it.

## Ruling 1: the five ARFM dark events

### a. Is there a switch that keeps the dark event and stops the sitrep? No.

- The sitrep is added by a bare `BattleData.ActiveSitReps.AddItem(...)` in each event's tactical-start function: `DE.uc:1827` MedicalEmbargo, `:1993` HairTrigger, `:2044` ExtraAmmo, `:2234` Fortress, `:2348` ImmortalPursuit. The only conditions around it are a tag lookup and, for Fortress and Immortal Pursuit, a mission-type switch (`:2213-2228`, `:2323-2342`). No config value is read.
- For four of the five the sitrep is the event's whole tactical effect (the function does nothing else). Medical Embargo also bans 17 heal abilities directly (`DE.uc:1788-1822`).
- ARFM has no mod-menu page: 0 hits for `MCM`, `ModConfigMenu`, `SaveConfig` in `ARFM\Src`. No `XComARFM*.ini` exists in Idi's Documents `Config` folder.
- The only other lever, deleting the five sitrep templates, would leave the dark events in the pool as duds that still take a monthly slot, and Medical Embargo would keep its heal ban. Rejected.

### b. The lever: ARFM's `CANACTIVATE_REQUIEMDARKEVENT_*` switches

- Declared `var config bool CANACTIVATE_REQUIEMDARKEVENT_MEDICALEMBARGO / _EXTRAAMMO / _FORTRESS / _IMMORTALPURSUIT` (`DE.uc:25, 28, 32, 34`), class `ARFM_DE_DarkEvents ... config(ARFM_DE_Config)` (`DE.uc:1`), no variable-level config name. File `XComARFM_DE_Config.ini`, section `[ARFMDarkEvents.ARFM_DE_DarkEvents]`. ARFM's own comment: "Change This Setting to false to disable Dark Events that you simply don't want in your campaign" (`ARFM\Config\XComARFM_DE_Config.ini:136`).
- Precedent in this install: `ODD\Config\XComARFM_DE_Config.ini:3-13` already switches off Betrayal, Blood Tide, Immortal Pursuit, Waves and Transcendence with the same `-...=true` / `+...=false` pair.
- Wiring per event:

| Dark event | Sitrep | CanActivateFn | Switch |
|---|---|---|---|
| ARFMDE_MedicalEmbargo | MedicalEmbargo | `DE.uc:3042-3045`, switch only | MEDICALEMBARGO |
| ARFMDE_ExtraAmmoI | ExtraAmmo | `:3111-3114`, switch only | EXTRAAMMO |
| ARFMDE_ExtraAmmoII | HairTrigger | `:2967-2988`, true only while ExtraAmmoI is in `ActiveDarkEvents` | none; dies with ExtraAmmoI |
| ARFMDE_Fortress | Fortress | `:3133-3136`, month 2+, force level 10+, switch | FORTRESS |
| ARFMDE_ImmortalPursuit | ImmortalPursuit | `:3143-3146`, month 2+, 2+ Chosen met, force level 6+, switch | IMMORTALPURSUIT (already false via Odd S9) |

### Why it is safe for objects already in the save

1. Nothing is deleted. The five templates still exist, so the five state objects created on 2026-11-08 keep resolving `GetMyTemplate()` (`CHL\XComGameState_DarkEvent.uc:60-67`).
2. The switch is not stored in the save. `ConfigCanActivate*()` reads `default.CANACTIVATE_...` (`DE.uc:3263-3391`), which is the class default loaded from ini at game start.
3. Monthly draw: `ChooseDarkEvents` (`CHL\XComGameState_HeadquartersAlien.uc:1663-1723`) draws only from `BuildDarkEventDeck()` (`:1836-1875`), which walks every dark-event object in the history and keeps one only if `DarkEventState.CanActivate()` is true (`:1850`). `CanActivate()` calls the template's `CanActivateFn` (`CHL\XComGameState_DarkEvent.uc:253-270`). A false switch means zero cards for that object, whatever its saved weight.
4. Chosen dark event: the Chosen action only sets `bAddChosenActionDarkEvent` (`CHL\X2StrategyElement_XpackChosenActions.uc:380-381`); the next `ChooseDarkEvents` tags the first card from the same deck (`:1686-1710`). Same filter.
5. Tactical side: only events in `AlienHQ.ActiveDarkEvents` run their tactical-start function (`CHL\X2TacticalGameRuleset.uc:2932-2941`). An event that can never be drawn never gets there.
6. Other ways into `ActiveDarkEvents` or `ChosenDarkEvents` in active mods (grep of every `.AddItem` on those arrays across `WS`): MOCX adds its own project event and four named vanilla events (`WS\1129661000\...\X2StrategyElement_MOCXMissionSources.uc:133-178`); ARFM's Requiem Dawn option adds 21 named events at campaign start, none of the five (`ARFM\...\X2DownloadableContentInfo_ARFMDarkEvents.uc:1546-1575`); ARFM's Perilous Yearning listener draws from the same filtered deck (`ARFM_Listener_PerilousYearning.uc:1593-1608`). The five names appear nowhere else in any mod's code or config (LWOTC rows in `ARFM\Config\XComLW_Overhaul.ini:8-12` aside; LWOTC is not installed).
7. Limit of the lever: an event already pending or active would still run, because activation checks `CanComplete()` (`:1952`), which ARFM leaves unset. The save shows this case does not exist (next block).

### Save check (newest strategy save)

- Save: `save_Operation Pillaging Pyre`, written 2026-11-14 19:14, header "Geoscape", game date 4/17/2035. (`hdr.py`; the 19:15 file of the same name with `_1` is the tactical start one minute later.)
- `python sr\de.py`: 134 dark-event objects. AlienHQ `ChosenDarkEvents` count 2 = `DarkEvent_LightningReflexes` (id 1550, ends 5/14/2035) and `DarkEvent_RapidResponse` (id 1580, hidden, ends 5/5/2035). `ActiveDarkEvents` not serialized = empty.
- The five: `ARFMDE_MedicalEmbargo` id 1647, `ARFMDE_ExtraAmmoII` 1652, `ARFMDE_ExtraAmmoI` 1653, `ARFMDE_Fortress` 1658, `ARFMDE_ImmortalPursuit` 1660. Each has Weight 5 (the starting weight) and no `TimesPlayed`, no `TimesSucceeded`. Never drawn, never active, not pending.
- Only three objects in the whole save have ever been drawn: SupremeArmor, LightningReflexes, RapidResponse.
- Second Wave list in the same save: BetaStrike, SkirmisherStart, ExtendedAvatarProject, PBNCE, GM_SWO_MutagenicGrowth, ARFMNoPostScamperReactions, ARFMRequiemBeginning, ARFMRequiemTraits, CI_NoUfoGate. `ARFMPerilousYearning` is off, which also closes path F of the 11-12 audit (Ambush on Covert Escape, Fortress on Chosen Strongholds).

### c. What was written

New file `JEP\XComARFM_DE_Config.ini`, 1192 bytes, CRLF (same as ARFM's file), ASCII, built by `sr\mk_arfm.py`:

```
; jepFixes 2026-11-15 (Idi) Four ARFM dark events switched off with ARFM's own switch, because their tactical code adds a blocked sitrep straight into the battle past every block list.
; (four more comment lines)
[ARFMDarkEvents.ARFM_DE_DarkEvents]
-CANACTIVATE_REQUIEMDARKEVENT_MEDICALEMBARGO=true
-CANACTIVATE_REQUIEMDARKEVENT_EXTRAAMMO=true
-CANACTIVATE_REQUIEMDARKEVENT_FORTRESS=true
-CANACTIVATE_REQUIEMDARKEVENT_IMMORTALPURSUIT=true
+CANACTIVATE_REQUIEMDARKEVENT_MEDICALEMBARGO=false
+CANACTIVATE_REQUIEMDARKEVENT_EXTRAAMMO=false
+CANACTIVATE_REQUIEMDARKEVENT_FORTRESS=false
+CANACTIVATE_REQUIEMDARKEVENT_IMMORTALPURSUIT=false
```

- Each `-` line is the raw bytes of ARFM's `+` line (`ARFM\Config\XComARFM_DE_Config.ini:153, 156, 160, 172`) with the first byte swapped; the script asserts no trailing bytes on the source lines.
- No backup: the file did not exist before (no `XComARFM_DE_Config.ini` anywhere under `...\XComGame\Mods`). Undo = delete the file.
- Immortal Pursuit is repeated on purpose, so the set of five holds if Odd S9 Tweaks is ever removed.
- Merge replay (`sr\replay_arfm.py`, engine rules: `+` add if absent, `-` remove the exact pair): with jepFixes last, the four keys end as the single value `false` in both possible orders of ARFM and Odd S9; the other 28 ARFM switches stay `true`, Odd S9's four others stay as Odd S9 leaves them.
- Precedent that jepFixes can carry another mod's private ini: `JEP\XComMoreDarkEvent.ini`, verified HOLDING in the 11-12 audit.

### Verified, and not

- Verified: declaring class and config name; byte-exact `-` lines; merge replay; deck code; save state.
- Not verified: the running game. The change loads at the next game start. Confidence that the four switches read false in game: high (same mechanism and syntax as the Odd S9 file, same carrier as the dark-event count file).
- Probe (no file change): none exists in the logs; ARFM prints nothing about these switches. Probe that needs the `jepCovertBlock` mod: log `CanActivate()` of the dark-event objects whose template is `ARFMDE_MedicalEmbargo` and `ARFMDE_ExtraAmmoI` (their check is the switch alone); `False` twice = held.
- Side finding, moot now: in the Medical Embargo, Hair Trigger and Extra Ammo functions the variable `XComHQ` is never assigned (`DE.uc:1778-1824, 1980-1990, 2031-2041`), so the tag lookup runs on an empty reference. Whether those three sitreps were ever really added depends on what the engine returns there. Unverified, low confidence either way.
- Effect on the monthly pool: four fewer events. Medical Embargo and Extra Ammo I were drawable from month 1 with weight 5 each.

## Ruling 2: Opportune Moment 1 and 2

### a. Every path that can attach them

| # | Path | Where | Open today? | What closes it |
|---|---|---|---|---|
| 1 | CI over-infiltration bonus, milestones GenericBuff1 and GenericBuff2 | `CI\Config\XComInfiltration.ini:354-355`; applied by `CI\...\X2StrategyElement_DefaultOverInfiltrationBonuses.uc:81-97` | OPEN, on purpose | nothing; consults no block list; `JEP\XComInfiltration.ini:4, 24-33` keeps both rows |
| 2 | Multiple Sitreps roller and repair on its 7 sources (Guerrilla Op, Supply Raid, Council, Resistance Op, Landed UFO, Retaliation, Alien Network) | pool = every sitrep template without `bExcludeFromStrategy` that has a title and passes `MeetsRequirements`: `MSR\...\X2DownloadableContentInfo_MultipleSitreps_REDUX.uc:424-446, 489-570`; sources `MSR\Config\XCom_Sitrep_Categories_REDUX.ini:44-50` | closed | ONLY `+BlockedSitReps` (`JEP\XCom_Sitrep_Categories_REDUX.ini:35-36`), read at `:440` and `:648` |
| 3 | More Mission SITREPs roller on Council, Resistance Op, Landed UFO, Retaliation, Alien Network | pool = every template without `bExcludeFromStrategy`: `MMS\...\X2DownloadableContentInfo_MoreMissionSITREPs.uc:99-109, 111-194` | closed | the same MSR entry, through MSR's pass after sitrep creation (`MSR ...uc:173-201`, called from `CHL\XComGameState_MissionSite.uc:539-543`) |
| 4 | Multiple Sitreps editor on squad select (change, randomize) | `MSR\...\UIScreen_MultipleSitreps_REDUX_Editor.uc:1634, 1671, 1727, 1788` | closed | the same MSR entry |
| 5 | CI environmental pick (50% per CI mission) | `CI\...\X2Helper_Infiltration.uc:830-879, 882-956` | closed twice | CI itself removes every sitrep that is an over-infiltration bonus from this pool (`:867-876`); `ENVIROMENTAL_SITREPS_EXCLUDE` (`JEP\XComGameData.ini:107-108`) is a second, redundant lock |
| 6 | CI assault mission positive sitrep | `X2Helper_Infiltration.uc:750-782` | closed | takes only bonuses of milestone `SitRep1` (`CI\Config\XComInfiltration.ini:45`); the two are GenericBuff1 and GenericBuff2 |
| 7 | Forced by a mission definition, a plot type or another mod's hook | grep `OpportuneMoment` over every `.ini` and `.uc` in `WS` and `...\XComGame\Mods` | none | hits only in CI and jepFixes |

Why paths 2 to 4 are real: the two templates are plain strategy sitreps. `CI\Config\XComGameData.ini:317-323` gives each only a tag and an effect; `bExcludeFromStrategy` is set nowhere in CI for them; no mission-type limit, no force-level floor. Path 2 is live in this campaign: the 11-10 retaliation got random sitreps from this roller (11-12 audit, missions 3 and 4).

Verdict: over-infiltration is NOT the only path. Per the ruling's condition, nothing was changed. Removing the two names from `+BlockedSitReps` would let them roll as random sitreps on retaliations, facility assaults, UFOs, resistance ops and council missions.

### Is the bonus "restored" already? Yes, by source and by save.

- Neither block list is read on path 1. `ENVIROMENTAL_SITREPS_EXCLUDE` is read only at `X2Helper_Infiltration.uc:856-858`. `BlockedSitReps` strategy-side passes run only for sources where `IsMissionSourceEnabled` is true (`MSR ...uc:189, 218, 382-399`); CI missions use CI's own source and are skipped.
- At launch MSR does strip blocked names from the battle's list for every mission (`MSR ...uc:52-111`), and the tactical map build then copies the mission's own list back over it (`CHL\XComTacticalMissionManager.uc:449`, called from `XComParcelManager.uc:1847`), before soldiers collect sitrep abilities (`CHL\XComGameState_Unit.uc:4907`). So the bonus reaches the battle. Confidence: medium-high, source reading only.
- Save: the current infiltration in `save_Operation Pillaging Pyre` lists `GenericBuff1 -> OverInfiltrationBonus_OpportuneMoment1` and `GenericBuff2 -> OverInfiltrationBonus_OpportuneMoment2` in `SelectedInfiltartionBonuses` (`python sr\ctx.py OpportuneMoment`). CI is offering both.
- Not observed in play: `sr\omscan.py` over all 47 saves since 11-09 finds the sitrep name on no mission and the tag `SITREP_OpportuneMoment` nowhere. Idi has not yet over-infiltrated to a generic milestone in this campaign, so there is no in-game proof either way.
- Probe: over-infiltrate one mission to the first generic milestone and launch. "Opportune Moment" in the mission's sitrep list and among a soldier's passive icons = held. If absent, the launch strip is winning and the fix is a jepFixes-side exemption, to be designed then.

### b. Idi's saved mod-menu file

- `grep -rl OpportuneMoment` over `C:\Users\Idi\Documents\My Games\XCOM2 War of the Chosen\XComGame\Config\` returns nothing. `XComMultipleSitreps_REDUX_MCM.ini` there holds counts and costs only. Nothing for him to click.
- Campaign-side seals (MSR stores them in the save): the strategy save holds no bare `OpportuneMoment1/2` name, so neither is sealed.

## Left for a ruling

Opportune Moment block entries. One choice:

| Option | What it does |
|---|---|
| A. Leave both lists as they are (recommended) | Bonus stays live on infiltrations; random rolls stay blocked. Zero change. |
| B. Drop the two names from `ENVIROMENTAL_SITREPS_EXCLUDE` only, with a dated comment | No behaviour change (CI already excludes bonus sitreps from that pool); removes the redundant lock and the "contradiction" flag of the 11-12 audit. |
| C. Drop them from both lists | Opens paths 2 to 4: Opportune Moment can appear as a random sitrep on non-infiltration missions. |

With A or B, a one-line comment above `JEP\XCom_Sitrep_Categories_REDUX.ini:35` saying "blocked from random rolls only; the CI over-infiltration bonus does not read this list" would stop the next audit from flagging it again.

## Not done

- Game not launched; no runtime confirmation of either ruling.
- No file other than the new `JEP\XComARFM_DE_Config.ini` was written outside scratch. No existing jepFixes file was edited, so no `.bak-1115` was needed.
- Unblocking or exempting Opportune Moment at MSR's launch-time strip: not attempted (no evidence yet that it bites).
