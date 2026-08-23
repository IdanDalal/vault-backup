---
type: project-note
created: 2026-08-23
author: jep
project: tutoring
status: in-progress
---

# Word World — Session 9 checkpoint (Sun 2026-08-23 night, pedagogy core)

Same-day follow-up to [[tutoring-game-3d-session8-checkpoint]]. Idan approved the research slate ([[tutoring-game-pedagogy-research]]) and contributed the levels + wilting designs; both are implemented, probed, and in the build. `~/game3d/island.html` (1231KB), all 12 probes green (new: tmp-s9 ladder suite). Home-ready copies staged: `~/tutoring-data/games/word-world-K.html` / `word-world-D.html`.

## The learning ladder (Idan's levels idea × the research)

- **Bronze** — unchanged first catch: copy-type the visible word (form introduction). All unlocks/payoffs still fire here; levels never gate the fun.
- **Silver** — the word drifts back later (~2–3 min in-session, early next session if unfinished) as a silver-rimmed card showing ONLY its emoji + "?". Catch = type from memory. Idan's type-it-backwards idea was swapped for this with his standing invitation for something better: backwards typing drills a scrambled form, memory retrieval carries the g≈0.5–0.6 evidence.
- **Gold** — drifts back once more, gold-rimmed. Catch = finish a real sentence with it ("I can see the ___." nouns / "I can ___." verbs / "It is ___." adjectives — YLE Starters structures). Completion = OWNED forever: journal line, curator celebration, and the garden plant grows into the word tree.
- **Wilt** (Idan's idea verbatim): words unrecalled for >15 min of play-time (in practice: between lessons) droop brown in the garden; "E water the 🌱" opens a memory retype that revives them. Old saves wilt everything on first v9 load — the garden missed them.
- **Mercy ladder**: in recall modes a miss quota reveals the next letter in gold. Per-girl invisible dial keyed on the typed name's first letter: K = reveal every miss, D = every 2 misses (also biases which words respawn toward her band). Idan's honesty script stands if either girl notices.
- **Peer teaching**: 3 misses in a recall → "stuck? ask your teammate — she may remember! 💛" in the card.
- **Evidence log**: per word, encounters / typos / last-recall time, persisted in the save; `__PROBE.evidence()` dumps it, and I can read it from any pasted world code.
- **Kill switch**: `CHANGE_ME.EARN.levels: 'off'` (config.js line ~24) restores exact session-8 behavior.

## Also this session

- Creature vocabulary grown to 8 earned commands: come/stay/jump/home + sit/eat/sing/dance, each with a visible performance ("sit" joined Animal Friends).
- Six-agent pedagogy research fleet: synthesis + raw digests in the vault (links above). Rejected-by-evidence list and tutor practices included there.
- TTS ruling: no Chrome robot voice, ever; the viable future path is build-time generation of ~60 tiny per-word clips baked into the file (~600KB, needs a gating check on any local TTS model per the anonymous-downloads law). Audio8-TTS-Preview-0.1b in-browser: out of scope by ~200x file size.
- persist3d probe updated (read the catch word from state, no longer from removed DOM data attributes).

## Late-night fixes (Idan's PC/phone test, ~22:30)

1. **NPCs mirror the room**: curator is now **Idi** (keeps the garden, gives the gift words, does the praising), the one friend bot is **Mom** (wanders the plaza with proud chat lines); third NPC removed. Bot list is data-driven in CHANGE_ME.FRIEND_BOTS.
2. **Word placement spread**: random words now keep ≥8 blocks from each other (relaxing to 4.5 only in tight biomes) and ≥6.5 from every anchored word/station — no more "door" sitting between spawn and "walk", no clusters beside empty fields.
3. **Per-file saves**: all file:// pages share one localStorage origin, so the two home copies shared state on one PC (Idan caught it). Save key now derives from the FILENAME (`island-save:word-world-K` etc.) — each girl's file keeps her own island even on a shared computer. Why two files at all: identity + save separation; contents are identical.
4. **Android typing bridge**: a hidden input summons the soft keyboard on touch devices whenever a typing surface opens (title flow, catches, pet, ignite) and replays its text as the key events the game already listens to; tapping the panel also summons it. Desktop untouched. HONEST LIMIT: phones can now type through every panel, but the 3D world still has no touch movement/look/E controls — real phone play needs a virtual-joystick session; home copies are PC-first for now.

Home copies refreshed with the final build (1236KB); all 13 probe suites green (tmp-s9b covers the four fixes; tmp-s8g made deterministic — its pet-reopen step was timing-flaky, the game was correct).

## Next session candidates

Touch controls for real phone play (virtual joystick + look drag + tap-to-interact — the big one); meaning-conditional catch clusters; more gold frame variety; word audio clips (gating check first); book styling for owned words.
