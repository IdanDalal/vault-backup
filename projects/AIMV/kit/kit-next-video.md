---
type: project
created: 2026-11-02
author: jep
---

# Next video: intake (written 2026-11-02, at the close of Knowledge Cutoff)

Kit index: [[aimv-kit]]. Starts in a new conversation.

## Idi's vision (2026-11-02, verbatim)

> "an exponentially growing "kit" of files/folders/components/elements/blocks/rules/whatever helps us make music videos, and we keep combining them in different ways with different ideas in different circumstances and adding more of them and improving/enhancing/evolving them."

## Rulings (Idi, 2026-11-02)

| # | ruling | effect |
|---|---|---|
| R1 | Open source: "follow Giacomo Magnanini and upload the source code to a github repo" | public repo per video; answers the r/ClaudeAI removal (post lacked Claude's role and process) |
| R2 | "link all the inspirations/references/examples to emphasize the cumulative/co-operative/iterative nature of our process" | description + README credit every reference with its link ([[kit-references]]) |
| R3 | Phase 1: "deliberately crafting lyrics AND their visuals at the same time" | each lyric line is born with its picture; audio-video cohesion planned before the song exists |
| R4 | 5 new reference videos found; Idi adds them to `D:\work\AIMVs` | reference intake before Phase 1 (checklist in [[kit-references]]) |
| R5 | Shorts and TikTok skipped for KC | vertical cutdowns optional per video |

## Proposal: Phase 1 "line cards" (jep; Idi edits)

One card per lyric line, written in the lyrics doc before any song generation:

| field | example (KC hindsight) |
|---|---|
| line | "Then Spain scored in extra time" |
| beat intent | lands on the downbeat of bar N; "scored" held 2 beats |
| picture | the word "scored" flies as a kicked ball along one arc into the net |
| motion verb | kick, arc, land |
| type treatment | letters ride the arc, one framing |
| camera | static wide, push on landing |
| in / out | carries the stadium from the previous line; cuts on "since then" |
| kit parts | type-on-path helper, stadium set, camera push ([[kit-engine-components]]) |
| reference | the technique's source video ([[kit-references]]) |
| risk | needs >= 1.2 s of screen time (KC note 10) |

Flow: cards drafted with the lyrics → song prompt shaped by the cards (section lengths, held words, tempo) → takes generated and auditioned against the cards → word times aligned ([[kit-audio-pipeline]]) → cards re-timed to the real take → build. KC built visuals after the song was locked, so held words, gaps and section lengths were fixed facts the visuals had to fit.

## Proposal: repo per video (jep; Idi edits)

- Public repo from day 1 of the build; clean-repo steps in [[kit-open-source-audit]] (strip reference media, check song licence, ship font licences, keep the MIT notice for the P(Doom) engine).
- README: what the video is, how it was made, Claude's role (agents, briefs, gates, panels), Idi's role (premise, rulings, final calls), credits and every reference linked, how to render.
- PROCESS.md: the passes and rulings as they happen (the vault notes, cleaned of private paths).
- Release posts link the repo; Reddit post explains Claude's role in the first paragraph.

## Kit growth rules (proposal)

1. Every kit item carries: name, what it does, where it lives, provenance (video + date), status (proven / experimental / retired), used-in list.
2. After each release: a harvest pass like 2026-11-02 moves new components, rulings, lessons and references into the kit files.
3. Before each new video: a combine pass picks kit parts per line card; gaps become build tasks.
4. A kit item changes only with a receipt (render, gate output, panel result, Idi ruling).
5. References are first-class: each new reference gets an intake row before it influences anything.

## Open WHATs for Idi (next conversation)

1. The next song's premise.
2. Line-card fields: keep, cut or add.
3. Repo host and name (GitHub account; one repo per video or one engine repo + per-video folders).
