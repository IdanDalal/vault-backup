---
type: reference
created: 2026-08-23
author: jep
project: tutoring
status: active
---

# Monday morning cheatsheet — Word World session (2026-08-25)

Read this once with coffee. Loose guidelines, no clock. The game does the heavy lifting; your job is to listen, steer gently, and talk English around it.

## The 60-second version

1. Before the screen opens: 2-minute cold probe (below).
2. Let them play. Say words out loud constantly; the game is silent on purpose.
3. Praise effort against her own past, never against her sister.
4. When someone is stuck, point her at her sister before you rescue.
5. If anything feels broken or overwhelming: one word in config turns the new system off (bottom of this sheet).

## Before the screen: the 2-minute cold probe (overlap confirmed — do it)

Words in the game that lessons already touched: **cat, red, sun** for sure (session-4 sheet), plus any you remember using. Pick 5. For each: say it in Hebrew or point at a picture → she says the English word aloud → spells it on the whiteboard. No grades, no drama, wrong answers just get a "we'll meet that one today." This is the retention ground truth AND a warm-up; from next session, probe words the game itself taught last time.

## What changed in the game since they last saw it (know this so nothing surprises you)

- **Words now have levels.** First catch works exactly as before (word visible, type it). Later the word comes BACK as a silver card showing only its emoji and "?" — she must type it **from memory**. Later still it returns gold: she completes a sentence with it ("I can see the ___."). Gold = hers forever, and her garden plant becomes a tree. Wrong guesses gently reveal letters, so nobody gets stuck.
- **The garden wilts** (your idea, live). Plants droop brown between lessons; standing near one shows "E water the 🌱" and re-typing the word from memory revives it. On their FIRST load with an old save, everything will be wilted — frame it as "the garden missed you," it's a feature.
- **Creatures obey 8 typed commands** now: come, stay, jump, home, sit, eat, sing, dance — each locked 🔒 until its word is caught. Every command performs visibly.
- **The campfire starts cold**: catch "fire" (floats near the cove), then type "start fire" at the circle to unlock storytelling forever.
- **Catching is a duel now**: player portrait VS the word, attack rings, a dramatic finish. Expect delight; it's untimed like everything.
- **N opens Island Magic**: every earned wonder (dragon, rainbow, stars, music, even color itself) has an on/off switch. Everything is their choice.
- **Boats appear** only after catching "boat"; every menu has a red ✕; pause shows island stats.
- **Idi and Mom live on the island now.** The garden keeper who gives the gift words and cheers every catch is Idi; Mom wanders the plaza saying proud things. The room and the world match.

## During play — the loose rules

- **Say every caught word aloud, twice, warmly.** The game has no voice; you are the audio channel. Ask her to say it back when it feels natural.
- **Praise the process, self-referenced.** "You remembered that with no help" / "three more than YOUR last time." Never "you're so smart," never anything comparing K and D. This is the single strongest rule in the whole research pile, especially for girls.
- **D-teaches-K, engineered casually.** When K is stuck on a silver card, the game itself suggests asking her teammate after 3 misses. Your moves: hand D jobs like "read the word to her" / "check her spelling" / "you hold the answer, she types." The research surprise: the TEACHER sibling learns more (g=0.39 vs 0.33) — so this costs D nothing, tell her so if she resists.
- **Difficulty self-tunes per girl** (typed name starting K vs D → different hint speeds and word choices, invisible). If either notices, your script: "one difficulty for age 9 and 12 wouldn't be fair or honest — if you two disagree, we scrap it." Then honor whatever they decide.
- **Let them chase what excites them.** The quest list suggests, never forces. 2–4 open goals at once is the sweet spot; if they're wandering happily and typing words, the system is working.
- **Rough success check, by ear:** breezing through everything → nudge toward longer/newer words (D's band). Frustration or guessing → steer to wilted-garden watering (easy wins) or bronze catches. Target feel: winning most of the time with occasional real effort.
- **Sentences and stories are the gold mine** — meaning lives there. If energy dips, the campfire (once lit) is the reliable high point.
- **Keep 5 minutes of English OUTSIDE the game** (a joke, a page, chat). Words must never become game-only currency.

## If things go sideways

- Too much, too new, or the level cards annoy them: open the file, find `EARN: {` (~line 24 of the config block), change `levels: 'on'` → `'off'`, reload. Everything else stays; it's exactly last week's game.
- Panel stuck or weirdness: every menu has a red ✕, Esc always works, reload loses nothing (autosave every 4s; world code in pause as backup).
- Too dark / raining at a bad time: N → Island Magic → set day/clear.

## Watch for (my asks — mention these in your notes after)

1. First reaction to a silver "remember me?" card — delight or stress?
2. Does K use the letter hints or freeze? Does D find silver too easy?
3. Does anyone water the garden voluntarily, or only when steered?
4. Any moment they describe as "the quiz part" — that's the alarm bell.
5. Whether D takes the teaching role willingly.

## If they ask to take the game home

Say yes, with one caveat. `word-world-K.html` and `word-world-D.html` are staged in the games folder; send each girl HER OWN file (the filename is what keeps their saves separate, even on a shared computer — don't rename the files). **Best on a PC/laptop.** On phones, typing now works everywhere (the keyboard pops up for every typing screen, English layout needed) but walking around the island still needs a real keyboard — phone-friendly controls are the next build. Their home play logs every attempt into the save; ask them to paste their world code at the next session and I'll read the evidence log from it. Home rules to give them: it never needs daily play, and nothing is ever lost by staying away.

## Paper trail

Session-9 details: [[tutoring-game-3d-session9-checkpoint]] · research behind every rule here: [[tutoring-game-pedagogy-research]] · what shipped Sunday daytime: [[tutoring-game-3d-session8-checkpoint]].
