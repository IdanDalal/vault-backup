---
type: reference
created: 2026-09-15
author: jep
project: XCOM 2 WotC campaign
status: active
---

# Config shortlist: campaign-shaping settings only

Rule: whole-experience levers only. Idi rules by index; jep writes into jepFixes. Base = Odd Season 9 tweaks as loaded. State after Idi's rulings of 2026-09-15.

## Written into jepFixes

1. Choose My Class: 30 choices at promotion.
2. Sitreps per mission: 1 guaranteed + 1 extra at 50% (Multiple Sitreps REDUX). MCM saved values override at runtime; if the game still shows 3, set 1 / 1 / 50 once in MCM.
3. Sitrep block list: Lightning Strike, Surgical, Fireteam, Location Scout, Stealth Insertion, Show of Force (both templates), Priority Objective, Low Visibility, Black Ops, Advanced, Waves, Phalanx (both templates), Experimental Stims, plus 37 more ruled 2026-09-15 (52 templates). Full list with effects and marks: `sitrep-list.md`. Closed.
4. Sitrep editing: change 10 intel, remove 0, seal 0.
8. Dark event pace: 1, 2, 2, 3, then 3 for good; doom bonus off; hard cap 3 (Scaling Dark Events; Odd S9 had 1,2,3,3 plus a doom term).
10. Field loot expiry: 3 turns for everything (psi was 2).

## Idi's, already set in game

6. Expected damage in the shot HUD: set by Idi in MCM.
7. Second Wave defaults: Idi's own ticks in the Second Wave Defaults panel. Grim Horizon stays off (it is the only thing that makes dark events permanent).

5. PCS: Agility, Conditioning, Focus, Combat Awareness, Emergency Life Support, Body Shield removed at every tier (jepFixes XComGameCore.ini, Long War 2 superset minus the six). Tiers and everything else untouched.

## Open

16. WSR skin-only weapons and Amalgamation spec exclusions: Next Campaign Notes list is stale. jep rebuilds it against the live mod list as the next pass, Idi rules on the fresh list.

## Verified, leave

9. Dark event durations: More Dark Events stat and ability events 31 days, never permanent; vanilla and Requiem events end on their own without Grim Horizon.
11. Alien turn speed 2x automatic, CapsLock toggles; Idi changes speed by hand constantly.
12. Save Scum Roller on: rerolls the RNG on reload, the mod the puzzle-by-reload style runs on.
13. Recruit screen hides pool class and psi (Odd S9).
14. Starting traits +11 / -1, +5 per rank (Odd S9).
15. Variable force level pace per campaign.

Reference for jep only: `mod-config-inventory.md`. Not for reading.

## Log

- 2026-09-15 built after Idi's correction: opinionated shortlist, no per-item tuning.
- 2026-09-15 rulings applied: 2, 3 (13 names), 4, 8, 10 written; 5 and 16 open; 6, 7 his; 9, 11 to 15 confirmed.
- 2026-09-15 evening: 3 closed (52 templates), 5 written (6 PCS types, Agility included). Open: 16 only.
