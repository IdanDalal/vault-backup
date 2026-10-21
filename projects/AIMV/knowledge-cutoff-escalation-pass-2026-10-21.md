---
type: project
created: 2026-10-21
author: jep
status: active
---

# Knowledge Cutoff: escalation pass done, full5 rendered (2026-10-21)

Follows [[knowledge-cutoff-notes3-2026-10-21]] (your 11 notes on full4).

**Watch:** `D:\work\AIMVs\ours\video\full5\kc-full-1080p.mp4` (194.1 s, 1080p60; this is render full5b, see "One fix after the render"). Sheet, one frame per 4 s: `D:\work\AIMVs\ours\video\full5\full5-sheet.png`.

## Your 11 notes, as built

| # | note | what you will see | verified by |
|---|---|---|---|
| 1 | chorus hop retired | kept retired; each setting's own landing | your word on full4 |
| 2 | "You're a wizard, Claude" | the letter reads it, "wizard" underlined twice | engine 4c6df8e |
| 3 | nothing twice, build to the final chorus | every recurring element on a ladder; the final chorus changes count, scale, camera, damage, time of day and interaction at once | escalation sheet per family; 3 critics; text repeats 55 → 29 |
| 4 | cut ladder | cuts per stamp 1, 2, 4, 8, 16, 32 (189 in all); the pieces pile into a heap (hourglass) that grows 1 → 35 % of the frame; cutoff6 turns to sand; the last blade stands in the heap | every-frame strips at all landings |
| 5 | time passing + mystery | the caret = the model's stopped clock, its shadow = the world's clock (a sundial, longer each visit, gone in the outro); one native clock per plate (stuck seconds flap, darkroom timer, Moon phase and seasons on the globe, liquid clock); 12 holes (`?`, blanks, the dater) open through verse 1 and fill toward the outro; the date fills last, on screen at 185.85 ("It's October."), and empties back to `?` at 192.60 for the loop | critic-e1-vb point (b), outro strips |
| 6 | pages = real days | 128 page-a-day leaves (June 16 to October 21), 30 with short headlines in our words, Moon phase drawn, no month names, October blank; a powers-of-ten pull back through the wall; no frames of the video anywhere | 30/30 headline days checked by script against sourced facts |
| 7 | the model's colourful commentary | 28 asides, `›` prefix + confidence chip, naive early (99 %) to knowing late; 4 plates stay silent on purpose | aside-collision check (new) 0 issues; 13.3 word rule |
| 8 | fps chart in words | dlss: no numbers; `buttery`, `like a dream`, `smooth` up top, `janky`, `slideshow`, `unplayable` below; rides high under RTX OFF, dives after RTX ON | critic-e1-vb |
| 9 | 2.5D depth | a perspective stage in six different forms: born floor, jimothy field to the horizon, dlss exploded card, pages wall pull-out, june3 flaps falling, tune3 corridor | strips at each depth move |
| 10 | R3 craft | fly through the O of KNOWLEDGE, window pushes, power-off, line match, tile flip, pull-back reveal, pixel mosaic + noise resolve, the liquid AGAIN tank, BE built from the pages leaves, frame-rate stutter in cutoff5 (world at 10.8 / 5.4 / 2.7 fps, caret at 60) | strips per transition; each kind at most twice |
| 11 | GTA VI + box office | `We got a new AI music genre before GTA VI.` (tune2); `Spider-Man made $2.5B. 0.26% of Anthropic's valuation.` (spinning2); The Odyssey and Spider-Man on page-a-day leaves | sourced: Box Office Mojo 2026-10-16, Series H $965B (2026-05-28) |

**Correction on note 11: your "0.01 % of Anthropic's market cap" is 0.26 %** ($2,516,315,789 / $965B). The line says "valuation": Anthropic is unlisted, so it has no market cap. Redo the number if it lists before release.

## Whole-render gates (full5b vs full4)

| gate | full4 | full5b | target |
|---|---|---|---|
| 4K check: words lit / issues | 483/483, 0 | **483/483, 0** | 0 issues |
| beat pulse gain, whole | 2.16 | **2.26** | 1.40+ |
| choruses 1 / 2 / final | 2.43 / 2.57 / 2.69 | **2.51 / 2.63 / 2.77** | rising |
| kick / snare, whole | 1.73 / 2.31 | 1.75 / 2.35 | 1.30+ / 1.40+ |
| timing vs drum hit | -15 ms | -17 ms | -40 to -5 |
| light/dark flips | 1 allowed | 1 allowed (184.33 whip) | 0 not allowed |
| loop first vs last frame | 39.45 dB | 39.46 dB | = full4 |
| tail | -91 dB | -91 dB | silent |
| text repeats (inventory) | 55 | **29** | down |
| meta words | 0 | 0 | 0 |
| subtitle meter above 2/6 | june1, june3 (3/6) | same; spoken outro lines exempt | 0-2/6 |

Receipts: `D:\work\aimv-lab\kc-engine\out\full5b\gates\` (check4k.json, avsync.log, inv/, flips.log).

## One fix after the render

full5's 4K check found one stacked frame at 1:48.58 (KNOWLEDGE over KEEPS and the globe for one frame). Cause: a cut sitting exactly on a frame time, inside the motion-blur shutter, so both pictures blend into that frame. 14 of 63 cuts sat that close (full4 had them too; only this one put a word on a word). The beat grid now steps every cut 2 ms clear of the shutter; re-rendered as full5b, checked frame by frame at the same spot: a clean cut. One cut (extratime, 1:11.08) now lands 41 ms before its beat, 1 ms past the 40 ms tolerance, because the next word lights too soon for the other direction; it is allowed by name.

## How it was made

Four plate agents (hook, chorus, verse-a, verse-b), a shared-window measure, three critics, fixes, one whole render plus one corrective re-render. Every critic reproduced the owners' numbers within 0.03. Engine commits 987e360 to 620b44a+ in `D:\work\aimv-lab\kc-engine`; all lead rulings in `reports/e1-lead-rulings.md`. New tools: an aside-collision test in check.ts, a whole-render gate script `gates-full.sh`, a shutter audit `scripts/shutter-audit.ts`.

## Open, small (next pass, or leave)

1. Final-chorus snare 2.52 vs full4 2.71: the one number that did not rise. turnedout3 alone now beats its target (3.23); the loss sits in june3 (power-off) and cutoff6 (sand pour fills the gaps between hits).
2. verse1 beat gain 1.86 vs 1.91.
3. Two strings read short: the younger aside (1.6 of 1.75 s), borrow1's receipt label during the line match (0.5 s).
4. june1 and june3 lines score 3/6 on the subtitle meter (same as full4).
5. The outro date reads `21 · 10` (the day made). If you publish on another day it still reads as a receipt.

Next: your eye on full5.
