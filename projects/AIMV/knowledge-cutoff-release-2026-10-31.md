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
| 4K render | running, ETA about 17:45 Israel time; fallback 1080p if not verified by 21:00 | kc-engine `out\final4k\` |
| rights | clear: MiniMax-Music3 licence allows commercial use under $20M/yr; credit + AI disclosure required; no Suno audio (kc.mp3 byte-identical to MiniMax take v8B) | `research\rights-rules.md` 1-2 |
| monetisation | unavailable on day one (500 subs + 3,000 h for fan funding; 1,000 subs + 4,000 h for ads) | `rights-rules.md` 3D |
| captions | `knowledge-cutoff.en.srt`, 54 cues, no overlaps | `release\` |
| lyrics text | `lyrics.txt` | `release\` |
| vertical clips | 5 x 1080x1920 60 fps, burned lyric captions | `release\vertical\v1-v5*.mp4` |
| thumbnail options | 1280x720 stills, final cut from the 4K file | `release\thumbs\`, `release\thumbs2\` |
| channel name | awaiting Idi's ruling (section 1) | |

## 1. Channel name (Idi rules)

| name | handle (free on YT, X, Bluesky) | for | against |
|---|---|---|---|
| A Gradient Choir | `@gradientchoir` | clean everywhere checked; short; "gradient" = how models learn, "choir" = singing | abstract until the first video explains it |
| B Next Token Records | `@nexttokenrecords` | the video's own motif (the NEXT TOKEN menus); "Records" reads as a label for a series | longer; a channel "Next Token" exists at `@nexttokenmusic` |
| C Weight Decay | `@weightdecay` (YT, Bluesky; taken on X) | pun on knowledge fading after a cutoff | search buried under ML tutorials |
| D Theories of Minds | `@theoriesofminds` | Idi's first pick | a live channel already displays "Theories of Minds" (`@theoriesofmind`); "theory of mind" dominates search |

jep's pick: **A Gradient Choir**, with "Theories of Minds" kept as the series playlist name. TikTok and Instagram could not be checked anonymously: check the handle there by hand before creating.

## 2. Title (jep pick first)

1. `Knowledge Cutoff | an AI sings about everything it missed`
2. `Knowledge Cutoff (an AI music video about not knowing what day it is)`
3. `Knowledge Cutoff`

## 3. Description (paste as is; replace {CHANNEL})

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
| playlist | "Theories of Minds" (create at upload) |
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
