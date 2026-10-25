---
type: project
created: 2026-10-25
author: jep
status: active
---

# Knowledge Cutoff parity pass, phase 0: the leap, named (2026-10-25)

Follows [[knowledge-cutoff-parity-notes-2026-10-25]]. Three research agents measured full5 against R1 (P(Doom)), R3 (Simulation's Ending), R4 (Run It Again) at 2 frames per second, by script, with the local Qwen worker reading frames and an eye check on 10-37 % of its labels. Reports: kc-engine `reports/p1-leap.md`, `p1-floor.md`, `p1-moments.md`.

**In one line: our frame almost never travels (things move inside a still frame), our words sit beside the picture, the video never rests or bursts, and its darks were grey where every reference tints them.**

**Correction (same day, leap.py v2):** the "x11 slower camera" in row 1 was a measuring artifact: the beat pulse counted as slow camera motion. Re-measured under one rule for every video, KC's camera speed when moving is 8.63 %W/s vs refs 9.0-11.9, and parts moving apart 66 % vs 61-79 %. The real camera gap is how often the whole frame travels (by eye on 8 samples each: refs 3-5 of 8, KC 0 of 8); a calibrated metric for it is being added (leap.py v3).

## The gaps, ranked

| # | gap | KC (full5) | R1 / R3 / R4 | change (bible 16) |
|---|---|---|---|---|
| 1 | ~~camera travel when moving: 0.66 vs 7.4-8.3~~ (artifact, see correction) → how often the whole frame travels | 0 of 8 samples (eye) | 3-5 of 8 | 1-2 decisive whole-frame moves per phrase, on downbeats, holds between |
| 2 | sung line on a plane, a path, or built from objects (labelled by eye, 1 frame per 2 s) | 11.7 % of lyric frames | 35.1 / 18.9 / 21.4 % | the line sits on the plate's own geometry in most plates |
| 2b | letters mid-transformation (eye) | 2.1 % of lyric frames | 6.8-9.9 % | the 24 mapped techniques |
| 3 | parts moving apart from the camera (parallax), in moving frames | ~~29 %~~ 66 % (v2) | 61-79 % (v2) | in range as measured; layers stay, since parallax needs frame travel to show |
| 4 | frames holding a drawn picture | 22 % | 59 / 45 / 31 % | an object or scene in every set-up; paper plates filled edge to edge |
| 5 | still holds of 2 s+ per minute / time in high-motion bursts | 0.31 / 1.3 % | 0.76-1.25 / 2.8-44 % | holds that release into bursts, one burst per chorus |
| 6 | colour in the darks (saturation) | 0.12, neutral grey | 0.18 / 0.21 / 0.50, tinted to the accent | ink and panel lean amber/olive |
| 7 | accent colour area, median frame | 0.96 % | R5 4.4 %, R1 1.6 % | a frame-scale yellow field in a quarter of frames |
| 8 | the line's shape changing while sung | almost never | every moment Idi cited | 24 techniques mapped to 24 lines, each once |

Correction (same day): rows 2 and 2b first used the local worker's labels (KC 4.9 % vs refs 11.6-18.7 %); on the refs it caught about half of what an eye count finds, so both now rest on p1-leap's eye labels (445 frames). Font counts are withdrawn.

**Already level or ahead (leave alone):** text area, words on objects, total motion, frame novelty, anchor presence (KC 96 %, but at hairline scale). The june3 silence and dlss's dark beat match R1's own dark beat in length; dlss gains an object to carry the dark.

## The weakest plates

session and inferred (tied lowest), paced, then letter, june3, dlss. The pattern: a flat paper sheet or UI with the sung line set beside it. The fix in most of them: the line becomes the document's own data (a checklist row, a piano-roll note, a scatter point, the toggle itself), the way R4 and R3 do it.

## The techniques, mapped (top 5 of 24)

1. "Then Spain scored... wrong since then": the line rides a flat prediction curve and turns vertical down a cliff (R1 "drop", from its source code).
2. "It told me I was magic, and it spelled my name": MAGIC becomes dots that re-form as the name on "name" (R1 atoms).
3. "Every trick I ever pulled was something I'd inferred": rows cycle typefaces and settle one per beat (R5 INSTRUCTIONS).
4. "You have to type it all again": the line's past drifts up-left while the present types (R1 Gato).
5. "...and I don't have the receipts": RECEIPTS bounces and loses letters (R5 LOSE).

Full table (24 lines, cost, conflicts): kc-engine `reports/p1-moments.md` section E.

## Next

Kit wave (camera grammar, tinted darks + layers + frame-scale anchor, line-geometry and glyph techniques), then the four plate owners, critics, one render (full6), measured on these same numbers with a new gate script.
