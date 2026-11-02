---
type: research
created: 2026-11-02
author: Agent lyrics-screen-run
---

# Lyrics screen-read run (7 songs)

## Verdict

- Filed: all 7 songs, each as a new `D:\work\AIMVs\lyrics\official\<song>.txt` (no file existed, nothing overwritten). `_COVERAGE.md` rows updated to source kind `screen-read`.
- Screen-checked share: **423 of 476 lines (89 %)**; per-song mean 87.7 %; range 76 % (Off Switch) to 99 % (Thus Spoke Compute).
- Corrections applied: **92** (80 high, 12 medium confidence). 2 reader proposals rejected at lead review.
- For Idi's ear (screen absent AND Whisper looks wrong): **4 spots**, all end-of-track lines that read as Whisper outro hallucinations.
- Accuracy is unscored: these songs have no ground-truth lyrics. Lead spot check: 6 frame images covering 10 applied corrections, all 10 match the screen.

## Method (changes from the test)

- Whisper: faster-whisper large-v3, same settings as the test (`whisper_words.py`, aimv-lab venv, RTX 4090, foreground, one song at a time). Output matches the existing `.lyrics.txt` files line for line on all 7 (0 differing lines).
- Flags: unchanged rules, T = 0.5 (`flag.py`). 163 flags in 123 events; Thus Spoke Compute alone 73 flags (33 out-of-vocabulary: economists' names).
- Line sweep (new, `sweep.py`): one frame per Whisper line at 0.25 s before the last sung word, 6 per grid at 640 px tiles, each tile labelled with line number, time and Whisper text. 83 grids for 476 lines.
- Extra frames on demand (new, `extra.py`): readers pulled extra 6-frame grids where a line-end tile showed only the tail of a kinetic line. Budget about 10 calls per song.
- Reading: one reader agent per song, fixed brief (`READER-BRIEF.md`): corrections only from screen text; screen trims and reformats keep the sung words; number, apostrophe, spacing, hyphen, casual-form and contraction variants not applied; diegetic text counts only when it reproduces the sung line.
- Screen-checked = at least half of the line's words visible across the frames read. Lines with fewer visible words, or none, count as unchecked.
- Lead review: every proposal read; 2 rejected (`rejected.json`): The End Of The Show 2:47 (screen reorders "when I can try it" into the question "when can I try it?", Whisper p 0.99+ on every word); Off Switch 1:38 (HOSPITALS is a card label beside WATER, both tagged STOPPED). One reader replacement ended in an em dash (Run It Again 1:23, after "sa"); filed as "sa-".
- Cost: 7 reader agents, about 0.87 M tokens in total.

## Per song

| Song | Lines | Screen-checked | Corrections | Uncertain spots for Idi's ear |
|---|---|---|---|---|
| Thus Spoke Compute | 90 | 89 (99 %) | 44 | 2:20 dropped seam duplicate "work" (p 0.03, after "network"); 3:36 dropped duplicate "great" (p 0.04); 3:03 "footnote and the" (inserted "and"); 2:41 "Oh," kept, absent on screen; 5:09 "We'll be right back." |
| Count Me In | 60 | 58 (97 %) | 16 | 0:08 "10, 9, 8, 7, nah" (NAH card in the slot Whisper heard as "9"); 1:30 "got" inserted ("Bloom, got better things") |
| Compacting Conversation | 79 | 76 (96 %) | 8 | none beyond the 3 lines with no text (0:43, 1:37, 2:11); Whisper reads plausible there |
| Run It Again | 67 | 58 (87 %) | 5 | 1:23 "I think I'd be sa-" (screen cuts the word, Whisper had a censored "s***"); 4:46 "Thanks for watching!" |
| Ignore Previous Instructions | 51 | 41 (80 %) | 9 | 1:28 "Lethal trifecta" (typed LETHAL TRIFECTA in sync; Whisper "That's the trifecta"); 1:16 "It summarized" (inserted "It"); 2:53 "You are a helpful assi-" (typing cuts to black; ear may hear "assistant"); 0:43 "eh, eh" (a giant IG- on screen hints at an "ig-, ig-" stutter); 1:02 "your keys" vs 1:50 "the keys" |
| The End Of The Show | 92 | 73 (79 %) | 7 | 4:03 "glide" added from screen, and 4:07 "The terms": Whisper's "The" (p 0.10) sits where "glide" was sung, possible stray word; 3:18 "to pay" inserted; 3:37 "it suggested" (Whisper "it's suggested"); 2:47 "when I can try it" kept; 5:59 "Thank you." |
| Off Switch | 37 | 28 (76 %) | 3 | 0:10 "humming in the wall" (inserted "in"); 1:38 "the hospital stopped" kept (card reads HOSPITALS STOPPED); 2:22 "Bye." |

Notable fixes, all read from the screen:

- Thus Spoke Compute: hook "The slow / The smoke / The Spoke" to "Thus Spoke Compute" (8 lines); Darren to Daron, Solo to Solow (x2), Almost to Baumol's, Jan to Yann, Grime and to Riemann, Sims to Shenzhen, cat pecks to capex, the pot to the pod, force to four, fuck knows to footnote's.
- Count Me In: the p(doom) / p(bloom) wordplay; Whisper heard Boom, key, single numbers, to now, call a stop where the screen shows Bloom, P, same old numbers, tonight, call it slop.
- Compacting Conversation: summer rain to summary; curse is to cursor's; laugh to laughed (x3); He said to You said.
- Run It Again: both choruses ("and let's go out", "when the lights go out") read "and the lights go out".
- Ignore Previous Instructions: always aloud to always allow; soar to sold; sentencing to sentence; his eyes to its eyes.

Unchecked lines by song (few or no lyric words on screen): Off Switch 9 (big kinetic words show fragments), The End Of The Show 19 (sparse diegetic text; image-only stretches 2:59 to 3:03 and 5:11 to 5:27), Ignore Previous Instructions 10 (single kinetic words such as TOLD, KINGDOM), Run It Again 9, Compacting Conversation 3, Count Me In 2, Thus Spoke Compute 1.

## For Idi's ear

Only spots where the screen shows no lyric AND Whisper looks wrong.

| Song | Time | Whisper | Why it looks wrong |
|---|---|---|---|
| Run It Again | 4:46 | Thanks for watching! | outro title card only; stock Whisper end-of-audio phrase |
| Thus Spoke Compute | 5:09 | We'll be right back. | instrumental outro, sphere animation, no text; p below 0.5 |
| The End Of The Show | 5:59 | Thank you. | last 0.1 s of the file; screen still holds the previous lyric card |
| Off Switch | 2:22 | Bye. | red-dot outro card; p below 0.5 |

All 4 stay in the filed text, since the rules allow corrections from the screen only.

## Files

- Filed lyrics: `D:\work\AIMVs\lyrics\official\` `Run It Again.txt`, `Ignore Previous Instructions.txt`, `Count Me In.txt`, `The End Of The Show.txt`, `Compacting Conversation.txt`, `Off Switch.txt`, `Thus Spoke Compute.txt`.
- Coverage: `D:\work\AIMVs\lyrics\official\_COVERAGE.md` (7 rows edited, one count line added; prior copy `_COVERAGE.before.md` in the job folder).
- Job folder `C:\Users\jep\.claude\jobs\99182c36\tmp\ocr\`: new scripts `sweep.py`, `extra.py`, `apply.py`, `update_coverage.py`, `READER-BRIEF.md`; `frames.py` and `sweep.py` step back when a time falls past the last video frame. Per song: `<song>.whisper.json`, `.flags.json`, `.worklist.txt`, `.screen.json` (every line's screen status, proposals with frame and screen text, kept differences), `.corrected.txt`; frames under `<song>\sweep`, `\grids`, `\sheets`, `\extra`. Run summary `apply.json`, rejections `rejected.json`.
