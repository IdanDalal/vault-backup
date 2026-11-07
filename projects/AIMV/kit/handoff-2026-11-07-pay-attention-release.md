---
type: project
created: 2026-11-07
author: jep
status: active
---

# Handoff: "Pay Attention" release path (all plates accepted)

Written 2026-11-07 while the first whole-video render ran. **Start the next session here.** Next ruling: **R34**. Live state: `D:\work\aimv-lab\pa-video\briefs\plates-plan.md` (section "Full render and release path"). Previous map: [[handoff-2026-11-05-pay-attention-phase4]]. Kit level-up (research, R32, R33): [[kit-levelup-2026-11-05]].

## 1. State

| window (engine s) | plate | state |
|---|---|---|
| 0-195.5 | open ... kitchen | accepted (2026-11-05) |
| 195.5-208.2 | exam | accepted (72bf56e; 2 critic rounds) |
| 208.2-238.2 | verse4 | accepted (c1dea39; 2 critic rounds + honest clarity: moving-flag clauses removed) |
| 238.2-261.1 | chorus3 | accepted (d5b9eb9; avsync 85 % from in-world beat events; lead waiver: 2 clarity texture flags on the room grid) |
| 261.1-300.37 | outro | accepted (b44cd09) |
| 300.37-311.37 | titlesOut, titlesIn (R24) | accepted (0bd82c3; a till built from the landed meter prints both slips) |

Engine repo `D:\work\aimv-lab\pay-attention` (local only). Assembly moves titlesIn to the front: the release is 5:11.37, the song starts at 0:05.00.

## 2. Lead changes this session (engine commits, each verified on stills)

1. Blank-frame class fix (open INK'S 19.37, fact THEY stamps): a slot's `out` hid at its frame edge before the next word lit.
2. PA post layer `paPost` in `timeline.ts`: chromatic aberration 0, amber halation 0 (treatment lines 21, 40); the rhythm kit's downbeat flash 0 (sourceless light, R31 rule 5); its whole-frame zoom/shake removed (moved the meter, rule 4; Idi R33 = A). Scene-set ca/halation kept for hits.
3. `TAIL = 8.37` (R23, END of the bill 300.37); title rows `titlesOut` / `titlesIn` (`fixed`, no beat snap; END 311.37).
4. The slip's header = R24's three lines in print order in open, chorus2, outro and the titles: CLAUDE OPUS 5.5 + MINIMAX MUSIC 3 (MONO 12) / CHORUS OF MINDS (MONO 16) / PAY ATTENTION (MONO7 24).

## 3. Next steps, in order

1. Whole render: `bash D:/work/aimv-lab/pa-video/tools/full-1080.sh` (resumable; output `out\full-1080\pa-full-1080p.mp4`, log `render.log`).
2. Gates per window + `tools\camprobe.py` + `tools\scans.py` on the whole render; avsync per window (chorus1, chorus2 lost their flash/pulse hits: add in-world beat events where a window drops under 45 %).
3. R25 particle blind panel; whole-video blind critic (two halves, template `briefs\critic-template.md`); one fix round.
4. `bash tools/assemble.sh <render> <review.mp4> review` -> Idi watches (known issues first, R31 + kit level-up 4.5).
5. L1-L6 A/B stills and clips for Idi (R32 = A), the kick in three clips (no kick / world-camera kick / old screen pulse, R33).
6. 4K master: segrender `--scale 2` (~14 h expected), `assemble.sh ... master` (H.264 CRF 12 capped 100 Mbps, AAC 384k 48 kHz).
7. VERIFY items before release (handoff 11-05 section 4.5).

## 4. Lessons

1. Inherited kit code carried three R31 breaks no plate critic could pin on a plate (ca, halation, screen pulse): audit post layers whenever a standard changes.
2. A gate the scene feeds (moving flags) can be gamed by the scene: audit what each builder registers.
3. avsync partly measured the sourceless flash: a metric that drops when a defect is fixed was measuring the defect.
4. The MP4 edit list hid the last frame: count decoded frames, never packets.
5. Agents survive usage-limit stops within a session (resume by message) and die with a session restart (respawn by name with the last commit and the uncommitted diff).
