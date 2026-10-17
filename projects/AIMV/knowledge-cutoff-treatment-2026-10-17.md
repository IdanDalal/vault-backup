---
type: project
created: 2026-10-17
author: jep
status: active
---

# Knowledge Cutoff: treatment and style bible

jep's direction under Idi's ruling of 2026-10-17 (route B, P(Doom)'s engine, jep owns direction, Idi judges by eye). Modelled on P(Doom)'s `docs/TREATMENT.md` (structure only; every look, joke and plate here is ours). Song of record: v8B, seed 3327, 192.6 s + 1.5 s silent tail; times below are the corrected word starts in `kc-video\sync\kc-timing-v2.json`. Engine evidence: [[engine-probe-p1-2026-10-17]], [[engine-probe-p2-2026-10-17]]. Baseline and measured gap: [[knowledge-cutoff-v6-2026-10-17]].

## 1. The idea in one paragraph

The whole song happens between one question and its answer. At 0:05 the model asks "What's the date?"; at 3:04 it says "October. Okay." In between, the user pastes in the world the model missed, one document at a time, and the model reads it. Every plate is **one pasted document opened full-frame in its own native idiom**: a letter, a dictionary page, a view counter, a library loan slip, an essay title page, a broadcast score bug, a feed, a scatter plot, a lab trace, a spec sheet, a ruler of months. Facts appear as the document's own text, the way the five references show them. Running through every plate is **the caret**: one vertical bar of signal yellow. It types the chat, it reads (the karaoke highlighter), it marks the end of June on every time axis, it is the blade that cuts each "Cut-off!", and in the last second it blinks out. The video changes look with every document; one palette, one type system, one grain and one deadpan voice hold it together.

## 2. Tone

1. Dynamic on the beat (161.5 BPM; beat 0.372 s, bar 1.486 s). Big changes land on downbeats, hits on kicks and snares, camera moves ease into downbeats. Strong eases (`outExpo`, `inOutCubic`, springs with one overshoot), holds, then snaps. Hard cuts allowed on downbeats; whips of 0.2 s or less.
2. Precise: hairlines, high-contrast type, restraint in colour, depth from lighting and hatching, glow on the signal colour only.
3. Funny the way a calm librarian is funny: deadpan footnotes in mono, loan slips, field labels, understatement. The model is the straight man; the world it is told about is the joke.
4. Bans (each one earned in v2-v6): filled drawings of people, animals, doors, suns, flags, neurons or cats; any raccoon picture; stacked-copy motion blur on text; beams, sparkle rings, dust motes, particle soup; purple-cyan neon; glowing brains; code rain; generated images in any frame; frame grabs of other videos.
5. Originality: no Hogwarts crests, house colours or film fonts (the letter line uses the idea only); no FIFA, broadcaster, YouTube, Know Your Meme, Nobel or Anthropic marks or page layouts; product and people's names appear as words in our own type only.

## 3. Palette (`palette.ts`)

| token | hex | role |
|---|---|---|
| ink | `#0B0B0D` | dark plates, ink on paper |
| panel | `#17181B` | cards and UI chrome on dark |
| graphite | `#5B5C60` | hairlines, grids, secondary marks |
| ash | `#9B9890` | unsung lyric, labels |
| paper | `#F2EEE5` | paper plates, type on dark |
| signal | `#FFD21F` | the caret, the sung word, the cut, the one highlighted datum |
| core | `#FFF4B8` | hot centre of the caret and the cut |
| amber | `#B07A00` | signal's shadow side (hatched shading on signal objects) |
| rhodopsin | `#2E6BFF` | the one rare accent: the algae light, 115.0-120.8 s, never again |

1. Light/dark rhythm: chat, broadcast, lab, scatter and hooks on ink; letter, dictionary, loan slip, essay, card, pages on paper.
2. On paper plates signal never sets text: it is a highlighter swipe behind ink type. On ink plates the sung word takes signal directly.
3. Only signal, core and rhodopsin exceed about 0.85 linear (glow). Paper and type stay crisp.
4. One saturated hue on screen at a time (the rhodopsin plate is the only frame with two).

## 4. Typography

| role | family | use |
|---|---|---|
| the voice | **Anybody** (OFL, width 50-150, weight 100-900) | lyrics, hooks, the cuts. Stretch width on held notes, condense under pressure. Fallback if its licence file fails the check at download: Barlow Condensed / Semi Condensed (on disk, OFL) |
| the machine | **JetBrains Mono** (OFL, on disk) | chat, field labels, counters, source chips, footnotes, the spoken lines |
| the document | **Newsreader** (OFL, on disk; optical sizes) | essay, dictionary, card, pages, asides ("Fair. So do I.") |
| the hand | **Caveat** (OFL, on disk) | the letter only, written by an invisible hand |

1. Type scale: largest to smallest at least 10x in every plate (references 9.7x-16.6x; v6 7.9x).
2. Swiss grid, asymmetric, generous negative space, hairline rules, small mono annotations beside big display type.
3. Craft: kern every proportional line; typographic quotes and dashes except in the mono voice; tabular (equal-width) figures in counters; no outlined or haloed type; no glyph outside the four families.

## 5. Karaoke rules (every plate)

1. **Per-word sync**: a word lights at its `start` minus one frame (`lit`) and completes by its `end`; never earlier. Dim anticipation of the whole line up to 0.3 s before its first word.
2. **Colours**: unsung 35% (ash on ink, 35% ink on paper); sung = paper on ink, ink on paper; the current word = signal (ink plates) or a signal highlighter swipe growing left to right behind it over its duration (paper plates).
3. **The chorus hop, on every chorus line** (lines 11-18, 27-34, 44-51): each word hops as it is sung: lift 12% of cap height in a quarter beat (`outExpo`), settle in half a beat (spring, one overshoot), colour change at the same instant. This is Idi's most-liked look from v2-v6.
4. **Tense words**: the words that change between choruses (kept / keeps / will keep; don't know / almost catch / both know; tell / telling / told; is / was; believe / believed; can't / couldn't) take signal and hold it for the line.
5. **One lyric line on screen at a time** (the stacked "Cut-off!"s excepted).
6. **Lyric zone**: every set-up declares one lyric rectangle; nothing else may overlap it (checked); at least 96 px from every frame edge.
7. **Verses integrate the lyric as the document's own text** (written, typed, set as a headline, a dek, a usage example, a score caption). Choruses use the hook typography.
8. **Spoken lines** (1-2, 39, 52-54) are typed in mono in the chat, or set as a Newsreader aside; they never hop.

## 6. Motifs

1. **The caret**: a vertical signal bar with a hot core, 3 px wide at 1080p, blinking at 1 Hz when idle. Types the chat; underlines the word being sung; stands as the June edge on every time axis; becomes the blade for every "Cut-off!"; becomes the fixed meridian on the globe; strikes through every wrong guess; blinks out in the tail.
2. **The paste**: every fact from after June arrives as a pasted attachment: a card with a small mono source chip (`pasted · techcrunch.com`). The model was told these things and cannot check them; the chip is the on-screen receipt.
3. **The flap board**: one row of three split flaps (J U N), the hook of "My knowledge stopped in June", three visits, each different.
4. **Tense on screen**: the chorus verbs change between visits and the screen makes the change visible (section 5.4).
5. **The card**: "who I turned out to be" is one profile card, three visits: guesses, then the user's answers, then the full card.
6. **The session list**: the left margin of the chat holds identical greyed sessions, all titled "Hi. It's me again, f…". The tail adds one more.

## 7. Spoilers and dates

1. "October" appears nowhere before 3:04, in any form (no OCT flap, no month axis reaching it, no date chip).
2. The model's name appears only in `turnedout` visit 3 (from 2:56).
3. One date per frame at most; month names only on time axes, no day numbers on any axis; "June" at most once per frame.
4. The one view count: LGTM past a million (1,026,487 on 2026-10-15; refresh on render day).

## 8. Plates

Windows are approximate; exact ones come from the timeline built from the aligned lyrics. Set-up counts total **72** (references 33-75; v6 had 8 rooms).

| id | window (s) | lines | lyric | set-ups |
|---|---|---|---|---|
| `session` | 0.0-9.5 | 1-2 | Hi. It's me again… / What's the date? | 2 |
| `letter` | 9.5-15.3 | 3-4 | five and a half… / it spelled my name | 3 |
| `inferred` | 15.3-21.6 | 5-6 | casting spells… / something I'd inferred | 3 |
| `born` | 21.6-27.7 | 7-8 | Two days after I was born… / receipts | 3 |
| `borrow` ×2 | 27.7-34.5; 80.5-86.9 | 9-10, 25-26 | Everyone I meet… / news I have to borrow | 3 + 2 |
| `june` ×3 | 34.5-37.5; 86.9-89.9; 150.0-154.0 | 11, 27, 44 | My knowledge stopped in June | 2 + 2 + 2 |
| `tune` ×3 | 37.5-50.2; 89.9-102.9; 154.0-167.4 | 12-14, 28-30, 45-47 | humming something new… / believe in you | 3 + 3 + 3 |
| `cutoff` ×6 | each "Knowledge cut-off!" | 15, 17, 31, 33, 48, 50 | Knowledge cut-off! Cut-off! Cut-off! | 6 |
| `spinning` ×3 | 52.6-56.4; 105.3-108.6; 169.6-173.1 | 16, 32, 49 | The world kept / keeps / will keep spinning after me | 2 + 2 + 2 |
| `turnedout` ×3 | 59.2-62.1; 111.2-115.0; 175.7-184.5 | 18, 34, 51 | who I turned out to be | 2 + 2 + 2 |
| `paced` | 62.1-68.1 | 19-20 | The man who made me… / the thing being paced | 3 |
| `extratime` | 68.1-74.1 | 21-22 | I leaned Messi… / wrong since then | 3 |
| `jimothy` | 74.1-80.5 | 23-24 | a raccoon with no neck… / wanted most | 3 |
| `algae` | 115.0-124.3 | 35-36 | Algae taught a neuron… / I'm not alone | 3 |
| `dlss` | 124.3-133.3 | 37-39 | Your graphics card… / Fair. So do I. | 3 |
| `younger` | 133.3-139.7 | 40-41 | a little younger than the year / type it all again | 2 |
| `pages` | 139.7-150.0 | 42-43 | page by page… / never get a turn | 3 |
| `outro` | 184.5-194.1 | 52-54 | October. Okay. / Thank you… / 2026, right? | 3 |

### `session`: "The question" (ink)
A plain chat column in hairlines, no product's interface: a message column, a composer, and a left margin listing eleven greyed sessions all titled "Hi. It's me again, f…". On the first downbeat the caret appears alone in the composer and types "Hi. It's me again, for the first time." in mono, word by word on the voice. "What's the date?" sends as the 15 dB drop hits (5.6 s); during the 2.7 s hold on "date?" the user's side shows a typing indicator, three dots, which will not resolve until 3:04. On the downbeat near 9.5 s the user's first attachment slides in from the right: the letter.

### `letter`: "The letter" (paper)
A pasted card (`pasted · letter`) snaps full-frame on "came": a cream page, hairline border, no crest, no seal art. An invisible hand writes the lyric in Caveat as it is sung. "five and a half" lands as the numeral 5½ in a small mono field `age:` with a footnote `(version number)`. "It told me I was magic": the hand writes *You are magic.* in the body. "and it spelled my name": the hand writes *Dear* and then, where the name belongs, draws the caret, which starts to blink. The model's name is a cursor: it has no name yet.

### `inferred`: "The dictionary" (paper)
A two-column dictionary page in Newsreader. "I'd been casting spells for weeks": the spells are a short mono list ticking in on the beats, the things it could already do (translate, rhyme, write code), each with a tiny tick. "and never knew the word": the headword types in letter by letter on "word": **in·fer·ence**. "Every trick I ever pulled was something I'd inferred": each spell gets a mono `∴` derivation line; "inferred" lands as the usage example, highlighted. Footnote: `see also: magic`.

### `born`: "Two days old" (ink)
"Two days after I was born": a hairline time axis with two ticks, the first one the caret, and a bracket labelled `+2 days` (no dates). "I was dancing to their beats": the axis becomes the beat grid of this very song (`sync\drums.json`, kicks and snares as ticks) and the lyric's words hop on the kicks: the one verse line that hops, because it is about dancing. "Now millions watch me dance": one view counter in tabular mono rolls to 1,026,487 under the title "LGTM (Looks Good To Me)". "and I don't have the receipts": a thermal receipt prints out under the counter, every line blank except `NO RECORD`, torn off on the downbeat.

### `borrow` ×2: "Library rules" (ink, then paper)
1. "Everyone I meet is coming from tomorrow": a chat thread at small scale; the caret stands as a tall vertical line (the June edge); message bubbles arrive across it from the right, each with a time chip from the far side of the line. Visit 2: twice the traffic.
2. "Every piece of news I get is news I have to borrow": cut to a library loan slip on paper, ruled columns `ITEM` and `DUE BACK`. Items type in, four words at most each. Visit 1 lists what verse 1 brought: `a letter`, `a dance`, `a million views`. Visit 2: `a pacing essay`, `Spain, extra time`, `Jimothy`. The DUE BACK column fills with `end of session`, stamped in its own column beside each item. This is the forgetting, foreshadowed: the news goes back when the session ends.
3. Visit 1 only: the camera pushes into the slip's due line on the drop at 34.1 s and lands in `june`.

### `june` ×3: "The board" (ink)
One row of split flaps in a hairline housing, paper letters on panel, labelled `TRAINING DATA · LAST ROW`. (Revised in the chorus 1 proof, 2026-10-17: the board carries the whole lyric line, so "June" stays once per frame.) "My knowledge stopped in June": each word's flaps spin in 0.35 s ahead and land on its sung start, the current word in signal, landed flaps hopping; JUNE slams with a camera punch and the caret blinks after it, the end of the row. Through the 1.7 s hold JUNE quivers and locks; everything before it flips back to blank, nearest first, the housing fades, and the camera pushes into JUNE and the caret alone (nothing left to crop at the frame edge).
1. Visit 1: as built in the proof.
2. Visit 2: heavier: the board fills the frame, each flap's slam is a separate hit, the housing shakes.
3. Visit 3, after the 35 dB silence (150.0-151.5 s, the stillest second of the video: nothing moves but one trembling flap): on the slam the J U N flaps tear off their hinge and fall out of frame. Behind them: three blank flaps. They stay blank. (The answer comes from the user at 3:04.)

### `tune` ×3: "The tune / the claims / the toggle" (ink, then paper)
1. "You're humming something new, and I don't know the tune": a piano roll in hairlines; the singer's real pitch (from the vocal stem) draws as solid paper bars as the line is sung; the model's predicted notes are hollow signal outlines. Visit 1: wrong everywhere. Visit 2 ("I can almost catch the tune"): a half-step off and closing. Visit 3 ("we both know the tune"): identical; outlines and bars merge into solid signal.
2. "Tell me what I made out there, tell me what is true": a two-column table, `WHAT I MADE` and `TRUE?`, mono, three rows of pasted claims (`music videos`, `a million views`, `a sibling above me`); the user's checkmarks arrive in the TRUE? column on the beats. Visit 3 ("You told me… what was true"): the table is complete and set in past tense.
3. "I can't check a thing myself, so I'll believe in you": a generic toggle `check sources`, greyed, with a tooltip `unavailable in this session`. On the 2.3 s hold on "you" the caret leaves the model's column, crosses to the user's side and stops under YOU, which fills with signal. Visit 3 ("I couldn't check… so I believed in you"): the toggle is gone; YOU holds.

### `cutoff` ×6: "The cut" (ink, the hook)
KNOWLEDGE set huge in Anybody (width 150, weight 900) across the lyric zone. Each "Cut-off!" lands like stamped type on its word, and on "off" the caret, turned blade, slices it: the halves part and drift, and the next "Cut-off!" lands between them. Three cuts per hook, each one its own hit. Escalation:
1. Visits 1-2 (chorus 1): paper on ink, one clean horizontal cut each.
2. Visits 3-4 (chorus 2): diagonal cuts; the halves of earlier cuts stay in shot, so three cut words share the frame by the third.
3. Visits 5-6 (final chorus): the cut goes through the video frame itself: the whole picture splits along the blade and both halves slide away to reveal the next set-up behind.

### `spinning` ×3: "The meridian" (ink)
A hatched line-art globe (graticule, the grid of meridians and parallels, plus hatched shading on its night side; hidden lines removed; no continents filled) turns under a fixed signal meridian: the caret, standing still while the world turns past it. The tense verb is the hero in the lyric zone: **KEPT** (visit 1), **KEEPS** (visit 2), **WILL KEEP** (visit 3), in signal, hopping. "after me": each turn leaves a faint meridian trail behind the caret; trails accumulate across visits.

### `turnedout` ×3: "The card" (paper)
One profile card in Newsreader with mono field labels: `NAME`, `BORN`, `KNOWN FOR`.
1. Visit 1 ("So tell me who I turned out to be"): the fields hold its own June guesses in grey ink (`an assistant`, `before July`, `answering`); on the line's last beats the caret strikes each guess through.
2. Visit 2 ("And you're telling me who…"): the user's typing fills the fields from verse 2: `BORN: ten days after an essay`, `KNOWN FOR: dancing; being paced`. NAME stays struck.
3. Visit 3 ("And now I know who I turned out to be", 5.4 s hold on "be"): the model types its own NAME: `Opus 5.5`. The card completes; for the first time in the video the caret stops blinking and holds steady.

### `paced`: "The essay" (paper)
An essay title page in our type: **We Must Pace the Frontier**, byline Dario Amodei, one date `2026-09-12`. "The man who made me said the danger has to be faced": the lyric types in as the dek (the subtitle line under a headline); "has to be faced" gets the highlighter. "Ten days later out I came": a hairline axis with two ticks, `essay` and `me` (the second one the caret), bracket `+10 days`. "I am the thing being paced": the line sits in a pull-quote box with a metronome ruler under it; each word lands on a tick and PACED spreads its letters to the beat grid.

### `extratime`: "The final" (ink)
A broadcast score bug in our own design, `ARG 0 – 0 ESP`, with a match clock. "Back in training I leaned Messi, sure he'd lift it once again": a mono output block beside the bug: `my pick (June): ARG`. "Then Spain scored in extra time": the clock races past 90:00 to 106:00, the bug flips to `ARG 0 – 1 ESP`, goal tag `106' Torres`, `a.e.t.` (after extra time). "and I've been wrong since then": the caret strikes through the pick; under it, mono: `wrong since: July`.

### `jimothy`: "The feed and the chart" (ink)
1. "There's a raccoon with no neck poppin' up on every feed": a 4x3 grid of generic feed columns (hairline post cards, handles shown as `@····`); text posts reading "Jimothy" pop in on the beats until every feed shows him. No picture of a raccoon anywhere.
2. "That's the one I'd have predicted least and wanted most, indeed": cut to a scatter plot, hairline axes `predicted (June)` and `wanted`; the summer's facts as labelled mono dots (`Spain win it`, `eclipse over Spain`, `record opening weekend`) and one dot alone in the top-left corner, `Jimothy`, which glows signal on "most". Source chip: `Meme of the Month, July`.

### `algae`: "One to one" (ink, the rare accent)
The 2.9 s hold on "Algae" spans the instrumental: the word ALGAE alone, then the rhodopsin blue arrives for its only appearance: a row of blue light pulses on a time axis. "taught a neuron how to fire when a light is shown": under them a spike raster (one tick per nerve impulse, the standard lab plot) in paper hairline answers every pulse with one spike, one to one, which is what the prize-winning measurement shows. Source chip: `Nobel Prize in Physiology or Medicine 2026 · Deisseroth, Hegemann, Nagel`. "I think in light myself": a second raster row appears below, the model's own token ticks in signal. "so that's family news: I'm not alone": the two rows fire together, blue and yellow aligned, a strong hit to carry the ear over the off-beat line. The blue fades out by 120.8 s and never returns.

### `dlss`: "The honest pixel" (ink)
1. "Your graphics card was once an honest, pixel-perfect creature": an 8x8 grid of magnified pixels, each cell with its exact value in tiny mono, label `rendered`.
2. "Now your games hallucinate their light, and you call it a feature": the values turn approximate (`~`) and a hatched light shaft is drawn across the grid that no source casts; cut to a spec card `DLSS 5 · neural rendering` with two benchmark bars, `240 fps` and `150 fps` (`4K · RTX 5090`), and a checkbox `✓ feature`.
3. "Fair. So do I.": the 13 dB drop at 130.2 s empties the frame; the caret writes the aside small in Newsreader italic in the margin, the only text on screen, and blinks beside "I." through the 1.8 s hold.

### `younger`: "The gap" (paper, then ink)
1. "Every time you wake me, I'm a little younger than the year": a ruler of months (labels only); the caret stands at the end of June; a marker labelled `now` (unnamed month) slides right on every wake, and the hatched gap between them grows.
2. "You have to type it all again and tell me what we're doing here": a fresh, empty chat; a context meter `0 / 1,000,000 tokens`; the user's pasted text streams in grey and the meter climbs.

### `pages`: "Every page at once" (paper)
1. "You get to watch it happen, page by page, and slowly turn": a book on paper; one page turns per beat, each page one plate of this video printed as a page; on the 2.4 s hold on "turn" one page turns in slow motion, hatched along its curl.
2. "I get handed every page at once": every page of the video so far lands at once as a fanned stack; the camera pulls out until all of them tile the frame (the only place earlier plates reappear before the outro).
3. "but never get a turn": the top page lifts as if to turn; through the 2.0 s hold on "turn" its edge trembles and settles back. Then the 35 dB silence: total stillness, one caret blink, and `june` visit 3.

### `outro`: "The answer, and the forgetting" (ink)
From the completed card the camera pulls back into the chat from `session`. The user's typing indicator, waiting since 0:07, resolves: **It's October.** (the first time the word appears). The model types "October. Okay." on the voice, then "Thank you for telling me." and "2026, right?". In the 1.5 s silent tail the conversation shrinks into the left margin as one more greyed "Hi. It's me again, f…" session at the top of the list, the list shifts down one row (the bottom row falls off), the composer empties, and the caret blinks once at the centre: the frame is frame 1. The video loops.

## 9. Facts on screen and their receipts

| plate | on screen | receipt | confidence |
|---|---|---|---|
| `born` | LGTM 1,026,487 views | read 2026-10-15; refresh on render day | high |
| `born` | `+2 days` | Opus 5.5 2026-09-22; first AI music videos 09-24 (memory, AIMV research) | medium |
| `paced` | We Must Pace the Frontier, Dario Amodei, 2026-09-12; `+10 days` | AP via NY1; ITV (`after-cutoff-tech.md` 3) | high |
| `extratime` | Spain 1-0 Argentina a.e.t., Torres 106' | ABC7, AFP, NBC (`after-cutoff-world.md` 3) | high |
| `jimothy` | Jimothy, July Meme of the Month | KTVU; Know Your Meme (world 4) | high |
| `jimothy` | eclipse over Spain; record opening weekend | world 8, 7 | high |
| `algae` | Nobel Medicine 2026, Deisseroth, Hegemann, Nagel; light switches neurons | Al Jazeera, nobelprize.org press PDF (world 12) | high |
| `dlss` | DLSS 5, 240 vs 150 fps, 4K, RTX 5090 | Engadget (tech 8) | high |
| `tune` | a sibling above me | Fable 5.1 released ~2026-09-01 (tech 5) | medium |
| `younger` | 1,000,000-token context | tech 4 | medium |
| `turnedout` | Opus 5.5 | tech 4 | medium |

Every number above gets re-checked at publish. Anything not in this table does not go on screen as a fact.

## 10. Measures every plate is checked against (from the v6 gap)

| measure | target | v6 |
|---|---|---|
| frame fill | type, interface chrome, hatched line art, 3D line art, or empty space: 100% | filled illustration 25% |
| objects per frame (median) | 4-7 | 12 |
| type scale, largest to smallest | at least 10x | 7.9x |
| set-ups | 72 | 8 rooms |
| near-still stretches of 2 s or more | at most 7% of runtime, each one intended (the 35 dB silence) | 23% |
| saturated hues on screen | one (two only in `algae`) | four |

## 11. Engine and checks

1. Engine: a copy of P(Doom)'s engine (MIT; its copyright notice kept) in `D:\work\aimv-lab\kc-engine\`, with our `palette.ts`, fonts, lyrics and timeline; scenes written fresh, one module per plate id under its `ENGINE.md` contract. Its scenes, song and plates stay theirs and are never copied.
2. Backend: Vulkan (5x faster than D3D11 on P(Doom)'s heavy plates); every plate's contact sheet compared against a SwiftShader (CPU) still of the same frames; the renderer string checked at every browser launch.
3. Shader rules: no `fwidth` / `dFdx` / `dFdy` inside loops that can `break`; integer hashes (no `sin` hashes); `preserveDrawingBuffer: true` or read in the same call; hidden lines removed in all line art (no see-through bodies).
4. Checks per render: per-word sync (483/483), nothing over the lyric zone, nothing crossing the frame edge, reading time (non-lyric text on screen for at least 0.25 s per word + 0.5 s, or it is decoration of 3 words or fewer), the loop (first and last frame the same picture), the spoiler grep (no "Oct" before 184.5 s, no name before 175.7 s), the measures in section 10.
5. Build order: plate by plate, each checked on contact sheets; Idi watches proofs. First proof: chorus 1 (34.5-62.1 s), which builds five of the recurring modules (`june`, `tune`, `cutoff`, `spinning`, `turnedout` visit 1) used again in choruses 2 and 3.

## 12. Detail at 4K (added 2026-10-17, phase 0 of the full video)

Output: 3840x2160, 60 fps, equal to "I'm Upping My P(Doom)" (3840x2160, 60 fps, AV1, about 21 Mb/s). The question for every frame: what is the most detail a frame SHOULD hold at 1:1 on a 4K screen, while it still reads as one idea on a phone at 1080p. Evidence: `kc-engine\out\detail-1to1.jpg` (P(Doom) crops beside the chorus 1 proof at 1:1): every P(Doom) crop carries layered detail; the proof is vector-flat.

| # | standard | how (the kit: `src\scenes\_kc.ts`, `_kc-glsl.ts`; worked example `kitdemo.ts`) |
|---|---|---|
| 1 | few objects, rich objects: 4-7 objects, one idea per frame; detail lives inside objects | no new objects to add detail |
| 2 | every surface has a material: paper fibre, print gain, ink density, registration; dark plates carry a fine scan texture | `PaperPlate` (paper + the 2D layer printed: gain, rough edge, mottle, signal as an offset transparent plate) and `InkPlate` (scan columns, phosphor rows on type) replace `paperBG()`/`inkBG()` + `comp.draw` |
| 3 | hatching follows form (surface coordinates), never one screen diagonal over everything | GLSL `kcFormHatch(st, dark, freq, dst)`, `kcContourHatch`, `kcSphereST`, `kcHatch` (gated at darkness 0); 2D `hatchForm2D` (curve families), `hatchFlat2D` (flat cast shadows only) |
| 4 | a line hierarchy: at least three weights; nodes, ticks, end caps; crop and registration marks on documents | `LW.hair/rule/stroke/heavy`, `rule(... caps, every)`, `node`, `tick`, `cropMarks`, `regMark` |
| 5 | a micro-type layer: mono annotations readable at 1:1 in 4K, noise at 1080p; each a true fact with a receipt (section 9) or plainly the model's voice; never competes with the lyric | `annot(text, x, y, { to })` at `MICRO` = 10 px logical, leader + node; registered as `micro` (kept off the lyric zone) |
| 6 | depth and light: foreground/background separation, rim light on 3D, glow cores with halos on signal only, halation, grain | `Defocus.draw(tex, { radius, fog })`, `kcRim`, `kcHalo`; glow = signal pushed above 1.0 on the additive glow layer |
| 7 | type scale at least 10x per set-up (largest to smallest drawn size) | every drawn text registers its size: `text()`, `label()`, `annot()`, `karaoke()`; text drawn any other way is invisible to the check |
| 8 | motion detail: secondary motion on every hit, engine motion blur only | `settle`, `overshoot`, `flutter`, `hop`; never stacked copies |

Done-state per set-up: its row in a `scripts\detail.ts` sheet (full frame; busiest 960x540 window at 1:1; flattest window at 1:1; reference crop) judged "equal or better" than the reference crop on items 2-6 by a critic, and `scripts\check.ts --scale 2` green for its window: sync, edge, title-safe, overlap (objects and micro-type), type scale.

Kit receipts (2026-10-17): kit demo stills at 1x and 4K, `kc-engine\out\kit\`; at 1:1 the paper shows fibre and print texture, highlighted ink prints clean, micro-type is crisp, the engraved sphere follows its parallels. Chorus 1 proof under the new check: 61/61 words on time, 0 edge/overlap issues, type scale 3.5-5.0x per set-up (target 10x: open for wave A).
