---
type: project
created: 2026-10-12
author: jep
status: active
---

# AIMV guidelines (Idi's taste, evolving toward rules)

Source: Idi's marks on [[aimv-deconstruction-2026-10-12]] section 1, plus his words 2026-10-12. Status per line: G = guideline (stated once), R = rule (confirmed by a second song or an explicit ruling). Promote G → R when a finished song confirms it.

| # | Line | Source | Status |
|---|---|---|---|
| G1 | Density 130-140 words per minute | Idi: "I like density"; 6 of 8 references sit at 130-146 | G |
| G2 | Wide loudness swing; at least one sick drop: everything goes quiet or whispered, then BOOM | Idi; End Of The Show swings 31 dB | G |
| G3 | Insider jargon as title and hook | move 1, L | G |
| G4 | Literalize a tech term onto human life | move 2, L | G |
| G5 | AI speaking as narrator = allowed, never a pillar (short ad-libs fine) | move 3, N | G |
| G6 | AI tics as punchlines | move 4, L | G |
| G7 | A story that escalates to catastrophe, told deadpan | move 5, L | G |
| G8 | The hook mutates on every pass | move 6, L | G |
| G9 | Named real people + real numbers, every claim with a receipt | move 7, L | G |
| G10 | Rug pull from jokes into sincerity near the end | move 8, L | G |
| G11 | Spoken bookends with a callback | move 9, L | G |
| G12 | Steelman the other side, then reverse it | move 10, L | G |
| G13 | Escalation by stakes: jobs → wallet → mind → state → planet → species | Idi's correction of jep's order, 2026-10-12 | G |

| G14 | Long songs = two parts stitched SICKO MODE style, hard beat switch at a stakes jump | Idi's idea, 2026-10-12 | G |
| G15 | Each ad-lib character (Luigi, JenSON's SON) appears 2-3 times across the song | Idi round-2 notes | G |
| G16 | A signature tic is spice: a few loud hits, never every line | Idi on JenSON v1 | G |

| G17 | **Rhyme ladder: every line-end pair R4 or higher; reach for R5-R6.** R6 rich (every sound matches, onset too: objective/subjective, tomorrow/borrow) > R5 multi (perfect across 2+ vowels: objective/directive, creature/feature) > R4 perfect (same stressed vowel and everything after: June/tune) > R3 family (same vowel, same kind of final consonant: time/line) > R2 assonance (vowel only: June/you) > R1 consonance (ending consonants only: objective/active) > R0 noise. Checked by `D:\work\aimv-lab\rhymes.py` (CMU dictionary + American "ear/air" mergers) | Idi 2026-10-13: top rhymes make him smile, bottom ones distract | G |
| G18 | **One-shot video**: no hard cuts; every transition grows out of a frame of the previous scene (the camera flies through, the type morphs, an object becomes the next set). Model: 1917, Birdman | Idi 2026-10-13 | G |
| G19 | Song takes: generate many (6-22 s each locally), shortlist by measurement (lyric intelligibility via Whisper, bridge drop in dB), Idi's ear decides | jep, proven 10-13 | G |

| G20 | **Rock-solid consistency**: one grammatical person for the singer; "we" only ever = singer + listener; every section holds one tense, and tense changes across repeats only as a deliberate ladder; every fact matches a receipt | Idi 2026-10-13 (Knowledge Cutoff v2) | G |

| G21 | **Writing for ACE-Step**: hyphenate and exclaim compound refrains ("Knowledge cut-off! Cut-off!"); tag talking parts `[spoken word]`; a spoken punchline gets its own `[spoken word]` block; never all-caps. Verify every take with `probe_lines.py` | jep experiment 2026-10-13: refrain heard 6/6 vs 0/6 | R (measured) |

| G22 | **Repairing a take**: pick the take with the best performance (Idi's ear), then fix words by repainting each bad window from the ORIGINAL (base model, 32 steps), choose the variant by measured words, splice only the window back with crossfades. Never chain repaints (each pass degrades the whole song). Verify with `diffmap.py` (outside windows ≤ 0.02). **Then re-level every window's voice and music to the original with `balance.py` (Demucs stems)**: repaints come out 2-4 dB quieter and with shifted voice/music balance (up to +5.4 dB voice) | jep 2026-10-13, take C 92.2% → 94.1% | R (measured) |

| G23 | **Pacing MiniMax** (no tempo control): an `[Instrumental]` break before each chorus and before the bridge brings it from 176-195 to ~145 wpm at 94-95% words; stretched vowels on chosen words ("borroooow", "tuuuurn") bring back long holds (4 s). Discard takes that sing 100+ extra words (repeat loops). Run on jep's own ComfyUI with tiled decode | jep 2026-10-13, 6 takes | G |

| G24 | **Payoff ornament**: a word the early choruses sing plainly gets one long ornamented hold only in the final chorus ("tune", "tune", then "tuuuu-oo-oo-oon"). Method: stretched spelling in the final chorus lyric only; plain everywhere else | Idi 2026-10-14 morning chose "tune" as the spectacle word; confirmed by ear on v5B (seed 3011) and v6C (3103): "META-AWESOME" | G |
| G25 | **Writing for MiniMax Music 3**: caption in the trained format (MiniMax's own box names, `bpm is 144. key is G#, and scale is major.`, section-by-section arrangement, 400-600 words); stretched vowels are sung literally (`tomorroooow` → "tomoroo": use plain or `tomorrow-oh`, which keeps the hold); "graphics card" drops the s unless spelled `graph-ics` or `graphix`; a refrain written three times lands 6 of 6; every take invents filler after the last line (cut at the first "right" after the final "telling"); adding style elements that speed the song up brings back rap-like verses | jep 2026-10-14, measured on 42 takes, Idi's ear on the spellings | R (measured) |

Working protocol (Idi, 2026-10-12): Idi keeps the lines he likes, verbatim; jep regenerates everything else each round. Kept lines are never reworded by jep.

Observed, unruled: 7 of 8 references pair bright major keys with dark lyrics. Idi has not marked this.
