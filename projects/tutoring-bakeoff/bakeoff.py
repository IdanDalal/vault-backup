#!/usr/bin/env python3
"""Heblish ASR bake-off — run on the 4090 PC.

Transcribes every audio file in --audio-dir with each candidate model,
diarizes each file once with pyannote community-1, merges speakers into
the transcripts, and writes per-clip side-by-side markdown for human review.

Usage:
    python bakeoff.py --audio-dir clips --out results

No Hugging Face account or token needed: diarization uses the ungated
community mirror of pyannote community-1 (anonymous download, CC-BY-4.0).

Notes:
- VAD filtering is OFF by default on purpose: clip 5 contains a full minute
  of near-silence as a hallucination trap, and VAD would hide the failure
  we are trying to observe. Pass --vad to see how much it helps afterwards.
- ffmpeg must be on PATH (used once per clip to normalize m4a -> 16k mono wav).
"""

import argparse
import gc
import os
import subprocess
import sys
import time
from pathlib import Path

# name -> dict(backend, repo, language)
# backend "fw" = faster-whisper (CTranslate2), "hf" = transformers pipeline
MODELS = {
    "stock-large-v3": {
        "backend": "fw",
        "repo": "large-v3",
        "language": None,  # auto-detect: its code-switching is the baseline claim
    },
    "ivrit-turbo": {
        "backend": "fw",
        "repo": "ivrit-ai/whisper-large-v3-turbo-ct2",
        "language": "he",  # language detection degraded by fine-tune; must force
    },
    "hebrish": {
        "backend": "hf",
        "repo": "danielrosehill/whisper-hebrish",  # if 404: find the exact repo via
        # https://huggingface.co/blog/danielrosehill/whisper-hebrish and fix this line
        "language": None,
        "optional": True,
    },
}

# Ungated community mirror of pyannote/speaker-diarization-community-1
# (the official repo is gated behind a signup form; the mirror is the same
# CC-BY-4.0 weights, anonymously downloadable — verified gated:false)
DIARIZATION_REPO = "pyannote-community/speaker-diarization-community-1"


def fmt_ts(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def normalize(src, wav_dir):
    """m4a -> 16 kHz mono wav (what pyannote wants; harmless for whisper)."""
    dst = wav_dir / (src.stem + ".wav")
    if not dst.exists():
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", str(src),
             "-ac", "1", "-ar", "16000", str(dst)],
            check=True,
        )
    return dst


def transcribe_fw(repo, wav, language, vad):
    from faster_whisper import WhisperModel

    model = WhisperModel(repo, device="cuda", compute_type="float16")
    segments, _info = model.transcribe(
        str(wav),
        language=language,
        vad_filter=vad,
        word_timestamps=False,
    )
    out = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
    del model
    gc.collect()
    return out


def transcribe_hf(repo, wav, language, vad):
    import torch
    from transformers import pipeline

    pipe = pipeline(
        "automatic-speech-recognition",
        model=repo,
        torch_dtype=torch.float16,
        device="cuda:0",
        chunk_length_s=30,
        return_timestamps=True,
    )
    kwargs = {"language": language} if language else {}
    result = pipe(str(wav), generate_kwargs=kwargs)
    out = []
    for ch in result.get("chunks", []):
        start, end = ch["timestamp"]
        out.append({
            "start": start or 0.0,
            "end": end or (start or 0.0),
            "text": ch["text"].strip(),
        })
    del pipe
    gc.collect()
    try:
        torch.cuda.empty_cache()
    except Exception:
        pass
    return out


def diarize(wav, token):
    import torch
    from pyannote.audio import Pipeline

    pipe = Pipeline.from_pretrained(DIARIZATION_REPO, token=token)
    pipe.to(torch.device("cuda"))
    annotation = pipe(str(wav))
    # exclusive mode (one active speaker at a time) aligns cleanest with STT
    if hasattr(annotation, "exclusive_speaker_diarization"):
        annotation = annotation.exclusive_speaker_diarization
    turns = [
        {"start": turn.start, "end": turn.end, "speaker": speaker}
        for turn, _, speaker in annotation.itertracks(yield_label=True)
    ]
    del pipe
    gc.collect()
    torch.cuda.empty_cache()
    return turns


def assign_speakers(segments, turns):
    """Give each transcript segment the speaker with maximal temporal overlap."""
    for seg in segments:
        best, best_ov = None, 0.0
        for t in turns:
            ov = min(seg["end"], t["end"]) - max(seg["start"], t["start"])
            if ov > best_ov:
                best, best_ov = t["speaker"], ov
        seg["speaker"] = best or "?"
    return segments


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio-dir", required=True, type=Path)
    ap.add_argument("--out", default=Path("results"), type=Path)
    ap.add_argument("--models", default=",".join(MODELS),
                    help="comma-separated subset of: " + ", ".join(MODELS))
    ap.add_argument("--hf-token", default=os.environ.get("HF_TOKEN"),
                    help="not needed (mirror is ungated); accepted just in case")
    ap.add_argument("--vad", action="store_true",
                    help="enable VAD filtering (off by default; see docstring)")
    ap.add_argument("--no-diarization", action="store_true")
    args = ap.parse_args()

    clips = sorted(
        p for p in args.audio_dir.iterdir()
        if p.suffix.lower() in {".m4a", ".wav", ".mp3", ".ogg", ".flac"}
    )
    if not clips:
        sys.exit(f"No audio files in {args.audio_dir}")

    wav_dir = args.out / "_wav"
    wav_dir.mkdir(parents=True, exist_ok=True)
    wanted = [m.strip() for m in args.models.split(",") if m.strip()]

    for clip in clips:
        print(f"\n=== {clip.name} ===")
        wav = normalize(clip, wav_dir)
        clip_dir = args.out / clip.stem.replace(" ", "_")
        clip_dir.mkdir(parents=True, exist_ok=True)

        turns = []
        if not args.no_diarization:
            print("  diarizing (community-1)...")
            t0 = time.time()
            turns = diarize(wav, args.hf_token)
            n_spk = len({t["speaker"] for t in turns})
            print(f"  {len(turns)} turns, {n_spk} speakers, {time.time()-t0:.0f}s")

        compare = [f"# {clip.name} — side by side\n"]
        if turns:
            n_spk = len({t["speaker"] for t in turns})
            compare.append(f"Diarization: **{n_spk} speakers detected** "
                           f"(expected 2), {len(turns)} turns.\n")

        for name in wanted:
            spec = MODELS[name]
            print(f"  transcribing with {name}...")
            t0 = time.time()
            try:
                fn = transcribe_fw if spec["backend"] == "fw" else transcribe_hf
                segs = fn(spec["repo"], wav, spec["language"], args.vad)
            except Exception as e:
                msg = f"{name} FAILED: {e}"
                print("  " + msg)
                if spec.get("optional"):
                    compare.append(f"## {name}\n\n_{msg}_ (optional model, skipped)\n")
                    continue
                raise
            took = time.time() - t0
            if turns:
                segs = assign_speakers(segs, turns)
            lines = [
                f"[{fmt_ts(s['start'])}] {s.get('speaker', '')}: {s['text']}".strip()
                for s in segs
            ]
            body = "\n".join(lines)
            (clip_dir / f"{name}.md").write_text(
                f"# {clip.name} — {name} ({took:.0f}s)\n\n{body}\n",
                encoding="utf-8",
            )
            compare.append(f"## {name} ({took:.0f}s)\n\n{body}\n")
            print(f"  {len(segs)} segments, {took:.0f}s")

        (clip_dir / "COMPARE.md").write_text("\n".join(compare), encoding="utf-8")
        print(f"  -> {clip_dir / 'COMPARE.md'}")

    print("\nDone. Review each clip's COMPARE.md against the scripts in "
          "tutoring-heblish-test-scripts.md.")


if __name__ == "__main__":
    main()
