---
type: project
created: 2026-11-02
author: jep
---

# Audio pipeline: how the Knowledge Cutoff song was made

Scope: the song pipeline as used for Knowledge Cutoff (KC), from engine trials to the word-timing files the video ran on. Every fact carries its source file. Paths: lab = `D:\work\aimv-lab\`, vault notes = `D:\work\vault\projects\AIMV\`.

Source keys:
- `SE` = `song-engine-research-2026-10-13.md` (ACE-Step knobs, repairs, MiniMax crashes and first takes)
- `PV4` = `knowledge-cutoff-prompt-v4-2026-10-14.md` (MiniMax caption format, F1-F6, knobs K1-K10)
- `AU` = `knowledge-cutoff-auditions-2026-10-14.md` (9 style auditions, v5-v9, the v8B ruling)
- `RSM` = lab `research-song-models.md`; `RR` = `D:\work\AIMVs\ours\release\research\rights-rules.md`
- `G` = `aimv-guidelines.md` (G19-G25 are the audio rules); `VTP` = lab `research-video-tech-plan.md` (sync measurements)
- `H14` = `handoff-2026-10-14.md`; `H17` = `handoff-2026-10-17-full-video.md`

## 1. Song of record

| fact | value | source |
|---|---|---|
| take | MiniMax Music 3, take v8B, seed 3327, lyric file `kc\lyrics-mm-p8b.txt`, caption `kc\caption-minimax-v8.txt` | `AU` v8 ruling; lab `kc\mm-v8.sh` |
| length | generated 240 s, cut at 192.6 s (47.4 s of invented filler removed); plus Idi's 1.5 s silent tail; "no audio edits" | lab `kc\mm-v8.log` line 71; `H17` line 24 |
| screen scores | words heard 98.6 %; refrain 6/6; intro 2/2; outro 3/3; 157 words/min; drops 11, 11, 35 dB; holds "turn" 2.4 s / 2.0 s | `kc\mm-v8.log` lines 83, 95, 107 |
| Idi's verdict | "a BANGER", "the best one yet"; emergent backing voice humming only in the final chorus; one flaw kept ("that's family news" off the beat): "I won't throw out more than 3 minutes of gold over less than 3 seconds of slop." | `AU` v8 ruling |
| file identity | `kc-engine\audio\kc.mp3` md5 = `kc\final\v8B-3327.mp3` md5 (`73bfc2e3...`): byte-identical; no Suno audio anywhere | `RR` section 2 |

## 2. Models tried, with outcomes

| engine | how run | best result | outcome | source |
|---|---|---|---|---|
| ACE-Step 1.5 turbo + 1.7B planner (AIO) | ComfyUI local API, port 8188, Kid Studio workflow | 40 s proof: 16 takes, ~6 s each; best 82 % words (seed 88, sang "my night stops in June"); chosen seed 11, 77 % | proof shipped 2026-10-13; full takes v1-v3; knob grid found no gain | `knowledge-cutoff-2026-10-13.md` 1; `SE` 2 |
| ACE-Step 1.5 knob grid | 7 settings x 4 seeds, lyrics v3 | defaults 87.5 % avg; diction tags 88.0 % (only gain: outro sung) | "knobs are spent on this model"; lower temperature or higher cfg hurt a lot | `SE` 2 |
| ACE-Step 1.5 turbo + 4B planner | split loaders, `wf_ace4b.json` | 92.1 % avg over 7 takes; 34 s per take; 0 crashes in 8 | take C (seed 906) = Idi's then-gold; repaired to 94.7 % | `SE` 4b, 4d, 4e |
| ACE-Step repaired take C | repaint + splice + balance (section 6) | 94.7 % words, 17 word differences, drop 19.0 dB | Idi: sounds patched, "mostly perfect parts and some least-bad-option parts"; ruling: find a one-shot take | `SE` 4f |
| MiniMax Music 3, first runs | Idi's ComfyUI | 1 take 79.4 %; invented filler past ~2:50 when given 4:00; crashed 2 of 3 runs | parked; cause later found: audio decode out of GPU memory | `SE` 4b, 4c, 4f |
| MiniMax Music 3, jep's ComfyUI | portable v0.39.0 at `C:\Users\jep\comfy`, port 8189, tiled decode `wf_minimax_tiled.json` | 9 takes, 0 crashes; one-shots 93-96 % standard prompt; paced seed 974 97.8 % | engine of record; v4-v9 batches | `SE` 4f; `H14` |
| Suno | not run | YuE2-paper PER 7.58 % (v6) | skipped: free tier v6-mini only, signup, "personal and non-commercial purposes"; earlier Idi rule "no Suno, no cloud" | `RSM` 5; `RR` 2 |
| YuE2 3B; HeartMuLa; LeVo 2; DiffRhythm 2 | not run | PER 8.44 / 10.71 / 26.12 (or 8.55 own) / 18.41 % | skipped (YuE2 non-commercial; others weaker or licence unclear) | `SE` 3; `RSM` 4 |
| Chatterbox 0.1.7 (voice clone, for spoken bookends only) | `C:\Users\jep\tts\venv`, 84 readings | words right 72 of 84 | Idi: all 14 picks "terrible in most aspects"; route closed, no clone, no stitched bookends | `AU` bookends round 2 |

Accuracy column caveat: PER (phoneme error rate) numbers come from one table in the YuE2 paper (WildSongBench), not replicated (`SE` 3).

## 3. Licence facts per model

| model | licence | duties for a public video | source |
|---|---|---|---|
| MiniMax Music 3 (used) | "MiniMax-Music3 COMMUNITY LICENSE", Copyright (c) 2026 MiniMax; ungated HF repo `MiniMaxAI/MiniMax-Music3` | credit text "MiniMax-Music3" (clause 3.1, cheap to comply even if a video is no "product"); revenue over US$20M/yr needs written authorization (3.2); AUP item 11: disclose machine-generated content publicly; item 12: no impersonation; output ownership not addressed; monetised YouTube not restricted | `RR` section 1 |
| Suno (not used) | free tier: outputs for "lawful, personal and non-commercial purposes"; paid tiers assign Suno's rights to the user subject to the terms | none: KC holds no Suno audio | `RR` section 2; `RSM` 5 |
| ACE-Step 1.5 (used for trials, repairs, captioner) | MIT, ungated HF repos | none beyond MIT notices (no ACE audio in the final song) | `SE` 3; `RSM` 1; lab `acestep-docs\README.md` line 295 |
| ACE-Step Captioner (ear for references) | MIT (Qwen2.5-Omni-7B fine-tune) | analysis only | lab `caption.py` docstring |
| Demucs htdemucs (stems) | not in files | analysis only | |
| Chatterbox (rejected) | MIT; keeps Resemble's Perth watermark | unused | `AU` |
| YuE2 | CC-BY-NC-4.0 | skipped | `SE` 3 |

YouTube side (`RR` section 3): tick "AI use" at upload (AI music is the main focus); the player label for AI music may appear; disclosure does not limit reach or monetisation eligibility.

## 4. Prompt formats

### ACE-Step era (G21, measured)
- Tags file + lyric sheet; hyphenate and exclaim compound refrains ("Knowledge cut-off! Cut-off!"): refrain heard 6/6 vs 0/6; tag spoken parts `[spoken word]`; never all-caps (`G` G21).
- Failed levers: pronunciation hints ("Mes-si", "Al-gee") 88.4 % vs 92.1 %; splitting long lines at commas 82.7 % (`SE` 4d).

### MiniMax Music 3 (the trained format, `PV4` F1-F6)
- Three sections from the official repo (github.com/MiniMax-AI/MiniMax-Music3): **Global Metadata, Vocal Details, Arrangement** (`SE` 3 note 1).
- Box names verbatim from MiniMax's 1,000 caption templates: `Basic Attributes`, `Global Emotional Progression`, `Application Scenarios & Imagery`, `Sonics & Production Profile`, `Vocal Gender & Timbre`, `Vocal Style`, `Harmony/Backing Vocals`, `Vocal FX`, `Instrument Lifecycle Description`, `Groove & Foundation Progression`, `Embellishments, Textures & Spatial FX` (`PV4` F1; `kc\caption-minimax-v8.txt`).
- Fixed phrasing `bpm is 122. key is D, and scale is minor.`; ComfyUI rewrites `<|bpm 124|>` into `bpm is 124` (`PV4` F1, F2).
- Templates run 500-600 words; the Arrangement is a section-by-section timeline; limit 5,000 tokens (`PV4` F3, F4).
- Lyric tags: `[Intro] [Verse] [Pre-Chorus] [Chorus] [Post-Chorus] [Bridge] [Instrumental] [Solo] [Outro]`; ComfyUI lowercases them; templates never quote lyric words, so word-level direction goes in the lyric spelling (`PV4` F5, F6).
- No exclude box: phrase exclusions inside Vocal Style (`reference-deconstruction-2026-10-14.md` 9, lesson 2).
- Lyric-layout levers (`G` G23, G24, G25): `[Instrumental]` before each chorus and the bridge slows 176-195 to ~145 wpm; stretched vowels are sung literally (`tomorroooow` -> "tomoroo"; use plain or `tomorrow-oh`); `graph-ics` or `graphix` keeps the s; a refrain written three times lands 6 of 6; a stretched spelling only in the final chorus gives the payoff hold ("tune", "tune", then "tuuuu-oo-oo-oon"); every take invents filler after the last line.

### Final prompt structure (v8, 656 words, `kc\caption-minimax-v8.txt`, quoted)
```
Global Metadata
Basic Attributes: bpm is 144. key is G#, and scale is major. Electropop / Synth-Punk with Chiptune Pop.
Global Emotional Progression: Aggressive, tense and confrontational with a cyberpunk edge and a playful,
  video-game sparkle. The song opens with a soft, slow, intimate spoken greeting over complete silence, ...
  each pre-chorus ends on a long held note, then the music drops out for a moment before the chorus
  explodes into a powerful anthem. ...
Application Scenarios & Imagery: ...
Sonics & Production Profile: ... Two sick drops: the music cuts out right before the first chorus and
  right before the final chorus, then slams back in at full power.
Vocal Details
Vocal Gender & Timbre: Singer A (Female). An assertive, confident female voice with a bright, digital, processed edge.
Vocal Style: ... Phrasing is steady and even ... Long held notes come only at the end of each pre-chorus
  and at the end of the bridge. Crisp diction, every word intelligible, every final consonant pronounced. ...
Harmony/Backing Vocals: ... energetic shouted "Wooh! Wooh! Wooh!" backing vocals between the chorus lines;
  the repeated hook "cut-off" is shouted three times by a gang of backing voices; ...
Vocal FX: ...
Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering): Primary: ... Secondary: ...
Groove & Foundation Progression: ... The drums and bass cut out right before each chorus and slam back in. ...
Embellishments, Textures & Spatial FX: ...
```
Lyric sheet (`kc\lyrics-mm-p8b.txt`, 74 non-empty lines): `[Spoken]` greeting one sentence per line ("It's me again... for the first time."), `[Instrumental]`, `[Verse]`, `[Pre-Chorus]`, `[Instrumental]`, `[Chorus]` with the triple refrain written out, and so on.

### How the prompt evolved (one line each)
- v1-v3 caption: ~163-180 words in 3 sections, an equipment list, no timeline; takes "so varied" (`PV4` F3; `H14` note 1).
- v4: trained format, 888 words; pace fell into 130-146 wpm; "Disney princess" voice traced to v4's own words ("bright, warm, clear mezzo-soprano, slightly airy", "soft piano") (`PV4` 2, 4).
- Reference deconstruction: 9 reference songs split into the MiniMax boxes with the ear + meter (`reference-deconstruction-2026-10-14.md`).
- 9 style auditions (2 seeds each, 18 takes): Idi picked 3 (like Ignore Previous Instructions), then 7 (like The Simulation's Ending); male voice rejected (`AU`).
- v5 = 3 + 7 combined; v5B (seed 3011) became gold; v6 = audition 3's prompt nearly verbatim + Idi's fixes; v7 = soft slow bookends (lost to v5B); v8 = v5 caption + bookends over silence + `[Instrumental]` around the spoken parts -> v8B picked; v9 (no outro break, harder `tuuuuuuune`) did not beat it (`AU`).

## 5. Generating takes

- Command: `COMFY=http://127.0.0.1:8189 WF=wf_minimax_tiled.json python -I gen_song.py <lyrics> <out dir> <seconds> 124 "D major" <seeds> <caption.txt>` (`H14` line 64). MiniMax ignores the BPM/key arguments: pace comes from caption + lyric layout (`H14`).
- Batch shape for v8: 2 lyric variants x 12 seeds, 240 s each, then `/free` unload, then the screen chain (lab `kc\mm-v8.sh`).
- Cost: ~4 min per MiniMax take; ~8 min when ComfyUI fell back to low-RAM mode (v9) (`AU` v9).
- Env options: `FREE_FIRST=1` unloads models before switching engines; `STATUS_LABEL/STATUS_TOTAL/STATUS_OFFSET` write Idi's status board `D:\work\AIMVs\ours\_STATUS.txt` (lab `gen_song.py`).
- Rule G19: generate many, shortlist by measurement, Idi's ear decides (`G`). Reference makers worked the same way: 10-12 takes (End Of The Show), 49 (Drop the Prompt), ~15 (Seguramente) (`reference-deconstruction-2026-10-14.md` 9; lab `research-video-makers-methods.md` 2.4).

## 6. Auditioning, ranking, repairing

Screen chain per batch (lab `kc\mm-v8.sh`): `audition.py` (trim filler, cut preview) -> `probe_lines.py` -> `pace.py` -> `v5check.py` -> `bookends.py`. Then Idi listens to a top 3 in `D:\work\AIMVs\ours\vN\`.

Repair route (ACE era, rule G22, measured): repaint each bad window **from the original** (base model, 32 steps, guidance 7, full lyric sheet, 4 variants), keep the variant that sings the expected words, splice only the window with 0.35 s equal-power crossfades, verify outside the windows with `diffmap.py` (<= 0.02), then re-level voice and music per window with `balance.py` (repaints came out 2-4 dB quieter, voice up to +5.4 dB hot). Never chain repaints: chained passes collapsed whole-song accuracy to 55.7 % (`SE` 4d, 4e; `G` G22).

Bookend edit route (v5B, later dropped): `stems44.py` -> `fix_bookends.py` (cuts in the middle of measured silences, sentences slowed 10 %, voice -3/-4 dB, backing faded before a clashing E/F synth) -> `cutcheck.py` gate (audio 50 ms around each cut 25 dB+ below the passage peak) -> `kc\gold\rebuild.sh` copies only on a pass (`AU`).

## 7. Stems, word timing, sync data

| step | tool | output | measured | source |
|---|---|---|---|---|
| stems | Demucs htdemucs: `stems.py` (vocal, 44.1 kHz mono), `stems44.py` (all 4, 44.1 kHz stereo), `refstems.py` (all 4, 22.05 kHz mono) | `kc\stems\`, `refs\stems\` | | script docstrings |
| raw word times | `align_take.py`: faster-whisper large-v3 word stamps mapped onto the written lyric (difflib), gaps interpolated, plus librosa beats + loudness | `kc\final\v8B-3327-timing.json` (54 lines, 483 words; keys match `align_take.py` output) | Whisper stamps run early: median 0.17 s inside lines, ~0.33 s at line starts | `AU`; `VTP` 3a |
| forced alignment | `research-video-tech\fa_align.py`: torchaudio MMS_FA CTC on the Demucs vocal stem, per line window | `research-video-tech\fa-v8B.json` (482 of 483 words) | FA start minus Whisper start median +0.174 s; line-first words unreliable (span stretches back up to 1 s in 19 lines) | `VTP` 3a |
| corrected times | `kc-video\sync\build_timing_v2.py`: FA start when score >= 0.5 and span < 0.6 s; else vocal-stem onset; line-first words from the loudness rise; starts monotonic, >= 3 frames on screen; lit = start - 1 frame (60 fps) | `kc-video\sync\kc-timing-v2.json` | | docstring; `VTP` 3b |
| ear check | `click_reel.py` (click on every word start over the song) + `verify_reel.py` (finds the clicks, compares) | `D:\work\AIMVs\ours\video\gate1\` | median and p95 error printed per run | docstrings |
| drum layer | `kc-video\sync\build_drums.py`: kicks, crashes, chokes (band stops dead), downbeats, section ones | `sync\drums.json` | | docstring |
| engine data | `kc-engine\tools\build_data.py` | `data\lyrics.json` (per word `start` = lit, `end`, `sung` onset; 54 lines, 483 words) and `data\audio.json` (duration 192.6, bpm 161.5, 514 beats, 135 downbeats, 11 sections, 18 chokes, kick/snare/hat/vocal onsets, 100 fps envelopes per stem) | grid moved -24 ms onto the drum hits (`GRID_SHIFT`); bar phase drifts, so the bar count restarts at every section start; one hand fix ("Algae" at 117.284 s) | script header |
| pitch | `kc-engine\tools\build_pitch.py`: pYIN on the v8B vocal stem | `data\pitch.json` (median MIDI per word, 50 fps contour) | | script header |
| captions | SRT from `data\lyrics.json` word times, one cue per sung line | `release\knowledge-cutoff.en.srt`, 54 cues, no overlaps | builder script not named in files | `handoff-2026-10-31-release.md` line 48; `knowledge-cutoff-release-2026-10-31.md` line 21 |
| gate on picture | per-word sync check in the render | 483/483 words lit, negative control 0, timing -17 ms (full6b) | | `knowledge-cutoff-parity-pass-2026-10-26.md` |

Sections in `audio.json` are typed by hand in `build_data.py` from the time map: intro 0-9.4, verse1 -27.6, pre1 -34.1, chorus1 -61.9, verse2 -80.3, pre2 -86.5, chorus2 -115.0, verse3 -133.2, bridge -150.0, final -180.4, outro -192.6 s.

## 8. Pacing

- Target band G1: 130-140 words/min (6 of 8 references sit at 130-146) (`G`).
- MiniMax has no tempo control; one-shots sang 176-195 wpm; `[Instrumental]` breaks brought ~145; the v4 trained format gave 130-146; adding speed words ("fast hi-hats", sparkle) brought back rap-like verses (`SE` 4f; `PV4` 2; `AU` v5).
- Same prompt, different seeds: v6 ranged 143-180 wpm (`AU` v6). Absolute timing exists only after a take is picked.
- Asked vs tracked: the caption asks `bpm is 144`; the engine grid reads 161.5 BPM (`audio.json`). Not reconciled in files; beat trackers read half or double tempo on references (`reference-deconstruction-2026-10-14.md` 0).

## 9. Scripts, one line each (lab root unless noted)

Interpreters: `V` = `venv\Scripts\python` (lab venv); `A` = `C:\Users\jep\acestep\python_embeded\python.exe`; `C` = ComfyUI embedded python. Usage strings are the scripts' own.

| script | does | command |
|---|---|---|
| `gen_song.py` | takes through ComfyUI's API (ACE-Step or MiniMax by `WF`) | `python gen_song.py <lyrics.txt> <out dir> <seconds> <bpm> <keyscale> <seed1,seed2,...> <tags file>` |
| `make_workflows.py` | builds `wf_ace4b.json`, `wf_minimax.json` | `python make_workflows.py` |
| `status.py` | writes Idi's status board line | `python status.py "<message>"` |
| `audition.py` | trims invented filler after the outro, cuts a preview | `V audition.py <in dir> <out dir>` |
| `rank_takes.py` | ranks takes by word accuracy (Whisper vs lyric) | `V rank_takes.py <takes dir> <lyrics.txt>` |
| `probe_lines.py` | refrain hits /6, intro, outro, "Fair" line, overall % | `V probe_lines.py <dir> <lyrics.txt>` |
| `errmap.py` | lists lyric spans Whisper did not hear, with times | `V errmap.py take.mp3 lyrics.txt` |
| `pace.py` | words/min and holds on key words | `V pace.py take.mp3 [...]` |
| `v5check.py` | triple refrain count, "graphics", anchored drops, pace | `V v5check.py file_or_dir ...` |
| `bookends.py` | intro/outro span, words/s, gaps, loudness; "tune" holds | `V bookends.py file_or_dir ...` |
| `kcmeter.py` | lyric-anchored drops, "tune" hold, "algae", sung % | run `stems.py` first; `V kcmeter.py` |
| `drops.py` | bridge drop: quietest 4 s in 55-85 % vs loudest after | `python drops.py <dir>` |
| `drops2.py` | 3 deepest short drops that slam back | `python drops2.py <file-or-dir>...` |
| `curls.py` | melisma: hold length and pitch travel on target words | `V curls.py <take1.mp3> [...]` |
| `tunehold.py` | pitch-based "tune" hold (failed validation, unused) | `V tunehold.py file_or_dir ...` |
| `tails.py` | last words heard in the last 14 s | `V tails.py file_or_dir ...` |
| `endwords.py` | word stamps from a start time to the end | `V endwords.py file.mp3 start_s` |
| `wordtimes.py` | Whisper word times inside a window | `V wordtimes.py take.mp3 <from_s> <to_s>` |
| `rhymes.py` | line-end rhyme pairs on Idi's R0-R6 ladder (CMU phonemes) | see docstring |
| `repaint.py` / `repaint2.py` | repaint a time window with the official ACE-Step pipeline | `A repaint.py <src.mp3> <start_s> <end_s or -1> <lyrics.txt> <caption.txt> <out_dir> <seeds>` |
| `check_repaint.py` | source match before the window, words inside it | `V check_repaint.py <src.mp3> <window_start_s> <listen_from_s> <repaint1.mp3> [...]` |
| `repair.py` | N variants per window, keeps the best-sung | `V repair.py <src.mp3> <fixes.json> <out_dir>` |
| `splice.py` | pastes windows into the original with equal-power crossfades | `python splice.py <original.mp3> <chosen.json> <out.mp3> [xfade_s]` |
| `diffmap.py` | spectral difference per 10 s block (0 = identical) | `python diffmap.py src.mp3 other.mp3 [...]` |
| `seams.py` | loudness jump vs original around each window | `python seams.py orig.mp3 final.mp3 chosen.json` |
| `balance.py` | re-levels voice and music of repainted windows to the original | `A balance.py <original.mp3> <chosen.json> <out_dir> [measure or fix]` |
| `stems.py` | Demucs vocal stem per take, 44.1 kHz mono | `A -I stems.py <cache> take.mp3 or dir ...` |
| `stems44.py` | full-quality 4-stem split, 44.1 kHz stereo | `A -I stems44.py <out dir> song.mp3` |
| `stemscan.py` | per-stem loudness in 0.5 s steps + 2 strongest pitch classes of "other" | `V stemscan.py <stem base> <from_s> <to_s>` |
| `fix_bookends.py` | re-spaces, slows, softens spoken intro/outro; fades a clashing synth | `V fix_bookends.py <stem base> <out.wav>` |
| `cutcheck.py` | gate: every cut sits in silence | `V cutcheck.py <stem base>` |
| `tts_gen.py` / `tts_screen.py` / `tts_reel.py` | Chatterbox clone readings, screen, listening reel (route closed) | `C:\Users\jep\tts\venv\Scripts\python.exe -I tts_gen.py <out dir>` etc. |
| `align_take.py` | Whisper word stamps onto the lyric, plus beats + loudness | `V align_take.py <take.mp3> <lyrics.txt> <out.json>` |
| `fix_timing.py` | caps stretched words, spreads clustered starts | `python fix_timing.py in.json out.json` |
| `timemap.py` | every line with start/end, section labels from lyric tags, deep drops, long holds | `V timemap.py <song.mp3> <timing.json> <lyrics with [tags]> <out.md>` |
| `research-video-tech\fa_align.py` | MMS_FA forced alignment on the vocal stem | `A -I fa_align.py <vocals.wav> <timing.json> <out.json>` |
| `research-video-tech\sync_offset.py` | how early Whisper starts sit vs vocal onsets | `V -I sync_offset.py <vocals.wav> <timing.json>` |
| `kc-video\sync\build_timing_v2.py` | corrected word starts (rule in section 7) | `V -I build_timing_v2.py` |
| `kc-video\sync\click_reel.py` / `verify_reel.py` | click reel for the ear; machine check of the reel | `V -I click_reel.py`; `V -I verify_reel.py` |
| `kc-video\sync\build_drums.py` | kicks, crashes, chokes, downbeats, section ones | see docstring |
| `kc-engine\tools\build_data.py` / `build_pitch.py` | engine `lyrics.json`, `audio.json`, `pitch.json` | `V -I build_data.py`; `V -I build_pitch.py` |
| `analyze.py` | Whisper lyrics + librosa measures for reference songs | `V analyze.py <mp3 dir> <out dir>` |
| `refmeasure.py` / `refstems.py` | reference stems and audio measures | `A -I refstems.py <cache> song.mp3 ...`; `V refmeasure.py <cache> <out.json> song.mp3 ...` |
| `caption.py` / `understand.py` | ACE-Step Captioner prose caption; ACE-Step understand mode (bpm, key, genre) | `A -I -X utf8 caption.py <out.json> song.mp3 ...`; `A -I understand.py <out.json> <runs> song.mp3 ...` |

## 10. What failed or wasted time

- ACE-Step knob grid: 28 takes, no setting beat the defaults (`SE` 2).
- MiniMax parked a day on crashes; the "two engines in RAM" theory was refuted; the real cause (decode out of GPU memory) was visible only in a ComfyUI log jep could not read on Idi's instance. Fix: jep's own ComfyUI + tiled decode (`SE` 4c, 4f).
- Chained repaints degraded the whole song (55.7 %); the careful repair still sounded patched to Idi and was abandoned (`SE` 4d, 4f).
- Lyric tricks that cost accuracy: pronunciation hints, comma splits (`SE` 4d); stretched spellings sung literally ("tomoroo", "borroo", "urn") (`PV4` 4; `AU`).
- v4 risers before breaks erased the pre-chorus drop (18 dB -> 0-4 dB) (`PV4` 2 reading 4).
- Voice wording made a "Disney princess" voice; piano partly MiniMax's own habit (5 of 16 audition takes) (`PV4` 4; `AU` finding 1).
- Voice-clone bookends: 84 readings, all rejected by ear (`AU`).
- First bookend edit cut inside words ("aga......in"): the transcriber's times run ~0.3 s early and re-transcription cannot hear a gap inside a word; fixed with `cutcheck.py` (`AU` correction 2026-10-15).
- Meters that misled: the anchored drop meter scored audition 3 at ~1 dB where Idi heard "sick drops"; `tunehold.py` failed validation; loudness misses riser/filter drops (`AU`; `PV4` footnote).
- v8 rates per take (payoff 4/24, quiet outro 1/24, slow intro 7/24): a take with all of them is "roughly 1 in thousands"; each round must raise one rate (`AU` v8).
- Reporting gap: v9 finished ~17:35 and Idi learned it 3 hours later; status board added (`AU`).
- Whisper word stamps used raw would have put lyrics early on screen, the fault viewers named in Run It Again (`VTP` 3a; lab `research-video-makers-methods.md` 1).

## 11. Phase 1 for the next video: audio while lyric lines and their visuals are designed together

Idi's new idea: craft each lyric line with its visual at the same time. Constraint from KC: exact word times exist only after a take is picked (seed-to-seed pace spread 143-180 wpm on one prompt, `AU` v6), and any lyric change after the pick means new takes (KC's song of record had "no audio edits", `H17`; repair and clone routes were rejected by Idi). So design runs on structure first and binds to times at lock.

Order of work:
1. Before any take: write line + visual pairs on the lyric sheet's structure (sections, line order, words per line, planned holds via spelling, planned drops via `[Instrumental]`). These lyric-layout levers are the only pace controls MiniMax has (`G` G23-G25). **Credit bookends (Idi R34, 2026-11-08, standing):** the sheet opens with `[Intro]` and closes with `[Outro]` instrumental bars, a few seconds each, so the credits ride music; the release carries no silent frame. Screen every take for them (`bookends.py`: first vocal onset and last vocal offset vs file length); a take whose voice starts in its first second or ends on its last fails this screen. KC's spoken bookends predate the rule; PA (vocal at 0:00.37) is grandfathered with credits on its L04 receipt.
2. Song style in parallel: run new references through `refstems.py` -> `refmeasure.py` and `caption.py`; draft the caption in the trained boxes; 2-seed style auditions with a preview reel for Idi's ear (`AU` method).
3. Scratch takes per lyric draft (~4 min each on MiniMax): `gen_song.py` -> `audition.py` -> `align_take.py` -> `timemap.py` give provisional line times, drops and holds for animatics.
4. Visual code looks lines up by content and snaps cuts to the beat grid, never hard-coded times (mexicat `timeline.ts` rule, lab `research-video-makers-methods.md` 2.1 and technique 8), so a new take re-times the picture for free.
5. Lock lyric, then the final batch (12+ seeds per variant), screen, Idi's ear picks.
6. After lock: the full sync chain (section 7) and the picture gate (483/483-style per-word check).

Audio facts the visual design needs, and the producer of each:

| fact | needed for | producer | when available |
|---|---|---|---|
| section boundaries | plate and scene windows | lyric `[tags]` -> `timemap.py`; hand list in `kc-engine\tools\build_data.py`; section ones in `build_drums.py` | structure now; times after a take |
| line start/end | line-level staging, animatic | `align_take.py` (provisional, early) -> `timemap.py` | each scratch take |
| word times (lit, sung, end) | per-word reveals, karaoke, captions SRT | `align_take.py` -> `fa_align.py` -> `build_timing_v2.py` -> `build_data.py` (`data\lyrics.json`); check `click_reel.py` + `verify_reel.py` | final take only |
| tempo | motion speed, pace of reveals | `align_take.py` (librosa beat_track); `refmeasure.py` tempo on drums; octave-ambiguous | each take |
| beat grid + downbeats | cuts and hits on the beat | `build_data.py` (grid shifted onto drum hits; bar count restarts per section) | final take |
| kick / snare / hat onsets, chokes | hits, flashes, freezes | `build_data.py` (drum stem onsets), `build_drums.py` (chokes), stems from `refstems.py` | final take |
| drops (depth, time) | visual silence, then the slam | `timemap.py`, `drops2.py`, `kcmeter.py` (lyric-anchored), `v5check.py` | each take |
| long holds and payoff word | held type, stretched letters | `timemap.py` (holds >= 1.5 s), `pace.py`, `bookends.py` | each take |
| spoken bookends (span, gaps) | open and close frames, the loop | `bookends.py` | each take |
| pitch per word, contour | type riding the melody (KC's pitch string) | `build_pitch.py` (`data\pitch.json`) | final take |
| loudness envelopes per stem | motion intensity, burst placement | `build_data.py` features (100 fps rms, low/mid/high, per stem) | final take |
| words/min | density of on-screen text | `pace.py` | each take |
