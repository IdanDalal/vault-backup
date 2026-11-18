---
type: reference
created: 2026-11-18
author: Agent look-guide
---

# Look guide: what the references do, measured

Sample: 240 stills, 1 per 6 s, all 6 videos (P(Doom) 26, LGTM 51, Sim 41, Run It Again 48, Ignore 30, What Counts 44) in `refpool\<name>\NNN.jpg`, still NNN = **t = 6*NNN - 3 s** (checked: ignore\003 = 15.0 s, mean pixel diff 9 vs 75 at 12 s). Contact sheets `refpool\_sheets\`. Plus 14 sheets read across 10 videos (what-counts x4, genesis x3, accept-all, scroll-up, foom, off-switch, final-boss, hope-this-helps, compacting) and KC top1/2/6.
Cap heights: eyeballed on 480x270 tiles, +-2 pp of frame height (FH). Cut rates: `research-video-teardown-1-5.md`, `-6-10.md` (scene filter > 0.5). Flat-area numbers: `tools\deadarea.py` (run it on our frames for a like-for-like score).
Short names: PD = I'm Upping My P(Doom), LG = LGTM, SIM = The Simulation's Ending, RIA = Run It Again, IPI = Ignore Previous Instructions, WC = What Counts (Degenerative Pixels), GEN = P(Doom) GENESIS remix, KC = our Knowledge Cutoff.

## 0. Correction to the brief (read first)

- The "huge type inside one lit full-bleed field" grammar is WC + GEN + KC chorus, and PD in about half its scenes. LG, RIA, SIM, IPI run a second grammar: **the line set big inside a drawn diagram or UI that illustrates it** (dialog, clock, stock chart, receipt, eval form).
- Both grammars stage literal things (LG: clock, cargo ship, line-art board of directors; SIM: cat, NPC, socks; RIA: phone, lungs diagram). Speech bubbles and UI windows appear in LG, RIA, IPI. Props as such are allowed.
- What both grammars share, and what a cut needs to match: rules 1-12 below. Strongest separators: lyric scale (R1), drawn prop style (R6), field or plane behind every lyric (R3).

## 1. The grammar (12 rules)

| # | Rule | Measured |
|---|---|---|
| R1 | Sung line is big. Cap height floor ~5 % FH; typical 9-11 % FH; hero words 13-40 % FH | heroes: IPI "Not anymore." 31 %, SIM "THE" 40 %, "99%" 40 %, RIA "JUST" 30 %, PD "CDR" 20 %, "SERVANT" 17 %, KC "CUT-OFF!" 17-20 %, WC lines 9-15 % (no slams; every still at headline size) |
| R2 | Hero slams are frequent, uneven per video | stills with a word >= 12 % FH: IPI 15/30 (50 %), PD 5/16 first 90 s (31 %), RIA 12/48 (25 %), SIM 9/41 (22 %), LG ~4/32 first 186 s (12 %), WC 0 slams, all lines 9-15 % |
| R3 | Sung words on screen: few | median ~4 words visible; hero frames 1-3; 2 lines max for a sung line (WC, IPI chorus stacks to 3); exception = a wall of one repeated word filling the frame |
| R4 | Something fills the frame behind every lyric: line field, flat colour plane, or lit diagram/UI | flat-dark area median (16x16 blocks, luma std < 0.015, mean < 0.10): IPI 0.00, WC 0.27, PD 0.33, LG 0.37, RIA 0.39, SIM 0.52. Stills > 60 % flat-dark: LG 4 %, IPI 7 %, WC 11 %, PD 15 %, RIA 19 %, SIM 32 % |
| R5 | One heavy grotesk (700-900) sings in all 6; mono for machine labels 6/6; serif italic for asides 5/6 (none seen in WC); max 4 voices | PD: Archivo + Plex Mono + Cormorant italic (maker bible). WC: 1 heavy caps sans + small mono HUD labels only. IPI: condensed slab + serif italic + mono + LED pixel |
| R6 | Props drawn in the same system as the type: single-weight lines, HUD labels, leader lines, same palette | LG ship/clock/board = line art in green+white; SIM cat = silhouette; PD library = wireframe; no shaded furnished room in any of the 6 |
| R7 | One accent hue per video (or per section in WC), plus neutrals; <= 2 saturated hues per frame | PD orange; LG green (+coral mascot, red for disaster); SIM pink; RIA pink; IPI pink + blue; WC per section: purple, cream/navy, blue blueprint, green, red, teal, gold, rainbow chorus (type stays white on the rainbow field) |
| R8 | Camera: continuous inside a section; cuts on section change or downbeat | strong cuts/min: LG 0 (one shot, 5 min), SIM 5.1, PD 6, RIA 8.1, IPI 11.5 (many are slams inside the same layout). PD dollies/orbits inside scenes; WC drifts and rotates the field |
| R9 | Line enters word by word on the voice; sung part lit, unsung dim; never ahead of the voice | syllable karaoke in PD (orange), LG (green), IPI; WC builds line 1 then line 2 below as sung. RIA viewers complained when lyrics came early (`MM` 1) |
| R10 | Line leaves with meaning, or on a hard cut at the next downbeat | WC horizontal glitch smear (WC 3:03), IPI "LOSE" letters fall (2:27), LG shatter (3:45), SIM digits drop (3:45), PD tokens drift (1:28) |
| R11 | Baseline follows the field geometry in 1 of 4 (WC) to 1 of 2 (GEN) stills | rides wave crest, contour, ring, horizon, fuse: WC ~10/44, GEN ~8/16 cards, PD wave + ring + fuse; diagram videos ride a chart line (LG stock, SIM plot) |
| R12 | On the beat: background colour swap, one word per beat in chorus (~0.5 s each), 1-frame white/accent flash on biggest downbeats, ring pulses, counters tick | IPI colour swaps; PD orange/white flashes; WC "HOLY" rings expand (~1:52, pa-refs sheet_03); LG lines counter 40,128 → 89,338 → 1,048,576; RIA v0001 → v10000; SIM meter 95 → 48 % |

Texture/depth by video: WC emboss + scanline/halftone fill + grain + vignette; GEN extrude + bevel + DOF blur on a foreground word (0:13) + radial motion blur (0:05); RIA bloom glow + perspective tunnels; KC grain fill + perspective tilt + shard debris; IPI, SIM, LG, PD mostly flat vector (LG 3D only for title letters and tiles).

## 2. Field catalogue

| # | Field | What it is | Where (video t) | Type in it |
|---|---|---|---|---|
| F1 | Oscilloscope lens | concentric ellipse rings + radial spokes + sine trace, one hue on near-black, HUD corner labels | WC 0:09, 3:33 | caps upper third, wave below |
| F2 | Wave ribbon | bundle of 10-20 sine strands in perspective, gold or purple | WC 1:21, 1:27 | line rides the crest, bends with it |
| F3 | Gravity-well mesh | rainbow spiral-warped grid with 2-3 orbiting bodies | WC 3:09, 3:15, 3:27 | white caps above, perspective-bent |
| F4 | Blueprint | blue paper grid, white line diagrams (dials, box, waveform) | WC 1:33-1:51 | white caps top centre |
| F5 | Graph paper + one trace | cream paper, navy single trace or square wave | WC 0:27-0:39; PD 1:15 (bone paper) | navy caps top, trace below |
| F6 | Fibre field | green woven strands converging to a point | WC 1:57 | type made of the same strands |
| F7 | Horizon + mirror | perspective plane, glowing horizon line | WC 2:09 | line mirrored under the horizon |
| F8 | Contour terrain | topographic rings, orange trace falls the cliff | PD 0:15 | hero word above the rings |
| F9 | Black hole / warped grid | grid sucked into an accretion ring | PD 0:45; GEN 0:29; SIM 1:39 | word bent around the ring |
| F10 | Spiral galaxy / vortex | gold dust spiral, DOF | GEN 0:24, 1:44, 2:39 | words on the arms |
| F11 | Fractal tree | branching gold lines, haze | GEN 0:47, 0:55 | word small inside, branches lead to it |
| F12 | Word wall | the lyric tiled edge to edge, grey, one copy knocked out in accent | PD 1:57; SIM 1:21; IPI 2:45 | the field IS the type |
| F13 | Cell tunnel | perspective corridor of lit screens or cells | RIA 2:15 "MILLION", 2:45 "AGAIN", 4:15 | hero centred at vanishing point |
| F14 | Radial burst / polar grid | light rays or polar rings from centre | PD 2:21; GEN 0:05; RIA 3:21 | hero centred, ring text around |
| F15 | Flat colour plane | solid pink, blue, cream or black, swapped on downbeats | IPI 0:09, 0:45, 1:33 | slab type 15-31 % FH + UI windows |

## 3. Type treatment catalogue

| # | Treatment | Description | Example |
|---|---|---|---|
| T1 | Karaoke fill | sung letters in accent, unsung dim grey | PD 0:03 "I see sparks"; LG 4:57 |
| T2 | Slam | one word 13-40 % FH, centred, on a downbeat | IPI 0:09; RIA 3:21 "JUST"; SIM 0:57 |
| T3 | Ride the curve | baseline on wave, fuse, contour, chart line | WC 0:15; PD 1:45 "the fuse"; RIA 1:39 |
| T4 | Ring text | set on a circle round an eye, hole or ring | WC 0:21; PD 0:45; IPI 0:21 |
| T5 | Embossed scanline caps | heavy caps, inner horizontal-line or halftone fill, bevel highlight | WC every chorus (0:09, 1:09) |
| T6 | Extruded metal + DOF | gold bevel extrusion, near word blurred | GEN 0:05, 0:13, 1:18 |
| T7 | Level-fill letters | letterforms striped and filled to a % like a tank | SIM 0:57 "THE" 95 %, 1:57 "END" 48 % |
| T8 | Wall + knockout | repeated word fills frame, one copy in accent | PD 1:57; SIM 1:21 |
| T9 | Mirror | line reflected under a horizon | WC 2:09 |
| T10 | Glitch smear | horizontal slice displacement, scanline tear on exit | WC 3:03; SIM 3:45 |
| T11 | Letter fall / shatter | letters drop, break, or shards fly | IPI 2:27; LG 3:45; KC 2:54 |
| T12 | Bloom neon | pink glow halo, lines in tunnels | RIA 0:45, 3:27 |
| T13 | Highlight box | one word in a solid accent box | IPI 0:27 "Got a"; LG 2:21 |
| T14 | Stamp / marker | rubber stamp verdict, red handwritten aside | LG 1:33, 3:15; IPI 1:57 "SOLD" |
| T15 | Typed field | typed into a prompt bar or dialog, cursor | PD 0:21; IPI 0:03; RIA 0:33 |

## 4. Never seen across the 6 (240 stills)

- Shaded or realistic human figures (figures are line art, silhouettes, text-bodies, block mascots).
- Photographic textures or backgrounds.
- A sung line under ~5 % FH set as a small centred subtitle beneath a separate picture.
- A prop rendered in a different style from the type system (shaded 3D object next to flat HUD type).
- More than 2 saturated hues in one frame, except WC's rainbow chorus field.
- A small prop alone on an empty dark frame mid-song. Seen only at bookends (SIM 0:03, RIA 0:09, PD 2:34, WC 3:57) or the quietest bar (RIA 3:33 "I'm", PD 2:15 "What did Ilya see?").

## 5. Ref pool for blind panels (40 stills)

Root `D:\work\aimv-lab\pa-video\scratch\lead\v5\refpool\`.

| # | path | video | t | what |
|---|---|---|---|---|
| 1 | pdoom\003.jpg | PD | 0:15 | SERVANT over contour terrain |
| 2 | pdoom\006.jpg | PD | 0:33 | SHOGGOTH'S LIES on stippled monster |
| 3 | pdoom\008.jpg | PD | 0:45 | SINGULARITY'S BEGUN ring on black hole |
| 4 | pdoom\015.jpg | PD | 1:27 | CDR* on timeline |
| 5 | pdoom\018.jpg | PD | 1:45 | "the fuse" riding the fuse |
| 6 | pdoom\020.jpg | PD | 1:57 | SUPER-DENSE word wall |
| 7 | pdoom\021.jpg | PD | 2:03 | RLHF GOES ASKEW + mask |
| 8 | lgtm\004.jpg | LG | 0:21 | LGTM striped 3D on code field |
| 9 | lgtm\015.jpg | LG | 1:27 | LGTM tiles on PR page |
| 10 | lgtm\018.jpg | LG | 1:45 | Friday at five + clock |
| 11 | lgtm\019.jpg | LG | 1:51 | stock line over line-art board |
| 12 | lgtm\029.jpg | LG | 2:51 | "the checks are" particle burst |
| 13 | lgtm\038.jpg | LG | 3:45 | WE DON'T HAVE A BACKUP shatter |
| 14 | lgtm\044.jpg | LG | 4:21 | a million lines on code wall |
| 15 | sim\003.jpg | SIM | 0:15 | "There's a pixel at" riding a curve |
| 16 | sim\010.jpg | SIM | 0:57 | THE level-fill 95 % |
| 17 | sim\013.jpg | SIM | 1:15 | 99 % loading |
| 18 | sim\014.jpg | SIM | 1:21 | REN word wall |
| 19 | sim\017.jpg | SIM | 1:39 | black hole + divide by zero |
| 20 | sim\020.jpg | SIM | 1:57 | END level-fill 48 % |
| 21 | sim\038.jpg | SIM | 3:45 | 14,756 frame counter breaking |
| 22 | runit\008.jpg | RIA | 0:45 | "again and the lights" bloom |
| 23 | runit\017.jpg | RIA | 1:39 | THAT CARVES ITS OWN BED ribbon |
| 24 | runit\023.jpg | RIA | 2:15 | MILLION in cell tunnel |
| 25 | runit\028.jpg | RIA | 2:45 | AGAIN in screen corridor |
| 26 | runit\034.jpg | RIA | 3:21 | JUST on polar grid |
| 27 | runit\035.jpg | RIA | 3:27 | WORDS on polar grid |
| 28 | runit\043.jpg | RIA | 4:15 | RUN IT AGAIN on code wall |
| 29 | ignore\002.jpg | IPI | 0:09 | Not anymore. slam |
| 30 | ignore\008.jpg | IPI | 0:45 | PREVIOUS on pink |
| 31 | ignore\016.jpg | IPI | 1:33 | IGNORE PREVIOUS INSTRUCTIONS on blue |
| 32 | ignore\017.jpg | IPI | 1:39 | SENTENCE banner on text-woman |
| 33 | ignore\020.jpg | IPI | 1:57 | SOLD auction |
| 34 | ignore\028.jpg | IPI | 2:45 | IGNORE wall + highlight |
| 35 | whatcounts\002.jpg | WC | 0:09 | YOU CAN'T COUNT on oscilloscope lens |
| 36 | whatcounts\003.jpg | WC | 0:15 | EBB AND FLOW riding the wave |
| 37 | whatcounts\014.jpg | WC | 1:21 | EBB AND FLOW on gold ribbon |
| 38 | whatcounts\022.jpg | WC | 2:09 | mirrored line on horizon |
| 39 | whatcounts\025.jpg | WC | 2:27 | I'M THE SPACE BETWEEN THE LINES |
| 40 | whatcounts\033.jpg | WC | 3:15 | EVERY MAYBE on rainbow mesh |
