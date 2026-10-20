---
type: project
created: 2026-10-20
author: jep
status: active
---

# Knowledge Cutoff: the typography pass (2026-10-19 to 10-20)

Verdict: **the lyrics are sung now, line by line, each in its own layout; no line reads as a subtitle row any more.** Watch: `D:\work\AIMVs\ours\video\full4\kc-full-1080p.mp4` (sheet `full4-sheet.png`, 24 frames). Follows [[knowledge-cutoff-rhythm-pass-2026-10-19]]; rules in [[knowledge-cutoff-treatment-2026-10-17]] section 5 (rewritten) and 5.3 (amended).

## 1. Idi's ask, and what the analysis found

Idi, on the rhythm-pass render: "We're listing the lyrics instead of singing them. The words should dance and be artistically, creatively displayed, not just left-to-right and top-to-bottom like every document ever."

| finding (kc-engine `reports/type-ours.md`, `type-r123.md`, `type-r45.md`) | number |
|---|---|
| lines scoring 6/6 on the subtitle score (one size, shared baselines, rows, full-width band, static, shown dim before sung) | 16 of 54, all verse lines |
| lyric screen time at 5/6 or 6/6 | 41 % |
| how early a word showed before it was sung | median 0.7 to 1.8 s (the whole line, dimmed) |
| references (R1-R5) using a plain line in a chorus | 0; plain rows only where the world itself types (chat, terminal, headline) |
| bug | at 4.917 s line 2 typed over line 1 ("WhatIt's"); no check tested lyric over lyric |

## 2. What changed

| layer | change |
|---|---|
| system (bible 5, rewritten) | a word appears when sung, lands in 2 to 4 frames; no dim copy ahead of the voice (unknown words show as [MASK] blocks, the model's own blindness); one hero per frame, the rest 3x smaller and 36 px or more; every line designed for its meaning: hero word, acting word (it does what it says), setting tied to the plate's object; no two neighbouring plates share a setting |
| engine | per-word lyric kit (`_kc-type.ts`); per-word title-safe, lyric-over-lyric and struck-ghost checks; machine-wide render lock in `kc.sh` |
| verses 1-2 (lines 1-10, 25-26) | first typed into the composer; the letter in a slanted hand with MAGIC on the highlighter; INFERRED split `in·ferred`; the line placed by time on the born axis; TOMORROW crossing the June edge into a [MASK] slot; borrow 2 as bubbles, then a stamp pile |
| verse 3 and bridge (19-24, 35-39) | FACED under the headline; PACED walks out to the 16ths; AGAIN slams beside the cup; WRONG stamped askew; MOST at the plot's glowing dot; the raster sets words by sung time; LIGHT lit by its own token tick; PIXEL-PERFECT in pixels; HALLUCINATE re-guesses its glyphs |
| choruses (12-18, 28-34, 45-51) | the line on its sung melody under the roll; the claim line across the form's columns (MADE over CLAIM, TRUE over SAYS YOU); the toggle line crossing the divide to YOU; "spinning after" turning on the globe's parallel with ME fixed on the caret; turnedout typed into a REMARKS form field, BE stretching beat by beat |
| outro and bridge plates (40-43, 52-54) | WAKE stands up; YOUNGER slides back along the ruler; TYPE typed huge in the composer; one word per page, TURN turning with the leaf; PAGE stamped on all 53 prints at once; "October." copied out of your bubble |
| critic fixes | 4 critics, every FIX applied: the per-beat lift of whole lines (it twitched and printed twice inside a frame) replaced by a hop on the sung word only, eased; the beat moved into the objects (page pushes, counters, receipts, replies, score bug, plot gridlines); 16 plate-end words carried across their cuts until sung end + 0.2 s |

## 3. Verified, and how

| check | rhythm pass (full3) | now (full4) | target |
|---|---|---|---|
| subtitle score per line | 16 lines at 6/6 | every line 0 to 2/6 | 3/6 or less |
| whole-song 4K check | 483 / 483 on time, 0 issues | 483 / 483 on time, 0 issues, 70 set-ups at type scale | green |
| beat pulse gain, whole video | 2.07 | 2.16 | 1.40+ |
| choruses 1 / 2 / final | 2.32 / 2.45 / 2.53 | 2.43 / 2.57 / 2.69 | 1.45+, rising |
| verse 1 / 2 / 3 / bridge | 1.92 / 1.67 / 1.37 / 1.81 | 1.91 / 1.77 / 1.48 / 1.76 | below their choruses |
| kick / snare gain | 1.74 / 2.19 | 1.73 / 2.31 | 1.30+ / 1.40+ |
| vocal gain (guard) | 1.38 | 1.33 | 1.10+ |
| graphic hits on the beat / spikes on a drum hit | 55 % / 25 % | 61 % / 28 % | 45 %+ / 25 %+ |
| hit timing vs the drum | 16 ms early | 15 ms early | 5-40 ms early |
| stillness / null control | 2 % / 0.84 | 2 % / 0.83 | 10 % or less / under 1.0 |
| light/dark jumps | 2 (allowed) | 2 (the same, allowed) | 0 open |
| text inventory | meta 0, repetition 53, reading 38 | meta 0, repetition 55 (turned pages list their words), reading 39 (the greeting recalled in borrow 1 for 1.2 s) | meta 0 |
| loop seam (first vs last frame, encoded) | 39.45 dB | 39.45 dB | unchanged |

Per group, after the last edit (receipts in kc-engine `reports/type-a.md` 7-8, `type-b.md`, `type-c.md`, `type-d.md` 5):

| group | lines | check.ts 4K | beat gain, mine / full3 |
|---|---|---|---|
| type-a | 1-10, 25-26 | 95/95 + 20/20 lit, 0 issues | 1.83 / 1.83, 2.30 / 2.32 |
| type-b | 19-24, 35-39 | 71/71 + 51/51, 0 issues | 1.78 / 1.73, 1.52 / 1.40 |
| type-c | 40-43, 52-54 | 59/59, 0 issues | 1.67 / 1.76 (younger+pages), 1.86 / 1.96 (outro) |
| type-d | choruses | 62/62, 65/65, 67/67, 0 issues | 2.37 / 2.35, 2.56 / 2.29, 2.96 / 2.48 |

Render: one detached run, 11,646 frames, exit 0, 820 s, only the two resource 404s every render prints. jep looked at 24 frames of the encoded video (sheet).

## 4. Rulings jep made (overrule any)

1. Vocal gain may fall below full3: hero sizing makes most words small, and the meter measures changed area. No flashes or inflated words to win it back.
2. Short words at a cut are carried across it; the cuts stay where the rhythm pass put them.
3. Bible 5.3 amended: in the choruses each setting's landing (slam, drop, stamp, the fall from the roll) replaces the per-word hop, which the bible records as your most-liked look from v2 to v6; in the verses only the sung word hops. Reason: each landing already carries a lift and a settle (kc-engine `reports/type-d.md` section 1); a hop on top was not tried. If you miss the hop at speed, say the word and it comes back on the sung word, eased.
4. The camera's beat punch from the rhythm pass stays as built (see 5.1).

## 5. For Idi's eye

1. The camera punch: on every beat the whole frame zooms up to about 4 % in the final chorus, in one frame. Big words near the edge jump 5 to 25 px (YOU in the toggle, 165.25). You saw it in full3 and liked the beat; it now shows more because the words are bigger. One number per section if it reads as shake.
2. Line 45 (157.9, "we both know the tune"): words sit on their sung pitch, so the row climbs and dips; the reading-order measure calls it 0.44. Judge at speed.
3. Still short of sung + 0.2 s: "receipts" (27.66 against 27.79, a hard cut with nowhere to carry it), "tomorrow" in borrow 1 and 2 (0.05 and 0.08 s short); younger+pages beat gain 1.67 against 1.76.
