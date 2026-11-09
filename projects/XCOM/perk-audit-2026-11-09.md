---
type: report
created: 2026-11-09
author: jep
---
# Perk audit: cards whose perks die in missions (2026-11-09)

Trigger: Idi's four screenshots after Gatecrasher (Swash, Marathonist, Phoenix, Samurai/Ninja). Root cause: every jep rule so far modelled weapons from each spec's AllowedWeapons. The game deletes perks by two other mechanisms that jep never read.

## How a perk dies (source-verified)

| Mechanism | Rule | Source |
|---|---|---|
| Ability To Slot Reassignment 2133397762 | perk listed with a weapon set and no inventory item of that set -> removed at mission start | `AbilityToSlotReassignmentLib.uc:164-255` |
| Musashi's Mods Fixes 2569592723 | merges same-name sets and every set a perk is listed under (union); widens Rapid Fire, In The Zone, Sharpshooter Aim, Demolition to all main weapons | `X2DLCInfo_WOTCMusashiModFixes.uc:341-536` |
| Amalgamation AbilityRestrictions | perk removed unless the weapon in a named slot has a named category (any entry) | `X2DownloadableContentInfo_AmalgamationClassesWOTC.uc:285-340` |

Audit = every card x every loadout the class allows (one primary + one secondary weapon); best loadout kept. Tool: `amalgamation-tools/audit.py`.

## Idi's four cases

| # | Card | Verdict | Fix |
|---|---|---|---|
| 1 | Captain - Swash - Sootsman | broken: squaddie Buckle Your Swash needs a pistol, card has two swords | cut; Swash now rides pistol primaries (Fusilier, Quartermaster, Pistoleer): its author built it as the sword half of a swashbuckler |
| 2 | Marathonist - Alien Hunter - Sentinel | works with a sword secondary; the card label prints Alien Hunter's first-listed weapon (bolt caster) | none; label note in `pick-sheet.md` |
| 3 | Desolator - Phoenix - Tech Medic | works: chemthrower + canister; Medishot is explicitly allowed on chemthrowers by the Tech Medic author | none; label note |
| 4 | Samurai - Ninja Warrior | Assassin was blocked by the Samurai author's ban | released; card now in the deck |

## Similar or worse cases found (all fixed)

- Config collisions killing guaranteed perks on EVERY card of a spec: Pathfinder Slam Fire (Sentry and Drumax restrict it to a rifle; hunter rifle is its own category), Rook Nimble Hands (only weapon entry is a SPARK-rifle set from a Modular Sparks mod), Maniac Fearsome (same Sentry/Drumax restriction), Agent Hamstring (Savage restricts it to a sword primary; Agent's is a knife perk). Fixed in jepFixes: 35 `AbilityRestrictions` lines (`XComAmalgamation.ini`), 1 line in new `XComAbilityToSlotReassignment.ini`. Owners' own rifle/sword specs behave as before.
- Broken classes: 152 of 1,645 before the fixes -> 11 after (10 Field Surgeon cards under bolt caster or sword primaries: the Tech Medic author excludes those on purpose; Swash's card). All 11 are cut.
- Perfect-tertiary blocks: 94 pairs (88 author bans, 6 jep) were the only thing blocking a WORKING tier-A card for a primary+secondary pair that had none. Released (113 byte-copied author lines, 9 jep lines). Effect: tier-A cards 211 -> 492.
- Cut rebuilt from scratch on the audit: deck 751 cards, 0 with a dead guaranteed perk; every spec >= 1 card (>= 3 where 3 working cards exist); only Commissar at 0 (your ruling). 1,443 `DisableClass` names.
- Random-roll perks: 550 cards fully clean; 201 have >= 1 optional perk that would die (most: Shadow Ops Assassin 57, Roving Chemist 31). Not cut: the promotion tooltip's yellow weapon list shows it; rule added to the pick sheet.
- Weights regenerated for 751 cards: all 141 specs within a median of 5 promotions (worst of 40 runs 8).

## Safety for the running campaign

- No class template removed: all 1,645 earlier classes still build (1,934 now). Today's edits only release pairs, add perk restrictions and change DisableClass (NumInDeck 0 keeps the template). Promoted soldiers keep their class; perk fixes apply at the next mission.

## Not verified

- No in-game check. Model confidence: medium-high (source read for all three mechanisms; load order rule proved 09-14). The reassignment mod logs only in debug builds, so no log receipt exists for perk removal.
- Probes, next launch: `Disabled classes 1443`; `jepClassWeights: set 739 classes, skipped disabled 0`. In a mission: a Pathfinder has Slam Fire, a Rook has Nimble Hands, an Agent has Hamstring.
- Card label stays cosmetic-wrong for Alien Hunter, Phoenix, Riot, SwordMaster (fixing it means rewriting four authors' spec entries; not worth the risk).

## 11-10 round (Idi's screenshots + rulings)

- SwordMaster on Marauder - Vengeance 2.0: works fully with bullpup + shield (0 dead perks); "/ Sword" is SwordMaster's first-listed weapon on the label.
- Raider: a combat knife keeps every perk (a sword loses Slash and Dash); "/ Combat Knife" on those cards is the tertiary's knife (Commando, Agent).
- NEW rule (Idi): no two specs sharing a guaranteed starting perk. Cut 26 cards (12 Fire Pistol, 14 Haywire Protocol). Reversible on his word.
- Floor now adds cards only from NEW primary+secondary pairs: Veil Walker - Water Vein - Keeper and Samurai - Corsair - Keeper gone (Frostmancer / Assassin stay).
- Rare alternatives, one card each: Impaler - Vengeance 2.0 (Ironclad loses 2 random-roll perks); Salamander - Bombarder (Rocketeer has 7 perfect cards elsewhere, Bombarder 0); Xeno - Gunslinger and Xeno MM - Hotshot (tie: split); Infantry - Gripsman (tie, scarcer); Predator - Clayman (tie, scarcer).
- Deck 751 -> 709; 0 broken, 0 shared starting perk, only Commissar at 0. DisableClass 1,485. Weights 699 classes, all 141 specs in a median of 4 promotions (worst 7). Probes: `Disabled classes 1485`, `jepClassWeights: set 699`.

## 11-10 second round (Idi: canister slot, empty secondaries, Marathonist)

- Canister: a chemthrower opens Mitzruti's aux slot for its canister (`MZ_StrategyElement_MZAuxSlot.uc:84`, Idi's in-game observation for all chemthrower classes). Audit (`audit2.py`) now gives a chemthrower its canister for free and never counts a canister as the secondary weapon.
- NEW rule (Idi): no card without a real secondary weapon. It removed one card (Desolator - Phoenix - Tech Medic). Phoenix revived by deleting 6 jep 09-16 R2 pairs that treated its canister as a secondary weapon: 11 Phoenix cards now (Desolator/Salamander x Agent, Commando, Engineer, Executioner, Liquidator, Officer), all with a weapon tertiary in the secondary slot.
- Equip lines: tie-break now prefers each slot's own spec weapon (the 11-09 sheet said pistol + empty slot for Quartermaster - Corpsman - Sootsman because "empty" sorted first; correct: pistol + autopistol).
- Marathonist: its own config lists shotgun and bullpup; no perk dies with either; the bolt caster came from Alien Hunter's list.
- Salamander - Rocketeer - Saboteur stays cut as Idi's explicit ruling (Salamander gained Phoenix cards, so the rare-pair rule no longer caught it).
- Deck 709 -> 719; 0 broken, 0 shared starting perk, 0 empty secondary, only Commissar at 0; no class template lost (1,945 build). DisableClass 1,486; weights 709 classes, all specs in a median of 5 promotions (worst 8). Pick sheet regenerated without ticks (Idi starts fresh).
