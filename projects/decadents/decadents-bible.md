---
type: note
created: 2026-09-10
author: jep
status: active
project: DECADEnts
---

# DECADEnts working bible (jep's distillation; Idi's December files are the source)

Scan doc. One line per fact. Sources at the bottom. Idi's own files in this folder stay verbatim; this file is the one jep updates.

## Premise (Idi, 2025-12-30)

- Decades as characters. Two per decade: one at the decade's biological age, one at its psychological age. Differentiation scales with complexity: 1920s pair near-identical (humor delivery), 2020s pair very different.
- Family of Time: a dysfunctional sitcom household. Biological age = years since the decade ended; personality = the decade's frozen archetype.
- Format: Ryan George "Pitch Meeting" model. One shot, one character, distinct background, cut every 3 to 5 s. Confessional mockumentary pilot, "The House of Time".
- Abstract heads: faces removed entirely, which deletes the hardest AI-video problem (face consistency). Heads are rigid objects; bodies wear period clothing.
- Endless-content model: Countryballs (low entry, high distinctiveness). Drop-in loop once the heads are learned.

## Cast grid (11 decades)

| Decade | Archetype | Alignment | Conflict | Head (Visual Dictionary) |
|---|---|---|---|---|
| 1920s | The Gatsby | Chaotic Evil | Man vs Machine | porcelain Art Deco mask, cracked glaze, no mouth, silent |
| 1930s | The Survivor | True Neutral | Man vs Nature | dusty burlap sack or gas mask |
| 1940s | The Soldier | Lawful Neutral | Man vs Man | steel helmet, only shadow where the face would be |
| 1950s | The Sitcom Dad | Lawful Good | Man vs God | chrome retro toaster or appliance |
| 1960s | The Hippie Grandma | Neutral Good | Man vs Society | lava lamp |
| 1970s | The Disco Anarchist | Chaotic Good | (none assigned) | disco ball or pet rock |
| 1980s | The Yuppie | Lawful Evil | Man vs No God | Memphis geometric shapes, floating |
| 1990s | Nostalgia Narcissist, 35 | Wildcard Good/Neutral | Man vs Self | CRT monitor, static or "Please Stand By" |
| 2000s | The Edgelord, 25 | Neutral Evil | Man vs Author | pixelated cube, early-3D texture |
| 2010s | The Influencer, 15 | Wildcard Chaotic/Neutral | Man vs Reality | Instagram icon or emoji head, gloss |
| 2020s | The iPad Toddler, 5 | Chaotic Neutral | Man vs Tech | VR headset or QR code, face fully obscured |

Ages 35/25/15/5 come from the feasibility report's four-character version; the production bible extends to 11 without ages for 1920s to 1980s.

## December pipeline (superseded where marked)

- Voice: Parler-TTS to design, F5-TTS or Kokoro to act, Audacity era filters (1940s radio: HP 300 Hz + LP 3 kHz + soft overdrive; 1990s VHS: wow-and-flutter + hiss; 1920s: no voice, MusicGen ragtime). Unbuilt. Preflight's licence rule (Apache/MIT only) now applies; Parler, F5, Kokoro licences unchecked.
- Body: Blender greybox, Mixamo rig, head object parented to the Head bone, export depth + canny, ControlNet into Wan 2.1. Unbuilt. Superseded for stills: Preflight locked Z-Image-Turbo, no ControlNet yet.
- Art: Flux LoRA / Midjourney named in December. Superseded: Z-Image-Turbo (Apache), local, 4 s per 1 MP still.
- Strategy: YouTube 2025 "inauthentic content" policy penalises mass-produced output; TikTok excludes AI from Creator Rewards; hybrid puppet workflow (static asset + lip-sync) recommended over pure video diffusion; Cat Biggie (6 people, 5 months, 60 min, ~40k views) as the failure case; Nothing, Forever as the low-fi success. All December claims, unverified by jep.

## Current state (2026-09-10)

- D1, 1990s: done. Render 2 (Idi's hand, seed 732135135824266) ruled as closing D1. Pick 6 from the sweep (seed 23069123189203) re-rendered at 4:3. Files in `renders/`.
- D1, 2020s: round 1 (A to D, `d1-2020s-contact-sheet.html`) picked 6 with notes. Idi's rule 2026-09-10, corrected the same day: **the head is the inanimate object so the character represents everyone; the body is a child in a suit, no visible gender or ethnicity.** The 2020s head = a 2029 sensory-immersion prototype plugging into all five senses, one intricate device, RGB-lit, ridiculous (his amendment to the December "VR headset / QR code" entry). Round 2 (E to H, `d1-2020s-contact-sheet-2.html`) picked 3, black sphere on a dino haptic suit. Round 3 (I to L, `d1-2020s-contact-sheet-3.html`): gaming helmet, PC tower head, five-sense pod, salon dome. **Idi picked 8 (2026-09-14): chrome helmet, iridescent visor, crying-emoji hologram.** His reason: genderless, raceless, and the visor is a front-facing screen that can show externally what the eye-projected screens do internally.
- 2020s head, locked: one glossy chrome helmet, large curved iridescent visor, a holographic emoji floating where the face would be (crying in the reference; the emoji is the character's mood display), black over-ear headphone cups built in, drinking port at the chin. No face, no skin anywhere.
- 2020s suit rules (Idi, 2026-09-14): juice box clipped to the belt with a straw tube to the chin port; spare juice boxes stowed in a chest rig like a soldier's magazines; no dinosaurs. The suit's print must serve four purposes: humor (unexpected, not unthinkable), characterization (a choice the character made), thematic expression (what Idi wants to say; the show's theme), lore (what a kid wears in 2029). Round 4 (M to S, `d1-2020s-contact-sheet-4.html`, 14 renders, seeds 3/4, 768x1344): M fictional sponsor patches, N app-icon merit badges, O product labels + barcodes + QR, P all-over smiley emoji print, Q real logos (legal test), R slang text, S sponsor patches under a kid's stickers. **Idi picked 4 (N app-icon badges, seed 4), 2026-09-14: "the right silhouette, we'll work out the details later."** His notes: the stickers are unrecognizable and one dinosaur patch remains. File: `renders/d1-2020s-pick4-badges-seed4-768x1344.png` (also `output\decadents\d1-2020s-r4\N-badges_00002_.png`).
- **D1 2020s: DONE, closed by Idi 2026-09-14** ("Close it. We're optimizing for throughput at this stage, quality in later stages."). D1 quest closed: two portrait files in `renders/`, seeds in the quest log. Stage rule from his words: throughput now, quality later.
- 2020s open details (deferred by Idi): badge content that reads at a glance (what a 2029 five-year-old earns: streaks, levels, app icons), the stray dinosaur, riff-brand juice boxes in the rig, the 2020s "film stock" look. Silhouette locked: chrome helmet, quilted grey suit, chest rig of juice boxes, hip juice box with straw, black gloves and boots.
- Round 4 findings: the chest rig of juice boxes renders in all 14; the hip juice box with a straw lands in the seed-4 renders (seed 3 tends to put the active box in the rig). Z-Image draws real logos legibly (McDonald's arches, YouTube, Coca-Cola, Disney, Fortnite, a small Nike swoosh) and short slang text legibly ("SKIBIDI RIZZ NO CAP", "GYATT" across the pouches), so both are choices, not model limits. Branded juice boxes in the rig (Q) read as sponsored ammo. The smiley print under the crying visor (P) is the one motif that states the character's split in a single frame.
- Prompt lessons: "head is a VR headset" renders as a worn headset; "shot on iPhone" renders a phone frame; "helmet" alone leaves the face open, so say "no skin visible anywhere" and "no face" explicitly, and prefer a sphere or a mannequin body. Negations leak: "no dinosaurs" in the prompt put a small dinosaur patch on 6 of 14 round-4 renders; never write the banned word at all.

## Real brand logos on the suit: legal read (jep, 2026-09-14, not legal advice)

- The question: 10+ recognizable real logos on a fictional character's suit, NASCAR-style. Does parody or satire protect it?
- US trademark, expressive works: Rogers v. Grimaldi (2d Cir. 1989) protects a mark used inside an expressive work when it has artistic relevance and does not explicitly mislead about source. Jack Daniel's v. VIP Products (US Supreme Court, 2023, unanimous) cut Rogers back: it does not apply when the mark is used as a source identifier for your own goods (the dog toy). A character wearing logos in a show is expressive use, not source identification, so Rogers still applies there. Medium-high confidence.
- US dilution: the federal statute (15 U.S.C. 1125(c)(3)) exempts parody, criticism and comment on the mark owner, and any noncommercial use. Medium-high confidence.
- US copyright: simple wordmarks and shapes (the swoosh, the arches) carry thin or no copyright; character logos (Disney's) do. Parody is a favored transformative use (Campbell v. Acuff-Rose, 1994) when it comments on the mark itself; satire aimed elsewhere gets less protection. Medium confidence.
- Israel: Copyright Act 2007 section 19 (fair use, open-ended list); Trademarks Ordinance infringement requires use in relation to goods in trade. Idi is in Israel; the show lives on global platforms, so US rules matter as much. Medium-low confidence on Israeli specifics; not researched beyond memory.
- Practical exposure ranks above the law: platform complaints. YouTube processes trademark complaints by form and removes clear cases; brand owners rarely chase satire, Disney is the exception. Merch flips everything: a t-shirt of the character wearing the arches is goods bearing the mark, Jack Daniel's territory. Medium confidence.
- jep's recommendation: fictional brands that riff on real ones (the sitcom tradition: Duff, Sprunk, Okama Gamesphere). Serves the four purposes better than real logos: the joke is in the twist, the invented 2029 brands are lore, and nothing is owed to a rights holder. Real logos: keep for a one-off gag, never on the base costume, never on merch.
- Tooling: `render.py` + `z-image-turbo.template.json` (slots only). ComfyUI drivable from jep on loopback. Seed sweeps at cfg 1 barely vary; vary the prompt.
- Nine decades: batch rendered 2026-09-14 (72 renders, `d1-nine-decades-contact-sheet.html`, quest `../decadents-d1-nine-decades-2026-09-14.md` with jep's picks 2, 9, 17, 31, 37, 45, 49, 59, 67 and flags). Idi ruled on all nine the same day (his notes in the quest file); round 2 (`d1-nine-decades-round2.html`, 32 renders) applied them; 2000s parked on his word. Awaiting eight numbers.
- Running gag (Idi, 09-14): the 1920s holds a drink and a cigarette in one hand at all times and never consumes either on camera; the 1980s repeats it with a brick phone and a cigar. Both render in one grip.
- Prompt lessons from the batch: masks and gas masks leak eyes; "pixelated cube" drifts to a CRT or to Minecraft Steve; exposed costumes show skin unless "long sleeves" is stated; the Instagram icon renders as the real Meta logo.

## Source files in this folder (Idi's, verbatim, never edited by jep)

| File | Words | Same as | Content |
|---|---|---|---|
| `DECADEnts.md` | 95 | `2025-12-30-decadents.md` (+ Nexus frontmatter) | the premise |
| `DECADEnts 1.md` | 3306 | `DECADEnts 2.md` (byte-identical), `2025-12-30-feasibility-and-strategic-analysis-of-decades-as-c.md` (+ frontmatter) | feasibility report, 4-character version, market and platform analysis |
| `DECADEnts 3.md` | 1099 | `2025-12-30-research-report-decadents---production-bible--tech.md` (+ frontmatter) | production bible: cast grid, Visual Dictionary, pipeline, pilot beats |

Three distinct documents, seven files. Deleting the four duplicates is Idi's call; jep never deletes.

## Log

- 2026-09-10 created after Idi dropped the seven files; Visual Dictionary found in `DECADEnts 3.md` section 2; 2020s sweep rendered.
- 2026-09-14 Idi picked 4 from round 4 (silhouette locked, details deferred); PNG copied to `renders/`. D1 closed on his word; W staged in the jar.
- 2026-09-14 Idi picked 8 from round 3; head locked. Suit rules and four purposes recorded. Round 4 rendered (14, `d1-2020s-contact-sheet-4.html`). Legal read on real logos added. Round-3 prompts were lost with the ComfyUI restart (history empty); round-4 prompts are stored inside the sheet's Prompts section.
