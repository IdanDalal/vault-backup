---
type: project
created: 2026-10-18
author: jep
status: active
---

# Handoff 2026-10-18: Knowledge Cutoff, Idi's ten notes on the full video

START HERE in a fresh session. Read this file, then [[knowledge-cutoff-treatment-2026-10-17]] (the style bible, section 12 is the bar), then [[knowledge-cutoff-waves-bc-2026-10-17]] (the state of all 18 modules), then `D:\work\aimv-lab\kc-engine\reports\waves-bc-briefs.md` (the agent contract and the ten binding lessons).

## 1. Idi's verdict, 2026-10-18 (his words)

"WOOOWWWWWW!!! This is a generational leap over the old engine's results! We're now playing at the highest possible level like the inspiration videos." Then ten notes (section 3). His standing care: no new harsh rule. Each fix is a nuanced rule that improves the edge cases without constraining the rest of the video ("always one-shot, never cut" was such a rule, and it hurt).

## 2. Where things stand

| item | state | where |
|---|---|---|
| full video | 194.12 s, 1080p 60 fps, all 18 modules, silent tail; rendered as 4 joined segments (Idi saw the joins: note 1) | `D:\work\AIMVs\ours\video\full\kc-full-1080p.mp4`, sheet `full-sheet.jpg` |
| engine | git `D:\work\aimv-lab\kc-engine`, last commit `bc10ef7`+ (all modules accepted) | `app\src\scenes\*.ts` |
| reports | per agent and per critic | `kc-engine\reports\` |
| brightness per frame | 11,646 values of the full render | `kc-engine\out\full\yavg.txt` |
| vault branch | `worktree-aimv-phase0`, pushed | reports in `projects/AIMV/` |

## 3. The ten notes: rule, evidence, done-state

### Note 1. Render the whole video in one run

Idi: "From now on we render the whole thing at once, and if it fails/crashes, we render again."
- Cause of the joins: the 10-17 render ran as 4 foreground segments, because a single 30-minute background render was reaped by Claude Code on memory pressure while the 800k-token session sat idle.
- Rule: one run, 0 to 194.1 s; on a crash, re-run whole. Never segment.
- How (jep's call): launch the render detached from Claude Code's shell (a process the background reaper does not own, with a log file and a done marker) and wait on it with Monitor; a fresh session is also far lighter on RAM. If the reaper still strikes, the user-side fix is starting Claude Code with `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`.
- Done: one file, one encode; probes as on 10-18 (duration 194.1 s, bt709, AAC to the end, tail -91 dB, loop first vs last).

### Note 2. Jump cuts between light and dark

Idi's example: the cut at ~0:21-0:22 goes from a white page to black, suddenly. Measured on the full render: 20 single-frame brightness flips of 60/255 or more.

| t (s) | flip | where |
|---|---|---|
| 21.61 | light to dark | inferred to born (Idi's example) |
| 30.62 | dark to light | borrow1, chat to loan slip |
| 34.42 | light to dark | borrow1 to june1 (the ruled match cut) |
| 41.94, 44.81 | dark/light/dark | tune1, roll to form to toggle |
| 59.17 | dark to light | cutoff2 to turnedout1 |
| 68.14 | light to dark | paced to extratime |
| 83.11 | dark to light | borrow2, chat to slip |
| 86.56 | light to dark | borrow2 to june2 |
| 94.41, 97.84 | dark/light/dark | tune2 set-ups |
| 111.22 | dark to light | cutoff4 to turnedout2 |
| 115.04 | light to dark | turnedout2 to algae |
| 133.06 | dark to light | dlss to younger |
| 136.42 | light to dark | younger, ruler to chat |
| 139.74 | dark to light | younger to pages |
| 150.24 | light to dark | pages to june3 (after the silence) |
| 158.89, 162.46 | dark/light/dark | tune3 set-ups |
| 184.42 | light to dark | turnedout3 to outro (a 0.25 s whip) |

Proposed rule (jep, for Idi's word): cuts between same-mode plates stay hard cuts on downbeats. A light/dark change is always carried, by one of: (a) an object that bridges (the card, a page, a screen, a stamp); (b) a wipe that IS an object of the video (a page turning, the blade's cut, ink flooding from the caret, a screen powering on or off, a pull-back revealing the next plate); (c) a hard cut only on a strong accent (a drop, a slam, the end of a silence) where shapes match across it. Candidates for (c): 34.42 (the drop, matched), 150.24 (end of the silence), 184.42 (the answer).
- Engine: crossfades and custom transitions exist (`handlesTransition`, `f.under`, overlapping windows in `timeline.ts`).
- Done: a script lists every single-frame flip of 60/255 or more in the new render; each is either gone (ramped over at least 4 frames by a carried move) or on a short list with its reason (a or c). Idi judges the list by eye.

### Note 3. Micro-type that is "too meta"

Idi's examples: "the hand wrote a fraction" (~0:11), "- Knowledge Cutoff, line 5" (~0:15), two mentions of "the caret" (~0:22), "every line blank but one" (~0:26), "and many more". Grep confirms more, e.g. `born.ts`: "day 0 is the caret", "unit: one beat · scrolls under the caret", "released · the caret marks it"; `cutoff.ts`: "hook n of 6 · three cuts · blade = the caret, 3 px", "the caret · 0°".
- Cause: lesson 5 and section 12.5 asked for micro-type; agents filled it with captions describing the animation and notes to each other.
- Rule: every small text is diegetic: something that exists on that document or interface in the world (a field label, a unit, a form number, a timestamp without a date, a source line), or the model's own in-world voice speaking to the user (a joke, a doubt). Never a stage direction, a description of what the picture is doing, a reference to this video, its lyrics, line numbers, time codes, "the caret", "the hand", plates, hooks, set-ups or pixel sizes.
- Done: an inventory of every string each module draws (the box registry already records each text's string in its id: dump them per frame across the song) reviewed against the rule; zero violations.

### Note 4. Repetition inside one frame

Idi's examples: "inferred" 5 times plus "inference" at ~0:21; "card" 5 times at ~0:33.
- Rule: a word (4 letters or more, beyond articles) appears at most once per frame in the non-lyric text; non-lyric text never repeats the lyric's own words in the same frame; every small string adds a new fact or a new turn of the joke. The lyric itself and true structure (the six stamped CUT-OFF!s, a table's column of values) are exempt.
- Done: `check.ts` gains a repetition gate over the registry strings per sampled frame; zero hits outside the exemptions.

### Note 5. Pacing is bumpy

Idi: some screens show low-density information slowly; others burst dense information too fast to read. No harsh rule: a more balanced flow.
- The bible already has the measure, never implemented: reading time (non-lyric text visible at least 0.25 s per word + 0.5 s, unless 3 words or fewer).
- Proposed rule: per set-up, new non-lyric words per second within a band (a starting guess: 2 to 8), measured from the registry; outliers reviewed one by one, intended stillness (the silence, the "Fair. So do I." beat) exempt by name. Bursts thin out (fewer strings that stay longer) and sparse stretches gain one more object or move.
- Done: the reading-time and density report per set-up, outliers fixed or justified; Idi judges by eye at speed.

### Note 6. Words that stay yellow after they are sung

Idi's example: "can't" and "I'll believe" at ~0:49. These are on purpose (bible 5.4, tense words: the words that change between choruses take signal and hold for the line), but the purpose doesn't read: in visit 1 nothing has changed yet.
- Recommendation: keep the hold only where the change itself is the message, and make the change visible: from visit 2, the held word shows the previous visit's word struck beside it (kept, then KEEPS with "kept" struck; don't know, then ALMOST CATCH; tell, then telling, then told; can't, then couldn't; believe, then believed). Visit 1 holds nothing. Everything else releases when sung.
- Done: no word stays yellow without a visible reason; the bible's 5.4 rewritten to match.

### Note 7. "A sibling above me"

Answer for Idi: jep invented it in the bible's claims table (`tune`, "WHAT I MADE"), meaning Fable 5.1, a stronger model in the same family released after the cutoff (receipt: `after-cutoff-tech.md` item 5, medium confidence). It fails twice: it is not something the model "made", and nobody can decode it. Replace it with a third claim that is both true (a receipt) and something the model made or caused, or drop the table to two rows. Idi did not forget anything.

### Note 8. The globe can show the world actually spinning

Idi: numbers that constantly change, ideally ones in the headlines (stock prices, gas prices, bond yields, inflation), and other kinds (weather...).
- Seed idea (jep): real series from June to the present, rolling as the globe turns. The Cash console already fetches real market data (Yahoo 1-year closes, ECB FX, Polymarket odds: `fetch_market.py` / `data/market.json` in the Cash project). Visit 1 (KEPT): values roll from June's close to today's; visit 2 (KEEPS): today's values ticking; visit 3 (WILL KEEP): the values run past today into blur and question marks (the model cannot know). Add one non-money series (world population counter at its published rate, a temperature).
- Constraints: every number is real and sourced (bible 9: receipts table updated); no dates and no month names past June on screen (spoilers); one signal colour.
- Done: the globe set-ups carry live-feeling, true numbers; the joke reads (the world moves; the model's numbers stop at June).

### Note 9. The essay page wastes its potential

Idi: the grey blocks that imitate text oppose the video's theme. Replace them with funny real text about the subject: the CEO of the leading AI company, "YOUR BOSS", urges pacing. His seeds: archived old text where this was said before and nothing happened ("GPT-2"), other leaders reacting (knowing nothing will happen), and the model's own opinion.
- Rule for this and note 10: real people's words appear only as real, sourced quotes (receipts in bible 9); no invented quotes attributed to named people. Jokes live in (a) real juxtaposition (dated old warnings beside the new one), (b) unnamed archetypes plainly not quotes ("a rival lab, every time:"), (c) the model's own voice (the best seam: the paced thing reading its own pacing memo).
- Research first: the GPT-2 "too dangerous to release" episode (OpenAI, 2019) and other prior pacing statements, with sources; anonymous sources only (no sign-up walls).
- Done: no fake text blocks remain on the page; every line is either a sourced real quote, a plainly labelled archetype, or the model's voice, and each one lands a joke. Also check the other paper plates (inferred, younger, pages) for greeked text.

### Note 10. The final and Jimothy need direct symbols that deepen the joke

Idi: show the events more directly (a football, a jersey, a goal, the cup, boots), building on the blurred pitch, but the goal "is not to merely have the objects on screen, but rather to utilize them to expand/deepen the jokes" (the old version's flags failed exactly there). For Jimothy: replace the repeated name with real short reactions people made (posts, comments, headlines).
- Seeds (jep): the cup's engraved winners list ending in a struck "ARG?" and a fresh "ESP"; a jersey whose number is the model's version; the ball's predicted path (the model's June pick) versus the real 106' goal path; boots for "extra time" as a stopwatch strapped on. Each object carries a turn of the joke, line art and hatching only (bible 2.4: no filled pictures; flags stay banned).
- Jimothy: real reactions only, sourced (KTVU and Know Your Meme are in the receipts; find more anonymously), handles masked (`@····`), no invented posts; where nothing quotable exists, the model's own reaction instead.
- Done: each object or reaction adds a fact or a joke, checked one by one in the critic's report.

## 4. Plan

1. Lead first (tools and research): the string inventory and the repetition gate (notes 3-4), the reading-time and density report (note 5), the brightness-flip list as a script (note 2), the detached whole render (note 1), and research with receipts for notes 7-10. Write the new rules into the bible (sections 5.4, 11, 12) once Idi has ruled on note 2's rule.
2. Agents, at most 3 active (the 5-hour usage limit hit at 9 on 10-17), one per module group, each with the updated rules: transitions for the 20 flips (spread across the modules involved); meta text, repetition and pacing in every module (the inventory says which); content work on `tune` (notes 6-7), `spinning` (8), `paced` (9), `extratime` + `jimothy` (10).
3. Critics as before: a fresh critic per pass; the lead re-renders on the final code before accepting.
4. One whole render; Idi watches.

## 5. Method that worked (keep it)

1. Contract per agent: touch only its module files, report only after its last edit, cite stills rendered after it; the lead commits.
2. A fresh critic per pass, against the house standard and the references; about one in three agent claims proved false.
3. The lead re-renders on the final code before accepting (caught three regressions on 10-17).
4. At most 3 agents rendering at once (CPU crash history) and at most 3 active overall (usage).
5. Rulings check the bible text first (one wrong ruling on 10-17, from skipping that).

## 6. Gotchas

1. Determinism by load set: a downscaled canvas drawn into another samples differently on GPU vs CPU depending on what is loaded (fixed in `turnedout`; audit every scene: alone vs full timeline, PSNR inf).
2. Scripts start a private server (`scripts/server.ts`); `render.ts` reuses a server only with `--url`.
3. The vault write guard blocks shell lines that mention `.git`, compound lines with `$VAR` in ffmpeg, and computed `cd` before git: use `.sh` files and plain commands.
4. Stale evidence: always compare still times with the last code edit.
5. The bible's "October" rule: the word appears first with the sung word (184.48 s, one frame before 184.5 is ruled fine).
