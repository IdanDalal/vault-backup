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

## Feedback (Idi, plain words)

Pending.
