---
type: project
created: 2026-11-03
author: jep
status: active
---

# "Pay Attention": MiniMax style auditions

Idi, 2026-11-03 (R18): "Lock v4 and start the MiniMax auditions." Lyric locked: [[video2-lyrics-v4]]. Method from KC ([[kit-audio-pipeline]] section 4): style auditions, 2 seeds each, previews for Idi's ear, Idi picks; then a seed batch on the picked style.

## Setup

| item | value |
|---|---|
| engine | MiniMax Music 3 (local), jep's ComfyUI on :8189, `wf_minimax_tiled.json` |
| length | 360 s per take: the node's maximum (`MAX_AUDIO_FRAMES` 9,000 / 25 per s, `comfy/ldm/minimax_music/ar.py:21-22`); the song needs ~330-345 s, so a take that runs slow loses the closing receipt (the screen flags it) |
| lyric sheet | `D:\work\aimv-lab\pa\lyrics-mm-v4.txt`: KC conventions (no line-end punctuation in sung lines; `[Spoken]` parts fenced by `[Instrumental]`; the drill call written "Atten... tion!") |
| captions | `D:\work\aimv-lab\pa\captions\` from `make_captions.py`: one shared structural timeline (the song's shape) + the sound-bar levers ([[research-sound-craft-2026-11-02]]: valleys, escalation, stop-and-slam, pumping sub; KC v8's "relentless" and "all instruments audible at all times" dropped); per style: genre, tempo, key, timbre, instruments, groove; 635-702 words each |
| batch | `pa\aud-batch.sh`: 6 styles x 2 seeds = 12 takes; Idi's status board `D:\work\AIMVs\ours\_STATUS.txt` |
| screen | `pa\pa_screen.py`: complete (reaches "Ask it." inside 360 s), words heard %, wpm, integrated LUFS, LRA, full stops, previews P1 (pre-chorus 1 into chorus 1), P2 (games into chorus 2), P3 ("Pencils down", the drill slam, the payoff), one reel per style. Tested on KC: LRA 4.3 LU, the sound report's figure |

## The six styles

| id | style | from Idi's bar |
|---|---|---|
| s1 | Trip-hop / bedroom pop growing into cinematic rock (the premise's planned sound) | Tell Me No → It Crossed The Line |
| s2 | Electro-funk / synth-punk with chiptune, pumping overdriven bass | Not My Fault |
| s3 | Cinematic indie rock / shoegaze with industrial walls | It Crossed The Line |
| s4 | Hyperpop / synth-pop with chiptune and video-game rock | Final Boss, Hope This Helps! |
| s5 | KC's electropop / synth-punk with the new dynamics levers | Knowledge Cutoff |
| s6 | Lullaby pop growing into stadium electro-rock | Off Switch (lullaby) + the outro |

All six: one female lead (the AI; KC's male voice was rejected), the same lyric, the same structural timeline.

## Targets the screen checks (measured on the bar, [[research-sound-craft-2026-11-02]])

| measure | KC | the bar |
|---|---|---|
| loudness range (LRA) | 4.3 LU | 6.4-11.8 LU |
| full stops | 1 | Tell Me No 6; It Crossed The Line 1; Final Boss 1+ |
| pace | 157 wpm | 79-175 wpm (song-bar six 102-175) |

## Results (2026-11-03; batch 15:05-16:12, about 6 min per take)

Files for Idi: `D:\work\AIMVs\ours\pa-auditions\` (`00-SAMPLER-the-slam-1-to-6.mp3`, 2:39: the "Pencils down" → drill call → payoff moment from the best-measured seed of each style, in order 1-6; `reels\<style>.mp3`, about 3.5 min each: both seeds, 3 moments each; `takes\` the full trimmed songs; `screen.md`).

| style | seed | song length | words heard % | wpm | LRA (LU) | full stops | in the sampler |
|---|---|---|---|---|---|---|---|
| s1 trip-hop → cinematic | 5011 | 5:00 | 96.4 | 141 | 5.2 | 6 | |
| s1 | 5012 | 4:39 | 96.7 | 132 | 7.0 | 2 | 1 |
| s2 electro-funk | 5021 | 4:49 | 93.7 | 135 | 6.6 | 5 | 2 |
| s2 | 5022 | 4:26 (ends at "one question") | 93.7 | 127 | 7.7 | 2 | |
| s3 cinematic rock | 5031 | 4:50 | 96.1 | 140 | 9.2 | 5 | 3 |
| s3 | 5032 | 4:31 | 94.7 | 133 | 5.1 | 4 | |
| s4 hyperpop | 5041 | 4:34 | 83.4 | 128 | 4.3 | 1 | 4 |
| s4 | 5042 | 4:30 | 95.5 | 135 | 5.9 | 1 | |
| s5 KC evolved | 5051 | 4:04 | 94.2 | 135 | 3.3 | 2 | |
| s5 | 5052 | 4:26 (improvised ending cut) | 93.6 | 166 | 7.5 | 3 | 5 |
| s6 lullaby → anthem | 5061 | 5:02 | 95.9 | 139 | 10.8 | 1 | 6 |
| s6 | 5062 | 4:31 | 93.7 | 135 | 6.6 | 0 | |

Readings (measured unless marked):
1. The dynamics levers worked: 9 of 12 takes reach 5.1-10.8 LU against KC's 4.3; 7 sit inside the bar's 6.4-11.8. s5 seed 5051 (3.3) shows KC's own style can still flatten.
2. Every take sings the whole lyric in 4:04-5:02; the 360 s cap leaves room. MiniMax still invents filler after the last line (KC lesson holds); two takes dropped or improvised the receipt's last words.
3. The slam shape ("Pencils down", about 1 s at -53 dB, a short burst, the band back at -16 dB) shows in s3 5031 and s1 5012; s6 5061 never drops to true silence. The burst inside the silence is probably the drill call; Whisper cannot confirm a single shouted word (inferred; Idi's ear decides).
4. Words heard 93-97 % except s4 seed 5041 (83 %); KC's final take scored 98.6 %.

Screen fix 2026-11-03: the first pass flagged 7 takes "TRUNCATED" because Whisper hears "Ask it" as "Ask a teen" / "Ask a ton"; the trim now anchors on "receipt" → "go on" → the next word. Checked by transcribing the tails of 4 takes.

## Round 2: v5rec on Idi's three keepers (2026-11-03)

Lyric `pa\lyrics-mm-v5rec.txt` (v5 with jep's recommended options), captions `pa\captions-v5\` (drill call removed; slam = silence → "Pencils down" → band; four held notes; the deliberate "twenty" stutter), each kept seed + 1 new seed. Files: `D:\work\AIMVs\ours\pa-v5\` (`moments\M1-M7`: the same moment cut from all 6 takes in order; `moments\ORDER.md`; `takes\`; `screen.md`).

| style | seed | words heard % | wpm | LRA (LU) | full stops |
|---|---|---|---|---|---|
| s4 hyperpop | 5042 | 96.1 | 139 | 7.1 | 3 |
| s4 | 5143 | 93.4 | 166 | 7.3 | 2 |
| s5 KC evolved | 5052 | 94.7 | 144 | 6.0 | 0 |
| s5 | 5153 | 96.5 | 145 | 4.4 | 1 |
| s6 lullaby → anthem | 5061 | 96.0 | 133 | 8.8 | 1 |
| s6 | 5163 | 96.8 | 137 | 9.2 | 3 |

All 6 complete (the whole lyric, receipt included). Translation checks (Whisper on the moment clips; Idi's ear rules):
- "twenty-twenty-twenty-two": heard as "In 2020, 22" (s6 5061): the stutter is sung.
- "is it?": heard cleanly in 6 of 6.
- "da-a-a-ark": heard "dark" in 2 of 6; split into "day ... arc" in 4 of 6. "gui-i-i-ide": heard "goo, I, I, I'd" (s6 5061). The hyphenated hold may be breaking words; alternative: plain spelling + "held note" in the caption.

Moment clips: M1 cold-open pauses, M2 twenty stutter + guide hold, M3 tutor 2023, M4 ranked stats + game hold + stop, M5 "is it" + dark hold, M6 silence → "Pencils down" → slam, M7 missed hold. In each clip the takes play in order: 1 s4 5042, 2 s4 5143, 3 s5 5052, 4 s5 5153, 5 s6 5061, 6 s6 5163.

## Round 3: the final batch (2026-11-03/04)

Winning style s5 KC evolved (R21), Idi's final lyric (`pa\lyrics-mm-final.txt`, holds in plain spelling, two `[Instrumental]` pads), caption `pa\caption-final-s5.txt` (pads described as about 15 s; holds as "one smooth sustained vowel, never broken into separate syllables"), seeds 5153 + 6001-6011. Files: `D:\work\AIMVs\ours\pa-final\` (`00-SHORTLIST\` 4 full takes; `moments\M1-M7` with all 12 takes in seed order; `takes\`; `screen.md`).

| seed | length | words heard % | wpm | LRA (LU) | full stops | shortlist |
|---|---|---|---|---|---|---|
| 5153 | 4:41 | 96.1 | 137 | 4.9 | 4 | 1 (Idi's seed) |
| 6001 | 4:39 (skips "Go on.", trimmed by hand) | 94.6 | 134 | 7.5 | 2 | |
| 6002 | 4:36 | 97.2 | 137 | 8.6 | 9 | 2 (most dynamic) |
| 6003 | 5:03 | 95.9 | 137 | 4.3 | 2 | |
| 6004 | 4:14 | 97.2 | 142 | 5.2 | 3 | |
| 6005 | 5:06 | 96.8 | 134 | 4.7 | 0 | |
| 6006 | 4:07 | 96.5 | 149 | 3.1 | 1 | |
| 6007 | 4:10 | 96.3 | 134 | 5.5 | 2 | |
| 6008 | 5:01 | 96.6 | 152 | 5.0 | 4 | |
| 6009 | 5:11 | 97.0 | 132 | 4.1 | 1 | 3 |
| 6010 | 4:27 | 96.4 | 134 | 5.4 | 2 | |
| 6011 | 5:21 | 94.4 | 128 | 5.4 | 1 | 4 (longest) |

Readings (measured; Idi's ear rules):
1. Plain-spelled holds no longer split words: "guide" and "dark" heard whole in every take (round 2: "goo, I, I, I'd", "day ... arc"). Whether each is held smoothly is for the ear.
2. 5 of 12 reach Idi's 5:00 (6003, 6005, 6008, 6009, 6011); the pads did not always run long.
3. Dynamics flatter than round 2's s6 (LRA 3.1-8.6 here vs 8.8-9.2); seed 6002 is the outlier at 8.6.
4. New flag: "without one" (the question mark gone) is heard as "with that one" in 10 of 12 takes: the line's point may be lost.
