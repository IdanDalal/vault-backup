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

## 5. Plan once the files are in place

1. 8 takes each: ACE-Step + 4B planner, MiniMax Music 3. Score with `probe_lines.py` + error map.
2. Winner → Idi's ear.
3. If a few words still slip: repaint those seconds in ACE-Step's own app.
