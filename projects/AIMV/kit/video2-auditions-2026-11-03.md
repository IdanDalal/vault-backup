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

## Results

Pending (batch running 2026-11-03).
