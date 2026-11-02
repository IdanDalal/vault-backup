---
type: project
created: 2026-11-02
author: jep
status: active
---

# Lexicon schema (the word kit)

Idi's ruling 2026-11-02 (#2): a semantic/cultural/linguistic kit beside the technical/visual kit; focus on wide, multi-meaning terms, because "as many components/elements of the result should serve as many roles/purposes/goals as possible".

Files: `terms.json` (master list, 252 ids, 4 batches) → `entries/<batch>.json` (one JSON array per batch) → `lexicon.py build` → `../kit-lexicon.md` (rendered view). Gold example: `entries/_example.json` (Attention).

## Entry fields

| field | type | rule |
|---|---|---|
| `id` | string | from `terms.json`, unchanged |
| `forms` | list | every spelling the lyrics might use: plural, verb, adjective, compounds (used for ref-lyric counts) |
| `ai` | object | `sense` (one clause, plain words), `origin` (who/when/what paper or post), `url` (real link or ""), `confidence` high/medium/low |
| `senses` | list | non-AI meanings: `domain` (closed list below), `meaning` (one clause), `phrase` (a real everyday phrase using it). One row per distinct meaning |
| `idioms` | list | fixed phrases people already say |
| `anchors` | list | cultural, historical, fictional anchors: `name`, `what` (one clause), `url` (or "") |
| `pivots` | list | draft lyric lines (≤12 words) true in 2+ senses at once: `line`, `senses` (domains it lights, "ai" counts) |
| `enact` | object | how the medium performs the word: `music` (arrangement/mix move), `picture` (one image that shows 2+ senses), `type` (typography move) |
| `sound` | object | `syllables`, `stress` (CAPS on stressed syllable), `rhymes` (perfect), `slant` |
| `stakes` | list | closed: jobs, wallet, mind, heart, body, state, planet, species (Idi's G13 ladder + heart, body) |
| `registers` | list | closed: tender, funny, ominous, awe, defiant, sad, smug, panicked, hopeful |
| `neighbors` | list | `id` (must exist in `terms.json`), `rel`: part-of, pairs-with, opposite, causes, same-family, rhymes |
| `risk` | string | cliché, overused in refs, hard to decode, factual trap; "" if none |
| `notes` | string | the one observation that makes the term useful |

Closed domain list (17): everyday, body, mind, love, family, school, work, money, law-state, war, faith-myth, sport-games, music, screen, science, nature, craft.

## Computed by `lexicon.py` (agents never fill these)

| field | rule |
|---|---|
| width | distinct domains in `senses` + 1 for the AI sense |
| class | wide = width 8+, mid 5-7, narrow 4 or less (calibrated 2026-11-02: median 7; 4 was the first guess and tagged 243 of 252 wide) |
| medium-native | has a `music` or `screen` sense: the song or the picture can perform it |
| refs | which reference songs' transcripts (`D:\work\AIMVs\lyrics\`, outside the vault) use any form, with counts |
| KC | count in the Knowledge Cutoff lyric |
| collisions | pairs of wide terms sharing 4+ domains beyond everyday: combination candidates |
| domain clusters | per life domain, the wide terms with a sense there: premise seeds |

## Rules

1. Pivot lines are jep drafts. Lyric protocol stands: Idi keeps lines verbatim, jep regenerates the rest.
2. AI senses attribute real sources; a guess is marked `low`.
3. A term changes only with a receipt (kit growth rule 4).
