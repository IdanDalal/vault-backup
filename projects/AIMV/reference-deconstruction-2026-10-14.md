---
type: project
created: 2026-10-14
author: jep
status: active
---

# The 9 references, taken apart box by box

Purpose: give Idi a menu. Per box, pick the song(s) whose value you want for Knowledge Cutoff, e.g. `B2: 9, B5: 3+6`. Mixing is fine, "none" is fine. Previous: [[knowledge-cutoff-prompt-v4-2026-10-14]].

Song numbers: **1** Count Me In · **2** I'm Upping My P(Doom) · **3** Ignore Previous Instructions · **4** LGTM · **5** System Prompt (For Humans) · **6** The End Of The Show · **7** The Simulation's Ending · **8** Thus Spoke Compute · **9** The Way I Look At You · **C** = our take C (seed 1004), for contrast.

## 0. Where each cell comes from

| Source | What | Trust |
|---|---|---|
| Ear | ACE-Step Captioner (MIT, the model ACE-Step built to label its training songs), run locally on each song in 3-5 parts | medium. Calibration: on take C it named 4 of 4 of Idi's own notes unprompted ("animated film theme", "clean piano", "gang 'Oh!' ad-libs", "noise section before cutting out"). One song, so n = 1 |
| Meter | measured on separated parts (drums, bass, other instruments, voice): tempo, key, loudness balance, drum hits per second, brightness, drops, voice pitch | high for levels and drops; tempo can read half or double; key medium |
| Maker | the creator's own words, or a production note they published | high |

Raw data: `D:\work\aimv-lab\refs-captions.json`, `refs-measures.json`, research files `research-prompts-songs-1-5.md`, `-6-9.md`, `research-audio-to-prompt.md`.

## B1. Genre, tempo, key

| # | Genre (ear) | BPM (meter) | Key (meter) |
|---|---|---|---|
| 1 | hyperpop, J-core electropop | 152 | D major |
| 2 | synth-pop; original Udio prompt: Electropop, Synthpop, Anthemic, Playful | 129-132 | D# major |
| 3 | aggressive electropop / synth-punk, cyberpunk | 144 | G# major (weak) |
| 4 | nu-disco, 80s dance-pop, retro-funk (maker hashtag: #nudisco) | 118 | D# major |
| 5 | hyperpop, glitchy, futuristic | 161 (drums half-time) | A# major |
| 6 | nu-disco synth-pop; audience: "80s-90s", "Ed Sheeran", "Jason Mraz" | 123 | G minor |
| 7 | chiptune pop / hyperpop, video-game | 92 or 185 | G major / E minor (weak) |
| 8 | theatrical orchestral hip-hop, musical-theater villain number; audience: "Disney villain song" (80 likes) | 144 | E minor |
| 9 | anthemic indie pop into 80s new-wave synth-pop, "stadium" | 128 (maker note) | E-flat major |
| C | electropop + piano ballad, "musical theater or animated film theme" | drums read 86 (asked 124) | D major |

## B2. Lead voice

| # | Who and how (ear) | Median note, range (meter) | Sung % (meter) |
|---|---|---|---|
| 1 | female, bright, bratty-confident, heavy auto-tune; rapid-fire almost-rap verses, soaring chorus | F#4, B3-C5 (highest) | 48 |
| 2 | female, clear, powerful, high; layered, reverb + delay | E4, C4-C5 | **74** |
| 3 | female, assertive, confrontational, digitally processed; near-spoken verses, soaring chorus | D#4, G#3-B4 | 66 |
| 4 | female, belted, confident + a robotic male vocoder voice rapping verses (call and response) | D#4, two voices | 45 |
| 5 | female, bright, heavily auto-tuned, "robotic precision", pitch-shifted | C#4, A#3-A4 | 54 |
| 6 | male, clear, conversational cynical narrator; patter-song verses, anthemic chorus | C4, D3-D#4 | 62 |
| 7 | female, high, Vocaloid-like; rapid almost-rapped verses, melodic chorus | D4, G#3-B4 | 52 |
| 8 | male, declamatory, theatrical; rap with show-tune flair, operatic chorus | G3, G#2-E4 (lowest) | 36 |
| 9 | male tenor, clear and earnest verses, powerful chorus | A#3, D#3-G#4 | 71 |
| C | female, clear, youthful; "almost rap-like" verse, emotive ballad section | E4, C#4-A4 | 59 |

## B3. Backing vocals and ad-libs

| # | What (ear, maker notes) |
|---|---|
| 1 | stuttering vocal chops, robotic countdown, shouted backing vocals, final whispered command |
| 2 | layered harmonies; wordless "oohs / ahs" hook near the end; vocal chops in the outro |
| 3 | robotic vocal sample opens; shouted chorus vocals; glitchy vocal chops |
| 4 | shouted gang-vocal responses; vocoder call and response |
| 5 | stuttering vocal chops, pitch-shifted harmonies |
| 6 | layered harmonies that grow into wide stadium gang vocals at the end |
| 7 | scat-sung hook, robotic voice sample, catchy post-chorus hook |
| 8 | mixed choir chanting the hooks, "robotic choir", gang chant |
| 9 | "whoa-oh-oh" hooks, gang-chant section, post-chorus "oh-oh-oh" ad-libs |
| C | gang "Oh!" ad-libs, choir-like harmonies |

## B4. Instruments

| # | Lead and bass (ear) |
|---|---|
| 1 | distorted growling synth bass, big synth chords, J-core arpeggios |
| 2 | pulsing sequenced synth bass, bright arpeggios, shimmering pads |
| 3 | gritty sliding distorted synth-bass riff as the main hook, glitchy stabs |
| 4 | funky synth bass, brassy synth stabs, arpeggios |
| 5 | distorted synth bass and deep sub, plucky leads, shimmering pads |
| 6 | funky melodic synth bass, brassy synth stabs, plucky keys |
| 7 | bouncy synth bass, chiptune arpeggios |
| 8 | orchestral strings (fast runs, staccato hits), brass stabs, timpani; synth bass in the rap parts |
| 9 | clean arpeggiated electric guitar, later brassy synth stabs and pads |
| C | **clean piano**, atmospheric pad, punchy synth bass |

## B5. Drums and groove

| # | Pattern (ear, maker) | Drum level vs mix (meter) | Hits per second (meter) |
|---|---|---|---|
| 1 | relentless, glitchy drum machine | -6.1 dB | 3.2 |
| 2 | four-on-the-floor | -3.1 | 2.8 |
| 3 | relentless four-on-the-floor | **-2.5** (loudest) | 3.1 |
| 4 | tight four-on-the-floor | -3.8 | 3.2 |
| 5 | punchy, half-time feel | -3.8 | 2.5 |
| 6 | four-on-the-floor | -2.8 | 3.1 |
| 7 | punchy drum machine | -4.5 | 2.8 |
| 8 | hip-hop beat, timpani | -7.2 | 2.0 |
| 9 | chorus 1 sparse ("claps and hats, no bass, no full kit"), kit stops for a line, slams back; gated-reverb drums | -4.2 | 2.4 |
| C | "simple steady beat with a snap" | -5.4 | **1.9** (974: 1.6) |

## B6. Arc, sections, drops

Drop = the music falls away for a moment, then slams back. Meter shows the deepest one and which parts vanish.

| # | Arc (ear, maker) | Biggest drop (meter) |
|---|---|---|
| 1 | spoken countdown intro; melodic bridge; **key change into the final chorus**; whispered ending | 22 dB at 2:00, everything out |
| 2 | atmospheric bridge, then a final climactic chorus; abrupt end | 18 dB at 2:19, band out, voice stays |
| 3 | robotic spoken intro and outro; filtered spoken monologue breakdown; riser into the final chorus | 15 dB at 2:11 |
| 4 | spoken intro and outro; vocoder section | 7 dB: steady energy, no real drop |
| 5 | robotic spoken intro; atmospheric bridge | 17 dB at 0:18 and 2:49, music and voice out, drums stay |
| 6 | pre-chorus, post-chorus hook; breakdown into the final chorus; "the drop into the outro" (maker note) | **40 dB at 4:41, total silence** |
| 7 | scat intro; filtered interlude; abrupt end | 36 dB at 3:54, total silence |
| 8 | spoken intro monologue; spoken interlude; cinematic instrumental climax | 25 dB at 0:21 and 4:54 |
| 9 | line sung over near-silence (0:34); silence before the bridge (1:53); quiet guitar outro | 11-13 dB |
| C | piano-ballad section; spoken interlude over silence; noise tail | 16-28 dB, voice-only gaps |

## B7. Mix

| # | Brightness (meter, Hz; higher = brighter) | Loud-quiet range (meter, dB) | Voice level vs mix (meter) |
|---|---|---|---|
| 1 | 2,864 | 8.8 | -4.3 |
| 2 | 2,426 | 9.4 | -6.6 |
| 3 | 2,495 | 14.6 | -9.1 (voice tucked under the drums) |
| 4 | 2,765 | 9.4 | -6.3 |
| 5 | 2,582 | 16.4 | -4.6 |
| 6 | 2,347 | 10.3 | -5.8 |
| 7 | **3,117** | 8.8 | -3.5 |
| 8 | 2,225 | 13.5 | -4.0 |
| 9 | 2,174 | 19.4 | -4.2 |
| C | 2,167 | 20.6 | **-2.9** (loudest voice of all) |

## 8. Where our takes differ from all 9 (meter, high confidence on the numbers)

1. Drums quieter: C -5.4, 974 -5.2 dB; 6 of 9 references sit at -2.5 to -4.5.
2. Drums sparser: C 1.9, 974 1.6 hits per second; references 2.0-3.2. Fits "loses the beat".
3. Voice louder than in any reference (-2.9 vs -3.5 to -9.1).
4. Darker mix: 2,017-2,167 Hz vs 2,174-3,117.
5. Genre words: the ear calls the references hyperpop, nu-disco, synth-punk, chiptune, cyberpunk, new wave. It calls C and 974 "musical theater" and "animated film". Of the 9, only 8 (Thus Spoke Compute) gets the theater label, and its audience hears a Disney **villain**.
6. Piano: the ear hears it in **0 of 9 references** and in both of our takes (both the v3 and v4 prompts asked for "soft piano": the piano is ours, and the fix is to drop it).

## 9. Real prompts found (verbatim, other makers)

None of the 9 songs has its own prompt published. Closest real ones:

| Whose | Prompt | Source |
|---|---|---|
| P(Doom) original (Udio, 2024) | `Female vocalist, Electronic, Electropop, Pop, Energetic, Anthemic, Melodic, Playful, Synthpop, Uplifting, Optimistic` | Udio public API |
| Song 4's maker, sibling song "Drop the Prompt" (Suno v6) | `dark hyperpop trap fusion, K-pop boy band polish, four male vocalists trading parts, dark creepy low raspy rap verse with a pitched-down demonic vocal double and sinister whispered ad-libs, soaring high tenor pre-chorus, explosive chorus with stacked group vocals and gang shouts, distorted electric guitar synth, heavy distorted 808s, hard crisp trap drums, glitchy vocal chops, menacing minor key, cocky swagger, playful melodic rap bridge over a stripped-down beat`; exclude `female vocals, ballad, acoustic, lo-fi, country, slow tempo` | YouTube description |
| Song 1's maker, "End of the Decade" (Suno) | `Indie folk ballad led by a music-box whistled hook, fingerpicked steel-string guitar ..., close-miked spacious mix, tape saturation, short room reverb, subtle double-tracked harmonies; restrained 78 bpm sway; intimate, dry female lead`; exclude `heavy distortion, screaming, rap, trap hi-hats, dark minor key` | github.com/JR-Morton/music-video-studio |
| Suno profile "claudepop", "Smile for the Eval" | `Dark theatrical electro-pop, industrial hip-hop groove, 114 BPM, minor key, commanding resonant male baritone, crisp diction, ... sudden silence before the final spoken line` | Suno public profile API |

Lessons, all stated by makers:

1. Voice cast per section ("rap verse, high tenor pre-chorus, gang-shout chorus").
2. An exclude list is standard; one maker excludes `rap` by name. MiniMax has no exclude box (inference: phrase exclusions inside Vocal Style, as v4 does).
3. Take selection does the work: song 6 = 10-12 takes, "Drop the Prompt" = 49 takes. Song 7's maker: "prompting isn't really the angle here. It's patience."
4. Asked tempo drifts (song 1's maker: asked 124, got 113).

## 10. Next, once you mark the boxes

jep writes v5 from your marks in MiniMax's trained format, runs 8 seeds, and **screens every take with the ear** (flag "musical theater", "piano ballad", "rap-like", "noise") before you hear the top 3.

Alternative (jep's divergent option): "auditions". Turn each reference's ear description into a MiniMax caption, sing our lyrics in all 9 styles, 2 seeds each (~75 min of machine time), and you pick by ear instead of by reading.
