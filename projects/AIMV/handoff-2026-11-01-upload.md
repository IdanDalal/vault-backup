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

## 2026-11-01 step 1 outcome (jep)

- Original 4K render FAILED: `out\final4k\DONE` = 1, 23:34 on 10-31, WebGL context lost + `readFinish: fence wait failed`; mp4 had no moov (index). No driver reset or low-memory event in the Windows logs 22:30-00:30; cause unproven (prior: GPU memory pressure).
- Idi ruled option A (repair + tail render) 11-01, on condition of no visible compromise.
- Recovered frames 0-10835 from the broken file (own scanner: audio packets matched a deterministic re-encode byte for byte, 7,822/7,822); tail 180.6-194.1 s re-rendered 4K, 1 worker, 810 frames, exit 0 (`out\final4k-repair\tail.log`).
- Overlap 46 frames: aligned (shift 0 = 43.6 dB, shift 1 = 20.1 dB), not bit-identical; engine renders to `tol` 3 levels, so two runs differ at that level everywhere. Join at keyframe 10836; consecutive-frame PSNR across the join 19.2 / 16.5 / 18.8 / 19.6 dB (no spike).
- mp4 assembled by own muxer (exact POC timestamps; ffmpeg raw-stream mux dropped frames 0, 4, 11645 and the audio, discarded).
- FINAL `D:\work\aimv-lab\kc-engine\out\final4k-repair\kc-full-2160p.mp4`, hard link `D:\work\AIMVs\ours\release\UPLOAD\knowledge-cutoff-2160p.mp4`, 13,608,210,133 bytes (handoff estimate 7 GB was wrong). Verified: 194.10 s, 3840x2160, 60 fps, H.264 High BT.709, AAC 44.1 kHz; 0 decode errors; 11,646/11,646 frames, order identical to the raw stream; tail pixel-identical to the tail render; audio byte-identical to the re-encode; six frames vs 1080 file 33.6-40.0 dB same picture; loop frame 0 = last frame shot.
- Scratch to delete once uploaded: `out\final4k\kc-full-2160p.mp4` (12.8 GB broken), `out\final4k-repair\recA.h264`, `joined.h264`, `tail.h264` (about 27 GB).
- Next: step 2 (channel, Idi's clicks). Open WHAT: the "Released 31 October" description line.
