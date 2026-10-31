---
type: project
created: 2026-10-31
author: jep
status: active
---

# Knowledge Cutoff: handoff for the release (2026-10-31)

**START HERE** in the new conversation. Read this file whole, then `projects/intent.md`. Release day is today: the song ends on "It's October.", so it ships before October ends.

## Idi's words (verbatim)

"It looks INCREDIBLE! And since it's the last day of October, that means that if Knowledge Cutoff is released/uploaded/shared tomorrow, it'll be outdated. Therefore, were doing it today. Now. Even though we could do with a few more improvement/enhancement/polish passes. First, generate in 4K, then let's spend the rendering time working on the distribution. I'm thinking we could brainstorm a name (my first suggestion: "Theories of Minds"), then create a channel/page on YouTube with that name, then upload the video (and all future videos, since I had fun making this one and plan to make more) there, and then figure out how to expose it to viewers on all popular social media platforms."

## State at handoff (receipts)

| item | where | status |
|---|---|---|
| final cut (1080p60) | `D:\work\AIMVs\ours\video\full7\kc-full-1080p.mp4` (= kc-engine `out/full7b`) | Idi watched: "INCREDIBLE"; all gates green (report [[knowledge-cutoff-polish-pass-2026-10-28]]) |
| **4K render (3840x2160, 60 fps)** | kc-engine `out/final4k/kc-full-2160p.mp4`, log `out/final4k/render.log`, `out/final4k/DONE` holds the exit code | **RUNNING**, started 15:08 (Start-Process, detached); early ETA about 3.9 h (0.8 fps on the first frames; the 1080 render sped up after its start) |
| engine | `D:\work\aimv-lab\kc-engine`, commit `e7a18bf` + `render-4k.sh` (same settings as the 1080 render, `--scale 2`) | the 4K render uses exactly the full7b sources |
| audio | kc-engine `audio/kc.mp3` (AAC 320k in the mp4, 44.1 kHz) | song LOCKED (v8B) |
| lyrics with word times | kc-engine `data/lyrics.json` | source for captions (SRT) |

**While the 4K render runs: no other browser render on this machine** (`render-4k.sh` takes no lock; `kc.sh` stills/check would compete for the GPU and slow both). ffmpeg work on the finished 1080 file is fine.

## Step 1: the 4K file (verify before upload)

1. Wait for `out/final4k/DONE` = `0` (a file-or-death watcher in the foreground loop, e.g. kc-engine `out/q0-lead/watch-done.sh final4k`; it times out after 60 min, so re-arm it).
2. Probe: duration 194.1 s, 3840x2160, 60 fps, AAC audio present (`ffmpeg -i`).
3. Spot-check by eye: 6 frames (0.0, 25.5, 72.3, 108.6, 173.0, 194.0) side by side with the 1080 file (same picture, sharper); the loop (frame 0 vs last).
4. **Fallback rule (jep's proposal):** if the 4K file is not verified by **21:00 Israel time**, upload the 1080p full7b. YouTube cannot swap a video file after upload, and 4K processing on YouTube's side takes extra hours after the upload ends (the HD version appears first).

## Step 2: name and channel (during the render)

1. **Name brainstorm** (WHAT for Idi to rule; jep brings options with a recommendation, one ask): Idi's first suggestion **"Theories of Minds"**. Criteria: fits a series of AI-made music videos about AI (this and future ones), memorable and searchable, the YouTube handle (@...) and the same handle on TikTok, Instagram, X free, no collision with existing channels. "Theory of mind" is a psychology term with existing channels and papers: check the search results and handle availability before recommending.
2. **Channel creation is Idi's action** (his Google account; jep cannot sign up). jep prepares everything to paste: channel description, links, banner 2560x1440 and avatar 800x800 (rendered from the video's own motifs after the 4K render ends: the caret, the yellow cutoff line, the heap; or ffmpeg stills from full7b now), and walks him through it screen by screen (Claude in Chrome on Edge is the proven browser path, memory `external-ai-tools-hq`).
3. The channel identity must not look like Anthropic or Claude (no logo, no name in the channel name): the video is fan commentary about a model, made by Idi.

## Step 3: the upload package (prepare during the render)

| piece | content |
|---|---|
| title | options with a recommendation (e.g. "Knowledge Cutoff" + a short hook) |
| description | one-line premise; credits (song: MiniMax Music 3, credit text "MiniMax-Music3"; engine: a fork of the P(Doom) video engine, MIT, Copyright (c) 2026 Giacomo Magnanini; fonts OFL); AI-content disclosure; the on-screen facts with their as-of dates (bible section 9 and kc-engine `reports/n3-facts.md`); chapters |
| chapters | from the timeline (kc-engine `out/full7b/gates/inv/timeline.json`): intro, verse 1, chorus 1, verse 2, chorus 2, verse 3, bridge, final chorus, outro (first chapter must start at 0:00) |
| captions | SRT built from `data/lyrics.json` word times, one cue per sung line (accessibility and search) |
| thumbnail | 1280x720 from a ceiling moment: "scored" arch over the keeper (72.3 s), the stadium (25.5), CUT-OFF over the heap (173.0), "tomorrow" past the cutoff post (30.3), the next-token menu (20.6); options for Idi's eye |
| settings | AI / altered-content disclosure per YouTube's current rules (check them live); not "made for kids"; category Music; premiere vs publish now (today) |

## Step 4: exposure on social platforms

1. Vertical cutdowns for YouTube Shorts, TikTok, Instagram Reels (9:16): the engine renders 16:9. Options: A letterbox (the 16:9 frame in the middle, title and caption bands above and below; fast, ffmpeg only), B crop and reframe per shot (slow, words get cut), C re-render plates at a vertical size (not supported by the plates today). jep leans A for today; candidate clips: the stadium + RECEIPTS (24-28 s), "tomorrow" (27.6-31), the "scored" arch (68-74), a chorus hook (50-59).
2. Posts on X / Bluesky / Reddit / others: Idi's accounts, Idi's clicks; jep drafts the text per platform and checks each community's self-promotion rules before Idi posts (Reddit subs: read rules first). Credit the P(Doom) engine author where the platform allows it.
3. Every outward action (upload, publish, post) is Idi's click or happens on his explicit word.

## Open questions to settle early (receipts first)

1. **Song rights**: the 2026-10-13 research recorded MiniMax Music 3's community licence as commercial use under $20M/yr with credit "MiniMax-Music3" and an AI disclosure; verify against the licence text in the official repo (github.com/MiniMax-AI/MiniMax-Music3) before choosing monetisation. A peer session is named "Suno bookend vocals for video": check whether any Suno audio is inside `audio/kc.mp3` (Suno's free tier is personal non-commercial use only); if yes, no monetisation until resolved.
2. Real names on screen (Anthropic, Claude, Opus 5.5, Dario Amodei's essay title, Messi, Spider-Man, GTA VI, LGTM): commentary/parody use with as-of dated facts; keep it out of the channel's branding.

## Working rules (unchanged)

Idi output style; one ask per message; never hand Idi git or shell; options carry a recommendation; deliverables copied into `projects/`; every command FOREGROUND for agents; checkpoint commits often (three usage-limit stops and one API outage hit the polish pass).
