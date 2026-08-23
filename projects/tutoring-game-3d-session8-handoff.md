---
type: project-brief
created: 2026-08-23
author: jep
project: tutoring
status: in-progress
---

# Word World — Session 8 handoff (Idan's 17 notes, Sun 2026-08-23 midday)

START-HERE for the next session. Read this, then the session-7 checkpoint in [[tutoring-game-3d-playtest1]] only if state questions remain. Idan's plan: parallelize pedagogy and fixing; the pedagogy queue lives at the end of the session-7 checkpoint.

## Standing context (do not re-derive)

- Master `~/game3d/island.html` (1180KB); sources `~/game3d/src/`; build `node ~/game3d/tools/build.mjs`.
- Probes run FROM `~/render-tools/`: gauntlet3d / slicec3d / setcomplete3d / persist3d + `tmp-s7.mjs` (session-7 visual suite, reusable). `__PROBE.start()` grants all action locks; `__PROBE.start(who, {keepLocks:true})` keeps them. Screenshot sets: `~/game3d/screenshots/s7/`.
- Verification ritual: every visual change passes the screenshot gauntlet before claiming quality. Deadline: game ready Monday 2026-08-25 morning; rate budget authorized hard through Sunday.
- Session 7 shipped: Word World title, EARN.actions First Words gating, quest checklist + sparkle guide, pet hi/commands, sky-dome-rides-camera (bubble root cause), keyLetter layout-proofing, sign rebuilds, speed dial, full tech queue. All probes green.

## The 17 notes (verbatim intent + implementation pointers)

1. **Tagline candidates** (iterate/combine with Idan in-session): "Where text comes to life" · "An island that listens" · "Where English is magic". Lives in `CHANGE_ME.TAG_LINE` (config.js); title screen reads it in showTitle (main.js).

2. **N no longer closes Sky Magic + Esc chains into pause.** KNOWN CAUSE, second occurrence of the same bug class: the session-7 fix moved the skypanel CLOSE listener before the OPEN listener, so now one N-press in skypanel mode closes (mode→'play') and the open listener fires on the SAME keydown and reopens. Esc path: closeSkyPanel → lockPointer; the Esc-initiated pointer-lock churn lands a pointerlockchange while mode==='play' → auto-pause. STOP PATCHING LISTENER ORDER. Build one keydown router that owns open/close for every panel (single listener, explicit precedence, one `e` handled once), plus: (a) a red ✕ close button on every menu (Idan asked explicitly), (b) pause-guard: ignore pointerlockchange auto-pause within ~400ms of any modal close (stamp `UI.modalClosedAt = e.timeStamp`). Affected listeners today: main.js (book/pause), words.js (catch, skypanel, play-interact), craft.js (bench, pet), story.js (story/perform), earn.js (earnflow).

3. **Pause menu redesign** — barebones, repeats the always-visible help line. Drop the key list; make it a warm "island status" card: resume, Change ✨, world code, plus flavor stats (words caught, sets done, stories told, day count). body.html #pause + style.css.

4. **Help line** — bigger type, THREE lines, more centered. body.html #help-line spans + style.css (font-size up from 13.5px, regroup: movement / actions / menus).

5. **Catch minigame → pokemon-parody duel presentation.** Idan wants maximal drama ("flex" register — house-restraint is WRONG here, this is a deliberate calm-laws exception at an achievement surface): screen pulses in instead of instant UI, dramatic music sting, player portrait vs the word/emoji as opponents, per-letter "attack hit" (big blue ring shrinking to a tiny red point on the emoji, which flinches and degrades), escalation letter by letter until the last letter is a held "opponent about to lose" tableau, final letter = exaggerated climax. Files: words.js (openCatch/catchKey/completeCatch), style.css #catch*, core.js SFX (add duel sting/hit/climax sounds; sidechain exists). Keep the untimed law: drama escalates only on PROGRESS, never on a clock.

6. **Signpost stick shows through the BACK text.** buildSignposts (craft.js): post is full-height at z=0, back text at z≈0.068, post radius 0.075 pokes past it. Fix: post ends below the board (height ~1.0 to board bottom) or sits fully forward of the back face; keep both text faces proud.

7. **Lock creature commands behind caught words — YES, do it.** Why session 7 shipped them free: come/stay/home are outside the word economy and the typed "hi" already gated the surface; a scope call, no deeper reason. Proposal: chips render locked (🔒 grey) until their word is caught; jump already exists in First Words; add come/stay/home as a small "Friends" word set spawned near the creatures' home biomes (pedagogy-day question: YLE fit — come=Starters, stay/home=Starters-adjacent). Typed greeting stays free.

8. **Journal layout** — width should fit the longest line unwrapped (fit-content + max-width cap), scrollable, sectioned: "who we are" (identity blocks) and "what we did" (event feed). journal.js renderJournal + style.css #journal.

9. **Story circle UI restyled after mengto.com — FEASIBLE, day-scoped.** It is a DOM panel (body.html #story + style.css), so this is CSS/motion work: gradient meshes, glass cards, springy transitions. Reference material ALREADY LOCAL: `~/game3d/ref/mengto/` (49MB, session-2 study set) and the licensing/pattern map in [[tutoring-game-3d-mengto-digest]] (MIT-safe list). Offline law: no CDN fonts/assets; embed everything.

10. **Harder "earned, not given" — story circle behind fire.** Idan's design: campfire starts COLD (no flames/crackle/glow), catch the word "fire", then TYPE "start fire" at the circle to ignite it and unlock storytelling. Direction: yes, and it establishes the typed-station-verb pattern (extensible later: "open book" at the library?). Files: story.js (buildStorySpot flame group hidden until lit, nearStorySpot prompt swaps to the ignite flow), words.js E-routing, core.js crackle gate, save flag (litFire). Note: "fire" is currently only a label word; add it to a set (pedagogy call: which) with an anchor near the cove.

11. **Speed toasts → short funny sentences** instead of "🐢 speed ×0.59": one line per band, e.g. sleepy-snail through rocket-with-no-brakes register. words.js adjustSpeed; keep the exact multiplier out of the copy or tiny.

12. **Toasts overlap the help line.** #toasts bottom:108px collides with the (soon 3-line) help block. Move toasts up (or dock help lower); recheck with journal ticker bottom-left law from session 6. style.css.

13. **Island rework, AAA-deliberate ground design (BIG PASS, authorized today).** Specific bugs: word garden has elevation variation inside the bed and a missing floor/ground corner (genGardenSoil skips columns where cur <= WATER_Y → holes when the yard clips the coast; also plots vs leveled height mismatch). Bigger indictment: ground reads as procedural block-noise, wants deliberate zoning by "an experienced AAA team": intentional material zones with edges/borders (path edging, plaza banding, biome transition strips, shoreline treatment), calm centers + detailed boundaries (MineBench digest laws in [[tutoring-game-3d-minebench-digest]]). Terrain passes live in world.js (genTerrain/genVillage/genGardenSoil/carvePath). WARNING: reseeding or moving landmarks orphans saves and probe anchors; keep landmark derivations, re-run ALL probes + 4-angle screenshot audit, budget the biggest slice of the session for this.

14. **Undo toggles for every world change.** Framing goal: "everything here was chosen by the player." Extend the Sky Magic panel into an "Island Magic" panel: one on/off row per activated payoff (night/rain/snow already toggle; add rainbow ✓ exists, dragon, mermaid, volcano smoke, shooting stars, big moon, music, EARNED COLOR itself, world tints from sentences). Rows appear only after earning. Persist in skyPrefs-style prefs (save v3 already carries skyPrefs). earn.js renderSkyPanel + wonder.js visibility gates.

15. **Asset-quality pass, round 2:** dragon, mermaid, shell "and many more." Shell/sea/sun/mountain/cloud still legacy `boxes:` format (config.js PROPS) — rebuild in the parts language; dragon and mermaid need the session-6 treatment (silhouette, face, proportions). Also check what reads as a "plane" (see 17). Verify each against calibration anchors via screenshots.

16. **Grass rethink.** Current: ~20k instanced 5-vertex blades, reads as "few large blades". Performance-light options to trial with screenshots: (a) denser + much shorter/thinner blades, (b) crossed-quad tufts with alphaTest texture (halo-safe recipe: alphaTest 0.5, dilated RGB, SRGB colorspace — digest 3 fix stack), (c) ground-color detail only (noise patches baked into mesher) + sparse tufts, (d) removal. Governor guards perf; SwiftShader fps is meaningless, judge by look.

17. **Boats + "planes" earned.** No boats visible until "boat" is caught (word exists, beach set); then SEVERAL sailboats (5–8; each ~10 meshes, cheap — cap and reuse). "Planes": likely what Idan sees is the dark flat jitterIco cloud blobs or distant birds reading as aircraft (see s7 title shots, saucer-like silhouette) — investigate first; if he truly wants planes, add a 'plane' word + toy prop + a few circling after catch. Gate NATURE.boats spawn/visibility on wordsState.caught (nature.js buildAmbientSea + tickNature); same pattern as EARN.actions.

## Suggested batching

Quick wins first (2, 6, 11, 12, 4, 3, 1), then 7+10+14 (one "earned interactions" pass), then 5 and 9 (two presentation set-pieces), then 13+16 (world pass, biggest), 15+17 riding on it. Probe + screenshot audit after each batch, vault checkpoint at the end.
