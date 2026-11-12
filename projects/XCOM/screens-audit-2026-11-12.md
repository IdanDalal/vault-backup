---
type: report
created: 2026-11-12
author: jep
---
# Six screenshots, 2026-11-12: findings, one fix applied, four rulings wanted

Source: `D:\work\screens\XCOM\1_COVERT.png` to `6_SENTINEL.png` (taken 11-09 to 11-11). Method: read each perk's source code and config, re-ran the card audit, simulated every proposed change before listing it. Nothing below was tested in the game by jep; "source" means read in the mod's code, "log" means read in your `Launch.log` files.

## Rulings wanted (reply "all rec" or name the K you overrule)

| K | Screenshot | Recommended change | What it does |
|---|---|---|---|
| K1 | 1 | Build a small script mod that removes my nine blocked covert actions from the board whenever the map loads, and logs what it removed | Blocked actions stop appearing even though the config block fails; the log line also tells us why the block fails |
| K2 | 2 | Add pistol and autopistol to Blindside's weapon list (one config file) | Blindside works on all 8 Rogue cards: flanking pistol shots gain +1 damage, rising to +4 at top rank |
| K3 | 3 | Release Captain x Buckler (one line of mine), cut all 12 pistol-primary Buckler cards | Buckler lives on 2 new cards, Captain - Buckler - Scout and Captain - Buckler - Smoker (sword + pistol), where Buckle Your Swash fires on every sword attack |
| K4 | 6 | Release Pistoleer x Assassin (one author ban), cut Pistoleer - Swash - Sentinel | Replaced by Pistoleer - Swash - Assassin: the tertiary's sword perks stack on Swash's sword. Exactly 1 new class appears, Swash stays at 3 cards |

After the word: one batch (config edits, weights regenerated, pick sheet refreshed), deck 717 -> 707.

## 1. Covert actions (1_COVERT.png)

- Blocked by jep, 9 templates, `jepFixes/Config/XComGameBoard.ini`, since 09-19: Teamwork Training, Intel Collection, Supply Run, Gain Ability Points (Combat Preparedness), Scavenge Alien Loot (2 templates), Our Experiment Now, Patrol Wilderness, Recover Useful Items (narrative title "Factory Reactivation").
- Blocked by Covert Infiltration itself, 9: Recruit Extra Faction Soldier, Recruit Scientist, Recruit Engineer, Increase Income, Rescue Soldier, Resistance Contact, Facility Lead, Alien Loot, Prepare Counter Dark Event. By Odd S9 Tweaks, 2: Exhaustive Training, Nuke.
- **The block is failing.** Log, this campaign: `CovertAction_SharedAbilityPoints`, `CovertAction_PatrolWilderness` and `CovertAction_UtilityItems` all finished (11-10 and 11-11). Three of my nine. None of Covert Infiltration's own nine appears among the 17 finished actions logged since 11-09.
- Checked and cleared: section and key match the source (`X2EventListener_Infiltration.uc:31`, `:535`); file is plain ASCII; jepFixes loads after every workshop mod (11-11 log); no other mod creates covert actions or touches the list (search of all mod sources and compiled scripts); every path that builds a faction's action list (`MeetXCom`, month end, influence gain) runs with the strategy listeners registered, by my reading of the Highlander source (`XGStrategy.uc:1227`).
- Cause: not found offline. Two candidates remain: my nine names never reach the game's copy of the list, or the list is built once without the filter. Confidence in "failing": high (log). Confidence in either cause: low.
- The 09-19 capture-risk lever lives in the same file. Unverified either way.
- K1's mod settles it: it prints the list as the game holds it, then removes unstarted offers of the nine. Cost: about one hour, same build path as jepNoCoverGrabs.

## 2. Rogue (2_ROGUE.png): true

- Source: `Isms_Effect_Blindside.uc:15` returns 0 bonus unless the firing weapon's category is in `Blindside_WeaponCats`; config `XComIsmsRogue.ini` lists SMG, Bullpup, Vektor_Rifle. The list is a config array, so it can be widened without code.
- All 8 Rogue cards sit on pistol primaries (Gunfighter, Vigilante, Quartermaster, Akimbo x Scout, Smoker), because Rogue carries a pistol secondary and rule W2 keeps pistol secondaries on pistol primaries. Blindside is dead on all 8.
- No other Rogue perk carries a weapon-category check (searched the Rogue ability set).
- Options: K2 widen the list (recommended); move Rogue to SMG/bullpup/vektor primaries (breaks W2, many releases); leave it dead.

## 3. Buckler (3_BUCKLER.png): broken on 10 of 12 cards, weak on 2

- Source: `MZPistol_AbilitySet.uc:1386`. Buckle Your Swash fires only after the soldier's own melee attack with a different weapon that costs an action.
- Hare's config binds it two ways (`3324703791/Config/XComAmalgamation.ini:832`, `:1129`): Swash = pistol primary + sword secondary; Buckler = melee primary + pistol secondary.
- Buckler's home is the sword primary Captain. My W1 pair (sword primaries only with sword secondaries) banned Captain x Buckler on 10-29. Own error: W1 was generated from weapon types alone; Buckler's perk text went unread.
- Live Buckler cards: Fusilier, Pistoleer, Gunfighter, Vigilante, Quartermaster, Akimbo x Scout, Smoker. Only Akimbo has a melee attack (Pistol Whip, 4th rank; judged from the perk names of all eight specs, medium confidence), so Buckle fires never on 10 cards and from the 4th rank on 2.
- Simulated K3: releasing the one pair builds 3 classes; best-tier rule keeps Scout and Smoker (both stack a pistol tertiary on the pistol secondary), drops Sootsman. Buckler 12 -> 2 cards; no primary falls under its floor.
- Assumption inside K3: Akimbo's 2 cards go too (the perk is dead for three ranks, then rides one skill). Say "K3 keep Akimbo" for 4 Buckler cards.

## 4. Oddsman - Ironclad (4_ODDSMAN.png): impossible, CUT today

- Trained Sniper gives Squadsight only with a sniper rifle in the primary slot (`ABBPerkPack_Perks.uc:1856`); Odd S9 Tweaks adds Long Watch on the same condition.
- Ballistic Shields refuses a sniper rifle beside a shield: `AllowedPrimaryWeaponCategoriesWithShield` (`3750594110/Config/XComShields.ini:136`) lists rifle, sword, sidearm, pistol, sawed-off, shotgun, bullpup, SMG, gauntlet, vektor; one other mod adds chemthrower.
- So: sniper rifle = no shield (Ironclad dead); shield = no sniper rifle (starting perk dead). "Shotgun" on the card is Riot's label only; Riot's real weapon is the shield.
- Applied under your standing rule "working cards only": `+DisableClass` for `Oddsman_Ironclad_Riot` and `Oddsman_Ironclad_SwordMaster`. Verified by re-simulation: deck 719 -> 717, Oddsman 26, Ironclad 7, Riot 6, SwordMaster 12, no spec lost its floor. Live after the next game launch. Backup `XComAmalgamation.ini.bak-1112a` in the job folder; vault mirror updated.
- Why the 11-09 audit missed it, and 2 and 3: it models the two mechanisms that strip a perk off the soldier. A perk that stays on the soldier and does nothing is invisible to it. Three new checks go into the audit with the batch: weapon lists inside perk effects, perks that need a melee weapon, shield-legal primaries.
- Same family, not cut: Impaler - Vengeance 2.0 - Aegis Defender (combat knife + shield; knife is absent from the shield list). You hold this soldier. Likely symptom: the armory refuses a new knife while the shield is equipped.

## 5. Infantry - Rocketeer - Heavy (5_HEAVY.png): stays

- Both specs live in the secondary slot. Equip the **Gauntlet**: every Heavy perk works (rockets and flamethrower), and Rocketeer's rocket perks accept the gauntlet (`1527656509/Config/XComGameData_SoldierSkills.ini:17`, `VALID_WEAPON_CATEGORIES_FOR_SKILLS`).
- With the Rocket Launcher instead, Heavy's five flamethrower perks die (Roust, High Pressure, Quickburn, Incinerator, Firestorm).
- The confusing text: Heavy Armaments lists the three weapon types it accepts; the card label prints each spec's first weapon. The squaddie starts holding the Rocket Launcher, so the swap is yours.
- Same answer for the 6 other Rocketeer + Heavy cards.

## 6. Pistoleer - Swash - Sentinel (6_SENTINEL.png): filler by elimination

- Pistoleer + Swash can take exactly two tertiaries today: Sentinel and Tech Medic. Every other tertiary is banned against one of the two specs, mostly by their authors. Sentinel won as the lesser filler.
- Assassin (sword tertiary) is banned against Pistoleer by Pistoleer's author. Simulated release: exactly 1 new class, Pistoleer - Swash - Assassin, top tier, 0 dead guaranteed perks, 1 dead optional perk.
- Smoker and Scout carry a pistol in the secondary slot, which Swash's sword occupies; those bans stay.

## Side findings

- 10 live cards carry no weight entry (default 1 ticket): the Drone Protocol x Modern Pirate / Artisan cards for Scavenger, Assault, Infantry, Marauder, Oddsman. Regenerated with the batch.
- Pick sheet updated today: 717 cards, four counts, your 100 ticks kept.
