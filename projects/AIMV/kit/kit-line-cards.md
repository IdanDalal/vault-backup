---
type: project
created: 2026-11-02
author: jep
status: active
---

# Line cards v2 (the card each lyric line is born on)

v1 = jep's 10-field proposal in [[kit-next-video]] (2026-11-02). Idi, 2026-11-02 (#3): "I love the line card idea as a foundation, we should build on it" with the lexicon ruling (#2). v2 keeps all 10 v1 fields and adds a word layer from [[kit-lexicon]]. Every field = one job the line does; the card makes the jobs countable.

## Fields

| layer | field | holds | source |
|---|---|---|---|
| word | line | the lyric line | draft; Idi keeps lines verbatim |
| word | terms | 1-3 lexicon ids the line carries | [[kit-lexicon]] |
| word | senses lit | per term, the domains this line activates at once (AI + life senses) | lexicon `senses` |
| word | both readings | the line in plain words per sense: "AI: ... / life: ..." | decodability rule (10-18: every on-screen claim decodable) |
| word | rhyme slot | end word, rhyme family, rung (G17: R4+) | lexicon `sound` |
| word | freshness | ref songs already using the term (0 of 22 = unclaimed) | lexicon `refs` |
| sound | beat intent | bar, downbeat, held words, planned drop | v1 |
| sound | music enactment | how the arrangement performs the term (duck, loop, drop, key change) | lexicon `enact.music` |
| picture | picture | one image that shows 2+ senses at once | v1 + lexicon `enact.picture` |
| picture | motion verb | 1-3 verbs | v1 |
| picture | type treatment | typography move | v1 + lexicon `enact.type` |
| picture | camera | framing and move | v1 |
| picture | in / out | what it inherits from the previous card, what it hands the next | v1 |
| web | callbacks | cards this one echoes or sets up (id + how) | new: connect, contextualize, complement |
| web | thread | 1-2 named motifs this line belongs to; a song holds 5 threads max, 5-15 lines each | Bright Mirror ([[research-brightmirror-2026-11-02]] lesson 5) |
| publish | note | the public note for the lyrics page: `kind` (Story, Reference, Meaning, Wordplay, In the video, Series, Callback, Word origin), `phrase` (exact substring of the line), body 1-3 short paragraphs, https sources | Bright Mirror note schema + its 7 build-check rules (lesson 1); "both readings" becomes the Wordplay note |
| build | kit parts | engine components reused | [[kit-engine-components]] |
| build | reference | source video of the technique | [[kit-references]] |
| build | risk | screen time, decodability, cliché | v1 + lexicon `risk` |
| score | roles | count = senses lit + music enactment (0/1) + picture showing 2+ senses (0/1) + type move tied to a sense (0/1) + callbacks | computed; a diagnostic, never a target to game |

## Example (lexicon-era, hypothetical; premise not chosen)

| field | value |
|---|---|
| line | "Attention is all you need, and you gave me none" |
| terms | attention |
| senses lit | ai (the Transformer paper), love (being noticed), mind (focus) |
| both readings | AI: the mechanism every model runs on / life: a lover who never looked up |
| rhyme slot | "none" → one, done, run, sun; rung R4 |
| freshness | 0 of 22 ref songs; KC 0 |
| beat intent | "none" lands on the downbeat, every stem cut for one beat |
| music enactment | all stems duck except the vocal, then silence on "none" |
| picture | attention-map lines fan from "you" to every word, then go dark |
| motion verb | fan, reach, drop |
| type treatment | "you" scales up, the rest dims; "none" draws with zero weight |
| camera | static, push on "you" |
| in / out | inherits the chat window; hands a black frame to the next card |
| callbacks | sets up the last chorus, where the lines finally reach back |
| kit parts | type kits (`_kc-type`), line renderer, rhythm cut on downbeat |
| reference | the technique's source video, from the intake |
| risk | the paper title is the most used pun in AI culture; the twist ("gave me none") carries it |
| roles | 3 senses + music 1 + picture 1 + type 1 + callback 1 = 7 |

## Flow (v1 flow, with the lexicon in front)

1. Lexicon built → domain clusters and collisions (sections in [[kit-lexicon]]) → premise candidates for Idi.
2. Premise ruled → cards drafted with the lyrics, terms picked from the cluster, roles counted.
3. Song prompt shaped by the cards (section lengths, held words, tempo) → takes → Idi's ear picks ([[kit-audio-pipeline]]).
4. Word times aligned → cards re-timed to the real take → build.
5. Release: cards export to `notes.json` + a lyrics page in the video's repo (click a line, the video jumps there; words light as sung), from timing data the engine already holds (Bright Mirror lesson 3).
