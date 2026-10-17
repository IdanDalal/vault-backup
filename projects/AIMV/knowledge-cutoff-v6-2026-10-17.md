---
type: project
created: 2026-10-17
author: jep
status: active
---

# Knowledge Cutoff v6 and the rules audit (2026-10-17)

Verdict: **v6 is rendered with your ruling A and notes 1-2 (483/483 words on time, 0 cut flags, seamless loop). The audit finds the gap to the five references in the visual approach: they build frames from type, interface and line art with 4-7 objects each; ours draws filled pictures with 12. Five early rules set that course, and one ruling decides v7 (section 6).** Follows [[knowledge-cutoff-v5-2026-10-16]].

Files: `D:\work\AIMVs\ours\video\gate3\knowledge-cutoff-v6.mp4` (3:14.1, the song plus 1.5 s of silence). The gap at a glance, six frames per video, references above ours: `D:\work\aimv-lab\kc-video\critique\v6\gap-sheet.jpg`.

## 1. v6: what changed

| time | change |
|---|---|
| 0:09-0:27 | The letter is handwritten by an invisible hand (Caveat), letter by letter as sung, in wet gold ink that dries dark. No highlight boxes, no grey preview (your note 1) |
| 1:02-1:20, 2:13-2:29 | Newsprint and the book: each letter stamps down like type, slightly out of line, wet gold then ink; "you" in blue ink (note 1) |
| every hook | All three CUT-OFF!s are cut by the red blade and split in two; the halves part over the next one landing (note 2) |
| 3:12.4-3:14.1 | Your ruling A: 1.5 s of silence. The song's last frame holds, the camera pulls back to the whole conversation, the conversation files into the sidebar as one more greyed "Hi. It's me again, f…" session, the list shifts down a row, "???" and 00 00 00 come back, and the loop lands on frame 1 |

Verified: every word lit on time in its own colour, 483/483 (`check_sync.js`); negative control (the same colour test 0.3 s before each word, where it should fail) 7%, the same 8 words as v5; 0 cut flags (ffmpeg scene scores, threshold 5) on the full render and on 6 window clips; 0 black frames; loop 52.1 dB (first and last frame the same picture; v5 47.7); the tail is digital silence (-91 dB); the copy in `gate3` is byte-identical (md5 `7ed72195…`). Not verified: v6 watched at speed by a person.

## 2. Why it is still far behind, measured

Agent A2 measured all five references and v5 on the same ten dimensions (`critique\v6\refs-approach.md`, 688 frames coded by eye, text recognition on 1,373 frames). Agent S2 read P(Doom)'s source and the makers' own words (`critique\v6\refs-build.md`).

| measure | the 5 references | v5/v6 |
|---|---|---|
| what fills the frame | type, interface or document chrome, line art, 3D, empty space: 86-100% | filled illustrations 25%, video grabs 6%, no line art |
| how facts appear | as the interface's own text (forms, logs, counters, dialogs) | as drawn props with captions beside them |
| objects per frame (median) | 4 to 7.5 | 12, the most crowded, and it rarely empties |
| type sizes, largest to smallest | 9.7x to 16.6x | 7.9x, the narrowest |
| lyric as a caption over a picture | 0-35% of frames | about 50% |
| set-ups across the video | about 33-75 | 8 rooms, visited 17 times |
| near-still stretches of 2 s or more (F6) | 3-7% of the runtime | 23% (43.5 s) |
| saturated colour | one hue takes nearly all (R5: two) | four hue families; gold on both letters and props |
| drawn people and animals | none, or one low-detail convention (outline, text-filled silhouette, cursor) | filled figures, a raccoon, flags, a cat, in several styles |
| code per second of video | P(Doom) 149 lines, Ignore Previous Instructions 129 | 11 |
| generated images in frames | none (P(Doom) read in its code; the others stated "every frame is code") | none |

How the references got there (S2, from their code and their makers' words): P(Doom) is 23,286 lines of TypeScript and three.js with a style bible (one page of visual rules every scene follows), one code module per scene, hatched line art (drawings shaded with parallel lines, like an engraving), a bloom (a glow that bleeds around bright colour) that only the orange reaches, and agents told to look at contact sheets. LGTM and The Simulation's Ending started from that engine. LGTM's maker: "hundreds of prompts across many sessions [...] the smaller the prompt, the better." v4 and v5, by contrast, were each built in one pass from 200-250 critic findings, and each pass added props, labels and gags.

## 3. The flaw hunt (your note 9)

Six agents reviewed v5 with no knowledge of our intentions, your 8 notes as the severity bar: 403 flaws (F1 66, F2 64, F3 72, F4 86, F5 54 by stretch; F6 61 across the whole video), files `critique\v6\flaws-F1..F6.md`. Spot-checked by me: "You're" over the DAYS SINCE JUNE counter at 0:39 (`critique\v5\lib\v5\frames\f00079.jpg`). They converge on nine causes:

| # | cause | seen by | examples | rule or default behind it |
|---|---|---|---|---|
| 1 | Text lands on text, props land on the lyric | all six | "You're" over DAYS SINCE JUNE (0:37, 1:29, 2:33); KNOWLEDGE on the E tile; LAST CHECKED stamp on the counts; a clock on "Everyone" (1:20) | props placed by hand with no grid; "no prop over the lyric" enforced by nothing; the sync check sees sung words only |
| 2 | Scenes keep adding and nothing clears | F1, F2, F4, F5 | 15 props on the letter by 0:25; "E", "KNO", "DAY" behind the portrait; dimmed rooms under every hook | one world of 8 rooms that stay on screen; the camera rests while lines are sung |
| 3 | Props cut by the frame edge | F1, F3, your 0:36 and 2:00 | clock, candle, Nobel plaque, newspapers | no safe-area check |
| 4 | Many clocks: dates disagree, "June" up to 7 times on one screen | F2, F4, F5, your 0:36 | pill Jun 30, board JULY, globe SEP 10, counter 072, timeline Sep 22, together | every prop carries its own copy of the fact |
| 5 | Filled drawings of people, animals and objects | your 0:29, 1:11, 1:16, 2:00; F4 | hall figures, raccoon, flags, neuron, algae, cat | every prop drawn from canvas shapes, a default nobody chose |
| 6 | Transitions turn text to garbage | F1, F2, F3, F5 | stacked-copy blur at 0:07, 0:09, 0:27, 0:33; beams and sparkle rings drawn through lyrics | 6-copy motion blur; every change a camera glide; effect layers on every frame |
| 7 | Text sized for a paused still | F3, F5, your 0:33 and 1:40 | 30 caption lines in the gallery; a 17-row recap; long headlines | facts as props plus a caption that restates the lyric |
| 8 | Repeat visits replay the first visit | F3, F6 | the calendar and the gallery fill 45% of the runtime; the globe ring plays 3 times, the month flaps 5 times; each repeat ships the same collisions again (fixing one timestamp leaves 2-5 copies) | one set per song section; one fixed layout per room |
| 9 | Spoilers: the payoffs are shown before their moment | F6, your 0:33 | the AI's name and birthday on screen 7 times from 0:11, so the 3:01 reveal is old news; "It's October." already answered by the OCT door (0:27), the OCT 15 axis (0:34) and the OCT flap (0:55) | every prop carries its own copy of the fact |

Worst single moment found: 3:03-3:04, the pull-out through the cursor fills the frame with a flat navy and yellow block for a second, and it reads as a broken render (F5).

## 4. The premature rules (your question)

Method: agent A1 listed every rule that shaped the video, 116 of them plus 15 unwritten defaults, each with its source and date (`critique\v6\rules-ledger.md`); 55 were set before any moving picture existed. I tested each against what the five references do (section 2) and against the flaw causes (section 3). Five of yours set the course:

| # | rule | made, when | what the references do | recommendation | what it changes |
|---|---|---|---|---|---|
| 1 | G18 one-shot, no hard cuts, enforced by my cut detector (0 flags) | you, 10-13, after the 40 s proof and before the full video; the detector bar is mine | 4 of 5 cut, 5.6 to 31.7 times a minute; LGTM keeps one world but stages about 46 documents with 0.2 s whips | keep one camera, give every line its own cleared set-up, judge motion by eye | the detector stops vetoing fast whips; rooms stop piling up; the second chorus gets new pictures |
| 2 | Gate 2 "keep all 9": palette and the six rooms locked | you, 10-15, from 9 stills, before any motion | 33-75 set-ups each | unlock the rooms | each line is staged fresh; the hall, margins, spark room and gallery get rebuilt |
| 3 | "Facts as visuals: Jimothy, DLSS5, flags, Dario" | your v3 note 6, 10-15; I built it as filled drawings | facts live as the interface's own text; objects are line art or icons | keep the facts, change the medium | the World Cup, Jimothy, DLSS 5 and the Nobel appear as the artefacts they live in (a broadcast score graphic, a meme post, a spec sheet, a prize page); any object as hatched line art |
| 4 | "Level up MASSIVELY: more effects, particles, spectacle" | your v3 notes 1 and 5, 10-15 | spectacle from staging, one glowing colour and a film finish; in P(Doom) only orange may glow | keep the ambition, move it from layers to craft | dust motes, per-word spark bursts, beams and sparkle rings go; bloom on the gold only, paper texture and hatching come in |
| 5 | Every view count shown, as "a flex" | your v4 note 8 | (you corrected it on 10-17) | as you said | one card: LGTM past a million |

Mine, which I will change unless you object: the 8-room world map (you never ruled on it), one text size per room, every line entering at the same spot the same way, props placed by hand with no grid, the 6-copy motion blur, building a version in one pass from 200-250 critic findings, and checks that see only sung words.

## 5. Outside help (your note 3)

1. **Gemini 4 Argon** (generally available 2026-10-13, S1, `critique\v6\staff-gemini.md`): reads text, images and video with sound; writes text only, so it cannot draw props. Video at 1 frame per second by default, one frame per 2.7 beats of this song, so it can judge scenes and legibility and cannot judge sync. Outside rankings: #1 on the Vals Index, #8 on Artificial Analysis; its video scores are Google's own. Access: the Gemini app on your AI Pro plan, and the Antigravity CLI `agy` (installed, v1.1.27) after one sign-in by you; whether `agy` needs the pricier Ultra plan is unclear until then. Driving the Gemini website from here breaks Google's terms and risks your account.
2. **Google's images** come from its Nano Banana models in the Gemini app and Flow, with no transparent backgrounds.
3. **The 4090:** Z-Image ran here for DECADEnts in your ComfyUI; mine holds only the music models.
4. **What the references used:** no generated images in any frame. Only Ignore Previous Instructions used an image tool, for character design references ("rather minimal"); LGTM's maker on later videos: "every frame built in code (no image generators)".

Recommendation: no generated images in the frames; the references' leap came from code craft. Gemini later as an outside critic of the v7 proof scene, if you want one (your one sign-in, about 7 minutes).

## 6. v7: options

- **A. Restage in our engine (recommended).** (1) A one-page style bible: palette with one glowing colour, type roles, line-art drawing rules, a reserved lyric zone, one idea and one date per frame. (2) Three automated checks beside the sync check: anything overlapping the lyric, anything crossing the frame edge, text on screen too briefly to read. (3) Rebuild scene by scene, each line staged as the artefact it names (the form, chart, screen or document the line talks about), 4-7 objects a frame. (4) A finish pass: glow on the gold only, paper texture, hatching. First domino: the hall (0:27-0:34, your 0:29 and 0:33 notes) rebuilt as a proof and shown beside v6 and the references. Cost: about one session for the proof; the whole video takes several.
- **B. Rebuild on P(Doom)'s engine** (MIT licence: free to reuse with credit; the base of 3 of the 5 references). Highest ceiling: GPU shaders, hatching, real bloom. Risks: this PC's GPU render path gave black frames twice, and every scene gets rewritten in TypeScript. First domino: a 5 s WebGL probe (WebGL: the browser's GPU drawing system).
- **C. Patch v6** flaw by flaw. Fastest; the eight causes in section 3 stay.

I recommend A, with B's 5 s probe run alongside: it is cheap and decides whether the finish can use GPU shaders.

**Say the word for A with rules 1-5 as recommended, or overrule any rule by its number.**
