---
type: reference
created: 2026-09-21
author: jep
status: active
---

# The spring 2026 stability fix, reconstructed from 21 phone photos

Source: `D:\work\screens\BIOS`, 21 photos, 2026-02-03 to 2026-05-05. Full transcriptions: `findings-feb-a.md`, `findings-feb-b.md`, `findings-spring.md` in this folder. Board Gigabyte Z790 AORUS ELITE AX, BIOS F13b, microcode 0x12B (unchanged today).

## Final stable state (2026-05-05 19:23, HWiNFO after the last BIOS change)

| Setting | Value then | Value now (after "load optimized defaults", 09-21) | Where in BIOS |
|---|---|---|---|
| Intel Default Settings | Performance | unknown, probably Performance | Tweaker, top page |
| Turbo Power Limits | Enabled | default | Tweaker > Advanced CPU Settings > Turbo Power Limits |
| Package Power Limit1 (PL1) | 180 W | 253 W (Gigabyte default for this profile, seen 05-05 17:18) | same page |
| Package Power Limit2 (PL2) | 200 W | 253 W | same page |
| CPU Clock Ratio | Auto (a 53x cap was tried in April, reverted 04-28) | Auto | Tweaker |
| XMP | Profile 1, DDR5-6000 36-38-38-80 1.35 V | off, RAM at 4800 | Tweaker, top page |
| Vcore, offsets, IccMax, LLC | Auto, offsets 0.000 V | Auto | Voltage Control |

## What the photos prove

- RAM passed MemTest86 11.6: 4 passes, 0 errors, 2 h 16 min, on 2026-02-10 (at 4800, the JEDEC speed). The stable months ran at XMP 6000, so RAM at 6000 is untested by MemTest but proven by use.
- The fix was power, never voltage: PL1/PL2 cut from 253/253 to 180/180 (Feb) then 180/200 (May). No undervolt anywhere in 21 photos.
- Cooling is marginal or failing: on 2026-05-05 at 253/253 the package sat at 97 to 101 C, throttling 70 percent of a game run, at a peak package power of only 165 W and Core VID up to 1.472 V. A 13900K at 165 W on a working AIO should sit far below 90 C. At 180/200 it still hit 96 C within 52 s of boot. Suspect the Corsair AIO pump or mount; the Corsair service crashes today. Heat plus 1.47 V is the known accelerant of 13th-gen Vmin degradation.

## To restore (Idi's hands, BIOS)

1. Tweaker > Advanced CPU Settings > Turbo Power Limits: Enabled. Package Power Limit1 = 180, Package Power Limit2 = 200.
2. Tweaker top page: Intel Default Settings = Performance.
3. Leave XMP off for now (RAM at 4800 is the safer state while the machine is suspect). Re-enable later if stable.
4. Save and exit (F10).

Then: check the AIO (pump RPM in iCUE or BIOS Smart Fan page; CPU temperature at idle should be under 45 C). Memory test only if crashes continue after step 4.
