---
type: note
created: 2026-09-07
author: jep
project: tutoring
status: active
---

# Studio, part two: connections (2026-09-07, 10:20)

Part one (categories) shipped this morning as Studio v4, live on `http://127.0.0.1:8787`, code mirrored in `projects/kidstudio/`. This note is the proposal for part two: turning separate outputs into one artifact. Research by the connections-research agent (web only, nothing downloaded) is appended below in full; "V" = verified on the source page, "I" = inferred.

## The unified artifact: a movie she made

One story = 4 frames, fixed count. Each frame is a picture from the v4 ingredient slots, plus one spoken line in her words. Her four lines become the lyrics of one song. The movie stitches frames, narration and song into one mp4 that KEEP sends to her phone. One process, one output, every generator feeding the same thing.

Why 4 fixed frames: the picture-series task is the only mechanism in the research with a measured language gain (sequenced group beat random order on narrative writing, 53 adults, PMC8615726, I). Every other coherence pattern (Toontastic's arc slots, Pixton's reused character, Storybird's locked art) has review evidence only.

## Three coherence mechanisms, in the same voice as the signposts

| Mechanism | On screen | Effect |
|---|---|---|
| Arc slots | Frame 1 BEGINNING (who? where?) → 2 PROBLEM (what goes wrong?) → 3 TRY (what does she do?) → 4 END (how does it end?) | "What happens next?" is asked by the page, in a question, never by Idan |
| Hero lock | After frame 1, WHO OR WHAT is prefilled and dimmed; SEED defaults to SAME | Same character across frames; one word changed per frame stays visible |
| Previous frame beside the new one | Frame N-1 shown small at the left of the stage while she types frame N | She writes against her own picture, the Storybird pattern |

These are questions and locks. No content words appear. The SAME signpost under YOUR RULES already points here.

## Video: what can move, and when

| Route | Cost | Wait per frame | Ready |
|---|---|---|---|
| Ken Burns pan-and-zoom on her stills + narration + song, ffmpeg via `imageio-ffmpeg` (60 MB pip wheel, static ffmpeg.exe; not yet in the studio venv, checked 10:20) | 60 MB, ~90 min build, one dry run | seconds | today if the word comes by 11:30 |
| Wan 2.2 TI2V-5B, start image + text, Comfy-Org repack, Apache 2.0, native template | 13 GB | 5 s 720p "under 9 min" on a 4090 (V, unoptimized); 768x512 short clips faster (I) | this week; too slow for a live session unless small and pre-rendered between sessions |
| Wan 2.2 14B I2V fp8 + lightx2v 4-step LoRAs | 36 GB | ~2 min per clip (I) | next week, if 5B quality disappoints |
| Qwen-Image-Edit-2511 ("this picture, now the cat is in the sea") | 30 GB, shares 9.4 GB encoder with HunyuanVideo 1.5 | seconds with Lightning LoRA (I) | the real "next frame" tool; frame N edits frame N-1 instead of regenerating |
| LTX-2.5 | 50 GB, click-gated | | excluded (gate) |

The phone station already does draw→video in 1 to 3 min via Meta AI (cheatsheet). Local video is a between-sessions batch job until a clip costs under 30 s.

## Options

A. **Story mode today, Ken Burns movie.** STORY tab: 4 arc slots, hero lock, previous frame beside, MOVIE button, KEEP sends the mp4. Risk: a pipeline dry-run on this PC has not happened yet; if ffmpeg misbehaves, the tab ships without MOVIE and the girls still get the 4-frame strip. Build ~90 min, done by 13:15 if the word comes by 11:30.
B. **Coherence only today, video this week.** Arc slots + hero lock + previous frame (about 40 min), no ffmpeg. Wan 2.2 TI2V-5B downloads tonight, movie stitching next session.
C. **Nothing new today.** v4 as is; the session runs on the cheatsheet; part two lands for session 8 with video tested calmly.

Recommendation: **A**, on the condition that the dry run passes by 12:30; otherwise A degrades to B automatically, nothing else changes. Reasoning: the 4-frame strip is what holds attention (one thing to finish), and the movie is the reason to finish it. Overrule if you would rather keep Monday's menu untouched (C).

Say the word: A, B, or C.

## Research report (connections-research agent, 2026-09-07, verbatim)

## 1. Image-to-video, local, ungated, ComfyUI, 24 GB

Ranked for "fastest acceptable storybook clip on a 4090". Start image + text = the model animates a given first frame under a motion prompt.

| Option | What | Download (GB) | Gated? | Comfy native? | Speed on 4090 | Start image + text? | Source | V/I |
|---|---|---|---|---|---|---|---|---|
| 1. Wan 2.2 TI2V-5B | 5B hybrid T2V/I2V, 720p 24 fps | 10 model + umt5 fp8 + VAE, ~13 total | No, Comfy-Org Apache 2.0 | Yes, template | 5 s 720p "under 9 minutes" unoptimized; shorter 768x512 clips proportionally faster (I) | Yes | [Comfy-Org repo](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models), [Wan2.2 README](https://github.com/Wan-Video/Wan2.2), [docs.comfy](https://docs.comfy.org/tutorials/video/wan/wan2_2) | V |
| 2. LTX-Video 0.9.8 2B distilled | Small, fast, weaker quality | 6.34 (fp8 4.46) + t5xxl_fp16 ~9.5 (I) | No | Yes, template | 0.9.5: 768x512 5 s in 1 m 30 s | Yes | [HF tree](https://huggingface.co/Lightricks/LTX-Video/tree/main), [localaimaster](https://localaimaster.com/blog/local-ai-video-generation), [docs.comfy](https://docs.comfy.org/tutorials/video/ltxv) | V |
| 3. Wan 2.2 14B I2V fp8 + lightx2v 4-step LoRAs | Best motion and quality | 14.3 + 14.3 + umt5 + VAE + LoRAs 0.64 + 0.74, ~36 | No | Yes, LoRA in templates | ~4 min per 81 frames 480p without LoRA (I); LoRA "about 2x faster" (V) so ~2 min (I) | Yes | [lightx2v LoRAs](https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main), [Comfy blog](https://blog.comfy.org/p/comfyui-wan22-fun-inp-support) | V/I |
| 4. LTX-2 19B distilled | Video + audio in one pass | fp8 27.1 or fp4 20 + Gemma3 fp4 9.45 + VAE, ~30 to 37 | No, Comfy-Org/ltx-2 hosts the Gemma repackage | Yes, template | Claim: 8 s 720p in ~25 s with NVFP4; 4090 lacks FP4 tensor cores, so treat as 5090 number (I). fp8 T2V 4 s 720p 3 to 5 min (V) | Yes | [Comfy-Org text encoders](https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders), [codersera](https://codersera.com/blog/run-ltx-2-on-comfyui-locally-and-free-generate-videos-with-audio/), [localaimaster setup](https://localaimaster.com/blog/ltx-2-local-setup-guide) | V |
| 5. HunyuanVideo 1.5 480p I2V step-distilled fp8 | 8.3B, 8 to 12 steps | 8.34 + qwen2.5-vl fp8 9.38 + byt5 0.44 + VAE, ~19 | No (Tencent community license, no click-gate seen) | Yes (I) | "within 75 seconds" per Tencent README (I) | Yes | [Comfy-Org diffusion](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/tree/main/split_files/diffusion_models), [text encoders](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/tree/main/split_files/text_encoders) | V/I |
| 6. LTX-2.3 22B distilled | Newer, 4K capable | 46.1 bf16; fp8 exists, size unverified; Gemma 3 from Google repo is gated, the Comfy-Org fp4 file reportedly works (I) | Model no, Google encoder yes | Yes, since ComfyUI 0.16.1, March 2026 | No 4090 figure found | Yes | [HF tree](https://huggingface.co/Lightricks/LTX-2.3/tree/main), [Thunder](https://www.thundercompute.com/blog/ltx-2-3-comfyui) | V |
| 7. LTX-2.5 22B | Newest, multishot | 50 | Yes, "Agree and Access" click-gate, Gemma 4 inside the gated repo | Yes | None published; 22.67 GiB resident on 4090 | Yes | [smeltcore](https://smeltcore.com/recipes/ltx-2-5-on-rtx-4090-fitting-the-22b-audio-video-dit-in-24-gb-via-comfyui-int8), [HF](https://huggingface.co/Lightricks/LTX-2.5) | V |
| 8. CogVideoX-5B I2V | 2024 model | ~20 (I) | No | No, kijai wrapper only | Slower than all above (I) | Yes | [search](https://stable-diffusion-art.com/cogvideox-i2v/) | I |

Under 2 hours today: options 1 and 2 (13 GB and 11 GB). Next week: 3, 4, 5. Excluded: 7 (gated), 8 (custom node, old).

## 2. Cheapest fallback: Ken Burns from stills, no new model

| Option | What | Download (GB) | Gated? | Comfy native? | Speed on 4090 | Start image + text? | Source | V/I |
|---|---|---|---|---|---|---|---|---|
| imageio-ffmpeg 0.6.0 | pip wheel bundles a static ffmpeg.exe for Windows, ~60 MiB; `get_ffmpeg_exe()` returns its path | 0.06 | No | n/a | Seconds per clip (I) | n/a | [PyPI](https://pypi.org/project/imageio-ffmpeg/), [README](https://github.com/imageio/imageio-ffmpeg) | V |
| ComfyUI core | requirements.txt has `av>=17.0.0` (PyAV), so native Create Video / Save Video nodes need no ffmpeg CLI; no ffmpeg.exe is bundled (I) | 0 | No | Yes | n/a | n/a | [requirements](https://raw.githubusercontent.com/comfyanonymous/ComfyUI/master/requirements.txt) | V |
| Video Helper Suite | requirements.txt = `opencv-python`, `imageio-ffmpeg`; prefers system ffmpeg, falls back to the bundled one | 0.06 | No | Custom node | n/a | n/a | [VHS req](https://raw.githubusercontent.com/Kosinkadink/ComfyUI-VideoHelperSuite/main/requirements.txt), [issue 149](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/149) | V |

Get the binary (portable ComfyUI uses its own Python):

```
python_embeded\python.exe -m pip install imageio-ffmpeg
python_embeded\python.exe -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
```

zoompan options z, x, y, d, s, fps confirmed on the [ffmpeg filter docs](https://ffmpeg.org/ffmpeg-filters.html#zoompan) (V). Upscale before zoompan to kill jitter ([ffmpeg-micro](https://www.ffmpeg-micro.com/blog/ffmpeg-zoompan-filter-ken-burns-zoom-and-pan-without-the-jitter), V). Pipeline, untested on this PC (I):

```
:: per frame i: 4 s, slow centered zoom, narration padded to 4 s
ffmpeg -y -loop 1 -framerate 25 -i img1.png -i nar1.wav ^
 -vf "scale=3072:-2,zoompan=z='min(zoom+0.0015,1.3)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=100:s=1024x576:fps=25,format=yuv420p" ^
 -af apad -t 4 -c:v libx264 -c:a aac clip1.mp4
:: list.txt lines: file 'clip1.mp4' ... then concat, then mix song at 25 %
ffmpeg -y -f concat -safe 0 -i list.txt -c copy story.mp4
ffmpeg -y -i story.mp4 -i song.wav -filter_complex "[1:a]volume=0.25[bg];[0:a][bg]amix=inputs=2:duration=first[a]" -map 0:v -map "[a]" -c:v copy -c:a aac movie.mp4
```

## 3. Story coherence in children's tools

| Option | What (mechanism) | Download (GB) | Gated? | Comfy native? | Speed on 4090 | Start image + text? | Source | V/I |
|---|---|---|---|---|---|---|---|---|
| Toontastic 3D | 5 arc slots: setup, conflict, challenge, climax, resolution; characters persist across scenes. Official site now redirects to google.com. Evidence: teacher reviews only | n/a | n/a | n/a | n/a | n/a | [SLJ](https://www.slj.com/story/toontastic-3d-new-and-free-from-google-education) | I |
| Storybird | Locked artwork library; child writes to fixed art. No engagement data cited | n/a | n/a | n/a | n/a | n/a | [Ezeh 2020, TESL-EJ](https://tesl-ej.org/wordpress/issues/volume24/ej93/ej93m1/) | V |
| Book Creator | Page and comic templates, text-to-speech; review claims TTS aids L2 engagement, no measurement | n/a | n/a | n/a | n/a | n/a | same | V |
| Storyjumper | Reusable scenes and props, voice narration per page | n/a | n/a | n/a | n/a | n/a | same | V |
| Pixton | One built character reused across panels | n/a | n/a | n/a | n/a | n/a | [saashub](https://www.saashub.com/compare-pixton-vs-storybird) | I |
| Scratch | Sprites persist across backdrops | n/a | n/a | n/a | n/a | n/a | general knowledge | I |
| StoryboardThat | 6-cell plot diagram: exposition, conflict, rising action, climax, falling action, resolution | n/a | n/a | n/a | n/a | n/a | [StoryboardThat](https://www.storyboardthat.com/articles/e/plot-diagram) | I |
| Story Spark | GPT-generated personalized stories for parents; no child-authoring sequence | n/a | n/a | n/a | n/a | n/a | [storyspark.ai](https://storyspark.ai/blog/create-your-childrens-story-with-story-spark-instead-of-chatgpt) | I |
| Picture series, EFL | 4-part graded picture sequence, easy to hard; 53 adults; sequenced group outscored random-order group on narrative writing | n/a | n/a | n/a | n/a | n/a | [PMC8615726](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8615726/), [ERIC EJ1075242](https://files.eric.ed.gov/fulltext/EJ1075242.pdf) | I |

Evidence quality: writing-score gains exist for picture series. Engagement evidence for every tool above is anecdotal.

## 4. Consistent character without training

| Option | What | Download (GB) | Gated? | Comfy native? | Speed on 4090 | Start image + text? | Source | V/I |
|---|---|---|---|---|---|---|---|---|
| A. Same seed + prompt, one word changed | In use | 0 | No | Yes | 8 s | n/a | current studio | V |
| B. Fixed hero-description prefix | Same 15-word character line every frame, plus A | 0 | No | Yes | 8 s | n/a | practice, no study found | I |
| C. Qwen-Image-Edit-2511 | Previous frame + instruction ("now the cat is in the sea"); character preservation is a stated feature; Lightning 4-step LoRA exists | fp8mixed 20.5 + qwen2.5-vl fp8 9.38 (same file HunyuanVideo 1.5 uses) + VAE, ~30 | No, Comfy-Org Apache 2.0 | Yes, template since Dec 2025 | ~16 GB VRAM fp8 (I); seconds per edit with Lightning (I) | Yes | [docs.comfy](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511), [HF tree](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/tree/main/split_files/diffusion_models) | V |
| D. IP-Adapter for Z-Image | Blog shows a custom IPAdapter node, model unnamed, style over identity | unknown | unknown | No | n/a | n/a | [zimage.run](https://zimage.run/blog/ei-016-ip-adapter-style-transfer-en-20260503) | V |
| E. ControlNet Union 2.1 for Z-Image | Pose or edge lock, custom node | ~2 (I) | No (I) | No | n/a | n/a | [SD Art](https://stable-diffusion-art.com/z-image-controlnet-union/) | I |

## Recommendation for a storytelling studio

1. Today, 14:00: no new model. `pip install imageio-ffmpeg` (60 MB), chain Z-Image stills + Kokoro narration + ACE-Step song into one mp4 with the zoompan pipeline above. Dry-run it once before the session.
2. This week: Wan 2.2 TI2V-5B, 13 GB, ungated, native template, verified 4090 figure, start image + text. Test 768x512 at 49 frames first.
3. If 5B quality disappoints: Wan 2.2 14B fp8 + lightx2v LoRAs (36 GB, ~2 min per clip, inferred).
4. Skip LTX-2.5 (click-gated) and CogVideoX (custom node). LTX-2 is the audio-plus-video bet for later.
5. Add Qwen-Image-Edit-2511 (30 GB, shares the 9.38 GB encoder with HunyuanVideo 1.5) so "this picture, now the cat is in the sea" edits the previous frame instead of regenerating.
6. Coherence mechanism 1: fixed number of frames in a sequence, ordered easy to hard (picture series, the only mechanism with measured writing gains).
7. Coherence mechanism 2: five arc slots on screen, Toontastic style, each slot a "who / where / what goes wrong / how it ends" prompt.
8. Coherence mechanism 3: locked hero line prepended to every prompt, plus the previous frame shown beside the new one (Storybird and Pixton pattern, review evidence only).
