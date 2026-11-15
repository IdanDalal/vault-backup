---
type: note
created: 2026-11-15
author: jep
status: active
project: DECADEnts
---

# DECADEnts T6: new head concepts (2026-11-15, partial)

Continues `handoff-2026-11-15.md`, dominoes 1 to 3. Scan doc. Tap sheet: `t6-concepts-2026-11-15.html` (same folder).

## State

1. Rendered and blind-checked: 26 of 46 pictures. All four new heads for 1940s, 1960s, 1980s; one of four for 2000s.
2. Stopped: the session's memory guard killed the render around 12:44 (PC critically low on memory; ComfyUI 12 GB, Idi's Vivaldi about 4 GB, free RAM 5.3 to 6.9 GB during the run against 9 to 14.6 GB on 11-13). jep stopped ComfyUI and did not restart it. Free RAM after the stop: 19.1 GB.
3. Not rendered (20 pictures, about 19 minutes): 2000s energy drink can, PC tower, subwoofer box; 1920s statue (two readings); 1930s black mirror lenses; 1950s and 1970s keeps; 2010s drawn face (two outfits). Prompts written.
4. Waiting on Idi: his word to render the 20; his taps on the sheet (partial taps are kept in his browser).

## Result (two blind critics, full size, shuffled names, head named before the brief was read)

| Measure | Count |
|---|---|
| Intended object named unaided | 26 of 26 |
| Head instruction followed | 22 fully, 4 partly, 0 not |
| Nothing human visible | 12 clean, 6 uncertain, 8 clear leak |
| Clear leaks by cause | 5 open shirt collar (1980s), 3 sleeve down a raised arm |
| Critics' look, funny (mean of 5) | new 4.12, 3.96; the four dropped concepts as hidden controls 2.75, 2.25 |
| Seconds per picture | 54.5 to 67.5, median 55.6 |

Critics' look and funny scores are triage for where to look. Idi's taps decide.

## Per head

| Decade | Head | Sheet pictures | Followed | Human parts | Look | Funny | jep |
|---|---|---|---|---|---|---|---|
| 1940s | radio in a helmet | 1, 2 | yes, yes | leak, uncertain | 3, 4 | 4, 4 | pick |
| 1940s | searchlight | 3, 4 | partly, yes | clean, clean | 5, 5 | 3, 4 |  |
| 1940s | fuel can in a helmet | 5, 6 | yes, partly | clean, uncertain | 4, 3 | 4, 4 |  |
| 1940s | binoculars in an officer's cap | 7, 8 | yes, yes | uncertain, uncertain | 4, 4 | 4, 4 |  |
| 1960s | yarn ball with needles | 9, 10 | partly, yes | clean, clean | 5, 5 | 4, 4 | pick |
| 1960s | teapot in a bobble cap | 11, 12 | yes, yes | clean, uncertain | 5, 4 | 4, 4 |  |
| 1960s | mushroom lamp | 13, 14 | yes, yes | leak, leak | 3, 3 | 3, 4 |  |
| 1960s | crocheted daisy | 15, 16 | yes, yes | clean, clean | 4, 5 | 4, 4 |  |
| 1980s | giant mobile phone | 17, 18 | yes, yes | uncertain, clean | 4, 4 | 4, 4 | pick |
| 1980s | cassette tape | 19, 20 | yes, partly | leak, leak | 4, 4 | 4, 5 |  |
| 1980s | boombox | 21, 22 | yes, yes | leak, clean | 4, 5 | 4, 4 |  |
| 1980s | briefcase | 23, 24 | yes, yes | leak, leak | 4, 4 | 4, 4 |  |
| 2000s | flip phone | 25, 26 | yes, yes | clean, clean | 4, 4 | 4, 4 |  |
| 2000s | energy drink can | not rendered | | | | | |
| 2000s | case-modded PC tower | not rendered | | | | | |
| 2000s | subwoofer box | not rendered | | | | | |

## jep's picks and reasons

1. 1940s: radio in a helmet. It is the toaster-with-a-hat formula you called funny, it keeps your original helmet, and the dial and speaker cloth give him a face plane that can glow and pulse in video. Its wrist gap is a sleeve fix. Second: the searchlight, the cleanest of the four with the critic (look 5 and 5, nothing human in both).
2. 1960s: yarn ball with needles. Both halves of the Hippie Grandma sit in one object (tie-dye, knitting), she knits from her own head, and the critic scored it look 5 and 5 with nothing human in either picture. Second: the teapot, a silhouette no other cast member has, and it can pour.
3. 1980s: giant mobile phone. It is the Yuppie's own object and it doubles your phone-and-cigar gag: a phone holding a phone. The narrow handset also hides the collar best (1 clean, 1 uncertain; the three wide heads leak neck in 5 of 6). The boombox has the best single picture (look 5), the cassette the best gag (funny 5). One dependency: the 2000s flip phone would make two phones in the cast.
4. 2000s: no pick until the other three heads exist. The flip phone is clean in both pictures.

## Fix list for the next renders (costume and wording; none changes a concept)

| Defect | Where | Fix |
|---|---|---|
| Neck patch in the open shirt collar | 1980s, 5 of 8 | head object rests on the shoulders and covers the collar; or a closed high collar |
| Wrist or forearm on a raised arm | radio (1 clear, 1 uncertain), mushroom lamp (2) | long gloves over the cuff; or keep both arms down |
| Helmet in the German shape | radio, both pictures | name the helmet type (US M1) |
| Dark chin-shaped mass under the head | binoculars, both | seat the binoculars directly on the collar |
| Helmet doubled | fuel can, picture 6 | reroll |
| Briefcase on its long side, cash on top | both | "standing on its short side" restated; notes in the side seam |
| Drawn faces and garbled lettering on posters | mushroom lamp | plain patterned wall |
| Period look | 1940s read as modern photographs (jep's eye) | open item from the handoff, untouched |

Re-render only the heads Idi picks.

## How to resume

| Step | Command |
|---|---|
| Start | `bash /c/Users/jep/comfy2-tools/comfy2_up.sh --fast-disk --disable-pinned-memory` |
| Render the remaining 20 (the runner skips what its manifest holds) | `cd /c/Users/jep/comfy2-tools && python -I t4_run.py hy3 t6_prompts.json t6-out 3,4` |
| Stop, always | PowerShell: `& "C:\Users\jep\comfy2-tools\comfy2_down.ps1"` |
| Blind set | `blind_set3.py` reshuffles everything; for round two build a set from the new 20 only, plus controls |
| Picks and sheet | `python -I make_picks6.py .` then `python_embeded/python.exe -I make_sheet6.py . t6-sheet/t6-concepts-2026-11-15.html` |
| Probe | `bash probe.sh <page> 1500 1000` and `484 900` |

Memory: ask Idi to close the browser first; the guard's second kill in this project came with it open.

## Receipts

- Prompts: `C:\Users\jep\comfy2-tools\t6_prompts.json` (23; checked by script for negations: 0).
- Pictures and manifest (seconds, lowest free RAM per picture): `C:\Users\jep\comfy2-tools\t6-out\`.
- Blind sets and key: `C:\Users\jep\comfy2-tools\blind3\`, `blind3-key.json`; critics' rows: `blind3-out\critic-A.json`, `critic-B.json`.
- Tallies by script: `make_picks6.py` (asserts the three sums).
- Sheet probe (headless Edge): 1500 px and 484 px, 0 overflow, 0 script errors, 35 pictures (26 plus 9 earlier ones as reference), 29 tap groups, scripted taps gave `DECADEnts T6 answers | 1940s: pick=radio in a helmet; radio in a helmet yes 4/5`. Screenshots viewed at both widths.
- ComfyUI: stopped (pid 23100), port 8190 closed.

## Log

- 2026-11-15 written after the partial run. Answers arrive as a pasted line starting `DECADEnts T6 answers |`.
