---
type: note
created: 2026-11-14
author: jep
status: active
project: DECADEnts
---

# Running the big models better on this PC (2026-11-14)

Idi, 2026-11-13: "I want your agents to research this github repo https://github.com/JustAResearcher/gpu-unlock-ada and other recent similar developments that might help us perform better with these new big models."

Done-state: the repository assessed for this PC with evidence; other options ranked with measured numbers kept apart from estimates; the free options tested here where possible.

## Verdict

1. **`gpu-unlock-ada`: skip.** It is real, and it speeds up a kind of GPU math our two models barely use. Expected gain here: 0 to 5% on H3-Image, about nothing on HunyuanImage. It works below the graphics driver at every boot.
2. **Free and measured here today: the HunyuanImage node's Spectrum option.** 54 s down to 44 to 49 s per picture, pictures nearly unchanged.
3. **The one change that would roughly halve HunyuanImage's time is more RAM** (estimate: 22 to 30 s at 64 GB; nobody has published that comparison). It costs money and carries a stability risk on this PC. jep's recommendation: hold.
4. **H3-Image's 6-second text encode has no free fix on a 4090:** its 4-bit format runs emulated on this card generation.

## Receipts

| What | How verified | Where |
|---|---|---|
| Repository facts | GitHub API metadata, file names, headings and keyword counts by script; its code and setup pages were never opened by jep | `C:\Users\jep\comfy2-tools\repo_census.py` |
| Reception and measurements by others | agent report: 4 news articles, 11 Reddit threads, 149 issue titles; no procedure reproduced | `research-2026-11-14/g3-unlock-reception.md` |
| Performance survey | agent report, about 30 sources; every gain for this PC marked as an estimate | `research-2026-11-14/g2-big-model-perf.md` |
| Spectrum | 4 pictures rendered here, same prompts and seed as the earlier set; times from the runner; 3 pairs compared by eye as thumbnails | `C:\Users\jep\comfy2-tools\t5-out\`, `cmp\` |
| Memory and board | jep's own query: 2 x 16 GB Kingston KF560C36-16 DDR5 at 4800 MHz, Gigabyte Z790 AORUS ELITE AX, 4 slots | PowerShell |
| Emulated format | ComfyUI startup log: "emulated ops: mxfp8, nvfp4"; PyTorch 2.14.1 with CUDA 13.0 already installed | `comfy2-*.log` |
| First attempt | the first agent on the repository was stopped by a safety filter while reading it and wrote nothing | - |

## 1. `gpu-unlock-ada`

| Question | Answer | Source, confidence |
|---|---|---|
| What it is | Published 2026-10-23; about 4,900 stars, 85 open issues, 25 commit authors, GPL-2.0; a port to RTX 40 cards of an earlier RTX 30 project | GitHub API, high |
| What it changes | Consumer RTX cards run one tensor-core mode (16-bit inputs summed in 32-bit) at half rate; workstation cards on the same chip run it at full rate. The project lifts that cap at boot, before the driver starts. Clocks, voltages, power limit and VRAM stay the same | TechSpot and a 433-point Reddit explainer, via the agent; medium to high |
| How it gets in | Through a flaw in a small NVIDIA-signed boot firmware. No VBIOS flash, no driver patch | same; medium |
| Raw gain | RTX 4090: 165.6 to 331.6 TFLOPS in a microbenchmark (author); 163.2 to 326.4 (independent owner) | issue titles, high |
| Real matrix math, RTX 4090 | +12 to +34% | TechSpot's summary, high |
| Image models in 16-bit float | +46 to +59% on an RTX 3090 Ti in ComfyUI, 15 images per state, identical pixels | Reddit test, high |
| Image models in 8-bit integers | +0.3%, +4.6%, +5.3%, 0% in four tests | same and issue reports, medium |
| RTX 4090, H3 video model in 8-bit integer format | 55.54 s to 55.81 s, 0% | Reddit comment, medium |
| Memory-bound or disk-bound work | no change ("If your process is memory bound, this isn't going to help") | Reddit, issue report; medium to high |
| Windows | Each port is tied to an exact card and motherboard; needs Secure Boot off and Fast Startup off; must run again from a USB stick after every cold boot; sleep untested in every report. Two desktop RTX 4090 runs on Windows are documented, each a single run | issue titles, Notebookcheck; medium |
| Harm reported | 0 dead cards, 0 blue screens in the reports counted (comments unread, so floors); a failed boot-time run "may deliberately halt with no display until power is removed"; power draw up about 10% under load | issue reports, medium |
| Verification | No outlet ran its own test; about 38 owner reports with matched numbers; no NVIDIA statement found | agent's count, medium |
| Copycat risk | At least 6 third-party forks and Windows ports, several written with AI assistants; in 2022 a fake "unlocker" on GitHub was malware | agent, medium |

Why it gives us almost nothing: H3-Image's image network here is an 8-bit integer build and HunyuanImage is a 4-bit build computed in 8-bit, and HunyuanImage's time goes to moving weights from disk. The unlock touches neither.

When to look again: if DECADEnts moves to a model stored in 16-bit float that fits in 24 GB of VRAM, and a Windows port for the Gigabyte Z790 AORUS ELITE AX has weeks of reports behind it.

## 2. Measured here today

| Test | Result |
|---|---|
| Spectrum on, HunyuanImage 3.0, 4 pictures | 48.9, 47.2, 43.5, 43.6 s against 58.6, 53.5, 53.5, 53.7 s for the same prompts and seed: 12 to 19% less time, 0 errors |
| Spectrum pictures | same design and composition in 3 pairs; small background differences; thumbnail comparison only |
| Browser closed against open, HunyuanImage | free RAM 12 to 14.6 GB against 9 to 10.5 GB; time the same, about 54 s. A few GB of extra free RAM changes nothing |
| H3-Image text encoder | `nvfp4` listed under emulated ops, with the PyTorch build one source says would enable fast kernels already installed |

## 3. Options, ranked for this PC

| # | Change | What it does | Gain | Cost | Risk |
|---|---|---|---|---|---|
| 1 | Spectrum on (HunyuanImage) | skips the heavy part of the network on some steps and predicts its output | measured here: 54 s to 44 to 49 s | free; jep sets it in the runner | small image drift |
| 2 | RAM to 64 GB | lets Windows keep the whole 47 GB file cached, so each step reads RAM instead of disk | estimate: 54 s to 22 to 30 s for HunyuanImage; H3-Image new prompts maybe 2 to 4 s faster. Unreplicated: no published 32 against 64 GB run | a second 2 x 16 GB DDR5-6000 kit lists at $438 in the US (Tom's Hardware index, 2026-11-11; prices have tripled in a year; Israeli price unchecked) | medium: four DDR5 modules train less reliably than two, on a PC with a suspect CPU; keep 4800 MHz and run a memory test |
| 3 | RAM to 96 GB (2 x 48) | same, with margin; pinned memory could come back | estimate: 22 to 26 s, the node author's range | $2,049 US | same |
| 4 | 2-step add-on for H3-Image | finishes a picture in 2 passes; stock needs 6 | measured by its author on a data-centre card: 1.4x at 16 MP; unreplicated; softer detail reported | free, 2 GB download | none for the PC |
| 5 | Windows hygiene | Defender exclusion for the models folder, page file left system-managed | unmeasured, small | free; the exclusion needs Idi's admin account | low |

Skip list: the GPU unlock projects; HunyuanImage's 8-bit file (82 GB, needs the 128 GB class); H3-Image's 8-bit text encoder (27 GB, larger than the card's VRAM); GGUF builds; pinned memory at 32 GB (it caused the error-1450 failure, a known ComfyUI issue).

## 4. Ruling staged for Idi: the RAM upgrade

| Option | What it does | jep's view |
|---|---|---|
| Hold | Stay at 32 GB, run HunyuanImage with Spectrum at about 44 s. A 32-picture sheet takes about 24 minutes | **recommended**: the saving is measured, free, and the purchase rests on an estimate nobody has replicated |
| Buy to 64 GB | About $438 US for a second 2 x 16 GB kit; estimate 22 to 30 s per picture | reasonable once HunyuanImage is the daily model and 44 s is what slows the work; get an Israeli price first |
| Buy to 96 GB | About $2,049 US | too much money for this stage |

## 5. Not done

- No RAM bought, no Windows setting changed, no Defender exclusion (needs Idi's account).
- H3-Image's 2-step add-on and its 8-bit text encoder: untested.
- Spectrum checked on 4 pictures; no blind read of its effect on the head instruction.
- Israeli RAM prices.

## Sources

- `projects/decadents/research-2026-11-14/g3-unlock-reception.md` (full source list: TechSpot, Notebookcheck, GameGPU, Pureinfotech, 11 Reddit threads, 149 issue titles)
- `projects/decadents/research-2026-11-14/g2-big-model-perf.md` (full source list: the node's README and pull requests, ComfyUI release notes and issues, Comfy blog, Tom's Hardware RAM price index)
- Repository: https://github.com/JustAResearcher/gpu-unlock-ada (metadata only)
- Model test: `projects/decadents/decadents-models-test-2026-11-13.md`

## Log

- 2026-11-14 created. Two agent reports, Spectrum measured, memory and emulation checked.
