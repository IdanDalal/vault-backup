---
type: project
created: 2026-10-31
author: jep
status: active
---

# Knowledge Cutoff: handoff for the upload (2026-11-01)

**START HERE** tomorrow. Package with every ruling and paste-ready text: [[knowledge-cutoff-release-2026-10-31]]. Previous: [[handoff-2026-10-31-release]].

## Idi's words (2026-10-31, verbatim)

- "I'd rather upload 4K tomorrow than 1080p today."
- "Keep the banner, creating the channel will wait for tomorrow, since I'm going to a Halloween party now. When I wake up tomorrow I'll come back to check the render output. You can stop "stressing about"/measuring the render time."

## Rulings locked on 10-31

| item | ruling | file |
|---|---|---|
| channel | **Chorus of Minds**, `@chorusofminds` (free on YT, X, Bluesky at 19:xx; TikTok/IG unchecked) | release doc section 1 |
| avatar | A4 neural chords ("perfect") | `D:\work\AIMVs\ours\release\UPLOAD\avatar.png` |
| thumbnail | tilted T1, S1 concert fonts, mirrored to 0.5 px ("perfect") | `UPLOAD\thumbnail.jpg` |
| banner | A4 + Cinzel name + "AI music videos about AI" (kept) | `UPLOAD\banner.png` |
| file | 4K only; 1080p fallback withdrawn | kc-engine `out\final4k\kc-full-2160p.mp4` |
| genre tag | `#AIDoompop` first hashtag; banner stays genre-free | release doc section 5 |

## Steps tomorrow, in order

1. **Verify the 4K file** (jep, before Idi touches anything): `out\final4k\DONE` = `0`; `ffmpeg -i` shows 194.1 s, 3840x2160, 60 fps, AAC; six frames (0.0, 25.5, 72.3, 108.6, 173.0, 194.0) side by side with the 1080 file (same picture, sharper); loop (frame 0 vs last). Expected size about 7 GB. Copy (hard link) into `release\UPLOAD\`. If DONE is missing or nonzero: read `render.log` tail, report, do not re-render without Idi's word.
2. **Channel** (Idi's clicks): release doc section 1 steps 1-4 (create, handle, phone verify, avatar/banner/description). Claim `@chorusofminds` on TikTok and Instagram by hand.
3. **Upload** (Idi's clicks): release doc section 4 settings + section 3 description + `knowledge-cutoff.en.srt` + `thumbnail.jpg`. AI disclosure = yes. Publish now. 4K processing on YouTube runs hours after the HD version appears.
4. **Shorts / TikTok / Reels**: `release\vertical\v1-v5*.mp4` (1080x1920, captions burned); Shorts "Related video" = the full video.
5. **Posts**: release doc section 7 drafts; Reddit rules unread (open each sidebar first).

## Open notes

- The description says "Released 31 October 2026, because the song ends in October." If the upload lands on 1 November, change that line (jep proposal: "Finished 31 October 2026, because the song ends in October."). WHAT for Idi.
- October 31 lasted in Los Angeles until 09:00 Israel time on 1 November (US clocks changed back that day).
- Monetisation: not available until 1,000 subs + 4,000 h (or 500 + 3,000 for fan funding). Licence allows it later (MiniMax-Music3 credit + AI disclosure).

## Working rules (unchanged)

Idi output style; one ask per message; never hand Idi git or shell; options carry a recommendation; deliverables copied into `projects/`; agents run commands in the foreground.
