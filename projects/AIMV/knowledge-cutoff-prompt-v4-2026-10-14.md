---
type: project
created: 2026-10-14
author: jep
status: active
---

# Knowledge Cutoff - MiniMax prompt v4, knob by knob

Previous: [[handoff-2026-10-14]]. Rules: [[aimv-guidelines]]. Lyrics: [[knowledge-cutoff-lyrics-v3-2026-10-13]].

## 1. What the official docs say (receipts)

Sources: MiniMax repo README + `skills/music-caption-rewriter` (github.com/MiniMax-AI/MiniMax-Music3), ComfyUI source `comfy/ldm/minimax_music/prompt.py` (jep's install, v0.39).

| # | Finding | Confidence | Consequence for us |
|---|---|---|---|
| F1 | MiniMax ships 1,000 caption templates. They use **your showcase box names verbatim** (`Basic Attributes`, `Global Emotional Progression`, `Vocal Style`, `Groove & Foundation Progression`...) and fixed phrasing: `bpm is 122. key is D, and scale is minor.` | high (read 3 templates) | Your YouTube knob list = the format the model learned from. v3 caption used neither the names nor the phrasing |
| F2 | ComfyUI rewrites `<\|bpm 124\|>` into `bpm is 124` before the model sees it | high (source code) | Confirms F1: "bpm is X" is the trained phrasing. BPM in our old "124 BPM" form may have been ignored |
| F3 | Templates run 500-600 words; the Arrangement is a **section-by-section timeline** (what enters, exits, grows per section) | high | v3 caption = 163 words, an equipment list, no timeline. Fits your note 1 (vague prompt → wild variety) |
| F4 | Caption limit 5,000 tokens | high (README) | v4 = 888 words ≈ 1,200 tokens. Room to spare |
| F5 | Official lyric tags: `[Intro] [Verse] [Pre-Chorus] [Chorus] [Post-Chorus] [Bridge] [Instrumental] [Solo] [Outro]`. ComfyUI lowercases every tag | high | Section directions belong in the caption timeline. Custom tags like `[Final Chorus - grand]` are untested and likely weaker (medium) |
| F6 | Templates never quote lyric words | high | A caption line like "melisma on the word 'tune'" probably has no effect (medium). Spelling in the lyric ("tuuuune") is the proven lever (G23) |

## 2. v4 = first test of F1-F6 (jep's recommended values in every box)

Files: caption `D:\work\aimv-lab\kc\caption-minimax-v4.txt`, lyrics `kc\lyrics-mm-p4.txt` (974's layout + `Al-jee` + `tuuuune` in the final chorus only), 8 seeds 1001-1008, 225 s.

New meter `D:\work\aimv-lab\kcmeter.py` (+ `stems.py`): drops anchored on the lyric (gap after "borrow"/"turn" up to the chorus's first word, 0.5 s window), the "tune" hold, and **sung %** = share of vocal time on held, stable pitch (Demucs vocal stem + pitch tracking). Sung % is a proxy for your note 2, unvalidated against your ear (medium-low confidence).

| Take | Words | Pace | Sung % | Drop borrow→ch1 / ch2 | Drop turn→final | Final "tune" | Flaw |
|---|---|---|---|---|---|---|---|
| 974 (your favorite, v3 prompt) | 97.8% | 145 | 57% | **17.8 / 18.3 dB** | 4.6 dB* | 0.3 s | |
| 971 / 975 (v3 prompt) | 94-97% | 145-159 | 41-44% | 5-13 dB | 9-10 dB | 0.3-0.5 s | |
| **A: 1006** | **97.3%** | 134 | 57% | 0 / 0 dB | 10.2 dB | **3.7 s** | no pre-chorus drops |
| **B: 1005 (trimmed)** | ~97%** | 146 | 49% | **20.0** / 3.6 dB | **27.6 dB** | 0.4 s | invented ~60 filler words after the outro: cut at 2:40.7, verified by Whisper |
| **C: 1004** | 96.1% | 133 | 58% | 2 / 3 dB | 3.6 dB | 0.3 s | cleanest all-rounder, flattest drops |
| 1001 | 93.9% | 130 | 56% | 1 / 1 dB | 11.3 dB | 2.6 s | outro missing |
| 1002 | 96.3% | 139 | 53% | 2 / 4 dB | 10.3 dB | 1.9 s | refrain heard 4 of 6 |
| 1003, 1007, 1008 | 89-95% | 141-160 | 47-58% | mixed | ≤5 dB | ≤0.4 s | 1008 repeats bridge lines |

\* You hear a sick drop there; the meter doesn't. That drop likely lives in a riser or filter sweep, which loudness can't see. Ear wins.
\** estimate: errmap on the trimmed file finds 15 word differences in 490; `probe_lines.py` not re-run on the trim. Untrimmed score was 81.6% because the filler counts as errors. Also: its outro starts with no gap after the last chorus word.

Reading, per claim:

1. **Pace fixed by the format** (high confidence): 145-195 wpm before, 130-146 now, 5 of 8 inside G1's 130-140 band. Same lyric layout, only the caption changed.
2. **Final "tune" spectacle works in 3 of 8** (1006 3.7 s, 1001 2.6 s, 1002 1.9 s): the stretched spelling in the lyric does it.
3. **Sung % rose a little**: v4 average 54% vs 47% for the three old takes; 974 = 57%. Small shift, unvalidated meter. Your ear decides note 2.
4. **The pre-chorus drop got worse** (high confidence on the number, medium on the cause): 974 has 18 dB, 6 of 8 v4 takes have 0-4 dB. Likely cause: v4's caption asks for "risers and reverse cymbals into each break", so the model fills the `[Instrumental]` with a rising sound instead of a cut. Fix candidate in K10.
5. **"Al-jee"**: Whisper writes "algae" either way; it cannot hear soft vs hard G. Your ear only.
6. Takes A/B/C in `D:\work\AIMVs\ours\kc-minimax-v4-*`.

## 3. The knobs: your rulings

Each row: what v4 says now (short), what it does, options, jep's pick. Answer by K-number, "keep" is a valid answer.

| # | Box | v4 now | What it does | Options | jep's pick |
|---|---|---|---|---|---|
| K1 | Basic Attributes | `bpm is 124. key is D, and scale is major. Synth-Pop / Electropop.` | Genre family + tempo the model anchors on | A keep · B Dance-Pop / Synth-Pop (groovier, funk guitar stabs) · C Cinematic Pop / Electropop (bigger, slower-feeling) | **A**: pace just landed in your band; changing genre resets it |
| K2 | Global Emotional Progression | wry verses → suspense held into a cut → euphoric chorus → whispered bridge → silence → final chorus explodes, key change up a whole step | The whole arc in one paragraph; the model's main map of "direction" | A keep · B drop the key change (some takes may wobble in pitch) | **A**: your note 4 asks for grandiose; a key change is the classic pop device for it. Listen for it in A/B/C first |
| K3 | Application Scenarios & Imagery | typography video, an artificial mind waking in a dark room, late-night headphones | Mood color, weak lever | A keep · B add "sounds like a modern film trailer finale" | **A** |
| K4 | Sonics & Production | glossy, wide, breathable dynamics, two drops named | Loudness contour | A keep · B "the music stops dead for one bar" wording (pairs with K10) | **B** |
| K5 | Vocal Gender & Timbre | `Singer A (Female)`, bright warm clear mezzo, slightly airy | Who the AI sounds like | A keep · B male · C female with a faint vocoder sheen on the spoken parts only (the AI "shows" in the talking) | **A**, C worth one test batch later |
| K6 | Vocal Style | fully sung, legato, no rapping; one melisma near the end of the final chorus; bends on some chorus endings | Your notes 2 and 5 | A keep · B also forbid long holds outside pre-chorus, bridge and final "tune" | **A** until you hear whether 2 is fixed |
| K7 | Harmony/Backing | ladder: verse solo → ch1 light double → ch2 thirds and sixths → final choir wall + gang shouts on the refrain | Makes each chorus bigger than the last | A keep · B gang shouts on every refrain | **A**: escalation needs headroom |
| K8 | Vocal FX | dry upfront verses and spoken parts, delay throws on chorus line ends, long hall on the bridge | The rise-and-fall "you" ends; intimacy | A keep | **A** |
| K9 | Instrument lifecycle | arps + pads primary; piano, bell synth, sub bass secondary; supersaws + string synths + choir join in the final chorus | Who plays when | A keep · B add a guitar (warmer, less "machine") | **A**: an all-synth band suits an AI narrator |
| K10 | Groove + Embellishments | four-on-the-floor; risers and reverse cymbals into each break; glitch and tape-stop in breaks | Drops and transitions | A keep · B **remove the risers before the pre-chorus breaks, describe a dead stop ("everything cuts to silence except the held last word"), keep risers only before the final chorus** | **B**: v4 lost 974's borrow drop (18 dB → 0-4 dB), most likely to these risers |
| L1 | "Algae" spelling | `Al-jee` | Your note 3 | A keep · B `Al-gee` · C `Aljee` | your ear on A/B/C decides; Whisper can't tell |
| L2 | Stretched "tune" | final chorus only (`tuuuune`) | Your note 5 spectacle | A keep · B also a shorter stretch in chorus 2 (`tuune`) | **A**: one spectacle stays special |

Next round (v5) = your rulings + K10 B, 8 seeds, same meter. Full caption text: `D:\work\aimv-lab\kc\caption-minimax-v4.txt`.

## 4. Idi's ear on A/B/C (2026-10-14)

| Take | Verdict | Good | Bad |
|---|---|---|---|
| A 1006 | hard no: "Disney princess song", too slow, subtle, cute | soft-G "Algae" right; excellent holds at the right moments | sings "tomorroo", "borroo" |
| B 1005 | same faults as A, "Disney princess rap" | same as A | holds "turn" so long it repeats "urn" |
| **C 1004** | **new gold standard**, still "Disney princess songness > 0" | longest, most deliberate holds (tomorrow, borrow, you, turn); backing "woah-oh / oh-whoah" between chorus lines | 2nd pre-chorus sings "tomorrow" line twice; too piano-y; randomly loses the beat and slows on random words; ends 3:30 with 15 s of noise |

jep's reading: the princess quality most likely came from v4's own words ("bright, warm, clear mezzo-soprano, slightly airy", "glassy bell synth", "sparkling", "soft piano", "wonder", "triumphant and grateful"); medium-high confidence. "tomorroo / borroo / urn" = the stretched spellings sung literally.

Next (Idi's idea): deconstruct the 9 reference songs into the MiniMax box format, so Idi can pick values per box from songs he knows.
