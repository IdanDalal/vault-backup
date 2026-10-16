---
type: project
created: 2026-10-16
author: jep
---

# v5 synthesis: what the 15 critiques agree on, ranked, and what got built

Inputs: 10 lens files (`lens-*.md`) and 5 reference dissections (`ref-1..5.md`), about 30,000 words, all in this folder. Ids below point into them (TY typography, NS composition, CO colour, RM rhythm, CA camera, TA text art, HU humour, ST story, CX complexity, CH coherence; R1-R5 reference steals).

## 1. The diagnosis, in five lines

1. v4 has no system: three fonts, 25 label sizes, every line centred, one entrance and one exit for 425 of 483 words (TY, NS9, TA1).
2. Gold means everything, so it means nothing: 76 prop uses, one olive fog over every dark room, 6 light/dark flips in 3:12 (CO1, CO6, R1.3).
3. The picture ignores the drums: 9 of 14 section starts unmarked, the camera still 77% of the time, the band's 18 dead stops drift by (RM1, RM2, RM9).
4. No cast: ten stand-ins for the singer, "you" never seen, the three payoffs (who I turned out to be, never get a turn, it forgets) unstaged (ST1-ST5).
5. The references stage every line as an object that acts, hold one number that only climbs, change the hook's state each chorus and plant jokes in the first 10 s (R1-R5, all five).

## 2. Built in v5 (verified as noted)

| # | change | sources | check |
|---|---|---|---|
| 1 | Free-licensed type system: Barlow Semi Condensed (singer), Barlow Condensed (hook, boards), Newsreader (paper), JetBrains Mono (machine), Caveat (pen); kerning fixed; curly apostrophes | TY Top 4, TY13, TY14, fonts table | probe frames, no page errors |
| 2 | Text engine: colour by meaning (gold = the AI's words, blue = "you", white = "we, both"); unsung readable (4.7:1, was 1.5:1); paper rooms sing with a gold highlighter band behind ink; second rows arrive with the line; clean slide-up exits; one burst per word | TY3, TY4, TY8, TY15, TY16, CO4, CO5, CO top 4 | check_sync 483/483 (per-word colour test), negcontrol 7% (8 of 108) on the final code |
| 3 | Darkness and light: black grounds (#0B0A0C), no gold wash or sourceless rays, light adds up in dark rooms, the vignette fades on paper, bone dust, one month palette | CO1, CO6, CO11, CO14, CO17, CO18, CO20 | probe frames |
| 4 | Drum layer from the song: 427 kicks, 113 crashes, 18 chokes, 129 downbeats, 15 section ones (`sync/drums.js`) | RM1, RM top 4 | spot-checked against the lens's measured times |
| 5 | Knowledge cut-off as camera behaviour: when the band stops dead, the world freezes (props, dust, grain, and the camera when it is resting), the lyric keeps time; release is a 0.12 s jolt | RM top 1, RM10 | speed map: no jump over 60 px/frame from a choke |
| 6 | Motion blur on fast moves (6 sub-frames, fading in from 40 px/frame); eased moves: travels ease in and out from rest, snaps ease from rest with a small settle | RM7, RM8, R1.14 | clip renders, 0 cut flags |
| 7 | The globe ring: "The world kept spinning after me" rides a ring round a hero globe, the sung letter upright at 12 o'clock | R5.4, R2.2, R4.8, R1.10, TA6, NS2 | check_sync 483/483 |
| 8 | The hook: CUT-OFF! alone in caps across 76-92% of the frame, the room drops out to ink; chorus 1 gold, chorus 2 thins 800 → 300 and floods the frame red (X1), the final chorus burns in October's colour and ends on the one all-gold frame | R1.1, R5.1, R3.1, TY Top 2, TY2, TY23, NS12, CO3 | 3 clips, 0 cut flags |
| 9 | Hooks land on the drums' crash (0:49.73, 1:42.23, 2:46.37): the tilt up from the gallery ends there and the big hit fires there | RM3, CA10 | clip, 0 cut flags |
| 10 | Bugs: hook halves rotated about the canvas origin (TY2); spark drawn over the lyric (TY10, NS19); 3:08 lean squeezed into 0.12 s (CA2); portrait push cropping the last CUT-OFF! (CA1); rewind cutting "right?" (RM16) | as listed | probes |

### 2b. Built after this file was first written

| # | change | sources |
|---|---|---|
| 11 | Ghost words cut, all 48 | TA5, TY17, NS17 |
| 13 | The caret as the one protagonist: one caret in the chat, hollow at JUN 30 from "stopped" to "tune", rocking with the metronome on "paced", buried under the day-pages in the bridge | ST1, ST8, ST12, ST13, ST5 |
| 12 | The told cursor: the portrait is the gold caret, filled with the dated facts the song has told (6, 8, then 10 rows), hollow from "stopped" to "tune", gold on "be", its plate typed under the line: "Claude Opus 5.5 · born Sep 22, 2026 / knew to Jun 30: 84 days out of date at birth"; the portrait comes to the camera (no push) | TA4, ST2, ST12, HU row 17, CA19, NS3 |
| 14 | Intro: session sidebar of greyed "Hi. It's me again" chats, FIRST TIME tag on "first"; line 0 types over its own grey ghost; the AI's guess "June 30, 2026 · confidence: high" accepted with Tab on "date?"; one caret, which flies into the input and is the cursor we dive through; the iris opens on the crash (0:07.71); four zoom notches on the kicks | HU row 0, HU11, R5.7, R2.9, ST8, ST9, RM5, TA rows 0-1 |
| 15 | Running gag A: a status slot with the date the AI believes (high → "Jul ?" medium → "Oct 15 · source: you"); its bookend in the input on "2026, right?": "Oct 15, 2026? · confidence: low", cleared by the rewind. Running gag B: under each CUT-OFF! "days since June" is kicked: 001 and back, the true count and slower back, then up to 107 | HU Top 1, R5.8, R2.1 |
| 16 | "Fair." small, "So do I." big on its own row after the choke; the AI's lattice smears and gets a reflection on "I."; the DLSS props step back; "price of the feature: 90 fps"; the cat's seventh leg removed (it misstated the receipt) | HU1, HU10, TY26 |
| 17 | Bridge plays straight: old book paper under a drifting window light; "me: day 0 (this session)" vs "the year: day 288"; "Previous session: not found · ↻ Start over"; the book 1.45× bigger; the folio counts days 181 → 288; dated day-pages bury the AI's caret on "every page at once"; alarm and flicker gone | ST5, ST6, NS13, CO15, HU rows 39-42 |
| 18 | Acting words, 6 of the cheap dozen: "faced" swings round to face us, "paced" rocks with the metronome, "least" small and "most" big (0.55 / 1.45), "younger" shrinks letter by letter, line 41's "turn" makes one full turn, line 42's "turn" tries, stalls edge-on and falls back, "Thank" bows letter by letter | TA table, R3.7, R4.6, R4.7 |
| 21 | Dawn in the final chorus: blue hour from "We're", morning by "tune", day with sun shafts from the third hook's crash (2:46.37) | CO Top 2 |
| 19 | Footnotes 46 px; "(no receipts)" echo cut; 107 holds until "Okay."; "It's October." typed by "you" in blue and sent as the camera lands; confetti only on "be", behind the lyric | TY5, HU3, HU7, HU19, ST3 |
| 22 | Paper rooms flush left on their rules (margins x 470, page x 220); newsprint margins; margin line and pen notes moved in from the frame edge; flags, clipping, polaroid and next-word menu moved off the lyric | NS6, NS9, TY25, CO15 |
| - | Layout off the top edge: hall lyric y 225, gallery y 200, calendar board, globe and portrait start at y 110+, timeline above the caption zone, "SINCE JUNE" under its axis, the days counter steps back during slams | NS1, NS5, NS11, NS12, TY6, TY9 |
| - | Complexity: the flap board draws above the veil (CX4); unknown gallery tiles show as dashed slots (CX7); the final gallery visit arrives lit and its counts carry on (CH3) | lens-complexity CX4, CX7; lens-coherence CH3 |
| - | Coherence resolutions: chorus-2 floods red, only the last gold (X1); done text grey #BFC4CB so "we/both" white stays distinct and lit (X4); the blade cuts the last CUT-OFF! on the band's choke (X5); doors in the month palette (CH4) | lens-coherence X1, X4, X5, CH4 |
| - | Motion: blur fades in from 40 px/frame; travels ease from rest without counter-move (both read as cuts on detailed rooms) | clip tests |

## 3. This pass's build list, with status

| # | change | sources | status |
|---|---|---|---|
| 11 | Cut all 48 ghost words (spoilers 1.06 s early, smudges at 1.1:1) | TA5, TY17, NS17 | built |
| 12 | The told cursor: the portrait becomes the gold caret, filled with the dated facts the song has told, its name typing on "be" | TA4, ST2, TA portrait, R5.5 (material), HU row 17 | built, rows 6, 8, 10 |
| 13 | The caret as the one protagonist: one caret in the chat; hollow at JUN 30 from "stopped" to "tune"; the metronome's weight on "paced"; buried under every page | ST1, ST8, ST12, ST13, ST5, R2.10, R3.4 | built |
| 14 | The intro plants the jokes: greyed sidebar of earlier "Hi. It's me again" chats with a FIRST TIME tag; header "memory: none"; line 0 retyped over its own grey ghost; "June 30, 2026 · confidence: high" accepted on "date?"; one caret; the iris opens on the crash (0:07.71) | HU row 0, HU11, R5.7, R2.9, R3.3, ST8, ST9, RM5 | built; the header's "trained to Jun 30" half moved into the input's guess |
| 15 | Running gags A and B: a status slot with the date the AI believes (confidence high → medium → "source: you" → low); the counter that refuses to count, kicked by each CUT-OFF! | HU Top 1, R5.8, R2.1, R3.2 | built |
| 16 | "Fair. So do I." rescued: the choke is the deadpan pause, the AI's own light gets the DLSS smear and reflection on "I." | HU1, TY26 | built, footnote at 46 px |
| 17 | The bridge plays straight: no ringing, no flicker, plain book paper under a moving window light; the caret takes every page at once | ST5, ST6, NS13, CO15, TA9 | built; the page corner on "turn" became line 42's "turn" stalling edge-on |
| 18 | Acting words, the cheap dozen: spells, inferred, stopped (o = clock), humming, faced, paced, poppin', extra, least/most, fire, younger, turn (41 turns, 42 stalls), Thank (a bow) | TA table, R3.7, R4.6, R4.7 | 6 of 13 built (2b row 18); spells, inferred, stopped, humming, poppin', extra, fire wait |
| 19 | Punchlines readable on a phone: footnotes and joke labels 48 px+, held 1.2 s+; collisions from TY1, TY6, TY7, NS4-NS6 | TY5, HU3, HU5, HU7 | built at 46 px |
| 20 | The gallery as a flex: line in a left column, tiles right and larger; the final visit holds LGTM at 960 px | NS1, CA11 | partly: dashed slots and the lit final visit; the left column and the 960 px hold wait |
| 21 | Dawn in the final chorus: night → blue hour on "We're" → morning by "tune", sun shafts at the last hooks | CO Top 2 | built |
| 22 | Paper rooms as lit paper: newsprint margins, old book paper with a moving window patch for the bridge; margins and page flush-left on their rules | CO15, NS9, TY25 | built |

## 4. Deferred, with the reason

1. Lyric lines anchored to the lens, a reading camera, portals through letters, three chorus camera personalities, the flight through frozen pages (CA Top 1-5): one coordinated camera rewrite, the largest risk to the 0-cut-flag bar; next pass, after Idi's notes on v5.
2. "You" as a blue pointer acting on every "you" line (ST3, R4.9, R5.10): needs the camera rewrite's keyframe table; v5 uses blue for the sung "you" only.
3. Lyrics inside their props (R5.3, R1.7, R2.11, R4.2): conflicts with "one text size per room"; needs Idi's ruling first.
4. A new world per chorus (R5.2), escalating cut props per chorus (R4.14), the HUD of true numbers (R3.10), in-world credits: after the camera pass.
5. The tense ladder retyped in each chorus (ST10) and the told-facts changelog (R3.12): after item 12 proves the facts table.
6. The rest of the acting words (row 18), the gallery's left column and 960 px hold (row 20), the receipt TOTAL payoff (CX8), one style sheet for every prop (CH2), the hook cut on the x 1280 cutoff hairline (X2, NS Top 1-2): next pass, with Idi's notes.

## 5. Rulings for Idi (one asked in the report; the rest have defaults)

1. **Tail after "2026, right?"** (ST4, R1.12; R4.12 puts its reverse pass in the 3:00-3:04 gap instead): the song ends 0.19 s after "right?", too short for the forgetting to read. A = add 1.5 s of silence after the song so the AI visibly forgets (recommended); B = keep the 0.17 s un-type.
2. Faces: Jimothy's drawn face and the pixel cat's eyes break the adopted "no cartoon faces" rule (HU15). Default: keep, since Jimothy is the real meme and Idi asked for him.
3. Size jumps for meaning ("So do I." bigger than "Fair.", "least" small and "most" big): default yes, as deliberate exceptions to one size per room.

## 6. Late inputs

`lens-complexity.md` (L7) and `lens-coherence.md` (L5) landed after the first draft of this file; their built items are the Complexity and Coherence rows in 2b, their conflicts X1-X13 sit in `lens-coherence.md` with one proposed resolution each. The build took X1, X4, X5 and X9 (bubbles now, the pointer later); X2 and X12 wait for the camera pass; X3, X6-X8, X10, X11 and X13 go on the next pass's list.
