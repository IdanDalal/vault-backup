---
type: project
created: 2026-10-17
author: jep
status: active
---

# Engine probe P2, 2026-10-17: P(Doom)'s own engine runs on this PC

Verdict: **P2 PASSES with one caveat per GPU backend.** P(Doom)'s engine boots on Windows, renders its plates on the RTX 4090 and matches its YouTube frames by eye on 13 of 14 plates on either backend. The 14th breaks differently on each backend, with the cause found. Speed on its heaviest kind of plate: 0.7 frames/s on D3D11, 3.7 frames/s on Vulkan.

Follows [[engine-probe-p1-2026-10-17]]. Installs okayed by Idi 2026-10-17 ("okay, install Bun and the packages, run P2").

## 1. What was installed

| item | where | receipt |
|---|---|---|
| Bun 1.4.3 (released 2026-10-10), `bun.exe` + `bunx.exe` copy | `C:\Users\jep\.bun\bin\` | GitHub release zip, anonymous; SHA-256 `0bf84e80...5d3d` = the release's `SHASUMS256.txt` |
| P(Doom)'s npm packages, 32 installed from `bun.lock` (`--frozen-lockfile`, no install scripts trusted) | `refcode\pdoom-video\app\node_modules` | three 0.186.0, opentype.js 2.0.0, vite 8.3.0, playwright-core 1.63.0, typescript 7.0.2, 3 type packages |
| `scripts/render-win.ts`: copy of `render.ts`, 3 changes | same repo, untracked | Edge by path in place of `channel: 'chrome'`; `--use-angle=${PDOOM_ANGLE ?? 'd3d11'}` in place of `metal`; prints the WebGL renderer at every launch |

P(Doom)'s own files are unchanged: `git status` shows only `render-win.ts` (one diagnostic edit, section 3.2, was reverted with `git checkout`).

## 2. Results

| test | D3D11 | Vulkan | receipt |
|---|---|---|---|
| boots, GPU | yes, 4090, 3.6 s | yes, 4090 | `RENDERER` lines in every log |
| 14 plate stills vs YouTube, by eye | 13 of 14 match; left turn (84.3 s) loses its contour lines | 13 of 14 match; shoggoth (31.9 s) gets stray outlines across the smiley card | `p2-pairs-1/2.jpg`, `p2-pairs-vulkan-1/2.jpg` |
| 14 stills, `--samples auto --shutter 0.2`, wall clock incl. boot | 45.2 s | 16.3 s | `p2/stills.log`, step lines |
| 5 s video, 30-35 s (shoggoth), P(Doom)'s 1080p export settings, 2 workers | 300 frames in 403.8 s = **0.7 frames/s**; matches YouTube at 30.5/32.5/34.5 s | 300 frames in 80.1 s = **3.7 frames/s**; the card artifact shows in all 3 checked frames | `p2-video-vs-yt.jpg`, `p2-video-vulkan-vs-yt.jpg`, `video*.log` |
| video file | h264 1920x1080 60 fps, `yuv420p(tv, bt709)`, AAC audio, 65.9 MB | same | ffmpeg probe |
| OpenGL backend (`--use-angle=gl`) | never reaches the GPU: 9 of 9 renderer checks fell back to SwiftShader (CPU) | | `p2/launch-gl.log`, P1 runs G1, G2 |

Sub-frames (motion-blur samples the engine chose): the 5 s clip used 108 per frame on 287 to 300 of 300 frames, so this is one of the heavy stretches. Ceiling, if every frame of the 156.65 s song were this heavy: 9,399 frames: D3D11 about 3.5 h, Vulkan about 42 min (arithmetic from the clip, untested on the full song; lighter plates will be faster). P(Doom)'s README: about 57 min on an M5 Pro, in context the 4K render (medium confidence on that reading).

## 3. The two plate bugs

1. **D3D11, left turn: derivatives inside a breakable loop.** `leftturn-map.ts:414` sizes the contour lines with `fwidth(h)` (a screen-space derivative: how fast a value changes between neighbouring pixels), inside `shade()`, which `main()` calls from a loop with an early `break` (lines 505-506). Direct3D leaves derivatives undefined in such loops, the line width collapses, the contours vanish and the face fill stays. Proof: with the loop removed (one call to `shade()`), D3D11 draws the contour mask and matches YouTube (`p2-leftturn-diag.jpg`); the compiler warning `potentially uninitialized variable (f_shade)` disappears too. Reverted afterwards.
2. **Vulkan, shoggoth: outlines leak through the smiley card.** Dark contour lines of the shoggoth show across the card (`p2-shoggoth-crop.jpg`, video sheet). D3D11 and the CPU renderer draw it clean. Cause not traced (inference: an edge or depth test that behaves differently on Vulkan).
3. **The CPU renderer (SwiftShader) draws both plates correctly** (`p2-gl-ctl.jpg`). It is slow but serves as the correctness reference.

Correction to my own P2 log: I first read an OpenGL driver message (`GL_CLOSE_PATH_NV`) as proof the GL backend reached the NVIDIA card. That name is enum value 0, printed for a zero ID; the GL stills were CPU renders. Retracted before this report.

## 4. What this means for Knowledge Cutoff (route B)

1. **The engine works here.** P(Doom)'s whole stack (Vite, three.js, its shader engine, its WebSocket frame pipe, ffmpeg) runs on this PC with a 3-line launcher change. Route B stands on a measured foundation.
2. **Backend: recommend Vulkan for our own engine**, at 5x the speed of D3D11, plus one guard: every plate's contact sheet compared against a SwiftShader still of the same frames. That catches both bug classes found today (and P1's Vulkan noise-hash artifact). D3D11 stays the fallback backend. Medium confidence: the 5x is one plate; the per-plate guard is what makes the choice safe.
3. **Shader rules from today's evidence:** no `fwidth`/`dFdx`/`dFdy` inside loops that can `break`; integer hashes in place of `sin` hashes (P1); `preserveDrawingBuffer: true` or read in the same call (P1).
4. **Every launch checks its renderer string** and relaunches on SwiftShader (P1: 1 of 16 parallel launches; P2: the GL backend always).

## 5. Not done

1. 4K (`--scale 2`) not tried.
2. Full song not rendered; the time ceiling in section 2 is arithmetic.
3. The Vulkan card artifact not traced to a line.
4. One 404 in every browser log, file not identified (probably a favicon); renders match regardless.

## 6. Files (`D:\work\aimv-lab\engine-probe\`)

| file | what |
|---|---|
| `p2.sh` | steps `gpu`, `stills`, `perf`, `video`, `yt` (PATH for bun + ffmpeg; `PDOOM_ANGLE` picks the backend) |
| `p2ctl.sh`, `p2launch.sh` | left-turn backend control; launch-rate test |
| `p2sheet.sh`, `p2vid.sh` | pair sheets; video vs YouTube sheet |
| `p2-pairs-*.jpg`, `p2-video-*.jpg`, `p2-leftturn-*.jpg`, `p2-shoggoth-crop.jpg`, `p2-gl-ctl.jpg` | the by-eye evidence |
| `p2\pdoom-30-35-d3d11.mp4`, `p2\pdoom-30-35-vulkan.mp4` | the two 5 s renders |
| `p2\stills*`, `p2\yt\`, `p2\ctl-*`, `p2\diag-noloop-d3d11\` | the stills |
| `refcode\pdoom-video\app\scripts\render-win.ts` | the Windows launcher |
