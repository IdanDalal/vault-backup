---
type: task
created: 2026-09-06
updated: 2026-09-06
author: jep
project: tutoring
status: todo
priority: high
due: 2026-09-06
---

# Sunday quest for session 7, in plain English

Goal: by Sunday night the PC has a kid-safe page where a girl types English words and gets a picture, a voice, or a song in seconds. Everything else is already decided in [[tutoring-session7-verdicts]]; how Monday runs is in [[tutoring-session7-cheatsheet]].

## Already done (2026-09-06, 16:20)

Steps 1 and 2 (Idan): song model installed, both recipe files saved. Step 3 (jep): the kid page is built at `D:\work\studio\kidstudio\` and tested against the real ComfyUI: picture 7.6 to 11 s, song 9 s for a 30 s clip, speech 2 to 6 s, unknown word turns red, PIN add works, QR points at the home network. Test outputs cleared. Code backed up in the vault under `projects/kidstudio/`.

## What is left, in order

| # | Who | What | Time |
|---|---|---|---|
| 4 | Idan | Phone test of KEEP; one firewall line if it fails | 3 min |
| 5 | Idan | Test Meta AI on your own phone, ask the mother one question | 10 min |
| 6 | Idan | Sunday night, 5-minute run-through as if you were a girl, then `reset.bat` | 6 min |

## Idan's steps

**Step 1. Song model.**
Open ComfyUI. Open the template browser (the "Templates" entry in the left sidebar, or the home screen). Search for `ACE`. Open the one called "ACE-Step 1.5 Music Generation AIO". ComfyUI will say some model files are missing and offer to download them. Say yes. When it finishes, find the box with the lyrics, delete what is there, type:

```
[verse]
my name is Idan
I love to swim
```

Press Run. You are done when a song plays in the browser. Write down roughly how many seconds it took.
If the search finds no ACE template, stop here and tell me. Song moves to the phone on Monday and nothing else changes.

**Step 2. Two recipe files.**
A recipe file is ComfyUI's own description of a working graph. My page fills in the words and hands the recipe back to ComfyUI, so I never build graphs myself.
With the picture graph open: top-left menu → Workflow → Export (API). If "Export (API)" is missing, open the gear icon (Settings) → search "dev" → turn on Dev Mode, then look again. Save the file as
`D:\work\studio\kidstudio\workflows\picture.json` (create the folders if Windows asks).
Now open the song graph from step 1 and do the same, saving as
`D:\work\studio\kidstudio\workflows\song.json`.
You are done when both files exist. I read them from there; I cannot see anything else in your account.

**Step 4. Phone test of KEEP.**
Double-click `D:\work\studio\kidstudio\start.bat`. On the page, press the pink square, then KEEP. A QR code appears. Scan it with your phone (same WiFi as the PC). A folder page opens. That is the whole step.
If the phone shows "cannot connect": open a terminal as administrator and run
`netsh advfirewall firewall add rule name="Kid Studio keep" dir=in action=allow protocol=TCP localport=8788`
then scan again. If it still fails, NordVPN is the likely blocker (it is connected on this PC): disconnect it for the session, or turn on its "LAN discovery" setting. Last resort Monday: USB cable or WhatsApp to the mother.

**Step 5. Your phone, Sunday.**
Open WhatsApp → Meta AI chat. Type `imagine a red cat`. When the picture comes, use the Animate option on it. Then type `make a video of a cat dancing` and see whether Meta AI makes a video from words alone. Write the two results in the cheatsheet where it says `______` under TEXT→VIDEO.
Send the mother one line: do the girls' phones have Meta AI inside WhatsApp? If she does not know, bring your old phone as the second station.

**Step 6. Sunday night run-through.**
ComfyUI running, then double-click `start.bat`; the page opens full screen by itself. The PIN is in `pin.txt` (default 2468; change it in Notepad). Then, as if you were K:
1. Type `pink cat dancing`, press GO. A picture appears within 10 seconds.
2. Type `pink unicorn`. The word `unicorn` turns red. Press the plus, type the PIN, and the picture appears.
3. SPEAK tab: type `My name is Idan.` and press GO. The PC says it.
4. SONG tab: type two lines. A song plays.
5. Press KEEP. A QR code appears. Scan it with your phone, save the picture to the gallery.
All five worked: the quest is done. Double-click `reset.bat` so Monday's word lists start at zero. Close ComfyUI's own browser tab (leave ComfyUI itself running). Anything failed: tell me which number and what the screen said.

**Optional.** If SPEAK says a word in a garbled way, install espeak-ng for Windows (its GitHub releases page, an ordinary installer). I will name the word if it happens.

## jep's step 3 (done 16:20; kept here so the design stays readable)

I built one local web page on the PC. It lives in `D:\work\studio\kidstudio\`, a folder I can write to. The girls only ever see this page; ComfyUI stays hidden.

What the page does:
- Two big buttons, pink and green, so the page knows whose turn it is. No names on screen.
- One text box, one GO button. English on every button.
- Every word she types is checked against a word list I keep. All words known: the picture, voice, or song is made. Any word unknown: nothing is sent, the unknown word turns red with "new word, ask Idan". You press a plus, type a 4-digit PIN, and the word joins the list for good. That is the safety gate, and also the spelling moment.
- Her words for the day appear in a list on the right. At 14:50 she copies them to her card by hand.
- Style buttons for pictures: CARTOON, ANIME, CLAY, PIXEL. Voice buttons for speech: GIRL, BOY, BRITISH, SLOW.
- KEEP shows a QR code. Her phone scans it on the home WiFi and saves the file. No account, no cable.

How I build it, in order:
1. The page and the word check, with a fake picture, so it can be tested before your recipe files exist.
2. Wire the picture button to ComfyUI using `picture.json`, the song button using `song.json`.
3. Install the voice (Kokoro, a small free model, about 330 MB) in my own Python and wire SPEAK.
4. Put the starting word list in `D:\work\studio\kidstudio\allow.txt`, one word per line, about 180 words: colors, animals, school, food, places, feelings, actions, plus the words from sessions 1 to 6. You can open it in Notepad and add or delete lines any time.
5. Write `README.md` with the one line that starts the page, and put the same line in the cheatsheet.

I check each part before I say it works: a small test for the word gate, a real picture and a real song timed and logged, a screenshot of the page.

## Done when

Your step 6 passes, or by Sunday 22:00 the cheatsheet says plainly which of picture, voice and song run on the PC and which moved to the phone. Either way Monday runs.

## What can go wrong

1. The song template is missing or its download fails: song goes to the phone, 0 cost to the rest.
2. My Python cannot install the voice model: I try an older Python; if that fails, SPEAK goes to the Google Translate speaker button on her phone.
3. A game or another program is holding the graphics card (it held 5 GB this morning): close games before the run-through and before 14:00.
4. The whole PC side fails on Monday: station 1 becomes the laptop with Game Lab, both phones become station 2. Cheatsheet card F3 covers it.

## Starting word list (preview; the full list lands in allow.txt)

colors: red pink blue green yellow orange purple white black brown gold silver rainbow. animals: cat dog fish horse dragon unicorn bird pig cow sheep rabbit frog bear lion tiger monkey elephant butterfly dolphin whale shark pony kitten puppy. people: girl boy baby mom dad sister brother teacher friend princess queen king robot alien fairy wizard pirate ninja superhero. school: school class book pen pencil bag backpack desk board homework. places: house home room bed kitchen garden park beach sea sky moon sun star cloud rain snow forest mountain city street bus car train plane boat rocket castle island. food: ice cream cake pizza candy chocolate cookie apple banana strawberry juice milk water sushi tuna hot dog burger. things: squishy toy game ball doll lego phone computer video music song dance party balloon gift crown hat dress shoes glasses coins money piggy bank treasure. feelings and looks: happy sad funny silly cute scary cool magic sparkly fluffy tiny giant fast slow big small little. actions: dancing singing swimming flying running jumping sleeping eating drawing playing reading cooking laughing smiling, and the same verbs plain. glue words: a an the and with in on of my your is are am I love like want go to name years old.
