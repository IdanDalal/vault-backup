---
type: reference
created: 2026-09-11
author: jep
project: XCOM 2 WotC campaign
status: active
---

# XCOM 2 handoff: black tactical scene, 2026-09-11 18:18 session

Paste-ready block for a fresh session. Everything below was verified by jep from files on this PC unless marked otherwise.

## Who and what

- Idi runs an XCOM 2 War of the Chosen campaign with 1,098 mods (AML launcher, `C:\XCOM2 AML 1.6.0-beta`, database `settings.json`) and 200 custom soldiers. Campaign 17, Legend, Second Wave with Beta Strike, Ironman off by design, reload-heavy puzzle style.
- jep (Claude Code on this PC, user `jep`) has read access to `C:\Users\Idi\Documents\my games\XCOM2 War of the Chosen\XComGame` (Config, SaveData, Logs, CharacterPool) and read access to the game install and workshop folders. jep cannot write to the game install, the launcher folder or the Documents folder: the safety classifier refuses. Fixes are staged in `D:\work\vault\projects\XCOM\fixes\` and Idi copies them into place.
- Rules: never hand Idi a shell or git command; one ask per message; verify before asserting; reports land in `D:\work\vault\projects\`.
- Prior work: `projects/xcom-sitrep-2026-09-10.md`, `projects/xcom-log-triage-2026-09-11.md`, `projects/xcom-playstyle-and-collab-2026-09-11.md`.

## State reached today

- Launcher: zero missing dependencies (was 285; 16 workshop IDs set as ignored dependencies, all superseded, BETA-vs-stable, or soft).
- `jepFixes` config-only mod live in the game's local `Mods` folder; its 8 corrected cosmetic entries import with zero errors. The broken originals in two workshop mods still log 1,198 redscreen lines per session (engine re-parses them); harmless noise unless the workshop files are edited by hand.
- Menu and Avenger render. First tactical map (Plot_WLD_Compound_Road_Ravine, Rescue the Prisoners, Skirmisher squad) renders black: only cover outlines, unit flags, HUD, and a beige outline pass on a tree draw; soldier bodies invisible. Screenshot: `D:\work\screens\XCOM-BLACK.png`. Idi quit at once.

## Evidence, ranked

1. **RenoDX + ReShade, prime suspect.** `Binaries\Win64` holds ReShade 6.8.0 (`dxgi.dll`, 2026-08-02), `renodx-xcom2.addon64` v0.2026.221.951 (2026-08-30 11:45), `renodx-dlss.addon64` (2026-08-31). This session's `ReShade.log` (28 MB): 132,421 lines tagged RenoDX, of which about 132,000 are `OnCopyTextureRegion(mismatched ... typeless vs float)`. That is RenoDX upgrading the game's render targets to float for HDR while the game copies scene buffers in the original format: a mechanism that blacks the scene and leaves the UI intact. The DLSS add-on reports `nvngx.dll`, `nvngx_dlss.dll` and `sl.interposer.dll` not found, hooks incomplete; DLSS cannot apply to this DX11 game. The preset (`ReShadePreset.ini`, unchanged since 08-31 18:49) enables one technique: `lilium__hdr_and_sdr_analysis`, a diagnostic overlay. `ReShade.ini` was rewritten at 17:52 today; `[renodx] SettingsMode=2`. The engine config carries `DefaultPostProcessName=XComEngineMaterials.DefaultScenePostProcess_NoTonemap`, the HDR-mod style setting. The only prior crash (2026-08-30 11:50, in the shell) came five minutes after `renodx-xcom2.addon64` was placed. Unknown: whether the 08-30 and 08-31 tactical turns rendered correctly with the same add-ons (autosaves at Mission 1 turns 4 to 6 exist, so Idi played turns).
2. **Config reset today.** Idi set default game options; `Config\XComEngine.ini` was regenerated at 17:48. Current values: 3840x2160 fullscreen, MaxQuality on, shadows 16 to 4096, DetailMode 2, AO and DoF on, texture streaming on, `PoolSize=10`. Nothing looks black-inducing by itself; relevant only if test 1 clears ReShade.
3. **Texture streaming and lighting.** 175 `TextureStreaming: About to request a -1 offset ... size=0` warnings against base-game caches (`World_XPACK_.tfc`, `Lighting_XPACK_.tfc`, `Textures-a_XPACK_.tfc`; all 21 tfc files dated 2026-07-27, sizes normal), one `Corrupt texture XComEngineMaterials.borderGradientDashed`, and `Can't find file 'WOTCCustomLightingMaps'`. Five lighting or weather mods are active: More Environmental Lighting Maps (908638853), DLC Lighting Maps (3325332092), Tunnel and Abandoned Lighting Maps (3306304260), Cloud Shadows (3337833717), Aquilio's Weather Pack (3326284263). Baseline unknown: the 08-31 log was rotated away today, so these may be old noise.
4. **Invisible bodies.** Tactical phase logs 117 `Can't find file for package 'wotc_grimstylearmor_WG'`. GrimStyle Armor was removed from the launcher in August; pool outfits still reference its parts. Invisible Body Parts For All is also active. Likely the missing soldier bodies, independent of the black scene.
5. **Other log facts.** `MW2ShadowCompany.u` in mod 3243288407 "contains unrecognizable data" (corrupt download, re-download the mod). `HareWackySkills_ModShaderCache.upk` missing in 3316181502. Materials failing to compile for SM4 and falling back to default: KatanaPkg wraith overlay, Chryssalid pupa transition. Launch args: `-review -noRedScreens -noStartUpMovies -allowConsole -USEALLAVAILABLECORES -malloc=system -refresh 120`.

## Test order for the new session

1. Launch once with ReShade out of the chain (rename `dxgi.dll` in `Binaries\Win64` to `dxgi.dll.off`, Idi's action), load the Campaign 17 tactical autosave, look. Scene renders: the fault is inside ReShade or RenoDX; proceed to 2. Still black: restore the DLL, go to 4.
2. With ReShade back, remove `renodx-dlss.addon64` (it cannot work here) and launch. Then, if still black, move `renodx-xcom2.addon64` out and launch. Then, if RenoDX HDR is wanted, check its settings in the ReShade overlay (the overlay key is code 220, the backslash key, per `KeyOverlay=220`) and turn off the lilium analysis technique.
3. If RenoDX HDR stays out, revert `DefaultPostProcessName` to `XComEngineMaterials.DefaultScenePostProcess` in the engine config, or confirm which mod sets it (grep the workshop configs for `_NoTonemap`).
4. Steam: verify integrity of game files (clears the tfc streaming warnings if they are real damage). Then disable the five lighting and weather mods together, launch, look.
5. Once the scene renders, inspect soldier bodies. If invisible: re-subscribe [WOTC] GrimStyle Armor (workshop ID 1128848767, present in the March database, removed in August) or re-outfit the affected soldiers in the pool.
6. After every launch jep reads `Logs\Launch.log` and the ReShade log and reports the delta against this session: redscreen lines 1,875, RenoDX warnings 132,421, -1 offset warnings 175.

## What jep rebuilds in the new session

Scripts from this session lived in a temporary job folder and are gone. Rebuild on demand: redscreen pattern counter for `Launch.log`, dependency checker for `settings.json`, staged-candidate generator for launcher edits. Each is under 60 lines of Python.

## Findings, 2026-09-11 evening session (jep, all from files on this PC)

- Test 1 DONE by Idi: `dxgi.dll` renamed, launch 18:39, tactical still black. `Launch.log` of that run: zero ReShade/RenoDX lines, `ReShade.log` untouched since 18:18, redscreens 1,874 vs 1,875. **ReShade and RenoDX cleared.** Idi restored the DLL (non-negotiable for the campaign).
- `_NoTonemap` CLOSED: it is the shipped default. `XComGame\Config\DefaultEngine.ini` lines 38 and 40, file dated 2026-07-27 17:26 (install day), no mod overrides it. Never revert it.
- `Can't find file 'WOTCCustomLightingMaps'` CLOSED: script-package probe for a content-only mod (Aquilio's Weather Pack, 3326284263, ships no `.u`). Same line appears for `WOTC_Clouds`. Noise.
- `-1 offset` texture streaming warnings: 200 this run, first at log time 0355 (Avenger phase, which renders). Not tactical-specific. Weak suspect.
- Renderer facts: `Using D3D11 adapter: NVIDIA GeForce RTX 4090`, RHI `PC-D3D-SM4`, 24,142 MB VRAM. Seven mod materials fail SM4 compile (Muton Devastator grenade x2, Katana wraith overlay, Skyranger skin, Chryssalid pupa x3). Base world materials compile.
- **Discriminator found.** Both black runs today: `Plot_WLD_Compound_Road_Ravine`, biome `Xenoform` (log `XCom_Maps:` line, save headers of `Campaign 18, Mission 1, Turn 1` and `Operation Gatecrasher_1`). The 08-31 session that rendered (turns 4 to 6 played): same plot, biome `Arid` (save headers of `Campaign 17, Mission 1, Turn 4/5/6`). Xenoform on wilderness is legal in base WotC (`DefaultPlots.ini` line 222, `DefaultGameData.ini` line 998, chance 33). Base ships `EnvLighting_Day_Xenoform.upk` and `EnvLighting_NatureNight_Xenoform.upk`. Mods add Wilderness+Xenoform lighting maps: Cloud Shadows 3337833717 (`EnvLighting_Day_Xenoform_CLD.upk`), Aquilio's Weather Pack 3326284263 (16 maps, e.g. `EnvLighting_Contact`, `EnvLighting_Saudade`), DLC Lighting Maps 3325332092. Which map was picked is not logged and the save body is compressed.
- **Changed since 08-31, in the environment**: NVIDIA driver installed 2026-09-04 08:56 and again 2026-09-07 05:13 (DriverStore `nv_dispi.inf_amd64_436833bbb0f00476`, `..._a3944b54ff18b284`; live 32.0.16.1664 dated 2026-08-24; previous driver folder `..._c8bc842500fab35b` from 06-20 still present). Options reset 17:48 today. Ten workshop mods updated 09-11 16:10 to 16:54 (ClausCompendium, qUIck_FLG, EggsaltAndBradford, Augments x3, MultipleFactionSoldierClasses, HunterRifles, two voice packs): cosmetic, UI, class, weapon, voice; none touches maps or lighting. 378 workshop files updated since 09-01, including map mod 3720645826 (LargeScout plots, not this plot).
- Next test (recommended): load `save_AUTOSAVE- Campaign 17, Mission 1, Turn 6` (08-31, Arid, same plot). Renders: fault is mission-instance specific, Xenoform lighting map from a mod; disable Cloud Shadows + Aquilio's Weather Pack + DLC Lighting Maps and start a fresh campaign. Black: fault is global; then video preset Low (bisect options) before any driver rollback (Device Manager, previous driver present).
- Tools rebuilt this session: none saved; all probes were one-line greps recorded above.

## Findings, 2026-09-12 morning (jep; screenshots `D:\work\screens\XCOM\MENU1.png`, `MENU2.png`, `CHARACTER.png`, log opened 08:55:38)

- Idi did not load the Campaign 17 save (missing-mods warning). Menu shell 1 (factory): environment lit, every MEC and soldier a pure black silhouette. Menu shell 2 (alien, no characters): perfect. Character pool: room, rifle and visor render; soldier body black, half-transparent, rim highlight only.
- **Unifying read: dynamically lit surfaces render black, baked and emissive surfaces render.** Shell and pool worlds are lightmapped; soldiers everywhere and the assembled tactical map are lit by dynamic lights. One cause covers all four screenshots. Medium-high confidence on the pattern, cause still open.
- Live `[SystemSettings]` (regenerated 09-11 17:48): `bUseMaxQualityMode=True`, `bEnableVSMShadows=True`, `DynamicShadows=True`, `ShadowFilterQualityBias=5`, `MaxShadowResolution=4096`, `bAllowWholeSceneDominantShadows=True`, 3840x2160. Engine base `BaseEngine.ini` ships `bUseMaxQualityMode=False`, `DynamicShadows=False`. Game `DefaultEngine.ini` sets none of them; no mod config touches `SystemSettings`. So the in-game options wrote them (the 17:48 reset on a 4090 lands on the top preset). If the dominant light's shadow pass fails at these settings, lit surfaces go fully shadowed: black. Cheapest test available.
- Base-package override scan (8,158 base files vs every workshop and local mod file): only 1796402257 Community Highlander ships `Core.upk`, `Engine.upk`, `XComGame.upk`, by design; its files are dated 2026-09-09 (updated after the last good session, v1.31.2 per the menu).
- Streaming `-1 offset` warnings this run: 90, top packages `AvengerExteriorDeck` 20, `Hair` 12, character faces and `Aviators`. `RemoveNetObject` duplicate NetIndex errors: 3,966, led by `Soldier_ANIM` 1,341, `DLC_3_FX_Arsenal` 496, `Hair` 54, base `Materials`. No baseline log survives (08-30 crash log is 189 lines), so unknown whether these are new. `Corrupt texture borderGradientDashed` was already present 08-30: old noise.
- Eleven mod `.u` script files "contain unrecognizable data" (voice packs and cosmetic packs, IDs 3049233226, 3012107571, 2998577461, 3516872904, 3243288407, 2948960636, 3340667510, 2971971626, 2856167395, 3311763067, plus `HareWackySkills_ModShaderCache.upk` in 3316181502). Corrupt downloads; unrelated to lighting, worth re-downloading later.
- Ranked causes: 1 graphics settings written by the reset (test: preset Low in Options, check the pool). 2 NVIDIA driver installed 09-04 / 09-07 (test: Device Manager roll back, previous driver folder still present). 3 Highlander 09-09 update or a mod shader cache (test: AML profile with all mods off, or Steam verify integrity for base shader caches).
- Image sharing rule for Idi: PNG or JPEG makes no token difference; only pixel size counts and every image is downscaled to about 1.5k px before jep sees it. Leave files as they are, name the folder; jep crops at full resolution when detail matters.

## RESOLVED 2026-09-12 (Idi): Depth of Field

- Preset Low fixed it; Idi raised every setting back one by one; **Depth of Field on = black dynamically lit surfaces**. DoF off, everything else at maximum, shells + Gatecrasher save checked, no flaws. Untested: whether DoF breaks alone or only together with ReShade/RenoDX or the 09-04 driver; keep DoF off and move on.
- Rank A above (settings written by the 17:48 reset) was the cause. B (driver) and C (Highlander) never tested.

## 2026-09-12 afternoon: shell defects, cleared and open

- Symptoms (Idi, in motion): soldier silhouette shadows stamped on distant surfaces in every shell, moving with the soldier; Lost shell missing fire escapes, props and a character floating. jep misread these as texture damage; corrected by Idi.
- CLEARED by test: ReShade off; Shadow Quality Low; `bUseMaxQualityMode=False`; NVIDIA driver 610.88 clean install (still broken). Steam verify running at time of writing.
- Mod-side facts: 42 mods changed since 08-31. 09-01: 3 map mods. 09-09 17:42 Steam sync: 20 (Highlander BETA 1796402257 v1.31.2, DLC2 Highlander, WOTC_AlienPack 34 files, AHWRequiemArmory, ClausCompendium, MeristPerkPack + Redux, WotCBallisticShields, TacticalUI_REDUX, MultipleSitreps_REDUX, CommanderHere_REDUX, WOTCStrategicShortcuts, WOTC_BD_RemoveMissingModsRedux, WOTC_BD_PoseListFixer, SmallMapsRemoval, AvatarPsiAmp, AHarderWarAbsurdAliens, ImmolatorChemthrower). 09-11 16:10 to 16:54 (before the first bad run 17:45): qUIck_FLG, EggsaltAndBradford, Augments x3, MultipleFactionSoldierClasses, HunterRifles, two voice packs. Local `jepFixes` added 09-11 15:48. StyrPerkPack 09-11 21:43 (after). Eleven packs re-downloaded 09-12 10:06 to 10:16 and still "unrecognizable data": built for another game version, not corrupt downloads (jep's earlier label wrong).
- Config scan of all changed mods: only `[Engine.ScriptPackages]` and `[Engine.Engine]` ModClassOverrides; no light, shadow, cutout or visibility keys. Highlander 1.31.2-beta notes (09-05): inventory slot, RemoveEffect events.
- Plan: first cut = disable the 30 pre-run changes (3 + 18 + 9, keeping both Highlanders) plus jepFixes, one launch. Clean: bisect those 31 (5 launches). Still broken: AML profile with only the two Highlanders on, then bisect all.

## RESOLVED 2026-09-12 evening: shell shadows and missing geometry = hand edits in XComEngine.ini

- Idi's hypothesis. Layered diff (BaseEngine + DefaultEngine vs live) found 42 hand-edited `[SystemSettings]` lines: foreground shadows on world, VSM, PCF, hardware shadow filtering, ShadowFilterQualityBias=37, ShadowTexelsPerPixel=8, pre-shadow factors, HighPrecisionGBuffers, and every TEXTUREGROUP forced to MinLODSize 4096 (the source of the "-1 offset" streaming warnings). Corrected file: `projects/XCOM/fixes/XComEngine.ini` (85 diff lines vs `XComEngine.ini.bak-2026-09-12`); Idi copied it in. Shells clean.
- jep cannot write into Documents (classifier + junction refusal); fixes go through `projects/XCOM/fixes/`.

## 2026-09-13 09:23 crash while choosing legs in the character pool

- Windows Error Reporting: XCom2.exe 1.0.0.10381, exception 0xc0000409 (fast-fail), fault offset 0x10a3b7c in the exe. Dump under ProgramData WER is unreadable to jep. Two earlier XCom2 crash reports 09-12 10:28.
- Log tail: dozens of `Failed to load 'wotc_grimstylearmor_WG'` while previewing parts from `wotc_grimstylearmor_extra`, then `Attempting to detach NULL component` on every preview, invalid NetIndex on Central and AvengerEngineer parts (Repurposed Gear 1132838346), last line a CombatKnives loader redscreen (benign).
- Cause found: Vanilla and Kitbash Redux (3736573340) ships `wotc_grimstylearmor_extra.upk` whose parts import from `wotc_grimstylearmor_WG`, the package of the original GrimStyle Armor mod 1128848767, which is not installed (removed in August). 96 config entries point at the extra package. Fix A: re-subscribe 1128848767. Fix B: disable the Redux mod.
