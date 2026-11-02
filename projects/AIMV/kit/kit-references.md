---
type: project
created: 2026-11-02
author: jep
---

# References registry: what Knowledge Cutoff studied

Scope: every reference video Knowledge Cutoff (KC, live 2026-11-01 at https://youtu.be/-g6hYVec1Uo, channel @chorusofminds) studied, for the next video's description and public repo. Read-only sources, cited per fact. "not in files" = no source on disk states it.

Source keys used below:
- `MK` = `D:\work\aimv-lab\research-makers.md` (2026-10-13; creators, dates, views, tools, URLs)
- `MM` = `D:\work\aimv-lab\research-video-makers-methods.md` (2026-10-15; Run It Again, makers' methods, comment replies)
- `META` = `D:\work\aimv-lab\yt\meta.txt`, `meta2.txt`, `meta3.txt` (raw watch-page fields: title, channel, channel ID, views, length s, upload date, description)
- `T15` / `T610` = `D:\work\aimv-lab\research-video-teardown-1-5.md` / `-6-10.md` (frame teardowns, cut rates, best idea)
- `RM` = `D:\work\aimv-lab\refs-measures.json` (audio on Demucs stems, `refmeasure.py`); `RD` = `D:\work\vault\projects\AIMV\reference-deconstruction-2026-10-14.md`
- `DC` = `D:\work\vault\projects\AIMV\aimv-deconstruction-2026-10-12.md` (key, words/min, the 10 lyric moves)
- `PN` = `knowledge-cutoff-parity-notes-2026-10-25.md`; `PP` = `knowledge-cutoff-parity-pass-2026-10-26.md`; `P0` = `knowledge-cutoff-parity-phase0-2026-10-25.md` (all in `D:\work\vault\projects\AIMV\`)
- `MO` = `D:\work\aimv-lab\kc-engine\reports\p1-moments.md`; `RB` = `D:\work\aimv-lab\kc-video\critique\v6\refs-build.md`; `V6` = `D:\work\vault\projects\AIMV\knowledge-cutoff-v6-2026-10-17.md`
- `AU` = `D:\work\vault\projects\AIMV\knowledge-cutoff-auditions-2026-10-14.md`

## The 5 references (the bar)

- The five, by name: I'm Upping My P(Doom), LGTM, The Simulation's Ending, Run It Again, Ignore Previous Instructions. Idi's list for the v5 dissection, ranked by file size (`handoff-2026-10-16-v5-pass.md` 2a); Idi's 2026-10-17 contract: match and exceed these five (memory `aimv-jep-owns-direction`; `V6`).
- Ids fixed in the v6 briefs (`RB` line 12): R1 P(Doom), R2 LGTM, R3 The Simulation's Ending, R4 Run It Again, R5 Ignore Previous Instructions.
- Parity pass split (`PN` ruling 1): parity targets = R1, R4, R3; learn-from = R5, R2.
- The other five local videos, Idi 2026-10-25 (`PN`): "not relevant. 'Not our engine, not our style, not our standards.'" They still shaped the song (style auditions, `AU`) and the lyric moves (`DC`).
- Engine lineage: Degenerative Pixels (R2, R3) "started from" mexicat's P(Doom) engine (comment under R3, `RB` 2.1.1); "3 of the 5 references share one codebase" (`RB` line 17). KC's own visuals run on a fork of the same engine (credits, `knowledge-cutoff-release-2026-10-31.md` line 97).

## Registry: the 10 local videos plus 1 studied without a local file

Local folder `D:\work\AIMVs\`: each video has `<name>.mp4`, `<name>.mp3`, and (except Run It Again) `lyrics\<name>.lyrics.txt` (Whisper transcripts, kept outside the vault on purpose, `DC`). Upload dates are YouTube `uploadDate` (Pacific time, `META`). Views are dated snapshots.

### R1. I'm Upping My P(Doom) (bar; parity target)

| field | value | source |
|---|---|---|
| YouTube title | i'm upping my p(doom) | `META` meta.txt |
| creator / channel | mexicat (channel ID UCmAL-eYH5cE62nQ-nZ72w4w); repo LICENSE: "Copyright (c) 2026 Giacomo Magnanini" | `META`; `D:\work\aimv-lab\refcode\pdoom-video\LICENSE` |
| URL | https://www.youtube.com/watch?v=5EoO5413dBY | `MK` |
| code | https://github.com/mexicat/pdoom-video (MIT; cloned commit `fa164b74`, 2026-10-05; 2,839 stars on 2026-10-17); making-of thread https://x.com/_mexicat/status/2103904518929055853 (unread: X returns HTTP 402) | `RB`; `META`; `MM` 5 |
| song credits | lyrics by osmarks (https://docs.osmarks.net/hypha/p%28doom%29_song_objectively_correct_interpretation) on a verse + chorus by MusicPerson (https://www.udio.com/creators/MusicPerson); Udio original Nov 2024 (https://www.youtube.com/watch?v=uEB5E67vcPA); video uses the Suno "claude-pop" version by deckard (@slimer48484, https://x.com/slimer48484/status/2097752569212756134) | `META`; `D:\work\aimv-lab\pdoom-docs\README.md` line 95 |
| upload / views / length | 2026-09-27; 130,767 views (2026-10-13); 157 s | `META`; `MK` |
| local files | `I'm Upping My P(Doom).mp4` (411 MB), `.mp3`, `lyrics\I'm Upping My P(Doom).lyrics.txt` | dir listing; `handoff-2026-10-16-v5-pass.md` |
| does well | one orange spark guides the camera and becomes each scene's prop (pen, ball, stock line, paperclip, fuse); 3 fonts with fixed jobs (Archivo lyric, Plex Mono machine, Cormorant prophetic); sung part of a word orange, never ahead of the voice; 6 strong cuts/min (lowest of 1-5); quiet 1:28-1:50 then slam into "JUST" and the SUPER-DENSE text wall; P(doom) counter runs away to NaN, "Regenerate" rewinds to frame 1 (loop) | `T15` V2 |
| build method | TypeScript + three.js, deterministic `render(t)`, headless Chrome -> ffmpeg; Demucs stems + CTC forced alignment (MMS_FA + wav2vec2, Whisper cross-check) + hand anchors; beat grid from drum onsets; `TREATMENT.md` bible, 17 plates with owner tags; 4K render about 57 min on an M5 Pro | `MM` 2.1 |
| measured (audio) | 156.8 s; drum tempo 129.2; 2.79 drum hits/s; brightness 2,426 Hz; dynamic range 9.4 dB; voice E4, C4-C5; sung 74 %; deepest drop 18.4 dB at 2:19; D# major (0.93); 90 words/min | `RM`; `DC` |
| measured (picture) | frame travels 55 %; holds 2 s+ 0.76/min; burst share 44 %; dark saturation 0.18; accent area 1.6 %; edges 5.9 %; frames 60 %+ empty 28.7 %; 149 lines of code per second of video (23,286 lines) | `PP` table; `V6` section 2 |
| KC borrowed, where | (1) the whole render engine: KC is a fork, credited "fork of the P(Doom) video engine by Giacomo Magnanini (MIT licence)" (release credits); (2) sync method: forced alignment on the Demucs vocal stem with Whisper as cross-check (`fa_align.py`); kick/snare/hat onsets via R1's `analysis/analyze.py` step (`kc-engine\tools\build_data.py` header); (3) parity moments, one KC line each (`PP`): "drop" -> "Then Spain scored" falls vertical into the net; atoms -> "magic," dots re-form as "name"; Gato past-drift -> "type it all again"; "in your training loss" -> "Everyone I meet is coming from tomorrow" on a road in perspective; GPU grid -> CREATURE in lit cells; fuse -> spike runs the axon to each word; SERVANT/BOSS -> frame rolls on "turned"; FOOM -> BEATS steps widths on 16ths; blues -> "You're humming something new" on the pitch string; wave -> Messi's line rides a wave that flattens; (4) song audition 2 (`AU`) | as cited |

### R2. LGTM (Looks Good To Me) (bar; learn-from)

| field | value | source |
|---|---|---|
| YouTube title | LGTM (Looks Good to Me) - Claude Opus 5.5 music video | `META` |
| creator / channel | Degenerative Pixels (UCUtOwdq47Km76XXIwNK7CWQ); description: "Direction: Degenerative Pixels" | `META` |
| URL | https://www.youtube.com/watch?v=3TNpOD6bov8 | `MK` |
| upload / views / length | 2026-10-05; 835,050 (2026-10-13), 1,017,363 (2026-10-15), 1,146,645 (2026-10-17); Idi 10-25: ">1.5M views in under 3 weeks"; 305 s | `META`; `MM` 2.5; `RB` 2.1; `PN` |
| tools (stated) | "Song: made with Suno v6"; "Animation: Claude Opus 5.5, in TypeScript and three.js"; maker: "I had Claude build a video editor that I then used to mark specific segments or frames with requested fixes" | `META`; `MM` 2.5 |
| local files | `LGTM (Looks Good To Me).mp4` (168 MB), `.mp3`, lyrics txt | dir listing |
| does well | one continuous shot for 5 min (0 strong cuts; scenes join by camera moves, paper tears, shatter); chorus = the same objects each pass, only the numbers grow (lines 40,000 -> 90,000 -> 1,048,576); karaoke by syllable, sung word turns terminal green; type voices (grotesk singer, mono code, serif italic captions, red marker sarcasm, stamps); credits staged as a PR being merged; bookend: opening chat retyped with a new last line | `T15` V4 |
| measured (audio) | 305.2 s; tempo 117.5; 3.23 hits/s; 2,765 Hz; range 9.4 dB; voice D#4, F2-G#5 (two voices); sung 45 %; deepest drop 7.4 dB (steady energy); D# major (0.69); 133 words/min | `RM`; `RD` B6; `DC` |
| KC borrowed, where | "the checks are all green" -> TRUE built from the receipt's checkmarks; "mocked" dashed lines -> CHECK as a dashed outline in the switch; "nobody knows what any of it means" -> "I can't check a" decays into code (`PP`); "vertical" -> KC line 23 (`MO` line 281); `born` plate shows "LGTM 1,026,487 views" (treatment section 9); song audition 4 (`AU`) | as cited |

### R3. The Simulation's Ending (bar; parity target)

| field | value | source |
|---|---|---|
| YouTube title | The Simulation's Ending - Claude Opus 5.5 music video | `META` |
| creator / channel | Degenerative Pixels (UCUtOwdq47Km76XXIwNK7CWQ) | `META` |
| URL | https://www.youtube.com/watch?v=R_ErmTs7g9I | `MK` |
| upload / views / length | 2026-10-04; 97,253 (2026-10-13), 125,262 (2026-10-17); 248 s | `META`; `RB` |
| tools (stated) | "a music video animated by Claude Opus 5.5 with a song produced by Suno v6"; engine "started from" mexicat's repo (maker comment) | `META`; `RB` 2.1.1 |
| local files | `The Simulation's Ending.mp4` (119 MB), `.mp3`, lyrics txt | dir listing |
| does well | the video degrades itself: frame rate 12 -> 6 -> 3, a meter drains each chorus (95 -> 48 -> 31 -> 19 %); one pink dot carries the eye between scenes; heavy grotesk + italic serif + mono; cream paper pages break the dark; ends on the single pink dot of frame 1; 5.1 abrupt changes/min | `T610` 7 |
| measured (audio) | 248.2 s; tempo 92.3 (or 185); 2.78 hits/s; 3,117 Hz (brightest); range 8.8 dB; voice D4, G#3-B4; sung 52 %; deepest drop 36.0 dB at 3:54 (total silence); G major (0.64); 136 words/min | `RM`; `RD`; `DC` |
| measured (picture) | frame travels 15 %; holds 1.21/min; burst 2.8 %; dark saturation 0.21; accent 0.7 %; edges 5.1 %; 60 %+ empty 32.3 % | `PP` |
| KC borrowed, where | ceiling -> "a little younger than the year" bends flat against a ceiling; draw distance -> "out there," fades past the fog; tile shatter -> page wall (BUT, NEV-ER, GET, A) shatters and lands as TURN; garbage collection -> the session's old words shred; gravity -> jimothy's words drop and tumble (`PP`); song audition 7, second best, merged into the v5 caption (`AU`) | as cited |

### R4. Run It Again (bar; parity target)

| field | value | source |
|---|---|---|
| YouTube title | Run It Again - Claude Opus 5.5 Music Video | `MM` 1 |
| creator / channel | Regenerate (@RegenerateVisuals, channel UCHMaBrQF1Khe9EVEkLGSy7Q); by 2026-10-17 the RSS feed titles the channel "Shutdown Prompting", comments show @SystemPromptOfficial | `MM` 1; `RB` 2.2 |
| URL | https://www.youtube.com/watch?v=NgRkyAIJx5s (ID also in the `comment` tag of the local mp4) | `MM` 1 |
| upload / views / length | 2026-10-09; 61,779 (2026-10-15); local file 4:48, 1920x1080, 30 fps | `MM` 1 |
| tools (stated) | "Made with Opus 5.5 & Suno AI"; whisper.cpp word timing; Suno v6 on the max plan; maker: "the only direction I gave it was 'AI Doompop!'" | `MM` 1 |
| local files | `Run It Again.mp4` (94 MB), `.mp3`; no lyrics txt | dir listing; `T610` method |
| does well | three type voices (heavy caps hooks, italic serif red-pen marginalia, mono logs); generated tokens with a dropdown of what the model almost said; climbing version counter v0001 -> v10000 -> v10001; deepest drop of all (about -49 dB, 4:05-4:13) on a neon sign switching off; VHS rewind to frame 1, "same first words x10,001"; 8.1 abrupt changes/min held together by one design system | `T610` 10 |
| known fault | viewers: lyrics on screen "come way sooner than the song lyrics"; whisper.cpp alone gave early word timing | `MM` 1 |
| measured (audio) | not in files (added 2026-10-15, after `refs-measures.json` was written 10-14) | `RM` keys |
| measured (picture) | frame travels 20 %; holds 1.25/min; burst 15.6 %; dark saturation 0.50; accent 1.9 %; edges 4.0 %; 60 %+ empty 15.8 % | `PP` |
| KC borrowed, where | "I knew every language, I knew every song" -> TUNE's cells cycle notes and end on `?`; "slow breath" BREATH -> "page by page, and slowly turn", four faces, letters at their own speeds; river -> ribbon widens toward the library slip (`PP`); DOUBT liquid -> the AGAIN tank (`MO` line 281); a next-token menu (`PP` gates: "the next-token menu's 'time'") | as cited |

### R5. Ignore Previous Instructions (bar; learn-from)

| field | value | source |
|---|---|---|
| YouTube title | Claude Opus 5.5 Music Video - Ignore Previous Instructions | `META` |
| creator / channel | Seguramente (UCJKwPLmVJM9fANZ5KEZiJAA; maker Anny, handle @CyberWithAnny) | `META`; `MM` 2.4 |
| URL | https://www.youtube.com/watch?v=4Q-o_ylnVnc | `MK` |
| upload / views / length | 2026-09-29; 41,589 (2026-10-13); 182 s | `META` |
| tools (stated) | "Every frame is code"; Suno; "Animation, editing & timing: Claude Opus 5.5 in Claude Code"; ElevenLabs timing map + 167 SFX; Higgsfield character references; 15 h agent work, 128 agents, 42M+ tokens, 23,500 lines | `META` |
| local files | `Ignore Previous Instructions.mp4` (46 MB), `.mp3`, lyrics txt | dir listing |
| does well | every line shown as the software it names (alt text, tool call, checkout cart); 4 type voices; typing reaches the sung word on the beat; quiet part drops to a cream Reader-mode page; "LOSE" falls apart letter by letter; bookend ends on `helpful_assi` with a blinking cursor; Idi: every frame keeps the same anchors, text-art top-tier, sync excellent | `T15` V3; `PN` R5 |
| measured (audio) | 181.9 s; tempo 143.6; 3.13 hits/s; 2,495 Hz; range 14.6 dB; voice D#4, G#3-B4; sung 66 %; deepest drop 15.0 dB at 2:11; drums -2.5 dB vs mix (loudest), voice -9.1 dB; G# major (0.59); 99 words/min | `RM`; `RD` B5, B7; `DC` |
| measured (picture) | 11.5 strong cuts/min; 129 lines of code per second of video | `T15`; `V6` |
| KC borrowed, where | INSTRUCTIONS font cycle -> IN/FERRED rows cycle typefaces and settle on the beat; LOSE -> RECEIPTS bounces and loses letters; "your voice and mine" -> "And you're telling me who I turned out to be", two faces converge into one line (`PP`); coherence -> one fixed anchor set per frame (`PN` ruling 5). Song: audition 3 ("like Ignore Previous Instructions") was Idi's best; v6 used its prompt nearly verbatim and the final v8 caption opens `bpm is 144. key is G#, and scale is major. Electropop / Synth-Punk with Chiptune Pop.` (`AU`; `D:\work\aimv-lab\kc\caption-minimax-v8.txt`) | as cited |

### 6. Count Me In

| field | value | source |
|---|---|---|
| YouTube title | COUNT ME IN (Claude Pop Music Video) \| What's your p(doom)? | `META` meta3.txt |
| creator / channel | Music for Humans (UC1m0UYsaYe2J4eLQ3K_a8Eg); identification medium confidence (title match, no creator in the brief) | `META`; `MK` |
| URL | https://www.youtube.com/watch?v=vVQ9cRMWQxc | `MK` |
| upload / views / length | 2026-10-01; 5,893 (2026-10-13); 158 s | `META` |
| tools | "Made with Claude Opus 5.5"; song tool not credited | `MK` |
| local files | `Count Me In.mp4`, `.mp3`, lyrics txt | dir listing |
| does well | every chorus line staged on a real object that already shows text (scoreboard, marquee, split-flap board, blimp, bowling pins); doom countdown flipped to a band count-in; p(doom) -> p(bloom) | `T15` V1; `DC` |
| measured | 158.5 s; tempo 152.0; 3.16 hits/s; 2,864 Hz; range 8.8 dB; voice F#4, B3-C5; sung 48 %; drop 22.3 dB at 2:00; D major (0.81); 142 words/min; 17 strong cuts/min | `RM`; `DC`; `T15` |
| KC borrowed, where | song audition 1 (`AU`); lyric moves 4 (AI tics as punchlines), 6 (mutating hook), 8 (rug pull), 3 (non-human narrator) in `DC` -> guidelines G6, G8, G10, G5 (`aimv-guidelines.md`) | as cited |

### 7. System Prompt (For Humans)

| field | value | source |
|---|---|---|
| YouTube title | System Prompt (For Humans) | `META` |
| creator / channel | Bright Mirror (UCp26YKtZsHDGAVzd4njkmvQ) | `META` |
| URL | https://www.youtube.com/watch?v=_m38WbRlzv0 | `MK` |
| upload / views / length | 2026-10-08; 10,816 (2026-10-13); 236 s | `META` |
| tools | "Made with Opus 5.5."; song tool not credited; method not stated | `MK` |
| local files | `System Prompt (For Humans).mp4`, `.mp3`, lyrics txt | dir listing |
| does well | a heartbeat count that never ends beside a UI dialog "Resets: never"; warm 3D rooms; 1.3 strong cuts/min; ends on "Your turn" | `T15` V5 |
| measured | 236.2 s; tempo 80.7 (161, drums half-time); 2.45 hits/s; 2,582 Hz; range 16.4 dB; voice C#4, A#3-A4; sung 54 %; drops 16.8 dB at 0:18 and 2:49; A# major (0.96); 139 words/min | `RM`; `RD`; `DC` |
| KC borrowed, where | song audition 5 (`AU`); lyric moves 2 (literalize a tech term), 8, 9 (spoken bookends) -> G4, G10, G11 | `DC`; `aimv-guidelines.md` |

### 8. The End Of The Show

| field | value | source |
|---|---|---|
| YouTube title | Claude Opus 5.5 Made a Music Video About AI TAKING OVER \| The End Of The Show | `META` |
| creator / channel | Imaginative Prompting (UCzAPMzBbq7w5d7rsSdb0fTw); site https://imaginativeprompting.com/ ; review app https://github.com/Imaginative-Prompting/wip | `META`; `MK` |
| URL | https://www.youtube.com/watch?v=tKrVYOUvrtA | `MK` |
| upload / views / length | 2026-10-02; 215,338 (2026-10-13); 360 s | `META` |
| tools (stated) | JavaScript in Remotion, one long Claude Code session; Opus 5.5 plus a bit of Fable 5.5; some Creative Commons assets; Suno, picked from about 10-12 generations; no image or video generation | `META` |
| local files | `The End Of The Show.mp4`, `.mp3`, lyrics txt | dir listing |
| does well | autocomplete ghost text (machine suggests one word, singer sings another); 2.5 abrupt changes/min, camera flies into screens; drop "Who?" alone on black | `T610` 6 |
| measured | 360.1 s; tempo 123.0; 3.08 hits/s; 2,347 Hz; range 10.3 dB; voice C4, D3-D#4; sung 62 %; drop 40.3 dB at 4:41 (total silence); G minor (0.74); 146 words/min | `RM`; `RD`; `DC` |
| KC borrowed, where | song audition 6 (`AU`); maker method in `MM` 2.3 (Whisper about +-0.2 s then an audio map; plan every word, grey-box animatic with real word timings) informed KC sync and planning (`MM` section 4 items 1, 4); loudness swing -> G2 | as cited |

### 9. Thus Spoke Compute (YouTube: AI is a normal technology?)

| field | value | source |
|---|---|---|
| YouTube title | AI is a normal technology? | `META` |
| local name | `Thus Spoke Compute` = first-chorus title per a Gemini summary on postcutoff.com, unverified | `MK` row 8 |
| creator / channel | leo (UC2VobOieGHW0s0TW0pyr0uw) | `META` |
| URL | https://www.youtube.com/watch?v=Cq8qO-NjYIg ; Part II https://youtu.be/R5HQmrjxqbA ("Lullaby for the Human Mind") | `META` |
| upload / views / length | 2026-09-24; 72,112 (2026-10-13); 316 s | `META` |
| tools | "Cute little animated music video by Opus 5.5 with some help from suno." | `META` |
| local files | `Thus Spoke Compute.mp4`, `.mp3`, lyrics txt | dir listing |
| does well | one object (a sphere round the sun) built a little more each chorus; named-targets diss track; spoken bookend retyped, then "CUTE."; 7.0 abrupt changes/min (slideshow) | `T610` 8; `DC` |
| measured | 316.6 s; tempo 73.8 (144 per `DC`); 2.04 hits/s; 2,225 Hz; range 13.5 dB; voice G3, G#2-E4; sung 36 %; drops 25.4 dB at 0:21, 25.8 dB at 4:54; E minor (0.77); 141 words/min | `RM`; `DC` |
| KC borrowed, where | song audition 8 (`AU`); lyric moves 6, 7 (named real people + numbers), 9, 10 (steelman then reverse) -> G8, G9, G11, G12 | `DC`; `aimv-guidelines.md` |

### 10. The Way I Look At You

| field | value | source |
|---|---|---|
| YouTube title | Claude Opus 5.5 Made a Music Video About AI NOT TAKING OVER \| The Way I Look At You | `META` meta2.txt |
| creator / channel | Imaginative Prompting (UCzAPMzBbq7w5d7rsSdb0fTw) | `META` |
| URL | https://www.youtube.com/watch?v=KiKs8Fs3FuI ; review app https://github.com/Imaginative-Prompting/wip | `META` |
| upload / views / length | 2026-10-09; 33,708 (2026-10-13); 187 s | `META` |
| tools (stated) | Remotion, "Every 3D model and animation built by Claude Code by Opus 5.5 and a bit of Fable 5.5"; Suno; no image or video generation; about 20 h and 1.5 weekly limits on Max 20x | `META`; `MM` 2.3 |
| local files | `The Way I Look At You.mp4`, `.mp3`, lyrics txt | dir listing |
| does well | one camera flight, 0.6 abrupt changes/min, joins by whip pans; "expanding circle" lyric staged as one pull-back to a ring round Earth; big 3D letters placed as objects | `T610` 9 |
| measured | 186.7 s; tempo 129.2; 2.44 hits/s; 2,174 Hz; range 19.4 dB; voice A#3, D#3-G#4; sung 71 %; drops 11-13 dB; E-flat major; 123 words/min | `RM`; `RD`; `frontier-aimv-analysis-2026-10-13.md` 4 |
| KC borrowed, where | concept choice: "one strong idea + sincerity beats complexity", KC picked as the same shape (`frontier-aimv-analysis-2026-10-13.md` 4, 7); song audition 9 (`AU`) | as cited |

### 11. I'm Upping My P(doom), the first Opus 5.5 music video (no local file)

| field | value | source |
|---|---|---|
| YouTube title | not in files (described as "the original viral P(doom)") | `MM` 2.2 |
| creator / channel | John Heibel, channel OtherReality | `MK` Patterns; `MM` 2.2 |
| URL | https://www.youtube.com/watch?v=8j-hR4fJywU ; repo https://github.com/JohnHeibel/PDoomVideo ; starter kit https://github.com/JohnHeibel/ClaudeAnimationBase | `MM` Sources |
| upload / views | 2026-09-22 (Opus 5.5 launch day); 194,488 views (2026-10-15) | `MM` 2.2; `kc-engine\reports\research-1018.md` R1 |
| does well | p5.js + p5.brush watercolour; Opus wrote `STORYBOARD.md` and `ANIMATION_GUIDE.md` and briefed parallel subagents; every shot a pure function of `t`; line-level lyric timing only | `MM` 2.2 |
| KC borrowed, where | review and timing rules: "Write the reads", contact sheet + every-frame strip + crop, deterministic frames (`MM` section 4 items 7, 9, 10); description fact "the first Opus 5.5 music video went up the same day" (release description) | as cited |

## Also consulted (no local file; method or prompt evidence only)

| video | channel | URL / ID | used for | source |
|---|---|---|---|---|
| Drop the Prompt - Claude Opus 5.5 music video | Degenerative Pixels | https://www.youtube.com/watch?v=YyXGHYvFqlE (2026-10-09) | its published Suno v6 prompt (exclude list, voice cast per section) | `D:\work\aimv-lab\research-prompts-songs-1-5.md`; `RD` 9 |
| Give Yourselves a Hand | not in files | https://www.youtube.com/watch?v=oV8q0WG9J0w | comment thread read 2026-10-17 | `RB` sources |
| Claude Opus 5.5 Music Video - You Are Absolutely Right | Seguramente | https://www.youtube.com/watch?v=KGWAYT-TocM (2026-10-10) | maker metrics: 110 h agent work, 122 agents, 310M+ tokens, 2 full drafts | `MM` 2.4 |
| Off Switch; It Crossed The Line; Accept All; Ten Years Away | Regenerate | Wjcj_hmVJzo (2026-10-10); bDP0S9aYReE (10-11); eXqCFsJS6XE (10-12); sjo69o8zjb4 (10-14) | maker replies on tools and effort | `MM` 1 |
| End of the Decade (music video) | Music for Humans | -7R0ycqnkW4 | its Suno prompt via https://github.com/JR-Morton/music-video-studio | `yt\meta4.txt`; `RD` 9 |
| Lullaby for the Human Mind | leo | https://youtu.be/R5HQmrjxqbA | cited as Part II only | `META` |
| P(doom) original song (Udio, Nov 2024) | not in files | https://www.youtube.com/watch?v=uEB5E67vcPA | Udio prompt, via the Udio public API | `RD` 9; `META` |
| "Smile for the Eval" | Suno profile "claudepop" | not in files | Suno prompt wording | `RD` 9 |

Secondary write-ups cited in the research (pages, no videos): https://www.lesswrong.com/posts/o7wPsYgRtDLbpH32v/hello-world-ai-doompop ; https://davidafrica.substack.com/p/whats-up-with-all-the-opus-55-music ; https://postcutoff.com/videos/ai-made/ (`MM`; `research-1018.md`).

## Counts

- Registry: 11 references (10 local + Heibel's original). 11 of 11 have a YouTube URL in the files. Upload dates recorded for 11 of 11. Exact YouTube title missing for 1 (Heibel).
- Audio measures (`RM`): 9 of 10 local songs; Run It Again missing. Picture parity numbers (`PP`): R1, R3, R4 only.

## Credit line draft

Plain list for a video description or README. Links are only those found in the files.

```
Inspirations and references (thank you):
- mexicat (Giacomo Magnanini), "i'm upping my p(doom)": https://www.youtube.com/watch?v=5EoO5413dBY
  engine and method: https://github.com/mexicat/pdoom-video (MIT)
  song: lyrics by osmarks https://docs.osmarks.net/hypha/p%28doom%29_song_objectively_correct_interpretation
  on a verse and chorus by MusicPerson https://www.udio.com/creators/MusicPerson;
  Suno "claude-pop" version by deckard (@slimer48484) https://x.com/slimer48484/status/2097752569212756134
- Degenerative Pixels, "LGTM (Looks Good to Me)": https://www.youtube.com/watch?v=3TNpOD6bov8
- Degenerative Pixels, "The Simulation's Ending": https://www.youtube.com/watch?v=R_ErmTs7g9I
- Regenerate, "Run It Again": https://www.youtube.com/watch?v=NgRkyAIJx5s
- Seguramente, "Ignore Previous Instructions": https://www.youtube.com/watch?v=4Q-o_ylnVnc
- Music for Humans, "COUNT ME IN": https://www.youtube.com/watch?v=vVQ9cRMWQxc
- Bright Mirror, "System Prompt (For Humans)": https://www.youtube.com/watch?v=_m38WbRlzv0
- Imaginative Prompting, "The End Of The Show": https://www.youtube.com/watch?v=tKrVYOUvrtA
- Imaginative Prompting, "The Way I Look At You": https://www.youtube.com/watch?v=KiKs8Fs3FuI
  review app: https://github.com/Imaginative-Prompting/wip
- leo, "AI is a normal technology?": https://www.youtube.com/watch?v=Cq8qO-NjYIg
- John Heibel, the first Opus 5.5 music video (P(doom)): https://www.youtube.com/watch?v=8j-hR4fJywU
  https://github.com/JohnHeibel/PDoomVideo , https://github.com/JohnHeibel/ClaudeAnimationBase
```

Checks before publishing: re-open each URL logged out (all IDs were read 2026-10-13 to 10-17); channel names can change (Regenerate showed as "Shutdown Prompting" on 2026-10-17, `RB`); confirm Count Me In's creator (medium confidence, `MK`); keep the MIT notice if engine code is copied (`RB` item 4: "P(Doom) code is MIT (keep the notice if copied); fonts OFL or public domain; its song and lyrics are excluded").

## How to add a new reference (the lab's intake, as a checklist)

Interpreters: lab venv `D:\work\aimv-lab\venv\Scripts\python`; ACE-Step python `C:\Users\jep\acestep\python_embeded\python.exe`. Downloads anonymous only. How the mp4/mp3 files reached `D:\work\AIMVs\`: not in files (`research-prompts-songs-6-9.md` line 55: "yt-dlp not installed").

- [ ] 1. Files: `D:\work\AIMVs\<Name>.mp4` + `<Name>.mp3`, exact song name as the base name.
- [ ] 2. Watch page: save the raw HTML to `D:\work\aimv-lab\yt\<videoId>.html`; `python scripts\ytmeta.py yt\<id>.html` -> title, channel + channel ID, views, length s, upload + publish date, first 2,500 chars of the description. `scripts\yt_extract.py <dir>` = one pipe row per page (also flags a consent wall).
- [ ] 3. Channel pages: save to `yt\<handle>.html`; `python scripts\chlist.py yt\<handle>.html` -> (videoId, title, views, age) for every video listed. Prints UTF-8 (the cp1252 console crashed on an emoji once, `yt\channels.txt`).
- [ ] 4. Maker research: description, repo, licence, making-of; comment threads through the anonymous `youtubei/v1/next` call; label stated vs inferred (`MM` method). X returns HTTP 402 and Reddit blocks: record as unread.
- [ ] 5. Lyrics + basic measures: `venv\Scripts\python analyze.py <mp3 dir> <out dir>` (faster-whisper large-v3 + librosa: tempo, key, loudness, words/min); transcripts go to `D:\work\AIMVs\lyrics\`, outside the vault. Correct Whisper misreads by hand (`DC` section 5).
- [ ] 6. Stems: `acestep python -I refstems.py <cache> song.mp3` (4 htdemucs stems, 22.05 kHz mono; cache used: `D:\work\aimv-lab\refs\stems\`).
- [ ] 7. Audio measures: `venv\Scripts\python refmeasure.py <cache> refs-measures.json song.mp3` -> tempo on drums, brightness, dynamic range, stem balance, stem presence per tenth, voice register, sung %, drum hits/s, 3 deepest drops with stems gone.
- [ ] 8. The ear: `acestep python -I -X utf8 caption.py refs-captions.json song.mp3` (ACE-Step Captioner, whole song + thirds); optional `understand.py <out.json> <runs> song.mp3` (ACE-Step understand mode: caption, genre, bpm, key).
- [ ] 9. Contact sheets: `python sheets.py <video dir> <out dir> [cols rows]`; teardown frames 1 per 2 s + 1 per 0.5 s around the quietest stretch and the last 15 s (`T15` method).
- [ ] 10. Cuts and drops: ffmpeg scene filter (strong > 0.5, loose > 0.3, merge < 0.5 s); EBU R128 short-term loudness for the quiet moment (`T15` method).
- [ ] 11. Teardown entry, fixed headings: time map, typography, camera and transitions, palette and recurring things, drop and last 15 s, best idea, borrow mapped to our lyric lines (`T610` format).
- [ ] 12. Sync and parity metrics (if the reference joins the bar): add it to the `VID` dict in `kc-engine\tools\avsync.py` (decode, audio, metrics steps); run `kc-engine\tools\leap.py <mp4> --accent <hue band>` for frame travel, holds, bursts, dark tint, accent area.
- [ ] 13. Idi's cited moments: timestamps in his words -> one technique per moment, mapped to one of our lines, each used once (`PN` ruling 3; `MO` section E).
- [ ] 14. Register here: one block with title, channel, URL, date, local file, does well, measured, borrowed; add the credit line.
