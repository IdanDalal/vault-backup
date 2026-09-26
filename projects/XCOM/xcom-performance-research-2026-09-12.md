---
type: reference
created: 2026-09-12
author: jep
project: XCOM 2 WotC campaign
status: active
---

# XCOM 2 at 4K with DLSS 5: where the frames go and how to get them back

Scope: Idi's ask of 2026-09-12, "significant performance without sacrificing significant visual quality", plus upscaling and frame generation for a 2016 DX11 game. Baseline: about 45 FPS average, RTX 4090, 3840x2160 fullscreen, every in-game setting at maximum except Depth of Field (off, it blacked dynamic lighting). Research done inline by jep on 2026-09-12; each claim carries its source and a confidence tag. Nothing below was tested on this PC yet.

## 1. What is actually running (receipts from the PC)

- `Binaries\Win64`: ReShade 6.8.0 (`dxgi.dll`), `renodx-xcom2.addon64` (HDR, v0.2026.221.951), `renodx-dlss.addon64` (ShortFuse's RenoDX DLSS addon), `nvngx_dlssnr.dll` (165 MB, the DLSS 5 neural rendering snippet), `nvngx_dlss.dll`.
- `ReShade.log` 2026-09-12 09:27: "DLSS-NR direct: backend-owned NVIDIA NGX core initialization succeeded for the D3D12 device", "created private output 1: size=3840x2160", EvaluateFeature succeeded on every options revision. **Neural rendering runs at full 4K on every frame.** It also reports `nvngx_dlss.dll` and `sl.interposer.dll` "not found", so DLSS Super Resolution and Frame Generation are not wired; only NR is.
- `ReShade.ini [RENODX-DLSS]`: `DirectNeuralRenderingIntensity=1`, `Style=1`, `HookPoint=5`, `DLSSQualityMode=6`, `FrameGenerationPresentationPath=1`, Streamline nits set but Streamline absent.
- `BACKUP\` holds the earlier pipeline from 08-30: `dlss5-feed.addon64` (DLSS5-Feeder), `renodx-dlss5.addon64` (community branch), the Streamline DLLs (`sl.*.dll`, `nvngx_dlssg.dll`). Idi moved from the Feeder to the direct addon on 08-31.
- Driver 616.64 (installed 09-04). The Feeder README documents a fault on 616.56/616.64 with the community `renodx-dlss5` v4.6/v4.7 branch only; the ShortFuse addon Idi runs evaluates fine per the log. No action.
- Live `[SystemSettings]`: `bUseMaxQualityMode=True`, `MaxShadowResolution=4096`, `ShadowFilterQualityBias=5`, `bEnableVSMShadows=True`, `AmbientOcclusion=True`, `AllowSubsurfaceScattering=True`, `DynamicShadows=True`. The 09-11 reset put everything at the top.

## 2. Step zero: measure the split (10 minutes, no downloads)

The 45 FPS is a sum of three unknowns: the game at max settings, the RenoDX HDR pass, the NR pass. The RTSS overlay already on screen shows frametime in ms. Same save, same camera, read ms four times:

| State | How | Writes |
| --- | --- | --- |
| Game only | rename `dxgi.dll` to `dxgi.dll.off` (proven safe 09-11) | ms_game |
| Game + HDR | ReShade on, NR addon disabled in the ReShade Add-ons tab | ms_hdr |
| Game + HDR + NR | current | ms_all |
| Game at High preset + HDR + NR | in-game preset High | ms_high |

ms_all minus ms_hdr = the NR tax. That number decides whether levers 3 or 4 matter more. Frames per second convert as 1000 / ms.

## 3. Lever: in-game settings, ranked by measured cost

Source: PCGamingWiki community port report "XCOM 2, Optimized Video Settings for Quality and Performance" (measured on 2016 hardware at 1080p; ratios, not absolutes; single tester, no replication). Confidence in the ranking: medium. Confidence that the ratios hold at 4K on a 4090: low, because the GPU-heavy items scale with pixels and the CPU-side ones do not.

| Setting | Cost of the top value | Recommended | Visual loss |
| --- | --- | --- | --- |
| Shadows: Full vs Directional Only | over 50% | Full at Medium quality first, Directional if still short | Directional drops point-light shadows; visible indoors |
| Shadow Quality High vs Medium | about 25% | Medium | soft edges; VSM at 4096 is the expensive part |
| Ambient Occlusion SSAO vs Tile AO | about 18% | Tile AO | slightly flatter contact shadows |
| Decals All vs All Static | 10 to 15% in the Avenger | keep All in tactical if affordable | fewer dynamic scorch marks |
| Screen Space Reflections | 5 to 10% | off | wet-surface reflections gone; NR re-adds some material response |
| Depth of Field Bokeh vs Simple | about 10% | already off | none for this campaign |
| Anisotropic 16x vs 8x | about 2% | keep 16x | none |
| Anti-aliasing MSAA 8x | frame rate "well below 30" (GamingBolt visual analysis) | FXAA | MSAA in this engine is both slow and weak; NR sharpens anyway |
| Bloom, Dirty Lens, High Res Translucency, Subsurface Scattering | "virtually no improvement" when disabled (same report) | keep on | none |

Config-side, the settings menu writes these keys; no hand edit needed. If Idi wants one hand edit later: `bUseMaxQualityMode=True` is an engine debug flag the base engine ships as False; the menu's top preset turns it on. Untested whether flipping it alone gains anything. Not recommended before the measurement.

Old community ini tweaks (PhysX heap sizes, mip fade speeds, `bDisablePhysXHardwareSupport`) come from 2016 forum threads without measurements. Skip unless stutter, rather than FPS, becomes the complaint.

## 4. Lever: cut the neural rendering tax

- **Feeder path has a resolution dial, direct path does not (as far as documented).** DLSS5-Feeder `work_resolution` (D3D11 only, 50 to 100%) downsamples the frame, runs DLAA plus NR at the smaller size, expands with bilinear or FSR 1. Author's own number, one game (Fable Anniversary): 50% work resolution 57 to 62 FPS vs 44 to 48 at 100%. Source: Feeder README. Confidence that it transfers to XCOM 2: medium; the mechanism is resolution-proportional.
- The ShortFuse direct addon exposes `DLSSQualityMode`, but without motion vectors DLSS Super Resolution cannot run, so this is no resolution dial in XCOM 2. A Nexus page claims "resolution mode" for the community `renodx-dlss5` stack; the page is behind a 403 and unread. Unverified.
- Intensity: `DirectNeuralRenderingIntensity=1` is the addon's neutral value (documented range 1.00 to 1.05 on dlss5mod.com). Intensity does not change cost; the model runs regardless.
- **Cheapest structural trick: lower the game's own resolution and let a spatial upscaler finish.** ReShade, HDR and NR all run at the game's swapchain size, so 2560x1440 costs NR about 44% of 4K. The upscaler options are in section 5. Visual loss: NR output at 1440p then spatially upscaled; NR's detail synthesis partly compensates. Untested.

## 5. Upscaling for a game with no DLSS inputs

| Path | What it is | Verdict |
| --- | --- | --- |
| DLSS Super Resolution native | needs engine motion vectors and depth | XCOM 2 has none; impossible without the Feeder |
| DLSS5-Feeder `work_upscale=2` | "experimental DLSS SR" on synthesized motion vectors from ReShade depth | exists, beta, "temporal quality of estimated motion vectors" is the stated weakness; HUD gets processed with the scene |
| dlss5-bridge substitute path | NVIDIA Optical Flow to fake DLSS inputs on DX11 | author: "text softens and dense foliage smears"; XCOM is foliage-heavy |
| NVIDIA Image Scaling (NIS) | driver spatial upscale plus sharpen, NVIDIA App per game | free, any game, works with ReShade because it acts at scanout; render at 1440p or 1800p, output 4K |
| Lossless Scaling LS1 / FSR 1 / NIS | app-side spatial upscale of a windowed game | same idea, bundled with its frame generation, $6.99 |

Recommendation: NIS or the Lossless Scaling upscalers, only if the measurement shows NR dominates. Temporal upscaling in a game with no motion vectors is where quality gets sacrificed.

## 6. Frame generation for a DX11 game from 2016

| Option | Cost | Requirements | Fit with Idi's stack | Confidence |
| --- | --- | --- | --- | --- |
| A. NVIDIA Smooth Motion | free | RTX 40 supported since the 2025-08-19 Game Ready driver plus NVIDIA App; DX11, DX12, Vulkan; per game under Graphics > Program settings > Driver Settings | Injects NvPresent64.dll, wraps the swapchain, presents twice per game frame; ReShade's chain runs inside Present, so NR frames get interpolated correctly on DX11. DLSS5-Feeder 0.8.0-beta.4 ships "Smooth Motion compatibility improvements", meaning people run both. Per-API kill switch exists in NVIDIA Profile Inspector (Smooth Motion Enabled APIs, bitfield 7; clear 2 for DX11). HDR: NVIDIA forum threads report flicker with RTX HDR, a different feature; no report found for RenoDX HDR. | high on availability, medium on artifact-free with this stack |
| B. Lossless Scaling LSFG 3.1 | $6.99 once, Steam | borderless windowed only (XCOM 2 is `Fullscreen=True` now); base 45 FPS is at the guide's "preferred" floor; cap base FPS with RTSS; HDR toggle only for games already in HDR (RenoDX qualifies) | vendor-neutral; ghosting on fast edges; developer's own latency figure, LSFG 3.1 vs 2: about 24% better at 40 FPS base, X2; dual-GPU offload exists but the Intel UHD 770 at 4K is unverified and probably short | high on availability, medium on quality |
| C. DLSS Frame Generation (DLSS-G) or MFG | free | a game that ships Streamline DLSS-G | MFGAdaUnlock "only unlocks existing frame generation, never adds it"; the RenoDX addon's Streamline settings need a native lifecycle. **Dead for XCOM 2.** | high |

Turn-based tactics tolerates frame-gen latency; camera pans and unit moves are where a doubled frame rate shows.

## 7. Context on "DLSS 5"

- NVIDIA: DLSS 5 launched 2026-09-03 in NBA 2K27, RTX 50 only at launch, "RTX 40 series support later this fall" (NVIDIA newsroom, TechPowerUp SIGGRAPH coverage). Three developer-facing models A, B, C.
- What runs on the 4090 today is a community pipeline around a leaked build (DSOGaming, igorslab, the DLSS5oneclick README say so plainly). Single-player only; the tools warn about anti-cheat. XCOM 2 is single-player.
- igorslab on a 4090: NR "can significantly reduce the frame rate", "DLSS Super Resolution and Frame Generation can only partially offset" it. No numbers published.
- When official 40-series support lands, the driver path may replace the ReShade injection. Worth a re-check in November 2026.

## 8. Quest list (jep proposes; Idi picks)

1. **Measure**: the four frametimes of section 2. Done-state: four numbers in the Whiteboard. Cost: 10 min.
2. **Settings pass**: FXAA, Tile AO, Shadows Medium, SSR off, everything else max. Done-state: ms_high2 written next to ms_all, screenshot judged by Idi. Cost: 5 min.
3. **Smooth Motion**: NVIDIA App > Graphics > XCOM 2 > Driver Settings > Smooth Motion on. Done-state: RTSS shows about 2x, no flicker on a camera pan over Xenoform foliage. Cost: 5 min, free, reversible.
4. **Only if NR still dominates**: game at 2560x1440 plus NIS to 4K, or Lossless Scaling with LS1 upscale plus LSFG X2 in borderless. Done-state: Idi's eyes on the same save at the same camera.
5. **Only if he wants the resolution dial inside NR**: return to the Feeder with `work_resolution` 67 to 75 and FSR 1. Cost: reinstall from `BACKUP`, medium risk of the 08-30-style crash.

## 9. Measured 2026-09-12 (Idi's screenshots `D:\work\screens\XCOM\NR-*.png`, RTSS overlay read at full resolution)

| State | FPS | ms | GPU |
| --- | --- | --- | --- |
| RenoDX HDR, NR off, max settings | 93 | 10.8 | 100% |
| HDR + NR, max settings | 45 | 22.2 | 99% |
| HDR + NR, Shadow Quality Medium + Tile AO | 53 | 18.9 | 99% |

- NR tax at 4K: about 11.5 ms per frame, larger than the whole game render. Two settings bought 3.3 ms. Ceiling with NR at 4K and a free game: about 87 FPS. **Only the NR resolution has real headroom.**
- Idi's verdicts: Smooth Motion "terrible" (disabled), Lossless Scaling excluded (does not coexist with RenoDX HDR, his earlier test), Directional-only shadows rejected (loss larger than gain). Frame generation is closed for now.
- Eleven corrupt mods re-subscribed.

### The NR resolution dial: three paths

| Path | What | Expected at 4K output | Source status |
| --- | --- | --- | --- |
| A. Driver NIS | game at 2880x1620 or 2560x1440, NVIDIA App Image Scaling to 4K; NR and HDR run at the game size | 1620p: NR about 6.5 ms + game about 6 ms, near 80 FPS; 1440p: near 100 FPS. Whole frame including UI is spatially upscaled and sharpened. HDR supported on Turing and newer (NVIDIA KB 5280). | free, installed, 5 min, reversible |
| B. Feeder `work_resolution` | DLSS5-Feeder from `BACKUP`, `work_resolution=75`, `work_upscale=1` (FSR 1); output and UI stay 4K, NR runs at 75% | author's one-game number: about 30% more FPS at 50% | anonymous GitHub (0.8.0-beta.4); the 08-30 attempt crashed once; community `renodx-dlss5` v2.5 in `BACKUP` is the Aug-29 yumlevi asset, byte-identical |
| C. ShortFuse addon build 2026-09-09 or newer | new "Scale" option runs the neural model at lower resolution, "single dial for FPS"; guide starting point Scale 75, Model C, 1 pass, intensity 0.6 to 0.7; 75% keeps most of the result, 50% shows hair artifacts (one tester, 4K); builds from 09-09 switch `DirectNeuralRenderingHookPoint` to `DirectNeuralRenderingHookMethod=2` | best quality per ms of the three | **Discord `#DLSS5` channel only** as far as found: RenoDX GitHub snapshot (09-06) and nightlies ship no DLSS addon; yumlevi and FF7R mirrors carry 08-28 and 08-30 builds; Idi's 08-31 binary has no Scale option (verified by reading its option table). Gated source, Idi's rule, Idi's call. |

## Sources

- NVIDIA newsroom, "NVIDIA DLSS 5 Delivers AI-Powered Breakthrough in Visual Fidelity for Games": https://nvidianews.nvidia.com/news/nvidia-dlss-5-delivers-ai-powered-breakthrough-in-visual-fidelity-for-games
- TechPowerUp, "NVIDIA Shows DLSS 5 Progress and Technical Details at SIGGRAPH 2026": https://www.techpowerup.com/350916/nvidia-shows-dlss-5-progress-and-technical-details-at-siggraph-2026
- NVIDIA GeForce news, Smooth Motion for RTX 40 plus global DLSS overrides: https://www.nvidia.com/en-us/geforce/news/gfecnt/20258/nvidia-app-global-dlss-overrides-rtx-40-series-smooth-motion/
- PC Gamer, RTX 40 driver frame generation first tests: https://www.pcgamer.com/hardware/graphics-cards/rtx-40-series-graphics-cards-can-now-enable-frame-generation-in-unsupported-games-via-the-drivers-up-to-a-44-percent-fps-improvement-in-my-initial-tests/
- DLSS5-Feeder README (work_resolution, Smooth Motion, driver 616.x note): https://github.com/jlrouzies-fr/DLSS5-Feeder
- dlss5-bridge README: https://github.com/NIGos/dlss5-bridge
- MFGAdaUnlock-RenoDx README: https://github.com/mavismmg/MFGAdaUnlock-RenoDx/
- dlss5mod.com install guide (ShortFuse addon settings): https://dlss5mod.com/guides/install
- igorslab, "Install DLSS 5 with ReShade": https://www.igorslab.de/en/install-dlss-5-reshade-compatible-games/
- DSOGaming, DLSS 5 in every DX9 to Vulkan game: https://www.dsogaming.com/articles/heres-how-you-can-install-dlss-5-to-all-dx9-dx10-dx11-dx12-and-vulkan-games/
- RHI detailed guide (Smooth Motion bitfield, NvPresent64 mechanism): https://github.com/RankFTW/RHI/blob/main/docs/DETAILED_GUIDE.md
- Lossless Scaling 2026 guide (price, modes, borderless, HDR, dual GPU): https://shattered.io/lossless-scaling-setup-guide/
- PCGamingWiki community port report, XCOM 2 optimized settings: https://community.pcgamingwiki.com/blog/features/port-reports/pc-report-xcom-2-optimized-video-settings-for-quality-and-performance-r193/
- GamingBolt, XCOM 2 PC visual analysis (MSAA 8x): https://gamingbolt.com/xcom-2-pc-visual-analysis-un-optimized-performance
- NVIDIA forum, RTX HDR and Smooth Motion flicker: https://www.nvidia.com/en-us/geforce/forums/support/559146/rtx-hdr-smooth-motion-flicker/

Unread (403 or rate-limited): Nexus "Applying RR and DLSS 5 RenoDX" (mods/site/2224), Nexus RHI page, PCGamingWiki main XCOM 2 page, Steam guides 1377951450 and 620508289, Prima Games. Steam guides open in Idi's browser if he wants the old ini lists.
