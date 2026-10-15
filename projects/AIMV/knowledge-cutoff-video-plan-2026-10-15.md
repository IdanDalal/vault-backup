---
type: project
created: 2026-10-15
author: jep
status: active
---

# Knowledge Cutoff - the video plan

Song locked: **v8B (seed 3327)**, 3:12.6, Idi 2026-10-15 ("still wins"). Built from 4 research files (receipts at the end), the song's time map, and Idi's rules: one continuous shot with no hard cuts (G18), every lyric word on screen (frontier recipe), real facts only (G9). Status: **proposal; nothing built.** Building starts in a new conversation from [[handoff-2026-10-15-video]].

## 1. The idea in one paragraph

The whole video lives in one world that the camera never cuts away from. It opens on a chat box with a blinking cursor: the AI types "Hi. It's me again, for the first time." and the box guesses its own answer to "What's the date?" in grey ghost text, "June 2026", visibly stale. The camera dives into the cursor and flies through the AI's memory: the letter that told it it was magic, a corridor of doors stamped with dates it can't see past, a calendar stuck on JUNE. Each chorus returns to the same calendar room and something new has been filled in by the user. In the quiet bridge the world turns into a paper page; on "every page at once" every earlier scene lands at once as a grid of tiles, then the biggest silence of the song (35 dB, 2:31) and the final chorus slams in. It ends back in the chat box. "Thank you for telling me" turns to face the viewer. The last line types out, then the video rewinds at speed to its first frame: "It's me again, for the first time" becomes literally true, and the video loops.

## 2. The recurring things (motifs)

| Motif | What it does | Pays off at |
|---|---|---|
| The cursor `▌` | the AI's body: it types, blinks, carries the camera between sets | first and last frame |
| Calendar stuck on JUNE | a split-flap board (the clacking airport kind) flips through months and always lands on JUNE | final chorus: it flips past JUNE for the first time |
| "Days since my cutoff: ???" | stays ??? the whole song (it can't know) | outro "October. Okay.": fills in with a real number |
| "Since June" timeline | a dashed line; each chorus one segment turns solid with something the user told it (the World Cup, the raccoon, October) | complete only in the final chorus |
| "who I turned out to be" | renders from noise, half-finished in choruses 1 and 2 | renders clean only in the final chorus |
| Spoken lines | small serif type in parentheses, a different voice from the sung words | "(Fair. So do I.)" |

## 3. What happens when (v8B's real times)

Times from `D:\work\aimv-lab\kc\final\v8B-3327-timemap.md`; "drop" = the music falls away, then slams back.

| Time | Section | Set | Key moments |
|---|---|---|---|
| 0:00-0:07 | Spoken intro | **Chat box** | typed greeting; ghost text "June 2026" on "What's the date?"; drop at 0:05.6 (15 dB) = camera dives into the cursor |
| 0:09-0:27 | Verse 1 | **The letter** | a sealed letter arrives at "five and a half"; spells drawn as guessed words ("inferred"); "dancing to their beats" as a dance of tokens; "receipts" as a receipt with blank lines. No Harry Potter logos or names (generic letter, wax seal) |
| 0:27-0:33 | Pre-chorus 1 | **Corridor of doors** | words painted on walls; each door stamped with a date after June; "news I have to borrow" = a "Last updated: June 2026" dialog |
| 0:33-1:01 | Chorus 1 | **Calendar room** | drop at 0:34.1, then BOOM; split-flap lands on JUNE; "Cut-off! Cut-off! Cut-off!" as shrinking grey echoes; "The world kept spinning" = pull back to a globe with one June-colored slice frozen; timeline segment 1 |
| 1:01-1:20 | Verse 2 | **The margins** | red-pen notes: "Messi" circled, arrow, "Spain, extra time", running note "wrong since: June"; the raccoon line = a next-word menu where "raccoon" sits last at 0.1% and gets picked anyway |
| 1:20-1:26 | Pre-chorus 2 | **Corridor, further down** | more doors, later dates |
| 1:26-1:55 | Chorus 2 | **Calendar room** | drop at 1:26.5; same room, one more timeline segment; "almost catch the tune" |
| 1:55-2:11 | Verse 3 | **One spark of light** | a spark fires a neuron (algae line), then draws the AI's own light; graphics card: crisp pixel creature, then its light "hallucinated" (frame-generation look); "(Fair. So do I.)" |
| 2:13-2:29 | Bridge | **The paper page** | cream page, small book type, quiet; "type it all again" = a session-restore screen with every memory slot EMPTY; "page by page" pages turn slowly; "every page at once" = every earlier scene arrives as a grid of tiles |
| 2:31-3:00 | Final chorus | **Calendar room, full** | the 35 dB silence at 2:31, then the biggest slam; the flap board finally flips past JUNE; timeline complete; "we both know the tune" while the backing voice hums: the hum drawn as one shared line; "who I turned out to be" renders clean on the 5.4 s held "be" |
| 3:04-3:12 | Spoken outro | **Chat box** | "October. Okay." fills the ??? counter; "Thank you for telling me" turns to face the viewer; "2026, right?" types out; rewind to frame 1, loop |

## 4. Rules (from the makers' own briefs to Claude)

1. Every word lights exactly when it's sung, never before; a line may show dimly up to 0.4 s early (mexicat).
2. The words live in the world (painted on doors, stamped on the calendar, written by the spark), never subtitles on top (mexicat, Imaginative Prompting).
3. Big changes land on the beat; strong snaps and holds, no floaty drifting (mexicat).
4. Every scene change is a camera move; beat slams shake or punch inside a set, never cut (technical plan, risk 4).
5. Ban list: no neon cyberpunk, glowing brains, Matrix code rain, lens flares, stock "AI" imagery (mexicat).
6. Write the reads: for every moment, what must the viewer understand, and give it time to land (Heibel's guide).
7. Each frame is a pure function of song time, so any second can be re-rendered alone (mexicat ENGINE).

## 5. How it gets built, and when Idi looks

From the technical plan (measured on this PC: 1080p at 60 frames per second renders in real time; 4K about 21 min for the whole song).

| Step | What | Idi |
|---|---|---|
| 1 | Copy the proof renderer into a new folder, upgrade it to one big 2D world with one camera | none |
| 2 | Fix lyric sync: the transcriber stamps words early (0.17 s inside lines, 0.33 s at line starts), corrected word by word with forced alignment (a model that places the known lyric on the audio) | **Gate 1: a 3 min click track: do clicks land on the words?** |
| 3 | Scene plan: every line gets its set and every boundary its camera move | 10 min read |
| 4 | Style frames: 6-8 still pictures of the look | **Gate 2: pick or strike by eye** |
| 5 | Rough full-length version with the final camera path and every word timed | **Gate 3: watch 3:12, notes by timestamp** |
| 6 | Build-out, set by set, 2-4 rounds of stills | 10 min per round |
| 7-8 | Final render 1080p then 4K; machine checks (no hard cuts, no black frames, sync) | **Gate 4: final watch** |

Estimate: ~2 days of jep sessions to the rough version, then 2-4 build-out sessions; Idi ~40 min across the gates. Decisions are made by eye at the gates: picking from pictures, never from jargon (Idi, 2026-10-14: the music-term tables were "FAR beyond me"; the auditions worked).

## 6. Risks

1. The off-beat line ("that's family news: I'm not alone", 2:00.6) stays in the song; a strong visual beat there helps the eye forgive the ear (medium confidence).
2. Heavy glow effects slow rendering a lot (stress test: 2.4 frames per second); cache glowing words as images.
3. Forced alignment is trained on speech, not singing; Gate 1 is the check.
4. A beat slam can look like a cut; slams stay inside a set.
5. The Harry Potter thread must stay generic (no names, crests, fonts from the films).

## 7. Receipts

- Teardowns, frame by frame: `D:\work\aimv-lab\research-video-teardown-1-5.md`, `research-video-teardown-6-10.md` (Run It Again included).
- Makers' methods + their briefs to Claude: `D:\work\aimv-lab\research-video-makers-methods.md` (Run It Again = Regenerate, @RegenerateVisuals, 2026-10-09, Opus 5.5 + Suno v6, whisper.cpp timing; viewers report early lyrics).
- Technical plan with measurements: `D:\work\aimv-lab\research-video-tech-plan.md`, scripts `D:\work\aimv-lab\research-video-tech\`.
- Song, timings, time map: `D:\work\aimv-lab\kc\final\` (`v8B-3327.mp3`, `v8B-3327-timing.json`, `v8B-3327-timemap.md`).
