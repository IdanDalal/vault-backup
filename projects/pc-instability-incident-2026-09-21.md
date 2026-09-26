---
type: report
created: 2026-09-21
author: jep
status: active
---

# PC instability incident, 2026-09-21

Verdict: hardware instability (CPU i9-13900K first suspect, RAM second), followed by system-file damage from the unclean shutdowns. jep's only change that day, the XCOM crash-dump registry key, is scoped to XCom2.exe and played no part; C: had 105 GB free.

Timeline (Windows logs): 11:40 hang, no signal (no bugcheck record: hard hang or power). 11:42 boot, BSOD 0x154; 11:44 boot, BSOD 0x18; 11:46 boot, BSOD 0x1; calm until 12:49 hang (0x3B); 12:50 boot, 12:50:49 hang; 12:53 boot, BSOD 0x1E (FLTMGR); 12:55 boot, stable since. BIOS "load optimized defaults" between 11:40 and 11:42 (RAM now 4800 instead of XMP 6000).

Signature after each boot: NordVPN, Steam, Discord, Defender engine, Corsair, Task Manager, XCOM2 Launcher crash within seconds, mixed codes, mostly in the .NET runtime compiler (coreclr, clrjit, clr.dll). Five different bugcheck codes. Code Integrity: fcon.dll and Defender helper hashes not found (36x), luafv driver blocked from loading. Microcode 0x12B (BIOS F13b, 12/2024); 0x12F exists (2025).

Plan handed to Idi: 1) memory test (mdsched), 2) if RAM passes, CPU: BIOS Intel Default profile, BIOS update to a 0x12F build, Intel RMA path (13th gen extended warranty), 3) repair system files (sfc, DISM) once stable. Kernel minidumps in C:\Windows\Minidump are admin-only, unread.

## History check (Idi's question: degradation or revived old problem)

System log begins 2026-06-04. Unexpected shutdowns with no blue screen (hard hang, code 0): 06-20, 06-30, 07-01, 08-13, 08-23, 09-14 x3 (20:36, 20:45, 20:53). Blue screen: 08-30 10:39 (0x7E), the same day the XCOM fail-fast family began. Then 09-21: 2 hangs + 5 blue screens in 75 minutes. Frequency: 3 events in June-July, 2 in mid-August, then 08-30, 09-14 x3, 09-21 x7. Read: the earlier fix reduced the fault to a hang every 2 to 3 weeks and never removed it; the curve steepens from late August, which is when the XCOM crashes started. Today's BIOS "optimized defaults" erased that fix and the raw fault returned in full: three blue screens in four minutes and every .NET app crashing at boot. Both of Idi's hypotheses hold: degradation progressed, and the reset revived it. jep cannot read BIOS settings, so the exact earlier fix is unknown; the vault holds no record of that episode (before jep's time on this PC).
