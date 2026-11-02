---
type: research
created: 2026-11-02
author: Agent lyrics-screen-test
---

# Lyrics screen-read test (2 songs)

## Verdict

- Run it on the other songs: **yes, on the 7 that have a video**, after one change: add a per-line frame sweep on top of the flagged-word frames.
- Recall on Idi's corrections: **19 of 26 fixed (73 %)**, 1 partial, 6 missed. LGTM 12/17, The Simulation's Ending 7/9.
- Screen reads held up: 25 proposals, 19 match Idi, 6 disagree with Idi and each one shows the lyric on screen (table below). No proposal was a misread of the screen.
- Losses come from flagging. All 5 LGTM misses sat above the p threshold (p 0.59 to 0.99) and all 5 are readable on screen at the word's own timestamp (diagnostic frames, outside the pipeline).
- 8 possible misses for Idi to judge (6 from the pipeline, 2 from diagnostic frames). Strongest: LGTM 2:57 and 4:27 "prod", LGTM 3:49 "Root cause", Sim 3:25 "bargain", Sim 1:33 "Time runs slow round".

## Method

- Whisper: faster-whisper large-v3, CUDA float16, same settings as `D:\work\aimv-lab\analyze.py` (beam 5, no VAD, `condition_on_previous_text=False`, librosa 16 kHz load) plus `word_timestamps=True`. Output segments match the old `.lyrics.txt` line for line (95 and 73 lines). Ran in the foreground on the RTX 4090.
- mp3 vs mp4 sync: onset cross-correlation, offset -0.046 s on all 9 songs checked (2 test + 7 survey). Timestamps transfer directly.
- Tokens: Whisper word pieces merged into whitespace tokens (`-L` pieces join, so `F-L-L-L-G-T-L` is one token). LGTM 637 tokens, Sim 562.
- Flag rules: R1 word probability below **0.5** (picked as a budget, about the lowest 5 % of tokens; sensitivity table below); R2 out-of-vocabulary (stem missing from the Whisper BPE single-token word list, missing from the AIMV lexicon terms and a small tech list); R3 letter strings and caps acronyms outside the tech list (`LGDF`, `L-L-L-G-T-S`); R4 same word 5+ times in a row.
- Flags: LGTM 40 (31 p, 10 letter-string, 1 OOV) merged into 33 events; Sim 39 (20 p, 20 OOV, 1 repeat; 15 of them are the Brin run) merged into 22 events. Flags within 1.2 s share one event.
- Frames: ffmpeg, 960 px JPEG, t-0.3 / t / t+0.3 for short events; events longer than 0.6 s get one frame every 0.4 s (cap 12). Three frames stacked per sheet for reading. Text tracks the vocal in both videos, no lag adjustment needed.
- Reading: line-level. A proposal may fix any word of the line visible in the event's frames (this fixed 4 unflagged Sim words: "in", "test", "they're", "say").
- Not applied, by rule: number and format variants (09 shown as "oh-nine", 40,000 as "forty thousand", 3 a.m. as "Three a.m.", `L-G-T-M` vs `LGTM`), apostrophe-only and spacing-only differences ('round vs round, plotline vs plot line). Letter strings keep Whisper's audible `L-L-` stutter and take the acronym from the screen.
- Scoring: word-level diff of normalized tokens (lowercase, alphanumerics only), regenerated Whisper vs Idi's file. One correction unit = one diff opcode. Brin line excluded. Punctuation-only edits ignored (LGTM 3, Sim 9).

## Scores per song

| | LGTM (Looks Good To Me) | The Simulation's Ending | Both |
|---|---|---|---|
| Idi correction units scored | 17 | 9 | 26 |
| Flagged by the rules | 12 | 4 | 16 |
| Fixed from screen | 12 | 7 | **19 (73 %)** |
| Partial | 0 | 1 | 1 |
| Missed: not flagged | 5 | 1 | 6 |
| Missed: no on-screen text | 0 | 0 | 0 |
| Missed: misread | 0 | 0 | 0 |
| Proposals applied | 16 | 9 | 25 |
| Proposals outside Idi's corrections | 3 | 3 | 6 |
| Frames extracted / read | 129 / 114 | 81 / 78 | 210 / 192 |
| Sheets read (3 frames each) | 38 | 26 | 64 |

- LGTM fixed: `F-L-L-L-G-T-L` x2, `L-L-L-G-T-S` x2, `L-L-L-GDF`, `LGTL`, `LGTS`, `LGDF` x3 (all to LGTM), pride to prod, that to their, Green cash to Great catch.
- LGTM missed, all "not flagged", all readable on screen per diagnostic frames: 1:09 marked to mocked (screen "mocked)"), 3:03 stack's to stock's ("The stock's g..."), 3:36 cash to catch ("Great catch!"), 4:01 won't you to won't do ("You marked it 'won't do'."), 4:41 ball to bot ("and the bot ge...").
- Sim fixed: fuck-a-fuck to f-f-fine; That matters, justice, ... they're to Dark matter's just ... that; Hot base to Base; Heat test to Heat death's; plotline in to plotline (spacing aside); say to save?
- Sim partial: 2:55 Like. Screen shows "Lag so bad"; Idi wrote "Lag's so bad".
- Sim missed: 3:53 duplicate "The simulation's end" (Whisper repeated the last line; a screen frame cannot show a duplicate).
- Corrected transcripts: `C:\Users\jep\.claude\jobs\99182c36\tmp\ocr\LGTM (Looks Good To Me).corrected.txt`, `...\The Simulation's Ending.corrected.txt`. The 5 LGTM misses are still Whisper's words there.

Threshold sensitivity (p rule alone; tokens flagged / Idi units containing a token below T):

| T | LGTM tokens | LGTM units (of 17) | Sim tokens | Sim units (of 9) |
|---|---|---|---|---|
| 0.3 | 13 | 3 | 6 | 3 |
| 0.5 | 31 | 5 | 20 | 4 |
| 0.6 | 46 | 8 | 30 | 4 |
| 0.7 | 62 | 10 | 39 | 5 |
| 0.9 | 109 | 15 | 77 | 5 |

The letter-string rule did most of LGTM's work (7 of 12 flagged units). Raising T past 0.7 doubles frames for 1 to 2 more units, which is why the recommendation below adds a line sweep instead.

## Possible misses for Idi to judge

Frame paths are under `C:\Users\jep\.claude\jobs\99182c36\tmp\ocr\`.

| Song | Time | Whisper | Idi | Screen says | Frame |
|---|---|---|---|---|---|
| LGTM | 1:13 | The velocity is vertical | The velocity is vertical | "The velocity's vert..." (contraction only) | `LGTM (Looks Good To Me)\e07_0075.27.jpg` |
| LGTM | 2:57 | Let's ship it to God | Let's ship it to God | "let's ship it to PROD" (diagnostic, unflagged, p 0.59) | `LGTM (Looks Good To Me)\diag\god_0179.26.jpg` |
| LGTM | 3:45, 3:47 | It's a bucket, it's a blameless review / It's a bucket, so we blame the intern | same as Whisper | "It's a BLAMELESS review, so we blame the intern." No "bucket" on screen; ear check, not applied | `LGTM (Looks Good To Me)\diag\bucket2_0228.30.jpg` |
| LGTM | 3:49 | It's a pocket phone, unclear action item, more AI | same as Whisper | "Root cause: unclear." / "Action item: more AI." ("It's a" absent from screen, kept) | `LGTM (Looks Good To Me)\e24_0230.54.jpg`, `e25_0233.23.jpg` |
| LGTM | 4:27 | Let's, let's ship it to pod | Let's, let's ship it to pod | "let's ship it to PROD" | `LGTM (Looks Good To Me)\e28_0269.22.jpg` |
| Sim | 1:33 | The time runs slower on heavy stuff | same as Whisper | "Time runs slow round heavy stuff, that's ju..." | `The Simulation's Ending\e08_0094.41.jpg` |
| Sim | 2:55 | Like so bad, we're rubber bending | Lag's so bad, we're rubber bending | "Lag so bad we're rubber-banding" | `The Simulation's Ending\e15_0177.65.jpg` |
| Sim | 3:25 | Ancestor sim on a parking GPU | same as Whisper | "Ancestor sim on a bargain G-P-U" | `The Simulation's Ending\e20_0206.83.jpg` |

Minor screen variants, not counted: LGTM 1:02 "oh-nine" for 09; LGTM 2:35 "The chart's up" for "The charts up"; Sim 0:34 and 0:40 "round" without apostrophe.

## The Brin line (Sim 1:18, excluded from scoring)

- Frames: `The Simulation's Ending\e06_0078.10.jpg` to `e06_0082.50.jpg` (12 frames, 78.1 to 82.5 s; Whisper's 15 "brin" span 78.6 to 83.4 s).
- 78.1 to 78.5: "Loading, loading, stuck at ninety-nine", 99 % then 100 %.
- 78.9: the screen shatters into tiles reading "REN".
- 79.3 to 80.1: a wall fills with rows of "REN REN REN ..." (3 rows, about 13 to 15 tiles visible), then one row "DER DER DER DER", then from 80.5 one row "ING ING ING ...".
- 81.3 to 82.5: one large "RENDERING" assembles over the wall ("REN ... RING" readable at 82.5).
- Reading: Whisper's "brin" is the syllable "ren". The screen supports a stuttered "ren, ren, ren ... der ... ing ... rendering". Tile counts are layout, so the sung count of each piece needs the ear. The pipeline proposed nothing here.

## Other 9 songs: lyrics on screen

6 frames each, 1.5 s into 6 evenly spread Whisper lines. Grids: `C:\Users\jep\.claude\jobs\99182c36\tmp\ocr\survey\<song>_grid.jpg`.

| Song | Lyric text on screen | Call | Notes |
|---|---|---|---|
| Thus Spoke Compute | 5/6 | yes | subtitle bar in caps on every sung line, word highlight; best case |
| Count Me In | 6/6 | yes | kinetic 3D words, neon signs |
| Ignore Previous Instructions | 6/6 | yes | typed prompt boxes and big kinetic words |
| Compacting Conversation | 5/6 | yes | kinetic words plus handwritten letter and code lines; one tile disagrees with Whisper ("User prefers dark mode") |
| Off Switch | 4/6 | yes | big caps words; 2 tiles are image-only scenes |
| Run It Again | 4/6 | yes | italic serif lines; one blurred transition, one outro card |
| The End Of The Show | 3/6 | partial | text sparse and partly diegetic (posters, UI); motion blur |
| It Crossed The Line | n/a | no video | only the mp3 is in `D:\work\AIMVs` |
| Tell Me No | n/a | no video | only the mp3 is in `D:\work\AIMVs` |

## Recommendation for the other songs

1. Run the 6 "yes" songs first, then The End Of The Show. It Crossed The Line and Tell Me No need their videos fetched before anything can run.
2. Add a per-line sweep: one frame near the end of every Whisper line (the full line is on screen at that point in both test videos), on top of the flagged-word triples. Untested as a sweep; the evidence is that 5 of 5 unflagged LGTM errors read correctly from frames at their own timestamps.
3. Pack sweep frames 6 per image at 640 px tiles (the survey grids read cleanly at that size). Cost per song: about lines/6 grids plus the flag sheets. Example: Thus Spoke Compute, 90 lines: 15 grids + about 20 sheets.
4. One agent per song. This test read 64 sheets for 2 songs, roughly 1.9k image tokens per sheet (pixel estimate), about 120k tokens of images.
5. Keep the not-applied rules: format variants, apostrophes, spacing. Keep "possible misses" as a separate list for Idi; the screen is often more exact than the ear (prod, bargain, rubber-banding) and still sometimes trims sung words (3:49 "It's a").

## Files

- Scripts: `C:\Users\jep\.claude\jobs\99182c36\tmp\ocr\` `whisper_words.py`, `flag.py`, `frames.py`, `score.py`, `diag.py`, `survey.py`, `offset.py`, `toks.py`.
- Data: `<song>.whisper.json` (word timestamps and p), `<song>.flags.json`, `proposals.json` (every proposal with frame and screen text), `score.json`, `score.log`.
