---
type: reference
created: 2026-08-23
author: jep
project: tutoring
status: in-progress
---

# Word World pedagogy — research synthesis (brainstorm working doc)

Six-agent fleet, 2026-08-23. Full digests + all source links: [[tutoring-game-pedagogy-research-digests]]. Companion context: [[tutoring-game-3d-session8-checkpoint]], [[tutoring-operating-principles]]. Status: awaiting brainstorm with Idan; nothing below is implemented.

## Convergent headline findings (multiple agents, strongest evidence)

1. **Retrieval beats copying, decisively.** Copy-typing a visible word is weak-to-NEGATIVE for vocabulary encoding (Barcroft TOPRA, replicated lab series). Typing FROM MEMORY with immediate feedback carries g≈0.5–0.6, one of the best-replicated effects in learning science (3 meta-analyses). Three agents independently named copy-typing the game's weakest mechanic and recall-mode its single highest-value upgrade.
2. **Spacing is the second lever.** Spaced re-encounters d=0.85 verbal (317 experiments). Successive-relearning protocol (3 correct retrievals, then relearn on ~3 later days) lifts 1-week recall from ~20% to ~80%. Exact schedule shape barely matters (equal ≈ expanding); re-meeting words at ~W+1/W+3/W+7 sessions is enough. Testing gains are LARGER after a delay (g=.82 at 1–6 days), so the weekly session rhythm is ideal.
3. **Attention is the mechanism.** Players learn exactly what the mechanic forces them to process (pre-registered replication of intrinsic-integration). Letter-matching mechanics teach letter-matching; meaning-conditional mechanics teach meaning. Four tests for any new mechanic: can you win ignoring the knowledge; is it still a game with content stripped; does the winning decision USE the meaning; does content live inside the fantasy.
4. **The reward design is already right.** World-changes-as-rewards are task-congruent informational rewards, the one class with no measured motivation undermining. The dangerous classes: expected tangible prizes, controlling framing, speed scoring, public rank. Undermining by tangible rewards is STRONGER in children (Deci meta; contested magnitude, solid for this class).
5. **The sisters are the top design-critical risk.** Comparison praise reduces intrinsic motivation for girls even while they succeed; adult comparison between siblings predicts real performance gaps; visible side-by-side numbers push the younger toward the helplessness pattern. Every agent that touched this converged: self-referenced progress only, per-girl difficulty, process praise, co-op structured as complementary roles.
6. **Guidance beats discovery at this age.** Unassisted discovery nets d=−0.38; guided discovery d=0.50; worked example before generation. Productive-struggle advantage REVERSES for roughly grades 2–5, so the 9-year-old needs instruction-first and graceful misses.
7. **Feedback: elaborated + immediate.** Right/wrong-only ES=0.05; elaborated (meaning shown, correct form retyped once) ES=0.49. Immediate wins for primary age.
8. **Success rate target ~85%** (70% floor before frustration dominates); knobs in evidence order: review/new word mix, word length/frequency, and never time pressure.
9. **Production closes the loop.** Receptive knowledge does not convert to productive without produce-from-meaning practice. Harvest-then-spend designs (Crystallize, the strongest trial-backed precedent in the niche) and campfire retelling are the right shape; frames need varied fillers AND varied frames or they freeze into rote.
10. **Enactment works.** Congruent action + word (creature obeys "sit") is the TPR/enactment sweet spot, durable at 14 months in classroom study. Session 8's expanded typed commands landed on the right mechanic by instinct.

## Protect list (already correct; guard during any redesign)

- World-unlocks as the only currency; no grindable non-word economy (anti-Prodigy).
- No timers, no failure penalties, untimed catches; accuracy over speed everywhere (anti-Kahoot/Nitro Type).
- Streaks celebrated within-session, reset with zero ceremony; never a calendar-day streak.
- No leaderboards, no cross-player numbers; hot-seat co-op framing.
- Adventure/narrative shape (adventure d=1.867 vs drill 0.705) and the earned-world fiction.
- Tutor present and talking (instructional support around games adds d≈0.34; games alone underperform).
- Screen-time worry: ignore minutes for this context; only late-night solo displacement matters.

## Gaps (ranked by evidence × fit)

1. Every catch is copy-typing (form intro only, never retrieval).
2. A word is met ~1–3 times ever (catch, maybe a sentence, maybe a story); target is 8–12 varied encounters with 3+ retrievals across sessions.
3. No meaning-conditional moment: typing the visible word never requires knowing what it means.
4. Wrong-letter feedback is right/wrong-only (wriggle + sound).
5. No audio channel for words (oral vocabulary should precede/accompany decoding at this age; dual coding).
6. Both girls draw from the same word pool at the same difficulty; progress surfaces are shared.
7. Success/difficulty is untuned and unmeasured; no retention ground truth (nothing tests a word a week later).
8. Home play has no attempt log for tutor review (fossilization risk unaddressed).
9. Walk gate has no graceful-miss path for the 9-year-old.

## Proposal slate for the brainstorm

### Game changes (ranked; my recommendation = ship A, B, C first)

- **A. Memory Catch (recall mode).** First catch of a word stays copy-typing (form introduction). Every LATER encounter of that word shows the emoji + a blanked word (letter count visible), type from memory; one miss reveals one letter (graceful), full reveal after two (falls back to copy). Converts existing keystrokes into retrieval practice; the untimed law and the duel presentation both survive intact.
- **B. Spaced respawn ("words drift back").** Caught words re-enter the world as recall-mode encounters, ~75/25 review/new mix, review picks biased toward longest-unseen, re-encounters spread across sessions (save already carries per-word data; playT gives session time). A word becomes "owned" (gold in the book, tree in the garden) after 3 spaced perfect recalls; ownership never decays.
- **C. Elaborated miss feedback.** On a wrong letter in recall mode: flash the emoji + the full word briefly, then retype it once correctly. On catch completion: word spoken aloud via the browser's built-in offline speech voice (adds the missing audio channel; needs a quick voice-quality check on the actual laptop before we commit).
- **D. Meaning-conditional catch moments.** Occasionally two or three word cards drift near one creature/object; only typing the matching word catches (typing the others whiffs harmlessly). Small dose, keeps the attention mechanism honest.
- **E. Per-girl profiles.** Word pool band (k/d words already tagged), recall-mode aggressiveness, and review mix keyed to the active player; each girl sees only her own garden/book counts. Invisible dials, never labeled easy/hard.
- **F. Frame variety.** Add 2–3 sentence frames per magic ("I can see a ___", "There is a ___ here" already exists; add "I like ___", "The ___ can ___") so slots and frames both vary; worked example shown filled-in before first use of any frame.
- **G. Walk-gate mercy.** After two misses on a gate word: reveal letters one at a time; play never fully stalls.
- **H. Attempt log in the save.** Per-word: attempts, typos, timestamps, recall-vs-copy mode; surfaces as a tutor-only table (world-code round trip already exists). Enables everything in the tutor list below plus home-play review.

### Tutor practices (no code; can start Monday)

- Weekly 5-word cold probe at session start: words caught ≥1 week ago, say/spell from meaning, before the game opens. The retention ground truth, 2 minutes, and itself a retrieval workout.
- Steer re-encounters at W+1/W+3/W+7; missed slots just shift.
- Session steering rule: perfect-rate >90% → introduce longer/newer words; <75% → cut new words.
- D-teaches-K moments (she reads the word, K types; D checks spelling): tutors gain MORE than tutees (g=0.39 vs 0.33).
- Process praise only, self-referenced ("more than your last week"); never compare the girls aloud.
- Keep some English outside the game each session (joke, book page, chat) so words never become pure game currency.
- Monthly YLE-Starters-style mini-check as external validation (picture yes/no, spell-the-pictured-word) using game words.

### Rejected by evidence (do them nowhere)

Calendar streaks with resets; leaderboards or side-by-side totals; speed-weighted scoring; tangible out-of-game prizes; points/badges layers; latency-based mastery rules; unassisted-discovery gates for the 9-year-old; fuzzy spelling acceptance.

## Open questions for Idan

1. Recall-mode dosage: every re-encounter, or start gentler (every second)?
2. Speech synthesis voice: acceptable on the actual laptop, or skip audio for now?
3. Per-girl profiles: how visible? (fully invisible vs a named "my island journal" per girl)
4. The weekly cold probe: in-game surface (curator asks) or paper ritual before the screen opens?
5. Which of A–H land in v9 vs later? (my slate: A+B+C+G now, H next, D/E/F after we watch a session.)
