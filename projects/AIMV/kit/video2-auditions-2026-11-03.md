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
