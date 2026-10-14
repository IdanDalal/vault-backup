---
type: project
created: 2026-10-14
author: jep
status: active
---

# Knowledge Cutoff - 9 style auditions

Why: Idi (2026-10-14) can't pick from music jargon ("I have no idea what any of them sound like"), so he picks by ear. Same lyrics (`kc\lyrics-mm-p4.txt`), one MiniMax prompt per reference song (`D:\work\aimv-lab\kc\aud\cap-1.txt` ... `cap-9.txt`, trained format, built from the ear's description + measured tempo, key, voice). Previous: [[reference-deconstruction-2026-10-14]].

## Listen here

`D:\work\AIMVs\ours\auditions\`

- `0 - PREVIEW REEL (all 9, first chorus each).mp3`: 6:13, a spoken number before each clip, each clip = first pre-chorus through first chorus.
- `1 - like Count Me In.mp3` ... `9 - like The Way I Look At You.mp3`: full songs, invented filler after the last line cut off.

## How each was chosen (receipts)

18 takes generated (2 seeds per style). Per style jep kept the take that the ear says sounds most like its reference with the fewest of Idi's past complaints (rap-like verses, "theatrical", piano), then words heard.

| # | Like | Take | Words heard | Ear says (first line) | Watch for |
|---|---|---|---|---|---|
| 1 | Count Me In | 2101 | 97.1% | energetic futuristic synth-pop | rap-like verses (the original has them too) |
| 2 | P(Doom) | 2201 | 96.7% | spoken intro, driving synth-pop | none flagged |
| 3 | Ignore Previous Instructions | 2302 | 95.1% | spoken intro cut by a glitchy tape-stop | none flagged |
| 4 | LGTM | 2402 | 96.5% | energetic, funky pop | none flagged |
| 5 | System Prompt | 2501 | 95.5% | energetic synth-pop | "almost rapped" verses |
| 6 | The End Of The Show | 2601 | 96.1% | theatrical funk-pop, slap bass (male) | "theatrical" |
| 7 | The Simulation's Ending | 2702 | 94.9% | modern electropop | synth piano under the spoken intro |
| 8 | Thus Spoke Compute | 2801 | 96.5% | theatrical show tune, cinematic, orchestra + choir (male) | intended: villain number |
| 9 | The Way I Look At You | 2902 | 91.2% | theatrical pop-rock, piano-driven (male) | **missed**: asked for guitar-led indie pop |

Dropped: 2701 (looped lines, 58.8% words), 2901 (ran out of time mid-line, no outro).

Findings:

1. MiniMax added piano in 5 of 16 takes although no audition prompt mentions piano: it is partly MiniMax's own habit, mostly in the theatrical styles. Correction to [[reference-deconstruction-2026-10-14]] B-section 8.6, which blamed only our prompts.
2. Every take ended early and invented 6-84 s of filler; the cut rule (first "right" after the final "telling") verified on all 9 picks by re-transcribing the endings.
3. Several takes double the last word ("right? Right?") inside the song itself.

## Feedback (Idi, plain words, 2026-10-14)

1. Almost all sing "tomoroo", "borroo" (jep: the stretched spellings `tomorroooow`, sung literally).
2. Almost all sing "graphic card", no "s".
3. Piano is fine; earlier complaint = piano was nearly the only audible instrument.
4. **Best = 3 (like Ignore Previous Instructions)**: long holds, sick drops, great beat, fitting voice, poppin' "Wooh! Wooh! Wooh!" chorus backings, sang "Knowledge cut-off! Cut-off! Cut-off!" (three times: "fits SO WELL").
5. Second = 7 (like The Simulation's Ending): same triple; random pauses (long gap after "a light is shown", "creature" rushed into "Now"; long pauses after "slowly turn" and "every page at once", sometimes good, feel random).
6. Male voice doesn't fit.
7. Direction: more takes combining 3 and 7 with these fixes.

## v5 (3 + 7 combined) and v6 (3 + fixes only)

Changes, both: triple refrain written into the lyric (all 6); female; "Wooh!" shouts; steady phrasing line. Lyric spellings tested: p5a `tomorrow-oh`, `borrow-oh`, `graph-ics` vs p5b plain `tomorrow`, `borrow`, `graphix`.

| Check | Auditions 3 / 7 | v5 (8 takes) |
|---|---|---|
| "graphics" heard with the s | no / no (matches Idi's ear) | **8 of 8**, both spellings |
| triple refrain, all 6 | 6 / 6 | 6 of 8 takes |
| "tomorrow" held | | `-oh` spelling: 2.8-4.0 s in 3 of 4; plain: 0.3-1.1 s |
| pace (words per minute) | 143 / 172 | 150-182 |
| ear: "almost rap-like" verses | none / | 6 of 8 |

Reading: v5 sped up (7's sparkle + "fast hi-hats" in jep's prompt), and speed brought back the rap feel. v6 = audition 3's prompt nearly verbatim + only Idi's fixes (`D:\work\aimv-lab\kc\caption-minimax-v6.txt`), p5a spellings, 8 seeds.

v5 picks for Idi: `D:\work\AIMVs\ours\v5\` A = 3004 (96.3% words, holds 4.0/2.6 s, drops 17/11 dB), B = 3011 (150 wpm, no rap flag, plain spelling), C = 3002 (holds 4.0/3.7/4.0/3.2 s, "almost rapped" flag).

Meter note: the anchored drop meter scores audition 3 at ~1 dB though Idi hears "sick drops": not used for selection.
