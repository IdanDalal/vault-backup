#!/usr/bin/env python3
"""lesson-transcribe — the production pipeline chosen by the bake-off (see VERDICT.md).

Diarizes each recording once (pyannote community-1, ungated mirror), transcribes
with BOTH engines (stock large-v3 + ivrit-turbo), and writes one LESSON.md per
recording with the two transcripts side by side. Where the engines agree, trust
it; where they diverge, read that moment carefully — divergences cluster at
code-switches, mumbles, and whispers, which is exactly the UAB-relevant stuff.

Usage (on the 4090 PC, venv active):
    python lesson-transcribe.py --audio-dir <folder with lesson audio>

Audio hygiene: lesson audio must live OUTSIDE the vault (vault-agent/inbox/...),
because the vault's backup layers make deletion impossible. Transcripts go in
the vault; audio gets deleted after extraction. This script prints a deletion
reminder and offers --delete-audio to do it in the same run.

VAD is OFF by design (VERDICT.md, resolved 2026-07-22): the VAD pass proved it
kills whispered speech in both engines, and whispers are real lesson data.
Silence hallucinations are handled at read time instead: segments overlapping
no diarization turn are flagged as probable fabrications, and the rest are
caught by cross-engine divergence. --vad remains available for experiments.
"""

import argparse
import time
from pathlib import Path

from bakeoff import (MODELS, assign_speakers, diarize, fmt_ts, normalize,
                     transcribe_fw)

ENGINES = ["stock-large-v3", "ivrit-turbo"]  # both, per VERDICT.md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio-dir", required=True, type=Path)
    ap.add_argument("--out", default=Path("transcripts"), type=Path)
    ap.add_argument("--vad", action="store_true",
                    help="enable VAD (only after the whisper-survival check passes)")
    ap.add_argument("--delete-audio", action="store_true",
                    help="delete each source recording after its transcript is written")
    ap.add_argument("--no-condition", action="store_true",
                    help="disable condition_on_previous_text. Use on any recording "
                         "longer than ~10 min: it removes the feedback path that "
                         "turns one bad window into a repetition loop.")
    ap.add_argument("--speakers", type=int, default=None,
                    help="how many people were in the room. Unconstrained clustering "
                         "merged two sisters into one label on 2026-08-10; pass the "
                         "true count (tutor included) to force the split.")
    ap.add_argument("--prompt", default=None,
                    help="vocabulary seed for both engines: planted words, student "
                         "names, expected English. Without it, a Hebrew-locked pass "
                         "renders English islands as Hebrew noise.")
    args = ap.parse_args()

    clips = sorted(
        p for p in args.audio_dir.iterdir()
        if p.suffix.lower() in {".m4a", ".wav", ".mp3", ".ogg", ".flac"}
    )
    if not clips:
        raise SystemExit(f"No audio files in {args.audio_dir}")

    wav_dir = args.out / "_wav"
    wav_dir.mkdir(parents=True, exist_ok=True)

    for clip in clips:
        print(f"\n=== {clip.name} ===")
        wav = normalize(clip, wav_dir)

        print("  diarizing...")
        turns = diarize(wav, token=None, num_speakers=args.speakers)
        n_spk = len({t["speaker"] for t in turns})
        if args.speakers and n_spk != args.speakers:
            print(f"  WARNING: asked for {args.speakers} speakers, got {n_spk}")

        doc = [f"# Lesson transcript — {clip.name}\n",
               f"Diarization: {n_spk} speakers, {len(turns)} turns. "
               "Reminders: transcripts cannot assess pronunciation (engines "
               "auto-correct it); ⚠ lines overlap no detected speech and are "
               "probably invented; where the two engines diverge over a quiet "
               "stretch, trust neither.\n"]

        for name in ENGINES:
            spec = MODELS[name]
            print(f"  transcribing with {name}...")
            t0 = time.time()
            segs = transcribe_fw(spec["repo"], wav, spec["language"], args.vad,
                                 condition=not args.no_condition,
                                 prompt=args.prompt)
            segs = assign_speakers(segs, turns)
            body = "\n".join(
                f"[{fmt_ts(s['start'])}] "
                + ("⚠ no speech detected here — probable hallucination: "
                   if s["speaker"] == "?" else f"{s['speaker']}: ")
                + s["text"]
                for s in segs
            )
            doc.append(f"## {name}\n\n{body}\n")
            print(f"  {len(segs)} segments, {time.time()-t0:.0f}s")

        out_md = args.out / f"{clip.stem.replace(' ', '_')}.LESSON.md"
        out_md.write_text("\n".join(doc), encoding="utf-8")
        print(f"  -> {out_md}")

        if args.delete_audio:
            clip.unlink()
            wav.unlink()
            print(f"  deleted {clip.name} (and its wav)")

    if not args.delete_audio:
        print("\nExtract-then-delete rule: once the tracker entries are pulled "
              "from these transcripts, delete the recordings (and transcripts/_wav):")
        for clip in clips:
            print(f"  {clip}")
    else:
        # the wav copies of undeleted runs may still linger from earlier passes
        print("\nSource recordings deleted. Check transcripts/_wav for leftovers.")


if __name__ == "__main__":
    main()
