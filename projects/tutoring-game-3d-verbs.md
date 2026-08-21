---
type: project-brief
created: 2026-08-21
author: jep
project: tutoring
status: in-progress
---

# 3D Game Verb Thesis v2 — Customize · Collect · Combine · Create

Companion to [[tutoring-game-3d-brief]] (tech + art contract) and [[tutoring-game-3d-collab-research]] (stack research). Input: Idan's verb thesis (2026-08-21) iterated through four research agents: sentence/story-construction games, typing + catch mechanics, ESL pedagogy, collection/customization loops. All sources anonymously accessible; unverified claims labeled. Open decisions for Idan at the bottom.

## The thesis, iterated

The four verbs survive research contact, with two sharpenings:

1. **Each verb has a distinct job.** Customize = identity on-ramp (and secretly an English domain: clothes, colours, body parts are all YLE Starters themes). Collect = the engagement engine, pedagogically light. Combine = where learning actually happens. Create = where language becomes performance and permanence. The load-bearing evidence: Involvement Load Hypothesis meta (Yanagisawa & Webb 2021, 398 effect sizes): the "search" component (hunting/finding) contributes ~zero retention; the "evaluation" component (using a word in a novel sentence, judging fit) carries the effect. So Collect earns fun and Combine earns learning; both jobs are real, and the design must gate rewards on evaluation.
2. **Idan's hunch that Create ≈ Combine at a larger scale is confirmed.** Words→sentence and sentences→story are one composition act at two zoom levels; one interface serves both, and pedagogy supplies the ladder between them (Talk for Writing: imitation → innovation → invention; retell a known skeleton, then vary it, then invent).

Direct architecture precedent, validated: **Crystallize** (Cornell, CHI 2016): 3D world, collect words from the environment into an inventory, construct target sentences in quests; the forced-collaboration version produced the highest learning rate. Cautionary twin: **Influent** (collect-only, no sentence stage): short-term recognition, low retention, motivation collapse. Collect without Combine is the documented failure shape.

## Collect — the catch interaction (timer verdict: REMOVED)

Evidence against the timed variant ("type it in under 2s"), converging from three directions:

- Timed-test literature (children, math): accuracy drops under time pressure; **girls specifically** showed the untimed-accuracy advantage while boys were unaffected (Caviola et al. review, Frontiers 2017). Anxiety interacts: pressure narrows strategy to fast-and-error-prone.
- WPM reality: age 9 ≈ 10–15 WPM (~1 letter/sec including thinking), age 12 ≈ 20–30. A 2-second window is physically impossible for K and trivial-to-hard for D; one clock can never fit both (typing games' documented 20–110 WPM spread problem).
- Every surveyed kids' typing product (TypingClub, Dance Mat, Mavis Beacon) is untimed at the interaction level; accuracy first, speed emergent. Kids-ESL game studies attribute anxiety reduction to the pressure-free environment.

**The catch shape that keeps all the Pokéball feel** (ZType + Pokémon GO + Bulbapedia mechanics, clocks stripped):

1. Approach: words idle in the world (bob, hum, glow), "notice" the player at close range and turn to face her. Anticipation phase, zero timing skill.
2. First typed letter locks the word (ZType target-lock = commitment moment).
3. Each correct letter: projectile/sparkle hit, letter chunk flies off, tick sound rising in pitch across the word, and a GO-style ring contracts one step. Ring color telegraphs rarity (green→red). Ring shrink is player-driven; keystrokes are the clock.
4. Final letter: 2–3 frame hitstop, jar/net rocks once per syllable (the Pokéball shake grammar as celebration pacing; outcome is already player-determined), click + star burst + "+1 WORD".
5. Zero-typo catch = "critical capture": golden flash, single decisive snap, sparkle on the collection card.
6. Wrong letter: word wriggles, letter bounces off with a boing, typed progress retained, next keystroke immediately live. Recovery is itself input; a word can never flee due to slowness.

Difficulty levers (per-girl profiles, adaptation signal = rolling accuracy): word-length bands (K: 3–4 letters, D: 5–7), rarity by placement (golden words at climb-worthy spots, deterministic, no RNG), recall depth on recapture: first catch = copy the visible word; recapture upgrades the card bronze→silver→gold via cloze (C_STLE) then memory-typing. Upgrades only add; the card keeps its best state. Craftable "net upgrade" reveals one missing letter (difficulty relief as collection reward, the Stardew Training Rod lesson).

## Combine — frames + consequences

- **Frame inventory (A1 band, K):** I like ___ · I have a ___ · It is (a) ___ · There is/are ___ · The [noun] is [adjective] · I can [verb] · The [noun] is [verb]-ing · [Name] [verb]-s the [noun]. A2 additions (D): past -ed, because-clauses, want to [verb]. Sentence-length targets: K 3–6 words present tense; D 6–10 words with and/but/because/then. Past tense stays optional for D and is off K's requirement list entirely.
- **Scaffold ladder, faded by design** (frames that never fade cap independence — Alvarez 2023): L1 frame + picture word bank → L2 frame with POS-labeled empty slots → L3 sentence starter only → L4 free slots.
- **Validation split:** the game validates form deterministically (POS-typed slots + small agreement lookup); the tutor rules on meaning and awards a "makes sense" star. Absurd-but-grammatical sentences ("The cat eats the school") count as valid and are a comedy feature; they still exercise the evaluation component. Duolingo-style token-array checks for quest sentences; the Wordscapes rule applies: any valid non-target sentence still pays out. No correct answer is ever wasted.
- **Sentences DO things** (intrinsic integration: Habgood & Ainsworth 2011, ages 7–11: math inside the verb beat quiz-gates by ~17 points at delayed test, ηp²=0.24, and kids chose the intrinsic version ~7× longer in free play). Micro-Objectnaut: a curated spawn table where completed sentences act on the voxel world. "I have a cat." spawns a voxel cat at the base; colour adjectives tint it, big/small scale it; "I can fly." grants 10s of glide. Even 20–40 spawnable nouns delivers the Scribblenauts magic ("does it know MY word?") at bounded cost.
- **Two-state words (Chants of Sennaar pattern):** pickup = dim/italic entry (found); first correct use in a sentence = solid/bold (owned, spendable). Crystallize-gate on evaluation, per the ILH finding.

## Create — story spots

- **Retell-then-vary:** 3–5 picture-panel story skeletons; first pass substitutes the girls' collected words into slots (swap the animal, the place, the food); free invention unlocks after 2–3 skeleton cycles. Matches the narrative-intervention literature (oral narrative meta, System 2025, abstract-verified; gains maintained after breaks in child studies).
- **The judge question, solved without AI.** Machine validates structure only: all dealt words used (Once Upon a Time / Story Cubes checklist pattern), slots filled with correctly-tagged words (Mad Libs POS pattern). Meaning is validated socially: the story is performed aloud at the story spot to the tutor + sister (bots gather and react on screen; the real audience is at the table). This converts typing into speaking practice, where the narrative literature's gains live. Elegy for a Dead World's tested warning applies: freeform froze native-speaker playtesters until fill-in-the-blank frames were added; beginner ESL needs frames more.
- **Ceremony + permanence:** finished story is typeset into a book object, bound, shelved in the base library; sentences post to a notice board. Stories live in the world code, so sharing the island shares the library. Optional v2: Storyteller-style micro-sim goals (actors with states; goal predicates like `dog.happy && bone.owner==dog`, ~150 lines) for guided story puzzles.
- Tutor's whole loop role, by design: semantic judge · story audience (one recast per story, no more) · pushed-output prompter ("What colour? Why?") · pronunciation model (voices each new word at pickup; no offline TTS exists in one file) · curator (picks next session's word set + skeleton). Moment-to-moment collect/combine runs tutor-free or it stops being a game.

## Word economy (curation scheme)

Source dataset: Cambridge YLE wordlist, machine-readable, 1,114 words with POS tags + 20 themes + per-level flags: github.com/ozbonus/yle-vocabulary-dataset (anonymous, MIT-adjacent; recompute per-level splits from the CSV). Official PDF: cambridgeenglish.org 506166 wordlist 2025.

- **Tier 0 — grammar glue, free forever:** ~25 function words (a, the, my, is, are, and, in, on, I, she...) pre-installed as distinct-colour blocks. Beginners fail on function words; failure should live in content choices.
- **Tier 1 — engine verbs (~25–30):** like, have, see, want, eat, go, play, jump, fly, open, make, find... each fits ≥2 frames; most-recycled class.
- **Tier 2 — concrete nouns by theme = the collectible economy:** spawned as the voxel objects themselves (voxel apple carries "apple"), free semantic grounding. Starters-flagged words in K's biomes, Movers/Flyers in D's.
- **Tier 3 — describers:** colours + size/feeling adjectives; each unlocks the [adjective] slot across every owned frame (one word upgrades everything).
- **Tier 4 — story connectors (D, Create-stage):** then, but, because, suddenly, one day, finally.
- **Set composition rule (Tinkham 1997 + replications):** THEMATIC sets (wave/shell/swim/sandy/splash: words sharing a scene) are learned faster; SEMANTIC same-category sets (red/blue/green) interfere and learn slower. Sets of 7–12 (practitioner heuristic), always spawned frame-completing (verb + 2 nouns + adjective that build a valid sentence together), so every trip ends buildable.
- **Session budget:** 5–10 new words per session, hard cap; each word needs 7–12 meaningful encounters before "owned", so the loop spends its remaining time recycling. Spaced reappearance at session+1 and session+3 (an "old word" door/gate); equal intervals suffice, no algorithm needed.

## Collection display + base + world

- **Word Garden at home base:** collected words are planted; each plant grows sprout→flower→tree as the word gets USED in sentences. One mechanic merges collection display, the evaluation gate, and grow-only stakes. Backed by garden-metaphor ed-games (GardenWords) and the Animal Crossing museum lesson: a collection as a walkable space the girls built beats any menu.
- **Sets UI:** island signposts show each biome's set as filled cards + grey silhouettes (Zeigarnik pull). Pre-stamp 2 words of set one as a gift from a named bot (endowed progress, Nunes & Drèze 2006).
- **Per-set instant rewards** (Stardew bundle pattern): each completed set immediately unlocks a cosmetic (trail, pet glow, hair, title) AND adds a physical piece to the base. Partial completion always pays.
- **Base functions stack four return-reasons:** garden · sentence workbench · notice board/book shelf (museum of THEIR output) · named bots who move in Terraria-style at milestones, one bot per biome, curator-bot delivers one delighted line per new word and per set (converts checklist progress into social recognition, the thing the CHI 2025 study says girls this age optimize for).
- **World layout:** 4–5 biomes (beach, forest, snowy peak, flower meadow, cave), each = a thematic word scene holding 2–3 sets; the biome is the mnemonic context. One central weenie: the Story Tree / lighthouse above the base, visible from everywhere through the fog; one sub-weenie landmark per biome. Triangle-rule terrain pass: collectibles just behind crests, sparkle leaking over the edge. No minimap needed at 96×96.
- **World code carries the flex:** visiting the sister's code = walking her garden, reading her board, her bots greeting the visitor by avatar name. Zero networking, full show-off loop.

## Customize

CHI 2025 (ages 8–13): girls' motivations = self-representation, idealized-self play, social connection; the "wardrobe effect" says kids converge on ONE favorite look, so depth of one look beats breadth. Ranked by identity-payoff per line of code:

1. Hair (6–10 box-cluster styles) + full palette swap (skin/hair/top/bottom) — the #1 named element, near-zero geometry.
2. Companion pet, one voxel mesh lerping behind, grows/gains emissive "neon" glow with collection progress (the Adopt Me lesson: pet = status earned here by collecting words).
3. Nameplate + earned titles ("Word Hunter", "Story Weaver") as set rewards.
4. Trail particles, palette-linked, rarer trails as milestones.
5. One head slot + one back slot (wings/cape; Roblox girl-culture staples, community-consensus level evidence).
6. "Twin look" one-click palette copy of the other girl (social-connection motivation, free since avatar lives in the world code).
7. Skipped: sliders, body morphs, big wardrobes (wardrobe effect + body-image anxiety flag from the Digital Wellness Lab).
8. Avatar shop is itself English practice: items bought by assembling "I want the red wings."

## Co-op (new pillar candidate)

Crystallize's strongest experimental finding: forced two-player collaboration produced the highest learning rate. With a 9/12 skill gap, head-to-head guarantees a fixed loser; the literature favors cooperative goals. Hotseat on one laptop: asymmetric word holdings (each girl's biomes hold words the other's frames need), shared island album ("40% complete"), shared stories requiring one sentence from each girl. Competition stays out of the scoring layer entirely.

## Design laws (each traced to evidence above)

1. Untimed everywhere; keystrokes are the only clock.
2. Reward accuracy streaks; speed is never scored (30 WPM @80% < 22 WPM @98%).
3. Collection gates rewards on USE, since pickup alone teaches ~nothing (ILH).
4. Every valid sentence pays something; wrongness costs one wriggle and zero progress.
5. Thematic sets, frame-completing spawns, 5–10 new words/session.
6. Sentences have world-consequences (intrinsic integration), quiz-gates banned.
7. Frames fade on a ladder; meaning-reward (audience) outweighs form-reward as girls level.
8. Cap K at present tense; D gets past tense as stretch.
9. Grow-or-pause stakes everywhere (garden, base, cards); recapture upgrades, no loss paths.
10. Content refresh every 2–3 sessions (collection-novelty decay is measured and real).

## Build-scope ladder (maps to the brief's 2+0.5 session estimate)

- **Slice A (target for lesson 5, Mon 2026-08-25):** island + walk/jump + place/break + avatar palette/hair + word pickups with the full catch ritual + word garden planting. Playable, magical, Collect-complete.
- **Slice B:** workbench frames + spawn-table consequences + sets/signposts + curator bot + set rewards.
- **Slice C:** story spots (skeleton retell → book ceremony) + titles/trails/pet + twin-look + spaced-word doors.
- Smoke-test gate from [[tutoring-game-3d-brief]] still applies before any of this.

## Decisions — RESOLVED by Idan 2026-08-21 (Friday night)

1. **Catch is untimed, permanently.** The 2-second variant is withdrawn; no-timers rule reaffirmed as absolute. Recapture depth comes from cloze/unscramble/memory-typing, no speed modes at all (opt-in challenge mode for D also skipped).
2. **Spawn-table magic is IN for v1.** Sentences act on the world (spawn/tint/scale/ability).
3. **Build weekend: Sat 2026-08-22 + Sun 2026-08-23, game ready Monday 2026-08-25 morning** for lesson 5. Idan prompts sparsely; each prompt kicks off one long autonomous slice. Must-have = Slices A+B; Slice C ships minimally (one story skeleton + book ceremony) if time runs short.
4. **One shared world.** Both avatars exist in the same island, hotseat co-op, one world code carrying two avatars + shared garden/album. Idan's framing: personalization happens IN the world, at avatar/base level, with a single shared world identity.

## Source-quality caveats (carry when citing)

Peer-reviewed anchors: ILH meta (Yanagisawa & Webb 2021) · Tsai & Tsai 2018 (d≈0.99, magnitude likely inflated; between-group d≈0.5–0.87) · Habgood & Ainsworth 2011 · Tinkham 1997 + replications · Crystallize CHI 2016 · Adesope 2017 retrieval meta (g=0.61) · CHI 2025 avatar study · timed-test girls' accuracy finding (Frontiers 2017). Practitioner-grade, label as design lore: sentence-frame efficacy (consensus, thin RCT base) · 7–12 set size + 40–60% tipping (Yu-kai Chou) · WPM-by-age figures (commercial aggregations, mutually consistent) · Talk for Writing (EEF "promise" level). Unverified web claims to never repeat as fact: 68% Common Sense avatar stat · 62% Minecraft skin survey · Scribblenauts parser internals · Story Cubes study effects.
