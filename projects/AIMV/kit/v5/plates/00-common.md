# Pay Attention v5 plates: common brief (lead jep, 2026-11-18). Binds every plate builder.

Idi ruled a type-first restart (v3 and v4 were "VASTLY inferior to any of the refs"). Three look tests passed a blind panel and his eye; this brief turns them into the film.

## Read first (all bind)

1. `D:\work\aimv-lab\pa-video\scratch\lead\v5\look-guide.md`: still-frame grammar (R1-R12: sizes, one drawing system, one accent, a field behind every lyric).
2. `...\v5\motion-guide.md`: motion grammar (M1-M14: big change every 2.2-4.5 s, small new thing every 1-2 beats, no hold over ~2 s, two clocks, carried transitions, slams 0.03 s in / 0.16 s settle, exits act out the word, instrumental bars move more with an accelerating counter).
3. `...\v5\film-plan.md`: the story in five acts, the easter-egg rules, the meter.
4. `...\v5\section-map.md`: fields and palettes per section (your plate brief refines its row).
5. The three approved tests, as the bar and as code to learn from: `app\src\scenes\v5-chorus1.ts` (+ `_v5-chorus1.ts`), `v5-ink.ts`, `v5-games.ts`; reports `reports\v5-chorus1.md`, `v5-ink.md`, `v5-games.md`; clips `D:\work\AIMVs\ours\pa-song\v5\`.
6. P(Doom)'s real scene code: `D:\work\aimv-lab\refcode\pdoom-video\app\src\scenes\`.

## Idi's rules from the tests (2026-11-18 night, his words in quotes)

1. REUSE: a word or object that comes back is the SAME object transformed, never a second copy. ("go back to the same PAY ATTENTION... and add the duplicate-in-depth effect there instead of adding another"; "reuse the word INK in some cool way since it appears 3 times").
2. NO MAGIC SPAWNS: "most of the words are spawned within line-of-sight of the camera, and we're sleeping on opportunities to reveal words instead, or pan the camera to where they already appear, or hand-written as one continuous line... or other alternatives to magically create letters out of thin air." Every word arrives by a cause. Causes: the camera finds it (it was already there); light, a wipe, a peel or a mask reveals it; something writes, types, prints, stamps, carves, burns or projects it; it is assembled from parts that were on screen; it grows out of the previous word; it falls, flies or is thrown in from a visible source. A plain fade-in or pop-in counts as magic.
3. VARIATION: "uniformly... boring, basic, uninspired, and wasteful of things we can control... latent space for creativity." Parallel items (lists, repeated words, the four arrows) each get a different treatment: direction, cause, timing, scale, camera.

## The film's shared systems (kit `app\src\scenes\_v5-film.ts`, built first by v5-t1; import it, never copy it)

- The billing meter: the film's "five minutes of attention", counting down 5:00 → 0:00 over the song, designed as the AI's meter (mono label, draining bar). One object, one place, every plate (the outro owns its end).
- `context N tokens`: the count of words sung so far (from `data\lyrics.json`), shown in HUD moments; it is always the true number.
- HUD label style (JetBrains Mono, 1.6-2 % of frame height, leader lines), the film voice (Anybody 700-900), slam and settle helpers.
- The attention diagram (tokens, weighted arcs) as exports, for chorus 2, chorus 3 and verse 4 ("eight heads").

## Facts

Every on-screen fact is true and sourced. Your brief lists candidates; verify each with a web source before you build it (note the URL in your report). Drop any you cannot verify. Never invent a quote, number or date.

## Files and process

- You own `app\src\scenes\v5-<plate>.ts` (+ optional `_v5-<plate>.ts`), your report `reports\v5-<plate>.md`, scratch `D:\work\aimv-lab\pa-video\scratch\v5-<plate>\`. Kit requests to `_v5-film.ts` go to v5-t1 through the lead.
- Render inside the film: `VITE_PA_V5=1` plays your `v5-<plate>.ts` in your plate's timeline row (rows and cut times in `app\src\timeline.ts`; ask the lead for row changes). Render your window with a 0.5 s margin each side.
- Seams: your first and last frames hand over to your neighbours by the carried object your brief names. Until a neighbour is built in v5 it is v3; compare both seams and state them.
- Other builders work in parallel in the same repo: commit only by explicit path; never stash, revert or edit their files; wait when `out\.render-lock` is held. Foreground only, no agents, no backgrounded commands. To wait for the lock, run ONE foreground tool call that polls `out\.render-lock` every few seconds and then starts your job (timeout up to 10 min, repeat if needed). Never go idle waiting for a lock or a background job: nothing wakes you, and four builders share one GPU. Commit after each working step, message naming the plate, ending `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Gates and deliverables

1. Check sync over your window (every sung word lit on its frame; negative control 0).
2. `deadarea.py` on your stills (under 0.40).
2b. SIZE (look guide R1), measured: a table in your report of every sung line's cap height as % of frame height (sung lines 9-11 %, heroes 13-40 %, nothing sung under 5 %). Lines in a corner or at 3 % of frame height are the v3/v4 fault that got the film rejected.
3. Motion: your own 8 fps sweep of the whole plate and a 30 fps strip around every transition; list every stretch over 2 s where nothing meaningful changes (target: none, except a placed rest the brief names).
4. Clip with the song `D:\work\AIMVs\ours\pa-song\v5\plates\<plate>.mp4`; 4 stills `<plate>-1..4.png` at its strongest moments.
5. Report: what each line does and by which arrival cause; facts with sources; gate numbers; seams; kit requests; the 3 things you are least sure of.
6. The lead runs a blind panel (your stills among 40 reference stills) and reads your sweep; a fix round follows. Then Idi sees it.

Final reply to the lead: at most 100 words, once.
