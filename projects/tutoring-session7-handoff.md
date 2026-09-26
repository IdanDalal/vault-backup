---
type: reference
created: 2026-09-05
author: jep
project: tutoring
status: active
---

# Handoff prompt for the session-7 conversation

Copy everything below the line into a new Claude Code session opened in `D:\work\vault`.

---

Session 7 with K (9) and D (12) is Monday 2026-09-07, 14:00 to 15:00, at my house, two girls at once. Goal of this conversation: research and refine the models, workflows, blocks and rules for a session built as a menu of generators, then hand me a Monday cheatsheet and an install quest list. The girls choose when to start and end which generator, the way they chose between installed games in sessions 5 and 6. Menu: text-to-image, text-to-speech, text-to-song, text-to-video, image-to-video.

Read first, in this order: `projects/tutoring-session7.md`, `projects/tutoring-word-world-memo.md` (evidence table, my thesis correction, the S7 section), `projects/tutoring-bakeoff/lesson-transcripts/31_Aug_at_8-56.DISTILLED.md` (the generative-media segment is the prototype: who typed what, the refusals, the timings), `projects/tutoring-bakeoff/lesson-transcripts/24_Aug_at_9-03.DISTILLED.md`, `projects/tutoring-operating-principles.md` (P6 counter rule), `projects/tutoring-lesson-cheatsheet-2026-08-25.md` (the format that worked), `inbox/Studio Preflight.html` and `projects/pc-hq-stack.md` (ComfyUI on 127.0.0.1:8188, Z-Image-Turbo, the 4090; zero renders so far, so the install is part of this quest), `projects/parts-registry.md` (level-designer policy, the Teacher and Mask entries), `projects/wins-jar.md` (Built/Received rules).

Rules already decided, do not reopen: the girl types every prompt and I spell on request, never voice input; every new English word she types goes to her own counter, monotonic, she performs the update; nothing generated from photos of the girls, ever; local generation runs behind a word allowlist because it has no moderation; two stations so K is never lost to Roblox while D generates; Word World stays installed as an opt-in only; anonymous downloads only, no gated model repos; the PC bills the Claude plan only, no API keys; jep never writes `atomic-notes/`, `telos/`, `.vault-config/`.

My state: mostly resistance, little excitement. In sessions 5 and 6 the girls disagreed, yelled, competed and pulled me in opposite directions; it felt like fighting two bosses at once. I typed 7 of 12 prompts in session 6 because it was faster. Design against both: the cheatsheet must make the two-station split and the "she types" rule structural, with a fallback card for each failure state (K demands an audience; D asks me to type; a generator stalls or refuses; both want the same station).

Research questions, with sources and confidence per claim: which local models run each modality on one RTX 4090 with results in seconds (image is settled: Z-Image-Turbo; settle TTS, song, text-to-video, image-to-video, or rule a modality out for Monday); what the free phone-side options are for the same modalities in Israel (Meta AI in WhatsApp is known to work for image-to-video); a word allowlist mechanism for the local image app that a nine-year-old cannot bypass by accident; how each output becomes a keepable artifact for the girl (file on her phone, printed, sent via the mother).

Deliverables, in this order: 1. a verdict per modality (local / phone / out) with the reason; 2. the install quest list for the PC, bounded, with acceptance criteria and a done-state, split into what I do as admin and what jep does as `jep`; 3. the Monday cheatsheet, dense scannable lines, opening block, the menu, per-generator prompt cards with example English words at the girls' level, the counter ritual, the fallback cards, the five things to watch for; 4. the wins-jar candidate line for the session.

Response shape: verdict first, numbered points I can answer by index, options as A/B/C with your recommendation and an invitation to overrule, under 400 words per reply with the bulk in files. No em dashes, no "not X but Y" framing, in chat or in any file. When I give a ruling, you may add one optional "Context, if you want it" prompt at the end; if I ignore it, drop it.