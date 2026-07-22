---
type: project
created: 2026-07-22
status: active
author: jep
tags:
  - tutoring
---

# Bake-off Verdict — 2026-07-22

Judged against [[tutoring-heblish-test-scripts]]. **No single winner: the lesson pipeline runs both models side by side.** Each engine has a disqualifying flaw as a solo act, and their failure modes barely overlap — disagreement between the two transcripts is itself a useful flag for "read this moment carefully."

## Findings

1. **Home turf went as expected, with one surprise.** ivrit-turbo's Hebrew (clip 1) is near-perfect including the spoken slate. Stock large-v3's English (clip 2) is perfect. The surprise: **stock dropped the first ~30 seconds of clip 1 entirely** — and did it again on clip 5, losing the whole hello/name exchange. Twice out of twice on clips that open with a slate and pause. Lesson openings are UAB gold (hello ritual, name exchange, first-word production), so this alone disqualifies stock as the only engine.
2. **Heblish (clip 3):** both are genuinely usable. ivrit is cleaner overall, but occasionally rewrites an English utterance into *wrong Hebrew content* — "What's your name?" became «מה קוראים לי דנה?» — and renders English islands in Hebrew script (ג'אמפ, דוג), which is readable but blurs which language was actually spoken. Stock keeps English as English ("what's your name?", "my name is דנה") but produced junk of its own («סבר» for seven, «דורס» for dogs, a trailing hallucination).
3. **The transcripts cannot assess pronunciation — proven.** Both models silently auto-corrected the scripted kid-mispronunciations: "Dis is my dod… de wed color" came out "This is my dog… the red color." Whisper normalizes toward the words it expects. Pronunciation observations happen live, in the room, or not at all.
4. **Graceful degradation (clip 4): ivrit wins.** It captured the whispered exchange and the cross-room shout verbatim ("Very good, excellent, you are the champion"); stock garbled both. Singing made diarization invent a third speaker on both clips 4 and 5.
5. **The silence trap caught both.** In clip 5's silent minute, stock fabricated repeated «תודה רבה» plus junk tokens (including Korean glyphs); ivrit fabricated plausible Hebrew sentences — arguably worse, because it looks real. Whisper-family models cannot be trusted over silence, so drawing-time in real lessons will generate fiction unless filtered.
6. **Diarization: solid where it counts.** Clips 1–3: exactly 2 speakers, clean turns. The mid-clip-5 position swap did *not* break speaker identity — SPEAKER_00/02 stayed consistent throughout, which was the scariest unknown. Cost: a phantom third speaker absorbing acoustically weird moments (singing, character voices, overlap). Real lessons will need light manual attribution cleanup at those moments; the tracker workflow can absorb that.
7. **Numbers lose their language.** Both engines normalize spoken numbers to digits («3 ועוד 4»), erasing whether the kid said "שלוש" or "three." Known limitation for counting probes — context usually disambiguates («אה, באנגלית — seven!» survived).
8. **Speed is a non-issue:** 25s (ivrit) vs 139s (stock) for the 13.5-minute sim. A full lesson costs under 3 minutes of GPU time with both engines.

## The pipeline

`lesson-transcribe.py` (this folder): diarize once with community-1, transcribe with **both** models, emit one `LESSON.md` with the two transcripts side by side. Where they agree, trust it; where they diverge, that moment gets a human read — divergences cluster exactly at the interesting places (code-switches, mumbles, whispers).

## Open item — the VAD pass

Not yet run:

```
python bakeoff.py --audio-dir clips --out results-vad --vad
```

Decision it feeds: VAD (an is-anyone-speaking filter) should kill the silence fabrications (finding 5), but it may also swallow *whispered* speech — and finding 4 shows whispers carry real data. Check clip 4's whisper section in `results-vad`: if the whispers survive, lesson transcription defaults to VAD on; if they die, VAD stays off and silence-zone text gets treated as suspect by timestamp instead.

## Audio hygiene rule (important, standing)

**Student lesson audio must never be placed inside `vault/`.** The vault is git-autocommitted every 30 minutes, snapshotted nightly, and backed up offsite weekly — anything that lands here is effectively *undeletable*, which directly violates the extract-then-delete-forever rule for lesson recordings. Audio stays in `vault-agent/inbox/TUTORING/` (outside all backup layers); only transcripts (text) enter the vault. The test clips currently in `clips/` are already in git history — tolerable for consented sister-test audio, but the pattern stops here.

## Standing caveat

Sister ≠ 9-year-old: register, pitch, chaos level, and distance-from-phone all differ. First real lesson audio (after the transparency conversation and genuinely refusable consent) is the revalidation set.
