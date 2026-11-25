---
type: plan
created: 2026-11-25
author: jep
---

# Pay Attention v6 plates: common brief (lead jep, 2026-11-25). Binds every v6 builder.

Idi rejected all 13 v5 plates, then answered the v6 room (79 beats, 78 questions; he kept jep's pick on 74, overrode 4, and wrote ~50 notes). Your plate brief holds every beat's RULED version. This file holds the film-wide rulings. v5's common brief (`../../v5/plates/00-common.md`) still binds where this one is silent: REUSE, NO MAGIC SPAWNS, VARIATION, CAUSE MIX, the engine traps, facts, files and lock rules.

## Film rulings (Idi's taps, 2026-11-25)

1. **Zero hard cuts, zero fades or dissolves** inside a plate and at its seams. Each plate hands over by a camera move into an object or field that becomes the next plate.
2. **Arrivals, mixed per section**: verses make each word in front of you (printed, typed, poured, carved, lit, grown); choruses use words that already exist in the space and light up when sung. No pop-ins from nothing.
3. **Line holds**: the whole line stays readable until the next line starts arriving; then it leaves by its material's physics (dissolves, burns, blows apart, sinks) or stays while the camera leaves it behind. Never mid-word, never before sung.
4. **Camera travels**: it moves through each field line by line, slow drift on held words. Smooth always: no jitter, no shake, no still stretch over ~1.5 s.
5. **3D with graphic beats (Idi's override)**: every plate is a lit 3D space with words as objects in it or on surfaces in it, except 2 or 3 deliberate flat graphic beats in the whole film, each designed flat on purpose. A flat overlay pasted over a 3D scene is never allowed. (Games owns one: the tweet in games-b10.)
6. **One film palette (Idi's override)**: the games combo (pink, teal, white, black) runs the whole film; sections change light and material, not hues. His words on balance, binding: the similar refs (P(Doom), Run It Again, Simulation's Ending) "pretty much ONLY use black, white, grey, and one OMNIPRESENT accent color... We're gonna be much softer, tamer, milder, and more subtle." So: no omnipresent pink; pink is a rare accent; teal and warm whites carry; mid-tones and soft light, never a high-contrast black-and-one-accent frame. Games v5 was "too pink".
7. **Earlier elements come back rebuilt** in v6's look (v3/v4 elements Idi liked).

## Finish gate (jep's, every beat, no exceptions)

Whole words only (no word cut before its last letter renders) · no clipping by frame edge, object or another word · kerning from the font, no hand-spaced letters · one lit word at a time while sung · text fits its container · nothing points at nothing · no blank frame while a word is sung · no jitter · no decoration without a reason (no hanger lines, empty squares, random numbers) · punchlines render.

## Idi's references for v6 (his words, film-wide answer)

- `D:\work\AIMVs\I Can Make Anything.mp4` and `Soon the Algorithm will MAKE everything you watch.mp4` (Imaginative Prompting): "for cinematography, scope, scale, density, and complexity" (their low-poly cel-shaded style is the opposite of ours: take the camera and scale, never the style).
- `I'm Upping My P(Doom).mp4`, `Run It Again.mp4`, `The Simulation's Ending.mp4`: "for atmosphere, motion/animation style, mix of 2D and 3D (though ours should be MUCH more 3D than 2D)", colours only as a warning (rule 6).
- Still pool with timecodes: `D:\work\aimv-lab\pa-video\scratch\lead\v5\refpool\` (still NNN = t 6*NNN-3 s), look guide `..\v5\look-guide.md`.

## Kit ideas Idi ruled "use in PA now"

Matrix code (open), tilt-shift miniature (class, verse 4), sculpted cube (kitchen, exam), laser cut (verse 1), explosions (games), embers (late), words on objects (verse 4). The other nine are kit-later: do not put them in PA.

## Files, render, process

- Start from your plate's v5 file: copy `app\src\scenes\v5-<plate>.ts` (and `_v5-<plate>.ts` if any) to `v6-<plate>.ts`; never edit the v5 files. Render with `VITE_PA_V6=1` (timeline plays v6 where it exists, else v5; lead commit e0eb79c). Report `reports\v6-<plate>.md`; scratch `D:\work\aimv-lab\pa-video\scratch\v6-<plate>\`.
- Render lock `out\.render-lock`, foreground only, never idle waiting (v5 common rules). Commit by explicit path after each working step, message naming the plate, ending `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Another builder works in parallel in the same repo. Never touch their files.

## Deliverables (the next review is per beat)

1. Your plate clip with the song: `D:\work\AIMVs\ours\pa-song\v6\plates\<plate>.mp4` (window with 0.5 s margins) and 4 stills `<plate>-1..4.png`.
2. **Two treatments on the hardest beats** (Idi ruled "v6 plus options"): for the 1 or 2 beats your brief marks HARD, render a second treatment as `<plate>-<beat id>-alt.mp4` (same window as the beat) and say in one line how it differs.
3. Gates: sync (every sung word lit on its frame, negative control 0); size table (sung lines 9-11 % of frame height, heroes 13-40 %); your 8 fps sweep + 30 fps strips at every change, listing any still stretch over 1.5 s; the finish gate above, beat by beat, as a checklist in your report.
4. Report: per beat, what the viewer sees and which ruling it answers; facts with source URLs; seams; the 3 things you are least sure of.
5. The lead reads your sweep and runs a blind critic; a fix round follows; then Idi sees v6 beside v5 per beat.

Final reply to the lead: at most 100 words, once, after the report is committed.

## Lessons from Games and Fact (three blind-critic rounds, 2026-11-25). Build these in from the start.

1. **Line bands never overlap**: an incoming lyric line never builds inside a band the outgoing line or its debris still occupies; alternate bands or separate them in depth. Measure per line change (glyph boxes of both lines) and drive overlap frames to 0. This produced most critic findings in every round.
2. **Nothing appears or vanishes in 1-2 frames**: words, debris, toasts, HUD readouts and signs travel visibly for 8+ frames (check fast moments at 30 or 60 fps).
3. **The meter is sacred**: nothing covers the billing meter or its label; the HUD and lyric lines keep 3 % margin from each other.
4. **Every sung word whole, inside the frame with 5 % margin at rest, readable on its beat** (no dark-on-dark, no word garbled by its own exit while still sung).
5. **Colour: soft, never grey**: warm whites and teal saturation in every stretch; critics flag teal-on-grey stretches as dull.
