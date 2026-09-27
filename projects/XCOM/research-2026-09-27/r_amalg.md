---
type: report
created: 2026-09-27
author: jep
project: XCOM 2 WotC campaign
---

# Amalgamation picks: dataset, rules, 15 more combos

Verdict: dataset recovered from the save (44 classes, 42 confirmed live in the 09-27 log). One rule dominates: every row of the class feeds a weapon he carries. 21 of 44 picks put the tertiary tree on the carried secondary weapon (7.2 expected by chance, 2.9x). 19 more pair an active device secondary (gremlin, grenade launcher, psi amp, BIT, arc thrower) with a utility tertiary. Only 4 of 44 break both patterns, and 2 of those are pistol doubles he ruled in on 09-18. Top 15 below: 12 use primaries he has never picked, and all 15 are in the live class deck and pass the 803 jepFixes pairs.

## 1. Dataset (how recovered)

- Log: `Launch.log` 09-27 (vault copy = Documents copy, 30,112,100 bytes). Amalgamation `LogDebug` prints `SOLDIER DEBUG: Soldier abilities <Primary> n <Secondary> n <Tertiary> n` per unit, where n = perks held from that spec. It lists 42 distinct triples. The 4 older logs (09-24 to 09-27) add none.
- Save: `save_AUTOSAVE- Campaign 30, Mission 14` (09-27 15:51, Geoscape). UE3 package, LZO1X blocks, magic `C1 83 2A 9E`. I decompressed it with a pure-python LZO1X in `lzo.py` (15,095,060 bytes, no block size mismatch) and parsed properties with `roster.py`: `strFirstName` / `strLastName` / `strNickName` come about 5 KB before `m_SoldierClassTemplateName`, and `m_SoldierRank` comes about 700 B after.
- Result: 44 Amalgamation classes. 42 match the log. 2 appear only in older history frames (Infantry_Valkyrie_CombatEngineer, Paramedic_rocketeer_Daeva) and are probably KIA or dismissed (unverified). 4 live units have no name in the save's delta frames.
- Bonus receipt: the save's HQ `SoldierClassDeck` = 2,519 Amalgamation classes, the actual offer pool. All 44 picks are in it. Current jepFixes rules block 8 of them (all Marathonist x Hotshot/rocketeer). I used this deck as the candidate universe.
- Offer model used for the null: Promotion Assistant shows one card per primary spec (09-17 report), with a uniform draw among that primary's classes. Expected counts below = sum over his 44 picks of each feature's share within that pick's primary. Limitation: the deck is today's. Rules changed 09-16 to 09-18, so earlier promotions saw a somewhat different pool.

| Class | Soldier | Rank | Weapons shown (P / S / T) | Archetype |
|---|---|---|---|---|
| ARFMTeslaTrooper_Dragoon_SkvArtisan | Brent Bowden 'Blowtorch' | Cpl | Tesla Rifle[Pri] / Gremlin[Sec] / Gremlin[Sec] | R1 stack |
| Adversary_Techspert_CombatEngineer | (no name in save) | Cpl | Sniper Rifle[Pri] / Gremlin[Sec] / - | R3 device+utility |
| Akimbo_gunslinger_Sentinel | Gershon Gavish 'Griffin' | Cpl | Pistol[Pri] / Pistol[Sec] / - | R3 other |
| AlienHunter1_Flamemancer_FieldSurgeon | Ruslana Remidova 'Roulette' | Cpl | Boltcaster[Pri] / PsiAmp[Sec] / - | R3 device+utility |
| Assault_Vengeance2_Riot | Percival Pegler 'Panzer' | Cpl | Shotgun[Pri] / Shield[Sec] / Shotgun[Pri] | R1 stack |
| Atrax_Burner_SkvFirebug | Neeraj Nedeesh 'Nitro' | Cpl | Vektor Rifle[Pri] / Gauntlet[Sec] / Gauntlet[Sec] | R1 stack |
| BattleAngel_ChryssalidWhisperer_FieldSurgeon | Hernando Hurtado 'Hermit' | Sqd | Bullpup[Pri] / Super Computer[Sec] / - | R3 device+utility |
| Desolator_Phoenix_TechMedic | Dawn Davenport 'Denmother' | Sqd | Chemthrower[Pri] / Chemthrower[Pri] / Empty[Sec] | R3 device+utility |
| Gunfighter_Hotshot_Daeva | Esperanza Estrada 'EZ' | Cpl | Pistol[Pri] / Pistol[Sec] / - | R3 other |
| Gunner_Grenadier_CombatEngineer | Clement Cervouis 'Cook' | Sqd | Cannon[Pri] / Grenade Launcher[Sec] / - | R3 device+utility |
| Gunner_SkvSiegeGunner_Liquidator | Hoon Choi Hee 'Helix' | Sqd | Cannon[Pri] / - / Sawed-Off[Sec] | R1 fills slot |
| Harbinger_SkvSiegeGunner_Blaster | Trisha Taggard 'Triclops' | Sqd | Cannon[Pri] / - / Claymore[Sec] | R1 fills slot |
| HareCaptain_HareBuckler_Smoker | Hermann Holtzer 'Hatchet' | Sqd | Sword[Pri] / Pistol[Sec] / Pistol[Sec] | R1 stack |
| HareFarseer_HareElectroWizard_Cryo | Gunhilda Gundersen 'GG' | Cpl | Sniper Rifle[Pri] / PsiAmp[Sec] / PsiAmp[Sec] | R1 stack |
| HareQuartermaster_HareSwash_Sentinel | Dagna Devrowski 'Dev' | Sqd | Pistol[Pri] / Sword[Sec] / - | R3 other |
| Impaler_Arcstrider_SkvMedic | Allegra Amaro 'Armada' | Sqd | Combat Knife[Pri] / BowCaster[Sec] / - | R3 device+utility |
| Infantry_HareWaterVein_Cryo | Heyla Holmers 'Hollow' | Cpl | Assault Rifle[Pri] / PsiAmp[Sec] / PsiAmp[Sec] | R1 stack |
| Infantry_Valkyrie_CombatEngineer (save only, not in 09-27 log) | (no name in save) | Cpl | Assault Rifle[Pri] / Gremlin[Sec] / - | R3 device+utility |
| Interceptor_SkvDemo_Retaliator | Einar Engstrum 'Eclipse' | Sqd | SMG[Pri] / Grenade Launcher[Sec] / - | R3 device+utility |
| Interceptor_Valkyrie_CombatEngineer | Shanice Siolo 'Slice' | Cpl | SMG[Pri] / Gremlin[Sec] / - | R3 device+utility |
| Jackhammer_DroneProtocol_FieldSurgeon | Jadwa Jebali 'Judge' | Sqd | Shotgun[Pri] / Gremlin[Sec] / - | R3 device+utility |
| Marathonist_HareGrimArtist_Smoker | Cormac Cullinfield 'Checkmate' | Sqd | Shotgun[Pri] / Pistol[Sec] / Pistol[Sec] | R1 stack |
| Maverick_Burner_heavy | Sergey Semyenov 'Slayer' | Lt | Assault Rifle[Pri] / Gauntlet[Sec] / Gauntlet[Sec] | R1 stack |
| MusaSamurai_LegendaryWarrior_SwordMaster | Donell Darby 'Deathwish' | Sgt | Sword[Pri] / Sword[Sec] / Sword[Pri] | R1 stack |
| Oddsman_Corpsman_KeeperTertiary | (no name in save) | Cpl | Sniper Rifle[Pri] / Autopistol[Sec] / - | R3 other |
| Paramedic_rocketeer_Daeva (save only, not in 09-27 log) | (no name in save) | Cpl | Chemthrower[Pri] / Rocket Launcher[Sec] / - | R3 device+utility |
| Pathfinder_Bloodmancer_FieldSurgeon | Kishida Kazehaya 'Katana' | Cpl | Hunter Rifle[Pri] / PsiAmp[Sec] / - | R3 device+utility |
| Pathfinder_ReconOfficer_Architect | Candice Callahan 'Calamity' | Sqd | Hunter Rifle[Pri] / - / Spire Gun[Sec] | R1 fills slot |
| Pioneer_Bombarder_Saboteur | Guadalupe Gortada 'Guardiana' | Sqd | Chemthrower[Pri] / Grenade Launcher[Sec] / - | R3 device+utility |
| Predator_ReconOfficer_Officer | Bracha Biton 'Bloodbath' | Sgt | Vektor Rifle[Pri] / - / Holotargeter[Sec] | R1 fills slot |
| PsiBlades_Stormmancer_KeeperTertiary | Tarika Tandekar 'Typhoon' | Sgt | Shard Gauntlets[Pri] / PsiAmp[Sec] / - | R3 device+utility |
| Ravager_Butterfly_Agent | Somsak Saetang 'Saber' | Lt | Sword[Pri] / Combat Knife[Sec] / Combat Knife[Sec] | R1 stack |
| Rookpressor_SkvSWAT_Retaliator | Satori Sujinoko 'Shinigami' | Cpl | Assault Rifle[Pri] / Arc Thrower[Sec] / - | R3 device+utility |
| Savage_Butterfly_Maniac | Kinianga Kelembo 'Kaboom' | Sqd | Sword[Pri] / Combat Knife[Sec] / Combat Knife[Sec] | R1 stack |
| Shadow_NinjaWarrior_SkvAssassin | Olga Ostapenko | Sqd | Vektor Rifle[Pri] / Sword[Sec] / Sword[Sec] | R1 stack |
| Shadow_Rogue_SkvScout | Lily Shen | Sqd | Vektor Rifle[Pri] / Pistol[Sec] / Pistol[Sec] | R1 stack |
| Shadow_Support_TechMedic | (no name in save) | Cpl | Vektor Rifle[Pri] / Grenade Launcher[Sec] / Empty[Sec] | R3 device+utility |
| Sharpshooter_BITpilot_Sentinel | Henriette Hilderbrand 'Hex' | Sqd | Sniper Rifle[Pri] / Spark BIT[Sec] / - | R3 device+utility |
| Toxicologist_CPUExpert_Daeva | Malee Mongkut 'Mayhem' | Cpl | Chemthrower[Pri] / Gremlin[Sec] / - | R3 device+utility |
| Toxicologist_Support_SkvMedic | Gloria Gallagher 'Glory' | Sgt | Chemthrower[Pri] / Grenade Launcher[Sec] / - | R3 device+utility |
| Veteran_Hotshot_Commissar | Warika Welvek 'Windwalker' | Sgt | Assault Rifle[Pri] / Pistol[Sec] / Assault Rifle[Pri] | R1 stack |
| Veteran_SkvSWAT_Engineer | Ettore Entonini 'Enforcer' | Sqd | Assault Rifle[Pri] / Arc Thrower[Sec] / Arc Thrower[Sec] | R1 stack |
| Vigilante_Ironclad_AegisDefender | Bessie Billcrest 'Blink' | Cpl | Pistol[Pri] / Shield[Sec] / Shield[Sec] | R1 stack |
| XenoZoologist_gunslinger_SkvScout | Genevieve Guillaume 'Gunpowder' | Sqd | Super Computer[Pri] / Pistol[Sec] / Pistol[Sec] | R1 stack |

Archetype counts: R1 stack 17, R1 fills slot 4, R3 device+utility 19, other 4.

## 2. Rules extracted (confidence, receipt)

- R1 weapon depth (high). The tertiary's weapon is one he already carries (stack), or it fills an empty secondary slot (Siege Gunner / Recon Officer + a tertiary that brings a weapon). Observed 21, expected 7.2. Stack alone: 17 vs 5.4. Triple-same-weapon: 4 vs 1.3. Receipt `rule1.py`.
- R2 generic passive tertiaries avoided (medium-high). Weaponless tertiary: 21 observed vs 32.0 expected. Sentinel 3/6.7, Retaliator 2/5.7, Keeper 2/5.3, Tech Medic 2/4.3, Saboteur 1/2.4. Receipt `speclift.txt`.
- R3 when the tertiary is utility, the secondary is an active device (medium, descriptive, no null computed). 19 of the 23 non-R1 picks have gremlin, grenade launcher, psi amp, BIT, arc thrower, rocket, bow or super computer secondaries. Tertiaries in that group: Field Surgeon 4, Combat Engineer 4, Daeva 3, Sky Medic 2, Tech Medic 2.
- R4 variety (medium). 36 distinct primaries in 44 picks vs 31.2 expected from uniform choice, and no Secondary+Tertiary pair repeats. 23 primaries in the deck remain unpicked.
- R5 exotic secondaries over common ones (low-medium, small n). Arc thrower 2/0.3, gauntlet 2/0.8, combat knife 2/0.9 above expectation. Pistol 7/9.2, Gunslinger 2/4.8, Blademaster 0/1.9 below.
- R6 sniper primaries under-picked (low-medium). 4 observed vs 7.5 expected. Six of the 23 unpicked primaries are snipers (Androctonus, ARFMFusil, Observer, Shootist, TankBuster, Survivalist).
- R7 doubled pistol shot tolerated when the kit is pure pistol (high, his ruling). jepFixes comment: "2026-09-18 Idi released the six doubled-pistol-shot pairs". Picks: Akimbo_gunslinger, Gunfighter_Hotshot.
- R8 element stacking (descriptive). Fire: Burner x2, Firebug, heavy, Flamemancer. Cold: Cryo x2 on psi amp builds. Electric: Stormmancer, Electro Wizard, SWAT+Engineer arc thrower, Tesla.
- Neutral: healing. 8 picks carry a medic tertiary, close to chance. He takes healing when it comes along but does not select for it.
- Unmeasured: 20 ability-tag families (crit, shred, mobility, action economy, stealth...) came out flat, observed within 15 % of expected (`lift.tsv`). My regex tags are crude, so "no signal" here means only that my tags don't pick one up.

## 3. Top 15 candidates (all in deck, unblocked, unowned, new Secondary+Tertiary pair)

Ranked by rule fit (R1/R3 plus R4 new primary), then my read of each ability tree. Heuristic score from `cands.py` in brackets. The trees in `picks_detail.txt` / `dump.py` support the one-line reasoning. None of this has been playtested.

1. Pistoleer_gunslinger_Commissar [10.1], new primary. Triple pistol: Quickdraw / Lightning Hands / Fan Fire / Faceoff + Commissar Hit and Run / Run and Gun + Magnum / Shootout. Mirrors his Veteran_Hotshot_Commissar. No doubled squaddie (Pistoleer starts with Lucky Day).
2. Juggernaut_Butterfly_Commando [9.0], new. Shotgun Run and Gun at squaddie, Hit and Run, Rapid Fire + double knife (heal-knife sustain, Fleche, Lone Wolf, Finesse). Mirrors his two Butterfly knife stacks.
3. Fusilier_Trickshot_Commissar [8.3], new. Pistol primary with elemental Fusil shots, Lightning Hands, Faceoff + autopistol Trickshot + Commissar (fires from pistol or autopistol, R7 exempt). Triple sidearm.
4. SAWGunner_SkvSiegeGunner_Executioner [5.7], new. Cannon Shredder / Hail of Bullets / Chain Shot / Kill Zone + Siege Demolition + sawed-off Point Blank / Both Barrels filling the empty slot. Same shape as his Gunner_SkvSiegeGunner_Liquidator. Risk: Shredder sits in both decks, so one rank-up may offer a duplicate.
5. BountyHunter_ReconOfficer_SkvAssassin [5.7], new. Nightfall concealment + Phantom + sword Stillness / Shadowstrike / Vanish filling the slot. Stealth assassin, same shape as his Recon Officer picks.
6. ARFMScav_Hotshot_Smoker [8.7], new. Vektor with Run and Gun / Phantom / Implacable decks + double pistol (bounty-hunter pistol perks + smoke kit).
7. savior_CombatMedic_SkvArtisan [7.6], new. Blood-magic self-sustain + double gremlin (Aid, Repair, Combat Protocol, Haywire). Mirrors his Tesla_Dragoon_SkvArtisan.
8. Dreadnought_SkvSiegeGunner_heavy [3.4], new. Salvo (grenades and heavy weapons don't end the turn) + Heavy Armaments rockets / flamer / Firestorm on the empty slot + Siege Kill Zone. The score is low because the tags miss the Salvo synergy. My read ranks it higher.
9. Marauder_ReconOfficer_Agent [6.0], new. Bullpup Skirmisher Strike / Hit and Run + Phantom + knife Slash and Dash / Perfect Plan / Hamstring.
10. Huntsman_Hotshot_Smoker [8.1], new. Rifle crit line (Precision, Anatomist, Lethal) + double pistol. A different primary from 6 on the same pistol pair; take one of the two.
11. Savage_ARFMPlunderer_SwordMaster [9.5], owned primary (1). Triple sword with Plunderer Bladestorm / Parkour / Phantom. Same shape as his MusaSamurai triple sword.
12. Akimbo_ReconOfficer_SkvScout [8.3], owned primary (1). Dual pistol + Phantom + Sky Scout pistol tree (Quickdraw, Lightning Hands, Fan Fire, Rapid Fire).
13. HareQuartermaster_SkvRaider_SkvAssassin [8.9], owned primary (1). Pistol primary + double sword (Bladestorm, Reaper, Implacable, Vanish).
14. TheRifleman_ReconOfficer_Commando [6.5], new. Rifle + Phantom + knife on the empty slot. The only R1 combo in that primary's 44 classes.
15. Androctonus_SkvStygian_SkvScout [9.6], new. Squadsight + Snap Shot (legal, sniper-only perk on a sniper) + Deadeye / In the Zone + pistol stack. Conflicts with R6 (he under-picks snipers). Listed as the one sniper worth a look.

Primaries without an R1 combo in the deck (Observer, Shootist, TankBuster, GhostRecon, Wrecker, Salamander): the best R3-shape cards there are device + utility at most. See `shortlist.tsv`.

## 4. Gaps

- Pick intent unverified. Some early picks (Sgt+ ranks) may predate Promotion Assistant or the 09-16 rules, or came from GTS training.
- The null assumes one uniform card per primary. If the Assistant weights classes differently, the expected counts shift.
- Effectiveness is judged from ability names and decks. Rank-up deck draws are random, so a combo's realised build varies.

## Files (C:\Users\jep\.claude\jobs\d60d4ae0\tmp)

`lzo.py`, `roster.py` (save decode) · `roster_amalg.tsv` (44 picks) · `pool_save.txt` (2,519-class deck) · `specs.py` → `universe.json` (167 specs, 523 decks, 10,709 exclusion pairs of which 801 jepFixes) · `tags.py`, `lift.tsv`, `speclift.py/.txt`, `rule1.py` (rules) · `cands.py` → `cands_ranked.tsv`, `shortlist.py/.tsv` (candidates) · `picks_detail.txt`, `picks_summary.txt`, `dump.py` (ability trees). `save_c30m14.bin` = decompressed save, 15 MB, can be deleted.
