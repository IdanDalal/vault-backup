---
type: report
created: 2026-09-16
author: jep
project: XCOM 2 WotC campaign
status: active
---

# Amalgamation combo curation: what the screenshots show, what the config can enforce

Sources: 96 active Amalgamation mods (base 2428993550 plus specs, Stukov's Exclusions 3088875530, Amalgamation+, Console Helper 2886967900, Promotion Assistant 3313946064). Every active `XComAmalgamation.ini` parsed, subfolders included. Candidate files: `amalgamation-exclusions-A.ini`, `amalgamation-exclusions-B.ini` (this folder).

## Mechanism

- A class = one Primary spec + one Secondary spec + one Tertiary spec. Each spec declares AllowedWeapons per slot. The class card shows each spec's squaddie weapon: "Sword + Empty Slot" = Samurai (sword) + Gripsman (declares weapon type `empty`) / Keeper (declares nothing).
- The only curation key: `+IncompatibleSpecs=(A=, B=)` in `[AmalgamationClassesWOTC.X2SoldierClass_Amalgamation]`. Any order, any pair of slots (Console Helper's ListRedundantSpecExclusions confirms cross-slot use). No weights, no per-spec probability, no three-way rule. Base mod: "To get other classes to appear more frequently you will need to increase their NumInForcedDeck" per class, not per spec.
- Installed today: 66 primary, 51 secondary, 41 tertiary specs. 138,006 theoretical combos, 8,874 exclusion pairs already active (Stukov 3,144, Drumax 1,096, Harehnoth 584, Amalgamation+ 409), 29,088 combos survive.
- Class list at promotion: jepFixes ChooseMyClass = 30; Promotion Assistant draws one class per primary spec.

## The five issues, mapped

1. No secondary weapon (A, Samurai-Gripsman-Keeper). Rule R1: secondary spec with no secondary weapon (Gripsman, Recon Officer, Siege Gunner) x tertiary with none (Keeper, Saboteur, Daeva, Field Surgeon, Retaliator, Sentinel, Tech Medic, Combat Engineer, the 8 MEC specs, Sootsman, Medic). 54 pairs. Over-excludes the 14 primaries that carry their own secondary; accepted.
2. Two secondary weapons (A, Sharpshooter-Support-Assassin: grenade launcher and sword). Rule R2: secondary x tertiary whose secondary-slot weapon types are disjoint. 1,033 pairs; 71 pairs share a type and stay (pistol + pistol, sword + sword, gremlin + gremlin), which is the "3 rows on 2 weapons" ideal. Share today: 9,178 of 29,088 surviving combos, 31 %. A four-card sample showing 3 of 8 is inside that rate.
3. Same as 2.
4. Assault rifle "as secondary" (B, Alien Hunter-Support-Commissar). Commissar declares rifle in the PRIMARY slot, so the card lists a second primary weapon, not a secondary. Rule R3: secondary/tertiary spec demanding a primary-slot weapon the primary spec cannot use. 531 pairs. Commissar under Infantry or Rifleman survives, which is the stated ideal. Nine specs do this: AlienHunter2, Brigand, Phoenix, DronePilot, LegendaryWarrior, Ironclad, Riot, Commissar, SwordMaster.
5. Same squaddie skill twice (C, Shadow-Recon Officer-Scout: Phantom). Rule R4: two specs of different slots with the same fixed rank-0 skill. 13 pairs: Shadow/ReconOfficer/MecInfiltrator (Phantom), Gunslinger or Hotshot x Gunfighter/Vigilante/Akimbo (pistol shot), Marauder x MecDervish (Skirmisher Strike), Techspert or SkvArtisan x MecDisruptor (Haywire), Brigand x GhostRecon (Shadow). Seven specs have a random rank-0 deck instead of a fixed skill (Veteran, LegendaryWarrior, Ironclad, Riot, SwordMaster, GrimArtist, ElectroWizard) and cannot be ruled.

Repetition: with 41 tertiaries and a 30-class list, repeats are certain (30 draws from 41). With 4 visible cards, one repeated tertiary has about 21 % odds per screen. The parse found no weighting anywhere, so the distribution is uniform over surviving classes; rare-looking specs are rare only because their pairs are excluded by Stukov-style rules. Unverified against a generated-class log; the mod does not write one.

## Options

| File | Rules | New lines | Combos left | Two-secondary combos |
|---|---|---|---|---|
| today | existing 8,874 | 0 | 29,088 | 9,178 (31 %) |
| A | R1 + R3 + R4 | 237 | 25,126 | 7,950 (31 %) |
| B | R1 + R2 + R3 + R4 | 714 | 17,176 | 0 |

Recommendation: B. 17,176 coherent combos is no scarcity, and every card then passes all five rules. Risks: 714 more pairs on top of 8,874 (load-time cost unknown, Console Helper `RollSpecs 50` after launch is the probe); new campaign required; the 7 random-deck specs can still double a squaddie skill.

Install (jep, on the word): copy the chosen file to jepFixes as `XComAmalgamation.ini`, mirror, launch, `RollSpecs 50` in the console, read 50 cards against the five rules.

## Installed 2026-09-16 (Idi ruled B)

- `jepFixes\Config\XComAmalgamation.ini` = file B, 716 pairs, trailing rule tags stripped (plain `+IncompatibleSpecs=(A="x", B="y")` lines only). Mirror identical.
- Probe after the next launch, in the console (Amalgamation Console Helper): `FindBlockedClasses Shadow ReconOfficer any` must list classes as blocked (rule R4), `RollSpecs 50` must show no empty-slot, no two-different-secondary, no foreign-primary, no doubled-squaddie cards. Then `Launch.log` for `IncompatibleSpecs` parse warnings.
- Idi's stance: more rules welcome later; four digits of combos is still abundance.

## 14:45 receipt and rule 6 proposal

- Log 14:30 (presets removed, 1118 mods): no crash, no GC failure through Gatecrasher, return, and a tactical reload. Amalgamation debug: 84,373 "Incompatible combination of specs" checks, 91 disabled classes. Option B is live. `LogDebug` stays on until the next edit is verified.
- Rule 6 (Idi, screenshot 3: Vindicator - Enchanter - Sentinel, shard gauntlets + psi amp, Sentinel squaddie): overwatch-flavored secondary/tertiary spec on a primary spec whose primary-slot weapons contain no firearm. Pistol secondaries do not rescue a class, since vanilla overwatch needs the primary weapon.
- 15:00 Rule 6 installed: 10 pairs (9 MecJaeger, plus Vindicator x Sentinel; Stukov's set already covered the rest). File now 726 pairs, mirrored, candidate B updated.
