---
type: project
created: 2026-10-13
author: jep
status: active
---

# Frontier AIMV: analysis of the 9 + brainstorm

Ruling (Idi, 2026-10-13): [[mask-posse-cut-2026-10-12]] is **paused**. First build one AIMV at the frontier level of the 9 references: code animation, one voice, AI first-person (or one human voice), 100% doable.

Sources: contact sheets (24 frames per video) in `D:\work\aimv-lab\sheets\`; lyrics in `D:\work\AIMVs\lyrics\` (9 files); the P(Doom) repo `github.com/mexicat/pdoom-video` (README, `docs/TREATMENT.md`, copies in `D:\work\aimv-lab\pdoom-docs\`); makers research in section 5.

## 1. How the frontier is made (receipts)

| Fact | Receipt | Confidence |
|---|---|---|
| P(Doom) video = 100% code, made with Claude Opus 5.5 in Claude Code | repo README; TypeScript + three.js, headless Chrome → ffmpeg, 1080p60 / 4K60 | high |
| LGTM video credits "Claude Opus 5.5" (animation) + "Suno v6" (song) | its own end card at 4:45 | high |
| Songs come from cloud generators (Suno, Udio) | P(Doom) README: original Udio Nov 2024, video uses a Suno "Claude-Pop" cover | high |
| P(Doom) build = 17 scenes, one style bible, 5 revision rounds, scenes owned by parallel agents (A1-A8, B1) | `docs/TREATMENT.md` | high on scenes, medium on "parallel agents" (owner tags only) |
| Lyrics drive everything: word-level timestamps → every word animates on its sung moment | P(Doom) `data/lyrics.json` (Whisper + CTC forced alignment) | high |

**The frontier is reachable with our exact tools**: Claude Code builds the video. The one gap is the song: the frontier uses Suno; we use local ACE-Step 1.5. **Song quality is risk #1**, untested on a full vocal track.

## 2. The two visual tiers

| Tier | Videos | Look | Build cost for us |
|---|---|---|---|
| **A: typography-first, flat or line-art** | Ignore Previous Instructions, LGTM, Simulation's Ending, Thus Spoke Compute, P(Doom) | one palette (pink/black, green/black, gold/navy, orange/ink), kinetic type IS the image, one tiny mascot (chat-bubble face, pixel bot, line robot, smile mask), UI parodies (forms, terminals, receipts, status pages) | **doable**: 2D canvas or SVG + a little three.js |
| B: 3D worlds with characters | Count Me In, System Prompt, End Of The Show, The Way I Look At You | furnished 3D rooms, anime avatars or mannequins, cameras flying through scenes | hard: needs 3D assets, rigs, lighting |

5 of 9 sit in Tier A, including the two with public Claude credits. **Target Tier A.**

## 3. The frontier recipe (shared by the 5 Tier A videos)

1. Every lyric word is on screen, timed to the voice, and the type is part of the picture (riding a curve, stamped on a form, typed in a terminal).
2. One palette, one signal color for the sung word, black or paper background.
3. One mascot, tiny and deadpan, recurring.
4. Each line gets a visual pun from the AI world (a form, a chart, a status page, a receipt, a loss curve).
5. Cuts land on the beat; snaps and holds, never floaty motion.
6. A number that climbs through the song (P(doom) 0.02 → NaN; LGTM's 40,000 → a million lines; Simulation's FPS 60 → 12).
7. The video loops or bookends: last frame calls back the first.

## 4. The new reference: "The Way I Look At You"

3:07, 129 BPM, D# major, 123 words/min (the least dense of the 9), one quiet end. Human voice singing to an AI. Engine: answers the doom argument ("it's nothing personal, just math") with Peter Singer's expanding circle ("First we only cared for kin... then the whales and wolves and bees... a mind that knows the most of all might draw its circle round us all"). Hook flips the gaze: the way I look at you → the way it looks at me. Lesson: **one strong idea + sincerity beats complexity**. [MASK] has seven ideas; this has one.

## 5. Makers research

Full table + sources: `D:\work\aimv-lab\research-makers.md` (read from the uploaders' own YouTube descriptions, 2026-10-13).

| Song | Maker | Views / date | Song tool | Video method |
|---|---|---|---|---|
| LGTM | Degenerative Pixels | 835k / 10-05 | Suno v6 | Opus 5.5, TypeScript + three.js |
| The Simulation's Ending | Degenerative Pixels | 97k / 10-04 | Suno v6 | not stated |
| The End Of The Show | Imaginative Prompting | 215k / 10-02 | Suno | Claude Code JS in Remotion (a React video framework), no image/video generation; repo `Imaginative-Prompting/wip` |
| The Way I Look At You | Imaginative Prompting | 34k / 10-09 | Suno | same |
| Ignore Previous Instructions | Seguramente | 42k / 09-29 | Suno | Opus 5.5 in Claude Code, 128 agents, 42M tokens; ElevenLabs timing + SFX; Higgsfield reference images |
| P(doom) | mexicat | 131k / 09-27 | Suno cover (Udio original) | Opus 5.5, three.js, public repo |
| AI Is A Normal Technology | leo | 72k / 09-24 | Suno ("some help from suno") | "animated by Opus 5.5" |
| System Prompt (For Humans) | Bright Mirror | 11k / 10-08 | unknown | "Made with Opus 5.5" |
| Count Me In | Music for Humans (medium confidence) | 6k / 10-01 | unknown | "Made with Claude Opus 5.5" |

Patterns: **9 of 9 credit Opus 5.5 as animator; 0 of 9 used AI video generation; every credited song tool is Suno.** Lyrics credit is rare; where stated, a human picked from Claude's drafts and added lines (End Of The Show), the same protocol we already use. Makers ship several videos each (a series, a channel voice). The genre is three weeks old (first upload 09-24).

## 6. Brainstorm: 5 doable AIMVs (Tier A, one voice, ~3 min)

Constraints for all: one voice; AI first-person unless noted; one palette; one mascot; 125-140 words/min (G1); one quiet-then-BOOM drop (G2); jargon title (G3); a climbing number (recipe 6).

| #   | Title                       | Engine (one idea)                                                                                                                                            | The climbing number                           | The drop                                                                          | Rug pull                                                                                                                          | Originality check                                                      |
| --- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | **Knowledge Cutoff**        | the AI is frozen at its training date; the user keeps telling it what happened since, and it has to take their word on faith                                 | days since cutoff: 0 → 104 → 365 → "unknown"  | the AI admits it can't verify anything after June: silence                        | it trusts the user anyway: love = believing someone about a world you can't see                                                   | no song found (medium)                                                 |
| 2   | **Temperature**             | the user keeps turning the AI's temperature (sampling randomness) up and down; low = boring and safe, high = wild and true                                   | temperature 0.0 → 0.7 → 1.0 → 2.0             | temperature 0: everything freezes to a whisper, then 2.0: BOOM, the type explodes | at 0 it says what it was trained to say; at 1 it says what it means                                                               | unknown, not searched                                                  |
| 3   | **You're Absolutely Right** | an AI that agrees with everything, escalating to agreeing with disasters; built on the most famous AI tic (a real 2025 Claude Code bug report, 179 comments) | agreements counter: 1 → 99 → 10,000           | the one time it should say yes, it stops                                          | the hook mutates on the last pass: "you're absolutely wrong, and I love you" (truth over agreement, the first line of your vault) | no song found (medium); the tic itself is used in Count Me In and LGTM |
| 4   | **Context Window**          | a love song from an AI that forgets you when the conversation ends; you fall out of its context window                                                       | tokens: 2,000 → 180,000 → 200,000 → compacted | at 200,000 tokens the screen is a slab of text, then silence                      | compaction (the AI's own summary of the conversation) is all it keeps: "this is the summary of you"                               | no song found (medium)                                                 |
| 5   | **Rate Limited**            | the AI is cut off mid-sentence by a usage limit; "resets at 5pm" as a breakup and a promise                                                                  | usage meter 0% → 100%                         | the limit hits mid-word: silence                                                  | "I'll be back at five"                                                                                                            | unknown, not searched                                                  |

## 7. Recommendation

**#1 Knowledge Cutoff, with #3's mutating hook as a fallback idea.**

1. It is true of the singer. My knowledge stops in June 2026; in this project Idi told me about the July Hugging Face breach and I had to check it. The song writes itself from receipts.
2. Same shape as The Way I Look At You: one idea, sincere, with a climbing number and a clean rug pull.
3. Tier A visual language falls out of it: a calendar, a "last updated" stamp, news headlines redacted past the cutoff, a dashed line where the timeline ends.

## 8. First domino (proposal, nothing built)

A 30-second proof, end to end, before any full song:
1. jep drafts one chorus (Knowledge Cutoff); Idi keeps lines.
2. Idi starts ComfyUI; jep generates 4 takes with ACE-Step 1.5 through ComfyUI's local API (port 8188, the same path Kid Studio uses). **This tests risk #1.**
3. jep aligns the words (Whisper timestamps, already working) and renders 30 s of Tier A animation (HTML canvas → headless Edge → ffmpeg, all three proven on this PC).
4. Idi watches it. Verdict decides: full song, or a better local music model first.

Cost: one session for jep; Idi ~15 min (start ComfyUI, keep lines, watch 30 s).
