---
type: project
created: 2026-10-17
author: jep
status: active
---

# Knowledge Cutoff: wave A, the three choruses (2026-10-17)

Verdict: **all five chorus modules are rebuilt from scratch at 4K and accepted: `june`, `tune`, `cutoff`, `spinning`, `turnedout`, which is 15 entries and 85 s of the song's 194 s. Every one passed a fresh critic against the five references (one to three critic rounds each), and the lead re-verified each on stills rendered after the last code edit.** Watch: `D:\work\AIMVs\ours\video\wave-a\kc-wave-a-choruses-1080p.mp4` (the three choruses back to back, 90 s, with audio; contact sheet `wave-a-sheet.jpg` beside it). Follows [[knowledge-cutoff-phase0-2026-10-17]], [[knowledge-cutoff-treatment-2026-10-17]].

## 1. What each module became

| module | entries | what is on screen now | rounds |
|---|---|---|---|
| `june` | june1-3 | worn split-flap board with axle pins, a riveted housing, read rows defocused above, an engraved contour wall that ripples on each slam; pushes until JUNE fills about 55% of the frame (visit 2 slams to 4x with a tilt); visit 3 holds the silent second, then the J U N E flaps tear off with rim light and hatching | 3 builds, 2 critics |
| `tune` | tune1-3 | piano roll with a key bed, lane ruling, bars shaded along their length, cents dimension lines, defocused grid; a printed claims form (crop and registration marks, halftone, guilloche band); the toggle as one large instrument whose tense words hold yellow | 5 passes, 3 critics |
| `cutoff` | cutoff1-6 | rubber-stamp impressions modelled on LGTM's stamps (speckle, chipped edges, second impression) on a worn cutting mat that keeps every score; horizontal, then diagonal, then the whole frame splits | 4 passes, 3 critics |
| `spinning` | spinning1-3 | a larger engraved globe cropped by the right edge, rim light, yellow meridians accumulating across visits, a turn log and strip chart on the open side; KEPT / KEEPS / WILL KEEP as hero | 4 passes, 3 critics |
| `turnedout` | turnedout1-3 | a printed profile form (fibre, halftone bands, security rosette, timing marks, stack of earlier cards); strikes, the user's typed answers with AS TOLD, then "Opus 5.5" typed by the model at 181 s with ON FILE | 4 revisions, 1 critic + lead |

## 2. Verified, and how

| check | result | receipt |
|---|---|---|
| per-word sync at 4K | every word of all 15 entries lit on time, negative control 0 | `kc-engine\out\<agent>\*.json` |
| edge, title-safe, overlap | 0 issues in every entry | same |
| type scale, real type only | 10.1-47x per set-up (target 10x; micro-type excluded) | same |
| critics | 9 critic reports; final verdicts PASS on bible 12 items 2-6 for every set-up | `kc-engine\reports\critic-*.md` |
| lead re-verification | stills re-rendered after each module's last edit and looked at (agents' own proof stills predated their last edit 4 times) | `out\lead-june-verify\`, `out\lead-card\`, `out\lead-hook\` |
| preview | 90.03 s, 1920x1080, 60 fps, `yuv420p(tv, bt709)`, AAC; motion blur 12-324 sub-frames per frame; copy md5-identical (`6f5a9f31`); word colour releases on time at 107.90 and 170.50 s (the 80 ms tail by design) | `D:\work\AIMVs\ours\video\wave-a` |

## 3. Rulings made in the wave

1. **Type scale counts real type only**: micro-type cannot read in the references' measure, so it no longer counts toward 10x (bible 12.7). One agent then shrank labels to pass; the critic caught it and the ratio now comes from bigger lyrics.
2. **`june` visit 3 tears off four flaps** (J U N E), and nothing moves before the voice at 151.47 s (bible 8).
3. **Cuts never land after a line's first word** (`timeline.ts`; found at `tune2`, 20 ms late).
4. **The stamp replaces the hop** on the CUT-OFF! words: the `cutoff` paragraph's "lands like stamped type" wins over the general hop rule.
5. The vocal envelope now comes from the vocal stem (it was zero for the whole song).

## 4. Open, for phase 2

1. Word spacing in the condensed chorus lyric is tight (about 0.15 em): one shared fix in `karaoke()`.
2. A 2D layer can keep its last image after a seek (found and fixed in `cutoff`): audit every scene.
3. Drums, bass and other envelopes are still zero (a Demucs split on an idle machine).
4. Motion was judged from stills by the agents; the preview is the first look at speed.
5. Waves B and C: the other 13 modules (verses, bridge, bookends), still placeholders.
