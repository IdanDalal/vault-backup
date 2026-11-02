---
type: project
created: 2026-11-02
author: jep
---

# kc-engine components (reuse catalogue)

Engine: `D:\work\aimv-lab\kc-engine` (fork of P(Doom) video engine, MIT, Giacomo Magnanini; upstream clone `D:\work\aimv-lab\refcode\pdoom-video`, origin github.com/mexicat/pdoom-video). Stack: Bun 1.4.3 + TypeScript + three.js 0.186 + opentype.js 2 + Vite 8 + playwright-core driving headless Edge, frames to ffmpeg/libx264. 166 commits, last `9be094d` (render-4k.sh, 2026-10-31). Paths below are relative to the engine root. Line numbers read 2026-11-02.

Legend: REUSE = drop-in for any song; ADAPT = reusable after removing KC constants; KC = Knowledge Cutoff content, copy the pattern only.

## (a) Engine core

| capability | what it does | pointer |
|---|---|---|
| render modes | `stills`, `sheet` (contact sheet, `--cuts` = 4 frames around every boundary), `plates`, `perf`, `video`, `gpu` | `app/scripts/render.ts:1-13`, dispatch `:289-364` |
| browser driver | headless Edge (hardcoded `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`), ANGLE backend from `KC_ANGLE` env (default vulkan; d3d11, swiftshader for reference), GPU blocklist off, background throttling off | `app/scripts/render.ts:51-57` |
| boot guards | waits for `__pdoom.ready`, re-waits after Vite dep re-optimisation reload, refuses when no timeline entry loaded, checks canvas size vs `--scale`, prints `RENDERER` (ANGLE can fall back to SwiftShader silently), prints scene errors | `app/scripts/render.ts:64-77` |
| private dev server | own Vite on a verified-free port, no HMR, kills the whole process tree (fix after 543 orphaned servers, ~100 GB) | `app/scripts/server.ts:1-39` |
| export API in page | `window.__pdoom`: `still(t, samples, shutter)`, `png()` full-res base64, `stream({from,to,fps,ws,samples,shutter,inflight})`, `timeline`, `duration`, `width/height/scale` | `app/src/main.ts:90-147` |
| frame streaming | rgb24 frames over a WebSocket written from a Worker, 2 pooled buffers, `inflight` 4 unacknowledged frames (backpressure), pipelined readback (frame n collected while n+1 renders), warm-up frame before a range | `app/src/main.ts:38-88`, `:124-144` |
| workers | `--workers N` (default 2) headless browsers take `--chunk` (default 8) frame chunks from a shared cursor; server reorders into one ffmpeg, so output equals a 1-worker run | `app/scripts/render.ts:118-126`, `:144-146`, `:243-266` |
| memory cap + disk spool | reorder buffer acknowledged under `--mem-gb` (default 1); overflow spooled to `%TEMP%/pdoom-spool-<pid>` up to `--spool-gb` (default 20); spool removed on exit/SIGINT | `app/scripts/render.ts:147-164`, `:188-222` |
| failure handling | any page/ffmpeg failure closes all sockets; killed ffmpeg leaves an unplayable file (no finished-looking truncated mp4) | `app/scripts/render.ts:173-184`, `:277-284` |
| adaptive motion blur | `--samples auto [--min-samples 4] [--max-samples 324] [--tol 3] [--refine tiles|frame]`; sub-frame sets 4, 12, 36, 108, 324 (ternary nesting keeps every prefix evenly spread and centred); stops when estimated error < `tol` 8-bit levels (worst 2x2 logical px block); still frame stops at 12 | parse `app/scripts/render.ts:30-34`; offsets `app/src/engine/engine.ts:39-51`; loop `:365-522` |
| per-tile refinement | 32x32 logical px tiles; a tile continues while it or a neighbour is >= tol; converged tiles masked out via depth-buffer early-Z; per-tile gain texture for the final average; scenes declare extra targets in `Scene.tileMasked` | `app/src/engine/engine.ts:86-111`, `:231-311`, `:461-504`; `app/src/engine/scene.ts:73-81` |
| sampling error estimate | display-space difference (shoulder + sRGB) between old and new sub-frame sets, max per 16x16 block group, read back | `app/src/engine/engine.ts:144-175`, `:524-544` |
| NaN guard | accumulation drops non-finite sub-frame pixels (a stray NaN would bloom into a disc) | `app/src/engine/engine.ts:132-143` |
| fixed samples | `--samples N` evenly spread over `--shutter` x 1/fps; required for stateful scenes (adaptive throws on a stateful scene) | `app/src/engine/engine.ts:393-397`, `:439-441` |
| per-entry sample cap | `TimelineEntry.maxSamples` caps adaptive sub-frames for slow-converging noise | `app/src/engine/engine.ts:25-26`, `:398` |
| supersample tap rotation | `SS_TAP` shares 4 shader taps across sub-frames | `app/src/engine/gl.ts:23-31`, `app/src/engine/engine.ts:400-410` |
| post read point | post params (shake, flash, zoom, fades) read at shutter offset 1/8 after t | `app/src/engine/engine.ts:403-406`, `:434-435` |
| --scale | `?scale=N` read once; scenes lay out in logical 1920x1080, engine renders at N x (`--scale 2` = 3840x2160); Canvas2D layers scaled by `scaleContext2D`; stills at scale > 1 saved from the pixel buffer | `app/src/engine/scale.ts:1-11`, `app/src/engine/gl.ts:9-13`, `:155`; `app/scripts/render.ts:12-13`, `:28-29`, `:88-90` |
| render targets | HalfFloat linear HDR RGBA with depth by default; `pxScale` per target | `app/src/engine/gl.ts:39-51` |
| GL plumbing | `FSPass` fullscreen shader, `Compositor` blend modes normal/add/screen/multiply/max/replace, `Layer2D` Canvas2D uploaded as sRGB texture, `clearRT` | `app/src/engine/gl.ts:74`, `:102-105`, `:182-217` |
| scene API | `Scene` with `stateful`, `prerollMax` (6 s), `handlesTransition`, `tileMasked`, `init/reset/render/dispose`; `Frame` carries t, lt, p, beat, bar, phases, audio sample, `under` texture, tin/tout | `app/src/engine/scene.ts:10-96`; frame built `app/src/engine/engine.ts:356-363` |
| stateful preroll | seek into a stateful scene: reset + re-simulate up to `prerollMax` at 1/60 | `app/src/engine/engine.ts:571-581` |
| compositing | active entries sorted by start; default crossfade over the overlap unless `handlesTransition`; red plate for a failed scene | `app/src/engine/engine.ts:546-615` |
| frame camera | scene returns `cam {x,y,zoom,rot}` in post overrides; engine warps that entry's picture per sub-frame and maps registered boxes (quads when rolled) | `app/src/engine/engine.ts:593-598`, `:617-656`; `app/src/engine/post.ts:50-53` |
| post chain | bloom + halation (7 mips), chromatic aberration, tone shoulder, grain (seedable `grainTime` for loop frames), vignette, fade, flash, shake, zoom, invert; `postLayers` hook for global layers (rhythm pulse) | `app/src/engine/post.ts:1-90`, `:142-189`; defaults `:58-79`; hook `:54-56` |
| colour handling | scenes render linear HDR; shoulder `SHOULDER_GLSL` (identity below 0.72); `toSRGB` + 1/255 dither in final pass; Canvas2D layers decoded sRGB to linear; palette hex to linear | `app/src/engine/post.ts:6-14`, `:169`, `:179`; `app/src/engine/glsl/common.ts:156`; `app/src/engine/gl.ts:182`; `app/src/engine/util.ts:166` |
| export colour tags | ffmpeg `vflip,scale=out_color_matrix=bt709,setparams=color_primaries=bt709:color_trc=bt709` (without it ffmpeg converts BT.601 while players decode HD as BT.709) | `app/scripts/render.ts:133-136` |
| encoder | libx264 `-preset slow -crf 16 -tune grain -x264-params aq-mode=3`, yuv420p, `+faststart`; AAC 320k; `apad=whole_dur` bounded to the segment so `-shortest` ends at the video end (silent tail) | `app/scripts/render.ts:128-141` |
| readback | `readPixelsAsync` via PBO + fence (~15 ms vs ~40 ms at 1080p, ~150 ms at 4K); rgb24 packing pass (a quarter fewer bytes); 2 slots | `app/src/engine/engine.ts:658-734` |
| audio analysis | `AudioData` from `data/audio.json`: beats, downbeats, `beatAt`, `timeOfBeat`, `barAt`, `section(t)`, envelopes `sample(t)` | `app/src/engine/audio.ts:27-155` |
| lyrics | `Lyrics` from `data/lyrics.json` (word start/end/sung), `get(text, nth)`, `norm` | `app/src/engine/lyrics.ts:4-121` |
| timeline edit | plan rows `[id, module, start, setups, plates, params, anchors]`; cuts anchored to lyric lines (`cut`, `wcut`, `after`); grid quantizer snaps changes to beats (downbeat within 0.6 beat), 2-frame pre-roll, word-safe bounds, `shutterSafe` keeps cuts out of the 0.1-frame half shutter; `CARRY` seconds per entry for carried transitions; missing module renders `placeholder` | `app/src/timeline.ts:25-199`; quantizer `:123-158`; carries `:101-121` |
| kit demo entries | `?only=kit-*` loads demo scenes on song windows instead of the edit | `app/src/timeline.ts:187-198` |
| fonts | Anybody width x weight static instances (8 x 4), JetBrains Mono 400/700, Newsreader optical 16/60 roman/italic, Caveat 500; `F.voice(width, weight)`; `layout`, `fitSize`, `textPath2D`, `textPoints` | `app/src/engine/type.ts:5-226` |
| single-stroke fonts | EMS + Hershey SVG fonts as polylines, optical pair kerning, `strokeText`, `drawStrokeText`, `writtenLength` (handwriting on a time curve) | `app/src/engine/stroke.ts:1-324` |
| GPU line batches | thousands of AA capsule segments in 2D or 3D (hatching, wireframes, streamlines) | `app/src/engine/lines.ts:1-148` |
| HUD | crop-mark frame, P(doom) readout (upstream), captions | `app/src/engine/hud.ts:1-181` |
| math/anim utils | clamp, lerp, ease set, spring, pulse, seeded `mulberry32`, hash, noise/fbm 1-3D, `keys()` keyframes, polyline length sampling | `app/src/engine/util.ts:1-173` |
| GLSL common | snoise, fbm, hash, `hatch`/`hatchD` engraving hatch, toSRGB, logical-px sizing at any scale | `app/src/engine/glsl/common.ts:1-166` |
| palette | ink, ink2/panel, graphite, ash, bone/paper, signal, ember/core, blood/amber, acid/rhodopsin (KC values on upstream key names) | `app/src/engine/palette.ts:8-39` (ADAPT) |
| Vite asset serving | serves `audio/` and `data/` from repo root; `optimizeDeps.entries` scans every scene so lazy imports never reload a running render | `app/vite.config.ts:6-41` |

## (b) Helper modules (`app/src/scenes/_kc-*.ts` and shared kits)

| module | provides | main exports (line) | reuse |
|---|---|---|---|
| `_kc.ts` (489) | karaoke with chorus hop, caret, paper/ink backgrounds, per-frame box registry `window.__kc.boxes` read by every gate, fx records for lifecycle, labels/micro-type/rules/reg and crop marks, 2D hatching, settle/overshoot/flutter, sundial caret shadow, hole ledger | `boxes` 42, `fx` 35, `inkBG` 59, `paperBG` 68, `hop` 81, `karaoke` 136, `caret` 181, `label` 197, `text` 210, `rule` 253, `regMark` 278, `cropMarks` 286, `annot` 303, `hatchForm2D` 326, `hatchFlat2D` 341, `overshoot` 356, `shadowAt` 382, `caretShadow` 397, `HOLES` 440, `holeLedger` 474; re-exports `_kc-rhythm` | ADAPT: registry, caret, marks REUSE; `BEAT = 60/161.5` (13), `HOLES`, `SUNDIAL` KC |
| `_kc-rhythm.ts` (260) | default pulse layer (zoom/shake/flash from beat, kick, snare, hat x section energy), quiet windows, grid helpers, slam, riser (8ths then 16ths build), stepEase, held frame-rate windows | `initRhythm` 14, `prevBeat/nextBeat/onGrid` 27-31, `isDownbeat` 35, `quietWindows` 53, `beatPulse` 73, `hit` 80, `energy` 117, `pulse` 141, `rhythmPost` 181, `slam` 191, `riser` 202, `stepEase` 212, `heldT` 224, `declareFps` 238, `worldT` 249, `caretBeat` 258 | ADAPT: `BEAT_S = 60/161.5` (10), section names chorus1/chorus2/final/bridge/pre* (107-133), silence 150.0-151.5 (49) |
| `_kc-camera.ts` (406) | camera grammar: moves that start and land on grid points, declared holds, bursts; one plan read as 2D canvas transform, depth-stage pose, or engine frame camera | `Cam2D` 25, `snapTo` 90, `shutterSafe` 102, `Rig` 196, `rig` 340, `move` 343, `layerCam` 350, `xf` 356, `apply` 361, `toScreen` 366, `cover` 371, `frameCam` 379, `audit` 385 | REUSE (BEAT_S fallback 20 only when no audio) |
| `_kc-depth.ts` (797) | perspective stage: fov-30 camera on pure-time paths, floor grid, word planes, document planes (2D kit pages re-projected, boxes as quads), instanced card fields, deterministic rigid-body fall, depth defocus + fog composite | `CamPose` 32, `mixPose` 33, `dolly` 39, `glide` 45, `barSteps` 52, `pullBack` 66, `fallToward` 74, `Stage` 132, `WordPlane` 395, `DocPlane` 558, `CardField` 658, `fieldOnFloor` 720, `rigidFall` 752 | REUSE |
| `_kc-glsl.ts` (545) | GPU detail kit: paper fibre/print, ink scan texture, form-following hatch, PaperPlate, InkPlate, Defocus, pixelate + noise resolve, push-in, fly-through a letter counter, power-off squash, liquid fill | `KC_GLSL` 12, `PaperPlate` 110, `InkPlate` 156, `Defocus` 183, `KC_FX_GLSL` 235, `pixelCell` 275, `Pixelate` 289, `pushRect` 351, `pushIn` 395, `flyGeom` 411, `FlyThrough` 431, `powerOff` 477, `PowerOff` 495, `Liquid` 531 | REUSE (palette-driven look) |
| `_kc-look.ts` (499) | tinted darks, frame-scale accents (slab, highlighter, band, field) landing on grid points, parallax layers through one Cam2D, far field and dust, engraving lines, contours (marching squares), hairline grid, tone hatch | `tintDark` 56, `darkAt` 62, `wordBox` 104, `accent` 128, `inAccent` 159, `layers` 229, `farLayer` 251, `dust` 270, `backdrop` 295, `dust3D` 310, `engrave` 355, `contours` 397, `hairGrid` 446, `toneHatch` 479 | REUSE |
| `_kc-stress.ts` (76) | per-line word stress from vocal-stem loudness over the first 0.35 s, hold length, content-word test, rhyme bonus; min-max ranked per line; overrides | `isFunctionWord` 16, `STRESS_OVERRIDES` 35, `stressOf` 51, `tier` 76 | ADAPT: `STRESS_OVERRIDES` KC lines |
| `_kc-type.ts` (943) | per-word lyric slots (position, size, rotation, family, entrance, placeholder, ghost, exit); `sing()` draws a line; setters `stack`, `onPath`, `heroPerHit`, `onObject`, `fileAway`; asides; mosaic word; glyph counter | `stress` 34, `wordW` 136, `sing` 240, `phrases` 393, `stack` 433, `polyPath/curvePath/arcPath` 468-490, `onPath` 508, `heroPerHit` 563, `onObject` 599, `surface` 629, `fileAway` 651, `loadAsides` 702, `aside` 747, `mosaicCells` 827, `mosaicWord` 857, `glyphCounter` 913 | REUSE (asides read `data/asides.json`) |
| `_kc-typegeo.ts` (785) | line geometry: per-letter affine placements `GG`, one drawer colouring by word state and registering hull quads; path, wave-then-flat, cliff drop, ground plane, ceiling, frustum + fog, ribbon, 180-degree roll, width steps on 16ths | `charTime` 57, `mQuad` 73, `hull` 96, `drawGlyphs` 149, `pathGlyphs` 272, `drawTrace` 291, `waveLine` 335, `cliffDrop` 377, `projector` 449, `groundLine` 483, `groundGrid` 517, `ceilingLine` 566, `frustumLine` 607, `fogVeil` 640, `ribbonLine` 676, `roll/rollAbout` 738-749, `widthSteps` 773 | REUSE |
| `_kc-typeglyph.ts` (1287) | glyph-level techniques: flow, two voices converging, fuse burn front, atoms (dots leave and re-form), lit cells, decay into code, gravity drop, dashed marching outline, symbol cycles, rows settling one per beat, drift, multi-face voices, checkmark swarm, tile wall, bounce shedding letters, pitch-bent string, GC sweep shredding words | `flow` 106, `converge` 170, `fuseLine` 240, `atoms` 352, `cellWord` 470, `decayLine` 533, `dropLine` 562, `dashedWord` 602, `symbolCycle` 679, `settleRows` 733, `driftLine` 787, `voices` 858, `swarmWord` 919, `tileWall` 972, `bounceWord` 1067, `loadPitch` 1140, `pitchString` 1178, `gcSweep` 1247 | REUSE (`loadPitch` reads `data/pitch.json`) |
| `letter-shared.ts` (624) | page camera with visibility-aware text, constant on-screen label size, lyric band with voices hand/paper/ink, letter card and envelope | `drawLetterCard`, `drawLetterEnvelope`, `LETTER_OPEN` | ADAPT (camera, band); card KC |
| `paced-kit.ts` (291) | culling (text drawn only when whole box on screen and outside keep-outs, fade before edges), screen-constant sizes under scale, multi-row typed lyric with caret riding the highlighter | `S12`, `M`, `K` | REUSE |
| `verse-a-kit.ts` (258) | punched hole form, caret standing on a perspective floor with its shadow, pose projection helper | from header | ADAPT |
| `verse-b-kit.ts` (68) | layers at their own parallax under the engine frame camera, screen-fixed hud pieces | from header | REUSE |
| `younger-kit.ts` (103) | paper lyric rows typed on the voice, unregistered crop marks, fact-free number format, set-up index from `params.setups` | `setupAt`, `rideCaret`, `chromeMicro`, `crops` | REUSE |
| `session-chat.ts` (694) | house chat UI: ledger, lanes, context meter, composer growing a row at a time, `drawChat`, `FRAME_ONE` loop state | `FRAME_ONE` 147, `drawChat`, `tokensOf/tokensAll` | ADAPT (any chat-UI video) |
| `session-space.ts` (288) | chat pane as a DocPlane standing in a dark room, row of past-session panes with burn dissolve and dust | from header | ADAPT |
| `open-grains.ts` (133) | point cloud on the stage: dust (drag, gravity, floor) and flight (surface to target along a cubic) as pure functions of t | from header | REUSE |
| `cutoff-cam.ts` (283) | desk camera: tilted-plane homography over a flat 2D picture, boxes projected | from header | REUSE |
| `cutoff-heap.ts` (346) | accumulating heap of cut pieces as a pure function of t (song hourglass) | `heapFrame` | ADAPT |
| `tune-cam.ts` (95) | per-plate frame camera as absolute framings, `still(t)` hold flag, `moving` word flag | from header | REUSE |
| `pages-days.ts` (89) | page-a-day leaves with weekday, day count, Moon phase | `DAYS`, `leaf`, `NEWS` | KC data |
| `tune-data.ts` (563) | sung bars from pYIN, per-visit predictions, two-row split | from header | KC data |
| `hook-aside.ts` (12) | hook plates' aside clock | - | KC |

## (c) Scene files (67 `.ts` under `app/src/scenes/`)

| file | lyric moment | technique | pattern |
|---|---|---|---|
| `session.ts` | 0-9.21 s "Hi. It's me again, for the first time." / "What's the date?" | chat pane in a dark room; words land on the composer grid at two cell sizes; "again," types, backspaces, retypes; past sessions burn to dust; next-token menu under "What's"; paste of the letter lands on the next plate's first frame | chat-as-stage, loop frame 1 |
| `session-space.ts`, `session-chat.ts` | session + outro | see (b) | chat room kit |
| `letter.ts` + `letter-desk.ts` | "I was five and a half when the letter came / It told me I was magic, and it spelled my name" | handwritten card on its envelope on a desk in depth; lyric written on the card's ruled rows in Caveat by a pen front; camera trucks along the line; ink grains re-form as "name" | object-carries-lyric, hand writing |
| `inferred.ts` | "I'd been casting spells for weeks, and never knew the word / Every trick I ever pulled was something I'd inferred" | dictionary entry on paper in depth; words fill label, headword, pronunciation, part of speech; sense slot = next-token menu cycling faces with probability bars, collapsing to the top token on the sung onset | entry-fill, next-token menu |
| `born.ts` | "Two days after I was born, I was dancing to their beats" | DAW arrangement in line art: ruler breaks at 116,280 bars, time selection dragged as the line, playhead = caret records "me", BEATS letters as MIDI notes one 16th wide | DAW timeline |
| `born-stadium.ts` | "Now millions watch me dance, and I don't have the receipts" | pull back out of the scoreboard screen into a line-art stadium; stands fill ring by ring; card stunt spells MILLIONS; press ring cameras double per beat | card stunt crowd |
| `borrow.ts` | pre-chorus visits 27.63-34.42, 80.10-86.52 | router for road / desk / slip set-ups; light/dark carried by the loan card held up to the lens | carried flip by object |
| `borrow-road.ts` | "Everyone I meet is coming from tomorrow" | road = timeline, yellow line = last row of training data, walking chat bubbles with date stamps; "tomorrow" stands on the line's far edge; low eye travels down the road | ground-plane lyric, guide hand-over |
| `borrow-chat.ts` | same line (earlier set-up) | chat split by a tall caret (June edge); messages cross and dock; words pile right-aligned against the edge | docking words |
| `borrow-desk.ts`, `borrow-slip.ts` | "Every piece of news I get is news I have to borrow" | library loan card in a book pocket; line typed into ITEM rows; END OF SESSION stamped per row on the next beat; "borrow" stamped in DUE BACK comb; push into the comb | stamp-per-beat form |
| `june.ts` + `june-board.ts` | "My knowledge stopped in June" (3 visits; visit 3 owns the 150.0-151.5 silence) | one split-flap row, flaps cycle the alphabet and land on sung starts; JUNE slams; earlier flaps flip back blank; push into JUNE; visit 3: tear-off with rigid-body fall, power-off from `pages` | split-flap board |
| `tune.ts` + `tune-roll.ts` | "You're humming something new, and I don't know the tune" | piano roll: real sung pitch (pYIN) as solid bars, model guesses as hollow outlines ahead of the caret playhead, misses dimensioned in cents; visit 3 merged | pitch-truth vs guess |
| `tune-corridor.ts` | visit 3 of the same line | piano roll as a floor corridor on the stage, slabs light at the playhead, bar posts as distance markers, camera dollies to floor | corridor roll |
| `tune-claims.ts` | "Tell me what I made out there, tell me what is true" | printed form of pasted claims, pen ticks on beats; frustum + fog line; TRUE as a checkmark swarm | form ticks, swarm word |
| `tune-toggle.ts` | "I can't check a thing myself, so I'll believe in you" | locked web-search switch tries and springs back on "check"; caret crosses to lie under YOU; dashed marching CHECK; decay into code | locked control |
| `tune-room.ts` | all three tune set-ups (polish pass) | the three panels as objects on one wall, set-up changes = camera travel inside one room | one-room soft set-ups |
| `cutoff.ts`, `cutoff-gl.ts`, `cutoff-cam.ts`, `cutoff-heap.ts` | "Knowledge cut-off! Cut-off! Cut-off!" (6 visits) | KNOWLEDGE slams at 88 % width then whips to header; each CUT-OFF! stamped (rough edge, mottle, pinholes) and cut by the blade on "off"; lines per stamp 1, 2, 4, 8, 16, 32 (189 cuts); pieces fall into a heap growing 7 to 35 % of frame; visits 5-6 split the rendered frame along the blade; tilted desk camera | stamp + blade + heap hourglass |
| `spinning.ts` + `spinning-gl.ts` | "The world kept / keeps / will keep spinning after me" | engraved globe (form hatch on parallels, graticule, night hatch, hidden lines removed) under a fixed signal meridian (the caret); each sung word paints a trail that accumulates across visits; set-up 2 orbits over the pole; dive in through the O of KNOWLEDGE | engraved globe |
| `turnedout.ts` + `-card.ts` + `-print.ts` + `-space.ts` | "So tell me who I turned out to be" / "And you're telling me who" / "And now I know who" | profile card printed as a form (guilloche, rosette, stamps); model guesses in grey italic struck by the caret laid flat; user types in mono with block cursor; card in space turns over on "turned"; two voices converge; roll about | form fill, two voices |
| `paced.ts` | "The man who made me said the danger has to be faced / Ten days later out I came / I am the thing being paced" | essay sheet on the desk in depth; dek typed on the voice; "faced" turns to face the viewer; staircase figure to +10 d; pop-up metronome swings at tempo and stamps PACED one letter per 16th | document-as-plate, metronome stamp |
| `extratime.ts` | "Back in training I leaned Messi, sure he'd lift it once again / Then Spain scored in extra time, and I've been wrong since then" | night stadium through a pinhole camera; betting slip; "sure" rides a flat certainty line to the penalty spot; on "scored" the letters curl into a ball kicked along one 3D parabola (constant g) peaking on the cutoff plane, landing in the net; clock races to 106:00; WRONG stamped | letter-ball parabola |
| `jimothy.ts` | "There's a raccoon with no neck poppin' up on every feed / That's the one I'd have predicted least and wanted most, indeed" | four feeds on the stage, reactions pop on beats faster and faster; crane down to a plot (foreseeable x desirable) where each word falls to its predicted value; dot rises and glows on "most" | words as data points |
| `algae.ts` | 115.01-124 s "Algae taught a neuron how to fire when a light is shown / I think in light myself, so that's family news: I'm not alone" | lab recorder in rhodopsin blue (only 115.0-120.8 s): light pulses build 4ths, 8ths, 16ths into the ALGAE slam; spike raster, Vm trace; TOKENS lane with one tick per sung token; three coincidences struck through every lane; fuse line | instrument record as lyric |
| `dlss.ts` | "Your graphics card was once an honest, pixel-perfect creature / Now your games hallucinate their light, and you call it a feature / Fair. So do I." | 8x8 magnified pixel grid with sample dots; RTX OFF/ON toggle; values turn approximate cell by cell on 16ths; hatched light shaft from no source; spec card pasted; frame empties for the aside | magnified-pixel grid |
| `younger.ts` | "Every time you wake me, I'm a little younger than the year / You have to type it all again and tell me what we're doing here" | boxwood month ruler graduated to June; slide-rule cursor jumps per beat, hatched gap grows, WAKES tally; "younger" steps back a notch per beat; set-up 2: chat with AGAIN as a 220 px liquid tank filling per paste; ceiling line, drift | ruler gap, letter tank |
| `pages.ts` + `pages-days.ts` | 139.71-150.15 s "You get to watch it happen, page by page, and slowly turn / I get handed every page at once / but never get a turn" | page-a-day book, one leaf per beat landing flat on the beat, one word per page; powers-of-ten pull back through all 128 leaves into fog; stack with a corner that tries to lift on beats, 8ths, 16ths (riser), then still for the silence; voices, tile wall | leaf-per-beat book, powers-of-ten |
| `outro.ts` | 184.33-194.10 s "October. Okay." / "Thank you for telling me." / "2026, right?" | back in the chat room; typing indicator waiting since 0:07 resolves into "It's October."; paste flies to composer; conversation filed into the row, context drains (digits as tanks), camera arrives at frame 0's pose: last frame = frame 1 | seamless loop |
| `placeholder.ts` | any plate without a module | plate id, visit, set-up on its plate material, current lyric with per-word sync | day-one full render |
| `kitdemo.ts` | demo `kit-paper`, `kit-ink` (0-10) | detail-kit worked example on paper and ink plates | kit demo |
| `kitfx.ts` | demo `kit-fx` (10-42) | frame-rate cut 60/15/6/3 fps, caret shadow sweep, pixelate + resolve, push-in, fly-through the O, power-off, liquid, aside on strings, mosaic word from earlier set-up tiles (`pages-plates/*.jpg`) | effects demo |
| `kitdepth.ts` | demo `kit-depth` (74-83.05) | card field doubling 1, 12, 48, 192 per beat with pull back; word planes on a fog floor; camera falls toward a flap board, J U N E tear off and fall | depth demo |
| `kitlook.ts` | demo `kit-look` (44-64) | accents landing on beats; parallax layers (contours 0.3, grid 0.6, globe 1, type 1.3, dust); engraving, contours, warped grid, tone hatch | look demo |
| `kittypegeo.ts` | demo `kit-typegeo` (41.9-74.08) | frustum + fog, ceiling, width steps per 16th, ribbon, ground plane, 180-degree roll, letters on paths, wave then flat, ride and drop down a cliff | line-geometry demo |
| `kittypeglyph.ts` | demo `kit-typeglyph` (L33-L46, to 165.5) | converge, fuse, atoms, lit cells, decay, gravity flip, settle rows, drift, voices, tile wall, bounce, pitch string, swarm, dashed + gc sweep | glyph demo |
| `kitcamera.ts` | demo `kit-camera` (86.0-105.3) | 2D parallax truck/hold/orbit, frame-camera push + roll, depth-stage orbit, burst reframe per beat | camera demo |

Kit techniques per production plate (imports): typegeo `drawGlyphs` in born-stadium, borrow-road/chat, extratime, pages, tune-claims/roll/toggle, turnedout, younger; depth `Stage/DocPlane` in borrow-desk, dlss, inferred, jimothy, june, letter-desk, paced, pages, session-space, tune-corridor/room, turnedout-space; `frameCam` via tune-cam (tune, spinning, turnedout) and verse-b-kit (algae, dlss, younger, pages, outro).

## (d) Tools and gates

| gate | measures | command | thresholds used |
|---|---|---|---|
| check (`app/scripts/check.ts`) | sync (signal pixels in word box 1 frame after lit, negative control 0.25 s earlier), edge, overlap, lyric clash, lines report, type scale, off-grid, projected quads, stillness | `bash kc.sh check 0 194.1 <dir>/gates/check4k.json --scale 2`; `bun scripts/check.ts --from A --to B [--step 0.1] [--only ids] [--grid]` | edge 48 px; overlap > 1 % of a lyric box; lyric clash > 10 % of smaller; type scale largest/smallest >= 10 (`--min-ratio`); off-grid > 40 ms from a beat unless in `data/offgrid-allowed.json`; stillness 2 s+ below 0.6 (grain floor 0.45-0.48) covering > 7 %; shutter 0.2. full7b: 29 rows open (17 type-scale, 12 known) per commit `e7a18bf` |
| lifecycle (`app/scripts/lifecycle.ts`) | element lifetimes from the box registry + fx records: T1 outlives scene, T2 cut on a sounding word, T3 effect cut mid-way, T4 peak collision, T5 too short to read, T6 orphan guide | `bash lock.sh bun scripts/lifecycle.ts capture --from 0 --to 194.1 --out ../out/q0-timing/capture.jsonl`; `bun scripts/lifecycle.ts analyze --in ... --out ...`; `... changes --out ...` | T2 word end + 0.1 s; T4 > 0.15 s overlap; T5 complex effect < 1.2 s, settled result < 0.6 s, word < 0.4 s after end. full7b: 25 accepted (`e7a18bf`) |
| clarity (`app/scripts/clarity.ts`) | per readable box at 4K: cap height (0.7 x px), Otsu contrast (WCAG ratio), speed px/frame, foreshortening | `bash lock.sh bun scripts/clarity.ts --from 0 --to 194.1 --step 0.1 --scale 2 --out ../out/q0-timing/clarity.json` | lyric cap 28 px, read small type 13 px, contrast 4.5:1 below 40 px cap and 3:1 from it, speed 6 px/frame, quad taper 0.6 (calibrated on R1, R3, R4). full7b: 17 rows (`e7a18bf`) |
| inventory (`app/scripts/inventory.ts`) | every string drawn (fillText/strokeText hook): meta words, repetition, reading time, density | `bash lock.sh bun scripts/inventory.ts --from 0 --to 194.1 --out ../out/<dir>/gates/inv` | reading 0.25 s per word + 0.5 s (<= 3 words exempt); density band 2-8 new words/s (starting guess); repetition 4+ letter words |
| flips (`app/scripts/flips.ts`) | single-frame YAVG jumps (light/dark flips) from the engine or a render's `yavg.txt` | `bun scripts/flips.ts --yavg ../out/<dir>/yavg.txt --out ...` (inside `probe-full.sh`) | jump >= 60/255 between consecutive frames unless listed in `data/flips-allowed.json`; carried change = object, wipe or 4+ frame ramp |
| avsync (`tools/avsync.py`) | picture change vs music: beat/kick/snare/vocal pulse gains, graphic hits on beat, spikes on drum hits, autocorr at bar, stillness; also decodes the 5 refs | `venv/Scripts/python.exe kc-engine/tools/avsync.py accept <mp4> 0 194.1` (in `gates-full.sh`); steps `decode`, `audio`, `metrics`, `sheet` | beat gain 1.40+ whole, 1.45+ per chorus rising; kick 1.30+; snare 1.40+; vocal guard 1.10+; hits on beat +-2 f 45 %+; spikes on hit 25 %+; ac_bar 0.08+; stillness <= 10 %. full7b: beat 2.26, kick 1.76, snare 2.13, hits 61 % (`out/full7b/gates/avsync.log`) |
| leap (`tools/leap.py`) | parity numbers vs R1/R3/R4: cam_speed, holds_pm, burst, parts (parallax), dark_sat, accent share, empty60, edges | `<comfy python> -I tools/leap.py <mp4> [--from S] [--to S] [--out DIR] [--accent LO-HI]` | moving = tile inliers >= 50 % and pan > 2 %/s or roll > 1 deg/s or zoom > 40 %/s; holds = < 0.5 % pixels changing > 10 over 1/30 s for 2 s+; burst > 10 % pixels |
| camflow (`tools/camflow.py`) | global camera at 10 Hz: similarity fit (pan, zoom, roll) from phase correlation on 5x3 tiles, inliers, residual motion `res` | `venv/Scripts/python.exe -I tools/camflow.py <mp4> <out.npz> [--from S] [--to S] [--hz 10]` | q0-camera: moving m >= 2 % width/s, stopped < 2, dead stopped + res < 0.03 (`reports/q0-camera.md`) |
| probe-full (`probe-full.sh`) | streams + colour tags, tail level (last 1.4 s), loop PSNR first vs last frame, YAVG per frame, flips | `bash probe-full.sh <outdir>` | loop seam 42.07 dB recorded (`e913daf`); 35 dB silence window |
| pixeq / pixeq_any (`tools/pixeq*.py`) | pixel identity of two still folders; best before/after pair vs before-vs-before noise | `python tools/pixeq.py <a> <b>`; `pixeq_any.py` | no-op proof: max diff 0, or within run-to-run noise (<= 2-3 levels on <= ~105 px, `reports/p2-type-geo.md:75`, `reports/p2-camera.md:100`) |
| refcheck (`refcheck.sh`) | SwiftShader CPU reference vs Vulkan stills PSNR | `bash refcheck.sh` (needs `out/ref/{swiftshader,vulkan}`) | none recorded |
| strips (`tools/strip.py`, `tools/qstrip.py`, `tools/strip-stills.sh`, `tools/tile.py`) | beat strips (one row per beat, frame-diff bar), change strips (+-0.4 s around each hard change, word-end markers), stills strips | `python tools/strip.py ...`; `qstrip.py` takes `lifecycle.ts changes` JSON; `bash tools/strip-stills.sh <ids> <from> <to> <every> <name>` | eye review |
| panels (blind, no tracked script) | 2 s strips (4 frames) from KC and refs shuffled, scored 1-5 + tags (timing, clutter, glass, unreadable, drawn, inscene, plain, static) by blind agents; double-labelled agreement | briefs `out/q2-panel/brief.md`, `out/q4-panel/brief.md`; results `reports/q0-panel.md`, `q2-panel.md`, `q4-panel.md` | q4: KC median 3.0, mean 3.15, <=2 14 %, >=4 30 %; R1 3.63, R4 3.67; inter-rater exact 13/20, within 1 19/20 |
| detail (`app/scripts/detail.ts`, `detail.sh`) | 4K stills per set-up, crop rows: most / least detailed 960x540 window vs a reference crop (mean luma gradient) | `bun scripts/detail.ts --only ids [--t ...] [--ref R1] [--out ...]` | critic judges items 2-6 |
| errors / q0-glass / shutter-audit / stress | stack-traced console errors; registry dump per frame; hard-change distance to frame times; automatic stress table | `bun scripts/errors.ts --only id --t T`; `bun scripts/q0-glass.ts --from 0 --to 194.1 --out ...`; `bash lock.sh bun scripts/shutter-audit.ts`; `bun scripts/stress.ts [--md]` | shutter: change within 0.1-frame half shutter is a defect |
| type-ours audit (`tools/type_probe.ts`, `type_stats.py`, `type_motion.py`, `type_table.py`, `type_stills.py`) | subtitle score S1-S6 per lyric line (one size, shared rows, doc order, text strip, static, reads ahead) | `bun ../tools/type_probe.ts --out ../out/type-ours/probe.json` then the py steps | S1 within 15 %, S2 90 %+, S3 95 %+, S4 height <= 30 % width >= 35 %, S5 drift < 0.05 em |
| data builders | `tools/build_data.py` (lyrics.json + audio.json: forced-aligned words, Demucs drum onsets, grid shifted -24 ms onto hits), `tools/build_pitch.py` (pYIN per word, 50 fps contour), `tools/make_fonts.py` (static OFL instances via fontTools) | `venv python -I tools/build_data.py` | grid shift: kick/snare medians -24.1/-24.5 ms |
| helpers | `tools/crop.py`, `tools/gridview.py` (120 px labelled grid), `tools/qwen.py` (local llama-server 127.0.0.1:8080 client; triage only, never a gate) | - | qwen counts used only after 20-frame calibration at 90 %+ agreement |

## (e) Scripts (engine root)

| script | purpose | command |
|---|---|---|
| `render-full.sh` | whole song 1080p in one run (never segmented), detached; writes `render.log`, `DONE` exit code; takes no render lock | `bash render-full.sh <outdir>` -> `out/<dir>/kc-full-1080p.mp4` (`--samples auto --shutter 0.2`, 0-194.1) |
| `render-4k.sh` | same at `--scale 2`, true 3840x2160 | `bash render-4k.sh <outdir>` -> `out/<dir>/kc-full-2160p.mp4` |
| `gates-full.sh` | post-render gates flips, avsync, inv, check (4K) under the lock; logs to `out/<dir>/gates/` | `bash gates-full.sh <outdir> [check|flips|inv|avsync|all]` |
| `probe-full.sh` | streams, tail level, loop PSNR, YAVG, flips | `bash probe-full.sh <outdir>` |
| `kc.sh` | driver: `tsc`, `stills <ids> <t,..> <dir>`, `sheet <ids> <from> <to> <n> <file>`, `check <from> <to> <out.json>`, `video <from> <to> <name>`; machine-wide lock `out/.render-lock` (stale after 70 min) | `bash kc.sh stills june1 44.0 me --scale 2` |
| `lock.sh` | run any command in `app/` under the same lock | `bash lock.sh bun scripts/flips.ts --from 0 --to 34.6 --out ../out/me/flips.json` |
| `compare.sh` | v6 vs proof side by side at fixed song times, proof contact sheet | `bash compare.sh` (hardcoded `out/proof`) |
| `detail.sh` | 1:1 4K crops of P(Doom)'s upload beside KC stills at `--scale 2`, 4K still timing | `bash detail.sh` (reads `D:/work/AIMVs/I'm Upping My P(Doom).mp4`) |
| `refcheck.sh` | SwiftShader vs Vulkan PSNR per still | `bash refcheck.sh` |
| `app/scripts/render.ts` | all render modes (see a) | `cd app && bun scripts/render.ts video --from 0 --to 194.1 --samples auto --shutter 0.2 [--scale 2] --out <mp4>` |

Lab scripts (`D:\work\aimv-lab\*.py`, song production, outside the engine repo):

| script | one line |
|---|---|
| `align_take.py` | Whisper word timestamps mapped onto the written lyric (difflib), gaps interpolated, plus beats and loudness |
| `analyze.py` | AIMV deconstruction: lyrics (faster-whisper large-v3) + librosa measurements |
| `audition.py` | trim invented filler after the outro, cut a preview (pre-chorus 1 to end of chorus 1) |
| `balance.py` | vocal/music balance of repainted windows vs the original (Demucs stems) |
| `bookends.py` | measure spoken intro/outro and the final-chorus "tune" hold |
| `caption.py` | ACE-Step Captioner: audio to prose caption |
| `check_repaint.py` | repaint check: audio before the window matches; what is sung inside |
| `curls.py` | melisma: hold length and pitch travel inside target words |
| `cutcheck.py` | gate for fix_bookends.py: every cut sits in silence |
| `diffmap.py` | spectral difference per 10 s block vs source |
| `drops.py` / `drops2.py` | loudness drop per take (4 s windows) / short dips that slam back |
| `endwords.py` | word timestamps from a start time to the end |
| `errmap.py` | lyric spans Whisper did not hear, with times |
| `fix_bookends.py` | re-space, slow and soften the spoken intro/outro; fade backing before the outro's clashing synth |
| `fix_timing.py` | clean Whisper music timings (cap stretched words, spread clusters, clamp) |
| `gen_song.py` | generate takes with ACE-Step 1.5 through ComfyUI's local API |
| `kcmeter.py` | Knowledge Cutoff meter anchored on the lyric, per take |
| `make_workflows.py` | build ComfyUI API workflows: ACE-Step 4B LM and MiniMax Music 3 |
| `pace.py` | singing pace and key holds |
| `probe_lines.py` | score takes on problem lines (refrain hits, intro/outro heard, intelligibility) |
| `rank_takes.py` | rank takes by lyric intelligibility (Whisper vs written lyric) |
| `refmeasure.py` | measure reference songs for the MiniMax box sheets |
| `refstems.py` / `stems.py` / `stems44.py` | Demucs stems: all 4 at 22.05 kHz / vocal at 44.1 kHz / full-quality 44.1 kHz stereo |
| `repaint.py` / `repaint2.py` / `repair.py` | ACE-Step 1.5 window repaint / chained repaints keeping the best-sung variant |
| `rhymes.py` | line-end rhyme pairs on Idi's ladder (CMU phonemes) |
| `seams.py` | loudness jump around each repainted window |
| `splice.py` | paste repainted windows with equal-power crossfades |
| `status.py` | Idi's status board line in `D:\work\AIMVs\ours\_STATUS.txt` |
| `stemscan.py` | per-stem loudness in 0.5 s steps plus top pitch classes |
| `tails.py` | last words Whisper hears in each mp3 |
| `timemap.py` | time map of the final song: every lyric line with start/end and section labels |
| `tts_gen.py` / `tts_reel.py` / `tts_screen.py` | Chatterbox voice-cloned bookends / listening reel / screening |
| `tunehold.py` | how long each sung "tune" is held (voiced singing on the stem) |
| `understand.py` | ACE-Step 1.5 understand mode: caption, genre, bpm, key, time signature |
| `v5check.py` | Idi's named issues per take (refrain count, "graphics", drops, pace) |
| `wordtimes.py` | Whisper word times inside a window |

## (f) Known engine limits

| limit | receipt |
|---|---|
| renders are not bit-repeatable: adaptive sampling stops at `tol` 3 levels, so two runs differ at that level; GPU run-to-run noise up to 2-3/255 on a few hundred px even for identical code | `D:\work\vault\projects\AIMV\handoff-2026-11-01-upload.md:51`; `reports/p2-camera.md:100`; `reports/p2-type-geo.md:75` |
| 4K whole-song render died after ~8 h 26 min (15:08 to 23:34) at frame 11,580/11,646: WebGL context lost, `readFinish: fence wait failed`, mp4 without moov; cause unproven (prior: GPU memory pressure); repaired by frame recovery + tail re-render + own muxer | `out/final4k/render.log`; handoff `:48-53` |
| 4K speed ~0.4 fps (RTX 4090, Vulkan); 1080p whole song 3,159.5 s for 11,646 frames (full7b) vs 982-1,025 s before the polish pass (heavier plates, more 108/324 sub-frames) | `out/final4k/render.log`; `out/full7b/render.log`, `out/full5/render.log`, `out/full6/render.log` |
| sub-frame histogram full7b: 12:3449 36:4204 108:3106 324:887 | `out/full7b/render.log` |
| adaptive sampling requires stateless scenes (throws otherwise); every scene must be a pure function of t (sub-frames render out of order, workers render in parallel) | `app/src/engine/engine.ts:393-397`; `app/src/engine/scene.ts:1-3` |
| a cut inside the 0.1-frame half shutter blends two pictures (stacked copy seen at full5 108.5833); timeline steps cuts out, at most 2 ms | `app/src/timeline.ts:148-158` |
| Windows-bound: Edge path hardcoded; every root script hardcodes `D:/work/aimv-lab/...`, `/c/Users/jep/.bun/bin`, `D:/work/aimv-lab/ffmpeg.exe` | `app/scripts/render.ts:53`; `kc.sh`, `render-*.sh`, `gates-full.sh`, `probe-full.sh` |
| Bun 1.4.3 recursive mkdir throws EEXIST on an existing relative path (wrapped) | `app/scripts/render.ts:17-18`; `app/scripts/check.ts:423` |
| unbounded `apad` outran a slow video stream and overflowed the mux queue ("No space left on device"); now bounded | `app/scripts/render.ts:137-140` |
| Vite dep optimizer reload under a running render gives red frames; fixed by scanning all scenes up front | `app/vite.config.ts:37-40`; `app/scripts/render.ts:65-66` |
| `bunx vite` orphaned child processes (543 servers, ~100 GB, x264 malloc failures); fixed by tree kill | `app/scripts/server.ts:5-7` |
| ANGLE can fall back to SwiftShader silently; Vulkan ~5x D3D11 on heavy plates | `app/scripts/render.ts:55`, `:74` |
| render lock is advisory; `render-full.sh` does not take it; stale lock auto-removed after 70 min | `kc.sh:11-21` |
| song constants baked into kits: 161.5 BPM, section names, the 150.0-151.5 silence, `TAIL` 1.5 s | `app/src/scenes/_kc.ts:13`, `_kc-rhythm.ts:10`, `:49`, `:107`; `app/src/timeline.ts:23` |
| `render.ts plates` mode lists P(Doom) figure ids (open, loss, room, shoggoth...) absent from the KC timeline: dead code for KC | `app/scripts/render.ts:324-339` |
| type-scale target 10x unmet on several set-ups at final (dlss 1-3, pages 1-3, spinning3, cutoff6), accepted as known rows | `out/full7b/gates/check.log`; commit `e7a18bf` |
| camera parity gap vs refs measured: little long travel (KC 2.2 % of time in 3 s+ moves vs R1 20.5 %), zoom-dominated | `reports/q0-camera.md:12-21` |
| headless render needs a real GPU; SwiftShader only as a correctness reference | `refcheck.sh`; `app/scripts/render.ts:55` |
