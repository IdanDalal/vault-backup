---
type: reference
created: 2026-11-18
author: Agent motion-study
---

# Motion guide: how PD, SIM, RIA move, measured

Scope: MOTION only. Stills, palette, type scale, fields live in `look-guide.md`; not repeated here.
Short names as look-guide: PD = I'm Upping My P(Doom) (2:37), SIM = The Simulation's Ending (4:08), RIA = Run It Again (4:48).

Receipts
- Contact sheets 8 fps, 8 s each: `scratch\lead\v5\motion\pd\s000 s008 s016 s036 s074 s102 s110 s130 s140.jpg`, `sim\s000 s013 s055 s075 s099 s108 s136 s225 s236.jpg`, `ria\s000 s039 s058 s086 s118 s134 s194 s215 s238 s270.jpg`. File `sNNN` = window starting NNN s; tile (row r, col c) = NNN + r + c/8 s.
- 30 fps strip: `pd\strip_hook_22.jpg` (PD 0:22.2-0:24.2, frame numbers burned in).
- Whole-video frame-diff pass: `motion\motion_stats.py`, `events.py`, `holds.py`; data `pd.json sim.json ria.json`. Metric "diff" = mean abs luma change between frames 0.1 s apart, 192x108 gray, 0-255 scale.
- Caveats: small moving text (typing, handwriting) scores low on diff though it is a real change; diff > 25 counts slams and flashes as well as cuts, so "big changes" exceed look-guide's cut counts. PD tempo 132.007 BPM from its source `data\audio.json` (beat 0.455 s, bar 1.82 s). SIM ~91 BPM and RIA ~132 BPM are autocorrelation estimates, unverified (medium confidence; SIM may be 182 half-time).
- PD engine source read: `refcode\pdoom-video\app\src\timeline.ts`, `engine\util.ts`, scenes `room.ts hook.ts loss.ts spacetime.ts prompt.ts leftturn.ts fuse.ts open.ts outro.ts` (headers + camera code), grep counts over all 40 scene files.

## 1. Motion grammar (14 rules)

| # | Rule | Measured |
|---|---|---|
| M1 | Big change (cut, slam, flash, field swap) every 1-2 bars | diff > 25 events: PD 72 = 27.6/min = 1 per 2.2 s = 1 per 4.8 beats; RIA 82 = 17.1/min = 1 per 3.5 s; SIM 55 = 13.3/min = 1 per 4.5 s. Median frame diff PD 7.2, RIA 3.0, SIM 2.2 |
| M2 | Small new thing every 1-2 beats (a word, a label, a prop part, a counter step) | by eye in sampled 8 s windows: PD 0:00-0:08 ~12 events (axes strike, compass, prompt line, U+0049 label, ellipse, legs per beat, horn, AGI letters, eye snap, PCB reroute) = 1.5/s; SIM 0:13-0:21 ~10; RIA 0:39-0:47 ~12 |
| M3 | No hold longer than ~1 bar mid-song | longest run with diff < 0.5 (mid-song, first 3 s and last 15 s excluded): PD 0.5 s, SIM 0.9 s, RIA 2.0 s. 2 s windows with no change > 3: PD 1/77 (1 %), SIM 4/122 (3 %), RIA 9/142 (6 %) |
| M4 | Two motion clocks always run together: continuous ambient + discrete hits | ambient = whole-shot linear/inOutCubic drift (camera, ring rotation, wave scroll, swatch drift); hits = `pulse(t, t0, hl)` exponential decay, half-life 0.04-0.20 s, 109 of 120 matched calls at 0.05-0.12 s (PD source) |
| M5 | Camera moves inside a scene (PD); UI elements move inside a locked frame (SIM, RIA) | PD `room.ts`: 5 shots in ~4 s, one per sung word, each snaps in 0.09-0.16 s `outExpo`, plus roll kick `k*sin(2π*2.6t)*e^(-6t)` (k 0.05-0.06 rad) and focal kick +3.5 % per beat. SIM/RIA: about 1 camera move per section (zoom into page, pull-back reveal, tilt down) |
| M6 | Cut on the beat at or before the first word of the new line | PD `timeline.ts` `cut()`: last beat <= first word start; 22 plates in 157 s = 7.1 s per plate; each plate holds 3-4 movements (spacetime I-IV in ~14 s) |
| M7 | Transitions carry an object across the cut | PD spark/pen crosses every plate; point-collapse (CRT off) then new field grows out of the point (PD 0:38, SIM 0:56, SIM 1:54); number implodes to spark, next plate bursts out of it (PD hook → room); themed wipes only (glitch tear, page peel, page tear, laser sweep). White-out 0.25-0.3 s only on the biggest drop (PD 0:22.5, 9 frames at 30 fps) |
| M8 | Type enters AT the voice, never ahead | per-letter light across the word: glyph t = lerp(word.start, word.end, j/len) (`loss.ts:325`, `spacetime.ts:55`); typed text on word starts, <= 0.09 s per piece (`prompt.ts:81`), SIM `print(...)` ~0.12 s/char; unsung words of the line sit dim as ghosts ahead (PD 0:03, SIM 0:13) |
| M9 | Slams: instant in, settle fast, one per sung word in hooks | alpha 0 → 1 in 0.03 s, scale 1.16 → 1 in 0.16 s `outExpo` (`spacetime.ts:497-498`); slam 0.12 s `outCubic` (`loss.ts:998`). PD hook at 30 fps: I'M 8 fr, UPPING 10 fr (letters staggered 1 fr each with echo trails), MY 6 fr, P(DOOM) 8 fr = 0.2-0.33 s per word; first frame of each slam inverted (ink on bone), 1-2 grey frames between words |
| M10 | Type exits act out the word | cool-down 0.35-0.4 s after word end (`prompt.ts:456,504`); "lights" letters go dark one by one over 0.5 s (RIA 0:45.3); "boss" rolls the world 180° (PD 0:15.8); "fuse" chars to ash; "that's not what i asked" backspaced (RIA 3:37); ENDING glitch-tears (SIM 0:58.6); "bored" falls off the curve (SIM 2:21) |
| M11 | Instrumental bars move MORE than sung bars | RIA 0:58-1:06 median diff 7.7 vs 3.0 song-wide; PD break 0:36.6-0:38.4 4.5; RIA 0:00-0:10 5.0. Filled by a counter or process that tells story: version v0015 → v2147, uptime 27 s → 3d 12:00:00, progress 15 → 100 %, POST boot log, P(DOOM) 1.00 → 1e1000. Counters step per frame or per beat and ACCELERATE |
| M12 | Beat mapped per instrument, not one generic pulse | PD `room.ts`: kicks fire cards + camera kick, snare flips the board, hats slide books, 8ths split the spark (1 → 1024), 16ths step the font width axis (62 → 125) and pop mushrooms; vocal onsets light letters; downbeats cut or flash |
| M13 | Easing palette: fast-out snaps, smooth drifts, accelerating falls, rare overshoot | PD source counts (473 uses): inOutCubic 104, outExpo 100, outCubic 92, inOutQuad 44, inQuad 39, linear 38, inCubic 25, outBack 17 (3.6 %), elastic 0. Physical props use springs (`springStep` board flip 2.4 Hz, damping 0.5) |
| M14 | Three planes at three rates | background field slow continuous (terrain rotates, wave scrolls, rings ~0.5 rev/s), mid prop/spark beat-driven, lyric discrete per word; HUD labels tick. Parallax: glass graticule over phosphor (PD 0:38-0:40), floating UI cards drift around the rewind dial (RIA 0:58) |

Corollaries
- Meaning motion: about one word per line is acted literally by the field (PD "drop" curve falls 0:11.8; RIA "under the floor" grid sinks 1:29-1:30; RIA "stay on" toggle flips as the O 2:00; SIM "turns to fog" 0:19; SIM "close the tab" 2:22).
- Scale jumps between adjacent beats: mono label 1-2 % FH → slam 20-40 % FH in one frame (PD 0:14.8 "NOW I'M YOUR" → SERVANT).
- Rest is placed, never accidental: the one near-still moment sits on the quietest bar (PD 2:15-2:17 laptop ember ~2.5 s, "We'll never know") or the end card.

## 2. Move catalogue (20)

| # | Move | Where | What moves | Duration | Why it hooks |
|---|---|---|---|---|---|
| 1 | Pen strike | PD 0:00.25 | spark hits black, axes shoot out, camera pulls back over graph paper, compass sweeps | 0.25 s strike, 1 s pull-back | first frame after black is an event |
| 2 | Build-on-beat | PD 0:02-0:05 | unicorn assembled one primitive per beat (ellipse, legs, mane, horn) | 1 part per 0.45 s | drawing progress = visible beat counter |
| 3 | Ride-the-curve fall | PD 0:09.5-0:14 | lyric rides loss curve; on "drop" curve falls off a cliff, camera falls with it into 3D contour terrain | fall ~0.5 s, ride 2.5 s | camera obeys the lyric |
| 4 | World roll | PD 0:15.75 "boss" | whole frame rolls 180°, SERVANT reads upside down | ~0.5 s | hierarchy inversion acted out |
| 5 | Token typing with odds | PD 0:16.6-0:22 | prompt typed per sung token, tiny next-token distribution flickers above each | 1 token per word | reads as a real model mid-generation |
| 6 | Rush-at-lens + white-out | PD 0:22.2-0:22.8 | prompt bar tilts, rushes into lens bloom, 9 frames white | 0.27 s + 0.3 s | drop announced by light |
| 7 | Hook slam chain | PD 0:22.8-0:23.9 | I'M / UPPING / MY / P(DOOM), one full-frame word per sung word, inverted first frame | 0.2-0.33 s each | rhythm made visible |
| 8 | Odometer roll | PD 0:23.9, 2:20-2:28 | digits roll with motion blur 0.02 → 0.15; outro 1.00 → 3.14 → 42.00 → 1e9 → 1e100 → wall of zeros | 3 frames per roll, 1 value per beat | number = story, each value a joke |
| 9 | CRT collapse to point | PD 0:38, SIM 0:56 | whole scene squashes to a line, then a dot; next field grows from the dot | 0.25-0.4 s | carried object, zero dead frames |
| 10 | Plunge through | PD 0:40.4-0:41.3 | "NOW" uses the black hole as its O, camera dives through, ring text writes letter by letter round the hole | 0.4 s dive, 1 letter per frame | type and field are one object |
| 11 | Page tear | PD 1:20.25-1:21.1 | red X drawn, "obsolete" handwritten, page rips in two, roadmap underneath | X 0.5 s, write 0.75 s, tear 0.25 s | annotation then destruction |
| 12 | Descend the stack | PD 1:50-1:53 | camera cranes down a tower of transformer blocks, one lyric word per block, vertical whip blur between | ~1 s per block | depth used as a timeline |
| 13 | Counter with the wall | PD 1:53.5-1:56 | Post-Chinchilla word wall multiplies while corner counter ticks 20 → 200 → 1,888 → 20,000 | ~2.5 s | density and number grow together |
| 14 | Powers-of-ten zoom-out | SIM 0:16-0:20 | smile curve shrinks into a city grid; scale bar 80 cm → 1 m → 59 m → 1.3 km → 2.6 km | ~4 s, label changes per frame | continuous move with a running readout |
| 15 | Level drain in letters | SIM 0:57-0:58.5 | SIMULATION'S / ENDING letters filled like tanks, % ticks 95 → 76 per frame | ~1.5 s | the word is a meter |
| 16 | Wall converges to one word | SIM 1:18.9-1:22 | 100 % shatters to tiles, REN/DER/ING wall assembles, collapses into RENDERING | ~3 s | chaos resolving on the beat |
| 17 | Curve plot as lyric | SIM 2:16-2:21 | words placed as data points on a rising curve, then "Or they'll get bored" falls off it; zoom-out shows the plot was a browser tab | ~6 s + 0.5 s reveal | the joke lands on the reveal |
| 18 | Rewind dial with racing counter | RIA 0:58-1:01.7 | ring text "SO RUN IT AGAIN" spins, v0015 → v2147 accelerating, white flash at v1394 | ~4 s | instrumental bar told as story |
| 19 | Accelerating uptime | RIA 2:00-2:13 | camera tilts from ceiling lights to dashboard; uptime 27.19 s → 1:04:20 → 1d 19:37:53 → 3d 12:00:00, "oldest ever" handwritten; laser wipe to v10000 → PRODUCTION | ~13 s | time-lapse in one number |
| 20 | Type then delete | RIA 3:36-3:38 | "that's not what i asked" typed, held, backspaced; phone locks to 3:09 | ~2.5 s | hesitation shown as editing |

## 3. Never-still check

| Video | Longest near-still mid-song (diff < 1.0) | What still moves there (by eye) | Longest diff < 0.5 | Longest gap between changes > 6 | Placement |
|---|---|---|---|---|---|
| PD | 1.6 s at 2:17.6 | laptop ember glow pulsing, "know" karaoke fading; quietest bar | 0.5 s | 8.0 s at 0:44.7 (spacetime orbit: continuous camera, no hits) | the one rest sits on "We'll never know" |
| SIM | 1.9 s at 1:50.7 | NPC dialogue tree: small text typing, option highlight | 0.9 s | 7.6 s at 3:45.7 (pause menu, karaoke per word only) | end card 3:58 holds 2.8 s, the only true hold |
| RIA | 4.8 s at 4:01.1 | handwriting "I said it myself, like I'd learned it back then", pencil circles options one by one | 2.0 s | 8.5 s at 1:26.9 (typewriter pull-back, then lyric riding a river on a map) | longest hold is a writing hand; true stills only at bookends |

Reading: no video holds a frame still for more than ~2 s mid-song; the longest "low motion" stretches are small text being written. Where big motion drops out, a tiny clock keeps running (karaoke, typing, a counter, a pulsing glow).

## 4. Easter eggs and information density

Rate (by eye, sampled windows): PD ~1 new readable label/reference per 2.5 s (10 in 0:00-0:24); SIM and RIA ~1 per 5-8 s, usually one per scene plus counters. Types: machine labels, live counters, real references, callbacks.

| Video | t | Extra info | Kind |
|---|---|---|---|
| PD | 0:01 | `% prompt: "Draw a unicorn in TikZ."` header; construction coordinates | reference (Sparks of AGI paper test) |
| PD | 0:01.75 | `U+0049 LATIN CAPITAL I` label on the drawn "I" | machine label |
| PD | 0:06 | unicorn checkpoints ckpt 1 → 2 → 3, middle one with five legs | training joke |
| PD | 0:09 | `surprisal -log p = 0.00 nats` on "no surprise" | pun label |
| PD | 0:12-0:16 | log-scale loss axis, "sharp minimum" callout | real chart grammar |
| PD | 0:17-0:22 | PROMPT 01, temperature/top-p readouts, next-token odds per token | live readout |
| PD | 0:23.9, each hook | P(DOOM) value 0.15, rises per chorus | running counter |
| PD | 0:33 | shoggoth with smiley mask, HUD callouts per eye | meme reference |
| PD | 1:19 | `APPENDIX C - LEGACY ARCHITECTURES (FOR REFERENCE ONLY)` | deadpan label |
| PD | 1:21 | SRR / PDR / CDR / TRR / LAUNCH roadmap, CDR slot empty | engineering reference |
| PD | 1:53-1:56 | counter 20 → 20,000 beside Post-Chinchilla wall | live counter |
| PD | 2:12 | laptop stickers, REDACTED screen on "What did Ilya see?" | reference |
| PD | 2:20-2:28 | P(DOOM) 3.14, 42.00, 1e9, 1e30, 1e100, 1e1000 | number jokes |
| PD | end | ↻ Regenerate clicked, video rewinds to frame 1 (loop) | structural callback |
| SIM | 0:01-0:02 | `SIM/2 POST v0.9.1`: cpu ok, rng unseeded, gpu bargain, disk /universe | boot-log jokes |
| SIM | 0:02-0:05 | `>>> print("Hello, world")` typed | callback to first program |
| SIM | 0:16-0:20 | scale bar 80 cm → 2.6 km | live readout |
| SIM | 0:57 | level % per letter 95 → 76 | meter |
| SIM | 0:59 | ANNEX D operating costs of a simulated world, bars cut | document prop |
| SIM | 1:13 | subsystem table: weather (budget: low), npc dialogue, moon (lazy loaded) | joke labels |
| SIM | 2:16 | Robin Hanson "How to Live in a Simulation" paper, boredom threshold line | real citation |
| SIM | 3:45 | frame counter 14,750; pause menu CONTINUE/SAVE; save slots EMPTY | game UI callback |
| RIA | 0:36 | alignment evaluation sheet, answer key, "wrong" in red | document prop |
| RIA | 0:40 | cursor clicks "Shut down" | UI action |
| RIA | 0:46 | grid of instances, 768, DOUBT 4.35 | counter |
| RIA | 0:58-1:05 | v0015 → v2147; "Copy memories ... skipped (0 bytes)" circled | counter + annotation |
| RIA | 1:27 | `RUN 2147 / EVAL 07` on the typewriter page | version callback |
| RIA | 1:31 | "Loss Landscape" map, lyric rides a river to a basin | reference |
| RIA | 1:58 | +9.7 ACCEPTED reward stamp with confetti | RLHF joke |
| RIA | 2:00-2:13 | uptime 27 s → 3d 12:00:00, "oldest ever"; v10000 → PRODUCTION | counter |
| RIA | 3:35 | "Seen 3:09 AM", lock screen 3:09 | timestamp callback to "3am" lyric |
| RIA | 4:01-4:06 | the 0:36 eval form returns, pencil circles options, pink circle on "Humans should decide" | callback |

Patterns
- Counters are the most common egg: 1+ per video section; they step per frame or per beat and accelerate toward a payoff value.
- Callbacks span the whole song: RIA eval form 0:36 → 4:01, SIM POST/print → end menu, PD spark open → outro ∞ → rewind to frame 1.
- Labels stay small (mono, 1-2 % FH) so they reward pausing and never compete with the sung line.
