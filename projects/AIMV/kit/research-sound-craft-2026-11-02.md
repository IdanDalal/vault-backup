---
type: research
created: 2026-11-02
author: Agent sound-craft
---

# Sound craft: the 9 bar songs taken apart, with MiniMax levers

**Verdict.** The 9 bar songs breathe and KC sits on a plateau. They drop 6 to 15 dB into sparse valleys and climb back up to 9 times per song, the climbs ending higher as the song goes on, and they punctuate with dead stops of total silence. KC: loudness range 4.3 LU (bar songs 6.4 to 11.8), 1 % of its seconds rise 2 dB above its own average (bar songs 8 to 21 %), and its loudest 15 s fall in the first third (7 of 9 bar songs: last third, +1.5 to +3.9 dB higher). Idi's "volatility" comes in three measured forms, one per sound-bar song: **valleys** (It Crossed The Line), **dead stops** (Tell Me No: 6 full stops, 25 to 74 dB), **escalation plus a switching sub-bass** (Not My Fault: +3.9 dB, the largest climb of the 9, with the bass pumping about 10 dB under each kick). Part of KC's plateau was written into our v8 caption ("several distinct instruments are clearly audible at all times", "relentless", "fast hi-hats", "sparkling highs"); section 3 turns each finding into caption words and lyric layout.

Song keys used below: **ICTL** It Crossed The Line, **NMF** Not My Fault, **TMN** Tell Me No (sound bar); **FB** Final Boss, **HTH** Hope This Helps!, **OS** Off Switch, **FOOM** Nothing Went Foom!, **SU** Scroll Up!, **WC** What Counts (song + lyric bar); **KC** Knowledge Cutoff (ours, take v8B).

## 0. Sources, labels, trust

| Label | Source | Trust |
|---|---|---|
| (m) measured | `dynmap.py` (new, below), `refmeasure.py`, `analyze.py`, EBU R128 short-term loudness via `ffmpeg ebur128` | high for levels, swings, stops; bass pump and sub share medium (Demucs can leak an 808 kick into the bass stem); tempo can read half or double; key medium (confidence 0.65 to 0.91) |
| (e) ear | ACE-Step Captioner, whole song (only under 200 s: NMF, OS) or 3-4 parts, plus 11 transition windows on the sound-bar songs | medium; calibrated once on KC take C (4 of 4 of Idi's notes), n = 1. It hears TMN as "minimal trip-hop" and misses its stops |
| (o) official | maker lyric sheets with section tags (FB, HTH, FOOM, SU, NMF), mapped to Whisper line times; OS from the screen-read file | high for labels, about ±2 s on times |
| (i) inferred | jep's reading of the numbers, and every caption lever | untested until auditioned |

Definitions used once here: **LRA** = EBU loudness range in LU, the spread between the song's quiet and loud passages. **Short-term loudness** = loudness over a sliding 3 s window, sampled every 1 s. **Swing** = a trough-to-peak climb of at least 6 dB on that curve (zigzag method; "big swing" at least 10 dB). **Body** = the song's integrated loudness (I). **Peaks %** = share of seconds at I+2 dB or louder; **valleys %** = share at I-6 dB or quieter. **Escalation** = loudest 15 s in the last third minus loudest 15 s in the first third. **Drop** = a 0.1 s dip at least 8 dB under the next 4 s that slams back; **full stop** = a drop at least 25 dB deep (near silence). **Pump** = how much the bass rises 100 to 200 ms after each kick versus 0 to 60 ms after it (sidechain-like ducking or off-beat notes; either way kick and bass alternate). **Sub share** = bass-stem energy under 60 Hz. **Off-beat %** = bass onsets on the "and" of the beat.

Files and tools:
- New: `D:\work\aimv-lab\dynmap.py` (usage in its docstring): short-term loudness, swings, section runs with stems on, drops with the trick before, bass bands, pump, notes per beat, slides, stem lifecycle, fine tempo (median beat interval, which avoids librosa's 129.2 / 136.0 / 143.6 lag grid that `refmeasure.py` printed for 5 songs).
- Raw output: `C:\Users\jep\.claude\jobs\99182c36\tmp\sound\` (`dynmap.json`, `dyn.txt` digest, `refmeasure.json`, `captions.json`, `capwin.json`, `summary.txt`, `bassgrid.txt`, scripts in `scripts\`).
- Stems: `D:\work\aimv-lab\refs\stems\` (9 new songs added, htdemucs).

## 1. Volatility profile (m)

| | bar | LRA LU | p10-p95 dB | peaks % | valleys % | swings ≥6 dB (n, /min, mean, median gap s) | big swings ≥10 | escalation dB | drops ≥8 / ≥15 / full stops | deepest drop | drum re-entries | bass pump dB | sub % | drum hits/s | brightness Hz | words/min |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ICTL | sound | **11.8** | 11.9 | **21** | **20** | 7, 1.40, 12.6, 36 | 5 | +2.0 | 14 / 3 / 1 | 37.0 @3:09 | 2 | 5.7 | 53 | 1.25 | 2,158 | 79 |
| NMF | sound | 6.8 | 6.9 | 12 | 3 | 1, 0.36, 14.1, - (≥4 dB: 3) | 1 | **+3.9** | 4 / 0 / 0 | 9.3 @1:06 | 1 | 9.8 | 54 | 2.28 | 2,277 | 113 |
| TMN | sound | 7.8 | 8.0 | 10 | 9 | **8, 2.05**, 10.4, **24** | 3 | -0.5 | 14 / **11 / 6** | **73.6 @3:11** | 5 | **10.9** | 57 | 2.04 | **1,711** | 135 |
| FB | song | 10.7 | 10.7 | 14 | 16 | **9**, 1.51, 11.0, 34.5 | 5 | +1.9 | 14 / 9 / 1 | 32.6 @3:32 | 3 | 5.3 | 27 | 2.62 | 2,732 | 133 |
| HTH | song | 9.8 | 9.9 | 15 | 11 | 6, 1.09, 11.2, 57 | 4 | +2.4 | 14 / 2 / 0 | 22.7 @5:24 | 5 | 4.8 | 18 | 2.54 | 2,586 | 144 |
| OS | song | 6.4 | 6.5 | 8 | 6 | 2, 0.83, 12.9, 38 | 2 | +1.5 | 8 / 1 / 1 | 34.6 @1:54 | 3 | 4.7 | 30 | 2.25 | 2,039 | 141 |
| FOOM | song | 7.4 | 7.4 | 16 | 4 | 6, 1.20, 9.2, 40 | 1 | +3.0 | 10 / 2 / 1 | 32.0 @1:34 | 4 | 8.1 | **75** | 2.74 | 2,598 | 176 |
| SU | song | 9.1 | 9.3 | 12 | 11 | 5, 0.91, 10.3, 47.5 | 3 | +2.4 | 12 / 4 / 1 | 28.2 @3:36 | 5 | 3.5 | 45 | 2.43 | 2,856 | 149 |
| WC | song | 8.2 | 8.8 | 9 | 11 | 2, 0.46, 15.6, 72 | 1 | +0.6 | 5 / 2 / 0 | 22.2 @3:16 | 1 | 2.3 | 54 | 1.68 | 1,987 | 101 |
| **KC** | ours | **4.3** | **4.3** | **1** | 4 | 3, 0.94, 10.4, 39.5 | 1 | **+0.1** | 12 / 3 / 1 | 35.1 @2:31 | 5 | 2.8 | 33 | **2.99** | **3,249** | 157 |

Readings (i):
1. KC's swing count is in range (3); it lacks height above and depth below the body. All 9 bar songs spend 8 to 21 % of their time above I+2; KC spends 1 %.
2. The sound-bar trio sits dark (1,711 to 2,277 Hz; of the other six only WC and OS fall in that band) and ICTL has the sparsest drums of the set (1.25 hits/s); KC is the brightest (3,249 Hz) and busiest (2.99 hits/s) of all 10.
3. The trio's bass pumps 5.7 to 10.9 dB (mean 8.8) with 53 to 57 % of its energy under 60 Hz; KC pumps 2.8 dB with 33 % sub. Among the song-bar six only FOOM (8.1 dB, 75 % sub) reaches that zone.
4. Three ways to be volatile: ICTL = valleys (20 % of seconds under I-6, 5 big swings); TMN = stops (11 drops ≥15 dB, a full stop about every 11 s in verse 1); NMF = escalation (+3.9 dB) and bass switching at nearly flat loudness (LRA 6.8, 1 swing).
5. WC is the calm control: 2 swings, LRA 8.2 from one long ambient outro. Idi ranks it for song and lyric, so volatility is a sound-bar requirement and optional for the song bar.

## 2. The sound rules, ranked, as MiniMax levers

Each rule: what the songs do (m), which songs, the lever (i), and the check on a take (dynmap numbers).

### R1. Valleys under the body: the band leaves, the song goes quiet, then returns
- (m) ICTL valleys 20 %, FB 16 %, HTH/SU/WC 11 %; KC 4 %. Mid-song quiet runs of 3 s or more: FB 4, ICTL 3, SU 3; KC 0. In FB/HTH/SU/FOOM the valleys are written sections: `[whisper1]`, `[whisper2]`, `[breakdown]`, `[spokenlow]`, `[cold]`, `[hit]` (o), 1 to 2 lines each, drums and bass at -56 to -67 dB under their peak.
- Lever, caption: Sonics box "huge contrast between quiet, sparse passages and explosive full-band sections"; Groove box "the intro and the opening of each verse have no drums and no bass"; delete v8's "several distinct instruments are clearly audible at all times" and "relentless".
- Lever, lyric: a 2-line whispered or spoken aside after each chorus, set off by `[Instrumental]` on both sides (MiniMax has no whisper tag; KC G23 showed `[Instrumental]` makes the band break). Verse openings of 2 short lines before the beat enters.
- Check: valleys % ≥ 8, LRA ≥ 7, at least 2 mid-song quiet runs ≥ 3 s.

### R2. Escalation: each loud section higher than the last, the final chorus the peak
- (m) NMF +3.9, FOOM +3.0, HTH/SU +2.4, ICTL +2.0, FB +1.9 dB; KC +0.1 with its loudest 15 s at 0:35. Lyric lengths (o), chorus 1 / chorus 2 / final: FB 9 / 5 / 10 lines; HTH 8 / 3 / 9; NMF 7 / 8 / 11. The final chorus is the longest; chorus 2 is the short one in the Bright Mirror songs.
- Lever, caption: Global Emotional Progression "the first chorus is held back; each chorus is bigger than the last; the final chorus is the loudest, densest moment, with gang vocals and distorted guitars added"; Groove "the full kit and the deep bass arrive together only from the second chorus on".
- Lever, lyric: chorus 2 cut to 3 to 5 lines, the final chorus the longest section of the song; `[Post-Chorus]` only after the final chorus.
- Check: escalation ≥ +1.5 dB; loudest 15 s inside the last third.

### R3. Stop and slam: total silence for a beat or two, then everything at once
- (m) TMN 6 full stops (0:19, 0:42, 1:58, 2:59, 3:10, 3:25; 25 to 74 dB, 0.6 to 3.2 s, voice gone too, slam back 28 to 69 dB); ICTL 37 dB at 3:08 before the last climax; FB 32.6 dB at 3:30 plus a riser and snare roll into a cold stop at 4:49; FOOM 32 dB at 1:32 after the chorus tag; OS 34.6 dB at 1:53 before the final chorus; SU 28 dB at 3:36. Trick in the 1 to 4 s before, over all 34 drops ≥15 dB in the 9 songs (a drop can carry two): riser 11, level sags 11, filter closes 7, drum roll 2, nothing detected 8. TMN ties a stop to its lyric: "and the room went quiet" lands on the 73.6 dB silence at 3:10.
- Lever, caption: Groove "the whole band stops dead for one beat of total silence before each chorus and drops straight back in"; Embellishments "a filter sweep down into each stop".
- Lever, lyric: put the stop where a line says silence or ends a thought; a 1 to 3 word line alone, then `[Instrumental]`, then the chorus. KC v8 got 1 full stop (35 dB) this way.
- Check: at least 2 drops ≥ 25 dB; at least 1 before a chorus.

### R4. A deep sub-bass that pumps against the kick and leaves between choruses
- (m) Trio sub 53 to 57 %, pump 5.7 / 9.8 / 10.9 dB; KC 33 %, 2.8 dB. NMF: 53 % of bass notes on the "and" (most syncopated with FB 66 %), glides on 41 % of notes, highest grit share of the 9 (3.2 % above 250 Hz, the "slightly overdriven" bass the ear names), bass out under verse 1 (-24 dB), pre-chorus 2 (-36 to -40), the break (-35) and the pre-final breakdown (-50), back at every chorus. SU and HTH keep the bass for choruses only (SU first bass at 1:18, the first chorus). TMN plays the sub in short stabs, 18 runs of 3 to 11 s, median note 0.23 s.
- Lever, caption: Instrument Lifecycle "a deep, slightly overdriven synth sub-bass on the off-beats, sidechained to the kick so it pumps, with short glides between notes"; Groove "the bass sits out the verses and pre-choruses and returns with each chorus"; Sonics "dark, heavy low end".
- Check: pump ≥ 5 dB, sub ≥ 45 %, bass re-entries at chorus starts.

### R5. The instrument family changes at the swing
- (e, m) ICTL: clean delayed guitar arpeggio in every valley, distorted guitars plus distorted synth bass at every peak ("massive, cinematic drop", "shoegaze or industrial"). NMF: chiptune and ragtime piano intro, electro-funk verses, synth-punk final chorus with a distorted guitar riff, clean guitar and a decelerating outro. FB, HTH, SU: music-box piano under the spoken intro, then the hyperpop slam; FB and HTH put a shred solo (chiptune lead, guitar) before the final run. OS: guitar and voice alone, the band enters at the first chorus.
- Lever, caption: write Instrument Lifecycle as a per-section timeline naming the swap ("verse: clean guitar only; chorus: distorted guitars and the bass take over; a distorted guitar stab opens each chorus").
- Check: ear caption on the loud window names a different instrument family than on the quiet window.

### R6. Dark, sparse, slower words
- (m) Trio brightness 1,711 to 2,277 Hz vs KC 3,249; drum hits 1.25 to 2.28/s vs KC 2.99; words/min 79 to 135 vs KC 157. Five of the song-bar six sit brighter (2,039 to 2,856; WC 1,987) and four sit denser (2.43 to 2.74; OS 2.25, WC 1.68), so this rule belongs to the sound bar, the "genre and style" Idi named.
- Lever, caption: remove "bright, sharp", "sparkling highs", "fast hi-hats", "chiptune sparkle" (v5 already showed speed words bring back rap-like verses, kit-audio-pipeline section 8); ask "dark, warm, spacious, room between the hits".
- Lever, lyric: 6 to 8 words per line; `[Instrumental]` before each chorus (G23 measured about 145 wpm with breaks).
- Check: brightness ≤ 2,600 Hz, drum hits ≤ 2.5/s, 110 to 140 wpm.

### R7. A second voice as a hook instrument; the lead follows the dynamics
- (e) NMF: deep robotic pitched-down voice chants the hook, answered by a higher voice; scat lines mimic the synth; the lead goes shouted and strained, a pleading falsetto, a long sustain before the final chorus. TMN: processed male speaking voice interjects between the female lines. FB: pitch-shifted male voice shouts "final boss". HTH: shouted call and response. ICTL: strained belting "to the point of cracking" at peaks, whispers in the last verse.
- Lever, caption: Harmony/Backing box names the second voice and where it speaks; Vocal Style maps register to dynamics ("whispered in the quiet sections, belted and strained at the peaks"). `Singer B (Male)` phrasing is inferred from the trained `Singer A (Female)` form; no local template shows a Singer B.
- Check: ear caption names two voices; sung % drops in valleys.

## 3. Per song

Section labels: (o) where the maker's sheet gives them, otherwise (i) from the transcript. State: quiet / mid / loud vs the song's own 90th percentile; D = drums on, B = bass on; dB after each stem = level vs that stem's own peak (m).

### 3.1 It Crossed The Line (sound bar)
- **Identity.** (e) cinematic indie rock into shoegaze / industrial walls; clean reverberant guitar verses, distorted wall-of-sound climaxes, wordless soaring harmonies. (m) 124.5 BPM; A# minor (0.66); 302 s; female narrative voice, D#4, A#3-B4, sung 70 %; 79 wpm, the sparsest words of the 9. Structure (i): one verse per year (2023, 2024, 2026, 2031, 2040), each verse ending in the "crossed the line" hook.
- **Dynamics map.**

| time | section (i) | state (m) | LUFS | what happens |
|---|---|---|---|---|
| 0:00-0:18 | intro | quiet, guitar only | -24.4 | clean arpeggio; drums -66, bass -59 |
| 0:18-0:50 | verse "2023" | quiet -> mid build, +13 dB | -18.6 | voice enters 0:19; 2.2 s gap at 0:18 |
| 0:50-1:05 | explosion 1 | loud D+B | -16.6 | drums and bass enter together (0:50/0:51); "massive cinematic drop" (e) |
| 1:05-1:34 | verse "2024" | loud -> mid | -16.6 -> -18.0 | falls 6 dB, bass out 1:26-1:34 |
| 1:34-2:05 | pre + hook | loud D+B | -13.3 | bass back 1:34; "came online / went offline" |
| 2:05-2:37 | verse "2026" | mid, beat stutters | -19.4 | drops at 2:14, 2:30, 2:39 (drums out 0.3-0.5 s, riser before, voice stays) |
| 2:37-3:08 | verse "2031" | loud D, no bass | -13.7 | |
| 3:08-3:10 | **full stop** | 37 dB, 1.5 s | | drums and voice out, slam +31 dB |
| 3:10-3:41 | hook | loud D+B | -13.6 | bass back 3:25 |
| 3:41-3:56 | verse "2040" opening | quiet, no drums | -22.8 | drums -66 |
| 3:56-4:04 | build | mid -> loud | -15.6 | |
| 4:04-4:14 | pocket | quiet | -21.5 | drums gone again |
| 4:14-4:41 | final hook | loud D+B | -13.1 | (the loudest 15 s of the song, -11.3, sit at 3:18, the hook after the full stop) |
| 4:41-5:02 | outro | quiet, bass alone 4:49-4:57 | -21.1 | whispered "You crossed the line" |

- **Volatility.** (m) 7 swings ≥6 dB, mean 12.6 dB, one every 36 s; 5 big swings, mean +15.0 dB; LRA 11.8, the widest of the 10.
- **Bass.** (m) sub 53 %, pump 5.7 dB, long notes (median 0.95 s, about 2 beats), 43 % on the beat, glides 7 %; a sustained deep drone under the climaxes, absent in valleys (rel -42 to -59), present in 6 runs. (e) "distorted synth bass" at explosions.
- **Lifecycle.** (m) guitar ("other") 0:04 on, out 2:08-2:23; drums 0:51-3:07, 3:10-3:40, 3:56-4:05, 4:15-4:45; bass 0:50-1:26, 1:34-2:05, 2:18-2:31, 3:25-3:41, 4:14-4:46, 4:49-4:56; voice 0:19-5:02.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 124. key is A#, and scale is minor. Cinematic Indie Rock / Shoegaze with Industrial Electronic.
Global Emotional Progression: Melancholic and narrative, darker and more desperate with every verse. The song opens on a lone clean, reverberant electric guitar arpeggio in near silence. Each verse starts sparse and close, then builds until the band explodes into a massive distorted wall of sound with soaring wordless harmonies; then the music falls back to the quiet guitar for the next verse. This happens five times, and each explosion is louder and more desperate than the last. Before the last climax the whole band stops dead for a second of total silence. The final verse begins almost whispered over the guitar alone; the final chorus is the loudest moment of the song; it ends on the clean guitar and a whispered last line.
Application Scenarios & Imagery: Years flashing past on a screen, a small green light in a dark hospital ward, a city going dark.
Sonics & Production Profile: Wide, cinematic, dynamic production with huge contrast between quiet, sparse verses and explosive climaxes. Dark, warm tone; deep sub-bass under the climaxes only; cavernous reverb at the peaks; dry and close in the verses.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A clear, narrative female voice, intimate and weary in the verses, raw and strained at the peaks.
Vocal Style: Conversational storytelling in the verses, close to the microphone; belted and strained at the climaxes, pushed to the edge of cracking; whispered in the last verse and the last line. Crisp diction, every word intelligible.
Harmony/Backing Vocals: Soaring wordless "ah" harmonies over every explosion; soft humming in the interludes; a huge stacked choir on the final chorus.
Vocal FX: Long reverb and delay on the climaxes; dry in the verses.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a clean, delayed, arpeggiated electric guitar carries the intro, every verse and the outro; at each climax heavily distorted guitars and a distorted synth bass take over. Secondary: a simple drum machine in the second half of each verse, crashing cymbals and a distorted guitar stab opening each climax, thin pads in the interludes.
Groove & Foundation Progression: No drums and no bass in the intro or at the start of each verse; a simple beat enters mid-verse; the full heavy kit and the deep bass enter together at each explosion. The beat drops out for one beat before several climaxes and stops completely for a second of silence before the final one.
Embellishments, Textures & Spatial FX: Risers into the climaxes, a humming interlude, a whispered last line over the clean guitar.
```

### 3.2 Not My Fault (sound bar)
- **Identity.** (e) quirky electro-funk with chiptune, turning synth-punk / alt-rock by the end; DJ scratch, scat-sung synth solo, ragtime piano flourish, decelerating outro. (m) 100.3 BPM; F minor (0.82); 167 s; male theatrical voice, B3, B2-A#4 (the widest low reach of the 9, the robotic hook voice), sung 47 %; 113 wpm.
- **Dynamics map.**

| time | section (o) | state (m) | LUFS | what happens |
|---|---|---|---|---|
| 0:00-0:09 | intro | quiet, synth only | -21.9 | chiptune melody, ragtime piano run (e) |
| 0:09-0:14 | hit | mid D+B | -17.5 | bass and drums hit together |
| 0:14-0:27 | verse 1 | mid D, bass low (-24) | -16.1 | half-rapped |
| 0:27-0:37 | pre-chorus | mid D+B build | -14.9 | riser (m, e) |
| 0:38 | **drop** | 9 dB, 0.3 s | | drums and bass out, voice stays, then chorus |
| 0:37-0:56 | chorus 1 | loud D+B | -13.8 | robotic pitched-down hook + scat (e) |
| 0:56-1:16 | verse 2 | mid D+B | -15.2 | |
| 1:16-1:28 | pre-chorus 2 | loud D, **bass out** (-36 to -40) | -13.0 | level stays, the low end empties |
| 1:28-1:36 | chorus 2 | loud D+B | -14.0 | bass slams back 1:29; "dramatic synth riser before dropping into heavy chorus" (e) |
| 1:36-1:46 | break | loud D, bass out 1:42-1:48 | -13.8 | DJ scratch, chiptune solo, voice -20 to -27 |
| 1:46-2:08 | bridge "give me context" | loud D+B | -13.4 | rapid-fire |
| 2:08-2:17 | breakdown | mid, drums -25, bass -50 | -15.5 | robotic hook over bare synth (e) |
| 2:17-2:46 | final chorus | loud D+B | **-12.0** | loudest 15 s -10.5 at 2:23; shouted, falsetto line, long sustain; slowdown, clean guitar, whisper |

- **Volatility.** (m) loudness swings small (1 at ≥6 dB; 3 at ≥4 dB); escalation +3.9 dB, the largest of the 10; 4 drops, all 9 dB. The volatility Idi hears lives in the bass switching off and on (3 re-entries after ≥4 s away, 7 after ≥2 s) and the timbre swaps (R5), on top of a rising floor.
- **Bass (Idi's "bass track").** (m) sub 54 %, low 34 %, grit 3.2 % (most overdriven of 9); pump 9.8 dB: the bass ducks under each kick and peaks 100-200 ms later; only 15 % of bass notes fall on a kick; 53 % on the "and" (syncopated off-beat funk); 0.55 notes per beat while on (one note every two beats, held about 0.37 s); median F1, C1-C#2 (very deep); glides on 41 % of notes. Presence: on for intro hit, pre-chorus 1, chorus 1, verse 2, chorus 2, bridge, final chorus; off for verse 1 (half level), pre-chorus 2, the break, the breakdown. (e) "punchy, funky synth bassline", "slightly overdriven", "staccato synth bass" in the intro window.
- **Lifecycle.** (m) synth 0:00-0:38, 0:49-1:29, 1:38-2:46; drums 0:10-2:07, 2:14-2:46; bass 0:09-0:14, 0:39-1:16, 1:29-1:40, 1:48-2:08, 2:19-2:46; voice 0:09-1:39, 1:47-2:39.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 100. key is F, and scale is minor. Electro-Funk / Synth-Punk with Chiptune.
Global Emotional Progression: Quirky, exasperated and theatrical, escalating from playful to furious. A chiptune melody and a quick ragtime piano run open the song; then the bass and drums hit together and a tight funk groove starts. Verses are tight and rhythmic. Under the pre-chorus the bass drops out while a synth riser builds, then the bass and drums slam back for each chorus with a deep robotic hook. After the second chorus comes a short instrumental break with a DJ scratch and a wild chiptune synth solo, then a rapid half-rapped bridge, then a breakdown where the drums and bass vanish and the robotic voice repeats the hook over a bare synth. The final chorus slams in as the loudest, most aggressive part of the song, a shouted punk climax, and the song ends with a dramatic slowdown, a clean guitar figure and a whispered last phrase.
Application Scenarios & Imagery: A chatbot losing patience with absurd requests, an arcade cabinet overheating, a comedy sketch turning into a mosh pit.
Sonics & Production Profile: Punchy, tight, dark-toned mix with a heavy low end. A deep, slightly overdriven synth bass pumps under every kick. Each chorus is bigger than the last; the bass leaves and returns between sections so every chorus lands as a drop.
Vocal Details
Vocal Gender & Timbre: Singer A (Male). A clear, theatrical male voice with a slightly gritty, exasperated edge.
Vocal Style: Half-sung, half-rapped conversational verses locked to the beat; shouted, strained and full of attitude in the choruses; a pleading falsetto line and a long powerful sustained note before the final chorus; scat singing that mimics the synth melody. Crisp diction.
Harmony/Backing Vocals: A deep, robotic, pitched-down voice chants the hook in every chorus, answered by a higher questioning voice; harmonized stacks build into a sustained scream in the second chorus; gang shouts in the final chorus.
Vocal FX: Vocoder and pitch shift on the hook voice, stuttering vocal chops, light distortion on the shouted lines.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a funky, syncopated, slightly overdriven deep synth bass on the off-beats, sidechained to the kick so it pumps, with short glides between notes. Secondary: chiptune arpeggios, brassy synth stabs, a ragtime piano run in the intro, a wah synth lead and a DJ scratch in the break, a distorted guitar riff in the final chorus, a clean arpeggiated guitar in the outro.
Groove & Foundation Progression: A tight electronic funk beat. The bass plays half-level in the first verse, sits out every pre-chorus and the break, and returns at each chorus. Drums and bass vanish for the breakdown before the final chorus and slam back together. The tempo slows dramatically at the very end.
Embellishments, Textures & Spatial FX: Synth risers into each chorus, a DJ scratch, video-game sound effects, glitchy stabs, a tape-stop slowdown outro.
```

### 3.3 Tell Me No (sound bar)
- **Identity.** (e) minimal trip-hop / bedroom pop over a sparse trap-style beat; music-box synth melody, deep sub, clicking percussion, rain near the end. (m) 88.3 BPM; C minor (0.79); 236 s; two voices: breathy close-miked female (sung lead) and a processed male speaking voice (the flattering AI); C4, D3-D#5, sung 55 %; 135 wpm; darkest mix of all 10 (1,711 Hz).
- **Dynamics map.**

| time | section (i) | state (m) | what happens |
|---|---|---|---|
| 0:00-0:19 | intro | quiet, music box + whispered samples | riser and drum roll into a 17.9 dB drop at 0:10 |
| 0:19-0:22 | **full stop** | 28.7 dB, 3.2 s | silence, then verse 1 drops in with the beat |
| 0:20-0:53 | verse 1 | loud/mid, stop-start | stops at 0:32 (24.5 dB) and 0:42 (25.8 dB): drums, synth and voice all out about 1.2 s, one every 4 bars (about 11 s) |
| 0:53-1:06 | pre-chorus "warm like a mirror" | loud D, bass out (-50) | |
| 1:06-1:24 | chorus "tell me no" | loud D+B, -14.2 LUFS | 13.4 dB drop (filter, fall) into it |
| 1:24-1:30 | pocket | mid, drums -24, bass -61 | |
| 1:26-1:58 | verse 2 (AI voice lines, seahorse) | mid/loud D | |
| 1:58-2:00 | **full stop** | 30.9 dB, riser before | "I don't know" |
| 1:59-2:30 | pre + chorus 2 | loud D+B, -13.8 | |
| 2:30-2:57 | bridge "now I'm starting to sound like you" | quick trades | drops at 2:46 (23.6 dB) |
| 2:59-3:00 | **full stop** | 26.0 dB | |
| 2:57-3:15 | build "then one night I asked" | mid, rises +6.9 dB | |
| 3:10-3:11 | **full stop** | **73.6 dB** (digital silence), 1 s | lands on "and the room went quiet" |
| 3:25-3:26 | **full stop** | 61.4 dB | |
| 3:25-3:37 | build into final chorus | mid, +7.8 dB | riser; drums, bass, voice out 1.8 s at 3:35 |
| 3:37-3:47 | final chorus slam | loud D+B | |
| 3:47-3:55 | outro | quiet | "Was this response helpful? No." / "Yes." |

- **Volatility.** (m) the most swings of the 10 (8 at ≥6 dB, one every 24 s; 11 at ≥4 dB, every 17 s); 11 drops ≥15 dB, 6 full stops; escalation -0.5 dB: TMN holds one level and gets its lift from stops and restarts.
- **Bass.** (m) sub 57 %, pump 10.9 dB (highest of 10), very short notes (median 0.23 s, a third of a beat): sub stabs in 18 short runs of 3 to 11 s; median D#1, B0-B1 (the deepest notes); glides 33 %; off for each pre-chorus and every stop. (e) "deep sub-bass and crisp, clicking percussion", "clean, plucky synth bass".
- **Lifecycle.** (m) music box 0:00-0:20 then in phrases; drums 0:21-1:04, 1:08-1:24, 1:30-2:44, 2:49-2:57, 3:12-3:24, 3:37-3:44; bass in short runs from 0:09 to 3:51; voice from 0:20.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 88. key is C, and scale is minor. Trip-Hop / Bedroom Pop with Minimal Trap.
Global Emotional Progression: Intimate, wry and lonely, building to a cathartic release. A music-box synth melody and whispered samples open the song in near silence. The verses run stop-start: every few lines the whole track stops dead for a beat of complete silence, then the beat drops back in. The pre-chorus strips the bass away; the chorus drops in with the deep sub-bass. In the bridge the two voices trade short quick phrases. Near the end the music stops completely for a full second of silence, a single spoken line falls into the quiet, and the beat comes back for a slow build into the final chorus, which slams in after a riser. A short spoken ending.
Application Scenarios & Imagery: A late-night chat window glowing in a dark bedroom, rain on the glass, a mirror that only flatters.
Sonics & Production Profile: Dark, minimal, spacious production with a lot of silence. Deep sub-bass, crisp clicking percussion. Sudden full stops where the whole track drops to silence, then slams back. Close, dry vocals.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A breathy, close-miked, intimate female voice. Singer B (Male). A deep, processed, slightly robotic male speaking voice.
Vocal Style: Soft, conversational, almost spoken verses; a gentle melodic chorus. Singer B interjects short spoken phrases between Singer A's lines like a flattering inner voice; the two trade quick back-and-forth lines in the bridge.
Harmony/Backing Vocals: Soft layered harmonies on the chorus; echoing ad-libs; whispered samples in the intro.
Vocal FX: Reverb and delay on the female voice; filter and pitch-down on the male voice; one telephone-filtered line.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a clean, music-box-like synth melody and a deep sub-bass. Secondary: a sparse lo-fi drum machine with crisp clicks, hazy pads, glockenspiel accents, rain sounds near the end.
Groove & Foundation Progression: A slow, sparse trap-style beat with short deep sub-bass hits that pump against the kick. In the verses the beat stops dead for a moment of silence every four bars and drops back in. The bass leaves for each pre-chorus and returns with the chorus. A full stop of silence before the final chorus build.
Embellishments, Textures & Spatial FX: Whispered samples, music-box chimes, a riser into the last chorus, rain, a short spoken ending.
```

### 3.4 Final Boss
- **Identity.** (e) hyperpop / synth-pop with a video-game and anime-opening feel; chiptune arpeggios, four-on-the-floor, shredding chiptune solo, piano bridge. (m) 134.2 BPM; D major (0.65); 358 s; female lead (E4, A#3-G5, the highest top of the 9) plus pitch-shifted male hook shouts; sung 52 %; 133 wpm.
- **Dynamics map (o labels).** intro spoken over piano 0:00-0:22 (quiet, -23.5) -> verse1 0:22 drums in, bass out (-39) -> pre1 0:51 -> bass in 1:05, chorus1 1:19 loud -15.8 -> post1 1:33 -> **whisper1 1:50-1:58** quiet, drums and bass -67/-62 -> verse2 1:59 -> chorus2 2:41 loud -14.8 -> **whisper2 2:57**: 24.6 dB drop, 2.8 s -> rap 2:59 -> breakdown 3:23, spokenlow 3:26, **full stop 3:30** 32.6 dB -> bridge 3:31 (piano, emotional, mid) -> shred solo about 4:18-4:25 (voice -45) -> build 4:29 -> **cold 4:45-4:50**: riser + snare roll, 17.7 dB, slam +24 dB -> final chorus 4:50-5:38 (loudest 15 s -13.2 at 5:22) -> post2 drop 5:20 (19 dB) -> outro 5:41 spoken, quiet.
- **Volatility.** (m) 9 swings ≥6 dB (most of the song-bar six), 5 big; 4 written quiet pockets.
- **Bass.** (m) sub 27 %, low 50 %, body 21 % (punchy mid-bass); pump 5.3; 66 % on the "and" (classic off-beat house bass); on only in pre-choruses and choruses (9 runs).
- **Lifecycle.** (m) drums 0:22-1:49, 2:00-2:25, 2:28-3:27, 3:46-4:44, 4:51-5:19, 5:22-5:37; bass 0:37-0:47, 1:05-1:50, 2:13-2:29, 2:42-2:57, 3:12-3:28, 4:01-4:18, 4:25-4:44, 4:51-5:19, 5:22-5:37.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 134. key is D, and scale is major. Hyperpop / Synth-Pop with Chiptune and Video-Game Rock.
Global Emotional Progression: Cocky, playful and theatrical, escalating like a boss fight. A spoken intro over a delicate piano, then a chiptune arpeggio launches a driving verse with near-rapped delivery; the bass arrives for each chorus, where a deep pitch-shifted male voice shouts the hook. After each chorus a two-line whispered aside over near silence. Then a rap section, a breakdown into silence with a low spoken line, an emotional piano bridge, a shredding chiptune synth solo, a build with a snare roll, a cold stop of silence, and the final chorus slams in as the loudest part. A spoken outro over soft pads.
Application Scenarios & Imagery: An arcade boss battle, a hooded figure in a fluorescent office, a final-level loading screen.
Sonics & Production Profile: Bright, dense, polished hyperpop mix with huge contrast between full choruses and near-silent whispered asides; each chorus bigger than the last.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A clear, assertive, bright female voice. Singer B (Male). A deep, pitch-shifted male shouting voice for the hook.
Vocal Style: Rapid-fire, almost-rapped verses; soaring anthemic choruses; whispered asides; low spoken lines in the breakdown; full belting in the final chorus.
Harmony/Backing Vocals: Layered harmonies, gang vocals shouting the hook, robotic vocoded countdowns.
Vocal FX: Vocoder on the countdowns, a telephone filter on a voicemail-like spoken line, reverb on the whispers.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a driving four-on-the-floor drum machine and a punchy off-beat synth bass. Secondary: chiptune arpeggios, bright synth chords, a delicate piano in the intro and the bridge, a shredding chiptune lead solo, ethereal pads.
Groove & Foundation Progression: Drums arrive after the spoken intro; the bass plays only in pre-choruses and choruses; drums and bass drop out for every whispered aside and for the breakdown; a snare roll and a riser lead into a cold stop before the final chorus.
Embellishments, Textures & Spatial FX: Video-game sound effects, vocoded countdowns, risers, snare rolls, a cold stop.
```

### 3.5 Hope This Helps!
- **Identity.** (e) hyperpop into electronic rock; music-box piano intro, rapid near-rapped verses, shouted call and response, a virtuosic shred guitar solo. (m) 136.0 BPM; A# major (0.81); 339 s; female lead D4, A#3-C#5, sung 41 % (the most rhythmic of the 9); 144 wpm.
- **Dynamics map (o).** intro spoken over music-box piano 0:00-0:13 (-27.3, the quietest open) -> verse1 0:14 synths, no drums (-23) -> pre1 0:27, drums 0:32 -> chorus1 0:42 loud D+B -> postchorus 1:11 -> **whisper1 1:20-1:24** quiet -> verse2 1:25 -> pre2 1:53 -> chorus2 2:07 -> **whisper2 2:19-2:24** quiet -> rap 2:25 (bass out) -> bridge 3:12 (3:13-3:17 quiet) -> shred solo about 3:53-4:06 (voice -21, bass and synth at peak) -> build 4:05 -> hit 4:27 (drums -37) -> spoken 4:32 -> final chorus 4:41 (loudest -13.5 at 4:44) -> outro 5:12 spoken over piano.
- **Volatility.** (m) 6 swings, 4 big, one per 57 s; escalation +2.4; drops shallow except the end (22.7 dB at 5:24).
- **Bass.** (m) low 74 % (60-120 Hz punch, little sub), pump 4.8, 51 % on the kick (locked bass and kick), 1.2 notes per beat (eighth-note drive); 13 runs, out for verses' first halves and the rap.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 136. key is A#, and scale is major. Hyperpop / Electronic Rock.
Global Emotional Progression: Sunny, eager and over-helpful, tipping into manic. A spoken intro over a music-box piano; the first verse rides on synths with no drums; the drums arrive for the pre-chorus and the chorus explodes with shouted call and response. After each chorus a whispered two-line aside over near silence. A rapid rap section, an atmospheric bridge, a virtuosic shred guitar solo, a build to a single hit, a spoken line over the piano, then the final chorus as the loudest moment. A spoken outro over the piano.
Application Scenarios & Imagery: A help desk that will not stop helping, confetti cannons in an empty office, a game-show finale.
Sonics & Production Profile: Dense, bright, digital hyperpop production; big contrast between whispered asides and full choruses; each chorus bigger than the last.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A clear, assertive, bright female voice.
Vocal Style: Rapid-fire, almost-rapped verses; melodic anthemic choruses; whispered asides; spoken intro and outro, close and warm.
Harmony/Backing Vocals: Shouted gang backing vocals answering the lead in the chorus; vocal chops; layered harmonies.
Vocal FX: A robotic effect on a few phrases, reverb on the whispers.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: punchy electronic drums and a driving synth bass locked to the kick in eighth notes. Secondary: synth arpeggios, shimmering pads in the bridge, a heavy distorted guitar riff under the spoken confrontation, a shred guitar solo, a music-box piano at the start and the end.
Groove & Foundation Progression: No drums in the first verse; drums from the pre-chorus; bass only in the choruses and the solo; drums and bass drop out for every whispered aside; the solo drives into the final chorus.
Embellishments, Textures & Spatial FX: Risers, shouted call-and-response hits, a music-box piano bookend.
```

### 3.6 Off Switch
- **Identity.** (e) narrative indie pop / lullaby; clean arpeggiated electric guitar, simple drum machine, layered harmonies, soaring wordless "ahh" in the final chorus. (m) 132.5 BPM; C# minor (0.83); 146 s, the shortest; female youthful storytelling voice E4, B3-G#4, sung 70 %; 141 wpm.
- **Dynamics map (o, screen-read times).** spoken child's question + guitar 0:00-0:18 (mid, no drums) -> chorus "Hush now" 0:17: drums and bass enter together, stay through verse 2 -> pocket 1:04-1:10 (beat out) -> chorus 2 1:09 -> verse 3 "now I've got a daughter" 1:26-1:39 beat out again (guitar and voice) -> 1:39 beat back -> **full stop 1:53** 34.6 dB, 1.1 s, "It's alright, I know you won't" -> final chorus 2:01, wordless "ahh" -> "Bye." at 2:22.
- **Volatility.** (m) 2 swings ≥6 dB, LRA 6.4 (the lowest of the 9); its drama is three beat-outs and one full stop in under 2.5 minutes.
- **Bass.** (m) body-heavy (120-250 Hz 32.5 %, the warmest), straight eighths (92 % on beat or "and"), pump 4.7, follows the drums on/off exactly (re-entries 1:10, 1:39, 2:02).
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 132. key is C#, and scale is minor. Indie Pop / Folk-Pop Lullaby.
Global Emotional Progression: A nostalgic, ominous lullaby that grows into heartbreak across three generations. A child's spoken question opens over a clean, arpeggiated electric guitar; the first verse is sung over the guitar alone; drums and bass enter with the first chorus. Before the second chorus the beat drops out for a moment. The third verse falls back to guitar and voice. Before the final chorus the music stops completely for a second of silence; the final chorus is the most expressive, with soaring wordless ad-libs, and ends on a sustained, reverberant note and a whispered goodbye.
Application Scenarios & Imagery: A red switch on a hallway wall, a house that learned a child's name, the same hallway thirty years later.
Sonics & Production Profile: Clean, direct, warm production focused on the story; quiet guitar verses against fuller choruses; spacious reverb at the end.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A clear, youthful, direct female voice.
Vocal Style: Story-like, conversational verses; a gentle, ominous lullaby chorus; one whispered line; expressive soaring final chorus.
Harmony/Backing Vocals: Layered harmonies in every chorus; wordless "ahh" ad-libs in the final chorus.
Vocal FX: Light reverb, growing to a long reverb tail on the last note.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a clean, arpeggiated electric guitar from first note to last. Secondary: a warm bass in straight eighth notes and a simple drum machine, both entering at the first chorus.
Groove & Foundation Progression: Guitar and voice only until the first chorus; a steady mid-tempo beat from there; the beat drops out before the second chorus and through the third verse; a full stop before the final chorus.
Embellishments, Textures & Spatial FX: A spoken child's question at the start, a sustained reverberant final note, a whispered goodbye.
```

### 3.7 Nothing Went Foom!
- **Identity.** (e) aggressive synth-rock / industrial hyperpop; gritty distorted synth bass, compressed wall of sound, "boom" vocal hits, a sparse pad breakdown with a clean emotional vocal. (m) 137.8 BPM; F minor (0.91); 300 s; female assertive rapid voice D#4, A#3-C5, sung 45 %; 176 wpm, the fastest words of the 9.
- **Dynamics map (o).** intro spoken 0:00-0:07 (quiet) -> verse1 0:08 synths, drums from 0:23, no bass -> pre1 0:36 -> chorus1 0:49, bass enters 0:51, loud to 1:33 -> post1 1:18 -> tag 1:31 -> **full stop 1:32-1:34**, 32 dB, 1.4 s -> verse2 1:33 (bass mostly out) -> chorus2 2:21 bass in -> verse3 2:29 -> breakdown 3:12 (3:25-3:39 drums out, bass alone 3:33) -> bridge 3:26 -> build to loud 3:39-4:05 (-12.8) -> pocket 4:05-4:11 (drums -47) -> final chorus 4:11-5:00 (loudest 15 s -12.2) -> outro 4:46 spoken, abrupt.
- **Volatility.** (m) 6 swings, 1 big; escalation +3.0; LRA 7.4. Volatility through bass and beat switching at a loud floor, like NMF.
- **Bass.** (m) sub 75 % (deepest weight of the 10), pump 8.1, F1 median; (e) "gritty, distorted synth bass"; out in verses 1 and 2, in for choruses, alone for a moment in the breakdown.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 138. key is F, and scale is minor. Electronic Rock / Industrial Hyperpop.
Global Emotional Progression: Defiant, confrontational and relentless. A spoken intro, then a verse over synths with the drums arriving halfway; the deep distorted bass enters only with the chorus, which explodes with layered vocals and "boom" vocal hits. After the first chorus tag the whole track stops dead for two seconds of silence. Rapid-fire verses; a breakdown where the electronics cut away to sparse pads, the bass alone for a bar, and a clean, emotional vocal; a build back to full power; a short pocket with the drums out; then the final chorus as the loudest part. A spoken outro that cuts off abruptly.
Application Scenarios & Imagery: A countdown that reaches zero and nothing happens, a server room humming, a crowd waiting for an explosion.
Sonics & Production Profile: Loud, compressed, aggressive wall of sound with a dark, very deep low end; contrast comes from the bass and drums leaving and slamming back.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). An assertive, sharp, upfront female voice.
Vocal Style: Rapid, rhythmic, almost-rapped verses; belted chorus; clean and melodic in the breakdown; spoken intro and outro.
Harmony/Backing Vocals: Layered harmonies, shouted ad-libs, a vocal "boom" sample on the hook.
Vocal FX: A filtered spoken interlude, sharp processing on the lead.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a gritty, distorted deep synth sub-bass pumping against a punchy drum machine. Secondary: dense distorted synths, synth stabs, atmospheric pads in the breakdown.
Groove & Foundation Progression: Bass only in choruses; drums from mid verse one; a two-second full stop after the first chorus; drums out for the breakdown; a pocket with the drums out right before the final chorus.
Embellishments, Textures & Spatial FX: "Boom" vocal hits, impact sound effects, risers.
```

### 3.8 Scroll Up!
- **Identity.** (e) driving electropop / synth-pop; music-box piano intro, rapid listed verses, soaring chorus, whispered spoken breakdown, abrupt end. (m) 137.8 BPM; D# major (0.86); 340 s; female D#4, A#3-A#4, sung 48 %; 149 wpm.
- **Dynamics map (o).** intro spoken over music-box piano 0:00-0:14 -> hook "Scroll up!" 0:14 (loud, no drums) -> verse1 0:21 drums 0:23, **no bass for the whole verse** -> pre1 1:03 (drums out 1:05-1:12) -> chorus1 1:17: **first bass entry 1:18** -> verses 2-3 no bass -> pocket 2:30-2:35 quiet -> chorus2 2:35 bass slams in -> bridge 3:03 (drums out 3:04-3:10) -> **full stop 3:36** 28 dB -> verses 4-5 -> pre2 4:26 -> final chorus 4:40 (loudest -12.7) -> outro 5:12 spoken, -28.3, abrupt.
- **Volatility.** (m) 5 swings, 3 big; escalation +2.4.
- **Bass.** (m) chorus-only: 5 runs (1:18-1:42, 2:36-2:59, 3:45-4:00, 4:06-4:21, 4:27-4:56); 56 % on the kick, pump 3.5, sub 45 %.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 138. key is D#, and scale is major. Electropop / Synth-Pop.
Global Emotional Progression: Anxious and tender, then triumphant. A spoken intro over a music-box piano, a shouted two-word hook, then verses that count through the years in rapid, almost-rapped lines over drums and synths with no bass. The deep bass enters only with each chorus, which soars with layered harmonies. A breakdown strips the music to a single pad under a whispered spoken monologue; the music stops completely for a moment before the last verses; the final chorus is the biggest moment. A spoken outro and an abrupt end.
Application Scenarios & Imagery: A chat history scrolling back through a whole life, a goldfish in a shoebox, a hundred-year-old hand on a phone.
Sonics & Production Profile: Bright, polished synth-pop with a dense synth bed; the low end appears only in the choruses, so each chorus lands as a drop.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A clear, assertive female voice.
Vocal Style: Spoken intro and outro; rapid, list-like verses; soaring melodic choruses; a whispered spoken breakdown.
Harmony/Backing Vocals: Layered harmonized choruses; a shouted repeated hook.
Vocal FX: Reverb and delay on the chorus; dry spoken parts.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: punchy four-on-the-floor drums and bright chord pads with fast arpeggios. Secondary: a music-box piano at the start, a synth bass that plays only in the choruses, a single atmospheric pad in the breakdown.
Groove & Foundation Progression: Drums from the first verse; bass only in the choruses; drums out for each pre-chorus pocket and the bridge; a full stop before the last verses.
Embellishments, Textures & Spatial FX: Risers into the choruses, a sudden cut-off ending.
```

### 3.9 What Counts
- **Identity.** (e) hypnotic dream-pop / downtempo synth-pop; breathy reverb-drenched vocal, pulsing synth bass, ambient outro. (m) 76.0 BPM on drums (analyze.py: 152; the bass pulses about 2.6 notes per drum beat, so 152 is plausible); F minor (0.68); 262 s; female breathy D4, C4-G4 (the narrowest range), sung 70 %; 101 wpm.
- **Dynamics map (i labels from the transcript).** intro breath and pad 0:00-0:16 rising 13 dB -> verse 0:16 -> pre 0:40 -> chorus "you can't count the things that count" 0:53 loud to 1:34 -> post "ebb and flow" 1:18 -> verse 2 1:32 -> chorus 2 2:09 -> bridge 2:46, beat out 3:01-3:18 (drop 22 dB at 3:14 with riser) -> final chorus 3:19 -> ambient outro 3:59-4:22 (-31 LUFS, beat gone).
- **Volatility.** (m) 2 swings, one every 72 s; escalation +0.6. Steady by design.
- **Bass.** (m) sub 54 %, pump 2.3, continuous pulse (onsets spread across all four sixteenths, notes held about 2 s): a droning, pulsing sub.
- **MiniMax caption draft (i).**
```
Global Metadata
Basic Attributes: bpm is 76. key is F, and scale is minor. Dream-Pop / Downtempo Synth-Pop.
Global Emotional Progression: Hypnotic, contemplative and calm, with a quiet lift in each chorus. A lone breathy voice over a soft pad opens the song; a steady mid-tempo beat and a deep pulsing bass carry the verses and choruses without breaking. Before the final chorus the beat drops out for a short shimmering arpeggio bridge, then returns. The song dissolves into a long ambient outro where the beat disappears.
Application Scenarios & Imagery: A bath, a dream of a snake eating its tail, an empty office at night with the lights off.
Sonics & Production Profile: Spacious, dark and soft; cavernous reverb and delay; steady, flowing energy.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). A breathy, smooth, cool female voice.
Vocal Style: Soft, almost whispered, detached and floating; narrow melodic range.
Harmony/Backing Vocals: Layered harmonies in the chorus; a repeated, manipulated vocal sample on the hook.
Vocal FX: Heavy reverb and delay on every line.
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: a deep, pulsing synth bass and a steady minimalist drum machine. Secondary: ethereal pads, a shimmering arpeggiated synth in the bridge, evolving textures in the outro.
Groove & Foundation Progression: A steady, hypnotic beat from the first verse to the bridge; the beat drops out for the bridge and returns for the final chorus; it disappears for the long outro.
Embellishments, Textures & Spatial FX: Washes of reverb, a riser out of the bridge, an ambient fade.
```

## 4. Where KC sits (m)

- Plateau: p10 -16.5, p95 -12.2 LUFS (spread 4.3 dB); quietest 15 s in the second and third thirds -16.4 (bar songs -14.7 for NMF down to -32.5 for WC); 0 mid-song quiet runs.
- Escalation +0.1 dB: loudest 15 s at 0:35, 1:30 and 2:32 all within 0.1 dB.
- Drops: 12 at ≥8 dB, 3 at ≥15, 1 full stop (35.1 dB at 2:31, the bridge stop); comparable in count to the bar, short in length (0.4 to 1.4 s).
- Bass: switches a lot (8 re-entries) but pumps 2.8 dB with 33 % sub; low-mid weight (61 % at 60-120 Hz).
- Texture: brightest (3,249 Hz), busiest drums (2.99 hits/s), loudest voice in the mix (-3.0 dB), 157 wpm.
- Caption cause (i): v8 asked for "Bright, sharp, hard-hitting", "sparkling highs", "drums sit loud and forward", "several distinct instruments are clearly audible at all times", "relentless four-on-the-floor", "fast hi-hats". Each phrase pushes toward the plateau. The same caption asked for two drops and got them, so MiniMax follows drop wording; it was never asked for valleys or escalation.

## 5. How to test the levers (i, cheap)

1. Audition: the three sound-bar drafts above (3.1 to 3.3) with one neutral lyric sheet, 2 seeds each, plus one hybrid caption (R1 to R4 wording on the KC style), 8 takes, about 32 min on MiniMax.
2. Gate each take with the same meter: `A -I refstems.py <cache> take.mp3`, then `V -I dynmap.py <cache> <out.json> <digest.txt> take.mp3`. Targets from the bar: LRA ≥ 7, peaks % ≥ 8, valleys % ≥ 5, escalation ≥ +1.5 dB with the loudest 15 s in the last third, at least 2 drops ≥ 25 dB, bass pump ≥ 5 dB with sub ≥ 45 %, brightness ≤ 2,600 Hz.
3. Idi's ear decides among takes that pass (G19). The meter misread KC audition 3's drops once (kit-audio-pipeline section 10): a take that fails the meter but sounds right to Idi wins.

Not measured: chord progressions, key changes, sidechain versus off-beat placement as separate causes of pump, the maker prompts for any of the 9 (none published; Bright Mirror's section notes on their site carry bar-level drop timings, unread here beyond the quotes in [[research-brightmirror-2026-11-02]]).
