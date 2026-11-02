---
type: project
created: 2026-11-02
author: jep
status: active
---

# Atlas schema (the who/what/where kit, sibling of the lexicon)

Idi's ruling 2026-11-02 (option B): people, companies, institutions, places, events and fictional works the AI world talks about, kept as a sibling shelf of the lexicon, cross-linked both ways.

Files: `atlas.json` (master list, 164 ids, 4 batches) → `atlas/<batch>-pN.json` → `python -I atlas.py build` → `../kit-atlas.md`; then `python -I lexicon.py build` adds atlas back-links to lexicon cards. Gold example: `atlas/_example.json` (Her).

## Entry fields

| field | type | rule |
|---|---|---|
| `id` | string | from `atlas.json`, unchanged |
| `what` | object | `line` (one plain sentence: who or what it is), `asof` (YYYY-MM-DD the facts were checked) |
| `forms` | list | DISTINCTIVE spellings counted in ref lyrics (surname, product, "Skynet"). A name that is also a common word ("Her", "Apple", "Meta") counts only distinctive forms ("Samantha", "iPhone"); leave the common word out |
| `aka` | list | aliases, nicknames, the [MASK] persona names (TRI-lon, AltSam); not counted |
| `receipts` | list | why the AI world talks about it: `claim` (one clause, with the number or date), `url` (primary source where possible), `date`, `confidence` high/medium/low. Web-checked, never from memory |
| `quotes` | list | verbatim only: `text`, `who`, `where`, `url`, `date`. A misquote is worse than none (craft rule: real quotes only) |
| `name_play` | list | puns and double readings of the name: `play`, `how` ("AltSam": Altman read as "alt man") |
| `pivots` | list | draft lyric lines (12 words max) true in 2+ readings: `line`, `readings` (free labels) |
| `visuals` | list | recognizable handles a frame can show (the leather jacket, HAL's red eye); no likeness of a real face as a gag |
| `lexicon` | list | `id` (must exist in `terms.json`), `how` (one clause) |
| `links` | list | `id` (must exist in `atlas.json`), `rel`: works-at, founded, leads, rival, invested-in, made, adapted-from, regulates, measures, located-in, depicts, inspired, same-family |
| `stakes` | list | same closed list as the lexicon |
| `registers` | list | same closed list as the lexicon |
| `risk` | string | defamation, likeness, trademark, staleness, contested facts |
| `notes` | string | the single most useful observation for a lyric or a frame |

Kinds (closed): person, company, lab, institution, place, law, event, work-film, work-tv, work-book, work-game, universe.

## Rules

1. Every receipt and quote is web-checked when written; unverifiable = `low` or left out. Confidence: high = primary source; medium = reliable secondary (a Wikipedia-only receipt caps at medium, applied 2026-11-02); low = unverified.
2. Living people: commentary on public acts with receipts; no invented quotes, no claims about private life.
3. Facts age: the `asof` date is on every card; a card older than 90 days is re-checked before use in a lyric.
