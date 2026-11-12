---
type: note
created: 2026-11-12
author: jep
status: active
project: DECADEnts
---

# DECADEnts restart: models and mediums (2026-11-12)

Idi's order, 2026-11-12: deep research on image models to replace Z-Image-Turbo (MiniMax H3-Image, HunyuanImage 3.0 80B); agents to find more ideas like "render the 1940s Soldier as comics or animation" for the weakest designs.

Done-state of this file: research distilled with sources, every idea rendered at least once, rulings staged with effects. Review surface: `projects/decadents/t1-medium-tests-2026-11-12.html` (54 pictures, tap answers, one line to paste).

## Verdict

1. **Design was the bigger lever. The model was the smaller one.** On the same model, three weak characters rose from 1.7 to 2.9 of 5 (September photographs) to 4.25 to 4.5 (new designs), scored by blind critics.
2. **HunyuanImage 3.0 (80B): no.** RAM: needs about 50 GB, this PC has 31.8.
3. **MiniMax H3-Image: real, open, ungated, best blind-vote score of any open model.** Licence bars displaying outputs in the USA, EU, UK and South Korea. Worth a lab test; publishing is Idi's ruling.
4. **The Soldier as comics: holds, with a condition.** A drawn medium hides nothing by itself (face in 14 of 14). Naming the head as an object hides the features (6 of 6); only the poster is fully clean; the result breaks when the wording moves.
5. **Nothing new is installed.** 54 renders ran on jep's own ComfyUI with the existing model.

## Receipts

| What | How verified | Where |
|---|---|---|
| 6 research reports, 2 blind critiques of renders | agents wrote files; jep read all eight in full | `projects/decadents/research-2026-11-12/` |
| H3-Image licence clauses | jep fetched and read the licence text (18 KB, anonymous) | section 3 |
| Qwen-Image-2.1 licence | jep fetched and read: "for research or evaluation purposes only" | section 3 |
| Gating and licence tags, 15 repos | HuggingFace API read anonymously by script | section 3 |
| 7 precedent claims | full pages opened by a fetch agent: 3 supported, 4 partly | section 5 |
| 54 test renders | jep viewed all; 50 also read by blind critics at full size | the review sheet |
| Review sheet | headless Edge at 1576 and 492 px: 0 overflow, 0 script errors, 55 images, scripted taps gave the expected answer line; looked at desktop and 390 px renders | the review sheet |
| PC facts | 31.8 GB RAM, RTX 4090 24 GB, C: = NVMe (Samsung 990 PRO, 257 GB free), D: = hard disk | PowerShell |

## 1. Why the September renders felt "low quality"

Source: first blind critic, 32 round-2 renders plus the 4 accepted portraits, no prompts or code seen. Sizes are its estimates by eye.

| Rank | Defect | Count of 32 |
|---|---|---|
| 1 | No gag in frame: the character stands or sits and poses | 32 |
| 2 | Human visible under or around the head: skin, eyes, hair, ears | 20 |
| 3 | Head worn on or pasted over a human head, so the image shows a person in costume | 17 |
| 4 | Head-to-body join unsolved: stump, plug, floating gap, lit neck under a void | 17 |
| 5 | Period look missing: noiseless, razor-sharp, modern lens blur | 16 |
| 6 | Head drawn in a different visual register from the body (flat fill, vector sticker, CGI ball) | 16 |
| 7 | Head too small or lost at thumbnail size | 14 |

Its three bins of cause:
- Model limits: fused hands, reflections of an absent room, gibberish text, pre-1950 film rendered as modern digital.
- Concept faults that any renderer hits: a mask is a face worn by someone (1920s); a gas mask has eye windows (1930s); "shadow" has no object (1940s); "floating shapes" has no silhouette (1980s); a lava lamp at real scale is a third of shoulder width (1960s).
- Art direction: no scripted action, no camera spec per decade, wide framing, designs drifting between prompt variants.

What the three accepted portraits share: one solid manufactured object, head-sized or larger, replacing the head; a face plane (screen, visor) that can carry expression; one light for the whole frame; medium shot; locked wardrobe; stacked jokes.

## 2. Test T1: same model, new designs

54 renders, Z-Image-Turbo, seeds 3 and 4, about 4 s each. Prompts: the agents', verbatim (in the sheet's folds and in `research-2026-11-12/t1_prompts.json`, `t2_prompts.json`). Scores: second and third blind critics, mean of craft and brief, 1 to 5.

| Character | September photo | Design tested | Pictures | Result | Score |
|---|---|---|---|---|---|
| 1980s Yuppie | 1.7 | solid totem seated in the collar, photograph | 31, 32 | no neck, no face in 2 of 2; wrist sliver in 31 | 4.5 |
| | | 1985 broadcast CGI | 27, 28 | no neck; reads as modern vector art | 3.25 |
| | | cut-paper collage | 29, 30 | no neck; shapes float loose; flesh paper hands in 30 | 3.25 |
| 1960s Hippie Grandma | 2.0 | psychedelic flat cel | 23, 24 | lamp is the head, 2 of 2 | 4.25 |
| | | light-show silhouette | 25, 26 | real head with a lamp on top | 3.0 |
| | | felt puppet | 21, 22 | human puppet holding the lamp | 2.5 |
| 1930s Survivor | 2.9 | work-relief silkscreen poster | 15, 16 | no face, no skin, 2 of 2 | 4.25 |
| | | scarecrow photograph | 19, 20 | sealed in 1 of 2; button eyes in 20; T-pose | 3.75 |
| | | carved-wood puppet | 17, 18 | carved face with bead eyes | 3.0 |
| 2000s Edgelord | parked | low-poly PC-tower head | 35, 36 | head sealed 2 of 2; flesh block hands | 3.5 |
| | | web-cartoon flip-phone head | 37, 38 | 38 works; 37 is a held prop | 3.5 |
| | | webcam with pixel mosaic | 33, 34 | mosaic holds; bare fingers; hair and neck in 34 | 2.75 |
| 1940s Soldier | 2.4 | seven mediums, first wording | 1 to 14 | face in 14 of 14 | 2.0 to 3.0 |
| | | poster, head named as an object | 43, 44 | fully clean 2 of 2; reads as menace; helmet leans German | 4.75 |
| | | ink cartoon, same wording | 41, 42 | features hidden; neck band in 41, bare fingers in 42 | 3.25 |
| | | comic panel, same wording | 39, 40 | features hidden; ear and neck wedge show | 3.0 |
| | | cel, caption box, censor block | 45 to 50 | faces in 5 of 6 | 2.0 to 2.75 |
| | | comic and ink, closed collar plus a chore | 51 to 54 | lower face back in 4 of 4 (jep's eye only) | - |

Caveats: two seeds per design; three separate blind agents shared one rubric, so the gaps are solid and the decimals are soft; own miss: jep first reported the reworded Soldier "sealed 6 of 6" from thumbnails, and the third critic's full-size read corrected it to 2 fully clean.

Rules the tests support (jep's reading):
1. **Name an object as the head.** "The head is a ..." seals. "A soldier whose face is hidden" draws a soldier.
2. **Seat the head in a collar and keep the collar in frame.** The toaster, the CRT, the totem, the lamp in the cel all sit in one.
3. **Puppets grow faces on this model** (4 of 4).
4. **Name props literally.** "Brick-sized mobile phone" drew a phone made of bricks (28, 31, 32).
5. **Mundane pose reads comic, stern pose reads menace** (third critic: 41 against 43, 44).
6. **Lettering goes in the edit.** Garbled in 12 of 38.
7. **Gloves must be stated in every prompt.**

## 3. Models

Leaderboards used: Artificial Analysis (AA) and LMArena. Both collect blind pairwise human votes on hosted, full-precision models, one image per prompt. Neither measures a compressed local build, seed variety, negative prompts, or object-headed characters. Elo: a rating where a 100-point gap means about 64% of votes.

| Model | Verdict | Fit on this PC | Licence for YouTube | Evidence | Confidence |
|---|---|---|---|---|---|
| Z-Image-Turbo (current) | baseline | runs, 4 s per image (measured today) | Apache-2.0, yes | AA 937, rank 77 of 112; LMArena 1082, rank 61 of 84 | high |
| HunyuanImage 3.0 (80B) | **no** | node author measured about 50 GB RAM held; 31.8 here; 3 anecdotes of 32 GB runs, none timed on a 4090; one 4090 owner with 64 GB reports 130 s against the thread's 26 s | Tencent licence excludes EU, UK, South Korea, outputs included | LMArena 1152, rank 35; AA 994 or 935 depending on host | medium |
| MiniMax H3-Image | **lab probe** | compressed pair 28 to 37 GB of files; no report from a 4090 with 32 GB; needs ComfyUI 0.45+; wants 4 MP or more; no negative prompt | bars display of outputs in the USA, EU, UK, South Korea (clause V.4); public posts must be labelled machine-generated; outputs may not train other models | AA 1067 text-to-image and 1138 editing, first among open models; about 68% preferred over ours; released 2026-11-10, sample two days old; no object-head test exists | high on facts, low on fit |
| MOSS-Image | test arm | about 20 to 30 GB; 45 to 50 s per image (estimate); needs ComfyUI 0.42+ | Apache-2.0, yes | undistilled: negative prompts and seed variety work; unranked on AA; Reddit split ("best base model", score 439, against "cannot get decent results", score 627) | medium |
| Z-Image base | control arm | 12.3 GB, reuses our encoder; about 25 s (estimate) | Apache-2.0, yes | AA 896, below Turbo; real guidance and negative prompts | medium |
| Krea 2 | optional arm | about 32 GB; ungated mirror | commercial use under US$1M revenue | strongest style-range evidence (community sheets, 9 official style add-ons); 512-token prompt limit | medium |
| FLUX 3 Image Klein | later, for re-posing a locked character | about 24 to 35 GB; ungated mirrors; ComfyUI 0.41+ | commercial outputs under US$5M revenue | AA editing 1069; weak from scratch; its maker now describes it as an editing model | medium |
| Qwen-Image-Edit-2511 | edit arm at zero download | **already in jep's ComfyUI** | Apache-2.0, yes | AA editing 996 | high |
| Qwen-Image-2.1 | out for published work | fits | research and evaluation only (read by jep) | AA 1047 and 1084 | high |

House rule on record: Apache or MIT only (the bible's Preflight line; the 2026-10-22 AIMV research applied it). H3-Image, Krea 2 and FLUX 3 Klein sit outside it.

Facts about the Reddit thread Idi sent: title reads "12-24 GB" (the dash was lost); posted 2026-10-06; the "about 30 s" figure is the author's own 188 GB machine; weights are ungated safetensors; the node's runtime code makes no remote-code or network calls (static read of 14 files by the agent).

## 4. Cohesion: one cast, several mediums

- Risk named by the Soldier report: one drawn character among photographed siblings reads as a guest from another show.
- Rule proposed by the decade report: **every decade appears in the format its own era used to picture ordinary people**, and the photographed decades carry period marks too (ratio, grain, intertitles), so no decade is the normal one.
- Its own counterpoint: the decades that change are exactly the weak ones, so without those marks the mix reads as a repair.
- This show's advantage: one character per shot, so two mediums never share a frame.
- Divergence, for completeness: one flat drawn style for all eleven (the Countryballs model named in the December premise). Sealed heads and consistency get easy; the per-decade film-stock joke goes.

## 5. Precedents checked on full pages

| Claim | Result |
|---|---|
| "The Amazing World of Gumball" mixes puppetry, CGI, stop motion and live action in one world | supported |
| Max Headroom (1985) was sold as computer-generated and was an actor in prosthetics | supported |
| Wilson's hidden face in "Home Improvement" was a running gag with a new obstruction each time | supported |
| Glenn Grohe's 1942 poster "He's Watching You" | partly: V&A catalogues a "peering enemy soldier... helmeted". A helmet over darkness meant the enemy in 1942 |
| "Drawn Together" | partly: reality-TV parody confirmed; confessionals unconfirmed |
| "WandaVision" | partly: decade-by-decade sitcom homages confirmed; per-decade aspect ratio unconfirmed |
| "Chip 'n Dale: Rescue Rangers" (2022) | partly: claymation, CGI, hand-drawn confirmed; puppets unconfirmed |

Every other name and date in the two design reports rests on search-result summaries (the agents' own statement). Treat as leads.

## 6. Rulings staged for Idi (answer by tap on the sheet)

| Ruling | Options | What each does | jep recommends |
|---|---|---|---|
| Cast mix | own-era format / drawn where needed / all photographic / one drawn style | see the sheet's effect lines | own-era format |
| Models to install | house rule plus H3 probe / house rule only / none yet | about 75 GB / about 35 GB / zero, all on C: | house rule plus H3 probe |
| One design per character | five picks | sets the direction for the next round | Soldier comic panel, Survivor poster, Grandma cel, Yuppie totem photo, Edgelord PC tower |

## 7. Next, after the rulings (jep's)

1. A second ComfyUI copy at 0.45+ beside the current 0.39, which stays untouched for AIMV and the song engine.
2. Downloads per ruling, to C: (the only fast drive).
3. Head-to-head on our own prompts: the T1 winners plus the known failures (sealed head, a banned object staying absent, seed variety, legible lettering), 8 seeds, blind labeller.
4. Soldier: close the neck two ways and compare: a black shape placed in the edit, and Qwen-Image-Edit-2511 (already local).
5. Art-direction pass: one gag per frame, a camera spec per decade, locked wardrobe.

## 8. Not done, not verified

- No new model installed or run. Speeds and memory on this PC: unmeasured for every candidate.
- Pictures 51 to 54: no blind read.
- Idi's ComfyUI Desktop version: unread (it was down). Tests ran on jep's portable copy, port 8189.
- Injection flag: the decade agent reports that several mirror pages in its search results carried instructions aimed at AI readers. It ignored them and cites none.
- 1920s Gatsby, 1950s, 1970s, 2010s: researched, untested. First critic's note on the Gatsby: a face-shaped mask is a face; a blank porcelain ovoid would fit the cast rule.

## Sources

Full source lists (URLs) sit at the foot of each report in `projects/decadents/research-2026-11-12/`:

- `research-m1-hunyuan3.md`: HunyuanImage 3.0, the ComfyUI node, the Reddit thread (via the Arctic Shift archive), Tencent licence.
- `research-m2-minimax-h3.md`: H3-Image, licence, Artificial Analysis readings, Reddit reception.
- `research-m3-landscape.md`: 27 open models compared, shortlist, leaderboard methods, test plan.
- `research-d1-soldier-medium.md`: 15 period mediums, face-hiding precedents, seven options.
- `research-d2-decade-mediums.md`: mediums per decade, fixes for the weak designs, cohesion rule.
- `research-d3-blind-critic.md`: the September renders.
- `research-d4-blind-critic-t1.md`: pictures 1 to 38.
- `research-d5-blind-critic-t2.md`: pictures 39 to 50.

## Log

- 2026-11-12 created. Six research agents, three blind critics, 54 test renders, review sheet. Awaiting Idi's taps.
