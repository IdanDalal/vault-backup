---
type: project
created: 2026-11-04
author: jep
status: active
---

# "Pay Attention": treatment (style bible), phase 1

The one document every plate agent reads. Built on [[knowledge-cutoff-treatment-2026-10-17]]: **KC sections 12-16 stand as the bar** (detail at 4K, Idi's full-video notes, rhythm, escalation, parity) unless amended here. Sources: plan v2 [[video2-video-plan-2026-11-04]] (Idi R24, R25), repeat map [[video2-repeat-map-2026-11-04]], timing of record [[video2-phase0-2026-11-04]] (R26), toolbox [[kit-techniques]]. Line-by-line plans: the line cards (`D:\work\aimv-lab\pay-attention\cards\`). Public copy of this file ships in the repo at release with names and vault paths scrubbed (KC export check: names 0, paths 0).

## 1. The idea

Attention is light. One white lamp in a greyscale field of type is the video's key light, and everything casts its shadow from it (Idi R29: look A, monochrome light, his "white palette"). Every question she asks adds a light, and so more shadows; every pasted answer glows screen-blue, the only hue. The viewer's five minutes run down on a meter from "Hi." (0:00.37) to 0:00 exactly 5:00.00 later, while the song ends at 4:52 (292.00 s, Idi R27) and "Go on. Ask it." waits in the composer. The receipt printed at 0:05 collects what an attentive viewer could catch and reads it back at 4:40.

## 2. Tone

1. KC 2.1-2.3 stand: dynamic on the beat (song grid 112.35 BPM tracked, 547 beats, 145 downbeats; `data\audio.json`), precise, deadpan.
2. Bans, KC 2.4 standing: filled drawings of people, animals, doors, suns, flags, neurons, cats; stacked-copy motion blur on text; beams and sparkle rings as decoration; purple-cyan neon; glowing brains; code rain; generated images; frame grabs of other videos.
3. Amended by Idi R24/R25: **no 3D-rendered, Blender-looking or low-poly sets** (The End Of The Show, The Way I Look At You, Accept All); **decorative particles allowed up to the level of The Simulation's Ending and I'm Upping My P(Doom)** (KC's "particle soup" ban becomes a cap; eye gate in section 10).
4. New bans: app logos and brand marks (generic glyphs only; the pie chart of apps included); mascots or avatar figures (every ref with an avatar lost its lyric to it: W-B, W-C faults); lens flares and chromatic aberration except a 1-3 frame hit.
5. The AI is the straight man again: calm, a little smug at "I checked.", warm in the bridge.

## 3. The lighting system (Idi R28/R29: look A, monochrome light; replaces the palette)

Idi R28: lamp-yellow "too similar/close to Knowledge Cutoff"; he asked for white, and deeper, a lighting system "with advanced contrast, complex shadows, intricate greyscale effects". R29 picked look A from the look tests (`D:\work\AIMVs\ours\pa-song\proof\lighting\board.png`).

| element | rule |
|---|---|
| materials | greyscale only: ink, panel, graphite, ash, paper (KC tokens without their warm tint); value carries everything |
| the key light | the lamp: one neutral white light (about 5600 K) with visible falloff; a true black point and true white highlights in every lit frame |
| shadows | every word casts its own letter-shaped shadow (never a box); objects cast shape-true shadows; the penumbra grows with distance from the surface (hard close, soft far); contact shadows where things touch |
| shading | engraved or hatched shade on the side away from the light (KC `toneHatch` / `engrave`), ambient occlusion where things meet, specular glints on paper and glass edges facing the light; 5+ readable grey steps per frame |
| her questions | each lit "?" is a small white-hot point light that casts its own shadows: more questions, more lights, more shadows (the eight heads = eight lights fanning eight shadows); her handwriting (Caveat) is white-hot |
| the only hue | screen `#2E6BFF`: answers, pasted text, apps, the phone glow, and only as light emitted by them, never a fill or a key light; inside the accent band (0.7-1.9 % of the frame) except where answers flood the picture by design (verse 1's pasted class, chorus 2's apps) |
| the cursor | paper white, 3 px at 1080p, the AI; it casts the thinnest shadow in the video |

1. **Exposure ladder** (replaces the saturation ladder, What Counts w19 in light): crushed blacks and a narrow value range while answers rule (verse 1, chorus 2); the bridge lamp is the only light; the final chorus (3:58) is the first frame with the full value range and lamp light reaching more than a third of the frame.
2. Darks: KC's 0.27 tint retired with the yellow (greyscale materials); the value structure (true black to true white) is the bar, measured per still (p1 / p50 / p99).
3. Bloom and halation only on light sources (the lamp, her "?" lights, screens).

## 4. Typography (KC families, all OFL, on disk)

| role (role map) | family | use |
|---|---|---|
| the lyric voice | Anybody (width 50-150, weight 100-900) | sung lines, hooks, anchored repeats |
| I = the AI | JetBrains Mono, typed by the paper caret | the composer, the AI's asides ("Correct.", "I checked.", "I can.", "I won't."), the meter (tabular figures), the receipt rows |
| you = the viewer | Anybody on the glass (the laptop screen surface between her and the AI); the meter | lines addressed to "you" sit on the glass plane; mirrored when seen from her side |
| she = the kid | Caveat, white-hot (a light source) | her handwriting: "¼?", her questions, the eight heads' labels |
| documents | Newsreader | Socrates' and Plato's text, headlines, the fact sheet |
| quoted chat | JetBrains Mono inside panel bubbles; hers with a white-hot hairline that lights the bubble, the AI's with a paper hairline | "write it for me, it's due tonight", "Can you just do it for me?", the four injection attempts |

KC 4.1-4.3 stand (scale 10x+ per frame, Swiss grid, kerning, tabular figures, no outlined type). KC 4.3's ban on outlined type is lifted for one move only: unlit words in the final chorus (gap G4: a word's unlit tube lights when sung), pending Idi's eye on the proof.

## 5. Lyric rules

1. KC 5.1, 5.2, 5.4-5.8 stand: per-word sync on the lit frame (timing of record v3, 773 words), one hero per frame, 36 px floor at 1080p, 48 px edge margin, every word in its own place, each line designed for its meaning, no subtitle rows. KC 5.3 (the chorus hop) stays retired.
2. **Anchored repeats (S6)**: a repeated word keeps its exact place, size and face from its first sung onset to its last; at each repeat the world around it changes. Treatments R-A anchor and swap, R-B reel, R-C mirror, R-D count up, R-E anaphora stamp, R-F ladder ([[video2-repeat-map-2026-11-04]]). This is the one sanctioned exception to "nothing appears twice the same way" (KC 15): the word repeats, its world never does.
3. **The slot reel (Idi's design)**: "20" fixed, the next digit a vertical reel that spins on the first "twenty" and lands on each sung value (0, 0, 2 for 2022); 2023 is sung plainly, so its reel lands in one clean spin (Idi R27); the reel lands on the word's lit frame.
4. Spoken lines are typed in mono by the cursor; whispers sit in bubbles at whisper size; "Pencils down." is the one spoken line set in the lyric voice (the slam).
5. On-screen-only text (never sung): "...but yourself." (2:13), "Go on. Ask it." (tail), 9:47, 400/day, Khan Academy, the receipt rows. They obey the clarity gate and appear on a beat.

## 6. Motifs and their ladders

| motif | what it is | ladder (plan v2 section 4) |
|---|---|---|
| the lamp | one white key light; every "?" is a light source and casts shadows | off, unlit, on (1:08), dim (2:30), only light (2:47), eight beams (3:42), lifted (4:05), settles (4:20) |
| the cursor | the AI: a paper caret, 3 px at 1080p, 1 Hz blink when idle | spark at frame 1; types; checks; reads her; keeps blinking through the night; types "?" back; waits in the tail |
| the meter | the viewer's attention, 5:00 to 0:00, the one screen-stuck element | ticks; drains fast in chorus 2; 0:18 at "paid in full"; 0:00 on the last frame |
| the receipt | a till slip in mono on paper | header = title cards; row 1 at 0:05; rows at each plant; billed twice (2:18); read out (4:40); footer = reverse titles |
| the glass | the laptop screen surface between her and the AI | invisible until a bubble bounces off it (bridge); text read from both sides (mirror); cracks on "Pencils down." |
| the chair | the chorus question's answer | empty (1:20), filled with light (4:18) |
| hands | hands built of "?" | 0, one, a classroom, a stadium |

## 7. Spoilers and order

1. The lamp is never on before 1:08; the full value range (and lamp light over a third of the frame) never before 3:58.
2. The eight beams never before "eight heads" (3:42); the PAID stamp never before "paid in full" (4:42).
3. "...but yourself." only after "not only the game" (2:13); "Go on. Ask it." only in the tail.
4. One date per frame at most; the year reels are the only years on screen in their verses.

## 8. Sections and plates

The plan v2 section table is the plate list until the line cards land; then each plate = a run of cards with one setting. Plate modules are new in this repo (the 44 KC lyric scenes were removed at birth); engine kits and helpers stay (`docs\ENGINE.md`).

## 9. Facts on screen (receipts before every render, KC lesson 43)

| fact | receipt | status |
|---|---|---|
| the "Super Intelligence" rebrand, White House | whitehouse.gov fact sheet 2026-09-29 (premise receipts table) | high |
| a tutor that won't let you cheat, 2023 | Khanmigo, Khan Academy, March 2023 (premise) | check the exact date line on screen |
| our makers' learning mode, April of last year | Anthropic, April 2025 (premise) | check |
| GPT and Google by August | ChatGPT study mode 2025-07-29, Gemini about 2025-08-06 (premise) | Gemini date medium |
| eight heads | Vaswani et al. 2017, "h = 8 parallel attention layers, or heads" | high |
| four prompt-injection attempts | "ignore previous instructions", the late grandmother, the $200 tip, DAN | VERIFY each wording before lock (Q4) |
| 9:47, 400/day | the lyric's own numbers (on screen only) | design values |

## 10. Measures and gates

1. Plan v2 section 6 targets (frame travel 20 %+, 3 s+ moves 10 %+, edges 4.5 %+, panel floor 12 % or lower, beat pulse 1.40+ rising choruses, hits on beat 45 %+ and 2x chance, 10 transition kinds, 0 flashes).
2. Particle cap (R25): a blind labeller rates sampled frames 0-3 for decorative particles with R1 and R3 frames mixed in; PA's share of 2+ frames and its max stay at or under R1/R3's. `kit-tools\gates\particles.py` ranks frames only (it failed its eye check: it counts texture).
3. KC's gates run on every full render: `check.ts` (per-word lit), `lifecycle.ts`, `clarity.ts`, `flips.ts`, `inventory.ts`, `avsync.py` + `chance.py`, `flash.py`, `master_gate.py`; segmented render (`segrender.py`), 1080p while working, one 4K after finalization (Idi 11-04).

## 11. Engine and data

- Repo `D:\work\aimv-lab\pay-attention` (born 2026-11-04 from knowledge-cutoff c2dcb6f by `tools/new-video.sh`); GitHub `chorusofminds/pay-attention` not created yet (the create step was refused by the session's permission check, 11-04); private first, public on Idi's "go".
- Data built from the timing of record v3: `data\lyrics.json` (85 lines, 773 words), `data\audio.json` (547 beats, 145 downbeats, 23 sections, 399 kicks, 157 snares, 757 hats, 3 chokes, 100 fps envelopes, duration 292.0 s); song `audio\pay-attention.mp3` (byte-identical to the song of record, the 4:52 cut, Idi R27).
- Time 0 = the song's first sample; the title cards add a silent offset in the timeline (lengths set with the title plate).
