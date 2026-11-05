---
type: project
created: 2026-11-05
author: jep
status: active
---

# Handoff: "Pay Attention" phase 4 (the whole video), mid-build

Written 2026-11-05 at the close of the session that fixed the proof (R30), recorded Idi's standard (R31) and built the video's plates in waves. **Start the next session here.** Next ruling: **R32**. The live state file is `D:\work\aimv-lab\pa-video\briefs\plates-plan.md` (update it at every wave change); this note is the map around it.

## 0. Read in this order

1. This file.
2. `D:\work\aimv-lab\pa-video\briefs\plates-plan.md`: every plate, its builder, status, the lead procedure, usage budget, kit decisions, log.
3. [[video2-standard-r31-2026-11-05]]: the 7 rules every plate and critic is held to (Idi R31, verbatim in [[kit-next-video]]).
4. `D:\work\aimv-lab\pa-video\briefs\plates-common.md`: the builder brief (hard rules, lessons, the recurring failures the blind critics found, gates); one `plate-<id>.md` per plate.
5. [[video2-proof-fixes-2026-11-04]]: the proof's three rounds (R30 defects, Idi's round-3 notes, the zoom into the reflection).
6. As needed: [[handoff-2026-11-04-pay-attention-plates]] (song, timing, data, look A, treatment, cards), the plate reports `D:\work\aimv-lab\pay-attention\reports\p4-<plate>.md`.

## 1. Where things stand

| window | plate | state |
|---|---|---|
| 0:00-0:27.9 | open (+ verse1) | accepted |
| 0:27.9-0:52.7 | class | accepted |
| 0:52.7-1:21.4 | late + chorus1 (the proof) | done; Idi's eye pending on fix3 (zoom into the reflection) |
| 1:21.4-1:44.4 | fact | accepted |
| 1:44.4-2:18.7 | games | accepted, one open check: its device's HUD may read screen-stuck (border on the frame edge, ~4 px of breathing); fix if the whole-video critic flags it |
| 2:18.7-2:42.8 | chorus2 | accepted |
| 2:42.8-3:15.5 | kitchen | accepted (7b1168b; critic round 1 fixed: `D:\work\aimv-lab\pa-video\briefs\findings-kitchen-r1.md`) |
| 3:15.5-4:53 + tail | exam, verse4, chorus3, outro | briefs to write (waves 4-5); title cards (R24) are the lead's |

Watchable for Idi: `D:\work\AIMVs\ours\pa-song\proof\pa-wip-0m00-1m21.mp4` (0:00-1:21 joined: 0 flashes, 0 flips, beat 60 % at 3.9x). Engine repo `D:\work\aimv-lab\pay-attention` (local only), commits by builders and lead (`git log`).

## 2. Lead procedure (it worked; keep it)

1. One brief per plate on disk; 2 builders at a time (a third only for a fix round).
2. On a report: sweep the render (`pa-video\tools\sweep-window.sh`: 8 fps grids + 30 fps at every change), diff full frames either side of every seam (`pa-video\tools`; bar under 1 % of pixels > 40, sung words excluded), then a blind critic agent with grids only and R31 rules 1-7 (prompt template: `D:\work\aimv-lab\pa-video\briefs\critic-template.md`; tools in `pa-video\tools\`: sweep-window.sh, gates-window.sh, full.sh, grid.py, board.py); send real findings back as a FIX/KEEP list; accept on re-render + clean gates.
3. Gates per window: `pa-video\tools\gates-window.sh FROM TO NAME pre|post` (check, clarity 4K, lifecycle, avsync PA wrapper, flash, flips).
4. Continuous seams: the next plate asks for `continuousIn: true` on its timeline row (no hard change for the gates; clarity keys elements by space), declares `handlesTransition`, and imports the previous plate's camera or drawing read-only so its first frame IS the last one.

## 3. Rulings made this session (jep; Idi may overrule)

| item | ruling |
|---|---|
| one board | verse 1's chalkboard IS the classroom board (chorus1's geometry); class opens on it and erases it on screen |
| class -> late | LEAN flattens into the beam (late.ts hand-over); the key ignites from dark |
| L39 | ME stays whole and rests above "...but yourSELF." (the card's "ME inside the last word" is impossible) |
| the meter | identical in every plate, no backing; `meter({ value })` exists for visual-only readings that hand back to the clock |
| devices | a frame-filling screen with a fixed HUD reads as screen-stuck: our camera lives relative to the glass |
| hard cuts | allowed between scenes on a downbeat with a stated reason (chorus2 at 138.58) |

## 4. Open items

1. Wave 4 briefs are written (`plate-exam.md`, `plate-verse4.md`; kitchen is accepted): spawn b-exam and b-verse4 first thing. Wave 5: write `plate-chorus3.md`, `plate-outro.md` (pattern: the wave 2-4 briefs; in/out links from the neighbours' reports; chorus3 = the final chorus with callbacks to every earlier plate: read every report's threads).
2. R24 title cards: silent receipt header before the song, the reverse after the bill; the meter's 5:00.00 from "Hi." stays outside them; tail 8.37 s. Needs a pre-roll in the timeline (engine time 0 = song 0 today).
3. Kit merges (optional): `ignite()`, the turning camera (open's camOf/pj).
4. R25 particle blind panel: not yet run on any phase-4 plate; run once on the full render.
5. VERIFY items before release: the cards' 24 (INDEX), the kitchen's four injection wordings (L50), the fact sheet URL and "c. 370 BC" (open plate report section 6).
6. Full render 1080p (`kit-tools\render-seg\segrender.py`), full gates, a blind critic over the whole video, a fix round, then Idi.

## 5. Lessons from this session

1. A defect list from Idi is a symptom list: find the class of cause (two drawings of one place; screen-space where world-space belongs) and fix the class.
2. Compare full frames either side of every handover; most seams that "matched" by eye differed by 1-18 % until measured.
3. Gates read cuts from the timeline: a continuous change needs `continuousIn`, or the gates flag the very words that prove continuity.
4. Blind critics with the owner's standard find 13-22 real items per plate that builders and gates missed; budget a fix round per plate.
5. Two builders + critics + lead use the 5-hour window in about 3.3 h: expect a stop per ~1.5 waves; builders commit often, resume by message with their last commit.
6. Builders' summaries arrive after the fact and repeat; act on the first, ignore the echo.
