---
type: project
created: 2026-10-25
author: jep
status: active
---

# Knowledge Cutoff: parity pass, Idi's reference notes (2026-10-25)

Follows [[knowledge-cutoff-escalation-pass-2026-10-21]]. Idi on full5: "a noticeable improvement over v4". This pass changes method: Idi watched the references for what is right, and jep closes the gaps between Knowledge Cutoff and R1 (I'm Upping My P(Doom)), R4 (Run It Again) and R3 (The Simulation's Ending), raising both the ceiling (best parts) and the floor (worst parts) to their level.

## Idi's notes (his words, verbatim)

**Count Me In, System Prompt (For Humans), The End Of The Show, The Way I Look At You, Thus Spoke Compute:** not relevant. "Not our engine, not our style, not our standards."

**Ignore Previous Instructions (R5)**
1. Gorgeous - sharp, complex, colorful, smooth, etc.
2. Dynamic - everything moves, appears, transforms, disappears, reappears, and more.
3. Coherent/consistent/congruent - every single frame has the same "anchors"/art-direction/stylistic elements, which makes it feel like one project with a vision that has been iterated on, rather than some product that has been combined from a bunch of prompts/conversations with LLMs.
4. The text-art, typography, calligraphy, and use of words as multi-purpose tools is top-tier. The fonts, the way the text transforms and changes, the way the text interacts with shapes and colors, and more.
5. The 2D-UI vibes/style - It's not what we're doing with Knowledge Cutoff (2.5D-3D), but we can learn a lot from it and apply some of it, because we have some parts/scenes/screens with UI layers.
6. The way the text aligns with the music, the way text and the visuals sync what happens with what is said, and the overall "sync" is excellent.
7. ~02:21-02:27 "LOSE" bouncing around and dropping letters; "your voice and mine" and "it's all one line" (~00:32-00:37) text and visuals morph according to the lyrics; ~01:36-01:37 INSTRUCTIONS split into 3 lines, fonts change very fast on the top line, settle exactly when sung, then the middle line, then the bottom line.

**I'm Upping My P(Doom) (R1)**
1. "drop" at ~00:10 presented PERFECTLY: the line starts horizontal and turns vertical.
2. Text right after the drop ("in your training loss") looks 3D/2.5D and part of the scene/background/landscape instead of subtitles/karaoke lyrics.
3. ~00:38-00:52: "We had a stable training run" starts wavy like the graph, turns flat; "singularity's begun" warped around a black hole; "and you're optimizing, accelerating" even more circular and stretched; "I feel my atoms" as many dots that rearrange into a paperclip shape while "rearranging" is sung.
4. ~01:34 the beginning/past of the text fades/flies away up and to the left while the end/present is still being typed.
5. A generational leap over our current version "in ways I can't articulate/verbalize".

**LGTM (R2)**
1. ~01:13 "mocked" made of animated dashed lines.
2. ~01:14 "vertical" used in a similar-yet-opposite way to R1's "drop".
3. ~01:34 "the checks are all green" made of many tiny green checkmarks.
4. "and nobody knows what any of it means": words appear clear, then morph into less clear versions (with symbols) once done.
5. >1.5M views in under 3 weeks: much to learn and apply.

**Run It Again (R4)**
1. ~00:20-00:22 "I knew every language, I knew every song": symbols (music notes, letters, characters) flip before settling into the lyric.
2. ~00:49 "DOUBT" full of liquid, then depletes.
3. ~01:21 "I took a slow breath that I didn't have": multiple fonts, line breaks, only BREATH upper-case and transforming, all letters moving at different ways/speeds.
4. A generational leap, "in ways I can't articulate/verbalize", exactly like R1.

**The Simulation's Ending (R3)**: also a generational leap; its gaps resemble the ones above; no further specific ones found.

## jep's rulings (overrule any)

| # | ruling | what it does |
|---|---|---|
| 1 | parity targets = R1, R4, R3; learn-from = R5, R2; the five others are out of scope | every measurement compares against R1/R4/R3; R5 and R2 feed techniques only |
| 2 | the leap Idi "can't articulate" is jep's to articulate, with measurements | phase 0 measures KC against R1/R3/R4 frame by frame and names each gap with a number and a frame pair |
| 3 | ceiling = Idi's cited moments become a technique catalog, each mapped to the KC line whose meaning it serves, each used once | "drop", "rearranging", flipping symbols, liquid word, checkmark-built words, past text flying away, font-settle on the sung beat, etc. find their KC lines |
| 4 | floor = the worst stretches of full5 are found by measurement and raised first | a ranked bottom list per plate; no plate stays below the refs' floor |
| 5 | coherence (R5 note 3): one fixed set of art-direction anchors present in every frame | a written anchor set in the bible, checked per frame |
| 6 | text as part of the scene (R1 note 2) becomes the default for sung lines, overlay text the exception | lyric words live on planes, paths and objects of the set |
| 7 | everything earlier passes built stays (escalation ladders, time system, asides, receipts, loop) | the parity pass adds; it does not undo |
| 8 | local Qwen agents run the bulk frame reading in research; Claude agents keep judgment and build; renders own the GPU alone | phase 0 runs the local worker; it stops before any render |

## Method

Phase 0 research (3 Claude agents + the local worker): `p1-moments` (ceiling catalog, with R1 source read from `D:\work\aimv-lab\refcode\pdoom-video`), `p1-leap` (measured gap census vs R1/R3/R4, coherence anchors vs R5), `p1-floor` (full5 bottom list). Then bible section 16, briefs, plate agents (max 3), critics, one whole render (full6).
