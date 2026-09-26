---
type: note
created: 2026-09-06
author: Agent kidstudio-research
project: tutoring
status: active
---

# Kid Studio: improvement research (2026-09-06, web only, nothing downloaded)

Research agent's report, filed by jep with a reconciliation section at the end. "V" = verified on the source page, "I" = inferred from the source. Effort S/M/L, confidence H/M/L. Page it applies to: `D:\work\studio\kidstudio\` (v2 shipped the same evening).

## 1. Language-learning mechanics

| Idea | What it does | Why for the girls | Source | Effort | Conf |
|---|---|---|---|---|---|
| Change one word | After a picture, she edits exactly one word; old and new picture shown side by side | Isolates one word's meaning; retention rises with task involvement (Hulstijn & Laufer 2001, composition beat fill-in); EFL learners iterating image prompts reported vocab-strategy gains (Hwang, Lee, Shin, arXiv 2311.05373, 2023-11-09, V) | https://arxiv.org/abs/2311.05373 ; https://cris.haifa.ac.il/en/publications/some-empirical-evidence-for-the-involvement-load-hypothesis-in-vo/ | S | M |
| Sentence frames | "A ___ is ___ing in the ___", she types only the blanks, frame gets thinner per session | ELLs gained more than natives from frames (V); keeps a 9-year-old producing full sentences | https://www.colorincolorado.org/teaching-ells/ell-classroom-strategy-library/sentence-frames | S | M |
| Karaoke lyrics | ACE-Step 1.5 already emits LRC line timestamps from DiT cross-attention (V, line level only, 2 s minimum display merge); whisperX wav2vec2 forced alignment on the rendered song gives word level (<100 ms claimed, V for speech, I for singing) | Same-language subtitling raises reading fluency (ERIC EJ1272853, V) | https://deepwiki.com/ace-step/ACE-Step-1.5/5.5-lrc-lyrics-and-timestamps ; https://github.com/m-bain/whisperX ; https://files.eric.ed.gov/fulltext/EJ1272853.pdf | M | M |
| Listen-then-type dictation | Kokoro reads a sentence she made yesterday; she types it; diff highlights letters | Hebrew-L1 kids spell English vowels and digraphs worst (Reading and Writing 2025, V); TTS dictation scored comparably to teacher dictation (ERIC EJ1204392, V) | https://link.springer.com/article/10.1007/s11145-025-10659-3 ; https://files.eric.ed.gov/fulltext/EJ1204392.pdf | S | H |
| Minimal pairs aloud | Kokoro reads ship/sheep, she types which one she heard | Perception training on minimal pairs held at 3 and 6 months (Japanese r/l study, V) | https://www.researchgate.net/publication/321101716_Speech_perception_training_as_a_serious_game_in_the_EFL_classroom | S | M |
| Picture-then-caption | Gallery picture shown with prompt hidden; she types the caption | Dual coding: verbal plus visual retrieval beats verbal alone in EFL (Frontiers 2022, V) | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.834706/full | S | M |
| Yesterday's words | Session starts with 3 words from her own counter log inside a frame | Spacing effect shown in young EFL learners (Cogent Education 2017, V) | https://www.tandfonline.com/doi/pdf/10.1080/2331186X.2017.1287391 | S | H |

## 2. Generator features (4090, ungated, ComfyUI)

| Idea | What it does | Why | Source | Effort | Conf |
|---|---|---|---|---|---|
| Draw-to-picture | Her scribble (canvas or phone photo of paper) as canny/HED/depth/pose into Z-Image-Turbo Fun ControlNet Union (alibaba-pai repo, V); Comfy template exists | Her drawing plus her words = two channels she owns | https://comfy.org/workflows/image_z_image_turbo_fun_union_controlnet-7553d92529e0/ | M | H |
| Edit my picture | Qwen-Image-Edit-2511, Apache 2.0 (V); Q8/FP8 fits 24 GB, 8-step Lightning LoRA (V) | "make the cat blue" = verb + adjective with instant visual check | https://huggingface.co/Qwen/Qwen-Image-Edit-2511 ; https://localaimaster.com/blog/qwen-image-edit-local-guide | M | H |
| Sticker sheet | BiRefNet background removal, built-in Comfy template, auto-downloads (V); tile 6 cutouts on A4 | Physical object from typed words; print and stick | https://docs.comfy.org/tutorials/utility/remove-background-birefnet | S | H |
| Coloring page | Canny/lineart pass on her picture, print | Reuses her own creation; she colors while re-saying the caption | https://civitai.com/articles/2843 | S | M |
| Print upscale | 4x-UltraSharp upscale model (Comfy supported model, V) | Fridge-quality print of her sentence | https://comfy.org/p/supported-models/4x-ultrasharp/ | S | H |
| Sound effects | MOSS-SoundEffect v2.0, 1.3B, Apache 2.0, 48 kHz, up to 30 s, no gate shown on HF (V); Comfy node envy-ai; first call compiles for minutes (V) | "a dog barking in the rain" = noun + verb + preposition, heard back | https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0 ; https://github.com/envy-ai/ComfyUI-MOSS-SoundEffect-v2 | M | H |
| Character voices | Kokoro voice blending, syntax `af_sarah:60,am_adam:40` (V); she names and saves her own blend | Same word in many voices = high-variability phonetic training (I) | https://github.com/nazdridoy/kokoro-tts | S | H |
| Picture-to-video | LTX-2.3 distilled, LTX-2 Community License, listed ungated (I from HF listing); fp8 ~18 GB; RTX 5090 does 5 s at 768x512 in 43.5 s (V); 4090 estimate 60 to 90 s (I) | Her sentence moves; costs a minute of waiting per clip | https://huggingface.co/Lightricks/LTX-2.3 ; https://huggingface.co/datasets/witcheer/rtx-5090-benchmarks/blob/main/reports/ltx-2.3.md | L | M |

## 3. UI/UX for children's creative tools

| Idea | What it does | Why | Source | Effort | Conf |
|---|---|---|---|---|---|
| Big targets, no drag | Tap and click only, no drag or fine gestures | NN/g tested 80 sites and 36 apps including Israel: big targets easy, dragging hard for kids (V) | https://www.nngroup.com/reports/children-on-the-web/ | S | H |
| Remix button | Any gallery item reopens with its prompt prefilled | Scratch data (2.4M projects): remixers have larger command repertoires (V) | https://dl.acm.org/doi/10.1145/2818048.2819984 | S | H |
| Tinkerable history | Every generation kept as a version chain with undo | Scratch design goal "tinkerability" (V) | https://en.scratch-wiki.info/wiki/Scratch_Design_Goals | M | M |
| Milestone moments | Confetti at her own counter milestones (10, 25, 50 words), screen states the number | Duolingo milestone celebrations are tied to a number the learner owns (V); no sister comparison | https://blog.duolingo.com/streak-milestone-design-animation | S | M |
| Word tiles | Allowlist words shown as tappable tiles beside the box, like Song Maker's pentatonic "no wrong notes" | Removes blank-page fear; still typed (tiles insert letters she must confirm) | https://www.musicconstructed.com/tool/chrome-music-lab-song-maker/ | S | M |

## 4. Safety and control

| Idea | What it does | Why | Source | Effort | Conf |
|---|---|---|---|---|---|
| Positive frame | Z-Image-Turbo uses no CFG and ignores negatives (V, 2025-11-27); wrap her words in a fixed "children's picture-book illustration, ..." prefix | Only prompt-side steering exists for this model | https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/discussions/8 | S | H |
| Image second net | AdamCodd/vit-base-nsfw-detector, Apache 2.0, 96.5% accuracy, author warns it is weaker on generated images (V); Falconsai model is Apache 2.0, HF page carries a content warning, gate status unverified | Cheap net; allowlist stays the primary gate | https://huggingface.co/AdamCodd/vit-base-nsfw-detector ; https://huggingface.co/Falconsai/nsfw_image_detection | S | M |
| Text guard for lyrics | Qwen3Guard-Gen 0.6B, Apache 2.0, 119 languages including Hebrew (V) | Lyrics are longer than prompts; catches allowlisted words combined badly | https://github.com/QwenLM/Qwen3Guard | M | M |
| Edge kiosk | `msedge.exe --kiosk http://localhost:PORT --edge-kiosk-type=fullscreen --no-first-run` (V); Win11 Pro Assigned Access single-app auto-restarts and hides Ctrl+Alt+Del unless breakout (V) | Child cannot reach desktop or other sites | https://learn.microsoft.com/en-us/deployedge/microsoft-edge-configure-kiosk-mode ; https://learn.microsoft.com/en-us/windows/configuration/assigned-access/configure-single-app-kiosk | S | H |
| Outputs off OneDrive | Windows 11 enables Known Folder backup by default; anything in Pictures/Desktop uploads (V); write outputs outside those folders and check OneDrive > Sync and backup > Manage backup | "Local only" silently breaks otherwise | https://www.pcworld.com/article/3215054/windows-11-quietly-backs-up-your-files-to-onedrive-heres-how-to-turn-it-off.html | S | H |

## 5. Other

| Idea | What it does | Why | Source | Effort | Conf |
|---|---|---|---|---|---|
| AutoDraw-style canvas | Reference UX: scribble, no login, no data (V); reuse the pattern as the ControlNet input, local | Lowers the drawing floor for the 9-year-old | https://www.kidsaitools.com/en/articles/best-free-ai-drawing-tools-for-kids | M | M |
| 2026 kid AI music roundups | All cloud (Soundverse, Boomy, Soundtrap) (V); the ACE-Step page is ahead on privacy | Nothing to adopt; confirms position | https://www.kidsaitools.com/en/articles/ai-music-tools-for-kids-2026 | - | H |
| Shadowing loop | Kokoro sentence at 0.75x, she repeats, page records nothing | Shadowing apps do this with cloud audio; local version is trivial | https://tts-free.online/en/use-cases/language-learning | S | M |

## Agent's top 5 to build next

1. Positive prompt frame + outputs folder outside OneDrive: two S-effort safety holes, both verified.
2. Karaoke lyrics from ACE-Step's own LRC: data already exists in the model you run.
3. Yesterday's-words frame + change-one-word: strongest research backing (spacing, involvement load) at S effort.
4. Draw-to-picture via ControlNet Union: the feature a 9-year-old will ask for daily.
5. Sticker sheet + upscale print pipeline: takes her English off the screen and onto paper.

## UI pass sources (jep, same night, for the v3 neon redesign)

| Source | What was taken |
|---|---|
| CSS-Tricks, "How to create neon text with CSS" (https://css-tricks.com/how-to-create-neon-text-with-css/) | Stacked text-shadow with a white core and widening colored halos; flicker via opacity keyframes with the shadow removed on the dim frames |
| testmuai, "47 best CSS glow effects" 2026 (https://www.testmuai.com/blog/glowing-effects-in-css/) | Render glow on a pseudo-element and animate opacity or transform, never blur radius; pair glows with a near-black ground for contrast |
| freefrontend neon collection (https://freefrontend.com/css-neon-effects/) | Rotating conic-gradient border through a masked pseudo-element |
| Brad Woods, "Juice" (https://garden.bradwoods.io/notes/design/juice) and hackread "The juice factor" (https://hackread.com/the-juice-factor-designing-game-feel/) | Every input gets more output than it deserves: sound on every press, squash on click, reveal animation on results, banner on milestones |
| aufaitux, UI/UX for children (https://www.aufaitux.com/blog/ui-ux-designing-for-children/) | 8 to 12 minute attention window per task; short loops with frequent informational feedback; immediate reaction to every tap |
| NN/g children on the web (already in lane 3) | Tap targets stay large; the only drag on the page is the optional panel splitter |

Applied in v3: dark ground, neon borders that rotate, flickering sign, sparks that follow the pointer, a blip on every button, confetti and a chime per result, a fanfare banner at word milestones, a cooking orb with a countdown. Kept out on purpose: streaks, timers, any second number next to the word count (P6).

## jep's reconciliation against v2 (same evening)

Already in v2: the positive prompt frame (12 style prefixes, every picture); outputs live in `D:\work\studio\kidstudio\out\`, outside any OneDrive known folder; remix (a gallery click prefills the words and settings); SAME seed (the "change one word" mechanic, minus the side-by-side view); big tap targets, no drag anywhere; per-item history in the gallery with its settings. So the agent's item 1 is done and items 3 (half) and the remix row are done.

Not yet built, ranked by jep for the girls, all local and ungated: (a) side-by-side "before / after" when SAME seed is on, S; (b) yesterday's-words opener from `log\K.txt` and `log\D.txt`, S; (c) karaoke line highlighting from ACE-Step's LRC output, M, needs the timestamps exposed in the ComfyUI graph first; (d) draw-to-picture with the ControlNet Union template (one extra 1 GB model file, an admin download), M; (e) sticker sheet + print, S once a printer is reachable; (f) Edge kiosk flag in `start.bat`, S, one line; (g) dictation mode (listen, then type, letters diffed), S, and the one with the strongest evidence for Hebrew-L1 spelling.

Not recommended now: a second-net NSFW classifier (the allowlist plus a fixed frame already bounds the prompt; the classifier's own author flags weakness on generated images); Qwen3Guard for lyrics (a 0.6B model in the loop for a kid's two lines is weight without a shown failure); LTX-2.3 video (a minute per clip, next-week quest as already decided).
