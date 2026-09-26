---
type: report
created: 2026-09-16
author: jep
project: XCOM 2 WotC campaign
status: active
---

# Cockroach audit 2026-09-16: five silent-failure reports, what the files and logs say

Source logs: `Launch-backup-2026.09.15-18.23.23.log` (17:47, 24 tactical inits) and `Launch.log` (19:38, 24 tactical inits), both 1117 mods, zero crashes. Dark Gatecrasher removal confirmed as the fix for the 14:01 crash (Idi, 09-16).

## 0. Detector rule

Every mod that loads writes one `Found X2DownloadableContentInfo <name>` line. Both mods below wrote theirs. A mod that loads but draws nothing writes nothing more. The log detects dead mods, not blind ones. Redscreens and `Unable to find a template` warnings are the second detector; today's log has one new one: `X2SitRepTemplateManager::FindSitRepTemplate(): Unable to find a template with DataName: AHWSitrep_OrbitalDrop` (something references an A Harder War sitrep that no active mod defines; harmless, one sitrep slot wasted).

Three more crashes 09-15 (10:02, 16:21, 16:32), all identical, none in play: `World <shell>.TheWorld not cleaned up by garbage collection! clearing CharacterPool and trying again` then crash, each time the Avenger loads from the main menu. Cause unverified. Not tied to Dark Gatecrasher (16:32 ran after removal).

## 1. Tactical UI Kill Counter Redux (2405013108)

- Loads: `Found X2DownloadableContentInfo X2DownloadableContentInfo_WOTC_TacCounters`, line 7270. No error lines.
- Saved settings, `Documents\...\Config\XComRustyCounter.ini`: `BoxAnchor=3 OffsetX=-420 OffsetY=50 noFadeout=False autoAdjust=True textAlignment=RIGHT`, counters all on, XCOM counts off, totals hidden until Shadow Chamber or Location Scout.
- Reading: it draws a 3-line box anchored at the top right, 420 px in, and fades it out after a few seconds (`noFadeout=False`). It also hides under narrative-moment video feeds (author's known issue). Bond HUD (BTHV2) draws at (950,10) in the same corner. Most likely it is there, faded, or under the bond panel or sitrep panel at 4K. Medium confidence.
- Fix (jep, one edit in the saved ini): `noFadeout=True`, `OffsetY=120`. Then MCM → Tactical Counter Redux to nudge live.

## 2. Sitreps: two blocked ones appeared

- MCM saved values match jepFixes: 1 guaranteed, 1 extra at 50 %, change 10 intel.
- Block list variable and section match the mod's own file (`+BlockedSitReps` under `[MultipleSitreps_REDUX.X2DownloadableContentInfo_MultipleSitreps_REDUX]`). The mod's comment: "These sitreps will not be rolled by this mod." Sealing in the squad-select editor works on the same pool ("Sealed SitReps are excluded from the random pool"). Sealing one by one would not have helped.
- The mission at 3434 s (Covert Infiltration supply extraction) carried `SITREP_LightningStrike`, `SITREP_ARFMHighground`, `SITREP_TheLost`. Lightning Strike is a Covert Infiltration over-infiltration reward (`XComInfiltration.ini` line 360, tier SitRep1). High Ground is the ARFM Dark Events covert-action risk (`ARFMDESitrep_HighGround`, its tag is spelled differently). Neither passed through the sitrep mod. Two channels the block list never sees: CI infiltration risks and bonuses, and ARFM dark events.
- Whether the block list works on its own channel: unverified (verbose logging off).
- Fix (jep, jepFixes, loads last, verified): `XComInfiltration.ini` with `-SitRepBonuses=` lines for LightningStrike, WellRehearsed, MentalReadiness, TacticalAnalysis, LocationScout, OpportuneMoment1, OpportuneMoment2 and `-FlatRiskSitReps=` lines for ShoddyIntel, AdventAirPatrols, IntelligenceLeak, UpdatedFirewalls, Phalanx_CI, RestrictedAirspace, ARFM HighGround, Brittleness, OverwatchWeakness, AlienArmor. Plus `bVerboseLogging = true` in the sitrep file for one session. Cost: over-infiltration tier 1 keeps only Comms Jamming, tier 3 only Shadow Squad. Dark-event-forced sitreps stay (counter the dark event in play).

## 3. Load from character pool (618960429)

- 2016, `BuiltForWOTC: False`. Loads (`X2DownloadableContentInfo_Loadfromcharacterpool`, line 7733).
- Source: on `UICustomize_Info` init, in the Armory only, it appends one list row "Load Character From Pool" at the bottom of the Info tab and forces the list height to 250 px. WOTC's Info tab is longer, and the row is added once (OnInit), so any list refresh wipes it.
- Check: Armory → soldier → Customize → Info → scroll to the very bottom right after opening. Absent there = dead in WOTC. Medium confidence.
- Overlap already installed: Character Pool Source Control (3766131235) gives per-source pool policies (starting soldiers, HQ recruits, rewards, SPARKs); the appearance-import use case is what this old mod did.

## 4. Roster size

- Base `NUM_STARTING_SOLDIERS=12` (`DefaultGameCore.ini` line 242). Covert Infiltration overrides to 16 (`XComGameCore.ini` lines 28 to 29). jepFixes already carries an `XComGameCore.ini` and loads after CI: a `-NUM_STARTING_SOLDIERS=16` / `+NUM_STARTING_SOLDIERS=N` pair there is the lever.
- No crew cap exists in the base game or in any active mod config (grep for cap keys: none). "Two crew size upgrades" has no match on disk. Nearest: Robo-Squad Size Enhanced (2360829219), `StartingSquadSize=4`, upgrades I to IV, `MaxDefSquadSize=12`, ranks and costs per tier. Awaiting Idi's meaning.

## 5. Persistent soldiers, Veteran Soldier Presets (3800165374)

- Kei, posted 2026-09-12, updated 09-15, four days old, "made for personal use, there may be unintended behavior". Picks pool soldiers and adds them to the starting roster with class, rank, weapons, abilities. Reported reliable for about 3 to 5 characters. Config in `XComCharacterPoolStartingSoldiersDefaults.ini`, data in `XComCharacterPoolStartingSoldiersUser.ini`.
- Covers Kazimir and Jane at Gatecrasher (2, inside the reliable band). Does not cover "after the first retaliation": no timed arrivals in this or any installed mod.
- Route for Dancis and Dawn: Source Control policy "Resistance HQ recruits = Character Pool Only" plus Rusty's Recruits Redux (already active) so they surface in the recruit list; or fold them into the presets (4 total, still inside the band) and accept day-one arrival.

## Applied 2026-09-16 10:15 (jep)

- jepFixes `XComInfiltration.ini` created: 12 `-FlatRiskSitReps` and 8 `-SitRepBonuses` removals, every blocked name found in CI's and ARFM's infiltration tables (52 names on the block list). OpportuneMoment1/2 left in place: CI's two generic milestones would hold zero bonuses. Mirrored in `projects/XCOM/jepFixes/Config/`.
- jepFixes sitrep file: `bVerboseLogging = true` for one session. Next log shows the roll, the block, the repair.
- Kill Counter: jep cannot write in `Documents\...\Config` (permission denied on the saved ini). Idi's click path: Options → Mod Settings → Tactical Counter Redux → No fadeout on, Offset Y 120.
- Unverified until the next log: the `-` removal lines match by parsed struct value; the verbose lines and a supply-extraction launch are the receipt.

## 4b. Crew size = Living Space Redux (3309295545)

- Workshop copy dated 07-27, no manual edits survive. `XComLivingSpace.ini`: `STARTING_CREW_LIMIT=30`; two `+CrewSizeUpgrades` entries, ADDCREW 10 (100 supplies, 10 elerium dust, upkeep 10, power 1) and ADDCREW 20 (200 supplies, 20 dust, 1 core, upkeep 20, power 2); cap 60. Engineers stop counting once a Workshop exists, scientists once a Laboratory exists. Over the limit: recovery time penalty 10 % per extra soldier.
- Lever: jepFixes `XComLivingSpace.ini` with `STARTING_CREW_LIMIT=N`, then `!CrewSizeUpgrades=()` (the clear operator, proved live by UECP's `!Groups=()`) and two fresh `+CrewSizeUpgrades` lines. Starting roster: jepFixes `XComGameCore.ini` gets `-NUM_STARTING_SOLDIERS=16` / `+NUM_STARTING_SOLDIERS=N` (CI sets 16, base 12).
- Proposal, sized for 70 to 80 soldiers per campaign: starting soldiers 24, starting crew limit 60, upgrade 1 +30 (cap 90), upgrade 2 +40 (cap 130). Costs unchanged. Awaiting the numbers.

## 6. Dark VIPs and MOCX/EXALT from the Importable files

- Mechanism (game source, `CharacterPoolManager.uc` lines 260 to 307, 432): every generated character calls CreateCharacter with the pool's global SelectionMode unless a mod overrides. Mixed = coin flip per character between pool and random. PoolOnly = pool entry whose type box matches (Dark VIP for Dark VIPs), random only when no unused eligible entry exists. The game reads one file: `DefaultCharacterPool.bin`. `Importable\` is inert until imported in the Character Pool screen.
- Main pool today: 453 characters. `Complete Season 8+9 VIP Pool.bin`: 127 characters, 0 present in the main pool. `EW EXALT Allstars-Deadput.bin`: 70, 1 present. Neither has ever been eligible. `Complete Season 8+9 Pool.bin`: 202, 9 present. `2025-05-19.bin`: 330, 177 present.
- MOCX Initiative (`XComDarkXCom.ini` lines 130 to 137): `DarkVIPsOnly = true`, `RandomizePool = false`, so MOCX follows the pool's global mode and takes entries tagged Dark VIP only. MOCX Customizer+ maps a Dark VIP entry's pool class to the MOCX dark class. EXALT is the same units with EXALT nationality (MOCX as EXALT 1.5).
- Global mode today: `eCPSM_Mixed` in the profile config (`XComGameData.ini` lines 368, 369, 1321). Source Control overrides starting soldiers (PoolOnly) and recruits (RandomOnly) but has no Dark VIP source.
- Procedure (Idi, Character Pool screen, jep cannot edit the binary pool): 1. Import `Complete Season 8+9 VIP Pool.bin` and `EW EXALT Allstars-Deadput.bin`. 2. Confirm each imported entry has only Dark VIP ticked (jep could not read the flag bytes reliably from outside). 3. Set the pool mode to Character Pool Only. 4. Export a fresh backup of the main pool. Receipt: first Dark VIP or MOCX pod shows a Season 8+9 name.
- Side effect of PoolOnly: friendly VIPs also come from entries with the VIP box, and Source Control keeps recruits random, so the 200 soldiers are unaffected.

## 13:10 log read (Launch.log 12:50, 1118 mods)

- Crash: garbage-collection failure on the tactical → Avenger transition, 140 worlds not released, 2.5 s after `Kismet: <<< Mission Complete >>>`. Same family as 09-15 10:02, 16:21, 16:32 and today 11:47 (Avenger → saved tactical). Five in two days, none in the 48 tactical transitions of 09-15 evening. Only mod-list delta since then: Veteran Soldier Presets 3800165374 (added 11:19, user file written 12:45). Console commands are not logged, so the KillAllAIs/ttc ending cannot be compared.
- jepFixes loads second to last (the last entry is the workshop root itself, chronic in every log). Sitrep verbose lines present (`[MultipleSitreps] Attached sitrep roller to: ...` for 7 mission sources). No Amalgamation warnings; `LogDebug = true` now set in jepFixes for a positive receipt next launch. Living Space and starting roster: no log line exists, the barracks count is the receipt.
- Kill Counter: `noFadeout=True` saved, OffsetY still 50; the mod writes nothing to the log in tactical, so load is proven and draw is not. Extended Information Redux 3 replaces `UITacticalHUD_Enemies`, the strip in the same top-right area; X2 Commander HUD replaces `UITacticalHUD_CommanderHUD`. Probe: MCM anchor to top-left, offsets 0 / 200.
- 15:00 Kill Counter bisect candidates: Commander HUD has 3 active dependents (LOS Preview, Manual Reveal+, Dark Events in Commander HUD), so Idi vetoed it. Tactical Squad HUD 3737250500 has no dependents, hooks UITacticalHUD, added 2026-08-30 after the counter. Single-mod bisect proposed. Steam page fetch for the counter: HTTP 429.
- 15:40 Kill Counter, closed as far as offline evidence goes. Facts: mod loads, MCM saves, its shell listener writes the version file; the panel is a plain child of the tactical HUD (original source, Luminger GitHub: GetTacticalHUD → GetChild → spawn, no visibility conditions); Speed Up Aliens uses the same pattern and draws. Bisected clean: Tactical Squad HUD off (its code never loaded, TSHSJ lines 0), Combat Log disabled by its own setting in the 15:12 log. No script warning names the counter in any log. Redux source not public. Remaining candidates untested: Extended Information Redux (BETA, 33 HUD references, owns the enemy strip), Robo-Squad Size Enhanced (171 references, relayouts the HUD for 12 soldiers), Commander HUD (vetoed, 3 dependents).

## 20:20 campaign crash 19:59:58 and the Combat Log

- Crash: Windows Application Error 1000, `XCom2.exe` exception `0xc0000409` (fail-fast, stack cookie check), fault offset `0x10a3b7c` inside XCom2.exe, WER bucket 1262953221989039713. No in-game crash handler ran, so `Launch.log` has no marker; it ends at 2891.38 s on `XComPawnPhysicsProp_79 is attached to XComAlienPawn_106 which is in another level`, a line repeating since 2814 s (a prop on a pawn that lives in a streamed cinematic sublevel; the ADVENT Shieldbearer reveal camera package was loaded in that window). Mission: Gatecrasher, Plot_WLD_Compound_ATT_Stream, pods AdvCaptainM1 x4 leaders, Sectoid x2, AdvTrooperM1 x2, loaded from save 6 times. Not the GC family. One sample, no log fingerprint, WER report folder denied to jep. Not bisectable yet; watch for recurrence at pod reveal or last-pod moments.
- Separate signal: four LiveKernelEvent watchdog dumps dated 2026-09-15 08:35 (`WATCHDOG-20260915-0835.dmp`, codes 1a8/1b8 = display driver timeout), reported by WER on 09-16 19:15. GPU hang on 09-15 morning, before any of the game crashes examined. Unlinked so far.
- Combat Log invisible: cause is in its own user file `Documents\...\Config\XComBattleChatter.ini`: `bEnabled=False`, panel saved at BottomLeft 240 x 16, global window off. The mod logs `bEnabled is FALSE` at every tactical start. Idi's MCM clicks: Enabled on, panel 400 x 510, global window on if wanted. jep cannot write that folder.

## 21:00 Windows crash archive, 22 XCom2 reports since 08-30 (read after Idi's icacls grant)

| Signature | Module, offset | Dates | Reading |
|---|---|---|---|
| BEX64 0xc0000409 | XCom2.exe 0x10a3b7c | 08-30 12:44, 09-13 09:23, 09-14 16:11, 09-16 20:00 | one fixed code path in the game, fail-fast; 08-30 instance ran without any RenoDX addon loaded, so the render hooks are not required for it |
| APPCRASH 0xc0000005 | XCom2.exe 0x6d4e66 | 09-15 10:02, 16:21, 16:32, 09-16 11:47, 12:50 | the garbage-collection family, one fixed offset; none since the presets removal across three runs |
| APPCRASH 0xc0000005 | XCom2.exe 0x10e6d5 | 09-16 14:11 | unexamined until now, see below |
| APPCRASH / BEX64 | nvngx_dlssnr.dll 0x147f8 / 0x88621 | 08-31 19:05, 09-12 09:50, 09-12 10:28 | DLSS-NR library crashes, none since the 09-14 addon swap |
| BEX64 | renodx-dlss5.addon64 | 08-30 15:08 | old addon build |
| APPCRASH | ntdll.dll | 08-30 11:51, 09-15 16:22 | secondary faults after a crash |
| AppHangB1 | | 09-13 10:11 | hang, no crash |

Kernel dumps in `C:\Windows\LiveKernelReports` are dated 09-10, not 09-15 (WER re-reported them on 09-16 19:15; the 09-15 files no longer exist): three watchdog events at 03:22 (codes 0x1A8, 0x1B8, param 0xA) and one `0x141 VIDEO_ENGINE_TIMEOUT_DETECTED` at 10:16 with an 8.3 GB live dump still on C:. GPU engine timeout on 09-10, before the XCOM render-stack work. Unlinked to the game crashes.

Every XCom2 report lists ReShade `dxgi.dll` and `GFSDK_Aftermath` loaded; RenoDX addons in all but the first three.

## 22:00 dumps read

- Tooling: WinDbg 1.2606 installed per user by jep from Microsoft's CDN (`winget` failed with 0x80070002, `Add-AppxPackage` on the downloaded bundle worked; no admin). Its packaged `cdb.exe` cannot be launched in place; a copy runs from the job temp dir. It refuses the game's own minidumps (`Conflicting Address Range`, the game writes overlapping memory ranges). jep's own minidump parser (`mdstack.py`, exception record, module list, stack scan from the thread record) reads them.
- 12:50 and 11:47 (GC family): `0xC0000005` read at address 0 in `XCom2.exe+0x6D4E66`, both. Stack: game code and the allocator only. No ReShade, RenoDX, DLSS or driver frame.
- 14:11 (unmentioned test-campaign crash, turn 1 of a Gatecrasher on Plot_WLD_Compound_ATT_Ravine): `0xC0000005` at `XCom2.exe+0x10E6D5`, stack game code plus 10 APEX physics frames. No hook frame.
- 09-15 14:01 (Dark Gatecrasher): rendering thread inside the NVIDIA D3D11 driver (45 driver frames, 14 d3d11, DXCore). No hook frame. Consistent with a failed draw from the lighting map.
- 19:59 fail-fast `0x10a3b7c`: no dump exists (WER uploads and deletes). Four occurrences: 08-30 12:44 without RenoDX loaded, 09-13 09:23, 09-14 16:11 in the main menu right after Campaign Notes "Saved to ini", 09-16 19:59 in tactical with no Campaign Notes activity for 4 minutes. Context differs each time; not attributable yet.
- Housekeeping: an 8.3 GB kernel live dump from 09-10 10:16 sits in `C:\Windows\LiveKernelReports\WATCHDOG-20260910-1016.dmp`, system-owned.
