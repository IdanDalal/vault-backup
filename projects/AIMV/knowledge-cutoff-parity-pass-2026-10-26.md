---
type: project
created: 2026-10-26
author: jep
status: active
---

# Knowledge Cutoff: parity pass done, full6 rendered (2026-10-26)

Follows [[knowledge-cutoff-parity-notes-2026-10-25]] (your reference notes) and [[knowledge-cutoff-parity-phase0-2026-10-25]] (the leap, named and corrected).

**Watch:** `D:\work\AIMVs\ours\video\full6\kc-full-1080p.mp4` (194.1 s, 1080p60; render full6b). Sheet: `full6-sheet.png` beside it.

## What changed, by gap (bible section 16)

| gap | full5 | full6 | refs R1 / R3 / R4 | what you will see |
|---|---|---|---|---|
| whole frame travels (blind eye, 80 samples each) | 10 % | **16.2 %** (target 20 %, not met; gain within noise) | 55 / 15 / 20 % | decisive camera moves on downbeats: crane, truck, orbit over the cutting mat, the globe trucked whole, a bullet-time orbit in cutoff5, beat reframes in cutoff6 |
| holds of 2 s+ per minute | 0.31 | **0.93** | 0.76 / 1.21 / 1.25 | the camera stops dead and only the type acts (session, extratime, tune1) |
| burst share | 1.3 % | **8.7 %** | 44 / 2.8 / 15.6 % | one burst per chorus, the biggest in the final |
| colour in the darks (saturation) | 0.12 | **0.33** | 0.18 / 0.21 / 0.50 | your tint: warm brown-black (ruled 10-25) |
| accent area, median | 0.96 % | 1.12 % | 1.6 / 0.7 / 1.9 % | in range; slabs only where a hero word earns one |
| fine detail (edges) | 3.80 % | **4.14 %** | 5.9 / 5.1 / 4.0 % | engraved linework inside subjects |
| frames 60 %+ empty | 13.6 % | **11.1 %** (moved away) | 28.7 / 32.3 / 15.8 % | the floor raises filled the weak paper plates edge to edge |
| lines whose shape is their meaning | a handful | **the 24 mapped lines** | every moment you cited | see the technique list below |

## Your cited moments, as built (one per line, each once)

R1 "drop", on "Then Spain scored": the line rides the prediction curve and "scored" falls vertical into the net, the frame following. R1 atoms, on "magic,": dots that re-form as "name". R5 INSTRUCTIONS, on IN/FERRED: rows cycle typefaces and settle on the beat. R1 Gato, on "type it all again": the past drifts up-left while the present types. R5 LOSE, on RECEIPTS bounces and loses letters. R1 "in your training loss", on "Everyone I meet is coming from tomorrow" on a road in perspective. R5 "your voice and mine", on "And you're telling me who I turned out to be": two faces converge into one line. R4 BREATH, on "page by page, and slowly turn": four faces, letters at their own speeds. R2 checks, on TRUE built from the receipt's checkmarks. R4 every language, on TUNE's cells cycle notes and end on `?`. R2 mocked, on CHECK as a dashed outline inside the switch. R2 nobody knows, on "I can't check a" decays into code. R3 ceiling, on "a little younger than the year" bends flat against a ceiling. R3 draw distance, on "out there," fades past the fog. R3 tile shatter, on the page wall fills syllable by syllable (BUT, NEV-ER, GET, A), shatters, lands as TURN. R1 GPU grid, on CREATURE in lit cells. R1 fuse, on a spike runs the axon and reaches each word on its onset. R1 SERVANT/BOSS, on the frame rolls on "turned". R1 FOOM, on BEATS steps widths on 16ths. R3 garbage collection, on the session's old words shred. R3 gravity, on jimothy's words drop and tumble. R4 river, on a ribbon widens toward the library slip. R1 blues, on "You're humming something new" stands on the pitch string. R1 wave, on Messi's line rides a wave that flattens.

## Gates on the whole render

Measured on full6b (the copy you watch): 4K check 483/483 words lit, negative control 0, 0 issues; beat pulse 2.07 whole, choruses 1.94 < 2.35 < 2.44 (rising; full5 2.51 / 2.63 / 2.77); timing -17 ms; flips 1 allowed; loop 39.4 dB; tail silent; meta 0; text repeats 31 (full4 55, full5 29: the two added are the dictionary's part-of-speech labels and the next-token menu's "time"). Three critics (choruses, verse a, verse b) reproduced the owners' numbers; their fixes are in. After full6, the lead's own look at every sung line found four flaws the gates missed (the pitch string reading as a strike-through on "You're humming something new", an empty [MASK] box in paced, two worded repeats); fixed and re-rendered as full6b, checked at full size. Receipts: kc-engine `out/full6b/gates/`, `reports/p2-*.md`, `reports/critic-p2-*.md`, `reports/p2-full6-eye.md`.

## Trade-offs, for your eye

1. **Beat contrast is about 8 % lower** (2.26 to 2.07 whole; choruses 0.2-0.6 lower), still about 35 % above the refs (1.5). The bursts and camera moves move the whole frame between hits. If the beat feels weaker than full5, the bursts get tuned.
2. **The page wall repeats syllables on purpose** (BUT x10, NEV-ER, GET, A at 147-149 s): "handed every page at once" as a wall of pages that all say the same thing. Your no-repetition rule is near; strike it if it reads as repetition.
3. **Negative space went down** (13.6 to 11.1 % vs refs 16-32 %): the floor raises filled the paper plates. The empty moments live in dlss's dark beat and the june3 silence.

## Not met, honestly

1. **Frame travel**: 16.2 % by an independent blind count (the plate agents' own counts ran 1.3-2x high: they knew where their moves sat). Level with R3/R4, far from R1. Moves are packed into two beats, then still, so most moments land on a still frame.
2. Line 21 ("Then Spain scored") and the june lines score 3/6 on the subtitle meter (accepted).

## Lessons kept (memory)

The local model chooses where Claude looks, never states what is true (your ruling A); a by-eye gate counts only from an independent labeller; agents report once.
