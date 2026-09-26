---
type: report
created: 2026-09-15
author: jep
project: XCOM 2 WotC campaign
status: active
---

# Weapon skin audit: what became a skin, what stayed an item

Idi's standard, final wording (2026-09-15, after three revisions): a weapon with a distinct gameplay quality (own stats, an added ability, a new mechanic) stays an item whatever its category, so the loadout list shows real strategic choices. A near-identical variant of a vanilla weapon is a skin, so the Reskin Weapons screen carries the looks. Skins are hidden with Weapon Skin Replacer lines in `jepFixes\Config\XComWeaponSkinReplacer.ini`; XSkin offers hidden templates as skins.

Skins, three groups: (1) every weapon whose damage, aim, crit and clip equal a vanilla weapon's with no added ability, resolved from each mod's source and config against all vanilla profiles; (2) all of Resistance Firearms, ruling C; (3) the TLP visual-attachment duplicates and Clean TLE, identical by their author's description. Items: everything else, including Katana, Wakizashi, Ninjato, the axes, Cosmo Dragoon, Central's and Uejji's battle rifles, Beowulf, Hunter Rifles, Avengers Endgame, Overwatch, Planetside's own-stat guns, and every new-role pack. Unresolved weapons stay items on purpose.

Deployed: 512 weapons hidden; 374 weapons remain items across the audited packs. Verify after launch: a soldier's primary list shows Katana, Axe, Cosmo Dragoon, Central's and Uejji's battle rifles, Beowulf, Hunter Rifle; Resistance Firearms guns appear only under Reskin Weapons.

| Pack                          | Weapons | Skins | Items | Note                         |
| ----------------------------- | ------- | ----- | ----- | ---------------------------- |
| Resistance Firearms           | 321     | 321   | 0     | ruling C                     |
| CBR Redux                     | 54      | 26    | 28    |                              |
| Planetside 2 NC               | 36      | 21    | 15    |                              |
| Mass Effect Cerberus Armory   | 30      | 21    | 9     |                              |
| Total Advent Weaponry         | 24      | 18    | 6     |                              |
| Clean TLE Weapons             | 15      | 15    | 0     | author-identical duplicates  |
| TLP Conventional attachments  | 15      | 15    | 0     | author-identical duplicates  |
| TLP Magnetic attachments      | 15      | 15    | 0     | author-identical duplicates  |
| TLP Plasma attachments        | 15      | 15    | 0     | author-identical duplicates  |
| Resident Evil 2 Weapon Pack   | 15      | 14    | 1     |                              |
| Mass Effect N7 Weaponry       | 18      | 10    | 8     |                              |
| Chimera Squad Weapon Pack     | 12      | 10    | 2     |                              |
| Overwatch Weapon Pack         | 31      | 7     | 24    |                              |
| Vektor Crossbows              | 3       | 3     | 0     |                              |
| Mercenary Plasma Hero Weapons | 4       | 1     | 3     |                              |
| MGS Patriot                   | 6       | 0     | 6     |                              |
| Avengers Endgame              | 15      | 0     | 15    |                              |
| Additional Weapon Pack        | 15      | 0     | 15    |                              |
| High Caliber Pistol           | 3       | 0     | 3     |                              |
| Mercenary Plasma Weapons      | 8       | 0     | 8     |                              |
| Laser and Coil weapons        | 12      | 0     | 12    | kept whole: false match risk |
| Nero's Advent Gear            | 14      | 0     | 14    |                              |
| Uejji Battle Rifle Pack       | 12      | 0     | 12    |                              |
| Katana Pack                   | 12      | 0     | 12    |                              |
| Combat Knives                 | 12      | 0     | 12    |                              |
| TheAxeMod                     | 6       | 0     | 6     |                              |
| Cosmo Dragoon                 | 4       | 0     | 4     |                              |
| SmartPistol                   | 4       | 0     | 4     |                              |
| BowCaster                     | 4       | 0     | 4     |                              |
| Beowulf Rifle                 | 3       | 0     | 3     |                              |
| Sawed-Off Shotgun             | 3       | 0     | 3     |                              |
| LW SMG Pack                   | 3       | 0     | 3     |                              |
| Hunter Rifles Redux           | 3       | 0     | 3     |                              |
| EW MEC Weapons                | 6       | 0     | 6     |                              |
| Legacy of Chosen              | 5       | 0     | 5     |                              |
| Psionic Implants              | 9       | 0     | 9     |                              |
| LW2 Secondary Weapons         | 12      | 0     | 12    |                              |
| Iridar SPARK Arsenal          | 21      | 0     | 21    |                              |
| Ballistic Shields Redux       | 6       | 0     | 6     | kept whole: false match risk |
| Kinetic Smite                 | 3       | 0     | 3     |                              |
| Chemthrower Redux             | 19      | 0     | 19    |                              |
| Immolator                     | 11      | 0     | 11    |                              |
| Heavy Elemental Throwers      | 8       | 0     | 8     |                              |
| Bitterfrost                   | 9       | 0     | 9     |                              |
| SPARK Flamethrowers           | 3       | 0     | 3     |                              |
| Chosen SPARK Arsenal          | 3       | 0     | 3     |                              |
| Five Tier Weapon Overhaul     | 15      | 0     | 15    |                              |
| Chosen Reward Variety         | 4       | 0     | 4     |                              |
| Harbinger bridge              | 5       | 0     | 5     |                              |

## Log

- 2026-09-15 audit run, 134 hide lines deployed, RF held.
- 2026-09-15 ruling C: RF 321 added.
- 2026-09-15 category extension (242) deployed, then withdrawn the same evening on Idi's clarification: distinct qualities stay items.
- 2026-09-15 final: 512 hide lines, 374 items.
