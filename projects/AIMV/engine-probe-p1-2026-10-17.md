---
type: project
created: 2026-10-17
author: jep
status: active
---

# Engine probe P1, 2026-10-17: WebGL renders headless on this PC

Verdict: **P1 PASSES on all four criteria.** Headless Edge renders WebGL on the RTX 4090, lossless, deterministic, byte-identical to a visible window, at 14 frames/s per worker and 41 frames/s on 4 workers. No installs (playwright-core 1.64 was already in `kc-video\node_modules`). Next domino: P2, which needs Idi's okay for installs (section 6).

From [[handoff-2026-10-17-engine-probe]] step 1. Baseline audit: [[knowledge-cutoff-v6-2026-10-17]].

## 1. Pass criteria

| criterion (handoff) | result | receipt |
|---|---|---|
| no black frame | PASS: 0 of 300 in every main run (A1, A2, V1, V2, W1, W2) and 0 of 3,600 in the parallel runs | `stats.json` `blackFrames: []`, max luma check < 16 |
| two runs md5-identical | PASS: A1 = A2, 300 of 300 frames; V1 = V2, 300 of 300; 12 parallel workers = A1, 300 of 300 each | `md5.txt` per run; md5 of A1, A2, W1 lists all `0b552e1d...2994` |
| equal by eye to a visible Edge window | PASS, stronger than by eye: visible window (W1 default flags, W2 same flags) byte-identical to headless, 300 of 300 | `side-f150.jpg` (left headless, middle visible) |
| at least 10 frames/s | PASS: 14.1-14.6 frames/s one worker, end to end, lossless PNG; 41 frames/s on 4 workers (3 of 3 runs) | `matrix.log`, `par-a/b/c.log` |

## 2. The probe

- Page `probe.html`: WebGL2, one fullscreen shader (domain-warped noise field + growing ring), bloom (bright pass, 2x separable Gaussian blur at half resolution, half-float targets, composite + tone curve), one karaoke line drawn on a 2D canvas and uploaded as a texture (words light and hop by time), a `t =` label. Pure function of `t`: `window.renderAt(t)`.
- Driver `run.js`: one Edge per run via playwright-core, 1920x1080, 300 frames = 5 s at 60 fps, `preserveDrawingBuffer: true`. Per frame: render, `readPixels` (luma check for black frames), lossless PNG encoded in the page, md5 of the PNG bytes in Node, every 30th frame kept.
- All in `D:\work\aimv-lab\engine-probe\`.

## 3. Every run (`matrix.log`)

| run | flags | WebGL renderer | engine ms/frame | end-to-end frames/s | black | md5 vs A1 |
|---|---|---|---|---|---|---|
| A1, A2 headless | `--in-process-gpu --use-angle=d3d11` | RTX 4090, D3D11 | 5.8 / 5.7 | 14.1 / 14.4 | 0 | A2 = A1, 300/300 |
| V1, V2 headless | `--in-process-gpu --use-angle=vulkan` | RTX 4090, Vulkan 1.4.341 | 2.4 / 2.3 | 14.3 / 13.8 | 0 | differs, 300/300 (section 4.3) |
| W1 visible window | none | RTX 4090, D3D11 | 5.9 | 14.3 | 0 | identical 300/300 |
| W2 visible window | `--in-process-gpu --use-angle=d3d11` | RTX 4090, D3D11 | 6.0 | 14.6 | 0 | identical 300/300 |
| X1 headless, 30 fr | none | RTX 4090, D3D11 | 6.1 | 17.7 | 0 | identical 30/30 |
| X2 headless, 30 fr | `--use-angle=d3d11 --disable-gpu-sandbox` | RTX 4090, D3D11 | 5.6 | 18.5 | 0 | identical 30/30 |
| X3 headless, 30 fr | P(Doom)'s set on Windows: `--use-angle=d3d11 --enable-gpu-rasterization --ignore-gpu-blocklist` | RTX 4090, D3D11 | 6.0 | 17.6 | 0 | identical 30/30 |
| X4 headless, 30 fr | `--disable-gpu --enable-unsafe-swiftshader` | SwiftShader (CPU) | 90.6 | 7.3 | 0 | (software, not compared) |
| D1, 60 fr | A flags, `preserveDrawingBuffer` off, read in the same call | RTX 4090 | 5.9 | 16.0 | 0 | identical |
| D2, 60 fr | A flags, `preserveDrawingBuffer` off, read in a later call | RTX 4090 | 6.2 | 12.9 | **60 of 60** | all frames one blank md5 |
| D3, 60 fr | A flags, `preserveDrawingBuffer` on, read in a later call | RTX 4090 | 5.7 | 8.8 | 0 | identical |
| Pa, Pb, Pc | 4 workers at once, A flags | RTX 4090 | 9.0-9.3 each | 41 total, each run | 0 | 12 of 12 workers identical |
| P (first try) | 4 workers at once, A flags | 3 of 4 on the 4090; **worker 2 had no WebGL** | | 12.1-12.3 each | 0 | 3 identical, 1 empty |

Engine ms = render + `readPixels` only, median of 120 frames. End to end = render, readback, PNG, transfer, md5, disk.

## 4. Findings

1. **WebGL reaches the 4090 with default flags today.** X1 and the unchanged 10-15 script (`research-video-tech\gpu-probe.js`, re-run today) both report the 4090 with no flags. The 10-15 note "default flags: no WebGL" does not reproduce, and X2 shows the GPU sandbox is no obstacle under `jep`, so the 10-15 inference about the sandbox is unsupported. Why 10-15 differed: unknown (low confidence guess: the PC instability period or a driver since then).
2. **The WebGL black-frame mechanism, reproduced on demand.** D2: `preserveDrawingBuffer` off + pixels read in a later call = 60 of 60 black. D1 and D3 = 0. Rule for the new engine: `preserveDrawingBuffer: true`, or read inside the same call as the draw.
3. **The 10-15 black frames were a Canvas2D problem, probably.** The old probe's 2D canvas under the GPU gives a 58,790-byte PNG where software gives 229,346, which suggests the 2D drawing comes out blank or partial on the GPU path (medium-low confidence: that PNG was not opened). Our probe's 2D text canvas, uploaded into WebGL as a texture, renders correctly under the GPU (contact sheet). Text-into-WebGL is the safe route.
4. **D3D11 is the backend of record.** Vulkan draws 2.5x faster but shows blocky squares in the noise field (`side-f150.jpg`, right panel): the `sin`-based hash in the shader loses precision there. PSNR (peak signal-to-noise ratio; above 40 dB is invisible) D3D11 vs Vulkan = 25.2-28.1 dB, a visible gap. If Vulkan is ever needed, shaders use integer hashes.
5. **The GPU is idle most of each frame; the transfer is the cost.** Per 1080p frame (`xfer.js`, median of 8): render 3.6 ms, `readPixels` 4.3 ms, raw RGBA to base64 19.6 ms, 11 MB string over the DevTools channel 103 ms, raw POST to localhost 141.7 ms, PNG in page 24.2 ms (1.21 MB). Lossless PNG in the page is the fastest exit found: 6.4 frames/s (raw base64) became 14-16 frames/s. Headroom left: the engine alone would run about 170 frames/s.
6. **One launch in 16 lost WebGL** when 4 workers started at once (first parallel try, worker 2: no WebGL2, no WebGPU, no error message). 0 failures in 12 later simultaneous launches and 0 in 20 single launches. Rule for the renderer: check the renderer string at worker start, relaunch on a miss.
7. **Planning number:** full song = 11,556 frames at 60 fps; at 41 frames/s that is about 4.7 min for probe-weight plates at 1080p. P(Doom)-weight plates will be slower (their 4K took about 57 min on an M5 Pro, their README).

## 5. Not done

1. 4K not tested (probe canvas fixed at 1920x1080).
2. P(Doom)'s own engine not run (P2, needs installs).
3. GPU-side encode (WebCodecs to the 4090's video encoder) and P(Doom)'s pixel-pack-buffer readback not tried; not needed at 41 frames/s.
4. The Canvas2D-on-GPU blank (finding 3) not opened or diagnosed; moot if the new engine is WebGL.

## 6. P2: what it installs (Idi's okay needed)

1. **Bun** (JavaScript runtime; P(Doom)'s `render.ts` calls `Bun.serve`, `Bun.spawn`, `Bun.write`, so Node would need a port): `bun-windows-x64.zip` from github.com/oven-sh/bun releases, anonymous, unzipped into a user folder, no admin, no installer.
2. **P(Doom)'s npm packages** via `bun install` from its `bun.lock` (76 lockfile entries, other-platform binaries skipped): three 0.186.0, opentype.js 2.0.0, vite 8.3.0 (+ rolldown and lightningcss Windows binaries), playwright-core 1.63.0, typescript 7.0.2, type packages. All from the public npm registry, anonymous. Lands in `refcode\pdoom-video\app\node_modules`.
3. Then: point its renderer at Edge (`executablePath`, `--use-angle=d3d11` in place of `metal`), render 5 s of its own plates, compare to its YouTube frames by eye, note speed.

## 7. Update after P2 (same day)

Finding 4 ("D3D11 is the backend of record") held for this probe page only. On P(Doom)'s engine each backend breaks one plate, and Vulkan renders 5x faster; the recommendation moved to Vulkan + a SwiftShader reference check per plate. Details: [[engine-probe-p2-2026-10-17]].

## 8. Files (`D:\work\aimv-lab\engine-probe\`)

| file | what |
|---|---|
| `probe.html` | the WebGL page |
| `run.js` | driver: one run, md5s, stats |
| `matrix.sh`, `matrix.log` | 13-run matrix and its output |
| `par.sh`, `par.log`, `par-a/b/c.log` | 4-worker tests |
| `xfer.js` | per-stage transfer timing |
| `sheets.sh` | contact sheets, PSNR, side-by-side |
| `sheet-A1-headless-d3d11.jpg`, `sheet-W1-headed-default.jpg`, `sheet-V1-headless-vulkan.jpg` | 11 kept frames each, t = 0 to 4.98 s |
| `side-f150.jpg` | frame 150: headless D3D11, visible D3D11, headless Vulkan |
| `out\<run>\` | `stats.json`, `md5.txt`, kept PNGs |
