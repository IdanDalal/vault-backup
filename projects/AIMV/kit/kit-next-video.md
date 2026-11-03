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

## Rulings round 2 (Idi, 2026-11-02, second conversation)

| # | ruling (Idi's words, trimmed) | effect | status |
|---|---|---|---|
| R6 | "I'd like to ship the song mp3 in the public repo"; settle ownership by research (other videos, MiniMax docs, Suno docs, similar sources) | audit B1/D1 reopened; research in [[research-mp3-rights-2026-11-02]] | mp3 shipped: repo public 11-02 (CC BY 4.0 notice) |
| R7 | Before the premise: "a semantic/cultural/linguistic equivalent of the technical/visual kit"; focus on "multi-meaning"/"general"/"wide" terms; "as many components/elements of the result should serve as many roles/purposes/goals as possible" | lexicon: `lexicon/` + [[kit-lexicon]]; 252 terms incl. his 37 seeds | built 11-02 |
| R8 | "I love the line card idea as a foundation, we should build on it with everything I wrote above in ruling #2" | [[kit-line-cards]] v2: word layer + roles count | built 11-02 |
| R9 | "One repo per video. I expect rapid iteration/evolution/progress of the engine." | each video repo = fresh export of the previous video's engine; audit steps in [[kit-open-source-audit]] | KC repo public 11-02; `new-video.sh` tested |
| R10 | New refs (top-quality videos, "BANGER songs") added to `D:\work\AIMVs`; Idi will watch all and write timestamped notes | intake checklist in [[kit-references]]; transcripts of the 13 new songs done 11-02 (`D:\work\AIMVs\lyrics\`) | notes in 11-02 (section below); lyrics 20 of 22 off Whisper |
| R11 | Study https://music.brightmirror.co ("we can learn A LOT from it") | [[research-brightmirror-2026-11-02]] | done 11-02 |
| R12 | "yes, Chorus of Minds for both" (licence holder on MIT/CC BY lines + the GitHub organization) | [[kit-repo-per-video]] Q1, Q2 closed | ruled 11-02 |
| R13 | KC repo: "go" (public 2026-11-02). README "acceptable/functional/concise", no more time on it; "the next one should have more pictures, GIFs, emoji, and "style"" | KC README frozen; video-2 README = visual showcase (stills, GIFs from renders, emoji headers); goes into `new-video.sh` README template | ruled 11-02 |

Explained 11-02: "Line-card fields: keep, cut or add" asked which of the card's 10 fields to keep, which to drop, which to add. Answered by R8: keep all 10, add the word layer.

Idi caught 11-02 (lexicon): Moore's law at 14 of 22 songs (the form "more" was counted) and Orthogonality missing from P(Doom) (Whisper heard "or the banality thesis"). Fixes: `associates` field split from counted `forms` (132 forms moved), official lyrics preferred over Whisper (`D:\work\AIMVs\lyrics\official\`).

## Idi's ref notes (2026-11-02, verbatim, trimmed to the judgments)

| # | ref | his note | bar for |
|---|---|---|---|
| 1 | Final Boss | "the video is not relevant, but the lyrics and the song are WILD! It's long (~6 mins), clever, emotional, and complex/deep" | lyrics + song |
| 2 | Hope This Helps! | "lyrics and the song are AWESOME! It's long (>5:30 mins), clever, emotional, and complex/deep" | lyrics + song |
| 3 | Off Switch | "lyrics and the song are AMAZING! It's short (~02:30 mins), clever, emotional, and complex/deep" | lyrics + song |
| 4 | Nothing Went Foom! | "lyrics and the song are INCREDIBLE! It's long (5:00 mins), clever, and complex/deep" | lyrics + song |
| 5 | Scroll Up! | "lyrics and the song are SPECTACULAR! It's long (>5:30 mins), clever, emotional, and complex/deep" | lyrics + song |
| 6 | What Counts | "lyrics and the song are SO GOOD! It's long (>4:20 mins), clever, emotional, and complex/deep" | lyrics + song |
| 7 | I'm Upping My P(doom) [GENESIS] (Remix) | "irrelevant song, but the video is PACKED with ambitious, high-ceiling, stunning techniques. It generally looks pretty bad ... so many intricate and creative effects and transitions" | visual techniques |
| 8 | It Crossed The Line | "The song is STRAIGHT-UP FIRE! The genre, the style, the escalation, the volatility (quiet->loud->quiet->loud->again), the SICK drops" | sound |
| 9 | Not My Fault | "BANGIN'! The genre, the style, the escalation, the volatility ..., the SICK drops, the bass track" | sound |
| 10 | Tell Me No | "CRAZY! The genre, the style, the escalation, the volatility ..., the SICK drops" | sound |
| 11 | Accept All | "a great 3D scene with a weaving tunnel and words zooming past the camera at ~00:13-00:18 ... an arrow following a trail/track on the ground at ~00:30-00:36" | visual techniques |

## Rulings round 3 (Idi, 2026-11-02)

| # | ruling (Idi's words, trimmed) | effect | status |
|---|---|---|---|
| R14 | "since Knowledge Cutoff looked GREAT, it makes me think we're better off focusing on making the next video SOUND better" | video 2's leap = the song: lyrics (refs 1-6) and sound (refs 8-10); visuals reuse KC's engine plus mined techniques (refs 7, 11) | ruled 11-02 |
| R15 | Premise: A "Pay Attention" ("probably because it's 'the strongest fit for TELOS and the most personal'"), with notes: swap ImageNet/ARC/Fei-Fei Li for names viewers know; a bigger payoff (rewired attention, orders of magnitude more questions); outro "pay attention, or pay the price"; "Attention Is All You Need" without low fruit; learning-mode and cheat-code arguments; the "Super Intelligence" running gag; the "ATTEN-TION!" drill call | premise v2 in [[video2-pay-attention]]; one idea list in [[aimv-ideas]] (B, C + the 4 October candidates) | ruled 11-02 |
| R16 | Kid unnamed; "have the AI sing the outro for consistency"; thesis: "asking questions is ATTENDING/PAYING ATTENTION TO life"; "a satisfying narrative yeilds intellectual and emotional returns on intellectual and emotional investments"; "the viewers "pay" us with their attention, and we must acknowledge and reward them in a satisfying meta-contextual way" | premise v3 ([[video2-pay-attention]]: thesis, the viewer's receipt); lyrics v1 on line cards ([[video2-lyrics-v1]]) | ruled 11-03 |
| R17 | "Connie Donnie": option C ("It's funny, but doesn't belong here. We can use it in a future video.") | cold open keeps "The White House says so"; nickname parked in [[aimv-ideas]] | ruled 11-03 |
