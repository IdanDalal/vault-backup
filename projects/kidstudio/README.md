# Studio (folder still named kidstudio)

A page where a girl types English words and gets a picture, a voice, or a song. Every word must be on the list in `allow.txt`; an unknown word turns red and needs Idan's PIN.

## Start (Monday, before 14:00)

1. ComfyUI must already be running (its window open, `http://127.0.0.1:8188` answers).
2. Double-click `start.bat` in this folder. A black window opens (the server; leave it) and the page opens full screen at `http://127.0.0.1:8787`.
3. Close ComfyUI's own browser tab if one is open. The girls only see the Studio page.
4. Make one warm-up of each: a picture, a SPEAK line, a song. The first of each is slower.

Or from a terminal: `D:\work\studio\kidstudio\venv\Scripts\python.exe D:\work\studio\kidstudio\server.py`

## After jep changes the code

The black server window holds the old code in memory. Close it (click its X), then double-click `start.bat` again. That is the whole reload.

## What v5 added (2026-09-07, late morning)

- STORY tab: one story = 4 frames, fixed: 1 BEGINNING (who is it? where are they?), 2 PROBLEM (what goes wrong?), 3 TRY (what do they do about it?), 4 END (how does it end?). Each frame = the four picture slots + a SAY IT line. GO makes the picture and speaks the line (about 5 s warm), plays it, shows the frame in the filmstrip, moves to the next frame. WHO OR WHAT is locked to the frame-1 hero from frame 2 on (tap SAME HERO to unlock); SEED defaults to SAME so the cat stays the cat. The previous frame stays on screen while she types the next one. Tapping a frame in the strip reopens it; GO makes it again. The story is saved per girl in `out\K\story.json` and survives a reload.
- MAKE THE MOVIE (after 2 or more frames): every frame becomes a 4 s clip (longer if her line is longer) with a slow zoom in or out, her spoken lines as narration, and her newest SONG of the day under it at 22 % volume, fading out at the end. 1280x720 mp4 in `out\K\`, plays on the stage, appears in the GALLERY as a clapper tile, KEEP sends it with everything else. Measured: 4 frames, 16 s of video, 1.4 s to stitch. NEW STORY archives the old one (`story-HHMMSS.json`) and clears the strip; the pictures and the movie stay in the gallery.
- ffmpeg: the static binary from the `imageio-ffmpeg` wheel inside `venv` (about 60 MB, installed 2026-09-07). `movie.py` holds the pipeline; run `venv\Scripts\python.exe movie.py a.png b.png x.wav` to dry-run it on any files.
- SPEAK has slots too: WHO, DOES WHAT, WHERE, AND THEN. The page joins them into sentences with a capital and a full stop ("My pink cat is dancing in school. She is happy."), which is what Kokoro reads.
- SONG has slots: WHO, WHAT HAPPENS, THE HOOK, THE END. The lyrics become verse (who, what happens), chorus (the hook twice), verse (the end), chorus (the hook). The `[chorus]`/`[verse]` tags are added by the page and skipped by the word gate. Every slot has its own YOU CAN signposts, same rule as pictures: questions, never words to copy.
- The signpost question next to GO is cleared when switching tabs.
- `allow.txt` gained 43 grammar words (she, he, they, them, can, only, from, not, then, next, now, first, last, again, very, this, that, there, here, has, have, was, were, up, down, out, into, under, over, behind, because, but, or, one, three, four, five, ten, all, some, every, always, never). Delete any you do not want; they are at the end of the file.
- The stage panel no longer grows wider than the screen when a row has many chips (SPEAK's 16 voices did that).

## What v4 added (2026-09-07, morning)

- The word "kid" is gone from the page, the window title and the server line. The sign in the empty stage is gone too; the title shows once, top left. The folder name and the firewall rule name are unchanged on purpose (paths in the cheat sheet, a rule that may already exist).
- PICTURE has four ingredient slots instead of the blank box: WHO OR WHAT, WHERE, LOOK CLOSER, YOUR RULES. Only WHO OR WHAT is required (one word still works). The prompt is the filled slots joined with commas, in the order who, closer, where, rules; the gallery caption shows that joined text and a gallery click refills the slots.
- Under the slots, one YOU CAN strip shows the signposts for the slot she is in (dashed chips: WHO, HOW MANY, SIZE, COLOR, DOING, FEELING for the hero; PLACE, TIME, WEATHER... for the place; ANGLE, CLOSE OR FAR, MIDDLE, EDGE, ONLY, NO, SAME for the rules). Tapping a signpost speaks its question ("from where do we look?"), shows it next to GO, and puts the cursor back in the slot. Signposts never type anything into the slot. Edit the lists in `SLOTS` at the top of `server.py`.
- Background is a lava lamp: eight blurred blobs drifting up and down, hue cycling through the whole spectrum every 36 s, drawn on a canvas at one sixth resolution. No fixed color in any corner, so it no longer fights the pink or the green profile.
- The milestone banner (10, 15, 20... WORDS) fires only for the girl whose typing crossed the number, once, and lasts 5.4 s with three confetti bursts (was 2.7 s, and it re-fired when switching from one color to the other).
- `archive\server.v3.py`, `archive\index.v3.html`, `archive\README.v3.md` are the previous version.

## What v3 added (2026-09-06, night)

- Dark neon studio: color-cycling blobs, a moving floor grid, neon sparks that follow the mouse, rotating conic borders on every panel, a flickering sign, glow on everything in the girl's color.
- LISTEN tab (dictation): press the ear, a sentence is spoken (half the time one she typed herself, otherwise a frame built from her own words), she types it, GO shows every letter green or red and the score. Correct words go to her counter. Evidence: Hebrew-L1 kids miss English vowels and digraphs most; TTS dictation matches teacher dictation.
- Warm-up opener: when she picks her color, the stage shows three words from her own list; tap to hear, type one to start.
- SEED: SAME now shows BEFORE and AFTER side by side with the changed word lit in yellow.
- Every word chip in MY WORDS speaks when tapped (never counts again).
- Milestone banner and fanfare at 10, 15, 20, 25, 30, 40, 50, 75, 100 words; the number is hers, no comparison.
- Resizable: drag the thin glowing bar between the stage and MY WORDS; the text box drags taller. Both remembered per browser.
- Word lists were reset on 2026-09-06 and seeded from previous lessons: K 7 words (cat, red, sun, light, water, oil, jump), D 12 words (cat, red, sun, girl, fish, tuna, school, squishy, draw, video, dragon, pig). Old outputs moved to `archive\2026-09-06\` (outside the phone folder).

## What the page has (v2, 2026-09-06 evening)

- PICTURE: 12 styles (cartoon, anime, clay, pixel, 3d, watercolor, crayon, sticker, comic, lego, neon, plush), shape (square, wide, tall), how many (1 to 4, each adds ~8 s), seed NEW or SAME (SAME keeps the last picture's seed, so changing one word shows what that word does).
- SPEAK: 16 voices (American and British, girls and boys, Santa included), speed slider 0.5 to 1.6.
- SONG: 12 genres, singer (girl, boy, kids choir, robot), mood, tempo, length 10 to 90 s.
- GALLERY tab: everything she made today, click to replay on the TV, with the words and settings under each item.
- Audio player: play/pause, seek bar, time, volume, speed x0.5 to x2, a live bar visualizer.
- Cooking bar with a countdown learned from the last run; confetti and a chime on success; a buzz and a red shaking word on a refusal; particles and a slow color-cycling sky.
- Page URL options for a second screen: `http://127.0.0.1:8787/?who=K&tab=gallery`.
- Change the lists of styles, genres, voices at the top of `server.py`; the page reads them at load.

## Files you may touch

- `allow.txt`: the word list, one word per line. Add or delete lines in Notepad any time; the server reads it fresh on every GO.
- `pin.txt`: the PIN for adding a word live. Default `2468`. Change it.
- `log\K.txt` and `log\D.txt`: the words each girl typed, with time stamps. This is the counter feed. Empty before a session if you want a clean list.
- `out\K\` and `out\D\`: their pictures, songs and voices. What the phone downloads.
- `log\build.txt`: every generation with its seconds; `log\server.out`: the server's own chatter.

## Send to phone (KEEP button)

KEEP shows a QR code pointing at `http://<this PC's home address>:8788/K/` (or `/D/`). Her phone must be on the same WiFi. If the phone cannot open the link:
1. Windows firewall: run once as admin: `netsh advfirewall firewall add rule name="Kid Studio keep" dir=in action=allow protocol=TCP localport=8788`
2. NordVPN is installed on this PC; if it is connected, turn on its "LAN discovery" setting or disconnect it for the session.
3. Fallback: USB cable, or send the file to the mother from WhatsApp desktop.

## Measured on this PC (2026-09-06)

Picture 1024px, 8 steps: 7.6 to 8.6 s. Song, 30 s clip: 9.0 s. Speech: 5.8 s on the first call, 2.2 s after (CPU).

## Safety notes

The word list is the only gate. Z-Image-Turbo ignores negative prompts, so nothing else filters the picture. The page listens on 127.0.0.1 only; the download helper on 8788 serves the `out\` folder only, read-only.
