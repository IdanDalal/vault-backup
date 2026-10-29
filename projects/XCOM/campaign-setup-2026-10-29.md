---
type: report
created: 2026-10-29
author: jep
---
# Campaign setup 2026-10-29: slot rules, Highlander, filters, Immolators

State after Idi's mod pass: 52 mods disabled since 09-28, 17 subscribed, AML active 1,079 of 1,131.

## 1. Amalgamation weapon slot optimization (installed, new campaign only)

Definition used: a spec "carries" a weapon in its own slot (primary spec: primary slot; secondary/tertiary spec: secondary slot). Checked against where each tree's abilities land (Veteran's pistol entry feeds nothing, so Veteran counts as rifle; AlienHunter2's tree feeds the sword slot).

| # | Rule | Specs | What it does |
|---|---|---|---|
| W1 | sword P <-> sword S | P: HareCaptain, MusaSamurai, Ravager, Savage. S: ARFMPlunderer, AlienHunter2, Blademaster, Brigand, Corsair, HareSwash, LegendaryWarrior, NinjaWarrior, SkvRaider | sword primaries only take sword secondaries, and the reverse |
| W2 | pistol P <-> pistol S | P: Akimbo, Fusilier, Gunfighter, HareQuartermaster, Pistoleer, Vigilante. S: Corpsman, Gunslinger, HareBuckler, HareGrimArtist, Hotshot, Rogue, SkvStygian, Trickshot | same; Ironclad (shield + pistol kit) also allowed under pistol primaries; replaces the 09-28 P1c DisableClass list (350 names, now dead) |
| W3 | gauntlet S <-> gauntlet T | Burner <-> Heavy, SkvFirebug | only together |
| W4 | gremlin T -> gremlin S | SkvArtisan, HareModernPirate (gremlin too, jep extension) -> CombatMedic, CPUExpert, Dragoon, DronePilot, DroneProtocol, Techspert, Valkyrie | gremlin tertiary never under a non-gremlin secondary |
| W5 | cannon P -> SkvSiegeGunner | Dreadnought, Gunner, Harbinger, SAWGunner, Wrecker | SiegeGunner is the only cannon secondary (no weapon of its own, every perk feeds the primary); the reverse was already the authors' rule |
| W6 | shield S <-> shield T | Ironclad, Vengeance2 <-> AegisDefender, Riot, SwordMaster | only together |
| C | Commissar off | self-pair `(A="Commissar", B="Commissar")` | `AreSpecsIncompatible` (X2SoldierClass_Amalgamation.uc:548) matches every class holding it: 0 Commissar classes |

- Releases: the mod authors ban most same-weapon pairings (Harehnoth, Musashi, Stukov's Exclusions, Drumax, Corsair, Gunfighter, Vigilante...). Their stated reason is taste ("fitting gameplay"); shared abilities per pair 0 to 5, no shared squaddie skill except the basic pistol shot. 73 pairs released by 106 `-IncompatibleSpecs` lines, each a byte copy of the author line (0 without an exact twin). jep's own 09-16..09-28 pairs stay (mechanical: Rogue Blindside, sidearm vs pistol, R4 squaddie duplicates).
- File: jepFixes `XComAmalgamation.ini`, block at the end of `[AmalgamationClassesWOTC.X2SoldierClass_Amalgamation]`: 300 new pairs + Commissar + 106 releases; P1c block removed; every other line byte-identical (diff: 421 added, 356 removed).
- Deck simulation (section-aware, all active `XComAmalgamation.ini`, mirrors the .uc loop): 1,888 -> 1,497 classes. Real file simulates to the identical class set. Rule violations in the final deck: 0 (the Ironclad exception aside).

Per spec, cards before -> after:

| Group | Change |
|---|---|
| sword P | HareCaptain 6->4, MusaSamurai 10->11, Ravager 7->0, Savage 6->0 |
| sword S | Blademaster 89->4, Corsair 37->2, NinjaWarrior 29->4, ARFMPlunderer 19->2, LegendaryWarrior 5->2, HareSwash 6->1, SkvRaider 23->0, Brigand 5->0 |
| pistol P | Akimbo 13->23, Fusilier 58->17, Gunfighter 10->21, HareQuartermaster 24->19, Pistoleer 6->17, Vigilante 28->29 |
| pistol S | Corpsman 2->16, Gunslinger 31->30, Hotshot 26->27, SkvStygian 0->15, HareGrimArtist 8->14, Rogue 5->11, Trickshot 5->9, HareBuckler 2->3 |
| gauntlet | Burner 42->11, Heavy 13->7, SkvFirebug 8->4 |
| gremlin T | SkvArtisan 10->23, HareModernPirate 0->22 |
| cannon | Gunner 54->7, SAWGunner 53->5, Harbinger 28->7, Wrecker 22->5, Dreadnought 21->4, SkvSiegeGunner 31->28 |
| shield | Vengeance2 33->6, Ironclad 4->1, AegisDefender 1->5, Riot 2->2, SwordMaster 7->0 |

- Gone (0 cards): Ravager, Savage, Brigand, SkvRaider, SwordMaster, Commissar (asked), plus collateral XenoZoologist 1, XenoZoologistMM 1, Maniac 1.
- Why the sword specs die: every sword+sword pair has an empty tertiary intersection. Each sword spec's author whitelists few tertiaries, and the whitelists do not overlap. Reviving them means releasing tertiary bans, which rewrites the authors' tree design; not done.
- Why SwordMaster dies: sword-and-shield needs a sword primary with a shield secondary, which W1 forbids.
- Already 0 before today: Androctonus, AlienHunter2, DronePilot.
- Tools (vault `amalgamation-tools/`): `specs.py` (spec table), `sim.py` (deck simulator), `slotrule.py` (W1-W6 pairs), `release.py` (byte-copy releases), `evalfull.py` (impact + violation check), `slotapply.py` (install).
- Probe, first launch: `Amalgamation DLCINFO INFO: Disabled classes 260` (was 610: the 350 P1c names are gone). In game: no promotion card shows a sword primary with a non-sword secondary, a pistol secondary under a rifle, Burner without Heavy/Firebug, Commissar.

## 2. Red Highlander dependency (fixed)

- 7 mods required stable CHL 1134256495; beta 1796402257 is active: Dont Unequip, Extra Abilities for Chosen Weapons, Mission: Control Point, Even More Abilities For Chosen Weapons, Research Tree (Civ style), x2loc Weapon Cat Names, Commands UI.
- `IgnoredDependencies` += 1134256495 on each, text-level edit of `C:\XCOM2 AML 1.6.0-beta\settings.json`, AML closed (tasklist). Verified: exactly 7 fields changed; active mods with a missing dependency now 0.
- Backups: `D:\work\aml-settings-2026-10-29-pre.json`, post copy `D:\work\aml-settings-2026-10-29.json`.

## 3. Sitrep and dark event filters (verified static)

| Layer | Where | Target mod | State |
|---|---|---|---|
| Sitrep count 1 + 1 at 50% | jepFixes `XCom_Sitrep_Categories_REDUX.ini`, `..._MCM_Defaults.ini` | Multiple Sitreps REDUX 3739636065 | active; MCM saved values in Documents override counts |
| Sitrep block list, 52 names | same | same | active; 4 AbiziOTS names now dead (mod off), harmless |
| CI environmental sitrep exclude, 52 mirror | jepFixes `XComGameData.ini` `[CovertInfiltration.X2Helper_Infiltration]` | Covert Infiltration 2567230730 | active |
| CI risk / over-infiltration bonus sitreps, 25 removals | jepFixes `XComInfiltration.ini` | CI + bridges 2608952868, 2608960168 + ARFM 2795578857 | all active; 25 of 25 `-` lines still have exact twins after this week's updates |
| Dark events per month 1, 2, 2, 3, cap 3 | jepFixes `XComMoreDarkEvent.ini` | Scaling Dark Events 3078247580 | active; Chosen-action DE can make a 4th (ruled B, 09-28) |
| ARFM dark-event sitreps (ARFMDESitrep_*) | in the 52-name list | ARFM Gameplay Mutators | active |

- No dark-event block list exists: counts only. A screenshot of an unwanted dark event -> jep finds its template and owning mod, then the lever (remove from deck, or block its sitrep).
- New mod Mission: Control Point: its only sitrep code swaps The Horde for The Lost on its own missions (`PostSitRepCreation`); its missions otherwise pass through the normal sitrep roll, so the block list applies (medium confidence until first sighting).
- Unwanted sitrep on a screenshot -> name lookup in `sitrep-list.md`, then the channel: mission roll (REDUX list), CI infiltration (exclude list), CI risk/bonus (`-` byte copy), or a dark event.

## 4. 200+ Basic Immolators

Cause (high confidence on the flag, medium-high on the trigger):

- Immolator Overhaul 2237137501 ships `Config/Compatibility/XComStrategyTuning.ini:2` `+arrMakeItemBuildable=(ItemName="MZImmolator_CV")`.
- Prototype Armoury 2567230602 applies it every launch: `PATemplateMods.uc:111-113` sets `CanBeBuilt=true`, `bInfiniteItem=false`. The base Immolator mod 1918448514 defines it infinite + starting item (`X2Weapon_Immolator.uc:110-112`). Config subfolders do load (Amalgamation's Sentinel lives in `Config\Tertiary\` and plays in game).
- Five chemthrower primaries (Desolator, Paramedic, Pioneer, Salamander, Toxicologist) use it as squaddie weapon. A finite squaddie weapon gets re-created by the Highlander loadout validation whenever a chemthrower soldier's primary slot is emptied; the old one returns too, so HQ gains one per soldier per strip.
- Triggers (agent's trace, `UIArmory_Loadout.uc:445-511`): "Make weapons available" in the Armory, robojumper Unequip Squad / Unequip Barracks. Plain locker swaps add nothing. None of this week's 17 new mods creates items; Dont Unequip reduces triggers.

Fix installed: jepFixes `XComStrategyTuning.ini` (config name matches `PATemplateMods` config(StrategyTuning)): `-arrMakeItemBuildable=(ItemName="MZImmolator_CV")`, byte copy of the source line. Effect: Basic Immolator infinite again, no longer buildable or sellable (it costs nothing anyway).

- The old 200+ stack lives in the old save only; the new campaign starts clean.
- Probe: Engineering / Build Items no longer lists Basic Immolator; HQ inventory shows it as infinite. Repro on a throwaway save (agent report): note the count, "Make weapons available" on a non-chemthrower soldier, leave the screen; count should stay put.
- Agent report (full trace): job tmp `immolator_report.md`, copied to `research-2026-10-29-immolator.md`.

## Not done

- No in-game or Launch.log verification yet: everything above is static (configs + simulation).
- Tertiary-ban releases that would revive Ravager, Savage, Brigand, SkvRaider, SwordMaster.
