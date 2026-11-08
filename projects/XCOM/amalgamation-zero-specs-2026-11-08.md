---
type: decision
created: 2026-11-08
author: jep
---
# Amalgamation: zero-card specs, case by case (Idi rules by index)

Idi 11-08: no spec may sit at 0 cards; each gets a ruling from what it was built for. Deck now 1,497 classes. Counts = simulated cards (section-aware simulator over every active `XComAmalgamation.ini`). "Built for" = the author's Steam text + the spec's ability list.

Rule names: W1 sword P <-> sword S; W2 pistol P <-> pistol S; W6 shield S <-> shield T (10-29). R2 secondary and tertiary carry different secondary-slot weapons; R3 secondary/tertiary lists a primary weapon the primary lacks (09-16).

## Cases

| # | Spec | Built for | Why 0 | Options -> cards | jep |
|---|---|---|---|---|---|
| Z1 | Ravager (P, Stukov's Fusilier and Ravager) | brute-strength melee, sword or glaive primary; Mitzruti Sabre perks (Flame/Frost/Storm Sabre, Sabrestorm, Sweeping Spin); its config lists an EMPTY secondary | W1; and R2 kills it with every sword secondary (its tertiaries carry knife, arc thrower, sawed-off) | A empty-slot secondary (Recon Officer; the tertiary weapon fills the slot) -> 5. B full W1 exemption -> 7 (adds Butterfly knife) | A |
| Z2 | Savage (P, Savage & Maniac) | high-end melee primary; author: "can use Sword as a primary, and allows Combat Knife as a secondary"; Run And Slice, Bladestorm, Hamstring | W1 | A knife secondary (Butterfly) -> 2. B full W1 exemption -> 3 | A |
| Z3 | Brigand (S, Stukov) | stealth ambusher, "unloading buckshot into their spines"; 8 perks fire from the primary slot, sword is the side weapon | W1 (sword secondary needs a sword primary; sword primaries fail its tertiaries) | A under shotgun primaries (Assault, Juggernaut, Veteran) -> 5 = full exemption | A |
| Z4 | SkvRaider (S, Richard's Classes) | ranger-style melee secondary, sword or knife under a gun: Slice, Bladefighter, Combatives, Sidearm Specialist | W1 | A exempt from W1 -> 23 | A |
| Z5 | SwordMaster (T, Dragontoast) | sword-and-board duellist: Duel, Parry, Guard, Blade Grasp, Last Stand; kit = sword primary + shield or sword secondary | W6 (shield tertiary needs a shield secondary) and W1 (sword primary needs a sword secondary) close both of its kits | A may sit with sword secondaries -> 9. B sword primaries may take shield secondaries -> 2. A+B -> 11 | A+B |
| Z6 | Xeno Zoologist (P) | supercomputer gauntlet that spawns and commands alien units; author keeps it "somewhat a rare spec", partners: gremlin, BIT, pistol, autopistol, holotargeter, arc thrower | its author's only tertiaries carry weapons (Officer, Engineer, SkvScout), so R2 kills them under a gremlin; the one survivor (Gunslinger + SkvScout) died to W2 | A pistol/autopistol secondaries allowed -> 1 | A |
| Z7 | Xeno Zoologist Monster Master (P) | same author and design, melee monsters (Devour, Quake, Running Bash) | same as Z6 | A -> 1 | A |
| Z8 | Maniac (T, Savage & Maniac) | knife tertiary, survival + single-target melee: Lacerate, Butcher, Parkour, Devil's Luck | lives only on Savage + Butterfly | follows Z2 A -> 1 | follows Z2 |
| Z9 | Androctonus (P) | patient long-range sniper; escapes close range by agility and elevation; its author pairs it only with pistol/autopistol or melee secondaries | 0 since 09-28: Idi's sniper whitelist (gremlin, GL, psi, bio, BIT) and its author's list never overlap; W2 also blocks the pistol | A pistol/autopistol secondaries allowed for Androctonus (Firaxis's own sniper + pistol) -> 26 | A |
| Z10 | AlienHunter2 (S, Stukov's Alien Hunter) | axe/sword hunter, bonus damage per alien type (Hunter of Vipers, Archons, Mutons...), Executioner, Bladestorm; author: "suggest equipping with Boltcaster ... for style points" | 0 since 09-16: **jep error**, R3 read the suggested bolt caster as a demand; now also W1 | A X1 + AlienHunter2 exempt from W1 -> 10 | A |
| Z11 | DronePilot (S, Dragontoast) | gremlin/BIT drone buffs and debuffs: Combat Scanner, Barrier Protocol, Haywire, Chaining Jolt; lists a pistol as an optional primary | 0 since 09-16: **jep error**, R3 read the optional pistol as a demand; 0 of its perks touch the primary slot | X1 -> 52 | X1 |
| X1 | R3 fix (jep bug, cross-cutting) | R3 keeps only specs whose trees fire from the primary (Brigand, SkvSiegeGunner, Phoenix) | dropped for AlienHunter2, DronePilot, SwordMaster, Riot, Ironclad, LegendaryWarrior; W rules stay intact | deck +63: DronePilot 0->52, Ironclad 1->10, Riot 2->7, AegisDefender +4 | yes |
| X2 | Weight rare classes (not built) | Choose My Class gives each class `NumInDeck` tickets (`UIChooseClass_WOTC_ChooseMyClass.uc:372`); a small jep script mod could give chosen classes 2-3 tickets | the 8 weaponless tertiaries hold ~85 % of the deck (Sentinel 264, Retaliator 249 cards) | e.g. weapon tertiaries x3 -> Architect ~3x more often | after you play with 100 offers |

All jep recommendations together (Z1 A, Z2 A, Z3 A, Z4 A, Z5 A+B, Z6-7 A, Z9 A, Z10 A, X1): deck 1,497 -> 1,645; specs at 0: only Commissar (your ruling). Still 1 card: HareSwash, Maniac, Phoenix, both Xeno Zoologists.

## Applied 11-08 (no ruling needed)

- Choose My Class offers 50 -> 100 (jepFixes `XComChooseMyClass.ini`). Each class's chance per promotion roughly doubles.
- 22 out-of-date pairs removed from jepFixes `XComAmalgamation.ini` (they named Arcstrider, Vindicator, ARFMTeslaTrooper, all disabled); simulated deck identical before and after.
- Kept on your word: gremlin-tertiary rule covers HareModernPirate; P1c list stays deleted.

## Odds per promotion, weapon tertiaries (current deck, 50 -> 100 offers)

| Tertiary | Cards | 50 | 100 |
|---|---|---|---|
| Riot, SkvAssassin, SkvClay | 2 | 6.6 % | 12.9 % |
| Architect | 3 | 9.7 % | 18.7 % |
| Biotic, SkvFirebug | 4 | 12.7 % | 24.2 % |
| AegisDefender | 5 | 15.6 % | 29.3 % |
| Heavy, Blaster, SkvScout, Smoker | 7 | 21.2 % | 38.4 % |
| Executioner | 8 | 23.8 % | 42.6 % |
| Agent, Liquidator | 9 | 26.4 % | 46.4 % |
| Officer | 11 | 31.3 % | 53.4 % |
| Engineer | 13 | 35.8 % | 59.4 % |
| Commando | 15 | 40.1 % | 64.7 % |

- Draw model: one ticket per class, drawn without replacement (`UIChooseClass_WOTC_ChooseMyClass.uc:365-378`); hypergeometric odds over 1,497 tickets. X1 and Z rulings change the card counts.
- Tools: `amalgamation-tools/zero.py`, `zero2.py`, `zero3.py` (block chains), `opt.py`, `combo.py` (option pricing), `cleanup.py`.

## Ruled 11-08: "all rec" (installed)

Z1 A, Z2 A, Z3 A, Z4 A, Z5 A+B, Z6-Z7 A, Z8, Z9 A, Z10 A, X1. 121 jep pair lines deleted from jepFixes `XComAmalgamation.ini` (comment block dated 11-08 lists them by rule). Real file simulates to the priced deck exactly: 1,645 cards; only Commissar at 0.

## X2 priced 11-08 (not built; awaits the word)

Mechanism: a small jep script mod (`jepClassWeights`, same build path as jepGTSFilter) sets each Amalgamation class's `NumInDeck` (= its Choose My Class tickets) after Amalgamation's own DisableClass pass; classes at 0 stay 0. Template Master cannot do it (no soldier-class editing).

| Scheme | Tickets per class | Weaponless tertiaries' share of offers | Promotions to see all 141 specs (median / worst of 40 runs) | 1-card classes per promotion |
|---|---|---|---|---|
| now | 1 | 84 % | 31 / 73 | 6.1 % |
| T: by tertiary rarity | 299 / cards of its tertiary, cap 50 | 28 % | (all 32 tertiaries: 2 / 6) | Phoenix, HareSwash get rarer; Recon Officer 20 % of offers |
| T + secondary cap 8 % | same, secondaries above 8 % scaled down | 33 % | (all 32 tertiaries: 3 / 13) | rare primaries/secondaries still starved |
| **R: by rarest spec (jep rec)** | rarest of its three specs sets the boost, cap 50; secondaries capped at 8 % | 51 % | **6 / 11** | **35.3 %** |

- Simulation: Choose My Class draw model (one ticket per NumInDeck, a class shown once per offer), 100 offers, 40 seeded runs. Tool: `amalgamation-tools/weights5.py`.
- Weights take effect at the next launch, mid-campaign included (template values, nothing stored in the save).
- Risk: NumInDeck also feeds the HQ random-class deck; Choose My Class hides the plain promote button, so no visible effect expected (medium confidence).

## Installed 11-08 evening (Idi: cut what he'd never pick + build X2)

- Cut, rule D4: within each primary+secondary pair keep only the best tertiary tier (A weapon > B utility > C passive/healing); a passive-only pair keeps one card, passive before healer, rarest first. 1,034 `+DisableClass` names in jepFixes `XComAmalgamation.ini` (new section at file end). Deck 1,645 -> 611; every spec keeps >= 1 card (only Commissar at 0). Real file simulates to the D4 set exactly.
- jepClassWeights script mod: local `Mods\jepClassWeights`, AML active (only that entry added). Weights from `weights5.py` on the 611 deck: 4,292 tickets, cap 50. Simulated: all 141 specs within a median of 5 promotions (worst of 40 runs 7); before today 31 / 73. Source + build/install scripts in vault `projects/XCOM/jepClassWeights/`. Compiled 0 errors (8 SDK base warnings).
- Pick sheet for alt-tab: `pick-sheet.md`.
- Probes, first launch (Launch.log): `Amalgamation DLCINFO INFO: Disabled classes 1294`; `jepClassWeights: set 611 classes, skipped disabled 0 , missing 0 of 611`. A mod change means regenerating the cut and the weights (cuts.py, applycut.py, weights5.py, genweights.py).
