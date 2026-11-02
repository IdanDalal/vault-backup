---
type: project
created: 2026-11-02
author: jep
---

# Release playbook (from Knowledge Cutoff, 2026-10-31 to 11-01)

Source: [[knowledge-cutoff-release-2026-10-31]], [[handoff-2026-11-01-upload]], [[kc-upload-checklist-2026-11-01]], [[chorus-of-minds-accounts-2026-11-01]]. Tools: `D:\work\aimv-lab\kit-tools\`.

## 1. Final render

| rule | why (KC receipt) |
|---|---|
| Render the master in chunks (4 x ~50 s, `--noaudio`), join at keyframes, mux audio once | one 8 h 26 min 4K render died at frame ~11,580/11,646 (WebGL context lost, `readFinish: fence wait failed`); single-file renders lose everything on one crash |
| `render.ts` kills ffmpeg on failure -> mp4 without moov (index) | by design; rescue recipe = `kit-tools\mp4-repair\README.md` |
| 4K = `--scale 2`, 0.4-1.4 fps on the 4090, ~9x the 1080 time | KC: 1080 render 54 min (full7), 4K 8 h 26 min |
| Stop llama-server and heavy apps before long renders; watch free RAM | 0.7 GB free at 20:20 on 10-31 (prior for the crash, unproven) |
| Expect reruns to differ at ~43 dB PSNR | adaptive sampling stops at tol 3 levels; a join between runs is invisible (seam PSNR in line with neighbours) |
| File size at CRF 16, tune grain, 4K60: ~70 MB/s of video (13.6 GB for 194 s) | handoff estimate 7 GB was wrong; YouTube takes up to 256 GB |

Verification before upload (all must pass): `ffmpeg -i` duration/size/fps/codecs; full decode 0 errors; frame count = duration x 60; six frames vs the approved 1080 cut (same picture); loop (frame 0 vs last); audio packets vs a fresh encode; `-y` on every check.

## 2. Thumbnail

| step | rule |
|---|---|
| Pick the moment | title-as-image read best at phone size (T1 KNOWLEDGE / CUT-OFF! stamp) |
| Build in code | PIL at 2x, video's own fonts and yellow; scripts `release\thumbv2\..`, `thumbv6\thumbv6.py`, `channel\header3x1.py` |
| Depth layers | real 4K frames as feathered pieces at far/mid/near depth; plate darkened in a shadow that follows the title (no boxes); title stays the only sharp yellow thing |
| Measure before showing | ink spans and midpoints in px (`kit-tools\thumbnail\measure-bands.py`); Idi caught a 48 px low centre on 10-31 |
| Phone check | 168 px wide preview, nearest-neighbour x3 (`preview-sheets.py`) |
| Blind panel | fresh agent, current version mixed in unlabelled; asks: readable text, eye order, artifacts, busy 1-5, click 1-10 |
| Slice effects | a shifted half moves letters: re-kern across the cut (KC: T-to-hyphen 34 -> 14 px) |
| Colour logic | Idi's rule: white above the cut line, yellow below (x in the credit line turned white) |
| Limits | 1280x720 JPG, under 2 MB (KC 290 KB); bottom-right stays clear for the duration badge |

## 3. Channel and accounts

- Channel via "Create a new channel" = Brand Account (Google Help 1646861): several owners; primary ownership transferable after both parties hold roles 7+ days (Help 7311601).
- Custom thumbnails need phone verification ("intermediate features", Help 9890437). One number = 2 channels per year (Help 171664). KC: the first code verified, the thumbnail still asked; Dad's number unlocked it. Check Studio → Settings → Channel → Feature eligibility first.
- Brand Gmail `chorusofminds@gmail.com` for every other platform; personal Gmail = recovery. Sign-up privacy: no Web & App Activity, history and ad personalisation off.
- Handles `chorusofminds` on YouTube, X, Bluesky, Instagram. TikTok: web sign-up forces the phone app (TikTok Help documents app sign-up only); skipped.
- Assets: avatar 800x800 (all), YouTube banner 2560x1440 (1546x423 safe area), header 1500x500 (X, Bluesky; no logo, the avatar overlaps bottom-left).
- Bios (Idi 11-01, interim): "Fan commentary. Not affiliated with any company."
- Passwords in a password manager; never in the vault (it pushes to GitHub).

## 4. Upload (YouTube Studio, 2026 layout)

| field | KC value / rule |
|---|---|
| Title | `Knowledge Cutoff | Claude Opus 5.5 + MiniMax Music 3` (Idi: tools in the title) |
| Description order (Idi's final) | lyrics first with [Intro]/[Verse]/[Chorus] labels → CREDITS → AI DISCLOSURE → ON-SCREEN FACTS with dates; 5,000 char cap (KC 3,925); no `<` `>` |
| Hashtags | type them in YouTube's description box: its dropdown shows video/channel counts; first 3 show above the title. KC: #aimusicvideo #aimusic #claudeai (#aidoompop does not exist on YouTube) |
| Tags field | plain words, misspellings and variants (YouTube: tags play a minimal role) |
| Subtitles | Video elements step → Add subtitles → Upload file → With timing (SRT from the word-timed lyrics) |
| Altered or synthetic content | Yes |
| Audience / category | not made for kids / Music |
| Processing | 2160p60 was served the same day (probe: watch page `qualityLabel`) |
| Honesty | dates and claims must stay true on the real publish date (KC: "Released 31 October" → "Finished 31 October") |

Post-publish probe (anonymous): oEmbed for title/channel, `i.ytimg.com/vi/ID/maxresdefault.jpg` for the thumbnail, watch page (cookie `SOCS=CAI`) for `qualityLabel`, `captionTracks`, `isUnlisted`.

## 5. Posting

| platform | rule |
|---|---|
| X | 280 chars, a link counts 23 (KC 279) |
| Bluesky | 300 chars, full link counts (KC 284); verify live via `public.api.bsky.app/xrpc/app.bsky.feed.getPostThread` |
| Instagram | link in profile Links; posts from instagram.com Create |
| Reddit | r/ClaudeAI removed the KC post: it did not explain Claude's role and the process. Next time: a process write-up + public repo link; post from an account with karma |
| Shorts / vertical | 5 clips built (`release\vertical\`), skipped by Idi 11-02 |

## 6. Close-out

Send jep the link → probe → log links in the release doc → delete render scratch only after the 4K probe passes (KC freed 40 GB) → memory + intent-log row.
