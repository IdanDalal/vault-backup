---
type: project
created: 2026-11-02
author: jep
status: active
---

# AIMV kit (index)

Harvested 2026-11-02 from Knowledge Cutoff (KC, live https://youtu.be/-g6hYVec1Uo). Grows after every video (rules in [[kit-next-video]]).

> Idi, 2026-11-02: "an exponentially growing "kit" of files/folders/components/elements/blocks/rules/whatever helps us make music videos, and we keep combining them in different ways"

## Files

| file | lines | holds | read when |
|---|---|---|---|
| [[kit-next-video]] | 63 | Idi's 11-02 rulings R1-R5, Phase 1 "line cards" proposal, repo-per-video plan, kit growth rules, open WHATs | first, at the start of the next video |
| [[kit-rulings]] | 236 | every Idi ruling and taste line in 8 domains (verbatim or paraphrase, sourced), jep rules Idi accepted, 16 reversals with both dates | before writing lyrics or a brief |
| [[kit-process]] | 391 | KC's 21 phases (cost, outputs, what worked, what failed), a 16-step reusable pipeline, 96 lessons with rules | planning any phase |
| [[kit-references]] | 257 | 11 reference videos (all with links), what each does well, what KC borrowed and where, credit-line draft, intake checklist | adding a reference; writing credits |
| [[kit-audio-pipeline]] | 239 | song pipeline: models tried, prompt format, takes, auditions, alignment, licences, scripts, Phase 1 audio facts the visuals need | Phase 1 |
| [[kit-engine-components]] | 230 | engine core, helper modules, 67 scenes with their technique, gates/tools, scripts, known limits (file:line pointers) | line cards; build |
| [[kit-open-source-audit]] | 130 | what blocks a public repo of kc-engine and the clean-export steps | before the first public repo |
| [[kit-release-playbook]] | 76 | final render, thumbnail, channel, accounts, upload, posting, close-out | release week |
| [[kit-lexicon]] | ~4,150 | the word kit (Idi R7, 11-02): 252 AI terms, 68 wide; per term senses across 17 life domains, origin, idioms, anchors, pivot lines, music/picture/type enactments, rhymes, ref-song usage; domain clusters (premise seeds); collisions (combination pairs). Source JSON + `lexicon.py` + `SCHEMA.md` in `lexicon/` | before the premise; writing every line |
| [[kit-line-cards]] | ~60 | line card v2 (Idi R8): v1's 10 fields + word layer, thread, public note, roles count | Phase 1 |
| [[kit-repo-per-video]] | ~40 | repo lineage and 8 steps (Idi R9), self-reproducing `new-video.sh` | before the first public repo |
| [[research-mp3-rights-2026-11-02]] | ~170 | mp3 ships (Idi R6): MiniMax texts, other providers, precedent repos, US/Israel law, CC BY 4.0 notice draft | writing the audio licence |
| [[research-brightmirror-2026-11-02]] | ~160 | Bright Mirror's site: 7 songs, 354 sourced line notes in 8 kinds, lyrics page, validator | line cards; release page |

Physical tools: `D:\work\aimv-lab\kit-tools\` (mp4-repair with its README, thumbnail measuring and phone-size previews), `D:\work\aimv-lab\kc-engine\` (engine, gates, render scripts), `D:\work\AIMVs\ours\release\` (thumbnail, banner and header builders).

## Headline findings (one line each, source in the file named)

- 55 of 116 rules were set before any moving picture existed, and 5 early versions (v2-v6) were thrown away [[kit-process]].
- The blind 1-5 panel before art took the floor share from 29 % to 14 %; Idi praised the method [[kit-process]].
- Song choices by ear beat jargon tables; MiniMax's own caption format fixed the pace, and the final song needed no audio edits [[kit-process]], [[kit-audio-pipeline]].
- Three of the five bar references share mexicat's (Giacomo Magnanini's) MIT engine, the one KC forks [[kit-references]].
- The final song prompt came from the "like Ignore Previous Instructions" audition: 144 BPM in G# major, that video's measured tempo and key [[kit-audio-pipeline]].
- Raw Whisper word times run ~0.17 s early inside lines and ~0.33 s at line starts; forced alignment plus a correction rule fixed them [[kit-audio-pipeline]].
- Most reusable parts: adaptive per-tile motion-blur renderer with workers and disk spool; the typography kits (`_kc-type`, `-typegeo`, `-typeglyph`); the gate suite (check, lifecycle, clarity, avsync) [[kit-engine-components]].
- Public-repo blockers: the song mp3 (licence silent on output ownership), a 166-commit history holding it and the internal notes (publish a fresh export), 83 files with private Windows paths; no secrets found [[kit-open-source-audit]].
- One 8.5 h single-file 4K render died 66 frames from the end; render in chunks [[kit-release-playbook]].

## Rulings, 2026-11-02 second conversation (detail in [[kit-next-video]] R6-R11)

1. mp3 ships in the public repo (R6); research confirms no MiniMax text restricts it; notice = CC BY 4.0 + disclosure + credit.
2. Premise waits for the lexicon (R7); lexicon built 11-02, premise seeds in its domain-clusters section.
3. Line cards: keep all 10 fields, build on them with the lexicon (R8) → [[kit-line-cards]].
4. One repo per video (R9) → [[kit-repo-per-video]].

## Open WHATs for Idi

1. Licence-holder name (recommend "Chorus of Minds") and GitHub home (recommend a `chorusofminds` organization).
2. The premise, after his timestamped notes on the new refs.
