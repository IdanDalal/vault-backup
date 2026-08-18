---
type: project
created: 2026-07-20
status: active
author: jep
tags:
  - tutoring
---

# Heblish Bake-off — run on the 4090 PC

Scores the transcription candidates against the five clips recorded 2026-07-16 (scripts + ground truth: [[tutoring-heblish-test-scripts]]). The audio lives in `~/tutoring-data/sessions/` on the laptop (outside vault/git/backups; pipeline rebuild 2026-08-18) — copy `.m4a` files to a `clips/` folder next to this script on the PC when re-running.

## Contenders

| Model | Backend | Why it's here |
|---|---|---|
| `large-v3` (stock) | faster-whisper | Best code-switching instincts of any Whisper; the baseline to beat |
| `ivrit-ai/whisper-large-v3-turbo-ct2` | faster-whisper | Best pure Hebrew (295h crowd + 93h pro fine-tune); language detection deliberately degraded, so it's forced to `he` — clip 3 tests whether English islands survive that |
| `danielrosehill/whisper-hebrish` | transformers | Optional. Code-switch fine-tune, but for *English-matrix* immigrant speech — the mirror image of our Hebrew-matrix lessons. Skips gracefully if the repo id is wrong; exact id findable via the [Hebrish blog post](https://huggingface.co/blog/danielrosehill/whisper-hebrish) |
| Meta Omnilingual ASR 7B | — | **Deferred.** ~29 GB, its own fairseq2 install stack. Only worth it if both Whispers disappoint on clip 3 |

Diarization: `pyannote-community/speaker-diarization-community-1` — the **ungated community mirror** of pyannote community-1 (the official repo sits behind a signup form; the mirror is the same CC-BY-4.0 weights, anonymously downloadable, verified `gated: false`). No Hugging Face account, token, or form anywhere in this pipeline. Run once per clip, merged into every model's transcript by overlap.

## Setup — Windows 11, one line at a time

Everything happens in **PowerShell**: press the Windows key, type `powershell`, press Enter. A blue-ish window with a blinking cursor opens — every command below gets typed (or pasted with right-click) there, followed by Enter.

**1. Install ffmpeg** (the audio converter the script uses to turn m4a files into the wav format the models want):

```
winget install --id Gyan.FFmpeg
```

`winget` is Windows 11's built-in app installer; this downloads ffmpeg and registers it so other programs can find it ("on PATH" means exactly that — findable by name from any folder).

**2. Close PowerShell and open a new one** (the "findable by name" registration only applies to windows opened *after* the install). Then confirm it worked:

```
ffmpeg -version
```

Success looks like several lines of version text. "ffmpeg is not recognized" means step 1 or the restart didn't take.

**3. Check whether Python is installed:**

```
python --version
```

If it prints something like `Python 3.12.x` → skip to step 5. If it prints nothing, errors, or **opens the Microsoft Store** (a Windows quirk — the `python` command is a Store shortcut until real Python exists), do step 4.

**4. Install Python** (only if step 3 failed):

```
winget install --id Python.Python.3.12
```

Then close PowerShell, open a new one, and repeat step 3 until it prints a version.

**5. Move PowerShell into this folder.** Syncthing has already put `tutoring-bakeoff` on this PC inside the vault copy. In PowerShell type `cd ` (c, d, space — don't press Enter yet), then find the `tutoring-bakeoff` folder in File Explorer and **drag the folder onto the PowerShell window** — its full path appears after your `cd `. Now press Enter. The prompt line should now end with `tutoring-bakeoff>`.

**6. Make the clips folder:**

```
mkdir clips
```

Then, in File Explorer, copy the five `.m4a` recordings into the new `clips` folder.

**7. Allow PowerShell to run local scripts** (a one-time Windows safety default; the next step's activation is technically a script):

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Answer `Y` if asked. This permits locally-created scripts only, for your user only.

**8. Create a virtual environment** (a private sandbox folder so everything we install stays inside `tutoring-bakeoff` and touches nothing else on the PC):

```
python -m venv venv
```

**9. Activate the sandbox:**

```
.\venv\Scripts\Activate.ps1
```

The prompt now starts with `(venv)` — that's how you know installs go into the sandbox. **Any time you open a new PowerShell window to work on this, redo steps 5 and 9** (just those two).

**10. Install PyTorch with GPU support** (~3 GB download; the `cu126` part selects the CUDA build, which is what makes the 4090 do the work instead of the CPU):

```
pip install torch --index-url https://download.pytorch.org/whl/cu126
```

If this errors, the front page of pytorch.org shows the current version of this exact line (pick: Stable / Windows / Pip / Python / CUDA).

**11. Install the rest** (the two transcription engines and the diarizer):

```
pip install faster-whisper transformers accelerate pyannote.audio
```

**12. Confirm the GPU is visible:**

```
python -c "import torch; print(torch.cuda.is_available())"
```

Must print `True`. If `False`, step 10 installed the CPU build — tell jep.

## Run

```
python bakeoff.py --audio-dir clips --out results
```

First run downloads ~8 GB of models (one-time, cached); the transcription itself is a few minutes total on the 4090. Progress prints as it goes. When it finishes, run the second pass, which measures how much VAD (an is-anyone-speaking filter) tames the silence-minute hallucinations:

```
python bakeoff.py --audio-dir clips --out results-vad --vad
```

**VAD is off in the first run on purpose** — clip 5's silent minute is a hallucination trap and we want to watch each model fall into it (or not) before deciding whether VAD belongs in the final pipeline.

## Judging (bring results back to jep)

The `results/` folder is created inside `tutoring-bakeoff`, so Syncthing carries it back to the laptop on its own — just tell jep it's done. Judging = each clip's `COMPARE.md` against the scripts:

- **Clips 1–2** — sanity floors: both models should be near-perfect in their home language.
- **Clip 3** — the decider: embedded English words, mid-sentence switches, spelled letters (C-A-T), mixed counting. Does forced-`he` ivrit mangle the English islands? Does stock large-v3 mangle the Hebrew matrix?
- **Clip 4** — graceful degradation: childish mispronunciations, singing, 5s overlap, whisper, distance.
- **Clip 5** — diarization truth (2 speakers? clean turns through the position swap?) and the silence-minute hallucination check.

Winner becomes the `lesson-transcribe` pipeline. Caveat carried from the design: sister ≠ 9-year-old — revalidate on real lesson-one audio once consent and the transparency conversation have happened.
