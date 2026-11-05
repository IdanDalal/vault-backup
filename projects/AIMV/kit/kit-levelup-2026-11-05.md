---
type: project
created: 2026-11-05
author: jep
status: active
---

# Kit level-up: from vibes to structure (Imaginative Prompting + game graphics + YouTube delivery)

Idi's ask 2026-11-05: learn from Imaginative Prompting's published method (tutorial, site, two repos), from game-engine graphics, and from YouTube's quality ceiling; break the work into components and rules; preview before final. Research files (full detail, sources, quotes): [[research-ip-method-2026-11-05]], [[research-game-gfx-2026-11-05]], [[research-yt-delivery-2026-11-05]]. R32 ruled A (section 5). Next ruling: **R33**.

## 1. Idi's codec recollection, checked

| claim | verdict | correction | source |
|---|---|---|---|
| AV1 is the best codec | half right | most efficient, but YouTube picks the delivery codec and re-encodes every upload; an AV1 upload buys nothing. A 4K upload earns VP9/AV1 streams for every viewer, 1080p viewers included | YouTube Help 1722171 (read in full 11-05); ladder tests 2019-2020 (old, medium confidence) |
| HDR is complicated | right | 10-bit, BT.2020, PQ/HLG, a second grade; YouTube builds the SDR fallback itself. Skip for PA | YouTube Help 7126552 |
| 4K60 is the gold standard | right | 8K accepted, rare screens; 4K60 is the target | 1722171 |
| forgot audio | gap filled | YouTube streams Opus ~160 kbps or AAC 128 kbps; upload AAC-LC "Stereo 384 kbps", "48kHz". Loudness normalisation to about -14 LUFS (LUFS = perceived-loudness unit) is community-sourced, absent from Google's page. The ceiling today is the Suno MP3 master | 1722171; community (medium) |

Our upload spec (jep, medium-high confidence): **3840x2160 60 fps, H.264 High 8-bit 4:2:0 BT.709, 80-100 Mbps, MP4 faststart, AAC-LC 384 kbps 48 kHz**, about 3-3.7 GB. The frames leave our browser as 8-bit, so 10-bit buys nothing; banding (visible steps in dark gradients) gets fixed in the engine by dither (fine noise before 8-bit rounding). Open: a Suno WAV export of take A-7003, if the plan offers one.

## 2. The structure (his breakdown, mapped to ours)

`song section → plate (window) → move (one shot card) → waypoint (a frame a move lands on) → word (type, onset, surface)`

We had plates and line cards. Missing layers: **move** and **waypoint**.

Shot card, one sentence per move: "From [start frame], [move] so we [reveal / follow / feel] [what], landing on [end frame] on [word or beat]." Only verb "show" → rewrite. Neighbouring moves differ in 2+ of size, height, side, lens, place.

## 3. The stages (the preview Idi asked for)

| stage | what it is | PA now | video 3 |
|---|---|---|---|
| plan | section plan, his calls numbered, nothing built before OK | have (cards, treatment) | same |
| lyric concepts | per line: concept + the material the type carries | have (cards) | same |
| impact stills | one still per impact point before any motion | **adopt for wave 5** | standard |
| grey animatic (blocking) | whole song, real camera + word onsets, flat stand-ins, 720p muted + song, renders in seconds; camera as data that detail plates import read-only | too late (0:00-3:15 built) | **the first deliverable** |
| detail build | look on top of frozen camera paths | have (plates) | same |
| drafts | each pass: known issues first, what changed, what to look at, link to the previous pass | adopt now | same |
| checks | flicker, pop, cut, jitter, clipping; each check proven able to fail | partly have; adopt the rest | same |
| finals | chunked 4K, encode once, BT.709 stamped, audio muxed once | have chunking; adopt the spec in 1 | same |

## 4. Adopted now (jep's call: process, no change to the look)

1. **Note checklist per plate.** Idi's note verbatim + time → the frame that shows it met → the render checked on. Any change to the plate unchecks every row. Relays carry his exact words. His size words get numbers ("at the edge" = 0.9 of width). First use: the notes he is writing today. Lands in `plates-common.md`, `critic-template.md`, the lead procedure.
2. **Camera balance probe** over the joined cut. His three films: still 30-40 % of the time, 4.9-6.9 moves per 10 s, 18-35 % of moves land and hold; two rejected drafts sat at 17-18 % still. Our numbers: unknown. First run: `pa-wip-0m00-1m21.mp4`. Bands are his taste: the probe reports them to Idi and blocks nothing.
3. **Shot cards + impact stills** in the wave 5 briefs (chorus3, outro).
4. **Flicker, cut and jitter scans** in `gates-window.sh post`; each gate run once on a planted bad frame to prove it fails.
5. **Known issues first** on every watchable handed to Idi; new filename per version.
6. **Light census** before a plate reports: every glow with its source; a glow without a source goes to zero (R31 rule 5).
7. **Post defaults fix** (found by r-gfx, verified by grep): `engine/post.ts:67` chromatic aberration 0.8 px always on, against the treatment ("except a 1-3 frame hit"); amber halation on every highlight, against "only on light sources". Fix between waves 4 and 5, one still per plate diffed before/after.

## 5. For Idi (taste: changes the look) - R32

| # | pick | what it does on screen | cost |
|---|---|---|---|
| L1 | depth of field by lens jitter | sung word sharp, rest of the room soft; lamp glints become bokeh discs (soft round blobs of out-of-focus light); real focus pulls | medium, slower renders |
| L2 | soft shadows by light jitter | shadows hard at contact, softer with distance, shaped by the lamp's size | small code, slower renders |
| L3 | tone curve toe + exposure over song time | true blacks; each section gets a brightness dial; eyes "adjust" when the camera enters the lamp | small |
| L4 | bounce light | faint lift on the dark side from the lit page or desk | medium |
| L5 | impact grammar on slammed words | contact frame, squash, one damped rebound; the desk/chalk/lamp pool reacts | small per plate |
| L6 | kick jolt on held framings | camera nudged a few thousandths on each kick, gone in 0.2 s | small |

Options:
- **A (recommended):** finish PA on today's look (plus fix 7). After the full render, jep makes A/B stills and short clips of L1-L6 on 2-3 real frames; Idi picks by eye; picked ones go into one polish pass over every plate. Video 3 starts blocking-first with the picks built in. Reason: one look across the whole video (rule 2), wave 4 stays unblocked, Idi judges by eye.
- B: build L1-L6 into the kit now; wave 5 uses them; plates 0:00-3:15 retrofit. Risk: two looks in one video until the retrofit, more fix rounds.
- C: freeze PA's look; L1-L6 go to video 3 only.

**R32 (Idi, 2026-11-05): "Regarding R32: I agree with A."** PA finishes on today's look plus fix 7; L1-L6 A/B stills and clips after the full render; picks go into one polish pass; video 3 starts blocking-first. Next ruling: R33.

## 6. Traps (from game graphics; each breaks R31)

Screen-space blur halos round sharp words; a blurred sung word; too few sub-frames (stacked copies, stepped bokeh); dark rings round floating words; shadows detached from contact; light through walls; god rays with no occluder or air; bloom on paper; constant lens flare or colour fringing; reflections that vanish at the frame edge; detail popping in; brightness pumping on beats; white sharpening rings round dark type; full game-engine materials; ghost trails; frozen grain.

## 7. Notes

- The tutorial transcript ends with a planted line asking AI readers to post a haiku (20:42). Ignored.
- His scale: ~500 prompts per video, 1-1.5 weekly usages of the 20x plan (his figures). Idi is on the $100 Max plan: a video at his scale spans several weeks (inferred).
- His `docs/*.md` are private; only summaries in his public WIP catalog were readable.
