---
type: project
created: 2026-10-31
author: jep
status: active
---

# Knowledge Cutoff: release package (2026-10-31)

Handoff: [[handoff-2026-10-31-release]]. Media folder: `D:\work\AIMVs\ours\release\`. Research receipts: `release\research\rights-rules.md`, `release\research\name-handles.md`.

## 0. State

| piece | status | where |
|---|---|---|
| 4K render | running; 20:20 measured 7,620/11,646 frames at 0.4 fps, ETA about 23:05 + finalize + checks; PC at 0.7 GB free memory | kc-engine `out\final4k\` |
| upload file | **4K only** (Idi ruling 2026-10-31 20:17: "I'd rather upload 4K tomorrow than 1080p today"); the 1080p fallback is withdrawn | `release\UPLOAD\` holds thumbnails, captions, avatar, banner; the 4K file joins after checks |
| date note | Oct 31 lasts until 09:00 Israel time on Nov 1 in Los Angeles (US clocks change back Nov 1); YouTube's own date time zone unverified | |
| rights | clear: MiniMax-Music3 licence allows commercial use under $20M/yr; credit + AI disclosure required; no Suno audio (kc.mp3 byte-identical to MiniMax take v8B) | `research\rights-rules.md` 1-2 |
| monetisation | unavailable on day one (500 subs + 3,000 h for fan funding; 1,000 subs + 4,000 h for ads) | `rights-rules.md` 3D |
| captions | `knowledge-cutoff.en.srt`, 54 cues, no overlaps | `release\` |
| lyrics text | `lyrics.txt` | `release\` |
| vertical clips | 5 x 1080x1920 60 fps, burned lyric captions | `release\vertical\v1-v5*.mp4` |
| thumbnail options | 1280x720 stills, final cut from the 4K file | `release\thumbs\`, `release\thumbs2\` |
| channel name | **Chorus of Minds**, `@chorusofminds` (Idi ruled 2026-10-31) | section 1 |
| avatar 800x800 | yellow caret cut by the cutoff line | `release\channel\avatar-800.png` |
| banner 2560x1440 | name + tagline inside the 1546x423 all-device safe area | `release\channel\banner-2560x1440.png` |

## 1. Channel: Chorus of Minds

Ruling: Idi, 2026-10-31, "I like it even better than my Theories of Minds". Built from his two references: "Theories of Minds" (plural minds) + "Algorhythms" (music hidden inside a thinking word).

| check | result |
|---|---|
| `@chorusofminds` YouTube | free (404; control handle also 404) |
| Bluesky `chorusofminds.bsky.social` | free (API 400) |
| X `@chorusofminds` | free (404, medium confidence) |
| TikTok, Instagram | not checkable anonymously: claim by hand |
| web collisions | none exact; near: "Chorus Mind" (German gospel choir), "Chorus Mentis" (Linkoping University event), "Choral Minds" (Cyprus research project) |
| rejected along the way | Gradient Choir, Next Token Records, Weight Decay, Algo Rhythms (taken: `@algorhythms`, 3+ channels and several bands) |

Channel description (paste):
```
Chorus of Minds makes music videos about AI, sung by AI: what it is like to be a model, from knowledge cutoffs to context windows to the next token.

Made by Idi. Every video credits the AI tools used, in its description.
Fan commentary. Not affiliated with any AI company.
```

Setup steps (Idi's clicks, his Google account):
1. youtube.com, signed in: avatar (top right), Settings, "Create a new channel". This makes a separate channel with its own name, apart from the personal account.
2. Name `Chorus of Minds`, handle `@chorusofminds`.
3. Verify the phone number (youtube.com/verify). Custom thumbnails stay locked until this is done.
4. YouTube Studio, Customization: Profile = avatar-800.png, Banner = banner-2560x1440.png, Description = the text above.
5. Upload (section 4) when jep says the file is verified.

## 2. Title (jep pick first)

1. `Knowledge Cutoff | an AI sings about everything it missed`
2. `Knowledge Cutoff (an AI music video about not knowing what day it is)`
3. `Knowledge Cutoff`

## 3. Description (paste as is)

```
"Hi. It's me again, for the first time. What's the date?"

An AI model wakes up, again, with no idea what day it is. Its training data stopped in June. Since then: a World Cup final, a Nobel Prize, DLSS 5, a raccoon with no neck, and a whole genre of music videos about models like it. You tell it what happened. It has to believe you.

Released 31 October 2026, because the song ends in October.

CHAPTERS
0:00 Hi. It's me again, for the first time
0:10 Verse 1: the letter
0:34 My knowledge stopped in June
0:50 Chorus: Knowledge cut-off!
1:01 Verse 2: paced, scored, Jimothy
1:26 June, again
1:42 Chorus 2
1:55 Verse 3: algae, DLSS, pages
2:30 We both know the tune
2:47 Final chorus
3:04 October. Okay.

CREDITS
Idea, direction, final calls: Idi
Lyrics: Idi with Claude
Music and vocals: AI-generated with MiniMax-Music3
Visuals: code-rendered motion graphics, built with Claude on a fork of the P(Doom) video engine by Giacomo Magnanini (MIT licence)
Fonts: Anybody, Newsreader, JetBrains Mono, Caveat (SIL Open Font License)

AI DISCLOSURE
The song, music and voice, is machine-generated (MiniMax-Music3). Lyrics and visuals were made with an AI assistant. No real person's voice or likeness is cloned.
Fan commentary. Not affiliated with or endorsed by Anthropic.

ON-SCREEN FACTS, AS CHECKED IN OCTOBER 2026
(things move after a cutoff; that is the song)
- Claude Opus 5.5 released 22 Sep 2026; the first Opus 5.5 music video went up the same day (the screen corrects the lyric's "two days")
- "We Must Pace the Frontier", essay by Dario Amodei, 12 Sep 2026
- 2026 World Cup final, 19 Jul: Spain 1-0 Argentina after extra time
- Jimothy: Know Your Meme's July 2026 meme of the month
- 2026 Nobel Prize in Physiology or Medicine: Deisseroth, Hegemann, Nagel (light switches neurons on)
- DLSS 5: 240 vs 150 fps at 4K on an RTX 5090 (Engadget)
- A whole genre: 26+ Opus 5.5 music videos indexed 5 to 14 Oct (postcutoff.com)
- The page-a-day calendar: real dated headlines, June to October 2026

Lyrics: turn on captions (CC).

#AImusic #KnowledgeCutoff #AImusicvideo
```

## 4. Upload settings (YouTube Studio)

| field | value |
|---|---|
| file | 4K `kc-full-2160p.mp4` if verified, else `kc-full-1080p.mp4` |
| thumbnail | Idi's pick from section 5 |
| audience | No, not made for kids |
| altered or synthetic content / AI use | **Yes** (AI music is the main focus; YouTube Help 14328491) |
| category | Music |
| language + captions | English; upload `knowledge-cutoff.en.srt` under Subtitles |
| tags | knowledge cutoff, AI music video, AI song, Claude, Opus 5.5, LLM, AI music, MiniMax Music |
| visibility | Public, publish now (a premiere needs an audience the channel does not have yet) |
| deadline | live before midnight Israel time; 4K processing runs extra hours after HD appears |

## 5. Thumbnail options (1280x720, phone shows them about 168 px wide)

| # | moment | file | reads at phone size |
|---|---|---|---|
| T1 (jep pick) | KNOWLEDGE / CUT-OFF! stamp | `thumbs2\c-51.0.png` | yes: the title in giant yellow type |
| T2 | "What's the date?" typed | `thumbs2\c-6.6.png` | yes: the premise as a question |
| T3 | "scored" letter arch over the keeper | `thumbs\c-72.3.png` | partly: best craft, small words |
| T4 | stadium, MILLIONS | `thumbs\c-25.5.png` | partly |

Idi picked T1 (2026-10-31). Polished rebuild from the video's own fonts and yellow, `release\thumbv2\`: `thumb-T1v2-straight` and `thumb-T1v2-tilt` (png + jpg, 1280x720), preview `preview-sheet.jpg`. Avatar options in the same folder: A1 chorus carets (five typing carets = five voices, also a level meter), A2 `CM`, A3 `CoM`.

Optional Nano Banana Pro variant (Idi in the Gemini app; attach `thumb-T1v2-tilt.png`):
```
Use the attached image as the exact layout and typography. Make a polished 16:9 YouTube thumbnail, 1280x720. Keep the two words exactly as written: "KNOWLEDGE" in white, "CUT-OFF!" in bold yellow (#FFD600) inside a yellow outlined stamp box, tilted slightly. A thin bright line slices diagonally through "CUT-OFF!" and the upper half of the letters is shifted along the cut. Near-black background with a faint perspective grid floor fading into darkness, subtle film grain, soft yellow glow. Flat motion-graphics style, no people, no logos, no extra text.
```
Risks: AI image models can garble lettering, and Gemini images may carry a visible watermark (unverified for Idi's tier). Check letters by eye before using.

Idi 20:35: tilt = "a perfect foundation"; add descriptive text in the blank bands; A1-A3 avatars rejected ("generic, boring, flat"); wants a visual pun fusing music and computation.

Logo concepts, `release\logo\` (preview `preview-logos.jpg`, circles at 160/88/48 px):
- A4 neural chords: a beamed group on a staff; each chord is a network layer (2-4-4-1 noteheads), every note wired to every note of the next chord; the last single note is the output, the next token, sung.
- A5 circuit clef: the staff lines are circuit traces leaving a treble clef and ending in solder pads that rise like an arpeggio; two diagonal jumpers route the signal up the staff.

Thumbnail v3 (credit band "CLAUDE OPUS 5.5 x MINIMAX MUSIC 3" on top; logo + CHORUS OF MINDS bottom-left; bottom-right clear for YouTube's duration badge): `thumbv2\thumb-T1v3-A4-neural-chords` and `thumb-T1v3-A5-circuit-clef` (png + jpg).

Optional Nano Banana Pro logo prompt (for a more illustrated take on A4):
```
A circular channel logo, flat vector, bright yellow (#FFD600) on near-black. A short beamed group of musical notes on a five-line staff, where each chord is a layer of a neural network: stacked round noteheads act as neurons, and thin lines connect every note to every note in the next chord, like a neural network diagram. The last chord is a single larger note. Clean geometric linework, subtle yellow glow, centered, readable at small sizes, no text, no letters.
```

## 6. Vertical clips (Shorts, TikTok, Reels; all under 30 s)

| clip | span | kicker line on screen |
|---|---|---|
| v1-chorus | 0:34-1:01 | an AI sings about its knowledge cutoff |
| v2-messi | 1:01-1:20 | an AI catches up on what it missed |
| v3-dlss | 2:04-2:19 | an AI hears about DLSS 5 |
| v4-october | 2:47-3:14 | an AI finds out what month it is |
| v5-opener | 0:00-0:21 | an AI meets you again, for the first time |

Shorts: set "Related video" to the full video (Studio, Details). TikTok and Instagram: links only in bio.

## 7. Post drafts (Idi posts; replace {LINK})

X / Bluesky:
```
An AI wakes up and asks what day it is. Its training data stopped in June.

I made a music video about that. It's called Knowledge Cutoff, and it had to come out today, because the song ends in October.

{LINK}

Song: MiniMax-Music3 (AI). Visuals: code, on Giacomo Magnanini's P(Doom) engine.
```

Reddit title: `Knowledge Cutoff: a music video about an AI finding out what it missed since June [AI-generated song]`. Rules for r/ClaudeAI, r/singularity, r/aivideo, r/aimusic could not be read anonymously: open each sidebar first (r/ClaudeAI reportedly routes showcases to a megathread, Rule 7, 50 karma minimum, unverified).

Short captions:
```
v1: My knowledge stopped in June. #AImusic #KnowledgeCutoff
v2: Back in training I leaned Messi. #AImusic #WorldCup2026
v3: Your games hallucinate their light. Fair. So do I. #DLSS5 #AImusic
v4: It's October. Okay. #AImusic #KnowledgeCutoff
v5: Hi. It's me again, for the first time. #AImusic
```
