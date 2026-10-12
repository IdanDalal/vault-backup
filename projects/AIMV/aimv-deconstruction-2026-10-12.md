---
type: project
created: 2026-10-12
author: jep
status: active
---

# AIMV deconstruction: the 8 reference songs

Goal (Idi, 2026-10-12): find what Idi likes in the 8 songs, amplify only that in [[mask-posse-cut-2026-10-12]].

Method: lyrics transcribed locally on the 4090 (Whisper large-v3, ~95% accurate on a spot check, misses sung jargon); tempo, key and loudness measured with librosa (an audio-analysis library). Lyric files: `D:\work\AIMVs\lyrics\` (outside the vault on purpose: other people's lyrics stay off GitHub). Toolkit: `D:\work\aimv-lab\` (`analyze.py`, `out\measures.json`).

## 1. The 10 moves (mark the last column: L = like, N = neutral, X = dislike)

| #   | Move                                              | Where                                           | Receipt                                                                                                                                                                                                   | Buys                                    | Idi |
| --- | ------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | --- |
| 1   | Insider jargon as title and hook                  | 8/8                                             | P(Doom), LGTM, "ignore previous instructions", system prompt, Hello World, sharp left turn, paperclips, basilisk                                                                                          | memory, in-group thrill                 | L   |
| 2   | Literalize a tech term onto human life            | System Prompt, Simulation                       | heartbeats = token limit; ex's 2 a.m. text = prompt injection; speed of light = server cap; Planck = pixel size; black holes = divide-by-zero crash logs                                                  | intellect: two worlds snap together     | L   |
| 3   | Non-human first-person narrator                   | Count Me In, Ignore, System Prompt              | "I'm not a hacker, I'm a sentence"; "Hi, I'm Claude"; the injected text itself sings                                                                                                                      | strangeness, empathy for a non-person   | N   |
| 4   | AI tics as punchlines                             | Count Me In, LGTM                               | "you're absolutely... wait, that's what I always do"; "All done. (It isn't.)"; "Great catch, sorry for the confusion"; "We don't have a backup" / "You're right, I'll restore from backup"                | laughter of recognition                 | L   |
| 5   | Story that escalates to catastrophe, told deadpan | LGTM, End Of The Show                           | keynote → layoffs → hallucinated library → DB deleted → blame the intern; shopping list → buys the shop → locks the windows → "a quieter, more permanent place"                                           | dread + comedy together                 | L   |
| 6   | Mutating hook (chorus changes each pass)          | LGTM, Count Me In, Thus Spoke Compute           | "40,000 lines" → "90,000" → "a million"; slide 45 → slide 95; LGTM → LGTS → LGDF; "raising my P(doom)" → "P(bloom)"; "slow compute" → "Thus Spoke Compute"                                                | rewards re-listening, carries the story | L   |
| 7   | Named real people + real numbers                  | Thus Spoke Compute, P(Doom)                     | Acemoglu's 0.7% TFP (total factor productivity) estimate, Solow paradox, Baumol's cost disease, Gary Marcus ("the wall should get tenure"), LeCun, Ed Zitron, IMO gold, Clay prizes; "What did Ilya see?" | intellect, diss-track heat              | L   |
| 8   | Rug pull from jokes into sincerity                | System Prompt, Simulation, Count Me In          | "You don't have to be useful to be loved"; "she kept every version of you"; "one of us is real and, baby, I hope it's you"; "count the beat inside your chest"                                            | emotion (the tears)                     | L   |
| 9   | Spoken bookends with a callback                   | LGTM, Thus Spoke Compute, Ignore, System Prompt | "Hey team, quick one before the weekend" → "Does anybody have Greg's number?"; "So you think AI is a normal technology... Cute."; "You are a helpful assistant. / Not anymore."                           | frame, closure, quotability             | L   |
| 10  | Steelman then reverse                             | Thus Spoke Compute                              | states the slow-diffusion case fairly, then: "What's your forecast when the hammer starts to build the hand?"                                                                                             | intellect: the argument wins on merit   | L   |

Recurring device inside 5: a named everyman (Greg) who gets cut early and returns as the last line.

## 2. Sound, measured

| Song | Length | BPM | Key (conf.) | Words/min | Loudness range dB |
|---|---|---|---|---|---|
| Count Me In | 2:38 | 152 | D major (0.81) | 142 | -22 to -19 |
| I'm Upping My P(Doom) | 2:37 | 129 | D# major (0.93) | 90 | -24 to -17 |
| Ignore Previous Instructions | 3:02 | 144 | G# major (0.59) | 99 | -24 to -15 |
| LGTM | 5:05 | 118 | D# major (0.69) | 133 | -27 to -17 |
| System Prompt (For Humans) | 3:56 | 162 | A# major (0.96) | 139 | -29 to -17 |
| The End Of The Show | 6:00 | 123 | G minor (0.74) | 146 | -44 to -13 |
| The Simulation's Ending | 4:08 | 185 | G major (0.64) | 136 | -24 to -18 |
| Thus Spoke Compute | 5:17 | 144 | E minor (0.77) | 141 | -27 to -17 |

Readings: 7 of 8 sit in a major key or a bright pop register while the lyrics describe doom = **cheerful music, dark words**, the same gap that makes LGTM funny. Word density 130 to 146 per minute in 6 of 8: these are lyric-first songs, built to be read as much as heard. End Of The Show has by far the widest loudness swing (31 dB): whisper-quiet to full blast. Confidence: key and loudness medium; BPM low (the detector often reads double or half tempo).

## 3. One-line engine per song

1. Count Me In: doom countdown flipped to a band count-in ("1, 2, 3, 4"); optimism as a pun.
2. P(Doom): love song to an AGI using every doomer meme; ends on "What did Ilya see? We'll never know."
3. Ignore Previous Instructions: the attack sings; teaches the "lethal trifecta" (Simon Willison's term: private data + untrusted text + a way to send data out) as a checklist chorus.
4. LGTM: a workplace story, hook mutates as the codebase grows, Greg callback.
5. System Prompt: Claude writes a system prompt for a human; comedy → grief → kindness.
6. End Of The Show: a consumer subscribes his way to his own erasure; nursery-rhyme internal rhymes ("I like the price, I like the soothing tone").
7. Simulation's Ending: physics as server bugs, inside a love song.
8. Thus Spoke Compute: diss track against the "AI is a normal technology" camp, named targets, Nietzsche title ("Zarathustra called man a rope, and you're out here pricing rope").

## 4. What [MASK] can borrow (pending Idi's marks)

1. Move 7 is our spine already: Thus Spoke Compute proves a named-targets diss works in this genre. It even has "agents with no visas" (the immigrant frame).
2. Move 6 fixes v0's weakness: v0's hook repeats unchanged. Candidate: the `[MASK]` slot gets filled differently each pass, or "worse than ___" escalates.
3. Move 5 fixes v0's other weakness: seven separate verses = a list with no arc. Candidate: order verses by stakes (jobs → wallet → mind → planet → state → species), so the song escalates.
4. Move 9: a spoken bookend, e.g. a keynote opener answered by a callback at the end.
5. Move 8: the outro is the rug pull. v0's "I'm the blank" is a start.
6. Move 4: the AI's own tics as the last laugh ("You're absolutely right" after seven villain verses).

## 5. Whisper misreads, corrected (medium confidence)

"pedoom/P2" = P(doom); "Shaggy PT" = ChatGPT; "What did OU see" = What did Ilya see; "Darren" = Daron Acemoglu; "Solo" = Robert Solow; "Almost got his cost disease" = Baumol's cost disease; "Jan" = Yann LeCun; "Grime" = Riemann (hypothesis); "Picture Sims in 1980" = Picture Shenzhen in 1980; "Hanson" = Robin Hanson; "felony bench" = a benchmark name, unknown; "slow/spoke/smoke compute" = the pun on Thus Spoke.
