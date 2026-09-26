---
type: note
created: 2026-09-06
author: jep
project: tutoring
status: active
---

# Session 7 generator menu: verdict per modality (researched 2026-09-06)

Machine: RTX 4090 24 GB, 32 GB RAM, Windows 11, ComfyUI absent as of 2026-09-06 10:50 (port 8188 silent, GPU shows 5.2 GB in use by something else). Every "local" verdict depends on [[tutoring-session7-quest]] landing by Sunday night. Confidence per claim: H verified from a source opened today, M from a search summary or a single secondary source, L inferred.

## Verdict table

| Modality | Monday | Engine | Why | Fallback |
|---|---|---|---|---|
| Text-to-image | LOCAL | Z-Image-Turbo in ComfyUI, behind the Kid Studio allowlist page | 8 steps, 2 to 3 s per 1024px image on a 4090 (M); Apache 2.0, ungated Comfy-Org repack (H); native template `image_z_image_turbo` (H) | Meta AI in WhatsApp, `imagine a red cat` (H, S6 tape + Meta help page) |
| Text-to-speech | LOCAL | Kokoro-82M, pip package, Python 3.12 venv on the PC (CPU) | Apache 2.0, ungated, 327 MB (H); measured 09-06: 5.8 s first call, 2.2 s warm, on CPU (H); 54 voices (H) | Google Translate speaker button on her phone (H, no account) |
| Text-to-song | LOCAL, phone as equal option | ACE-Step 1.5 native ComfyUI template "ACE-Step 1.5 Music Generation AIO" | Apache 2.0, Comfy-Org repack, ComfyUI auto-downloads the files (H); "under 10 s per track on a 3090 and up" (M); 1 min of audio in 1.74 s on a 4090 at 27 steps (M, one benchmark) | D's own phone app (identity unknown, see open items); Suno free 50 credits/day (M) but ToS minimum age 13, so D only with parental consent, K excluded (H) |
| Image-to-video | PHONE | Meta AI in WhatsApp: photo of her drawing, `Animate` | Worked on 08-31 in Israel (H, S6 tape); refuses child photos, which is the rule anyway (H); 1 to 3 min wait (H, tape) | None local Monday; LTX-2.3 is the next-week quest |
| Text-to-video | OUT Monday | none | Local: LTX-2.3 is ungated, native in ComfyUI, fp8 needs ~16 GB and "seconds to ~2 minutes" per clip on a 4090 (M), a second ~30 GB download with no time to dry-run; Wan 2.2 5B is 2 to 4 min per 5 s clip (M). Phone: Meta AI Israel launch claims "generate videos from text" (M, ynet), unverified in WhatsApp | Idan tries `make a video of a cat dancing` in Meta AI on his own phone Sunday; if it works, it joins the phone menu as the fifth item |

## Per-modality notes

### Text-to-image
- Files (Comfy-Org/z_image_turbo, ungated, H): `z_image_turbo_bf16.safetensors` 12.3 GB → `models/diffusion_models/`; `qwen_3_4b.safetensors` → `models/text_encoders/`; `ae.safetensors` → `models/vae/`. The bf16 file is bigger than the Preflight's "~10 GB" line; int8 (6.2 GB) and nvfp4 (4.5 GB) variants exist in the same repo (H). Take bf16 on 24 GB.
- Negative prompts do nothing: distilled model at CFG 1 (H, Tongyi prompting guide discussion and two secondary guides). Consequence for the allowlist design: all steering lives in the positive prompt. Kid Studio prepends a fixed style phrase ("children's book illustration of ") and the allowlist is the only content gate. There is no second net.
- Speed claim "2 to 3 s at 1024px, 8 steps" (M, localaimaster 2026). The first render after model load is slower; warm up before 14:00.

### Text-to-speech
- Kokoro-82M: Apache 2.0, ungated on HF, `pip install kokoro soundfile` (H). espeak-ng is the fallback phonemizer for words outside its lexicon; on Windows it is a separate installer (H). Children's vocabulary sits inside the lexicon, so Monday runs without it; install it only if a word comes out garbled (L).
- Voices for the buttons: `af_heart` (American girl), `am_michael` (American boy), `bf_emma` (British girl); speed parameter exists, so SLOW is a real button (H for voice names, M for speed param name).
- Python 3.14 is jep's default interpreter; PyTorch wheels for 3.14 are documented with kokoro 0.9.4 in one 4090 setup (M). If pip fails, jep falls back to a 3.12 venv.

### Text-to-song
- ACE-Step 1.5: template names "ACE-Step 1.5 Music Generation AIO" and the split-files variant; lyrics typed into the prompt node with `[verse]` `[chorus]` tags; 4 GB VRAM minimum (H, techtactician 2026-02-09 and docs.comfy.org). The 1.74 s per minute of audio figure is one 4090 benchmark at 27 steps (M). Plan on 10 to 20 s per 30 s clip and be pleased.
- Suno: 50 free credits per day, about 10 songs, no rollover (M). ToS: 13 minimum, under-18 with parental consent (H). Rules K out, D in only with the mother's yes. Prefer the local engine.
- D's app, "the YouTube one that makes songs" (S6 open item 1): still unidentified after search; no YouTube first-party lyrics-to-song app surfaced. Ask D to show the icon at 14:00 and write the name in the record.

### Image-to-video and text-to-video
- Meta AI in WhatsApp: Hebrew launch confirmed for Israel, "edit and generate images and videos from text" (M, ynet, undated in the fetch). Help page: generate an image, then `Animate` with an optional prompt, result arrives as a notification (H). Quotas unpublished (H). Child-image refusal observed twice on 08-31 (H).
- LTX-2.3 (Lightricks, 2026-03-05): open weights under the LTX-2 license, free under $10M revenue, native ComfyUI templates for T2V and I2V, fp8 fits 16 GB (M). LTX-2.5 is gated behind a HF agree-and-access form, excluded by the anonymous-downloads rule (H). Next-week quest, one evening, dry run before any session.
- Wan 2.2 TI2V-5B: Apache 2.0, ungated, 2 to 4 min per 5 s clip on a 4090 (M). Too slow for a child at a keyboard.
- Gemini free tier has no video generation; Google Flow gives 50 free credits a day, about two Fast generations (M). Needs a Google account per girl; not for Monday.

## The allowlist mechanism (a nine-year-old cannot bypass it by accident)

Kid Studio: one local web page at `http://127.0.0.1:8787`, served by a Python standard-library server jep writes under `D:\work\studio\kidstudio\` (jep has full control of `D:\work`, verified with icacls today). ComfyUI's own UI stays closed; the girls never see a node graph.

1. Input path: one text box. The server lowercases the text, splits on spaces, and checks every token against `allow.txt` (one English word per line). One token missing → nothing is sent, the missing word turns red on screen with "new word, ask Idan". No partial send.
2. Adding a word: a plus button asks for a 4-digit PIN Idan knows. The word is appended to `allow.txt` and the prompt reruns. Every add is a spelling episode on purpose.
3. Steering: the server prepends a fixed phrase to every prompt ("children's book illustration of") and fills only the prompt and seed slots of an exported API-format workflow. Fill slots, never build graphs (Preflight D3 rule).
4. Counter feed: every accepted token not previously typed under that girl's profile is appended to `log/K.txt` or `log/D.txt` with a timestamp. The page shows her list; at 14:50 she copies it to her card by hand.
5. Same gate for SPEAK (Kokoro, sentence allowed if every word passes; punctuation stripped before the check) and SONG (ACE-Step, same rule per line).
6. Outputs land in `out/K/` or `out/D/`; a KEEP button shows a QR code to a LAN link on port 8788 serving only that girl's folder. Same WiFi, no account, phone camera opens it, "save to gallery".
7. Limits, stated: the gate is a word list, so two allowed words can still combine into something odd. Z-Image has no negative prompt to catch it. Seed list of ~180 words in the quest file, all nouns, colors, verbs and places from S1 to S6 vocabulary; nothing anatomical, no weapons, no "blood", no "naked", no "kiss".

## Keepable artifacts

| Source | How it becomes hers | Confidence |
|---|---|---|
| Kid Studio (PC) | QR on the KEEP button → LAN link → save to gallery; fallback USB cable (worked in S5, 151:26) or WhatsApp desktop to the mother | H for cable, M for LAN (needs one firewall allow click by the admin, see quest) |
| Meta AI in WhatsApp | Already in the chat; long-press → save, or forward to the mother | H |
| D's song app | Share sheet → WhatsApp to herself or the mother | M (app unknown) |
| Any | Print one image per girl on Monday if a printer is reachable | L, printer status unknown |

PairDrop (Snapdrop successor) still exists in 2026 and works LAN-only with no account (M); it is the fallback if the QR route fails, since it needs no build.

## Open items

1. D's song app identity (ask at 14:00).
2. Meta AI text-to-video inside WhatsApp in Israel: one try on Idan's phone Sunday settles it.
3. Whether the girls' phones have Meta AI enabled (the S6 session used D's phone for the song app and, by inference, Idan's phone for Meta AI; the tape does not say whose phone). Ask the mother Sunday, or bring Idan's old phone as station 2.
4. Session-4 counter values per girl, for the card headers. Not in any vault file jep can read; Idan's whiteboard photo if it exists.

## Sources opened today

docs.comfy.org z-image-turbo tutorial; huggingface.co/Comfy-Org/z_image_turbo tree; Tongyi-MAI/Z-Image-Turbo discussion 8 (prompting guide); huggingface.co/hexgrad/Kokoro-82M; docs.comfy.org ace-step-v1; techtactician ACE-Step 1.5 ComfyUI tutorial (2026-02-09); insiderllm local AI video guide (2026-02-05, updated 2026-08-18); docs.comfy.org ltx-2-3 (via search summary); ltxworkflow LTX-2.5 gated-repo guide (via search); ynetnews Meta AI Israel launch; meta.com help 1337455336906126; suno.com terms and help article 9720001 (via search); schlagmichdoch/PairDrop on GitHub (via search).
