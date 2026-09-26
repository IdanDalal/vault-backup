# BIOS / stress-test photo transcription, 2026-04-20 to 2026-05-05

Machine per HWiNFO: IDI-PC, GIGABYTE Z790 AORUS ELITE AX, Intel Core i9-13900K (B0 stepping, MCU 12B, SSPEC SRMBH), BIOS F13b dated 12/04/2024, UEFI, Windows 11 Pro build 26200.8246 (25H2). RAM: 2 x 16 GB Kingston KF560C36-16 (DDR5-6000 / PC5-48000), running at 3000 MHz DDR clock (6000 MT/s), 36-38-38-80, tRC 118, tRFC 480, CR 2T, Quad-Channel. No BIOS setup pages are in this batch; the only BIOS screen is one Save & reset dialog.

Reading conventions: HWiNFO Sensors columns are Current / Minimum / Maximum / Average. The five 5 May afternoon photos share one continuous HWiNFO run (elapsed 2:34:12 to 2:35:24), so their Min / Max / Avg history is identical. The two 5 May evening photos are a fresh HWiNFO run (elapsed 0:00:52 and 0:00:56) after a reboot with changed power limits.

---

## PXL_20260420_095124136.jpg

Screen: Clonezilla (ocs-sr) image verification console, end of run. Not a BIOS page.

- Job name = 2026-04-20-desktop-990pro
- Target disk = nvme0n1 (Samsung 990 PRO 1 TB per later HWiNFO)
- Partition table type = gpt
- Partition table file = /home/partimag/2026-04-20-desktop-990pro/nvme0n1-pt.sf
- nvme0n1p1 = restorable
- nvme0n1p2 = saved by dd or partclone.dd, "no need or no way to check the file system integrity", restorable
- nvme0n1p3 = restorable
- nvme0n1p4 = restorable
- Result = "All partition and logical volume images in this image were checked and are restorable"
- Note = "We are not unmounting the bitlocker partitions, for if we do we break the clone_server (ocs-onthefly)"
- Ending /usr/sbin/ocs-sr at = 2026-04-20 12:50:09 UTC
- Progress box: Total Time = 00:00:06, Remaining = 00:00:00, Ave. Rate = 5.90 GB/min, Data Block Process = 100.00%, Total Block Process = 100.00%
- Prompt = Press "Enter" to continue...

Interpretation: a full image of the boot NVMe was taken and verified on 20 April, before BIOS experimentation. No CPU or RAM settings on this screen.

---

## PXL_20260428_105755655.jpg

Screen: Gigabyte AORUS UEFI BIOS, "Save & reset" confirmation dialog (Save & Exit). Orange Aorus theme. Page path behind the dialog not visible.

- Dialog title = Save & reset
- Prompt = Save configuration and reset?
- Buttons = Yes (highlighted, cyan) / No
- Last Modified = Performance CPU Clock Ratio [53] -> [Auto]

Interpretation: on 28 April the P-core turbo multiplier was moved from a manual 53x (5300 MHz) back to Auto. 53x is the stock 13900K max turbo ratio, so this reverts a manual pin at 53 or a profile that had written 53 explicitly. Only one modified setting is listed, so this save changed nothing else.

---

## PXL_20260505_171812697.jpg

Screen: Windows desktop, HWiNFO64 v8.46-5960 with three windows: Sensors Status, "CPU #0 - Active Clock" per-core panel, System Summary. A game (RTSS overlay top-left: GPU1 61 C 99%, MEM1 15842 MB, CPU 99 C 15%, RAM 21434 MB, D3D12 100 FPS, frametime 9.6 ms) runs behind. HWiNFO elapsed = 2:34:12. Blurry "Perform Action / Activate Terminal" lines in the background are a game menu.

System Summary (identical in every 5 May photo, listed once here):
- CPU = Intel Core i9-13900K, Intel 7, Stepping B0, TDP 125 W, MCU 12B, Codename Raptor Lake-S 8+16, SSPEC SRMBH, Prod. Unit, Socket V (LGA1700)
- P-core = 8 / 16, E-core = 16 / 16
- Cache L1 = 8x32 + 8x48 and 16x64 + 16x32, L2 = 8x2M and 4x4M, L3 = 36M
- Motherboard = GIGABYTE Z790 AORUS ELITE AX, Chipset = Intel Z790 (Raptor Lake-S PCH)
- BIOS Date = 12/04/2024, Version = F13b, UEFI
- Memory Size = 32 GB, Type = DDR5 SDRAM, Clock = 3000.0 MHz = 30.00 x 100.0 MHz, Mode = Quad-Channel, CR = 2T
- Timing = 36 - 38 - 38 - 80, tRC = 118, tRFC = 480
- Memory module #1 [BANK 0/DDR5-A2] = Kingston KF560C36-16, 16 GB, 3000 MHz, ECC No, DDR5-6000 / PC5-48000 DDR5 SDRAM UDIMM
- SPD profile table (Clock / tCL / tRCD / tRP / tRAS / RC / Ext. / V):
  - 3000 / 36 / 38 / 38 / 80 / 118 / XMP / 1.35
  - 2600 / 32 / 33 / 33 / 70 / 103 / XMP / 1.35
  - 2400 / 30 / 31 / 31 / 64 / 95 / XMP / 1.35
  - 2200 / 28 / 28 / 28 / 59 / 87 / XMP / 1.35
  - 1800 / 22 / 23 / 23 / 48 / 71 / XMP / 1.35
  - 2800 / 36 / 38 / 38 / 80 / 118 / XMP / 1.25
  - 2400 / 32 / 33 / 33 / 69 / 101 / XMP / 1.25
  - 2000 / 26 / 28 / 28 / 57 / 84 / XMP / 1.25
  - 3000 / 36 / 38 / 38 / 80 / 118 / EXPO / 1.35
  - 2600 / 32 / 33 / 33 / 70 / 103 / EXPO / 1.35
- Operating Point: LFM (Min) = 800.0 MHz x8.00; Base Clock (HFM) = 3000.0 MHz x30.00; Turbo Max = 5300.0 MHz x53.00; Ring/LLC Max = 5000.0 MHz x50.00
- GPU (iGPU) = Intel Raptor Lake-S Integrated Graphics, Intel UHD Graphics, Raptor Lake-S/HX GT1, PCIe v2.0 x0 (5.0 GT/s) @ [DISABLED], 16.00 GB SDRAM 64-bit, Xe Cores 2, EUs/ALUs 32 / 256, GPU clock 1650.0, Memory 3000.0
- OS = UEFI Boot, Secure Boot, TPM, HVCI (all green), Windows 11 Pro (x64) Build 26200.8246 (25H2)
- Drives = WDC WD30EFRX-68EUZN0 [3 TB] SATA, WDC WD10EZEX-08M2NA0 [1 TB] SATA, WDC WD40EFRX-68WT0N0 [4 TB] SATA, Samsung SSD 990 PRO 1TB [1 TB] NVMe x4 16.0 GT/s

Operating Point live rows (this photo): Avg. Active Clock = 4512.5 MHz x45.12, VID 1.3518 V; Avg. Effective Clock = 826.6 MHz x8.27; Ring/LLC Clock = 4500.0 MHz x45.00, VID 1.1862 V

Sensors Status, CPU [#0] (Current / Min / Max / Avg):
- Core VIDs = 1.312 V / 0.695 V / 1.472 V / 1.253 V
- Uncore VID = 1.179 V / 0.656 V / 1.264 V / 1.117 V
- SA VID = 1.249 V / 1.249 V / 1.249 V / 1.249 V
- Core Clocks = 4,408.3 MHz / 800.0 MHz / 5,301.3 MHz / 4,060.7 MHz
- Bus Clock = 100.0 MHz (all columns)
- Ring/LLC Clock = 4,300.0 MHz / 800.0 MHz / 4,601.1 MHz / 3,845.2 MHz
- Core Effective Clocks = 813.3 MHz / 0.2 MHz / 5,180.8 MHz / 676.4 MHz
- Average Effective Clock = 979.4 MHz / 38.3 MHz / 1,778.0 MHz / 795.8 MHz
- Core Usage = 16.0 % / 0.0 % / 95.3 % / 14.3 %
- Max CPU/Thread Usage = 72.1 % / 11.5 % / 95.3 % / 61.6 %
- Total CPU Usage = 16.0 % / 2.1 % / 37.8 % / 14.3 %
- On-Demand Clock Modulation = 100.0 % (all)
- Core Utility = 26.2 % / 0.0 % / 166.4 % / 22.0 %
- Total CPU Utility = 26.2 % / 1.3 % / 50.4 % / 22.0 %
- Core Ratios = 44.1 x / 8.0 x / 53.0 x / 40.6 x
- Uncore Ratio = 43.0 x / 8.0 x / 46.0 x / 38.5 x

DTS:
- Core Temperatures = 87 C / 33 C / 100 C / 74 C
- Core Distance to TjMAX = 13 C / 0 C / 67 C / 26 C
- CPU Package = 97 C / 40 C / 100 C / 82 C
- Core Max = 97 C / 38 C / 100 C / 82 C
- Core Thermal Throttling = Yes / No / Yes / 70 %
- Core Critical Temperature = No / No / No / 0 %
- Core Power Limit Exceeded = No / No / No / 0 %
- Package/Ring Thermal Throttling = Yes / No / Yes / 70 %
- Package/Ring Critical Temperature = No
- Package/Ring Power Limit Exceeded = No

Enhanced:
- CPU Package = 97 C / 40 C / 106 C / 83 C
- CPU IA Cores = 97 C / 38 C / 107 C / 82 C
- CPU GT Cores (Graphics) = 76 C / 36 C / 81 C / 65 C
- Voltage Offsets = 0.000 V / 0.000 V
- VDDQ TX Voltage = 1.250 V (all)
- VR VCC Current (SVID IOUT) = 62.524 A / 1.180 A / 160.440 A / 74.704 A
- CPU Package Power = 125.891 W / 5.053 W / 165.342 W / 91.429 W
- IA Cores Power = 123.558 W / 3.625 W / 163.106 W / 89.358 W
- GT Cores Power = 0.123 W / 0.000 W / 0.135 W / 0.086 W
- Rest-of-Chip Power = 1.300 W / 0.542 W / 1.723 W / 1.102 W
- PL1 Power Limit (Static) = 253.0 W (all)
- PL2 Power Limit (Static) = 253.0 W (all)
- VR VCC Power (SVID POUT) = 96.000 W / 8.000 W / 216.000 W / 100.683 W
- OC Ratio Limits = 24.0 x (Min) / 58.0 x (Max)

C-State Residency: Package C2 = 0.0 %, Package C3 = 0.0 %, Core C0 = 16.6 % / 0.0 / 97.9 / 14.4, Core C1 = 32.5 % / 0.0 / 99.6 / 29.6, Core C6 = 45.2 % / 0.0 / 100.0 / 46.4, Core C7 = 0.0 % / 0.0 / 99.9 / 13.6

Performance Limit Reasons: IA Limit Reasons = Yes / No / Yes / 100 %; GT Limit Reasons = Yes / No / Yes / 100 %; Ring Limit Reasons = Yes / No / Yes / 100 %

Active Clock panel: P0-P4 = 5100 MHz x51.00; P5-P7 = 5200 MHz x52.00; E8-E23 = 4200 MHz x42.00

---

## PXL_20260505_171817927.jpg

Screen: same HWiNFO layout, elapsed 2:34:18, six seconds later. RTSS: GPU1 61 C 98%, MEM1 15842 MB, CPU 100 C 15%, RAM 21466 MB, 100 FPS, 9.6 ms. Min / Max / Avg identical to the previous photo, only Current listed.

- Core VIDs = 1.352 V; Uncore VID = 1.124 V; SA VID = 1.249 V
- Core Clocks = 4,450.0 MHz; Bus Clock = 100.0 MHz; Ring/LLC Clock = 4,200.0 MHz
- Core Effective Clocks = 849.3 MHz; Average Effective Clock = 1,010.1 MHz
- Core Usage = 17.1 %; Max CPU/Thread Usage = 72.5 %; Total CPU Usage = 17.1 %
- Core Utility = 27.5 %; Total CPU Utility = 27.5 %
- Core Ratios = 44.5 x; Uncore Ratio = 42.0 x
- Core Temperatures = 87 C; Core Distance to TjMAX = 13 C; CPU Package = 95 C; Core Max = 97 C
- Core Thermal Throttling = Yes; Package/Ring Thermal Throttling = Yes; Critical = No; Power Limit Exceeded = No
- Enhanced CPU Package = 97 C; CPU IA Cores = 97 C; CPU GT Cores = 76 C
- VR VCC Current = 128.588 A; CPU Package Power = 123.422 W; IA Cores Power = 121.127 W; GT Cores Power = 0.078 W; Rest-of-Chip Power = 1.307 W
- PL1 = 253.0 W; PL2 = 253.0 W; VR VCC Power = 168.000 W
- Core C0 = 17.6 %; C1 = 33.0 %; C6 = 43.4 %; C7 = 0.0 %
- Operating Point: Avg. Active Clock = 4450.0 MHz x44.50, VID 1.3521 V; Avg. Effective Clock = 904.4 MHz x9.04; Ring/LLC Clock = 4200.0 MHz x42.00, VID 1.1235 V
- Active Clock panel: P0-P3 = 4800 MHz x48.00; P4-P7 = 5200 MHz x52.00; E8-E23 = 4200 MHz x42.00

---

## PXL_20260505_171850829.jpg

Screen: same HWiNFO layout, elapsed 2:34:50. RTSS: GPU1 62 C 99%, CPU 100 C 16%, RAM 21483 MB, 99 FPS, 9.3 ms. History columns unchanged.

- Core VIDs = 1.366 V; Uncore VID = 1.179 V; SA VID = 1.249 V
- Core Clocks = 4,508.3 MHz; Ring/LLC Clock = 4,400.0 MHz
- Core Effective Clocks = 792.6 MHz; Average Effective Clock = 973.3 MHz
- Core Usage = 15.7 %; Max CPU/Thread Usage = 72.1 %; Total CPU Usage = 15.7 %
- Core Utility = 25.6 %; Total CPU Utility = 25.6 %
- Core Ratios = 45.1 x; Uncore Ratio = 44.0 x
- Core Temperatures = 87 C; Core Distance to TjMAX = 13 C; CPU Package = 99 C; Core Max = 97 C
- Core Thermal Throttling = Yes; Package/Ring Thermal Throttling = Yes
- Enhanced CPU Package = 99 C; CPU IA Cores = 99 C; CPU GT Cores = 76 C
- VR VCC Current = 112.072 A; CPU Package Power = 124.605 W; IA Cores Power = 122.261 W; GT Cores Power = 0.122 W; Rest-of-Chip Power = 1.312 W
- PL1 = 253.0 W; PL2 = 253.0 W; VR VCC Power = 152.000 W
- History maxima: Package Power 165.342 W; VR VCC Current 160.440 A; VR VCC Power 216.000 W
- Core C0 = 16.2 %; C1 = 34.2 %; C6 = 44.1 %; C7 = 0.0 %
- Operating Point: Avg. Active Clock = 4508.3 MHz x45.08, VID 1.3661 V; Avg. Effective Clock = 1055.9 MHz x10.56; Ring/LLC Clock = 4400.0 MHz x44.00, VID 1.1786 V
- Active Clock panel: P0-P3 = 4500 MHz x45.00; P4 = 4600 MHz x46.00; P5-P7 = 4900 MHz x49.00; E8-E23 = 4000 MHz x40.00

---

## PXL_20260505_171853762.jpg

Screen: same HWiNFO layout, elapsed 2:34:54. RTSS: GPU1 62 C 99%, CPU 97 C 16%, RAM 21478 MB, 100 FPS, 10.0 ms.

- Core VIDs = 1.280 V; Uncore VID = 0.996 V; SA VID = 1.249 V
- Core Clocks = 4,216.7 MHz; Ring/LLC Clock = 3,600.0 MHz
- Core Effective Clocks = 789.2 MHz; Average Effective Clock = 968.7 MHz
- Core Usage = 15.5 %; Max CPU/Thread Usage = 73.0 %; Total CPU Usage = 15.5 %
- Core Utility = 25.5 %; Total CPU Utility = 25.5 %
- Core Ratios = 42.2 x; Uncore Ratio = 36.0 x
- Core Temperatures = 87 C; Core Distance to TjMAX = 13 C; CPU Package = 99 C; Core Max = 97 C
- Core Thermal Throttling = Yes; Package/Ring Thermal Throttling = Yes
- Enhanced CPU Package = 96 C; CPU IA Cores = 96 C; CPU GT Cores = 76 C
- VR VCC Current = 97.916 A; CPU Package Power = 122.776 W; IA Cores Power = 120.477 W; GT Cores Power = 0.092 W; Rest-of-Chip Power = 1.299 W
- PL1 = 253.0 W; PL2 = 253.0 W; VR VCC Power = 144.000 W
- Core C0 = 16.1 %; C1 = 34.3 %; C6 = 44.1 %; C7 = 0.0 %
- Operating Point: Avg. Active Clock = 4216.7 MHz x42.17, VID 1.2798 V; Avg. Effective Clock = 1051.5 MHz x10.52; Ring/LLC Clock = 3600.0 MHz x36.00, VID 0.9960 V
- Active Clock panel: P0-P3 = 4200 MHz x42.00; P4-P7 = 5000 MHz x50.00; E8-E15 = 4000 MHz x40.00; E16-E19 = 4100 MHz x41.00; E20-E23 = 4000 MHz x40.00

---

## PXL_20260505_171924444.jpg

Screen: same HWiNFO layout, elapsed 2:35:24. RTSS: GPU1 62 C 99%, CPU 100 C 16%, RAM 21517 MB, 99 FPS, 8.5 ms.

- Core VIDs = 1.233 V; Uncore VID = 1.156 V; SA VID = 1.249 V
- Core Clocks = 4,083.3 MHz; Ring/LLC Clock = 4,300.0 MHz
- Core Effective Clocks = 784.3 MHz; Average Effective Clock = 970.9 MHz
- Core Usage = 16.0 %; Max CPU/Thread Usage = 70.4 %; Total CPU Usage = 16.0 %
- Core Utility = 25.3 %; Total CPU Utility = 25.3 %
- Core Ratios = 40.8 x; Uncore Ratio = 43.0 x
- Core Temperatures = 88 C; Core Distance to TjMAX = 12 C; CPU Package = 100 C; Core Max = 99 C
- Core Thermal Throttling = Yes; Package/Ring Thermal Throttling = Yes
- Enhanced CPU Package = 101 C; CPU IA Cores = 101 C; CPU GT Cores = 77 C
- VR VCC Current = 89.658 A; CPU Package Power = 123.396 W; IA Cores Power = 121.062 W; GT Cores Power = 0.117 W; Rest-of-Chip Power = 1.302 W
- PL1 = 253.0 W; PL2 = 253.0 W; VR VCC Power = 128.000 W
- Core C0 = 16.0 %; C1 = 35.3 %; C6 = 43.2 %; C7 = 0.0 %
- Operating Point: Avg. Active Clock = 4083.3 MHz x40.83, VID 1.2332 V; Avg. Effective Clock = 803.8 MHz x8.03; Ring/LLC Clock = 4300.0 MHz x43.00, VID 1.1565 V
- Active Clock panel: P0-P3 = 4900 MHz x49.00; P4-P6 = 4300 MHz x43.00; P7 = 4700 MHz x47.00; E8-E23 = 3800 MHz x38.00

Afternoon-run summary (17:18 to 17:19): PL1 = PL2 = 253 W static, package temperature 95 to 101 C with thermal throttling active 70 % of the 2.5 h run, package power around 123 to 126 W at photo time even though the limits allow 253 W (the cap is thermal; IA/GT/Ring limit reasons all Yes), peak package power 165.342 W, peak VR current 160.440 A, peak Core VID 1.472 V, peak core clock 5,301.3 MHz, peak ring 4,601.1 MHz. Memory at XMP 6000 (3000 MHz DDR clock), 36-38-38-80, 2T.

---

## PXL_20260505_192356781.jpg

Screen: same HWiNFO layout, fresh run, elapsed 0:00:52. RTSS: GPU1 60 C 99%, MEM1 12786 MB, CPU 100 C 15%, RAM 14937 MB, 105 FPS, 9.7 ms. Min / Max / Avg now cover only about 52 s.

CPU [#0] (Current / Min / Max / Avg):
- Core VIDs = 1.343 V / 1.159 V / 1.443 V / 1.351 V
- Uncore VID = 1.186 V / 1.061 V / 1.249 V / 1.191 V
- SA VID = 1.249 V (all)
- Core Clocks = 4,433.3 MHz / 3,900.0 MHz / 5,300.0 MHz / 4,474.7 MHz
- Bus Clock = 100.0 MHz
- Ring/LLC Clock = 4,500.0 MHz / 3,900.0 MHz / 4,500.0 MHz / 4,403.7 MHz
- Core Effective Clocks = 762.3 MHz / 0.6 MHz / 4,376.6 MHz / 755.2 MHz
- Average Effective Clock = 961.8 MHz / 776.7 MHz / 1,007.5 MHz / 941.7 MHz
- Core Usage = 15.1 % / 0.0 % / 85.3 % / 14.9 %
- Max CPU/Thread Usage = 71.1 % / 65.9 % / 85.3 % / 71.5 %
- Total CPU Usage = 15.1 % / 11.9 % / 16.8 % / 14.9 %
- On-Demand Clock Modulation = 100.0 %
- Core Utility = 24.6 % / 0.0 % / 145.0 % / 24.3 %
- Total CPU Utility = 24.6 % / 20.0 % / 25.8 % / 24.3 %
- Core Ratios = 44.3 x / 39.0 x / 53.0 x / 44.7 x
- Uncore Ratio = 45.0 x / 39.0 x / 45.0 x / 44.0 x

DTS:
- Core Temperatures = 87 C / 80 C / 100 C / 88 C
- Core Distance to TjMAX = 13 C / 0 C / 20 C / 12 C
- CPU Package = 96 C / 94 C / 100 C / 97 C
- Core Max = 96 C / 95 C / 100 C / 98 C
- Core Thermal Throttling = Yes / No / Yes / 100 %
- Core Critical Temperature = No; Core Power Limit Exceeded = No
- Package/Ring Thermal Throttling = Yes / Yes / Yes / 100 %
- Package/Ring Critical Temperature = No; Package/Ring Power Limit Exceeded = No

Enhanced:
- CPU Package = 101 C / 95 C / 102 C / 99 C
- CPU IA Cores = 101 C / 95 C / 102 C / 99 C
- CPU GT Cores (Graphics) = 77 C / 75 C / 77 C / 77 C
- Voltage Offsets = 0.000 V
- VDDQ TX Voltage = 1.250 V
- VR VCC Current (SVID IOUT) = 82.579 A / 57.806 A / 127.408 A / 92.367 A
- CPU Package Power = 121.004 W / 113.714 W / 122.476 W / 119.003 W
- IA Cores Power = 118.667 W / 111.488 W / 120.187 W / 116.699 W
- GT Cores Power = 0.141 W / 0.000 W / 0.168 W / 0.124 W
- Rest-of-Chip Power = 1.277 W / 1.144 W / 1.393 W / 1.262 W
- PL1 Power Limit (Static) = 180.0 W (all columns)
- PL2 Power Limit (Static) = 200.0 W (all columns)
- VR VCC Power (SVID POUT) = 152.000 W / 80.000 W / 176.000 W / 132.741 W
- OC Ratio Limits = 24.0 x / 58.0 x

C-State: Package C2 = 0.0 %, Package C3 = 0.0 %, Core C0 = 15.5 % / 0.0 / 85.7 / 15.4, Core C1 = 34.5 % / 0.0 / 99.7 / 34.7, Core C6 = 44.8 % / 0.0 / 99.9 / 44.7, Core C7 = 0.0 %

Performance Limit Reasons: IA = Yes / No / Yes / 100 %; GT = Yes / No / Yes / 100 %; Ring = Yes / No / Yes / 100 %

Operating Point: Avg. Active Clock = 4625.0 MHz x46.25, VID 1.4182 V; Avg. Effective Clock = 1028.0 MHz x10.28; Ring/LLC Clock = 4500.0 MHz x45.00, VID 1.1886 V

Active Clock panel: P0 = 5100 MHz x51.00; P1-P7 = 5300 MHz x53.00; E8-E23 = 4300 MHz x43.00

System Summary: identical to the afternoon photos (BIOS F13b, memory 3000 MHz 36-38-38-80 2T, XMP profile table) except iGPU Current Clock GPU = 1200.0 (was 1650.0).

---

## PXL_20260505_192401206.jpg

Screen: same HWiNFO layout, elapsed 0:00:56. RTSS: GPU1 61 C 99%, MEM1 12786 MB, CPU 100 C 16%, RAM 14935 MB, 105 FPS, 9.2 ms.

- Core VIDs = 1.324 V / 1.159 V / 1.443 V / 1.353 V
- Uncore VID = 1.156 V / 1.061 V / 1.249 V / 1.190 V
- SA VID = 1.249 V
- Core Clocks = 4,412.5 MHz / 3,900.0 MHz / 5,300.0 MHz / 4,477.7 MHz
- Ring/LLC Clock = 4,400.0 MHz / 3,900.0 MHz / 4,500.0 MHz / 4,406.9 MHz
- Core Effective Clocks = 778.8 MHz / 0.6 MHz / 4,376.6 MHz / 756.6 MHz
- Average Effective Clock = 983.3 MHz / 776.7 MHz / 1,007.5 MHz / 944.3 MHz
- Core Usage = 15.6 %; Max CPU/Thread Usage = 63.9 % / 63.9 % / 85.3 % / 71.2 %; Total CPU Usage = 15.6 %
- Core Utility = 25.1 %; Total CPU Utility = 25.1 %
- Core Ratios = 44.1 x / 39.0 x / 53.0 x / 44.8 x
- Uncore Ratio = 44.0 x / 39.0 x / 45.0 x / 44.1 x
- Core Temperatures = 87 C / 80 C / 100 C / 88 C; Core Distance to TjMAX = 13 C / 0 C / 20 C / 12 C
- CPU Package = 97 C / 94 C / 100 C / 97 C; Core Max = 95 C / 95 C / 100 C / 98 C
- Core Thermal Throttling = Yes / No / Yes / 100 %; Package/Ring Thermal Throttling = Yes / Yes / Yes / 100 %
- Critical Temperature = No; Power Limit Exceeded = No (core and package)
- Enhanced CPU Package = 101 C / 95 C / 102 C / 99 C; CPU IA Cores = 101 C / 95 C / 102 C / 99 C; CPU GT Cores = 76 C / 75 C / 77 C / 77 C
- Voltage Offsets = 0.000 V; VDDQ TX Voltage = 1.250 V
- VR VCC Current = 84.939 A / 57.806 A / 127.408 A / 92.098 A
- CPU Package Power = 119.891 W / 113.714 W / 122.476 W / 119.076 W
- IA Cores Power = 117.585 W / 111.488 W / 120.187 W / 116.772 W
- GT Cores Power = 0.124 W / 0.000 W / 0.168 W / 0.123 W
- Rest-of-Chip Power = 1.262 W / 1.144 W / 1.393 W / 1.262 W
- PL1 Power Limit (Static) = 180.0 W (all columns)
- PL2 Power Limit (Static) = 200.0 W (all columns)
- VR VCC Power (SVID POUT) = 80.000 W / 80.000 W / 176.000 W / 129.931 W
- OC Ratio Limits = 24.0 x / 58.0 x
- Core C0 = 15.8 %; C1 = 35.2 %; C6 = 43.6 %; C7 = 0.0 %
- IA / GT / Ring Limit Reasons = Yes, 100 %
- Operating Point: Avg. Active Clock = 4433.3 MHz x44.33, VID 1.3398 V; Avg. Effective Clock = 782.1 MHz x7.82; Ring/LLC Clock = 4500.0 MHz x45.00, VID 1.1862 V
- Active Clock panel: P0-P7 = 5100 MHz x51.00; E8-E23 = 4100 MHz x41.00
- System Summary: same as the 19:23:56 photo, iGPU GPU clock = 1200.0

---

## Cross-photo deltas

| Item | 28 Apr | 5 May 17:18 to 17:19 | 5 May 19:23 to 19:24 |
|---|---|---|---|
| Performance CPU Clock Ratio | 53 -> Auto (saved) | Turbo Max x53 (Auto) | Turbo Max x53 (Auto) |
| PL1 / PL2 (static) | not visible | 253 W / 253 W | 180 W / 200 W |
| Memory | not visible | XMP 6000, 36-38-38-80, 1.35 V, 2T | same |
| BIOS | not visible | F13b (12/04/2024) | F13b |
| Peak Core VID in run | not visible | 1.472 V | 1.443 V |
| Peak package power in run | not visible | 165.342 W | 122.476 W |
| Package temp at photo | not visible | 95 to 101 C, throttling Yes | 96 to 101 C, throttling Yes |
| iGPU clock | not visible | 1650.0 | 1200.0 |

Observations:
- PL1 180 W / PL2 200 W in the evening photos matches no Intel 13900K default (Performance = 253/253, Extreme = 253/253 with 400 A IccMax, Baseline = 125/188). 180/200 reads as a hand-set value in BIOS between 17:19 and 19:23 on 5 May. High confidence on the values, medium confidence that they were set by hand rather than by a Gigabyte preset.
- IccMax is not shown in any photo. VR VCC Current peaked at 160.440 A (afternoon) and 127.408 A (evening); neither reaches the 307 A or 400 A Intel limits, so the photos say nothing about the IccMax setting.
- Voltage Offsets = 0.000 V in every photo, so no undervolt offset was applied in either state. Core VID peaks of 1.472 V (afternoon) and 1.443 V (evening) sit under the 1.55 V ceiling of Intel microcode 0x12B, which HWiNFO shows as MCU 12B.
- The CPU thermally throttles at about 100 C in both states while drawing only about 120 W, which points at cooling (mount, paste, AIO) rather than power limits as the throttle cause. Whether 180/200 W was the stability fix cannot be verified from these photos; it caps sustained package power below the thermal ceiling and would trim Vcore excursions under all-core load.
- No test-result screens (OCCT, Prime95, MemTest86, Windows Memory Diagnostic) are in this batch. All seven HWiNFO photos were taken while a D3D12 game ran at about 100 FPS, so the load is gaming, not a synthetic stress test.
- Unreadable: the BIOS page behind the 28 Apr dialog; the RTSS overlay second line ("Automated Porter ...") in every 5 May photo; the game menu text beyond "Perform Action / Activate Terminal".
