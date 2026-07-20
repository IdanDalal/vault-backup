---
type: project
created: 2026-07-20
status: active
author: jep
tags:
  - tutoring
---

# Heblish Bake-off — run on the 4090 PC

Scores the transcription candidates against the five clips recorded 2026-07-16 (scripts + ground truth: [[tutoring-heblish-test-scripts]]). This folder syncs via Syncthing; the audio lives in `vault-agent/inbox/TUTORING/` on the laptop — copy the five `.m4a` files to a `clips/` folder next to this script on the PC.

## Contenders

| Model | Backend | Why it's here |
|---|---|---|
| `large-v3` (stock) | faster-whisper | Best code-switching instincts of any Whisper; the baseline to beat |
| `ivrit-ai/whisper-large-v3-turbo-ct2` | faster-whisper | Best pure Hebrew (295h crowd + 93h pro fine-tune); language detection deliberately degraded, so it's forced to `he` — clip 3 tests whether English islands survive that |
| `danielrosehill/whisper-hebrish` | transformers | Optional. Code-switch fine-tune, but for *English-matrix* immigrant speech — the mirror image of our Hebrew-matrix lessons. Skips gracefully if the repo id is wrong; exact id findable via the [Hebrish blog post](https://huggingface.co/blog/danielrosehill/whisper-hebrish) |
| Meta Omnilingual ASR 7B | — | **Deferred.** ~29 GB, its own fairseq2 install stack. Only worth it if both Whispers disappoint on clip 3 |

Diarization: `pyannote/speaker-diarization-community-1` (pyannote.audio 4.0), run once per clip, merged into every model's transcript by overlap. Uses exclusive mode (one speaker at a time) — cleanest for aligning to STT timestamps.

## Setup (once)

1. **HF token** (free): huggingface.co → Settings → Access Tokens → "read" token. Then open the [community-1 model page](https://huggingface.co/pyannote/speaker-diarization-community-1) while logged in and accept the gated-access form (CC-BY-4.0; fully offline after download).
2. **ffmpeg** on PATH (used to normalize m4a → 16 kHz wav).
3. Python env:

```
python -m venv venv
venv\Scripts\activate          # Windows — or: source venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install faster-whisper transformers accelerate pyannote.audio
```

## Run

```
set HF_TOKEN=hf_xxx            # Windows — or: export HF_TOKEN=hf_xxx
python bakeoff.py --audio-dir clips --out results
```

First run downloads ~8 GB of models; transcription itself is a few minutes total on the 4090. Then a second pass with `--vad` on clip 5 only, to measure how much VAD tames the silence-minute hallucinations:

```
python bakeoff.py --audio-dir clips --out results-vad --vad
```

**VAD is off by default on purpose** — clip 5's silent minute is a hallucination trap and we want to watch each model fall into it (or not) before deciding whether VAD is part of the pipeline.

## Judging (bring results back to jep)

Copy `results/` into the vault (e.g. `vault/projects/tutoring-bakeoff/results/`) so it syncs back, then compare each clip's `COMPARE.md` against the scripts:

- **Clips 1–2** — sanity floors: both models should be near-perfect in their home language.
- **Clip 3** — the decider: embedded English words, mid-sentence switches, spelled letters (C-A-T), mixed counting. Does forced-`he` ivrit mangle the English islands? Does stock large-v3 mangle the Hebrew matrix?
- **Clip 4** — graceful degradation: childish mispronunciations, singing, 5s overlap, whisper, distance.
- **Clip 5** — diarization truth (2 speakers? clean turns through the position swap?) and the silence-minute hallucination check.

Winner becomes the `lesson-transcribe` pipeline. Caveat carried from the design: sister ≠ 9-year-old — revalidate on real lesson-one audio once consent and the transparency conversation have happened.
