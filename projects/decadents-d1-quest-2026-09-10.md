---
type: note
created: 2026-09-10
author: jep
status: done
project: DECADEnts
---

# DECADEnts D1 quest, 2026-09-10

Done-state (Studio Preflight D1): one portrait file on disk per Character Visual Dictionary entry, in that decade's film stock, chosen by Idi. Whole-quest done = two files named in the log at the bottom, seeds recorded. Deadline from the Preflight's own rule: 2026-09-29.

## State found today, from the `jep` account (receipts)

- ComfyUI Desktop 0.35.0, frontend 1.51.10, PyTorch 2.12.1+cu130, serving `127.0.0.1:8188`. `GET /system_stats` 200 from `jep`. RTX 4090, 24.1 GB VRAM free idle, 4.4 GB free with Z-Image loaded.
- Models present: `z_image_turbo_bf16.safetensors` (diffusion_models), `qwen_3_4b.safetensors` (text_encoders), `ae.safetensors` (vae), `ace_step_1.5_turbo_aio.safetensors` (checkpoints; music, ACE-Step 1.5). Empty: upscale_models, loras, controlnet, clip_vision. Custom nodes: none. Absent: UltimateSDUpscale, DetailDaemon, FaceDetailer.
- Renders on disk: 35, `output\z-image-turbo_00001_` to `_00035_`. Renders 2 and 3 = the 1990s CRT-head. The other 33 = template test (Latina, harbour) and Kid Studio style tests (cats, dragons, unicorns, claymation, watercolor).
- Whiteboard line of 09-09 "no render exists" was a stale prior. Corrected: two CRT-head renders predate today. Date unknown from here; `/history` was empty (server restarted since).
- Workflow in every render = the shipped Z-Image-Turbo template: `res_multistep`, `simple`, 8 steps, cfg 1.0, `ModelSamplingAuraFlow` shift 3.0, negative = `ConditioningZeroOut`, bf16 weights. Subgraph ids `57:xx` in the executed graph point to the template origin (medium confidence). Nothing to tune for D1.
- Timing measured: cold 15.2 s (model load), warm 4.1 s per 1024x1024 image, 8 seeds 29.4 s, 1152x864 4.1 s.
- December Character Visual Dictionary: zero hits in this vault (grep of every `.md` for "Visual Dictionary", "CRT", "toddler"). Its CRT-head entry survives only as the prompt text of render 2, quoted below. The 2020s toddler entry does not exist on this PC.

Render 2 prompt (Idi's hand, verbatim): `waist-up portrait, 50mm, of a figure whose head is a beige 1990s CRT monitor with faint scanlines glowing on the curved glass, wearing a boxy denim jacket over a striped tee, head tilted slightly toward the camera, standing in a wood-panelled living room, direct on-camera flash throwing a hard shadow on the wall behind, shot on Fuji Superia 400, visible grain and green-tinted shadows, 4:3 snapshot framing, no text, no watermark`

## Rule crossed today, named

Preflight D1 = by hand, D3 = agent connects only after D1 and D2. On "you should be able to see it, control it", jep queued 12 renders through the API: 2 under `output\jep-probe\`, 10 under `output\decadents\d1-crt\` (8 sweep, 2 script tests). Slots filled, graph untouched, per D3's own rule. Delete `jep-probe\` for a clean folder; the sweep folder is the contact sheet's source.

## Quest

| # | Owner | Item | Done = | Cost | jep pre-test |
|---|---|---|---|---|---|
| 0 | Idi | Rule: does render 2 close D1 for the 1990s? | yes / no | 1 min | viewed: CRT head, scanline, denim, striped tee, wood panel, flash shadow, grain, all present; square, not 4:3 |
| 1 | Idi | Pick from the contact sheet (`projects/decadents/d1-contact-sheet.html`, open in Vivaldi on this PC) | 1 to 3 indices, 0 to 8 | 3 min | 8 sweep URLs answer 200 image/png; page rendered headless in Edge |
| 2 | jep | Re-render the picks at true 4:3 (1152x864) with their seeds, plus 4 prompt variants x 2 seeds at 4:3 | files under `output\decadents\d1-crt\` + contact sheet | 4 s each | `test43_00001_.png` rendered at 1152x864 in 4.1 s, viewed: 4:3 holds, shadow and panelling intact |
| 3 | Idi | Drop the December Visual Dictionary into `inbox/`, or paste the 2020s toddler entry under Dump | file or paragraph exists | 5 min | none possible |
| 4 | jep | Toddler sweep, 8 seeds, 2020s stock per the entry | 8 files + contact sheet | 30 s | the CRT sweep |
| 5 | Idi | Select one per decade | 2 indices | 3 min | none |
| 6 | jep | Log both files and seeds here; propose the Whiteboard item 2 rewrite and one jar row | this file's log | 2 min | none |

Skipped, with reason: D2 refinement (Detail Daemon, 2x upscale, Ultimate SD Upscale). All three pieces absent from this install; rule of three not bitten once; 1024-class output is enough for screen. Revisit at first print or first video frame.

## Tooling shipped (D3-sized, `projects/decadents/`)

- `z-image-turbo.template.json`: the executed graph, one slot `{{PROMPT}}`; seed, size, prefix filled by script. Loaders pinned to the three model files above.
- `render.py`: `python render.py --prompt "..." --count 8 --size 1152x864 --prefix decadents/d1-crt/sweep --fetch DIR`. Tested: seed 1990, 1024x1024, 4.1 s, fetched 1,526,537 bytes; seed 1990 at 1152x864, 4.1 s. Exit 1 on ComfyUI error or unreachable port.
- `d1-contact-sheet.html`: 9 images embedded as JPEG q70 copies (1.4 MB, opens anywhere). Loopback loading failed: ComfyUI answers 403 to any request carrying `Sec-Fetch-Site: cross-site`, so a `file://` page cannot pull from `:8188`; curl without that header gets 200. Rendered headless in Edge, all 9 visible, captions checked.
- ComfyUI's own Queue side panel also lists all 12 API renders with previews, since they went through `/history`.

## Finding from the sweep

Eight seeds of this prompt at cfg 1.0 produce near-identical compositions (same pose, framing, monitor placement; sweep 6 and 8 tilt slightly). Turbo distillation plus a fully specified prompt collapses seed variance. Consequence for item 2 and 4: vary the prompt (pose, lens, distance, room, tee stripe colour), 2 seeds each, instead of 8 seeds of one prompt. Medium-high confidence; one prompt tested.

## Optimizations considered, none applied

- Steps: 8 is Turbo's design point; a distilled model does not gain from more (Z-Image-Turbo model card, 8 NFE; medium-high confidence).
- fp8 weights: frees roughly 6 GB VRAM at a quality cost; pointless on 24 GB.
- Batch: 2 at 1280x768 already ran; 4.4 GB free after load suggests batch 4 at 1024 fits (medium confidence, untested).
- 4:3: Z-Image was trained around 1 MP; 1152x864 keeps that budget at 4:3.

## Log

- 2026-09-10 quest written; 12 API renders; tools tested; awaiting Idi on items 0 and 1.
- 2026-09-10 Idi's rulings: item 0 = yes, render 2 closes D1 for the 1990s (`output\z-image-turbo_00002_.png`, seed 732135135824266, his hand). Item 1 = pick 6 (`output\decadents\d1-crt\sweep_00006_.png`, seed 23069123189203). Item 2 done: pick 6 re-rendered at 1152x864 as `output\decadents\d1-crt\pick6_00001_.png`, 3.7 s. **D1 1990s: DONE.** One W staged for the jar (Built: a crafted list reached done with a receipt). Open: items 3 to 5, the 2020s toddler, blocked on the Visual Dictionary entry.
- 2026-09-10 13:10 Idi's Everything search shows the DECADEnts sources: `D:\KEEP\NEXUS BACKUP\projects\Idiverse\DECADEnts.md`, `DECADEnts 1.md`, `2.md`, `3.md` (2025-12-30), and two Nexus atomic notes `2025-12-30-decadents.md`, `2025-12-30-research-report-decadents---production-bible--tech.md` (2026-01-16); a second copy under `D:\KEEP\Vaults BACKUPS\Idiverse\` with the same names and dates. jep: Permission denied on `D:\KEEP` (Phase B). Pull blocked until the read grant on the Whiteboard runs; then pull into `projects/decadents/source/` verbatim (his files, his authorship, never edited by jep) plus the 3 D1 renders into `projects/decadents/renders/`.
- 2026-09-10 13:16 Idi dropped the seven December files into `projects/decadents/` himself (grant not needed). Visual Dictionary found: `DECADEnts 3.md` section 2, 11 heads. 2020s = "VR Headset / QR Code, face fully obscured by tech"; archetype "iPad Toddler, 5". Item 3 closed, item 4 done: 8 candidates (A VR couch, B QR selfie, C VR tantrum, D QR stroller; seeds 2020/2021; 768x1344), 34 s total, sheet `decadents/d1-2020s-contact-sheet.html`, verified in Edge. Finding: "head is a VR headset" renders as a worn headset with mouth visible (1, 2, 5, 6); QR panel variants obscure the face (3, 4, 7, 8); "shot on a 2023 iPhone" made number 2 render inside a phone frame, drop that phrase. Distilled bible: `decadents/decadents-bible.md`. Awaiting one number for item 5.
- 2026-09-10 14:00 Idi: pick 6 "far from perfect": visibly a white boy with dark hair; wants an inanimate figure with no gender or ethnicity, wearing a 2029 sci-fi sensory-immersion prototype (Matrix-like helmet/suit plugging into all five senses, not the brain). Round 2: E glossy white sealed suit, F black sphere helmet + dino haptic suit + 5 cables, G mirrored faceplate + ribbed tubes, H white mannequin + translucent visor; seeds 2029/2030; sheet `decadents/d1-2020s-contact-sheet-2.html`, verified in Edge. jep's read: E (1, 2) and G (5, 6) still show a crying child's face through an open helmet, fail the rule; F (3, 4) and H (7, 8) show no skin; F's "five cables" rendered as antennae; H reads as a white doll with a mouthpiece under the visor. Awaiting one number.
- 2026-09-10 14:20 Idi corrected the rule: the HEAD is the inanimate object so the character represents everyone; the body stays a child in the suit. Pick from round 2: 3 (black sphere, dino haptic suit). Asked for round 3: funnier, one intricate integrated device instead of separate parts, RGB. Round 3 (I oversized RGB gaming helmet with juice snorkel, J gaming PC tower as head, K five-sense pod with braided cable and pacifier, L chrome salon dome with crying-emoji hologram; seeds 3/4; 768x1344): all 8 sealed, no skin, `decadents/d1-2020s-contact-sheet-3.html`, verified in Edge. jep's recommendation: 4 or 3 (PC tower head: strongest silhouette, most literal 2020s object, funniest). Awaiting one number.
- Inversion logged (meta-rule 10): the first reply asked three things in one message and mixed quest item numbers with contact-sheet indices. Idi said he spent "A LOT of energy" decoding it. Fix applied: one question per message, one index scheme per message.
- 2026-09-14 Idi picked 8 from round 3 (chrome helmet, crying-emoji visor): genderless, raceless, and the visor is a front-facing screen for the character's internal state. New suit rules: juice box on the belt with a tube to the chin port, spare juice boxes as magazines on a chest rig, no dinosaurs, and the print must serve humor, characterization, thematic expression and 2029 lore. Round 4 (M fictional sponsors, N app badges, O product labels, P smiley print, Q real logos as a legal test, R slang text, S sponsors under kid stickers; seeds 3/4; 768x1344; 14 renders in 67 s): `decadents/d1-2020s-contact-sheet-4.html`, verified in Edge. Legal read on real logos in the bible. jep's recommendation: P (smiley print under the crying visor) with branded juice boxes as the sponsor layer. Awaiting one number, 1 to 14.
- 2026-09-14 Idi picked 4 from round 4 (N app-icon badges, seed 4): "the right silhouette, we'll work out the details later"; stickers unrecognizable, one dinosaur left. Copied to `decadents/renders/d1-2020s-pick4-badges-seed4-768x1344.png`. jep's read: D1 2020s can close on this file (done-state = one portrait file chosen by Idi); details belong to the next stage. Awaiting his ruling.
- 2026-09-14 **D1 CLOSED** on Idi's word ("Close it. We're optimizing for throughput at this stage, quality in later stages."). The two files: 1990s = `renders/d1-1990s-crt-render2-seed732135135824266.png` (seed 732135135824266, his prompt, 09-10); 2020s = `renders/d1-2020s-pick4-badges-seed4-768x1344.png` (seed 4, N-badges prompt in contact sheet 4, 09-14). Details deferred to later stages: legible badges, stray dinosaur, riff-brand juice boxes, 2020s stock look. Nine decades still have no render; that is the next quest, under the throughput rule.
