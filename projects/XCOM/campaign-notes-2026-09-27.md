---
type: report
created: 2026-09-27
author: jep
---
# XCOM campaign notes, 2026-09-27

Idi's nine notes after the 09-27 `Launch.log`. Full research with receipts: `projects/XCOM/research-2026-09-27/` (four files). Live mod dir: `...\XComGame\Mods\` (jepFixes, jepNoCoverGrabs, jepReusePCS), mirrored in `projects/XCOM/`.

## Status

| # | Note | Status | What changed |
|---|---|---|---|
| 0 | 09-26 fixes in the log | VERIFIED in log | grabs patched x5, Emergency Defense 0 hits |
| 1 | Bolt Caster, Frost Bomb, Hunter Axe missing | ANSWERED, no change | moved by Alternative DLC Integration |
| 2 | Shield attachments | ANSWERED, no change | slots exist; opened from Squad Select |
| 3a | One PCS drop so far | JEP BUG FOUND + FIXED | 09-15 PCS removal never worked; rebuilt |
| 3b | PCS swap like weapon mods | BUILT + INSTALLED | script mod `jepReusePCS` |
| 4 | Ever Vigilant, two mods | ANSWERED, keep both | no conflict |
| 5 | Bond mod cluster | ANSWERED | dependency table below |
| 6 | Psi blade color | ANSWERED | RGB below; button limited by code |
| 7 | Amalgamation combo rules | ANSWERED | 8 rules, 15 candidates |
| 8 | Total Advent Weaponry | INSTALLED (hide 11 more) | all TAW = skins; removal not needed |
| 9 | Avengers Endgame | INSTALLED (hide 15 + flatten) | skins; owned CV copies at vanilla sword stats |

## 0. 09-26 fixes, log receipts

- jepNoCoverGrabs: `patched:` x5 (log 244586-244590), `not found:` 0.
- Emergency Defense: `EmergencyDefense` 0 occurrences.
- Details and the 13 unpatched grab-type abilities: `chosen-missions-2026-09-26.md` section 4c.

## 1. Alien Hunters tier-1 weapons

- Not removed. Alternative DLC Integration 3208771302 blocks the tier-1 build in Engineering (`X2DownloadableContentInfo_AlternativeDLCIntegration.uc:34-132`). High.
- Routes: integrated-DLC campaign = Experimental Weapons research, then four Proving Ground projects; otherwise the one-time Hunter Weapons scan site (appears after the Blacksite is viewed and a Covert Infiltration Intelligence / Datatap / Informant mission succeeds; if it spawned and expired, it never returns).
- Ionic Axe without the tier-1 axe: No Missable Alien Hunter Upgrades 3326247546 + Alternative DLC Integration strip the "own tier 1" gate; left: Stun Lancer autopsy + 10 engineering.
- No ini lever. Fallback: console `GiveItem` (untested).

## 2. Shield attachments

- Shield Attachments 2197927839 adds no slots itself; Ballistic Shields Redux gives 1/2/2 slots, nothing overrides it. Medium-high.
- The Armory "Weapon Upgrade" button opens the primary only (`UIArmory_WeaponUpgrade.uc:130,189`). Shield slots open from the icons under the shield on robojumper's Squad Select screen.
- Drops: about 1-2% early loot; Priest and Shieldbearer corpses 50%. No buy path. Drafted lever to raise early odds in the research file, not applied.

## 3a. PCS drops (jep bug, fixed)

- Correction, jep: the 09-15 removal of six PCS types (Agility, Conditioning, Focus, Combat Awareness, ELS, Body Shield) never took effect. Its `-` lines matched their targets only if whitespace is ignored, so three tables stayed live (log: `PCSDrops* duplicate name - INVALID` x2) and Cut Content Psionics' table won: Conditioning, Focus, Agility = 63% of every PCS roll.
- Fixed in jepFixes `XComGameCore.ini`: six byte copies of the Cut Content Psionics and Odd S9 `+` entries as `-` (script check 6 of 6 exact; Long War 2's copy is already removed by Odd S9's own exact line). jep tables rescaled to sum 100 (were 50/56/66, which would have left rolls empty): Basic 16/16/20/20/14/14, Rare 14/14/20/20/16/16, Epic 14/13/17/17/9/13/17. Rest of the file byte-identical to the backup.
- Rate (unchanged by the fix): Covert Infiltration = 2 timed-loot carriers per mission; only ADVENT carriers can hold a PCS, 50% x count 0-1. About 0.23-0.46 PCS per mission. P(at most 1 PCS): 10 missions 33%/6%, 15 missions 14%/0.8%. One drop is plausible luck up to ~10 missions, suspicious past ~15. Medium.
- Side note: `RarePCSPsi` references a missing ability (log), so that drop is a dud item. Not changed.
- Probe, next launch: `Launch.log` has no `PCSDrops... duplicate name` lines.

## 3b. Reusable PCS: jepReusePCS (built 09-27)

- Vanilla destroys a replaced PCS unless `XComHQ.bReusePCS` is on; only the breakthrough "Reuse PCS" sets it (`UIInventory_Implants.uc:341-348`, `X2StrategyElement_XpackTechs.uc:1258-1264`).
- The mod sets the same flag when Modular Weapons completes (listener on `ResearchCompleted`) and on loading a strategy save where Modular Weapons is already done. Effect: removed or replaced PCS go back to storage, swap popups skip, Remove All PCS button (2782908294) turns on. Gate tech lives in `Config/XComjepReusePCS.ini` (`RequiredTech=`; empty = from campaign start).
- Build: SDK compile 0 errors, `jepReusePCS.u` 12,005 bytes; installed to `Mods\jepReusePCS`, AML entry active (diff = one entry). Source mirror: `projects/XCOM/jepReusePCS/`.
- Probe: `Launch.log` line `jepReusePCS: bReusePCS set (load)` on the first Avenger load; in the Armory, removing a PCS returns it to the list.

## 4. Ever Vigilant

- Keep both. Reliable Ever Vigilant Redux 3546124299 replaces the overwatch trigger; Maybe Vigilant 3657133353 adds per-soldier toggles and blocks toggled-off soldiers (listener priority 100 before 55). No class overrides, no double fire. High.
- Log warnings about missing packages point to the original REV mod (not installed): harmless.
- Open: whether the game reads Maybe Vigilant's `Config/Base` ini. Test: toggle one soldier off, end turn without acting, confirm only the others overwatch. Medium.

## 5. Bond mod cluster

| Mod | Needs | Needed by |
|---|---|---|
| Cohesion Matchmaker 3523258775 | Complex Bonds (code), Re-enabler (declared only) | nothing |
| Love, Kin, Friend or Foe 3468585452 | Complex Bonds (force-loads its package) | nothing |
| Complex Soldier Bonds 3428787645 | nothing | Matchmaker, Love/Kin |
| Team Cohesion Re-enabler 3499811007 | nothing | Matchmaker (declared) |
| Soldier Life Events 3422452897 | nothing | nothing |

- Removal order if dropping some: Matchmaker, Love/Kin, Complex Bonds, Re-enabler; Life Events any time. None of the six other bond mods (Color Coded, More Benefits, Avenger Defense fix, NoDD Bond Slot, Bond To Header 2, Cooldown Teamwork) needs any of the five. Remove from the Avenger, not mid-mission. About 85% confidence.

## 6. Psi blade color

- "Original" = linear RGB (0.20, 0.10, 1.00) (`XComTemplarPsiColorMod.ini:49`). On screen (sRGB): **124, 89, 255** (#7C59FF). Raw 0-255 of the linear value: 51, 26, 255.
- The in-game button offers only the vanilla weapon-color palette chips (`TPC_UICustomize_BladeColor.uc:75`), no RGB entry. Pick the nearest chip.
- Button eligibility: Templar class always; any other class needs rank 1+ and a primary from a hard-coded list of 12 gauntlets (`TPC_ParticleColorPatcher.uc:2056`: ShardGauntlet / CasterGauntlet CV/MG/BM and Left versions). No config line extends it. Likely blocker for Slice: a modded gauntlet template. Diagnostic lever (not applied): `bEnableCustomizationEligibilityDiagnostics=true` under `[TemplarPsiColorMod.TPC_ParticleColorPatcher]`, then grep `TPC_UI_ELIGIBILITY`.

## 7. Amalgamation picks

- Dataset: 44 classes, recovered from the Campaign 30 Mission 14 autosave and the 09-27 log (`Soldier abilities <P> <S> <T>` lines).
- Rules, strongest first:
  - R1 every tree feeds a carried weapon: the tertiary stacks on a weapon he already carries, or fills an empty secondary slot. 21 picks vs 7 by chance. High.
  - R2 generic passive tertiaries avoided: 21 vs 32 expected (Sentinel, Retaliator, Keeper, Tech Medic lowest). Medium-high.
  - R3 a utility tertiary rides with an active-device secondary (gremlin, grenade launcher, psi amp, BIT, arc thrower). 19 of the other 23. Medium.
  - R4 variety: 36 primaries in 44 picks (31 by chance), no repeated secondary+tertiary pair. Medium.
  - R5 exotic secondaries (arc thrower, gauntlet, knife) over pistols. Low-medium.
  - R6 snipers under-picked, 4 vs 7.5. Low-medium.
  - R7 doubled pistol tolerated in pure-pistol kits (his 09-18 ruling).
  - Healing: taken at chance rate, never sought.
- Top 15 from today's 2,519-class deck, all unblocked, unowned, new secondary+tertiary pair:
  1. Pistoleer / Gunslinger / Commissar: triple pistol (Quickdraw, Lightning Hands, Fan Fire, Faceoff, Hit and Run).
  2. Juggernaut / Butterfly / Commando: shotgun Run and Gun + double knife.
  3. Fusilier / Trickshot / Commissar: elemental pistol + autopistol, triple sidearm.
  4. SAW Gunner / Siege Gunner / Executioner: cannon Shredder, Kill Zone + sawed-off on the empty slot (Shredder may duplicate).
  5. Bounty Hunter / Recon Officer / Assassin: concealment + Phantom + sword Shadowstrike, Vanish.
  6. Scavenger / Hotshot / Smoker: Vektor Run and Gun + double pistol.
  7. Savior / Combat Medic / Artisan: blood-magic sustain + double gremlin.
  8. Dreadnought / Siege Gunner / Heavy: Salvo + rockets and flamer on the empty slot.
  9. Marauder / Recon Officer / Agent: bullpup Hit and Run + Phantom + knife.
  10. Huntsman / Hotshot / Smoker: rifle crit line + double pistol (pick 6 or 10).
  11. Savage / Plunderer / Sword Master: triple sword (owned primary).
  12. Akimbo / Recon Officer / Scout: dual pistol + Phantom (owned primary).
  13. Quartermaster / Raider / Assassin: pistol + double sword (owned primary).
  14. Rifleman / Recon Officer / Commando: rifle + Phantom + knife.
  15. Androctonus / Stygian / Scout: the one sniper, against R6.
- Limits: effectiveness is read from ability trees, not playtested; early picks may predate the 09-16 rules.

## 8. Total Advent Weaponry

- Removal: no mod depends on it, but equipped TAW items lose their template; an equipped Advent gremlin is the crash risk. Not needed: hiding gives the same result with zero save risk.
- Installed: jepFixes `XComWeaponSkinReplacer.ini` +11 (`SMG_Advent_*` x3, `PsiAmp_Advent_*` x3, `GrenadeLauncher_Advent_CV/MG`, `Gremlin_Advent_*` x3); with the 18 from 09-15, all 29 TAW templates are skins. This overrides the 09-15 audit's six kept items, on his 09-27 word. Names verified in the mod source.
- Owned copies already built stay equippable (WSR limit). None known.

## 9. Avengers Endgame

- Installed: WSR hide all 15 (`Mjolnir`, `Stormbreaker`, `ThanosBlade`, `WidowBaton`, `RoninBlade` x CV/MG/BM). Hide list now 538 lines (512 + 26), prior content byte-identical.
- The five CV copies he owns (starting items) stay equippable, so new jepFixes `XComEndgameWeapons.ini` flattens them to the vanilla CV sword: damage 4 spread 1 crit 2, aim 20, crit 10; disorient, stun and +1 mobility off. The mod has no MCM and no Documents user ini (checked), so no SaveConfig hijack. Medium: verify in the Armory (Mjolnir CV should read like a plain sword).
