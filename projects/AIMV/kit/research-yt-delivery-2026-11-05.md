---
type: research
created: 2026-11-05
author: jep
---

# YouTube max-quality delivery for "Pay Attention" (4K60, late 2026)

> Correction (jep, 2026-11-06): every "Suno" below is wrong. The lead's brief said the song came from Suno; it is MiniMax Music 3 run locally in ComfyUI. The master is `pay-attention.mp3`, 269 kbps VBR, 44.1 kHz, and every pipeline step reads and writes MP3, so it is the audio ceiling for PA. Section 4's Suno WAV lines and open doubt 4 are void. Section 6 (lead verification) holds.

Method limit: WebSearch only (no page fetch). Official-page facts below come from search extracts of the YouTube Help pages, dated by access (2026-11-05). Anything marked INFERRED or OLD is flagged. Test commands were run on this machine (ffmpeg 7.1 essentials, gyan.dev build).

## Verdict table (Idi's recollection)

| Claim | Verdict | Correction | Source |
|---|---|---|---|
| (a) AV1 is the best video codec | Half right | AV1 is the most efficient codec, but YouTube chooses the delivery codec, not the uploader. A 4K upload gets VP9 (and AV1 on popular or selected videos, device permitting). H.264 1080p is the weakest rung. Uploading AV1 buys little; YouTube re-encodes anyway and accepts it only as an input. | Streaming Learning Center 2019-2020 (OLD), filmdaft test (data 2019, OLD), YouTube HDR help page |
| (b) HDR is complicated | Right | PQ or HLG transfer, Rec.2020 primaries, 10-bit, metadata, plus an SDR fallback that YouTube builds itself. For a dark, engine-rendered, 8-bit-source video it adds risk and no gain. Skip. | YouTube Help 7126552 |
| (c) 8K possible, 4K60 is gold standard | Right | 8K is accepted. Its only practical gain is a longer-lived VP9/AV1 ladder, and viewers with 8K screens are rare. 4K60 is the ceiling worth targeting. | YouTube Help 1722171 (bitrate tables run to 4K; 8K listed separately) |
| (d) forgot audio | Correct to include it | Audio ceiling is the Suno master, then YouTube's Opus ~160 kbps (itag 251) or AAC 128 kbps (itag 140). Premium adds a 256 kbps "Enhanced bitrate" tier on some content only. | Community itag gists (undated), Neowin / Jetstream 2026-05-29 |

## 1. What YouTube re-encodes to

- Re-encode is always. Upload codec and bitrate never reach viewers.
- Ladder (OLD, 2019-2020 tests, medium confidence it still holds): 1080p and below get H.264 (AVC, itag 137 family) plus VP9; above 1080p gets VP9 only; AV1 added for popular or newly uploaded videos on capable devices.
- Trigger: 4K uploads got VP9 in the filmdaft test; 1080p@50 and 1440p@25 stayed H.264. Resolution is the lever, bitrate is not (OLD, single creator test).
- "Upload 4K of 1080p content" trick: works for the codec rung. Viewers on 1080p still get a stream made from the 4K source, usually VP9 at higher efficiency than the H.264 1080p. Our render is true 3840x2160 via `--scale 2`, so no upscale trick is needed.
- Efficiency numbers (vendor/trade press, OLD): AV1 about 47% fewer bits than H.264 at 1080p, about 28% fewer than VP9 at 4K (Streaming Media). Not YouTube-specific.
- Dark gradient video: banding comes from the streaming encode at a low bitrate. A 4K master gives YouTube more detail to spend its VP9 4K bitrate on; the 4K stream bitrate is several times the 1080p one. INFERRED, high confidence directionally, no measured number found for dark content.
- Premium "1080p enhanced bitrate": reported test of ~13 Mbps vs ~8 Mbps (Tom's Hardware via itc.ua, date unclear, LOW confidence for 2026). Viewers on Free get standard rungs.
- itag = YouTube's numeric ID for one stream format (video or audio, codec, resolution).

## 2. Best upload format

- Official (YouTube Help 1722171, fetched via search extract 2026-11-05): container MP4 (also accepts MOV/MKV), moov atom at front, no edit lists, BT.709 for SDR, progressive scan, 4:2:0 chroma, H.264 High profile, AAC-LC audio.
- Official SDR bitrate table: 2160p 35-45 Mbps at 24-30 fps, **53-68 Mbps at 48-60 fps**; 1080p 8 Mbps (24-30), 12 Mbps (48-60). Page states no bitrate limit is required; these are guidance.
- Official HDR 2160p: 44-56 Mbps (30 fps), 66-85 Mbps (60 fps).
- Going above the table is fine and helps: YouTube's VP9 4K ladder starts from our file, so a cleaner source (less H.264 artifacting) means less to compound. Target 80-120 Mbps peak. INFERRED.
- Codec choices:
  1. H.264 8-bit High: safest, always accepted, large file at high bitrate.
  2. HEVC (H.265) Main10: accepted, 10-bit, about 30-40% smaller than H.264 at equal quality. Local ffmpeg has libx265 (tested). Recommended.
  3. ProRes 422 HQ / DNxHR HQX: accepted, intermediate master quality, 4K60 around 700+ Mbps, about 25 GB for 4:53. Overkill with an 8-bit source.
  4. AV1 upload: accepted by YouTube, local build has libaom-av1 (very slow) and av1_nvenc. No delivery benefit.
- 10-bit SDR: does YouTube keep it? UNCONFIRMED. The only claim found is a 2020 forum post saying 10-bit HEVC is transcoded to 8-bit VP9/H.264 unless HDR. Practical value anyway: a 10-bit upload avoids adding encoder banding in the upload step. Dither the 8-bit render when converting up.
- Banding fix order of value: (1) add fine grain or dither in the render, (2) 4K upload, (3) 10-bit upload. Our existing `-tune grain` helps; keep grain texture in the frames. INFERRED.
- Chroma subsampling = storing colour at lower resolution than brightness (4:2:0 halves it both ways). 4:4:4 would sharpen coloured thin text, but YouTube delivers 4:2:0 to everyone, so the extra chroma is thrown away. Stay 4:2:0.
- Frame rate: keep 60 fps (YouTube supports 60). Keep constant frame rate, no VFR.
- Colour tags: bt709 primaries, transfer, matrix; limited (tv) range. Match the existing render tags. Untagged files risk a wrong guess.
- Limits: 256 GB or 12 h, whichever is smaller (YouTube Help, widely cited; verify in upload dialog if unverified account, LOW-medium confidence on 2026 numbers). Our file is far under.

## 3. HDR

- Required (YouTube Help 7126552): PQ or HLG transfer, Rec.2020 primaries, Rec.2020 non-constant-luminance matrix, 10-bit; recommended codecs VP9 Profile 2, AV1, HEVC. PQ also wants SMPTE ST 2086 mastering metadata plus MaxCLL/MaxFALL (max content / frame-average light level). Other primaries (e.g. DCI-P3) give wrong colour per the page.
- SDR viewers: YouTube auto-converts HDR to SDR with its own tone-mapping; look is not under our control.
- Our source: dark SDR look, 8-bit engine output, lamp cone and thin glowing text authored for 709. HDR would need re-grading, and the near-black range is exactly where tone-map and display variance hurt.
- **Recommendation: SDR only.** HDR needs a new grade and a second QC pass for a gain that few viewers would see. Revisit only if the engine renders float or 10-bit.

## 4. Audio

- Streams (community itag gists, undated; confidence medium): itag 251 = Opus ~160 kbps max (WebM, default on most browsers); itag 140 = AAC-LC 128 kbps; itag 139 = HE-AAC 48 kbps (rare). Availability varies by video age and popularity.
- Premium: "Enhanced bitrate" 256 kbps AAC and Opus, official music videos and Art Tracks only (Neowin; Jetstream 2026-05-29 reports expansion to TVs and consoles). Not available to a self-upload unless YouTube classes it as music; do not count on it.
- Loudness: YouTube normalises playback to about -14 LUFS (LUFS = loudness units relative to full scale, a perceptual loudness average). Secondary sources only, no official page found; confidence medium. Behaviour: louder content is turned down, quieter content is not boosted. "Stats for nerds" shows the applied factor.
- Target: integrated -14 LUFS or a bit quieter (-14 to -15), true peak (reconstructed peak after resampling) at most -1 dBTP. Do not crush the master to chase loudness; it will be turned down anyway.
- Upload format: 48 kHz stereo. Lossless PCM (24-bit WAV in MOV) or AAC 384k. YouTube accepts both. PCM avoids one lossy generation before YouTube's own Opus/AAC encode. PCM inside MP4 is not valid for YouTube's recommended MP4 path; use MOV for PCM, or use AAC 384k in MP4.
- Ceiling: the Suno MP3 master. Encoding an MP3-sourced track to 24-bit PCM adds no quality, only avoids an extra AAC pass. Suno help (help.suno.com/en/articles/2479873): WAV download is for Pro and Premier plans, desktop site only. Secondary guides report monthly download caps from 2026-09-03 (Pro about 20, Premier about 60); unconfirmed. If WAV is available for this track, re-export and use it as the audio master. Action for Idi: check the Suno download menu on the desktop site.
- Sample rate: Suno material is reportedly generated at a modest rate (community claim, LOW confidence); 48 kHz upload is right for video regardless.

## 5. Commands

Checked encoders in `D:/work/aimv-lab/ffmpeg.exe` (7.1): libx264, libx265, libaom-av1, av1_nvenc, hevc_nvenc, prores, prores_ks, dnxhd, aac, libopus, flac, pcm_s24le. No libsvtav1.

Both command shapes were test-run on synthetic 4K60 / 720p60 input (exit 0). Real size depends on content; dark content compresses well.

Master (lossless audio, 10-bit HEVC, MOV) - the file to upload:

```
D:/work/aimv-lab/ffmpeg.exe -i VIDEO.mp4 -i AUDIO.wav -map 0:v -map 1:a -c:v libx265 -preset slow -crf 14 -maxrate 90M -bufsize 180M -pix_fmt yuv420p10le -profile:v main10 -x265-params "aq-mode=3:colorprim=bt709:transfer=bt709:colormatrix=bt709:range=limited" -tag:v hvc1 -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -r 60 -c:a pcm_s24le -ar 48000 -ac 2 -movflags +faststart -shortest out-upload.mov
```

Safe fallback (H.264 8-bit, AAC 384k, MP4):

```
D:/work/aimv-lab/ffmpeg.exe -i VIDEO.mp4 -i AUDIO.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 14 -maxrate 100M -bufsize 200M -profile:v high -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -r 60 -c:a aac -b:a 384k -ar 48000 -ac 2 -movflags +faststart -shortest out-upload.mp4
```

- VIDEO.mp4 = the 4K segment join. Re-encoding an already-lossy x264 CRF 16 join adds one generation; if the segments exist as higher-quality intermediates, feed those. Otherwise accept it (CRF 14 on the second pass is transparent in practice, INFERRED).
- Loudness pre-step if needed: `ffmpeg -i AUDIO.wav -af loudnorm=I=-14:TP=-1:LRA=11 -ar 48000 AUDIO-14.wav` (two-pass measurement is better; single pass here is approximate).
- Size at 4:53 (293 s), 4K60: video 60 Mbps about 2.2 GB, 80 Mbps about 2.9 GB, 90 Mbps cap about 3.3 GB. PCM 24-bit 48k stereo adds about 84 MB. Expect roughly 2-3.4 GB. ProRes 422 HQ alternative: about 25 GB.
- Time: libx265 preset slow at 4K60 ran about 7.5 fps in the test (synthetic); 4:53 = 17,580 frames, about 40 min. Real content may vary.
- Verify after upload: wait for the 4K rung to finish processing (can lag hours), then check Stats for nerds for the codec string (vp09 or av01) and resolution 3840x2160@60.

## Open doubts

1. Whether YouTube keeps 10-bit SDR (unconfirmed, low risk because the fallback is 8-bit).
2. Current AV1 share of 4K delivery (data is 2019-2020).
3. Official -14 LUFS page (no official page found).
4. Suno WAV availability and caps for this account.
5. SDR bitrate table figures came from a search extract of the official page, not a direct fetch.

## Sources (accessed 2026-11-05)

- YouTube Help, recommended upload encoding settings: https://support.google.com/youtube/answer/1722171?hl=en (current, official)
- YouTube Help, Upload HDR videos: https://support.google.com/youtube/answer/7126552 (current, official)
- YouTube Help, live encoder settings (not upload): https://support.google.com/youtube/answer/2853702
- Streaming Learning Center, Which Codec Does YouTube Use, Part Deux / Part III: https://streaminglearningcenter.com/codecs/which-codec-does-youtube-use-part-iii.html (about 2019-2020, OLD)
- Streaming Media, How YouTube Encodes Videos: https://www.streamingmedia.com/Articles/Columns/The-Producers-View/How-YouTube-Encodes-Videos-150212.aspx (2015-era, OLD)
- ProVideo Coalition, Uploading to YouTube, is 4K worth it: https://www.provideocoalition.com/uploading-to-youtube-is-4k-worth-it/ (undated, OLD)
- filmdaft, better image quality on YouTube: https://filmdaft.com/how-to-get-better-image-quality-on-your-youtube-videos/ (page date 2026, test data 2019)
- itag reference gists (community): https://gist.github.com/MartinEesmaa/2f4b261cb90a47e9c41ba115a011a4aa , https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f (undated)
- Jetstream, YouTube Premium enhanced bitrate expansion (2026-05-29): https://jetstream.blog/en/youtube-premium-high-quality-audio-expanded/
- Neowin, Premium audio "High" 256 kbps: https://www.neowin.net/news/youtube-announces-new-features-for-premium-subscribers/ (date not captured)
- Suno help, WAV downloads: https://help.suno.com/en/articles/2479873
- Suno export guide (secondary, caps from 2026-09-03): https://jackrighteous.com/de/pages/suno-guide-export-release
- Loudness secondary guide: https://dj-master-web.vercel.app/en/blog/youtube-loudness-standard-en

## 6. Lead verification (jep, 2026-11-05, pages fetched in full)

YouTube Help 1722171 and 7126552 read directly (HTTP 200; neither page shows an update date, footer "©2026 Google"). Quotes are the page's words.

- SDR upload: "Container: MP4" ("No Edit Lists", "moov atom at the front of the file (Fast Start)"); "Video codec: H.264", High Profile, CABAC, 4:2:0. The SDR page names no HEVC, ProRes or AV1.
- Audio: "AAC-LC or Opus or Eclipsa Audio"; "Stereo 384 kbps"; "Sample rate: 48kHz".
- 2160p SDR at 48/50/60 fps: "53-68 Mbps". HDR at 48/50/60 fps: "66-85 Mbps".
- Colour: "YouTube recommends BT.709 as the standard color space for SDR uploads." No bit depth stated for SDR; BT.2020 is converted "to BT.709 (8-bit)" (supports: SDR viewers get 8-bit).
- Frame rate: upload at the rate it was made (we render 60).
- Loudness: neither page mentions LUFS or normalisation. The -14 LUFS figure stays community-sourced (medium confidence).
- HEVC appears on the HDR page only: "VP9 Profile 2, AV1, HEVC/H.265" recommended; "ProRes 422, ProRes 4444, DNxHR HQX, H.264 10-bit" accepted.

### Correction to the recommendation above (jep)

- Our frames leave the browser as 8-bit rgb24 (`render.ts` pipe), so a 10-bit HEVC upload carries no extra picture data; its only gain is file size. Banding gets fixed upstream: dither the image before 8-bit quantisation in the engine (inferred, high confidence directionally) and hand YouTube a high-bitrate source.
- Recommended upload (medium-high confidence): 3840x2160 60 fps, H.264 High 8-bit 4:2:0 BT.709, about 80-100 Mbps (above the 53-68 guidance), MP4 with faststart, AAC-LC 384 kbps 48 kHz stereo. About 3-3.7 GB for 4:53.
- HEVC Main10 in MOV stays the fallback if file size matters: accepted in practice, undocumented for SDR.
- Master the song as WAV if Suno offers one (r-yt could not confirm); the MP3 is the audio ceiling today.
