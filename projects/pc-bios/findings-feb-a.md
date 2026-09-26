# BIOS and MemTest86 photo transcription, 2026-02-03 to 2026-02-10 (batch A)

Board: Gigabyte AORUS (Z790 AORUS ELITE AX per task brief; board model string not visible in any photo). No BIOS version string visible in any of the seven photos.

Sidebar note: the BIOS sidebar (CPU / Memory / Voltage panel) is identical across all four 02-03 photos and is transcribed once under photo 1. Only deltas are listed for the others.

## 1. PXL_20260203_173811768.jpg

Screen: BIOS Advanced Mode, Tweaker tab, scrolled to the CPU/PCH Voltage Control and DRAM Voltage Control sections. Clock on screen: 02/03/2026 Tuesday 19:38.

Cursor-selected row: DDR5 Voltage Control (submenu entry, highlighted orange).

CPU/PCH Voltage Control:
- Vcore Voltage Mode = Auto
- CPU Vcore = Auto (current reading 1.200V) [starred row]
- Dynamic Vcore(DVID) = Auto (+0.000V)
- BCLK Adaptive Voltage = Auto
- CPU Graphics Voltage (VAXG) = Auto
- CPU RING Voltage = Auto (1.050V)
- CPU RING Voltage Offset = Auto (+0.000V)
- Internal L2Atom Override Mode = Auto
- Internal L2Atom = Auto
- Internal L2Atom Offset = Auto
- Internal VCCSA = Auto
- CPU VCCIN AUX = Auto (1.800V)
- VCC1P05 = Auto (1.050V)
- V0P82 PCH = Auto (0.820V)
- V1P8 CPU = Auto (1.800V)
- VCC1V8P = Auto (1.800V)
- Advanced Voltage Settings (submenu)

DRAM Voltage Control:
- VDDQ CPU = Auto (1.100V)
- VDD2 CPU = Auto (1.100V)
- DDR5 Voltage Control (submenu, selected)

Sidebar (identical on all four 02-03 photos except where noted):
- CPU Frequency = 5502.16MHz (secondary figure 4234.01, likely E-core clock)
- BCLK = 100.00MHz
- CPU Temperature = 40.0 C
- CPU Voltage = 0.969 V
- Memory Frequency = 4800.00MT/s
- Memory Size = 32768MB
- Module MFG ID = Kingston
- DRAM MFG ID = Hynix
- +5V = 5.055 V
- +12V = 12.168 V
- VCCSA = 0.798 V
- CPU Biscuits = 81.505 CP (Gigabyte silicon quality score, rendered as "Biscuits" in this firmware)

## 2. PXL_20260203_173822182.jpg

Screen: BIOS Advanced Mode, Tweaker tab, top of page. Clock: 02/03/2026 Tuesday 19:38.

Cursor-selected row: Intel Default Settings (highlighted orange).

- Intel Default Settings = Extreme
- GIGABYTE PerfDrive = Optimization
- CPU Upgrade = Default
- CPU Base Clock = Auto (100.00MHz) [starred]
- Enhanced Multi-Core Performance = Auto [starred]
- Performance CPU Clock Ratio = Auto (30) [starred; 30 is the displayed base ratio]
- Efficiency CPU Clock Ratio = Auto
- Max Ring Ratio = Auto [starred]
- Min Ring Ratio = Auto [starred]
- IGP Ratio = Auto [starred]
- Advanced CPU Settings (submenu)
- DDR5 Auto Booster = Auto
- High Bandwidth = Enabled
- Low Latency = Enabled
- DDR5 XMP Booster = Disabled
- Extreme Memory Profile(X.M.P.) = XMP 1 (DDR5-6000 36-38-38-80-1.350) [starred]
- System Memory Multiplier = Auto (6000) [starred]
- Advanced Memory Settings (submenu)
- Vcore Voltage Mode = Auto
- CPU Vcore = Auto (1.200V) [starred]

Sidebar: same as photo 1. Note the contradiction: XMP 1 is selected with multiplier 6000 shown, but the live sidebar reports Memory Frequency 4800.00MT/s. The setting shown is the pending or profile value; the running speed at this boot was 4800.

## 3. PXL_20260203_173856981.jpg

Screen: BIOS Advanced Mode, Settings tab, main page (IO Ports section). Clock: 02/03/2026 Tuesday 19:38. Help text at bottom: "Select which video display output will be enabled during POST".

Cursor-selected row: Initial Display Output.

- Initial Display Output = PCIe 1 Slot
- Internal Graphics = Enabled
- SPD Write Disable = TRUE
- DVMT Pre-Allocated = 60M
- Aperture Size = 256MB
- PCIE Bifurcation Support = Auto
- OnBoard LAN Controller = Enabled
- Audio Controller = Enabled
- Above 4G Decoding = Enabled
- Above 4GB MMIO BIOS assignment = Enabled
- Re-Size BAR Support = Enabled
- IOAPIC 24-119 Entries = Enabled
- GNA (Gaussian & Neural Accelerator) = Disabled
- Gigabyte Utilities Downloader Configuration (submenu)
- USB Configuration (submenu)
- Network Stack Configuration (submenu)
- NVMe Configuration (submenu)
- SATA Configuration (submenu)
- VMD setup menu (submenu)
- Realtek PCIe 2.5GBE Family Controller (MAC:74:56:3C:37:6D:B5) (submenu)

Sidebar: same as photo 1.

## 4. PXL_20260203_173915106.jpg

Screen: BIOS Advanced Mode, Settings tab, Miscellaneous page. Clock: 02/03/2026 Tuesday 19:39. Help text: "LEDs in System Power On State: On/Off".

Cursor-selected row: LEDs in System Power On State.

- LEDs in System Power On State = On
- LEDs in Sleep, Hibernation, and Soft Off States = Off
- Addressable LED Strip = Auto
- RST_SW (MULTIKEY) = Set this button to HW Reset
- Intel Platform Trust Technology (PTT) = Enabled
- 3DMark01 Enhancement = Disabled
- CPU PCIe Link Speed = Auto
- PCH PCIe Link Speed = Auto
- PCH PCIe X4 Link Speed = Gen3
- VT-d = Disabled [starred]
- Trusted Computing (submenu)
- Acoustic Noise Settings (submenu)

Sidebar: same as photo 1 except +5V = 5.047 V.

## 5. PXL_20260207_150415875.jpg

Screen: BIOS Advanced Mode, Tweaker tab, Advanced CPU Settings submenu, scrolled to Turbo Power Limits. Clock: 02/07/2026 Saturday 17:04. Help text: "Turbo Power Limits". Left edge of the frame is cropped, first characters of some row names cut off.

Cursor-selected row: Turbo Power Limits.

- per Core HT Disable Settings = Auto (row name partly cropped, likely "Hyper-Threading per Core HT Disable Settings")
- C-States Control = Auto (collapsed group)
- Turbo Power Limits = Enabled
- Package Power Limit1 - TDP (Watts) = 180
- Package Power Limit1 Time = Auto
- Package Power Limit2 (Watts) = 180
- Package Power Limit2 Time = Auto
- Platform Power Limit1 (Watts) = Auto
- Platform Power Limit1 Time = Auto
- Platform Power Limit2 (Watts) = Auto
- DRAM Power Limit1 (Watts) = Auto
- DRAM Power Limit1 Time = Auto
- DRAM Power Limit2 (Watts) = Auto
- DRAM Power Limit2 Time = Auto
- Core Current Limit(Amps) = Auto
- Turbo Per Core Limit Control = Auto (expanded group)
- P0 Fused Max Core Ratio = 55
- P1 Fused Max Core Ratio = 55
- P2 Fused Max Core Ratio = 55
- (rows below P2 not visible)

Sidebar (changed from 02-03):
- CPU Frequency = 5302.05MHz (secondary figure 4111.74)
- BCLK = 100.00MHz
- CPU Temperature = 40.0 C
- CPU Voltage = 0.969 V
- Memory Frequency = 4800.00MT/s
- Memory Size = 32768MB
- Module MFG ID = Kingston
- DRAM MFG ID = Hynix
- +5V = 5.055 V
- +12V = 12.186 V
- VCCSA = 1.248 V (was 0.798 V on 02-03)
- CPU Biscuits = 87.463 CP (was 81.505 on 02-03)

Reading of the deltas: PL1 and PL2 are both 180 W, which is neither the Intel Extreme profile default (253 / 253 for the 13900K) nor Auto, so this is a manual cap. The CPU frequency reading dropped from 5502 to 5302 MHz between 02-03 and 02-07 and VCCSA rose from 0.798 to 1.248 V. Both point to a different Intel Default Settings profile or a manual change made between the two dates. The Intel Default Settings row is not in this frame, so the profile in force on 02-07 is not confirmed by this photo.

## 6. PXL_20260209_113106959.jpg

Screen: PassMark MemTest86 V11.6 Free, run in progress. Photo timestamp 2026-02-09 11:31.

- CPU = 13th Gen Intel Core i9-13900K
- Clk/Temp = 3028 MHz / 59C
- L1 Cache = 80 KB, 365.8 GB/s
- L2 Cache = 2 MB, 76.2 GB/s
- L3 Cache = 36 MB, 32.8 GB/s
- Memory = 31.7 GB, 20.8 GB/s
- RAM Config = DDR5 4800MT/s / x2 Channel / Kingston KF560C36-16
- RAM Temp = 37C
- Pass progress = 33%
- Test progress = 65%
- Current test = Test 4 [Moving inversions, 8-bit pattern]
- Address = 0x100000000 - 0x8BFC00000
- Pattern = 0xDFDFDFDF
- CPUs Found = 32
- CPUs Started = 8
- CPUs Active = 8
- CPU list = 0123456789ABCDEFGHIJKLMNOPQRSTU (32 logical CPUs)
- State = |D/D\D/D/D/D/D|DDDDDDDDDDDDDDDD| (8 running, rest D = disabled)
- Time = 0:00:55
- AddrMode = 64-bit
- Pass = 1 / 4
- Errors = 0

Note: RAM running at 4800MT/s during this test, so this MemTest86 run tests JEDEC speed, not the XMP 6000 profile.

## 7. PXL_20260210_110230934.jpg

Screen: PassMark MemTest86 V11.6 Free, run complete, PASS banner. Photo timestamp 2026-02-10 11:02. The PASS overlay covers the middle of the status block.

- CPU = 13th Gen Intel Core i9-13900K
- Clk/Temp = 3028 MHz / 59C
- L1 Cache = 80 KB, 367.0 GB/s
- L2 Cache = 2 MB, 76.2 GB/s
- L3 Cache = 36 MB, 32.8 GB/s
- Memory = 31.7 GB, 20.9 GB/s
- RAM Config = DDR5 4800MT/s / x2 Channel / Kingston KF560C36-16
- RAM Temp = 37C
- Pass progress = 100%
- Test progress = 100%
- Last test = Test 13 [Hammer test] - Verifying pattern
- Address = 0x880000000 - 0x8BFC00000
- Pattern = 0x6E4098EA
- CPU list (visible part) = 01234567
- State (visible part) = \DWDWDWD
- Active = 8
- Time = 2:16: (seconds cut off by the overlay; elapsed at least 2 h 16 min)
- Errors = 0
- Log lines = Finished pass, Finished pass, Finished pass, Finished pass, Releasing memo(ry), > Test Complete
- Banner = PASS, "Test complete, press any key to display summary"
- Pass count = 4 of 4 completed (four "Finished pass" lines; the Pass: x / 4 field is hidden by the overlay)

Note: RAM again at 4800MT/s. Both MemTest86 runs (02-09 and 02-10) ran at JEDEC 4800, not XMP 6000, and both show zero errors. The 02-09 photo shows 0:00:55 elapsed at 11:31 and the 02-10 photo shows 2:16 elapsed at 11:02 the next day, so these are two separate runs.

## Unreadable or absent

- BIOS version string: absent from all photos.
- Photo 5 left margin: first characters of the top row name are cropped.
- Photo 7: the Pass: x / 4 counter, CPUs Found, CPUs Started and the seconds of the elapsed time are hidden behind the PASS overlay.
- Intel Default Settings value on 02-07: not in frame.
