---
type: research
created: 2026-11-14
author: Agent g3b-unlock-reception
---

# GPU tensor unlock (gpu-unlock-ada): public reception, 3 weeks in

Scope: what other people report. Sources read: 4 news articles, 11 Reddit threads (Arctic Shift archive, up to 100 comments each), titles of 149 GitHub issues and pull requests (numbers 1 to 151) plus the opening text of the ones that report a result or a failure. Repository code, build files and setup documents were left unopened. No procedure is reproduced here.

Confidence tags: high = several independent sources agree, or a controlled measurement with method stated. medium = one credible source, or several uncontrolled ones. low = single anecdote or my inference.

## Verdict for this reader (three lines)

1. Workload A (10 s per picture, 8-bit integer weights, 4-bit text encoder): expect 0 to 5 percent, about 0 to 0.5 s per picture. Integer-weight pipelines measured +0.3 %, +4.6 %, +5.3 % and 0 % on four separate tests. Confidence medium.
2. Workload B (55 s per picture, limited by system RAM and disk streaming): expect about 0. The unlock changes one kind of GPU arithmetic and touches nothing in memory or disk transfer. Nobody measured this exact case. Confidence medium-high on "near zero".
3. Risk on this PC: a boot-time USB application that is tied to an exact card model, firmware version and motherboard, needs Secure Boot off and Fast Startup off, and must run again after every cold boot. On a machine with recent blue screens, any new crash becomes impossible to attribute. **Recommendation: skip.** Revisit only if he moves to 16-bit float workflows (BF16, FP16, FLUX fp8, GGUF video models), where 14 to 59 percent was measured on other cards.

## 1. What independent writers say it does

| Point | What the source says | Source | Confidence |
|---|---|---|---|
| The limit | GeForce tensor cores (the matrix-multiply units used for AI math) run one mode at half rate: 16-bit inputs (FP16, BF16) with results summed in 32-bit (FP32 accumulation). Workstation cards on the same chip run it at full rate. | TechSpot [S1] | high |
| Where the limit lives | A factory-set fuse value read at boot says "half speed" for that mode on consumer cards. An override setting exists and is locked to NVIDIA's most privileged firmware. | r/StableDiffusion explainer by panchovix, 433 points [S5]; GameGPU [S3] | medium (one technical author, one outlet repeating it) |
| Why it was unavailable | Market segmentation between GeForce and workstation lines. TechSpot: the cap appears in NVIDIA's own spec sheets. | [S1], [S5] | high on the cap existing, medium on motive (writers' reading, no NVIDIA statement) |
| How the unlock gets in | A flaw in a small NVIDIA-signed boot firmware lets the unlock set the override to full speed before the normal driver starts. No VBIOS flash, no driver patch. Credited to a June 2026 paper by Jon Pry, "A Canary in the Crypto Mine" (I did not open the paper). | [S5], [S3], [S1] | medium |
| What stays the same | Clocks, voltages, power limit, core count, VRAM. One Reddit commenter describes the limiter as inserted idle gaps between instructions. | [S5] and comments | medium |
| RTX 50 series | Same fuse scheme, different boot security chain; no unlock exists. | [S5], [S3] | medium |
| Lineage | First release: Zagitta's gpu-unlock for RTX 30 (Linux). gpu-unlock-ada is the RTX 40 port. A third project covers RTX 20. | [S1] | high |

## 2. Real workloads: measured before and after

### 2a. Microbenchmarks (kept apart from end-to-end)

| Test | Stock | Unlocked | Hardware, who | Source |
|---|---|---|---|---|
| Raw instruction rate, FP16 in / FP32 sum | 165.6 TFLOPS | 331.6 | RTX 4090, project author | [S1], [S7] #67 |
| Same, independent owner | 163.2 | 326.4 | RTX 4090 MSI Suprim Liquid X, Linux | [S7] #111 |
| Real matrix multiply (cuBLAS, NVIDIA's math library), FP16 | 115.5 / 163.1 / 170.8 | 138.9 / 209.1 / 191.8 (+20 / +28 / +12 %) | same card, three matrix sizes | [S7] #111 |
| Real matrix multiply, BF16, largest size | 148.45 | 150.21 (+1.2 %) | RTX 4090, Linux | [S7] PR #45 |
| Windows, raw instruction rate | 149.2 | 297.6 | RTX 4090 Founders Edition, MSI B650 board | [S7] PR #104 |

TechSpot's summary: the doubling is a raw issue rate; real matrix workloads on an independently owned 4090 gained 12 to 34 percent [S1]. Confidence high.

### 2b. End-to-end image and video generation

| Workload | Stock | Unlocked | Change | Hardware, OS | Who, method | Source | Conf. |
|---|---|---|---|---|---|---|---|
| MOSS-Image BF16, 50 steps | 71.98 s | 45.40 s | +58.6 % throughput | RTX 3090 Ti, Linux, ComfyUI 0.42.1 | Reddit user under-_-null; 15 images per state, 3 warmups, identical pixels | [S4] | high |
| MOSS-Image INT8 | 27.31 s | 27.23 s | +0.3 % | same | same | [S4] | high |
| Qwen-Image 2.1 Turbo BF16, 8 steps | 8.51 s | 5.41 s | +57.2 % | same | same | [S4] | high |
| Qwen-Image 2.1 Turbo INT8, 8 steps | 3.92 s | 3.75 s | +4.6 % | same | same | [S4] | high |
| FLUX.1 dev fp8 file (computed in BF16) | 31.96 s | 20.66 s | +54.6 % | same | same | [S4] | high |
| MiniMax H3 video, INT8 ConvRot | 155.07 s | 118.21 s | +31 % | same | same; sampling 143.7 to 106.9 s, rest unchanged | [S4] | medium (one run set) |
| Qwen-Image 2.1 INT8 ConvRot + INT8 text encoder, 25 steps | 72.73 s | 68.90 s | +5.3 % | RTX 4070 Ti SUPER, **Windows 11** | issue reporter, same workflow A/B | [S7] #92 | medium |
| FLUX.1 dev fp8, 20 steps | 22.1 s | 16.1 s | +37 % | RTX 4070 Ti SUPER, MSI Z790, **Windows** | PR author, one run per state | [S7] PR #149 | medium |
| Wan2.2 video, GGUF Q4_K_S | 66.2 s | 46.2 s | +43 % | same | same | [S7] PR #149 | medium |
| LTX-2.5 INT8 video | 14.1 s | 12.4 s | +14 % | same | same | [S7] PR #149 | medium |
| SDXL, 27 steps | 7.94 s | 6.06 s | 1.31x | RTX 4080 SUPER, Linux | issue reporter, 6 runs per state | [S7] #74 | high |
| Z-Image Turbo, Q6_K GGUF, BF16 compute | 9.445 s | 7.564 s | 1.25x | RTX 4070, Linux | issue reporter, 10 images per state | [S7] #124 | high |

### 2c. End-to-end on an RTX 4090 specifically

| Workload | Stock | Unlocked | Change | Who, method | Source | Conf. |
|---|---|---|---|---|---|---|
| FLUX.2 Klein 9B text-to-image | not given | not given | +0.2 % per image | owner, Linux, matched pairs | [S7] #111 | medium |
| MiniMax H3 video, INT8 ConvRot, ComfyUI | 55.54 s | 55.81 s | 0 % | Reddit user Friendly_Olive5460 | [S5] comment | medium |
| Wan2.2 video, FP16 weights, ComfyUI | 139.83 s | 138.37 s | +1 % | same | [S5] comment | medium |
| MiniMax H3 video, BF16 with offload | 309.6 s | 267.3 s | 13.7 % less time | PR author, Linux, identical outputs | [S7] PR #45 | medium |
| MiniMax H3 pruned INT8, 15 s clip | 240 s | 179 s | 25 % less time | Reddit user BitterFortuneCookie, Linux | [S5] comment | low (no method) |
| ComfyUI, unnamed workflow | 26 s | 16.31 s | 1.6x | owner, states it is uncontrolled | [S7] #110 | low |
| SDXL image, Windows | about 4 s | about 3.5 s | 12 % less time | Reddit user Wanabeelee2 | [S6] comment | low |
| BF16 "Anima" image model, Windows | not given | not given | about 10 % | Reddit user Relevant-Dentist-733 | [S5] comment | low |

Spread on the 4090: 0 % to 1.6x, and the two highest figures have no stated method. Explanation offered by Reddit user fallengt (tested several setups): integer and 4-bit pipelines gain only when the attention step runs through plain PyTorch; with the fast attention backends most ComfyUI users enable (Comfy Kitchen, SageAttention with FP16 accumulation) they gain nothing [S5]. Confidence medium.

### 2d. Language models and training

| Workload | Result | Hardware | Source | Conf. |
|---|---|---|---|---|
| Transformer training, BF16 | +8.8 % (15,821 to 17,218 tok/s) | RTX 4090, Linux | [S7] #102 | medium |
| Small transformer training | +7.7 % (power-capped) | RTX 4090, Linux | [S7] #111 | medium |
| LoRA training, H3 INT8 model | +3 % (6.34 to 6.15 s/it) | RTX 4090 | [S5] comment | medium |
| llama.cpp, 8-bit quantized 27B: prompt processing | +0.9 %; generation unchanged | RTX 4090 | [S7] #111 | medium |
| llama.cpp-type engine, 3-bit quantized 79 GB model partly in system RAM | 0.98x (no gain) | RTX 4090 48 GB mod | [S7] PR #21 | medium |
| vLLM server, 4-bit float checkpoint, prompt processing | +20 to 22 % from the unlock alone (plus +20 % from a raised power cap) | 4x RTX 4090 48 GB, production traffic, control cards | [S7] #81 | high |
| Claimed 2.0 to 2.7x generation speed | retracted by its own author (baseline ran under other load) | RTX 4090 | [S7] #79 | high |
| Token generation in general | "hardly move", memory-bandwidth bound; prompt processing +14 to 36 % | outlets' summary | [S1] | high |

## 3. Which number formats benefit

| Format or situation | Effect | Source | Conf. |
|---|---|---|---|
| FP16 or BF16 inputs with 32-bit summation | up to 2x raw; 12 to 34 % in real matrix math on a 4090 | [S1] | high |
| TF32 (NVIDIA's reduced-precision 32-bit mode) | about 2x raw; +73 % real matrix math on a 4090 | [S7] PR #45 | medium |
| FP8 (8-bit float), RTX 40 only | 2x raw; 1.44 to 1.63x real matrix math on a 4090 | [S7] #65 | medium |
| FP16 with 16-bit summation | unchanged (already full rate) | [S7] #108 | medium |
| INT8 and INT4 tensor math | unchanged: 1.01x control | [S7] #65, [S5] | high |
| Plain FP32 on ordinary cores | unchanged | [S5], [S7] | high |
| Models stored as 8-bit integers (INT8, ConvRot) | 0 to 5 % in 4 of 6 tests; +14 % and +31 % in two video pipelines whose attention or audio parts still run in float | [S4], [S7] #92, PR #149 | medium |
| Models stored as 4-bit GGUF | depends on the math at run time. GGUF image and video loaders convert weights to 16-bit float before multiplying, so they can gain (+25 % Z-Image Q6, +43 % Wan2.2 Q4) when the GPU is the limit. Integer 4-bit paths gain nothing. | [S5], [S7] #124, PR #149 | medium |
| Workloads limited by memory transfer | no change. "If your process is memory bound, this isn't going to help" (Reddit); 79 GB model partly in system RAM: 0.98x | [S6] comment, [S7] PR #21 | medium-high |
| Games | no change | [S1], [S5] | high |

## 4. Windows 11 with an RTX 4090

| Report | Board | Result | Limits stated by the reporter | Source |
|---|---|---|---|---|
| MSI RTX 4090 Suprim X, i9-13900K, Windows build 26200, driver 617.14, Secure Boot off | MSI MEG Z790 GODLIKE | One run completed, Windows started, raw rate above stock ceiling | No matched stock run; "one-system reference", author plans no support; lives in a third-party repository | [S7] #43 |
| RTX 4090 Founders Edition, driver 610.88 | MSI MAG B650 Tomahawk WiFi | One cold manual run; raw rate 149.2 to 297.6 | One short run; return to stock after power-off unchecked; a Windows update replaces the boot file the port pins | [S7] PR #104 |
| RTX 4090 Laptop, Windows 11 build 26300 | MSI Raider GE78HX | FP16 +85 % | Earlier runs reached Windows and fell back to stock speed; held only after runtime power-down was switched off for the card | [S7] #117 |
| RTX 4090 Laptop | Alienware m18 R1 | 2.00x raw | Local build | [S7] #132 |
| MSI RTX 4090 Suprim Liquid X, i9-14900KF | MSI MEG Z790 ACE | Request for help; no result in the opening text | | [S7] #95 |
| Two Reddit users, desktop 4090 on Windows | not named | "about 20 % on BF16", "about 10 %" | No method; one used an AI-modified port | [S5], [S6] comments |

Counts: 22 of 92 issue titles mention Windows or UEFI; 2 desktop RTX 4090 Windows runs are documented, each a single run on one board. Confidence high on the count, low on generality.

| Question | Finding | Source | Conf. |
|---|---|---|---|
| Board dependence | "All currently released Windows unlockers only run on exact board models + ROM combinations"; another board needs a port. A separate "universal" UEFI tool exists; Notebookcheck says RTX 40 support still awaits user confirmation. | [S6] thread, [S2] | medium |
| Survives reboot | Lost at power-off; must run again each cold boot from a USB stick. One Linux multi-GPU report saw the unlocked state persist across power cycles, which contradicts this. | [S5], [S2], [S8]; [S7] #55 | medium |
| Survives driver updates | One Windows report (RTX 4070 Ti SUPER) held the same ratio across drivers 610.88, 621.14, 621.24. No report of a driver closing it. Reddit users are holding back updates as a precaution. | [S7] PR #149, [S6] thread | medium |
| Sleep | Untested in every report that mentions it; "genuine sleep recovery remains unqualified" in one Windows write-up. | [S7] #92, #64, #74 | high that it is untested |
| Other Windows conditions | Secure Boot off (breaks anti-cheat games that require it), Fast Startup off, BitLocker off in the tested setup. | [S2], [S7] #92 | medium |

## 5. Failures and risks reported

Counted from 149 issue and pull-request titles, their opening text, and 11 Reddit threads. Issue comments were not read, so counts are floors.

| Kind | Count | Detail | Source |
|---|---|---|---|
| Dead or permanently damaged card | 0 | None attributed to the unlock. One Reddit comment ("just lost my 3090 a few weeks ago") gives no cause. | [S6], [S7] |
| Blue screen or system crash | 0 | One Windows user states "no blue screens, crashes or freezing". | [S6] |
| Card temporarily lost | 1 | One RTX 4090 in an 8-GPU Linux server vanished from the driver after the unlock sequence re-ran on cards already in the unlocked state; it returned after a full power cycle and a BIOS change. | [S7] #55 |
| Unlock ran but speed stayed at or fell back to stock | 4 | RTX 4090 Laptop (Clevo), RTX 4070 Laptop, RTX 4050 Laptop, RTX 4090 Laptop on Windows (later fixed). All laptops, all tied to power-saving states. | [S7] #4 via #132, #87, #130, #117 |
| Unlock failed to apply | 3 | Ubuntu load-order failure every boot; two "target not matched / how to make it work" reports. | [S7] #112, #22, #131 |
| Build or install failure | 3 | openSUSE build; a pinned download returning 404 (two reports). | [S7] #30, #145, #146 |
| Performance claim withdrawn or below expectation | 2 | 2.0 to 2.7x claim retracted; BF16 matrix math flat on RTX 4090 D. | [S7] #79, #90 |
| "No gain for me" on Reddit | 4 | RTX 3070, RTX 3090 (two users), RTX 4090. | [S5], [S6] |
| Success-type issue titles, for scale | about 38 | Matched stock/unlocked numbers on 4050 through 4090. | [S7] |

| Risk | What is reported | Source | Conf. |
|---|---|---|---|
| Failed boot-time run | Two Windows port authors write that a failure after the change starts "may deliberately halt with no display until power is removed", and call it an unresolved safety limitation. A failed run needs a full power-off before retry. | [S7] #107, #139; [S5] | medium |
| Heat and power | Card draws more under the same cap because it does more work: 313 to 346 W (4090), 316 to 339 W and 63 to 66 C (4080 SUPER), 227 to 292 W (4070 Ti SUPER). Reddit: 2 to 3 C. Cards then sit at their power cap. | [S5], [S7] #74, [S2] | high |
| Hardware damage | Zagitta calls it "very unlikely" because throttling and power management stay active. The RTX 20 project warns that sustained full-rate use "may damage hardware". | [S1] | medium (opinions, no data) |
| Long-term stability | Longest test runs found: a 10-minute matched soak and about 30 minutes of load. Production report: 4 cards, 8 hours, zero driver errors. No multi-week data. | [S7] #106, PR #21, #81 | high that long-term data is absent |
| NVIDIA statement | None found in four articles and two searches. | [S1], [S2], [S3], [S8] | medium |
| NVIDIA closing it | Not reported. Writers name two ways it could happen: a driver that refuses the change, or a one-way fuse update. | [S5] | medium |
| Warranty, licence | No source read discusses either. The method runs an exploit against NVIDIA's signed firmware. | [S3], [S5] | low (absence of coverage) |

## 6. Verification, hoax and malware signs

| Check | Finding | Conf. |
|---|---|---|
| Outlets covering it | TechSpot, Notebookcheck, TweakTown, PC Games Hardware, GameGPU, Pureinfotech. | high |
| Outlets that ran their own test | None of the four I could read. All relay developer and user numbers. TweakTown and PCGH pages were unreadable (blocked). | medium |
| Independent replication | About 38 success-type owner reports in the issue tracker, many with matched stock/unlocked numbers; a 15-image-per-state ComfyUI test on Reddit with identical output pixels; outputs reported bit-identical in at least 6 reports. | high that the raw-rate change is real |
| Disputes | The dispute concerns size of real-world gain. TechSpot, Reddit testers and the project's own caveats agree that application gains are far below 2x. One Reddit title says the Zagitta result was "confirmed by KohakuLab and ComfyUI" (image only, unverified). | medium |
| Malware reports | None found (one search). | low on absence |
| Caution signs | At least 6 third-party forks and Windows ports by different authors, several written or adapted with AI assistants; one promotional r/LocalLLaMA post removed by the spam filter; an AI-assembled benchmark site that states it ran no tests; issue-tracker posts from content promoters. In 2022 a fake "RTX LHR unlocker" on GitHub was malware. | medium |
| Paid unlock tools | None found. | low on absence |

## 7. Verdict detail

| Item | Estimate | Basis | Conf. |
|---|---|---|---|
| Workload A sampling (about 4 s, 8-bit integer weights) | 0 to 0.2 s saved | INT8 pipelines: +0.3 %, +4.6 %, +5.3 %, 0 % | medium |
| Workload A text encoding (about 6 s, 4-bit encoder) | 0 to 0.3 s saved; unmeasured by anyone | If it is a GGUF file converted to 16-bit float it could gain a little; if it waits on memory it gains nothing | low (my inference) |
| Workload B | about 0 s saved | Memory-bound and disk-bound work is outside what the unlock changes | medium-high |
| Cost on this PC | Secure Boot off, Fast Startup off, a USB step at every cold boot, a port that must match his exact card firmware and motherboard, sleep untested | [S2], [S6], [S7] | medium |
| Interaction with the unstable CPU | No report links the unlock to crashes. A machine that already blue-screens removes the ability to tell a CPU fault from an unlock fault, and a failed boot-time run can leave no display until power is cut. | my inference from [S7] #107 | low-medium |
| Decision | **Skip now.** Re-check in 2 to 3 months if (a) he adopts BF16, FP16 or FLUX fp8 workflows that fit in VRAM, and (b) a Windows port for his exact board has multi-week reports. | | |

One free alternative mentioned in the threads for integer-weight users: stay on INT8, which several commenters call faster than unlocked BF16 on these cards [S4], [S6].

## Sources

- [S1] TechSpot news item 114351 (headline taken from the URL slug): https://www.techspot.com/news/114351-hackers-unlock-hidden-ai-performance-nvidia-rtx-20.html
- [S2] Notebookcheck, Bogdan Solca, 2026-10-30, "UEFI-level pre-driver Nvidia GPU unlocker now available for RTX 2xxx, 3xxx and 4xxx GPUs on Windows and Linux": https://www.notebookcheck.net/UEFI-level-pre-driver-Nvidia-GPU-unlocker-now-available-for-RTX-2xxx-3xxx-and-4xxx-GPUs-on-Windows-and-Linux.1438153.0.html
- [S3] GameGPU, Maxim Boldson, 2026-10-27, "NVIDIA has closed the option to remove hardware limits for tensor cores in the GeForce RTX 50 series": https://en.gamegpu.com/news/zhelezo/nvidia-zakryla-vozmozhnost-snyatiya-apparatnykh-limitov-tenzornykh-yader-v-geforce-rtx-50
- [S4] r/StableDiffusion, under-_-null, "I tested the RTX 30-series GPU Unlock: up to 59% higher throughput in ComfyUI (3090 Ti)" (137 points): https://www.reddit.com/r/StableDiffusion/comments/1xdoh8k/i_tested_the_rtx_30series_gpu_unlock_up_to_59/ (read via https://arctic-shift.photon-reddit.com/api/comments/search?link_id=1xdoh8k&limit=100)
- [S5] r/StableDiffusion, panchovix, "GPU unlocks (FP32 accumulation): Why can it be unlocked on Turing, Ampere and Ada but no consumer Blackwell and some misconceptions" (433 points), with comments by Friendly_Olive5460, fallengt, BitterFortuneCookie, Relevant-Dentist-733: https://www.reddit.com/r/StableDiffusion/comments/1xgacis/gpu_unlocks_fp32_accumulation_why_can_it_be/
- [S6] r/comfyui threads: "ELI5: the new RTX unlock everyone is talking about" https://www.reddit.com/r/comfyui/comments/1xeiumj/eli5_the_new_rtx_unlock_everyone_is_talking_about/ ; "Will RTX 4070 get unlocked for windows too" (1xghib8); "GPU Unlock for Nvidia Cards" (1xfwrm0); "Does the new 621.14 driver break the gpu-unlock AI throughput mod on Linux?" https://www.reddit.com/r/comfyui/comments/1xryxme/does_the_new_62114_driver_break_the_gpuunlock_ai/ ; "RTX40 series tensor performance unlock readiness tool" (1xi7xeo); "ComfyUI gpu-unlock timings: BF16 vs INT8" https://www.reddit.com/r/comfyui/comments/1xeprfe/comfyui_gpuunlock_timings_bf16_vs_int8_with/ ; r/LocalLLaMA 1xnjhiq and 1xthfpt
- [S7] GitHub issue and pull-request titles and opening text, JustAResearcher/gpu-unlock-ada, fetched 2026-11-14: https://api.github.com/repos/JustAResearcher/gpu-unlock-ada/issues?state=all&per_page=100 (items cited by number: #4, #21, #22, #30, #43, #45, #55, #64, #65, #67, #74, #79, #81, #87, #90, #92, #95, #102, #104, #106, #107, #108, #110, #111, #112, #117, #124, #130, #131, #132, #139, #145, #146, #149)
- [S8] Pureinfotech, "Windows 11 users can unlock more AI performance on NVIDIA RTX 20, 30, and 40 GPUs": https://pureinfotech.com/?p=193174
- Not readable (blocked to automated reads), cited for existence only: TweakTown https://www.tweaktown.com/news/114288/modders-unlock-nvidia-geforce-rtx-20-30-and-40-series-compute-limits-nearly-doubling-some-tensor-core-throughput/index.html ; PC Games Hardware https://www.pcgameshardware.de/Grafikkarten-Grafikkarte-97980/News/Nvidia-Geforce-RTX-Tensor-Unlock-Linux-KI-Leistung-1557737/
- Background on the 2022 fake unlocker: HotHardware https://hothardware.com/news/bios-unlocker-restore-crypto-mining-nvidia-rtx-30-lhr-cards (search result title only, page unopened)
