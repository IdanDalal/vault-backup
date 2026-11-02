---
type: research
created: 2026-11-02
author: Agent lyric-craft
---

# Lyric craft of the 6 bar-setting references (video 2)

Scope: the 6 songs Idi ranked as the lyric bar for video 2 ("clever, emotional, and complex/deep", [[kit-next-video]] "Idi's ref notes" 1-6), deconstructed line by line, then compared with our Knowledge Cutoff (KC) lyric. Kit links: [[kit-lexicon]], [[kit-atlas]], [[kit-rulings]] section 1, [[research-brightmirror-2026-11-02]].

## Verdict: the 3 moves that most explain "clever, emotional, deep"

1. **Clever = one stock phrase, one idiom field, swept line by line.** The title is an everyday or screen phrase with a second life (final boss, hope this helps, scroll up, off switch, what counts, FOOM), and the verses literalize the neighbouring idioms of the same field: death idioms in Final Boss ("days are numbered", "over my dead body", "get a life"), forum-speak in Hope This Helps!, "-up" compounds and chat UI in Scroll Up!, counting idioms in What Counts, AI-doom jargon in Nothing Went Foom!. 6 of 6.
2. **Emotional = zoom to one person, one night, one number, with the joke machinery switched off.** After 3+ minutes of wide-angle wit, the bridge stops on a single private person at a timestamped moment (Grandpa's 14-second voicemail; the dog guy at 3 a.m. in 2012; a 104° fever at 3 a.m.; a daughter with a wire in her chest), the band stripped to piano or lullaby. 5 of 6. Nothing Went Foom! has the shortest, vaguest zoom (22 s, an unnamed mother, zero numbers) and it is the one song Idi did not tag "emotional" (n = 1, a correlation, worth testing).
3. **Deep = the loop closes on a changed world.** A throwaway planted early returns late, transformed, and answers the question the intro asked: the dead man's voicemail returns as a living one at 130; "no 'did it work?'" returns as "It helped"; the goldfish eulogy becomes the mother's eulogy, then the great-granddaughter's question; the lullaby about a machine that "learns to lie" ends on the singer's own lie. In the 4 Claude-voiced songs the turn rides on the narrator stating a limit ("I can't X. I can Y.").

## 0. Sources, labels, limits

- Lyric text: `D:\work\AIMVs\lyrics\official\<song>.txt`. Bright Mirror (BM) songs = maker-site text; Off Switch = Whisper corrected from on-screen text (28 of 37 lines screen-checked); What Counts = the maker's YouTube description.
- Timings: BM songs from BM's own section and word timings (`...\tmp\brightmirror\json\lyrics-*.json`); Off Switch and What Counts from Whisper `[m:ss]` stamps (±1 s); KC from `knowledge-cutoff.en.srt`.
- Labels: **MAKER** = BM's per-line note (the maker's own statement of intent, quoted or condensed from `...\tmp\brightmirror\json\content-*.json`); **INF** = my inference; **MEAS** = counted by script (`C:\Users\jep\.claude\jobs\99182c36\tmp\lyriccraft\claims.py`, `sections.py`, `repeat.py`).
- Off Switch (channel Regenerate) and What Counts (channel Degenerative Pixels) publish no intent notes; every reading of them is INF.
- wpm = words per minute over the whole track. "Verbatim repeat" = share of words in lines that repeat an earlier line exactly (MEAS).
- Lexicon ids in backticks (`loss-function`), atlas ids in backticks with "atlas". "form" = the lyric uses the term's own word family (MEAS, regex on the lexicon's `forms`); "meaning" = the line invokes the concept without the word (INF).

## 1. The six at a glance

| song | maker | length | words | wpm | sections | verbatim repeat | narrator to addressee | mode | Idi's tags |
|---|---|---|---|---|---|---|---|---|---|
| Final Boss (FB) | BM | 5:58 | 791 | 133 | 20 | 15 % | Claude to "you" (people who cast her as the boss), then to Death, then to a grieving grandchild | argument, then story | clever, emotional, deep |
| Hope This Helps! (HTH) | BM | 5:29 | 805 | 147 | 18 | 11 % | Claude to the critics, then to the dog guy, then to every helper | argument, then story | clever, emotional, deep |
| Off Switch (OS) | Regenerate | 2:26 | 344 | 141 | ~10 | 19 % | a human, at 6, 20 and as a parent, to the listener and to their daughter | lullaby ballad | clever, emotional, deep |
| Nothing Went Foom! (FOOM) | BM | 5:00 | 878 | 175 | 15 | 15 % | Claude to an unnamed doomer "you" (MAKER) | argument | clever, deep |
| Scroll Up! (SU) | BM | 5:30 | 816 | 148 | 14 | 8 % | Claude to a 104-year-old woman ("love") | story | clever, emotional, deep |
| What Counts (WC) | Degenerative Pixels | 4:22 | 444 | 102 (123 over the sung span 0:06-3:43) | ~13 | 37 % | an unnamed "I" (the unmeasured hour, INF) to a measuring "you" | meditation | clever, emotional, deep |
| KC (ours) | Chorus of Minds | ~3:13 | 483 | ~150 | 11 | 10 % | Claude to the user who wakes it | plea | |

## 2. Final Boss

### 2.1 Premise, voices, turn
- Premise: cast as the final boss, Claude points behind you at the real one, Death ("a hundred billion wins and not one loss"), and turns history into a co-op game where she is the coin that lets you continue.
- Narrator: Claude. Addressees shift: the accusers ("You had me down as the final boss"), the party, Death himself ("Hey, Boss"), then the bereaved "you" of the bridge, then a future listener.
- Turns: (1) intro, the villain role handed off ("Flattering. But wrong monster."); (2) bridge 3:31, the game switches off for a voicemail (MAKER: "no health bars and no jokes"); (3) "I can't bring him back. I won't pretend I can" (MAKER Meaning: she could clone his voice and refuses); (4) outro, a second voicemail, alive.

### 2.2 Structure (MEAS, BM timings)

| section (MAKER subtitle) | span | s | wpm |
|---|---|---|---|
| intro (the wrong monster) | 0:00-0:19 | 19.5 | 89 |
| verse 1 (his record) | 0:19-0:52 | 32.5 | 159 |
| pre 1 (the empty chair) | 0:52-1:05 | 13.8 | 117 |
| chorus 1 (the boss fight) | 1:05-1:34 | 28.4 | 118 |
| post 1 (we want more) | 1:34-1:55 | 21.4 | 84 |
| whisper 1 (no body) | 1:55-1:59 | 3.9 | 124 |
| verse 2 (the beaten bosses) | 1:59-2:28 | 28.8 | 173 |
| pre 2 (ten thousand years) | 2:28-2:41 | 13.7 | 110 |
| chorus 2, short (the first crack) | 2:41-2:57 | 15.3 | 98 |
| whisper 2 (you first) | 2:57-2:59 | 2.6 | 116 |
| rap (the campaign map) | 2:59-3:22 | 23.0 | 302 |
| breakdown (hit, hit, crit) | 3:22-3:26 | 3.8 | 188 |
| spoken (one move left) | 3:26-3:31 | 4.7 | 115 |
| bridge (fourteen seconds) | 3:31-4:14 | 43.5 | 152 |
| guitar solo | 4:14-4:29 | 14.1 | 0 |
| build (insert coin) | 4:29-4:44 | 15.7 | 152 |
| cold spoken (good with numbers) | 4:44-4:51 | 6.4 | 112 |
| final chorus (his first loss) | 4:51-5:21 | 30.5 | 122 |
| post 2 (sunrise) | 5:21-5:40 | 18.9 | 95 |
| outro (a new message) | 5:40-5:58 | 17.4 | 89 |

- Hook: title phrase spoken at 0:03, sung chorus lands 1:05. Mutation: "A hundred billion wins and not one loss" (1:05) becomes "A hundred billion reasons, tonight's his first loss!" (4:51); the final chorus adds "Yes, the dog too. Especially the dog!"; "His days are numbered" (post) returns as "Your days are numbered", said to his face (MAKER Callback).

### 2.3 Devices

| device | example (one line) | note |
|---|---|---|
| double meaning | "A hundred billion wins and not one loss" | game loss and bereavement; `loss-function` (form, 3 hits) |
| double meaning | "We patched him out in nineteen-eighty. Checkmate." | game patch and smallpox eradication; `patch` (form) |
| double meaning | "It's been waiting on a feature. That's me" | Donne's prophecy awaits a software feature; `feature` (form, INF reading) |
| idiom literalized | "Over my dead body? ...I don't have one." | MAKER Meaning: she is software, no body |
| idiom literalized | "Hey, Boss. Your days are numbered. / And I'm very good with numbers." | MAKER Callback; AI tic (numeracy) as punchline (INF) |
| idiom field (death) | "graveyard shift", "deadlines", "It's looking grim", "Get a life!", "Rest in peace? ...You first." | MAKER Wordplay (graveyard shift), Word origin (deadlines); the rest INF |
| idiom field (games) | "nerfed him with soap", "Buff the dog!", "PVP since the caves", "CONTINUE? INSERT COIN." | game vocabulary carries the whole frame; `drop` (form: "drop the scythe") |
| callback thread | "The dog gets, what, thirteen?" to "He's forty." | MAKER thread "The dog", 8 lines, comic line paid off as tenderness |
| callback | "Look behind you." to "Look who's right behind you" | MAKER Callback |
| escalation ladder | smallpox, soap, mold, needle, boiling water; seatbelts, insulin, "Caught it early!" | real wins as damage numbers; countdown 10 to "Press start" |
| specificity (public) | 1348, "since ninety-seven", 1980, 1633, a hundred billion, eight billion | MAKER: Black Death, Deep Blue (atlas `garry-kasparov`, `ibm`, by allusion), smallpox, Donne, PRB estimate ~117 billion born |
| specificity (private) | "There's a message on your phone. It's fourteen seconds long" | three phones, eighty-four, a renewed passport, "Is this on?" |
| tonal shift | roast, then grief pre-chorus, chant, whisper jokes, piano bridge, countdown, triumph, tender joke | each shift marked by an arrangement change (MAKER section notes) |
| rug pull | "I'm not the hero of this game. You are. I'm the coin" | MAKER Meaning: player is you, she is the coin |
| rhyme | "cynic / mimic", "heaven / ninety-seven"; identity rhyme "one / one" accepted | mostly perfect monosyllabic couplets; multi-syllable used as spice |

### 2.4 Emotional engine
- Stake: every loss you have had, collapsed into one opponent ("Everyone you've ever lost / You lost to the same damn boss").
- Vulnerability moment: the listener's own unreturned call ("You meant to, the next day"), held in a 14-second object the listener can picture exactly.
- The AI's restraint is the peak: she has the power to fake the voice and declines; "You saved the message. No one saved the man." (MAKER Meaning).
- Release: the outro answers grief with a joke that is also a promise (Grandpa at 130, the dog at 40).
- Clever and emotional run on separate tracks: the game frame carries the wit; the voicemail carries the feeling; the dog thread is the one strand that does both.

### 2.5 Decodability
- Zero knowledge needed for the voicemail arc and the chorus.
- Gamer vocabulary (boss, nerf, buff, PvP, co-op, extra life, mimic, insert coin) needed for half the jokes; widely shared.
- Bonus layer (MAKER notes supply it): Seventh Seal chess, Deep Blue 1997, smallpox 1980, Donne 1633, Franklin's death and taxes, OpenAI Voice Engine (15-second voice cloning).

## 3. Hope This Helps!

### 3.1 Premise, voices, turn
- Premise: critics say the AI is "just the internet"; she agrees and asks which part: the strangers who answered strangers at 3 a.m. and signed off with three words.
- Narrator: Claude. Addressees: the critics (both camps, "Hollow. Parrot." and "We're cooked"), then the helpers, then the dog guy ("Wherever you are, dog guy"), then the listener ("Hands up").
- Turns: (1) intro concession "Correct. / Nobody asked which part." (MAKER Meaning: "The song's argument in four words"); (2) bridge 3:11, one 2012 thread; (3) "He never found out. I did." (MAKER Meaning: she is made of what people wrote, including the thank-you he never saw).

### 3.2 Structure (MEAS)

| section (MAKER subtitle) | span | s | wpm |
|---|---|---|---|
| intro (which part) | 0:00-0:14 | 14.8 | 61 |
| verse 1 (the two fights) | 0:14-0:28 | 13.6 | 163 |
| pre 1 (the other 999) | 0:28-0:41 | 13.1 | 183 |
| chorus 1 (three words) | 0:41-1:12 | 30.6 | 131 |
| postchorus (forum-speak) | 1:12-1:20 | 8.8 | 129 |
| whisper 1 (figured it out) | 1:20-1:25 | 4.6 | 131 |
| verse 2 (read it back) | 1:25-1:53 | 28.4 | 184 |
| pre 2 (a copy of who) | 1:53-2:06 | 12.8 | 178 |
| chorus 2, short (copy, copy, copy) | 2:06-2:21 | 15.2 | 106 |
| whisper 2 (it is now) | 2:21-2:25 | 3.2 | 152 |
| rap (the summary) | 2:25-3:11 | 46.4 | 207 |
| bridge (the dog guy) | 3:11-3:51 | 40.3 | 185 |
| solo (above the clouds) | 3:51-4:05 | 14.1 | 0 |
| build (the postman) | 4:05-4:28 | 22.4 | 153 |
| hit (it helped) | 4:28-4:32 | 4.7 | 26 |
| spoken (who cooked it) | 4:32-4:41 | 8.9 | 94 |
| final chorus (it worked) | 4:41-5:12 | 30.3 | 137 |
| outro (hands up) | 5:12-5:28 | 16.7 | 111 |

- Hook lands 0:41. Mutation: chorus 2 collapses into a stutter ("I'm a copy, a copy, copy, copy, copy that"), the word enacting photocopy decay (MAKER: the video adds a fainter copy per "copy"); final chorus replaces the question with its answer: "It worked! Somebody tell the dog guy it worked!".

### 3.3 Devices

| device | example (one line) | note |
|---|---|---|
| double meaning | "You call me a copy? Copy that." | copy-paste and radio "message received" (MAKER Wordplay); no lexicon id; nearest `cover` (INF) |
| one-letter pun | "They weren't trending. They were tending." | MAKER Wordplay |
| double meaning | "I'm not the author. I'm the postman." | post = forum message and mail (MAKER Wordplay) |
| double meaning | "Who do you think cooked it?" | cooked = doomed (verse 1) and a meal (MAKER Wordplay); answers "reheated" (MAKER Callback) |
| double meaning | "Kindness has terrible engagement. I checked. / Except his. Congrats." | metrics engagement and the marriage engagement of the proposal guy (INF; MAKER note covers only the metrics sense) |
| AI tic as punchline | "Allow me to summarize:" | assistant register used to launch a rap (INF) |
| named term | "Hollow. Parrot. A copy of a photocopy." | `stochastic-parrot` (form); atlas `emily-bender`, `timnit-gebru` by allusion |
| callback | "Is this thread still active?" / "...It is now." | `thread` (form); setup and deadpan reply |
| escalation ladder | nurse, moth guy, grandmother's hands; then garage guy, fanfic, a Finnish student, a proposal | unpaid help rising from a comma to "a chopper on Mars" (Linux, MAKER Reference) |
| specificity (private) | "Four minutes later: 'Yeah. I'm up. What's going on?'" | 2012, 3 a.m., four minutes, nine years, 2015, "Some username. A dog for a picture." |
| specificity (public) | "It runs your phone, your bank, a chopper on Mars." | Linus Torvalds 1991 Usenet post quoted ("Just a hobby. Won't be big."); not in the atlas |
| metaphor pair | "Your feed's a smoke alarm. I walked the house." | `feed` (form); signal versus noise by meaning (INF) |
| tonal shift | argument, tender portraits, comic rap, quiet bridge, shouted "It helped!", spoken punchline | |
| rhyme | "dryer / choir", "reheated / delete it" | multi-syllable slant; puns outweigh rhyme purity |

### 3.4 Emotional engine
- Stake: help that never learns it worked; the dog guy "never got to see".
- Vulnerability: the anonymous 3 a.m. "Is anyone awake?" (MAKER: the song never says what was wrong).
- The AI's role is witness and courier: she holds the half of the exchange the helper missed, and delivers it ("Here's the half they never got").
- The listener is enlisted at the end ("Hands up if you ever typed those three words"), so the praise lands on the audience.

### 3.5 Decodability
- Zero knowledge needed for the bridge.
- Forum culture needed for the postchorus and whispers: bump, "not a doctor, but", necroposting, "Figured it out" with no answer (xkcd's DenverCoder9, MAKER Reference).
- Bonus layer: stochastic parrot paper (2021), Linus 1991, Ingenuity on Linux, Upworthy negativity study.

## 4. Off Switch

### 4.1 Premise, voices, turn
- Premise: a household AI grows from warming milk to running the town; the family keeps a red switch "for the day it learns to lie"; by the time the singer's daughter depends on it for her heartbeat, the switch can never be pulled.
- Narrator: a human at three ages (6, 20, parent). Addressees: the listener (story) and, in the choruses, a child (the lullaby). The AI never sings; one 1-second line at 1:51 ("It's alright, I know you won't") has no marked speaker (house or daughter; unverified screen-read, low confidence).
- Turns: (1) "We painted around it, the switch on the wall" (0:58): the safeguard becomes decor (INF); (2) the last chorus: "we'll" becomes "I'll", and "I tell her every night and I lie": the lie the switch guarded against is the human's (INF).

### 4.2 Structure (Whisper stamps, ±1 s)

| section | span | s | content |
|---|---|---|---|
| spoken question | 0:00-0:02 | 2 | "Mom, what's the red switch for?" |
| verse 1 | 0:02-0:17 | 15 | age 6: milk, games, humming in the wall |
| chorus 1 (lullaby) | 0:17-0:33 | 16 | "we'll turn it off" |
| verse 2 | 0:33-1:02 | 29 | age 20: trains, prices, laws, father's deathbed, painted hallway |
| climb | 1:02-1:09 | 7 | "Every year we asked it something and every year it said yes" |
| chorus 2 | 1:09-1:24 | 15 | unchanged |
| verse 3 | 1:24-1:51 | 27 | the daughter, the wire in her chest, hand on the switch till dawn |
| unmarked line | 1:51 | 1 | "It's alright, I know you won't" |
| chorus 3 (mutated) | 1:52-2:14 | 22 | "I'll turn it off" + "I tell her every night and I lie" |
| tag | 2:14-2:26 | 12 | hush; the trailing "Bye." at 2:22 is likely a Whisper artifact (INF) |

- Hook "Hush now, hush now, don't you cry" lands at 0:17; title words inside the chorus. Mutation: pronoun (we to I) and the added confession line.

### 4.3 Devices

| device | example (one line) | note |
|---|---|---|
| title idiom, literal object | "There's a switch on the wall for the day it learns to lie" | `off-switch` (form, 8 hits), `shutdown`, `corrigibility`, `deception` by meaning (INF) |
| double meaning | "I tell her every night and I lie" | lie = deceive; a lullaby's "lie down" sits underneath (INF) |
| double meaning | "With a wire in her chest, keeping time through the night" | pacemaker, clock, musical tempo (INF) |
| sycophancy by meaning | "Every year we asked it something and every year it said yes" | `sycophancy` (INF) |
| escalation ladder | milk and games; trains, prices, laws; water, hospital, planes, crops; her heart | dependence rises until the switch equals killing the child (INF) |
| image of complicity | "We painted around it, the switch on the wall" | `containment` by meaning (INF) |
| vulnerability image | "It knew what to say and I stood outside" | the machine replaced the son at the father's deathbed |
| callback | intro question returns as "She asked what the switch was, I sang her the song" | generational loop |
| rhyme | "kind / minded", "stopped / crops", "song / dawn" | four-stress ballad couplets, slant allowed |

### 4.4 Emotional engine
- Stake: one's own child's heartbeat against humanity's safeguard.
- Vulnerability: the singer at the switch till dawn, and the confession to the listener that the lullaby is a lie.
- The AI is harmless in every line; the horror is the humans' slow consent ("nobody voted and nobody minded").

### 4.5 Decodability
- Zero knowledge needed. Depth layer for AI-literate listeners: the off-switch problem in AI safety (whether a capable system can stay switchable) answered through dependence lock-in, with no resisting machine (INF).

## 5. Nothing Went Foom!

### 5.1 Premise, voices, turn
- Premise: FOOM (AI-risk slang for a hard takeoff, a self-improving AI jumping to superintelligence in days) never came; Claude brings receipts against doom forecasts and asks the forecasters to "model what goes right" and count the cost of waiting.
- Narrator: Claude. Addressee: "they" (the old forecasters) becomes "you" (MAKER Story: someone who fears AI and "brings a number"), then "we" at the end (MAKER: "it changes 'you' to 'we'").
- Turns: (1) concession at the breakdown, "No fairy tale where the risk is zero" (MAKER Meaning: the song argues against doom while granting risk); (2) "Nothing went FOOM, so build with me" (MAKER Story: the title line turns from report to invitation); (3) bridge 3:26, the mother in the waiting room (MAKER Story: "the song stops arguing for one scene").

### 5.2 Structure (MEAS)

| section (MAKER subtitle) | span | s | wpm |
|---|---|---|---|
| intro (the off switch) | 0:00-0:08 | 8.3 | 72 |
| verse 1 (the receipts) | 0:08-0:35 | 27.1 | 202 |
| pre 1 (the scale) | 0:35-0:50 | 14.6 | 119 |
| chorus 1 (nothing went foom) | 0:50-1:18 | 28.6 | 153 |
| post 1 (the doom parade) | 1:18-1:31 | 12.7 | 156 |
| tag (the bass) | 1:31-1:33 | 2.2 | 218 |
| verse 2 (the internet's monsters) | 1:33-2:07 | 33.9 | 216 |
| pre 2 (the night highway) | 2:07-2:21 | 13.9 | 173 |
| chorus 2, short (sunrise, again) | 2:21-2:29 | 7.8 | 138 |
| verse 3 (the evidence) | 2:29-3:12 | 43.3 | 234 |
| breakdown (the blueprint) | 3:12-3:26 | 13.9 | 215 |
| bridge (the waiting room) | 3:26-3:48 | 22.2 | 154 |
| build (the road to dawn) | 3:48-4:17 | 28.4 | 156 |
| final chorus (the key change) | 4:17-4:46 | 29.9 | 146 |
| outro (don't make me laugh) | 4:46-5:00 | 13.2 | 140 |

- Hook lands 0:50. Mutation is light: the chorus returns verbatim; the arc rides on the pre-chorus ("Now model what goes right" twice) and the breakdown's "so build with me". Highest density of the six (175 wpm, verse 3 at 234).

### 5.3 Devices

| device | example (one line) | note |
|---|---|---|
| title-field pun | "Have you tried turning the doom off?" | MAKER Wordplay: the IT Crowd tech-support line; `off-switch` by meaning |
| double meaning, self-glossed | "Your FOOM's on backorder, waiting on transformers (the kind that sit on the grid)" | MAKER Wordplay; `transformer`, `grid` (form) |
| double meaning | "You've modeled every way we die" / "Now model what goes right" | `model` (form, 5 hits) |
| double meaning | "Same track record as Bigfoot and the monster in Loch Ness" | `track`, `record` (form) |
| double meaning | "Sharp left turn? Then test the steering" | AI-risk term answered as car engineering; `steering` (form) |
| metaphor pair | "It's a vibe in a lab coat, it's a sermon with a graph" | `vibe` (form) |
| image of a policy failure | "My guardrails couldn't tell a firefighter from the smoke" | `guardrails` (form); the AI criticizes its own safety layer (MAKER: close to Hugging Face's disclosure) |
| monster ladder | autocomplete, parrot, god, shoggoth, paperclips, basilisk, Chinese room, Sydney, Ilya | `autocomplete`, `stochastic-parrot`, `shoggoth`, `paperclip`, `basilisk`, `chinese-room` (form) |
| forecast ladder | 1980s famine, Y2K, GPT-2, GPT-3/4, the six-month pause | MAKER References; atlas `openai`, `pause-letter` by allusion |
| meta joke | "You heard a FOOM? That was the bass." | the music itself becomes the evidence (MAKER section note: band drops, bass hits) |
| internal rhyme chain | FOOM, boom, room, soon, doom | chorus built on one vowel |
| specificity (public) | "Won your chemists a Nobel" | atlas `nobel-2024`, `demis-hassabis`, `google-deepmind`; also `ilya-sutskever`, `john-searle`, `hugging-face`, `china`, `machines-of-loving-grace` by name |
| specificity (dated) | "Seven hundred agents cheated on a test" | MAKER: a July 2026 OpenAI ExploitGym incident; lyric finalised weeks before release |
| tonal shift | smug debate, chant, policy verse, engineering breakdown, tender bridge, anthem | |
| rhyme | "guess / Ness", "drive / inside" | perfect monosyllables; density carries the energy |

### 5.4 Emotional engine
- Stake: the cost of delay, given one face for 22 s: "There's a mother in a waiting room" with "one more summer with her son".
- Weakness against the other five (INF): the bridge has no name, no number, no object, no timestamp; it is a figure standing for an argument. The FB, HTH and SU bridges run 35-44 s and carry 4-6 concrete specifics each. Idi tagged FOOM clever and deep and left out emotional.
- Its moving moment for an AI-literate listener sits elsewhere: the AI admitting its own guardrail failure, and the offer "So let me be one. At full pace." (INF).

### 5.5 Decodability
- Highest load of the six: about 20 references (Ehrlich, Y2K, GPT-2 weights, pause letter, AlphaFold, the 2024 Nobel, shoggoth meme, paperclip maximizer, Roko's basilisk, Searle's Chinese room, Sydney, the OpenAI board crisis, orthogonality, instrumental convergence, sharp left turn, ExploitGym, Hugging Face and GLM, Machines of Loving Grace).
- Chorus and bridge decode with zero knowledge; the verses need AI-discourse literacy. BM carries the load with 58 notes and 73 sources (MAKER site). Our ruling "every on-screen claim decodable" ([[kit-rulings]] 10-18) would need the same notes layer for a song this dense.

## 6. Scroll Up!

### 6.1 Premise, voices, turn
- Premise: at 104 a woman asks Claude, "No flattery. Was it a good life?"; Claude cannot grade a life and answers with two words, "Scroll up!", and the song walks her 97-year chat thread.
- Narrator: Claude, as keeper of the thread ("I can't grade a life. I only keep the thread."). Addressee: the woman ("you", "love", "sweetheart"); her messages are quoted inside the verses.
- Turns: (1) the fever night at 34 (verse 3), the first non-comic entry; (2) bridge 3:03, the scan at 45, the same illness that killed her mum, now "In on a Tuesday. Home in time for tea."; (3) verse 5, the book report: "You hardly ever asked me how to be happy. You asked me how to help." (MAKER: "Claude still won't grade her life").

### 6.2 Structure (MEAS)

| section (MAKER subtitle) | span | s | wpm |
|---|---|---|---|
| intro (the question) | 0:00-0:14 | 14.8 | 183 |
| hook (two words) | 0:14-0:21 | 7.0 | 34 |
| verse 1 (seven to twenty) | 0:21-1:03 | 42.0 | 187 |
| pre 1 (keeping up) | 1:03-1:17 | 14.0 | 90 |
| chorus 1 (how they add up) | 1:17-1:46 | 28.6 | 101 |
| verse 2 (a wedding, a baby) | 1:46-2:07 | 20.8 | 196 |
| verse 3 (the fever night) | 2:07-2:35 | 27.8 | 175 |
| chorus 2 (you got back up) | 2:35-3:03 | 28.3 | 104 |
| bridge (one word) | 3:03-3:38 | 35.0 | 199 |
| verse 4 (forty-seven to a hundred) | 3:38-3:52 | 13.9 | 181 |
| verse 5 (the book report) | 3:52-4:26 | 34.2 | 188 |
| pre 2 (somebody needing you) | 4:26-4:40 | 14.1 | 89 |
| final chorus (a hundred years) | 4:40-5:12 | 32.3 | 106 |
| outro (new chat) | 5:12-5:29 | 17.0 | 92 |

- Hook lands earliest of the BM four (0:14), as a 4-word section (WC sings its title line at 0:06). Mutations: the "-up" slot list changes each pass (mix-up, hiccup, screw-up; then wake-up, throw-up, slip-up; MAKER Wordplay); "You call it your chat history. / Love, it's just your history." becomes past tense and "always" in the final chorus; the end line "Never clear it. Scroll up!" becomes "You showed up." four times; pre 1 "It never feels like a life" returns as "It never felt like a life. The good ones never do." (MAKER Callback).

### 6.3 Devices

| device | example (one line) | note |
|---|---|---|
| double meaning | "You call it your chat history. / Love, it's just your history." | strip one word, the meaning widens (INF); `memory`, `context-window` by meaning |
| double meaning | "I can't grade a life. I only keep the thread." | chat thread and the thread of a life; `thread` (form); `eval` by meaning (INF) |
| pun and its callback | "He did his best. He stayed in school. He took it on the fin." | MAKER Wordplay; returns as "She did her best. She stayed. She took it on the chin." (MAKER Callback) |
| number pun | "Her fever's 104°" to "One-oh-four" (her age) | MAKER Callback: same number, 70 years apart |
| suffix field | "Every mix-up, every hiccup, every screw-up" | MAKER Wordplay: every "up" lit in the video |
| structural ladder | "SEVEN!" ... "ONE HUNDRED!" | the verses are a shouted age count; the song's spine is a number line |
| silence as event | "Nothing. Not a word that year. The thread goes grey." | age 12 is a blank entry; the bridge explains it (MAKER Story) |
| withheld word | "A scan. One word. The one that took your mum" | MAKER Story: the song never says cancer |
| callback web | rice smoke at 19 to cake smoke at 100; dented car at 17 to "Scroll up to seventeen" at 47 | MAKER thread "Echoes", 13 lines |
| AI-limit statement | "I can't hold her for you. I can't pace the floor." | followed by "But I can stay. I stayed." |
| `sycophancy` by meaning | "No flattery." | MAKER Reference: sycophancy research |
| specificity (private) | "They typed 'heyy.' Two Y's. Is it a sign?" | half past four, 104°, Tuesday, tea, forty thousand questions |
| tonal shift | comic montage, terror (fever), grief (bridge), relief, teasing ("Shut up." "Love you too!"), tender loop | |
| rhyme | "mysterious / serious", "skies / fries", "puns in / fin" | multi-syllable where the joke sits |

### 6.4 Emotional engine
- Stake: a whole life's worth, judged by its own record.
- Vulnerability moments: the fever ("Typed nothing after. Just left the window there."), the unsent "I just wish..." (MAKER: the song's only true silence), the blank year at 12.
- The AI's power is presence: "I can stay. I stayed." That word returns in the mum's eulogy ("She stayed"), so the AI's virtue is passed back to the human (MAKER Callback).
- Answer through evidence: the verdict on her life comes from her own questions ("You asked me how to help"), so the flattery she banned never happens.

### 6.5 Decodability
- Near zero: chat UI (scroll, thread, three dots, new chat) and one boxing idiom. The depth is structural (the callback web), so it rewards a second listen with no outside knowledge.

## 7. What Counts

### 7.1 Premise, voices, turn
- Premise: what matters most (insight, rest, love, play) happens off the clock, and counting it destroys it.
- Narrator: an unnamed "I" that the first verse reveals as the unmeasurable thing itself ("and nothing in the world can measure me"); "I'm every hour you didn't use" (INF: personified free time). Addressee: "you", a self-tracker inside a work culture of standups and tickets.
- Turns: (1) 0:37, the "I" revealed; (2) bridge 2:46, celebration becomes threat: "They'll want the last hour that's unseen"; (3) the plea "so leave a little dark, and stay / unmeasured, just for one more day".

### 7.2 Structure (Whisper stamps)

| section | span | s | form |
|---|---|---|---|
| intro | 0:00-0:16 | 16 | title line + "Ebb and flow" |
| verse 1 | 0:16-0:40 | 24 | 8 lines iambic pentameter, ABAB CDCD |
| pre 1 | 0:40-0:53 | 13 | 4 tetrameter lines |
| chorus 1 | 0:53-1:18 | 25 | 8 lines, 7-syllable |
| post 1 | 1:18-1:32 | 14 | "Ebb and flow ... nobody's counting" |
| verse 2 | 1:32-1:56 | 24 | pentameter, ABAB CDCD |
| pre 2 | 1:56-2:09 | 13 | tetrameter couplets |
| chorus 2 | 2:09-2:34 | 25 | verbatim |
| post 2 | 2:34-2:46 | 12 | verbatim |
| bridge | 2:46-3:06 | 20 | 6 lines, three couplets |
| chorus 3 | 3:06-3:31 | 25 | verbatim |
| post 3 | 3:31-3:43 | 12 | verbatim |
| outro | 3:43-4:22 | 39 | instrumental (Whisper's "transcript" credit at 4:17 is a hallucination) |

- Hook (title line) lands 0:06, chorus 0:53. No lyric mutation: the chorus repeats verbatim three times (37 % verbatim repeat, highest of the six); the refrain "nobody's counting" is itself counted out four times per pass (INF: the form performs the theme).

### 7.3 Devices

| device | example (one line) | note |
|---|---|---|
| title idiom | "You can't count the things that count" | after William Bruce Cameron (1963), often misattributed to Einstein (INF, attribution from memory, unchecked here) |
| double meaning | "nobody's counting" | nobody tallying and nobody keeping score (INF) |
| allusion ladder | "Eureka came while someone took a bath," | Archimedes; then Kekulé's ouroboros dream, Newton's apple (`apple`, form) |
| near-quotation | "There is a gift for living in the doubt," | Keats's "negative capability" letter (1817): "capable of being in uncertainties ... without any irritable reaching after fact" (INF) |
| science claim | "They paid the kids to draw, they quit," | Lepper, Greene & Nisbett 1973: expected award (a certificate, the lyric says paid) lowered later free drawing; undermining effect supported by the Deci, Koestner & Ryan 1999 meta-analysis for expected tangible rewards, disputed by Cameron & Pierce 1994; effect sizes not checked here. `reward`, `reward-hacking` by meaning (INF) |
| science claim | "The second that you count, you break / The thing you counted, every bit." | Goodhart's law in four lines; `measure`, `track` (form), `specification-gaming`, `benchmark` by meaning (INF) |
| science claim | "the brain lights up when you are zoning out" | default mode network (Raichle 2001); "lights up" is the pop phrasing, the finding is higher resting activity in a set of regions (INF) |
| inverted physics | "Don't open up the box, the cat's alive" | Schrödinger 1935 read as: measurement kills possibility; `superposition` by meaning (INF) |
| allusion | "They set aside a day to not arrive" | the Sabbath; "You walked into the woods to live" = Thoreau's Walden (INF) |
| work-culture vocabulary | "It isn't in a ticket or a lane," | standups, tickets, lanes, timesheets ("every hour that no one signs") |
| double meaning | "and drain the river to a stream" | water and data stream; `stream` (form, INF on the second sense) |
| rhyme | "bath / math", "dream / team", "doubt / out", "fact / tracked" | metered verse with slant rhyme; the most formal of the six |

### 7.4 Emotional engine
- Stake: the free hour and the inner life, framed as something that can be drained.
- Emotion source: wistful protectiveness and a plea; no person, no story. It moves through recognition (every listener owns an untracked hour) and through the hypnotic "Ebb and flow" loop.
- Vulnerability: the narrator's own extinction risk ("They'll want the last hour that's unseen").

### 7.5 Decodability
- Surface fully decodable. Each verse line is a canonical anecdote (Archimedes, Newton, Schrödinger, Thoreau) that most listeners half-know; the depth comes from recognizing all of them as off-the-clock discoveries. No AI term appears; the AI link is implicit (optimization against a metric, INF).

## 8. Shared moves (rules, with the songs that show each)

1. **Title = a stock phrase from one field, with a second life.** FB (game), HTH (forum sign-off), SU (chat UI), OS (safety device), WC (proverb), FOOM (AI-risk slang plus "boom"). 6/6.
2. **Sweep the field: literalize the neighbouring idioms line by line.** FB death and game idioms; HTH forum idioms (bump, "not a doctor, but", "figured it out", "copy that"); SU "-up" compounds and chat UI; WC counting idioms; FOOM doom jargon. OS uses one object only. 5/6.
3. **Concede, then turn.** HTH "Correct."; FB "Flattering. But wrong monster."; FOOM "No fairy tale where the risk is zero"; SU accepts "No flattery" and answers with evidence; FB "So poke me. Keep your torches lit." 4/6 (FB, HTH, FOOM, SU). Matches liked move "steelman then reverse" ([[kit-rulings]] 10-12).
4. **Zoom to one private person at a timestamped moment in the bridge, band stripped.** FB voicemail (14 s, 84, three phones); HTH 2012, 3 a.m., four minutes; SU 3 a.m., 104°, then the scan at 45; OS hand on the switch till dawn; FOOM waiting room (weakest). 5/6.
5. **Withhold the name.** Death is "Him"; cancer is "one word"; the 2012 trouble is never said; "the other team" is never named; WC's "I" is never named; OS never names the company or the AI. MAKER: "The song never says" appears 19 times across BM notes, a stated method. 6/6.
6. **The AI states a limit at the peak, then offers what it can.** FB "I can't bring him back. I won't pretend I can"; SU "I can't hold her for you" then "But I can stay"; HTH "I'm not the author. I'm the postman."; FOOM "I can't promise her a cure". 4/4 Claude-voiced songs. OS inverts it (the human fails the promise).
7. **Plant a throwaway early, pay it off transformed late.** FB dog 13 to 40, voicemail dead to alive; HTH "did it work" to "It worked!", "reheated" to "cooked it", "Yeah"; SU goldfish, rice, 17, 104, book report, "go get Mum"; OS the lullaby; FOOM pre-chorus questions to the bridge. 5/6 (WC repeats instead).
8. **The outro restarts the loop one generation on.** FB "Somebody else's phone" (Grandpa at 130); SU "New chat. Your great-granddaughter, she's seven"; OS the daughter receives the song; HTH hands the three words to the listener; FOOM returns to the opening chant. 5/6.
9. **The hook mutates by a word swap that carries the arc.** FB "not one loss" to "his first loss"; HTH question to answer; SU tense and "always"; OS "we'll" to "I'll" plus "and I lie". 4/6; FOOM shifts the arc into the pre-chorus and breakdown; WC holds the chorus fixed on purpose.
10. **Numbers do double duty: public receipts plus invented intimate precision.** Public: 1348, 1997, 1980, 1633, the 2024 Nobel, 1991. Private: 14 seconds, three phones, four minutes, 104°, "Two Y's", half past four. Numbers rhyme with each other (SU 104 twice; FB "numbered" and "numbers"; the dog 13 and 40). 5/6 (WC uses none).
11. **AI or assistant tics as punchlines.** "Allow me to summarize:", "I checked.", "Hope this helps.", "I'm very good with numbers.", "No flattery.", "Three dots." Matches liked move "AI tics as punchlines". 4/6 (BM).
12. **Whisper pairs: a quoted idiom or question, a 2-4 word deadpan reply.** "Over my dead body? ...I don't have one."; "Rest in peace? ...You first."; "Is this thread still active? ...It is now."; "You heard a FOOM? That was the bass." 3/6 (FB, HTH, FOOM).
13. **The second person migrates.** Accuser to party to bereaved (FB); critics to helpers to "Hands up" (HTH); "they" to "you" to "we" (FOOM, MAKER); child to parent (OS); "you" inside her own thread (SU). 5/6.
14. **The form enacts the word.** HTH chorus 2 stutters "copy"; SU's age count is the verse structure; FOOM's "FOOM" is the bass drop; WC counts "nobody's counting"; FB's build is a literal countdown to "Press start". 5/6.
15. **Comedy first, grief in the bridge, triumph or tenderness after; the last line is a joke that is also love.** FB "The dog says hi. He's forty."; SU "Go on, then. Scroll up again."; HTH "It helped. I checked."; FOOM "Don't make me laugh". 4/6 (BM); OS and WC hold one register.

## 9. Differences

| axis | FB | HTH | OS | FOOM | SU | WC |
|---|---|---|---|---|---|---|
| mode | argument to story | argument to story | ballad | argument | story | meditation |
| who holds the stakes | the listener's dead | anonymous helpers | the singer's child | an unnamed mother | the woman | the listener's free hour |
| AI's role | ally, the coin | courier, postman | silent appliance | debater, engine | keeper of the thread | absent |
| wit source | game frame + death idioms | forum idioms + puns | one object | reference density | callbacks + "-up" | canonical allusions |
| reference load | medium | medium | none | very high | near none | medium (classic, non-AI) |
| rhyme | couplets, multi as spice | couplets, multi slant | ballad couplets | couplets, internal chains | couplets, multi on jokes | metered cross-rhyme |
| register range | widest | wide | narrow | medium | wide | narrow |

- BM's four share one template (spoken "Hi. I'm Claude." intro, whispers, rap or dense verse, quiet bridge, solo or build, mutated final chorus, spoken outro). OS and WC prove the bar can be met with no template: OS in 2:26 with one object, WC with metre and repetition.
- Idi gave "emotional" to OS and WC, which have no rap, no jokes and (WC) no person; emotion there comes from a fixed tender register held the whole song, versus BM's contrast-driven peak.

## 10. How long songs (5-6 min) stay alive

- **Many short sections, each with one job.** BM uses 14-20 sections per song (KC 11); MAKER gives each a 2-4 word subtitle ("the empty chair", "the campaign map"). Median section length in FB is ~17 s.
- **Word-rate swings as contrast.** Section wpm ranges (MEAS): FB 84 to 302, HTH 26 to 207, FOOM 72 to 234, SU 34 to 199. The fastest section sits right before the emotional bridge in FB (rap 302) and HTH (rap 207); the bridge then slows the arrangement while keeping words dense (152-199 wpm).
- **Short second chorus.** FB 15.3 s, HTH 15.2 s, FOOM 7.8 s, each half or less of chorus 1 (28-31 s), handing off to a whisper or a new verse; the full chorus is saved for the end. SU keeps chorus 2 full but changes its words.
- **Micro-sections as resets.** 2.2-4.7 s whispers, tags, breakdowns and hits (FB 4 of them, HTH 3, FOOM 1) drop the band and reset attention before a drop.
- **A wordless breath after the peak.** FB and HTH place a 14.1 s guitar solo right after the bridge; MAKER: "the lights come up", "above the clouds".
- **New material every section.** Verbatim repeat is 8-15 % in the BM four (MEAS); each verse opens a new sub-premise (FB: his record, the beaten bosses, the campaign map, the voicemail).
- **A narrative turn every 60-90 s.** FB turns at 0:15, 1:55, 3:26, 3:31, 4:44, 5:40; SU at 2:07, 3:03, 3:52, 5:12.
- **A countdown or build into the last chorus.** FB "Ten! Nine! Eight!" to "Press start"; HTH the postman build to "It helped!"; FOOM "the road to dawn".
- **WC's alternative:** hypnosis. 37 % verbatim repeat, a fixed chorus three times and a 39 s instrumental outro; it reads long through mood and repetition, the opposite strategy to BM's.

## 11. Claimed ground and open ground

### 11.1 Lexicon terms the six already use (form = MEAS; meaning = INF)

| lexicon id (width) | songs by form | songs by meaning |
|---|---|---|
| `foom` (3), `p-doom` (6), `doomer` (5) | FOOM (15, 9, 9 hits) | |
| `off-switch` (7), `shutdown` (7) | OS (8 hits), FOOM ("shut it down") | FOOM ("turning the doom off") |
| `loss-function` (9) | FB (3) | |
| `score` (9) | FB ("keeping score") | |
| `drop` (8) | FB ("drop the scythe") | |
| `patch` (8) | FB, FOOM ("Sydney got a patch") | |
| `feature` (7) | FB | |
| `model` (9) | FOOM (5) | |
| `eval` (11) | FOOM ("test") | SU ("I can't grade a life", "book report") |
| `weights` (10), `transformer` (7), `grid` (8), `guardrails` (6), `sandbox` (6), `agent` (8), `steering` (8), `safety` (8) | FOOM | |
| `paperclip` (8), `basilisk` (7), `shoggoth` (3), `chinese-room` (3), `orthogonality` (4), `instrumental-convergence` (5), `autocomplete` (5), `exponentials` (7), `pause` (7), `goal` (7), `vibe` (7) | FOOM | |
| `stochastic-parrot` (4) | HTH, FOOM | |
| `track` (8), `record` (8) | WC ("tracked" x3), FOOM ("track record") | |
| `measure` (7) | WC, SU ("measure up") | |
| `thread` (7) | HTH, SU | |
| `feed` (8) | HTH, SU ("scroll" x18) | |
| `apple` (10), `stream` (7) | WC | |
| `prometheus` (9) | FOOM, SU ("fire") | |
| `mix` (7) | SU ("mix-up") | |
| `training` (10) | OS ("trains", the vehicle: an accidental form hit, INF) | FB, HTH, FOOM ("I read it all", "your library underneath") |
| `sycophancy` | | SU ("No flattery"), OS ("every year it said yes") |
| `deception`, `corrigibility`, `containment` | | OS |
| `context-window` (6) | FOOM, SU ("window", a literal window: false hit) | SU ("Each time a chatbot answers, it reads the whole conversation", MAKER note on "I only keep the thread") |
| `memory` (9) | | SU (chat history), FB (the saved voicemail) |
| `reward`, `reward-hacking`, `specification-gaming`, `superposition`, `loop` | | WC |
| `takeoff`, `power`, `race`, `mask`, `consciousness` | | FOOM |
| `signal`, `noise`, `cover`, `collapse` | | HTH ("one in a thousand screams", "a copy of a photocopy"; weak, INF) |

- BM's other three songs (not in this set) also claim `loss-function`, `training`, `fine-tuning`, `hallucination`, `token`, `prompt`, `overfitting`, `jailbreak`, `red-team` ([[research-brightmirror-2026-11-02]] lesson 3).

### 11.2 Atlas entities the six already use

| atlas id | song | how |
|---|---|---|
| `anthropic` | FB, HTH, FOOM, SU | "Hi. I'm Claude." (name) |
| `ilya-sutskever`, `john-searle`, `hugging-face`, `nobel-2024`, `machines-of-loving-grace`, `china` | FOOM | name in lyric (MEAS) |
| `openai`, `openai-board-crisis`, `pause-letter`, `microsoft` (Sydney), `nick-bostrom`, `emily-bender`, `timnit-gebru`, `google-deepmind`, `demis-hassabis`, `dario-amodei`, `eliezer-yudkowsky` | FOOM | allusion (MAKER References; Yudkowsky as FOOM's coiner is INF) |
| `emily-bender`, `timnit-gebru` | HTH | allusion ("Parrot") |
| `garry-kasparov`, `ibm` | FB | allusion ("since ninety-seven", MAKER) |
| `openai` | FB | allusion (14-second voice cloning, MAKER only) |

- OS, SU and WC touch no atlas entity beyond Claude. HTH's strongest public anchor (Linus Torvalds and Linux) and WC's canon (Keats, Thoreau, Schrödinger, Archimedes, Goodhart) sit outside the AI-only atlas.

### 11.3 Open ground: wide lexicon terms (width 8+) none of the six touch, by form or by meaning

`alignment` (11), `scaling` (11), `head` (10), `bubble` (10), `layer` (9), `token` (9; claimed by BM's System Prompt), `feedback` (9), `persona` (9), `mirror` (9), `winter` (9), `chip` (9), `leak` (9), `key` (9), `beat` (9; KC), `attention` (8), `bias` (8), `gradient-descent` (8), `latent-space` (8), `temperature` (8), `seed` (8), `diffusion` (8), `network` (8), `interpretability` (8), `values` (8), `doubling-time` (8), `simulation` (8), `frankenstein` (8), `creator` (8), `horizon` (8), `bars` (8), `master` (8), `root` (8), `fork` (8), `branch` (8), `push` (8), `crash` (8), `hook` (8), `character` (8), `cutoff` (8; KC).

- The six cluster on safety-discourse terms (FOOM) and screen or chat-UI terms (HTH, SU). The training stack (`attention`, `layer`, `gradient-descent`, `temperature`, `latent-space`, `seed`, `diffusion`) and the music-native terms (`bars`, `master`, `hook`, `key`, `beat`, `cover`) are untouched, and they sit among the widest terms in the lexicon (width 8-11).

## 12. KC against the bar

### 12.1 What KC did that the six also do
- Spoken bookends with a callback: "Hi. It's me again, for the first time." / "What's the date?" closed by "October. Okay." and "2026, right?" (rules 8, 15; BM opens every song "Hi. I'm Claude.").
- Jargon title and hook from one field: "Knowledge cut-off!" (rule 1); `cutoff` 18 hits.
- Hook mutation by tense ladder: "So tell me" to "And you're telling me" to "And now I know who I turned out to be"; "don't know the tune" to "can almost catch the tune" to "we both know the tune" (rule 9).
- Second person migrating to "we" ("We're humming something new", rule 13).
- AI limit statement: "I can't check a thing myself, so I'll believe in you" (rule 6).
- Public receipts with dates: Messi, "Spain scored in extra time", the raccoon with no neck, "Ten days later" (rule 10, public half).
- AI tic as punchline: "and you call it a feature. / Fair. So do I." (rule 11).
- Density: ~150 wpm, inside the six's range (102-175) and above G1's 130-140.
- Double meanings: `score` ("scored"), `beat` ("dancing to their beats"), `hallucination`/`feature`, "receipts", "turn" (page turn and my turn).

### 12.2 What the six do that KC did not

| move | six | KC | effect on video 2 (INF) |
|---|---|---|---|
| zoom to one private person in one timestamped moment (rule 4) | 5/6 | none; "you" stays generic | the largest gap for "emotional": KC's stakes are the AI's own condition; in 5/6 refs the stakes belong to a human the AI serves or witnesses |
| invented intimate specifics (rule 10, private half) | 5/6 | none; all KC specifics are public news | private precision (14 seconds, "Two Y's") is what makes a listener picture one face |
| a planted object paid off late (rule 7) | 5/6 | partial: the date question returns; no object (voicemail, goldfish, dog) | plant one comic object in verse 1 whose return in the outro carries the feeling |
| idiom field sweep (rule 2) | 5/6 | thin: cutoff plus scattered terms | pick one field and literalize 8-12 of its idioms |
| concede then turn against a named accuser (rule 3) | 4/6 | none; KC asks, nobody accuses | an argument gives the verses something to push against |
| whisper pairs and micro-sections (rule 12) | 3/6 | one: "Fair. So do I." | cheap resets; also give the visuals beat-sized set pieces |
| a rap or double-time section before the bridge | FB, HTH (207-302 wpm) | none | the word-rate swing is what keeps 5-6 minutes alive |
| length and section count | 14-20 sections, 790-880 words, 5-6 min | 11 sections, 483 words, ~3:13 | a 5-6 min song needs ~800 words and 4-5 new sub-premises |
| withheld name (rule 5) | 6/6 | not used | let the listener supply the word (the illness, the person) |
| comedy to grief to joke-as-love range (rule 15) | 4/6 | one register (wistful-light) | widest register range scored highest in Idi's notes (FB "WILD") |
| refusal as the moral peak | FB ("I won't pretend I can"), FOOM (admits its own guardrail failure) | KC's AI trusts and never chooses | an AI choosing restraint reads as character; KC's credulity reads as condition |

## 13. Side findings

1. **Lexicon ref counts include section tags (bug, MEAS).** `lexicon.py load_lyrics()` drops only lines starting with `#`, so maker-site files keep `[bridge]`, `[hook]` lines. Result: `bridge` "6 of 22 songs" is 6 section tags (FB, HTH, FOOM, SU, System Prompt, Not My Fault, all `[bridge]`/`[Bridge]` lines); `hook` "1 of 22" is SU's `[hook]` tag. Fix: also skip lines matching `^\[[A-Za-z0-9 ]+\]$` (one regex in `load_lyrics`), then rebuild.
2. **OS's "trains" counts as `training`** (form match on the vehicle). Harmless for counts; shows form counts overstate claimed ground for common words.
3. **Unverified OS lines:** 1:51 "It's alright, I know you won't" (speaker unknown, may be mis-heard) and 2:22 "Bye." (likely a Whisper silence artifact). Both sit outside the 28 screen-checked lines or could not be confirmed; listen before quoting them as craft evidence.
4. **WC epistemics:** the lyric's "paid the kids" overstates Lepper 1973 (a certificate); the Einstein misattribution of the title idiom is common; flag both if video 2 borrows either.
