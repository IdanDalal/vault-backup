---
type: project-note
created: 2026-08-23
author: jep
project: tutoring
status: in-progress
---

# Word World — Session 8 checkpoint (Sun 2026-08-23, agent session)

All 17 handoff notes from [[tutoring-game-3d-session8-handoff]] are implemented. Build `~/game3d/island.html` (1214KB), all 12 probes green (gauntlet3d, slicec3d, setcomplete3d, persist3d, tmp-s7 visual suite, new tmp-s8a…s8f). Screenshot sets: `~/game3d/screenshots/s8/`.

## Shipped, by note

1. **Tagline**: set to `an island that listens` (config.js TAG_LINE); the other candidates are preserved in a comment on the same line. PROVISIONAL: Idan wanted to iterate in-session, so this is a default to react to, one line to change.
2. **Keydown router**: single listener in main.js (`routeKey`) now owns every panel open/close with early-return dispatch by mode. Typing listeners (catch/pet/earnflow/ignite) handle letters only and `preventDefault()` what they consume; the router honors `e.defaultPrevented`. This killed a second latent bug of the same class: the final letter of a typed phrase ("start fire", pet "come") closed its panel and the same keydown then re-opened another. Red ✕ close button on all 10 menus. Pause-guard: pointerlockchange auto-pause is ignored for 400ms after any modal close (`UI.modalClosedAt`, stamped in `UI.setMode`).
3. **Pause redesign**: "Our Island" status card. Stats: words caught, sets complete, stories told, island days (play-seconds persist in save as `playT`, day = SKY.cycleLen). Key list dropped.
4. **Help line**: three grouped rows (movement / actions / menus), 15.5px.
5. **Catch duel**: pokemon-parody presentation. Entrance pulse + card slam + `SFX.duelSting`; portrait VS emoji arena with plates; per-letter attack ring (blue collapse to red point), emoji flinch + progressive greyscale droop, card kick scaling with progress; one-letter-left "desperate" tableau (red wobble, holds until the keystroke); climax flash + foe spin-out + `SFX.duelWin`. Untimed law kept: everything advances on keystrokes only.
6. **Signpost**: post ends below the board (h 0.98); finial knob moved onto the board plane. Back text clean, verified by screenshot.
7. **Pet commands earned**: come/stay/home/jump chips render 🔒 grey until caught, typing matcher and `petCommand` gate through `actionUnlocked`. New word set `friends` ("Animal Friends", meadow, come/stay/home) with signpost + SET_REWARDS entry (Animal Whisperer). Typed "hi" stays free.
8. **Journal**: sections "who we are" / "what we did"; panel width fits the longest line (fit-content, cap min(560px, 58vw)), long lines scroll horizontally.
9. **Story circle mengto set-piece**: campfire-dusk gradient mesh (fire-orange, violet, teal, pink radials over deep indigo), frosted glass cards (blur + hairline light borders), springy cubic-bezier(0.34,1.56,0.64,1) hovers, its own spring entrance. Scoped entirely to #story. Offline law kept (zero external assets).
10. **Fire-gated storytelling**: campfire starts COLD (flames/glow hidden, unlit wood shown, no crackle). New word `fire` (band k, beach set, anchored 3 blocks from the circle). Flow: E at cold circle without the word nudges; with it, an ignite panel copy-types `start fire` → flames, celebration, journal line, save flag `litFire` (v3 save, round-trip probed). Prompt swaps "light the campfire 🪵" ↔ "tell a story 🔥". `storyLit()` honors `__ACTFREE` and the EARN.actions dial. buildSignposts skip rule changed from some-anchored to all-anchored so beach keeps its board.
11. **Speed toasts**: one funny line per band ("🐢 a turtle with nowhere to be." … "🚀 good luck steering THIS."), multiplier removed from copy.
12. **Toast overlap**: #toasts bottom 178px, clear of the 3-row help block (probe checks rect intersection).
13. **World pass**: (a) garden bug fixed: underwater yard columns now BUILD UP to yard height (stone footing below waterline, soil above) so the coast-clipped corner has floor; heights verified uniform by map dump. (b) Ground zoning `genGroundZones` (surface material swaps only, heights untouched): wet-sand shoreline band, dry-grass seam where meadow meets beach, worn-dirt patches under peak slopes, cobble edging beside paths/plaza. Plaza rebanded: paver medallion, cobble medallion ring, calm stone field, cobble border under the wall. Three new border blocks (16 cobble, 17 drygrass, 18 wetsand); atlas rows 6→7.
14. **Island Magic panel**: Sky Magic renamed + extended, one on/off row per activated payoff, rows appear only after earning, all persisted in skyPrefs: rainbow, dragon, mermaid, volcano smoke, shooting stars, big moon, music (off/calm/party, synced with M key), island color (off returns the storybook grey), sentence magic (world tints apply neutral when off, stored values kept). Visibility gates live in tickWonder / sky.js / computeColorTarget / applyWorldTints.
15. **Asset pass round 2**: dragon rebuilt (arched neck, snout + nostrils, swept horns, spike row, big raked membrane wings, finned tail, belly plate); mermaid rebuilt (proportioned head, seashell top, scale waistband, curved tail + real fluke, draped hair, smile + cheeks); shell/sun/mountain/cloud/sea converted from legacy boxes to the parts language (scallop dome + ridges; 8-ray sun; twin-peak + snow cone; water disc + crest + foam; puff cluster). Calibration renders in `screenshots/s8/props/` via new offscreen-render probe tmp-s8f (reusable for future asset passes).
16. **Grass**: trial (a) shipped: 6–9 blades per column (was 3–5), scale 0.42–0.76 wide (was 0.75–1.35), height 0.5–0.9 (was 0.8–1.45); tufts shortened. Reads as ground cover at eye level (g8 shot). Options b/c/d not needed.
17. **Boats + planes**: six sailboats ring the island, hidden until "boat" is caught (tickNature visibility gate, payoff toast). "Planes" root cause confirmed: Lambert cloud undersides went dark grey and read as aircraft. Fixed with emissive lift on the cloud material + rounder puffs; verified from below.

## Flags for Idan (answer when convenient)

1. Tagline: `an island that listens` is live; say the word to swap to `where text comes to life` / `where english is magic` / old one.
2. Pedagogy (from note 7): YLE fit of come (Starters) / stay / home — the Friends set is live either way; words can move sets in one line.
3. `fire` landed in the Beach Day set (nearest coherent home to the cove). Beach set is now 7 words, so completing it requires fire. If it should live elsewhere, one line in config.js.
4. One-time side effect: the plaza banding changed how many random draws terrain gen makes, so randomly-placed word cards landed in new spots this build. Anchored words (First Words, sky, wonder, fire) are unmoved; saves and landmarks are unaffected.
5. The story clearing (6.5 blocks around the cove) now refuses random word spawns; a card floating at the campfire used to shadow the E-interaction.

## Probe additions (all in ~/render-tools)

tmp-s8a (router/✕/pause/helpline/toasts/journal/signpost), tmp-s8b (pet locks, fire flow, Island Magic toggles, litFire persistence), tmp-s8c (duel presentation), tmp-s8d (story restyle), tmp-s8e (world 4-angle + zoning closeups + boats gate + cloud underside), tmp-s8f (offscreen prop calibration renders). setcomplete3d now enumerates the beach set live. Headless caveat learned: background tabs throttle setTimeout, so probes wait for `mode()==='play'` after typeCatch instead of fixed sleeps.

## Next

Monday 2026-08-25 morning deadline: game is feature-complete on the 17 notes; remaining work is Idan's review of the flags above + the pedagogy queue at the end of [[tutoring-game-3d-playtest1]]. Per-girl copies in `~/tutoring-data/games/` still need a re-copy from master once Idan approves the build.
