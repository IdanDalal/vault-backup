---
type: reference
created: 2026-09-28
author: jep
---
# Amalgamation pick rules (Idi's, ruled 2026-09-28)

Source: jep's extraction from 44 picks in Campaign 30 (`research-2026-09-27/r_amalg.md`), corrected by Idi 2026-09-28. Use at every rookie promotion.

## Rules

- R1 weapon depth: every tree feeds a carried weapon. Tertiary stacks on a weapon already carried, or fills an empty secondary slot.
- R2 generic passive tertiaries (Sentinel, Retaliator, Keeper, Tech Medic, etc.): low priority; pick only where they harmonize with / support the primary and secondary.
- R3 utility tertiary rides with an active-device secondary (gremlin, grenade launcher, psi amp, BIT, arc thrower, etc.).
- R4 variety: as many unique primaries as possible; no repeated secondary+tertiary pair.
- R5 exotic secondaries (arc thrower, gauntlet, knife) over pistols, generally. Pistol classes: best picked for pistol-only combos.
- R6 sniper primaries: under-picked because the deck keeps pairing them with short-range secondaries. Good and bad pairs below.
- R7 doubled pistol tolerated in pure-pistol kits.
- R8 healing never sought, only accepted; great when it combines in harmony with the other two trees.

## Sniper pairings (R6)

Why: a sniper rifle cannot fire after moving (vanilla, needs both actions), and squadsight shots come from far behind the line. The secondary should add value from the sniper's own tile, or fill the turns the rifle cannot fire. jep reasoning from vanilla rules, medium confidence, not playtested.

Deck receipt, 2026-09-27 pool (2,519 classes, 469 with a sniper primary, 10 sniper primaries: Adversary, Androctonus, ARFM Fusil, Farseer, Observer, Oddsman, Sharpshooter, Shootist, Survivalist, Tank Buster):

| Secondary weapon | Sniper cards | Fit | Why |
|---|---|---|---|
| Gremlin (Drone Protocol, Combat Medic, Techspert, Dragoon, CPU Expert, Valkyrie) | 106 | best | Aid, scan, Combat Protocol, Haywire at range; uses the turn the rifle sits idle |
| Grenade launcher (Support, Grenadier, Bombarder, G. Connoisseur, Demo) | 51 | strong | long-range cover strip / shred that sets up the rifle shot; no move needed |
| Psi amp (Enchanter, Water Vein, the -mancers, Electro Wizard) | 46 | strong | range-agnostic casts from the back line |
| BIT (BIT Pilot) | 26 | strong | drone acts at range, sniper stays put |
| Rocket, super computer | 7 | good | same logic, few cards |
| Pistol / sidearm (Gunslinger, Grim Artist, Hotshot, Stygian, Buckler, Corpsman, Trickshot) | 139 | Firaxis's own answer, weak under R5 | vanilla Sharpshooter = sniper + pistol: the pistol fires after moving and covers close threats; clashes with R5 unless the pistol tree carries it |
| Sword, knife, wrist blade (Blademaster, Corsair, Plunderer, Ninja, Swash, Butterfly, Raider, Ripper) | 72 | bad | pulls the sniper forward, off its squadsight tile |
| Arc thrower, flame gauntlet (SWAT, Burner) | 8 | bad | short range |
| Empty slot (Recon Officer, Gripsman) | 14 | depends on tertiary | R1: the tertiary should bring a ranged or device weapon |

On a 50-card offer, about 9 are sniper cards; about 4.5 of those are the four strong pairings above.

## Enforced in jepFixes (new campaigns only)

- **R6, installed 2026-09-28 on Idi's word:** sniper primaries only with gremlin, grenade launcher, psi amp, bio amp (Biotic tertiary via an empty slot) or BIT. 420 new `IncompatibleSpecs` pairs in jepFixes `XComAmalgamation.ini` (803 -> 1223, prior lines byte-identical): sniper x 27 secondaries with any other displayed weapon, sniper x 16 tertiaries that put any other weapon in the secondary slot. Empty-slot secondaries stay so Biotic (or a gremlin/psi tertiary) can fill them. Deck simulation: sniper cards 469 -> 230, all 229 gremlin/GL/psi/BIT sniper cards kept.
- Literal whitelist side effect: 10 sniper cards with unlisted ranged gear also go (Officer holotargeter 2, Rocketeer 2, Chryssalid Whisperer super computer 5, Blaster claymore 1). His Campaign 30 pick Oddsman / Corpsman / Keeper (sniper + autopistol) is now excluded by his own rule.
- Earlier rules still in force: 09-16 R1 no-weapon secondary x no-weapon tertiary, R2 (file B) two different secondary weapons, R3 foreign primary weapon, R4 same squaddie skill twice; 09-17/18 displayed-weapon rules.

### Round 2, 2026-09-28 (Idi's rulings)

- **Placement fix (jep error):** the first R6 install appended the 420 pairs at the end of the file, inside the `[AmalgamationPexmBridge...]` section, where Amalgamation never reads them. Moved into `[AmalgamationClassesWOTC.X2SoldierClass_Amalgamation]`; check = same lines, reordered only. Other 09-26/27 appends checked: correct sections.
- **Released for snipers:** Officer (holotargeter, acts from the sniper's tile) and Chryssalid Whisperer (summons a Chryssalid; every perk text reads "Your Xeno...", so the soldier stays put). 20 pairs removed. Rockets stay excluded. Pairs now 1203.
- **P1c installed:** a pistol or autopistol secondary only with a pistol primary or a pistol tertiary (SkvScout, Smoker; Commissar counts). Pairs cannot express a three-spec rule, so the 350 offending classes are listed by exact name under `+DisableClass=` (section `[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]`). DisableClass sets NumInDeck 0; Choose My Class offers only NumInDeck > 0 (`UIChooseClass_WOTC_ChooseMyClass.uc:355`); the one other listener on that check touches only Denmother's Keeper. Medium-high: untested in game.
- Deck simulation (09-27 pool): 2,519 -> 2,287 after R6 -> 1,937 after P1c. Sniper cards 237. His 44 picks hit: only Oddsman / Corpsman / Keeper (his words: bad luck, no better option).
- Limit: the DisableClass list is built from the 09-27 deck. A spec added later by a new mod needs a regenerate (`amalgamation-tools/p1c.py`).
- Probe, first launch: `Amalgamation DLCINFO INFO: Disabled classes 441` (09-27 log: 91, plus 350); `No class template` errors stay at 42 (09-27 count, other mods' lists).

### Verification pass, 2026-09-28 (four read-only audit agents; reports in the job tmp, v_A..v_D.md)

- Fixed: jepFixes `XComLootPostMover.ini` had the 09-15 expiry keys under the DLCInfo section; the class that reads them is `XComGameState_LootDropSplitter` (config LootPostMover). Loot expiry 3/3 never applied in Campaign 30 (psi loot stayed at 2). Header corrected.
- Fixed: one exact duplicate pair line removed (1202 pairs); stale "230" comment updated to 237; misleading jepReusePCS config comment corrected.
- Open, needs Idi: the Promotion Assistant's GTS alternative (`bEnableGTSAlternative=true`, `UISL_AmalGTS.uc:16-94`) picks one class per primary from its own hash and ignores NumInDeck, so P1c-disabled classes can appear on the GTS rookie-training screen. Choose My Class promotions honour P1c. R6 (pairs) holds everywhere.
- Checked, no action: MEC-spec pairs from 09-16 are inert (the MEC generator only combines its own specs, so those combos never exist); ELR ResidentEvilLeaders blank line is inherited from UECP and its units are not installed; ARFM Gameplay Mutators adds its own story Chosen strengths (Dedication/Aspect) by strategic action, outside the random pool the whitelist governs.
- Only in-game proof remains: first-launch log lines listed above plus `jepReusePCS: bReusePCS set`.

## Proposals (tested against his 44 picks; P1c and P2-holotargeter installed in round 2)

| # | Rule | Deck cards removed | His picks it would have removed | jep |
|---|---|---|---|---|
| P1 | pistol secondary only with a pistol primary | 396 | 6 | reject: too strict |
| P1c | pistol secondary only with a pistol primary or a pistol tertiary (Commissar counts, its perks fire from the pistol) | 350 | 1 (Oddsman / Corpsman, already banned by R6) | recommend: R5 as he worded it |
| P2 | release holotargeter + rocket for snipers (unlisted ranged gear) | adds back 4 | 0 | optional |

- R2 and R8 (passives and healing only "in harmony") are judgment calls; a pair rule cannot see harmony, and the only mechanical form (passive tertiary with a weapon-less secondary) is already banned by the 09-16 R1: 0 cards left to cut.
