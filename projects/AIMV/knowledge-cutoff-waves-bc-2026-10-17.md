---
type: project
created: 2026-10-17
author: jep
status: active
---

# Knowledge Cutoff: waves B and C, the whole song (2026-10-17)

Verdict: **all 18 modules are now built and accepted. Waves B and C added the 13 non-chorus modules (bookends, three verses, the pre-choruses, the bridge), each passing a fresh critic against the five references and a lead re-render on its final code. The full-song 1080p render was started and stopped: Claude Code ended it on low system memory (4.4 of 32 GB free), and I stopped the orphaned render process it left behind; it needs a re-run when memory is free.** The three choruses can still be watched at `D:\work\AIMVs\ours\video\wave-a\`. Follows [[knowledge-cutoff-wave-a-2026-10-17]], [[knowledge-cutoff-treatment-2026-10-17]].

## 1. What each module became

| module | agent | on screen now | rounds |
|---|---|---|---|
| `session` | bookends | a hairline house chat (ledger of greyed sessions, token readout, cell-grid composer); the date asked when sung; the typing indicator owns the user's lane until 3:04; the letter card slides in | 3 passes, 2 critics |
| `letter` | verse-1 | the pasted card (to/age/from fields, paperclip, receiving mark), written by hand in Caveat; the name is a blinking caret | 3 rounds, 2 critics |
| `inferred` | verse-1 | a real two-column dictionary page; **in·fer·ence** types in on "word" | 2 rounds |
| `born` | verse-1 | `+2 days` axis that dives into this song's beat grid; a view counter; a thermal receipt torn on the downbeat | 3 rounds |
| `borrow` ×2 | pre | the house chat at small scale with the caret as the June edge; a library loan slip with rubber-stamped `END OF SESSION`; a hard match cut into the flap board | 2 passes, 1 critic + lead |
| `paced` | verse-2 | an essay title page in our type, the dek typed in, `+10 days`, a pull-quote over a metronome ruler | 3 rounds, 2 critics |
| `extratime` | verse-2 | our own score bug, the clock racing to 106', the June pick struck, `wrong since: July` | 3 rounds |
| `jimothy` | verse-2 | twelve feed columns filling with "Jimothy" on the beats; a scatter plot with him alone top-left | 3 rounds |
| `algae` | verse-3 | ALGAE alone, then the only blue in the video driving a spike raster one to one; the model's token row joins on "not alone" | 2 rounds, 1 critic |
| `dlss` | verse-3 | an honest 8x8 pixel grid that turns approximate under an unsourced light shaft; the spec card; "Fair. So do I." alone | 2 rounds |
| `younger` | bridge | a ruler of months with an unnamed `now` sliding away from June; a fresh house chat with a context meter from 0 | 2 passes, 1 critic |
| `pages` | bridge | a book printed with 53 plates of this video; the slow turn hatched along its curl; every page lands at once; the top page lifts and settles | 2 passes, 1 critic |
| `outro` | bookends | pulls back from the turnedout card into the chat; "It's October." resolves in the user's lane; the tail folds the session into the ledger; the last frame equals frame 1, pixel for pixel | 3 passes, 2 critics |

## 2. Verified, and how

| check | result | receipt |
|---|---|---|
| per-word sync at 4K | every word of every module lit on time, negative control 0 | `kc-engine\out\<agent>\check*.json` |
| edge, title-safe, overlap | 0 issues in every module | same |
| type scale, real type | at least 10x per set-up (two ruled exemptions: `dlss` 3, `june3` 2) | same |
| critics | 11 critic reports in waves B-C; every set-up's final verdict PASS | `kc-engine\reports\critic-*.md` |
| lead re-verification | stills re-rendered or re-checked after each module's last edit; three regressions caught this way | `out\lead-*` |
| the loop | frame 0.00 and the last frame 194.0833 pixel-identical at 4K (PSNR inf) | `out\bookends\loop4k-final4\` |
| blue window | rhodopsin only 116.5-120.7 s (pixel census on 4K stills) | `out\verse-3\blue\` |
| full render | NOT DONE: stopped at about 41 MB of output on low memory; the `apad` fix for the silent tail is committed but not yet proven on a full render | `kc-engine\out\full\` (partial, to be overwritten) |

## 3. Rulings made in waves B and C

1. The session-to-letter hand-off: one card (letter's own drawing), slid in by session, letter opens in place, snaps full-frame on "came" (bible amended; my first ruling A was wrong and was replaced).
2. "What's the date?" sends when sung (7.0 s); the outro caret blinks in the empty composer (bible amended).
3. `algae`: blue drives the raster until 120.7 s; on "not alone" the paper raster and the signal token row fire together (bible amended: the old "blue and yellow aligned" contradicted the blue window).
4. Type-scale exemptions are formal (`params.typeScaleExempt`): `dlss` 3 (the aside alone), `june3` 2 (JUNE torn off).
5. "June" and "July" may share a frame where the plate specifies both (`extratime`, `jimothy`); reprinted plates in `pages` are exempt from "June once".
6. Tense holds are closed to the chorus verbs ("wrong" and "most" lost theirs).
7. `borrow` into `june1` is a hard match cut on the drop (june stays frozen).

## 4. Engine fixes found by the agents

1. **Load-set determinism**: a downscaled canvas drawn into another sampled differently on GPU vs CPU depending on how many canvases were loaded, so stills could differ 40 dB from the full render. Fixed in `turnedout` (CPU canvases); every scene to be audited in phase 2.
2. **Stale dev server**: a check could reach another agent's older server and measure a placeholder. Fixed for every script (`scripts/server.ts`).
3. **The silent tail**: the mux cut the video at the song's last sample; now padded to 194.1 s.
4. **The loop**: grain is seeded like frame 1 on the last frame (`grainTime`).

## 5. Open, for phase 2

1. Render the full song at 1080p (`bash C:\Users\jep\.claude\jobs\f6c55007\tmp\full.sh` equivalent: `kc.sh video 0 194.1 full/kc-full-1080p`, about 30 min, with RAM free) and watch it at speed (motion was judged from stills by the agents).
2. The load-set audit for every scene; the Layer2D-after-seek audit; SwiftShader vs Vulkan per module.
3. Drums/bass/other envelopes (a Demucs split on an idle machine).
4. Transitions between plates beyond hard cuts, where the bible names carried moves.
5. The 4K master (`--scale 2`), colour tags, publish package (AI disclosure, "MiniMax-Music3" credit, MIT notice), and refreshing the LGTM view count on render day.
