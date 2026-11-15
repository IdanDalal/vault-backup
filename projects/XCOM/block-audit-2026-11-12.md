---
type: report
created: 2026-11-12
author: jep
---
# jepFixes block audit, 2026-11-12: which blocks hold in the live campaign

Asked by Idi after the covert action block was found failing: "other blocks might be failing silently, check/verify them all."

Method: three audit agents, one per layer, each block checked four ways: lever against the declaring class in source, bypass paths in code, evidence in the 8 `Launch.log` files on disk (11-09 to 11-12), and state read from your latest save (`save_Save 258_1`, written 11-12 13:03) with a read-only save reader the strategy agent built. A HOLDING verdict requires positive evidence from the running game; a config that only looks right earns UNPROVEN. Full receipts with file and line: `block-audit-2026-11-12/strategy.md`, `sitreps.md`, `items.md`. Save reader: `save-tools/`.

Nothing here was tested by launching the game.

## Update 2026-11-15 (after Idi's 11-14 session and his rulings)

Read from the 11-14 `Launch.log` (probe lines tagged `jepCovertBlock`) and applied on his words "all rec", "remove those five ARFM dark events", "restore Opportune Moment if it only appears as an over-infiltration bonus".

| Row below | New state | Receipt |
|---|---|---|
| 1 covert list | **HOLDING since the first month end**; it failed only for the first month's offers | Probe: the game's list holds all 19 names, mine included (`Launch.log:57983`). Month end at `:58076`: new offers on all three factions, none of the nine, and the sweep mod removed nothing |
| 2 PCS side routes | Three routes closed (V1); unseen in game | Replay on live files: Black Market tables one per name with 0 of the six types; `EpicPCS` deck 19 -> 13; salvage lists 0 of the six. Next launch: no `BlackMarketPCS` duplicate lines, `EpicPCS contains 13`. MOCX's two projects stay open |
| 15 sitrep exclude list | **HOLDING** | Probe prints 53 names (`:57985`) |
| 16 risk and bonus removals | **HOLDING** | Probe prints 5 rows left, none of the removed ones (`:57988`) |
| 18 loot expiry | normal loot logged at 3 turns (`:115963`); psi loot not seen yet | Logging stays on until a psi drop |
| 19 boss lists | **HOLDING** | "Lists after" dump: Frost Abomination in the Psionic Storm boss list, `AdvGeneralM2_LW` in the field commander list (`:18820`, `:18828`) |
| orders removed (row 4) | confirmed again | Probe prints the removed-order list (`:57990`) |

Covert cause, best reading now (medium-high): the starting faction's first offer list is built during campaign creation, before Covert Infiltration's filter is listening. Every later list passes through the filter. `jepCovertBlock` stays as the net for month one of any future campaign and logs whatever it removes.

Applied 11-15:
- **Stygian Slayer** (Idi's `SNAPSHOT.png`): Snapshot is a penalised primary-weapon shot that hides whenever a standard shot exists (`X2Ability_SharedPerksRSAbilitySet.uc:1679-1688`), so it only acts on a sniper rifle. 12 pistol-primary cards cut; the spec stays on Androctonus - Stygian Slayer - Scout. Deck 707 -> 695 (simulated), weights regenerated, pick sheet refreshed with 112 ticks kept. An eye pass over the starting perks of all 141 specs found no other case. Own regression: a 09-17 rule already said this and was lost in a later cleanup.
- **V1** (agent `fix-items`, checked by jep): `jepFixes/Config/XComGameCore.ini` (Black Market), `XComGame.ini` (reward deck), new `XComCorpseLooting.ini` (salvage). Choice made: where the two source Black Market tables disagreed, each roll group keeps the larger total, so stock chances never drop.
- **V2**: 95 dead names out of the weapon hide list (513 -> 418 merged), six Mandalorian helmet lines out, `XComTemplateEditor.ini` and `XComEndgameWeapons.ini` moved out (kept in the job folder and in git history). Four more Resistance Firearms names look dead by the same test and were left in.
- **Four ARFM dark events switched off** with ARFM's own switches in new `jepFixes/Config/XComARFM_DE_Config.ini` (class and config name checked: `ARFM_DE_DarkEvents.uc:1,25-34`): Medical Embargo, Extra Ammo, Fortress, Immortal Pursuit. Hair Trigger's event (Extra Ammo II) has no switch and can only follow Extra Ammo I, so it goes with it. No switch separates the sitrep from its dark event, so removal was the only way. Safe mid-campaign: templates stay; the switch is read each time the monthly deck is built. Newest save: none of the five active or pending. Next launch: four probe lines print `False`.
- **Opportune Moment 1 and 2: no change needed.** They are ordinary strategy sitreps, so three random rollers could draw them; the block list entry is what stops that. The over-infiltration bonus path reads neither block list (source reading, medium-high; your current infiltration offers both bonuses in the save). Today's state is already "only as over-infiltration bonuses".
- Second Wave "Perilous Yearning" is off in this campaign, which closes the Ambush and Fortress path listed below.

Appendices added: `block-audit-2026-11-12/items-fix.md`, `sitreps-fix.md`.

## Verdicts (as of 2026-11-12)

| # | Block | Verdict | Evidence | Next proof |
|---|---|---|---|---|
| 1 | Covert actions never offered at random (9 names) | **FAILING**, fixed by the new mod | Logs: 3 of the 9 completed, one again on 11-12. Save: Recover Useful Items exists as an action object | Next launch: `jepCovertBlock` log lines |
| 2 | Six PCS types removed at every tier | **FAILING on four side routes** | Main loot tables hold (game's own loot check flags no `PCSDrops` duplicate). Open: Black Market tables, More POI Types reward deck (log: 19 entries, all six inside), ARFM Scavenger salvage, MOCX proving ground projects. No removed PCS seen awarded | Ruling V1 |
| 3 | Capture risk off | HOLDING | Save: 5 actions that carry Captured in vanilla hold Wounded + Ambush only. Logs: 0 of 326 attached risks | - |
| 4 | 31 orders removed | HOLDING | Save: 20 card states = 52 minus 32 removed | - |
| 5 | Chosen trait whitelist | HOLDING, side effect | Save: all 12 rolled traits are on your list | See note A |
| 6 | Dark events 1, 2, 2, 3, cap 3 | HOLDING | Save: month 1 rolled 1 event; the other active mod's numbers would give 2 or more | Third monthly report shows 2 new events |
| 7 | Emergency Defense missions removed | HOLDING | Absent from the startup dump of 115 mission types in every log | - |
| 8 | Basic Immolator infinite | HOLDING | Log "Making 156 items buildable" = replay with the removal (157 without) | - |
| 9 | Crew limit 50, +20, +30 | HOLDING | Save: limit 50, then 70 after the first upgrade | - |
| 10 | Sitrep count 1 + 1 at 50% (Multiple Sitreps missions) | HOLDING | Your saved mod-menu file is the live source and reads 1 / 1 / 50 | - |
| 11 | Enemy groups, 34 of 35 added entries | HOLDING | Live "Lists after" dump; Muton Adolescent spawned and died in missions | - |
| 12 | Amalgamation cuts and class weights | HOLDING | 11-12 log: `Disabled classes 1332`, weights `missing 0 of 699` | - |
| 13 | Class choices 100, starting roster 40 | HOLDING (medium) | Your screenshots: scrolling class list; barracks 42 on 11-09 | - |
| 14 | 52 sitreps blocked on Multiple Sitreps missions | UNPROVEN | 0 blocked on 2 retaliation launches; too few draws | 20 reloads with verbose logging, only if you want certainty |
| 15 | 52 sitreps excluded on Covert Infiltration missions | UNPROVEN, leaning holding | 0 blocked in 10 mission sitrep arrays in the save | Next launch: probe line prints the list (53 names = held) |
| 16 | 25 infiltration risk and bonus sitreps removed | UNPROVEN | All 25 `-` lines byte-identical to live `+` lines; none seen on 6 missions | Next launch: probe line prints the table (9 rows = held) |
| 17 | 509 weapons hidden | UNPROVEN, suspicious | Save: 103 hidden weapons exist as items. 0 carried in 226 logged loadouts. Resistance Firearms re-creates 307 of them on every load; the hide mod edits 1 of 5 difficulty copies | Armory, any rifle soldier, primary list: "AK-47 Type 1" present = failing |
| 18 | Loot expiry, psi loot 3 turns | UNPROVEN | A 3-turn timer seen in a tactical save; same as the mod default for normal loot | Logging switched on today: next psi drop logs its timer |
| 19 | Frost Abomination and two Generals in boss lists | UNPROVEN | Their three lists were never printed | Printing switched on today: next launch |
| 20 | Nimble Hands set, Chosen reveal wrap, General buff list, Mass Effect leg parts | UNPROVEN | Levers correct, nothing logged | In-game sightings listed in `items.md` |

## Paths no jepFixes list can reach (other mods' code)

- ARFM dark events add five blocked sitreps inside a mission, after every filter: Medical Embargo, Hair Trigger, Extra Ammo, Fortress, Immortal Pursuit (`ARFM_DE_DarkEvents.uc:1827-2348`). Blockable only by removing those five dark events.
- Covert Infiltration missions have no sitrep count limit. Most seen on one mission: 2.
- Opportune Moment 1 and 2 sit on both block lists and stay wired as over-infiltration bonuses on purpose (09-28: they are the milestone's only entries). The game still grants them.
- Dark events can reach 4 in a month when a Chosen plays its Dark Event action (you accepted this on 09-28).
- ARFM mutator strengths go straight onto a Chosen, past the whitelist. None present yet.

## Note A: Chosen whitelist side effect

Save: Hunter holds `[IncreaseCrit, None]`, Warlock 2 strengths, Assassin 3, with 3 starting strengths configured. The 13-name list ran out of strengths that fit at campaign start, so two Chosen began one strength short and the Hunter carries an empty slot. Effect so far: slightly weaker Chosen. Risk: a screen that prints the empty slot. Recommendation: leave it; widening the list only changes future level-ups.

## The covert block's cause, narrowed

- The file loads: the capture-risk lever in the same `XComGameBoard.ini` holds (row 3).
- The filter runs: Covert Infiltration's own nine blocked actions never exist as action objects in the save.
- Names added by other mods' files do not take effect: mine exist as actions, and so does Exhaustive Training, which Odd S9 Tweaks adds to the same list (that one may arrive by another route; unverified).
- Why additions fail while the same pattern works for order removal: unknown. Confidence in "additions never reach the list": medium.
- `jepCovertBlock` now asks the game directly on every map load: four `get` lines print the lists as the game holds them (covert list, sitrep exclude list, risk table, removed orders). Whether the `get` console command exists in this build is unverified; an empty answer proves nothing, and the sweep works either way.

## Dead lines found (your standing rule: out-of-date lists get removed)

- Weapon hide list: 87 names belong to inactive mods, 8 match no template.
- `XComTemplateEditor.ini` (target mod inactive; Template Master logs 2 errors per launch), `XComEndgameWeapons.ini` (inactive), six Mandalorian helmet lines in `XComContent.ini`.
- 14 of the 52 blocked sitreps have no live template.

## Rulings wanted

| V | Change | What it does |
|---|---|---|
| V1 | Close the three PCS routes config can reach: Black Market tables, the More POI Types reward deck, ARFM Scavenger salvage lists | The six removed PCS types stop appearing in the Black Market, in that point-of-interest reward and in salvage. MOCX's two proving ground projects stay open (hard-coded) |
| V2 | Remove the dead lines listed above | Two Template Master errors per launch disappear; the hide list shrinks from 509 to 414 names; no gameplay change |

jep recommends both.

## Changed today for this audit

- `jepFixes/Config/XComELR.ini`: three `+ListsToLog` lines (row 19).
- `jepFixes/Config/XComLootPostMover.ini`: `bEnableLogging = true` on the DLCInfo class, declaration checked (`X2DownloadableContentInfo_WOTCLootPostMover.uc:11-13`) (row 18). Switch off after the proof.
- `jepCovertBlock` rebuilt with four `get` probes and chunked log output.

## Not done

- No fix for the PCS routes or the dead lines (rulings V1, V2).
- Weapon hide list not settled: needs one look at the Armory.
- Sitrep block on Multiple Sitreps missions not proven; the proof costs about 20 reloads.
- One log rotated out during the audit (the campaign-start session); lines quoted from it cannot be re-read.
