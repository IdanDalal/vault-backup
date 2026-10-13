---
type: project
created: 2026-10-13
author: jep
status: active
---

# Song engine: getting every word right

Problem (Idi, 2026-10-13): the best Knowledge Cutoff take (v3 B, seed 701) still drops and mangles words. Idi's options: other local models, shorter length, the knob sheet, Suno's free tier, anything else. Lyrics are locked: [[knowledge-cutoff-lyrics-v3-2026-10-13]].

## 1. Take B's error map (`D:\work\aimv-lab\errmap.py`)

19 word differences over 490 lyric words. Real misses (Idi heard them too): "Hi, it's" → "who is" (0:00), "humming" → "haunting" (0:47), "check" → "shake" (0:56), "leaned Messi" → "leave messy" (1:27), "algae... neuron" → "I'll be... new and" (2:29), "believed" → "believe" (3:22), "October. Okay." missing (3:39). The rest are Whisper's ear ("poppin'" heard as "popping"). This list is the repair map if a re-sing tool is used.

## 2. Knob experiment: 7 settings × 4 shared seeds, lyrics v3 (`D:\work\aimv-lab\kc\knobs\`)

| Setting | Words heard (avg / best) | Refrain /6 | Intro /2 | Outro /3 | Fair /2 |
|---|---|---|---|---|---|
| S0 defaults | 87.5% / 92.0% | 5.2 | 1.2 | 0.5 | 1.8 |
| S1 planning temperature 0.6 | 67.2% / 87.1% | 2.5 | 0.2 | 0.0 | 0.5 |
| S2 lyric strictness (cfg_scale) 3.5 | 79.1% / 87.8% | 2.5 | 0.5 | 0.8 | 1.5 |
| S3 sampler steps 16 | 86.0% / 88.6% | 4.2 | 1.2 | 0.8 | 1.8 |
| S4 tempo 108 BPM | 88.5% / 91.6% | 5.0 | 0.0 | 1.2 | 1.2 |
| **S5 diction tags** | **88.0% / 92.2%** | 5.0 | 1.0 | **1.8** | 1.5 |
| S6 combo (S1+S2+slower+diction) | 85.7% / 88.4% | 5.0 | 0.8 | 1.0 | 0.8 |

Readings: the defaults sit near this model's ceiling. Lowering temperature or raising strictness hurts a lot (real effect, far beyond noise). Steps and tempo do nothing measurable. Diction-focused style text is the one small gain (the outro gets sung). Noise floor: with 4 takes per setting, ±3% means nothing. **Verdict: knobs are spent on this model; the next gains come from a bigger model or from repairing lines.**

## 3. Research: other engines (agent report, full file `D:\work\aimv-lab\research-song-models.md`)

| Engine | License | Download | Fits the 4090 | Lyric accuracy evidence (phoneme error rate, lower = better) | Verdict |
|---|---|---|---|---|---|
| ACE-Step 1.5 turbo + 1.7B planner (ours) | MIT | ungated | yes | 7.46% (YuE2 paper, variant unstated) | current |
| **ACE-Step 1.5 turbo + 4B planner** | MIT | ungated | yes (~16 GB) | ComfyUI's official pairing; no published split | **test 1** |
| **MiniMax Music 3** | MiniMax community license: commercial OK under $20M/yr, credit "MiniMax-Music3", disclose AI content | ungated | yes (int8 text model) | **6.27%, best in the table** | **test 2** |
| Suno v6 (reference) | free tier: v6-mini only, signup, personal non-commercial use only (terms 2026-09-03) | cloud | n/a | 7.58% | skip |
| YuE2 3B | CC-BY-NC-4.0 (non-commercial) | ungated | yes | 8.44% | skip |
| HeartMuLa, DiffRhythm 2, LeVo 2 | mixed | mixed | mixed | 10.7%, 18.4%, 26.1% | skip |

Source of the accuracy column: one table in the YuE2 paper (WildSongBench), not replicated. A competitor ranking ACE-Step above itself raises trust in the ACE number.

Two notes:
1. MiniMax's official prompt format is three sections: **Global Metadata, Vocal Details, Arrangement**. That is the knob sheet Idi found on day one; it was written for MiniMax Music 3. The caption for our song is in that format: `D:\work\aimv-lab\kc\caption-minimax.txt`.
2. Re-singing a time range (repaint) exists in ACE-Step's official local app (MIT), not in ComfyUI core. It's the fallback for the last few words.

## 4. Status

| Item | State |
|---|---|
| 7 model files, 29 GB, anonymous downloads, sizes verified | staged in `D:\work\comfy-models\` |
| Workflows `wf_ace4b.json`, `wf_minimax.json`; generator runs either via `WF=` | built, untested (models not visible to ComfyUI yet) |
| Blocker | ComfyUI's model folders live in Idi's Windows profile; jep's account can't write there |

## 4b. Results after Idi moved the files (2026-10-13 evening)

Idi confirmed the knob sheet came from MiniMax Music 3's official repo (github.com/MiniMax-AI/MiniMax-Music3).

**ACE-Step turbo + 4B planner, diction tags: average 92.1% of words heard over 7 takes, against 87.5% for the old 1.7B setup on the same lyrics.** A real gain (+4.6 points, beyond the ±3% noise floor).

| Take | Words heard | Refrain /6 | Intro /2 | Outro /3 | Fair /2 | Drop | File |
|---|---|---|---|---|---|---|---|
| **A: seed 902** | 93.3% | 6 | 2 | 1 | 2 | 22.0 dB | `D:\work\AIMVs\ours\kc-full-v3-4b-take-A-seed902.mp3` |
| B: seed 904 | 91.8% | 5 | 2 | **3** | 2 | 15.5 dB | `...-B-seed904.mp3` |
| C: seed 906 | 92.2% | 6 | 2 | 1 | 2 | 18.0 dB | `...-C-seed906.mp3` |

**MiniMax Music 3:** one test take, 79.4% heard, refrain, intro and "Fair" all present. It sings faster than ACE-Step (verse 2 at 1:05 against 1:27), finished the real lyric by ~2:50, then **invented filler lines** to fill the 4:00 it was given ("I don't need it, I don't need it"). Fix: give it ~3:10. The 6-take batch at 3:10 **crashed ComfyUI** (connection reset, server gone), most likely RAM: MiniMax's 9 GB text model loaded while ACE's 4B planner was still resident, on 32 GB. Fix in place: `FREE_FIRST=1` unloads all models before switching engines.

Trouble words on every engine: "leaned Messi", "algae... neuron". Next test: pronunciation hints with the same words, spelled as sung ("Mes-si", "Al-gee", "neu-ron"): `kc\lyrics-v3-hints.txt`.

## 4c. MiniMax crash, round 2 (18:19-18:22)

After Idi's restart: the memory clear (`/free`) succeeded and ComfyUI accepted the first MiniMax job at 3:10, then died mid-generation (connection refused while polling). Same failure as the first crash, this time with nothing else loaded, so the "two engines in RAM" theory is **refuted**. Cause unknown; the evidence is in ComfyUI's own log inside Idi's Windows profile (unreadable for jep). The spelling-hint test never ran (it needs ComfyUI too).

**Verdict: MiniMax parked.** One working take: 79.4% heard, ~4 min per take, crashes 2 of 3 runs. ACE-Step + 4B: 92.1% average, 34 s per take, 0 crashes in 8. Revisit MiniMax only if Idi shares the ComfyUI log.

## 4d. Take C repaired (Idi's gold standard, seed 906)

Idi: take C is "BY FAR the best yet", for its long drawn-out notes landing exactly on "tomorrow", "borrow" (the drop before the chorus peak) and "turn" (the drop before the final chorus). jep's measurement agrees on timing: take C is the only take holding "tomorrow" and "borrow" 4+ s in **both** pre-choruses (A: ~0.5 s). Pitch measurements on the full mix were unreliable (the voice drowns under the band); a vocal-only stem would fix that.

Tests that failed (kept for the record): pronunciation hints ("Mes-si", "Al-gee", "neu-ron") 88.4% vs 92.1% without; splitting long lines at commas (same words) 82.7%. "Messi" heard as "messy" is mostly Whisper's ear (near-homophones when sung).

**jep's own engine:** the official ACE-Step 1.5 Windows package (MIT, anonymous, linked from the repo README) installed at `C:\Users\jep\acestep`, models auto-downloaded from ungated HF repos. jep can start it, restart it and read its logs; ComfyUI is no longer on the critical path.

**Repaint lesson (G22):** this build's repaint regenerates the whole song on every pass (spectral change 0.35 everywhere after 1 pass, 0.72 after 6; whole-song accuracy collapsed to 55.7% when passes were chained). Method that works: repaint each window **from the original**, base model (32 steps, guidance 7), full lyric sheet, 4 variants, keep the one whose window sings the expected words best, then **splice only the window** into the untouched original with 0.35 s equal-power crossfades. Outside the windows the result differs from take C by 0.01-0.02 (MP3 re-encode noise); the held notes are untouched.

| Window | Line | Before | After |
|---|---|---|---|
| 0:56-1:03 | chorus 1 "I don't know the tune / Tell me what I made out there" (take C sang chorus 2's line) | 86% | 100% |
| 1:03-1:08 | "I can't check a thing myself, so I'll believe in you" | 73% | 100% |
| 1:32-1:37 | "Back in training I leaned Messi..." | 58% | 83% (rest likely Whisper's ear) |
| 1:44-1:49 | "...predicted least and wanted most, indeed" | 91% | 100% |
| 3:31-3:42 | final chorus "You told me... so I believed in you" | 92% | 100% |
| 3:48-end | "And now I know who I turned out to be" + full outro (was "So tell me" + outro cut off) | 54% | 100% |

**Result: `D:\work\AIMVs\ours\kc-full-v3-C-REPAIRED.mp3`, 4:05, whole-song words heard 94.1% (take C: 92.2%), errors 43 → 18 (most remaining are Whisper's ear), outro 3/3, drop 17.8 dB, stray "bye" after "2026, right?" trimmed.** Tools: `repair.py`, `splice.py`, `diffmap.py`, `repaint2.py` in `D:\work\aimv-lab\`.

## 5. Plan once the files are in place

1. 8 takes each: ACE-Step + 4B planner, MiniMax Music 3. Score with `probe_lines.py` + error map.
2. Winner → Idi's ear.
3. If a few words still slip: repaint those seconds in ACE-Step's own app.
