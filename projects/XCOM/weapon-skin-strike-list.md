---
type: reference
created: 2026-09-15
author: jep
project: XCOM 2 WotC campaign
status: active
---

# Weapon packs: skin-only strike list (item 16)

Mechanism, verified in the mod files: Weapon Skin Replacer takes one `+WEAPONS_TO_HIDE=<template>` line per weapon and removes the item and its schematic from the campaign; XSkin (installed) lists every remaining weapon template as a wearable skin, so hidden guns stay available as looks on vanilla weapons. Resistance Firearms also has its own blacklist, which deletes the gun outright; not used. All lines go into `jepFixes\Config\XComWeaponSkinReplacer.ini`.

Your 2025 list, mapped: Half-Life 2 and Max Payne are ghost packs already (skin-only by construction). The rest are no longer separate mods: ACR and Honey Badger live inside Resistance Firearms, the ARES SMGs and the Infantry Rifle inside CBR Redux; Resident Evil Village, Weapons Bundle, F2000, MDR, MP7 and Vector are not installed at all. Both hosts are in list B, so those guns become skins with their pack.

## A. Already skin-only, nothing to do (15)

XSkin, Half-Life 2, Max Payne, Mercenary Plasma Weapon Skins, PAYDAY 2 Shield Skins, Chimera Squad Shield Skins, Chimera Squad Weapons Ghost, Iridar LW2 Laser and Coil Ghost, Iridar ADVENT Arsenal Ghost, Gears of War 5 Ghost, Exalt Ghost, Predator Crossbow Ghost, two Blue Magnetic ghost packs, Deadput's Alien Reskinner.

## B. jep recommends skin-only (strike by index to keep as items)

1. Resistance Firearms Main Module, 321 guns. Real-world arsenal; as items it floods the build list.
2. CBR Redux, 54 (ARES SMGs, carbines, combat rifles). Same reason.
3. Planetside 2 New Conglomerate, 36.
4. Overwatch Weapon Pack, 31.
5. Mass Effect Cerberus Armory, 30.
6. Mass Effect N7 Weaponry, 18.
7. Resident Evil 2 Weapon Pack, 15.
8. Avengers Endgame Weapon Pack, 15.
9. Additional Weapon Pack, 15 (side-grade shotgun, carbine, LMG, SAW, marksman rifle).
10. Total Advent Weaponry, 24 (ADVENT guns for XCOM, cosmetic by intent).
11. Chimera Squad Weapon Pack, 12. Its ghost twin already supplies the skins; the items are duplicates.
12. Mercenary Plasma Weapons + Hero Weapons, 8 + 4. Author calls them cosmetic alternatives; the skins twin exists.
13. TLP Conventional, Magnetic and Plasma "with visual attachments", 15 each, and Clean TLE Weapons, 15. Duplicate tiers of the Legacy Pack guns made for looks.
14. MGS Patriot, 6.
15. High Caliber Pistol, 3.

## C. Keep as gameplay items (jep's call; move to B by index if you disagree)

16. Five Tier Weapon Overhaul and its Laser and Coil weapons: the tier system itself.
17. Secondaries and class gear: LW2 Secondary Weapons, Katana Pack, Combat Knives, The Axe Mod, Ballistic Shields Redux, Kinetic Smite Module, Psionic Implants, Cosmo Dragoon, SmartPistol, BowCaster, Vektor Crossbows, Sawed-Off Shotgun, LW SMG Pack, Beowulf Rifle, Hunter Rifles Redux, Uejji Battle Rifles (custom abilities), Enemy Within MEC Weapons.
18. SPARK and specialist gear: Iridar SPARK Arsenal, Chosen SPARK Arsenal, SPARK Flamethrowers, Chemthrower Redux, Immolator, Heavy Elemental Throwers, Bitterfrost Protocol.
19. Hero and bridge items: Legacy of Chosen, Chosen Reward Variety, Harbinger Rifle bridge, Xeno Zoologist arms, Musashi's fixes.
20. Nero's Advent Gear, 14: custom weapons with abilities built on Template Master. Undecided; your call.

Enemy and faction weapon sets (ABA, LWOTC Standalone, Requiem, Frost Legion, MOCX, Pathfinders, Faction Heroes) are not XCOM items and stay untouched.

## D. Amalgamation exclusions: nothing to rule

115 specializations installed (51 primary, 38 secondary, 26 tertiary). The spec mods ship 9,165 incompatibility rules of their own. Odd Season 9 adds 74 pairs and 9 disabled classes; 54 of those pairs name a spec no longer installed (dead, harmless), 20 are live. The two-weapon rule is enforced at promotion by your Choose My Class pick, not by exclusions. Closed unless you want the 54 dead pairs cleaned for tidiness.

## E. Not achievable

The 2025 note asking for blue magnetic versions of 11 weapons: the blue ghost packs carry meshes for two, the rest need models that do not exist.

## Log

- 2026-09-15 evening: superseded by Idi's stats rule; results in `weapon-skin-audit.md`.
- 2026-09-15 built from the live mod list (78 XCOM weapon packs scanned by template count), WSR and XSkin configs, Odd S9 Amalgamation file.
