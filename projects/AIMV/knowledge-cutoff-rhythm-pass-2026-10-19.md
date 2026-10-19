---
type: project
created: 2026-10-19
author: jep
status: active
---

# Knowledge Cutoff: the rhythm pass (2026-10-19)

Verdict: **the video now moves with the drums as well as the words, and every measured target is met on one whole render.** Watch: `D:\work\AIMVs\ours\video\full3\kc-full-1080p.mp4` (sheet `full3-sheet.jpg`). Follows [[knowledge-cutoff-notes-pass-2026-10-18]]; rules now in [[knowledge-cutoff-treatment-2026-10-17]] section 14.

## 1. Idi's ask, and what the analysis found

Idi: "the connection between the music/beat/rhythm and what's shown on screen is weak and inconsistent. It feels like we're telling a story more than singing a song." Plus: ALGAE appears seconds before it is sung; DLSS could use an "RTX OFF / RTX ON" gag.

Three analysis agents (kc-engine `reports/rhythm-measure.md`, `rhythm-r123.md`, `rhythm-r45.md`) measured R1-R5 and ours:

| finding | ours | references |
|---|---|---|
| picture motion on a beat vs between beats (1.0 = none) | 1.05 | 1.46-1.54 (R1, R2, R3, R5; R4 none, the narrative one) |
| on a kick | 0.94 (calmer than between kicks) | 1.32-1.51 |
| on a sung word | 1.16 | mostly lower |
| choruses vs verses | choruses locked worse; final chorus calmest | choruses lock hardest, escalate per visit (R5 1.40 / 1.79 / 2.01) |
| song loudness swell into choruses | about 1 dB | 4-5 dB: our picture has to supply the energy |
| engine | no snare/hat onsets; grid 24 ms behind the drums; post zoom/shake/flash unused | R1's code: zoom +1-1.5% and 1.5-5 px shake per beat, even in a drumless verse |

ALGAE: faster-whisper on the vocal stem puts "Algae" at 117.28 s (on a beat); our timing file had 115.01. Idi's ear was right: 115.0-117.28 is instrumental.

## 2. What changed

| layer | change |
|---|---|
| engine (R0) | snare, hat and 18 drum chokes from the stem; grid moved 24 ms onto the drums; a default pulse on every plate scaled by a section energy map (verses light, pre-choruses build, choruses escalate per visit, silences and chokes still); cuts and set-ups snapped onto the grid about 2 frames early; the caret breathes on the beat; "Algae" at 117.284 |
| choruses (hook) | KNOWLEDGE / CUT-OFF! at about 88% of the width, slammed per word; the blade on the drum when within 90 ms; june whips onto each sung word, flap letters 27-30% of frame height; the globe turns in beat steps with the ticker landing on beats; KEPT / KEEPS / WILL KEEP at 25%+ |
| tune and card | chorus lines sung one phrase at a time at 15% of frame height with slams; the roll, claims table and toggle land on the beat; downbeat reframes; chorus 2 swaps ink / graphite / panel on downbeats; the card's lines sung at the same scale; claims columns now `CLAIM` / `SAYS YOU` (the old heads repeated the sung words) |
| verses | objects count the beat everywhere (spells, counters, slip items, feed posts, page turns landing flat on the beat); borrow 1-2 build bar over bar into each chorus; the outro pulls back one framing per beat; ALGAE slams on 117.28 after a blue build on the beat; dlss: `RTX OFF` over the honest grid, `RTX ON` on the downbeat of "Now" with light from no source |
| fix found on the way | `scripts/server.ts` left a web server running after every script (543 orphans, about 100 GB of memory) until renders failed; it now ends the whole process tree |

## 3. Verified, and how

| check | before | after | target |
|---|---|---|---|
| beat pulse gain, whole video | 1.00 | 2.07 | 1.40+ |
| choruses 1 / 2 / final | 1.09 / 0.95 / 1.02 | 2.32 / 2.45 / 2.53 | 1.45+, rising |
| kick / snare gain | 0.94 / 1.02 | 1.74 / 2.19 | 1.30+ / 1.40+ |
| vocal gain (guard) | 1.16 | 1.38 | 1.10+ |
| graphic hits on the beat | 29% | 55% | 45%+ |
| visual spikes on a drum hit | 12% | 25% | 25%+ |
| hit timing vs the drum | late | 16 ms early | 5-40 ms early |
| bar-period autocorrelation | 0.00 | 0.10 | 0.08+ |
| stillness | 8% | 2% | 10% or less |
| null control (events shifted half a beat) | 0.93 | 0.84 | under 1.0 |
| whole-song 4K check | | 483 / 483 words on time, 0 issues, type scale 10x+ in 70 set-ups | green |
| light/dark jumps | 3 (allowed) | 2 (allowed) | 0 open |
| text inventory | | meta 0; repetition only named exemptions | |
| render | | one detached run, exit 0, 194.10 s, bt709, tail -91 dB, md5 `ea9017d0` | |
| critics | | 4 fresh critics, every FIX fixed; jep viewed frames of the render | |

Measure: `tools/avsync.py accept` (kc-engine). Verse 1 / verse 2 / verse 3 / bridge: 1.92 / 1.67 / 1.37 / 1.81, all below their choruses.

## 4. For Idi's eye

1. Strength: ours now measures above the references (2.07 against 1.46-1.54), partly because the ratio flatters a picture that used to be still between beats. Judge whether any section feels like too much; each section's amount is one number in the energy map.
2. At 170.5 s WILL shows grey, not held in yellow (visit 3's changed word): check by eye.
3. The loop: first and last frame were pixel-identical in the engine (critic, after the last outro edit); after encoding they compare at 39.4 dB (43.2 before; the bitrate rose with the motion).
4. Six short reading times from the notes pass remain, plus the chat greeting at 2.2 of 2.5 s.
