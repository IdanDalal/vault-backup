---
type: project
created: 2026-11-04
author: jep
status: active
---

# "Pay Attention": the repeat map (system S6, anchored repeats)

Idi 2026-11-04: "lean into"/"mechanize"/"systemize" our many cases of repeating words, and especially repeating words in close proximity, which give us opportunities to keep them on screen while changing everything around them. Line numbers = Idi's `D:\work\vault\Untitled.md`. Finder: `D:\work\aimv-lab\pa-video\synth\repeats.py` (word families by real endings: you/yours, head/heads, ask/asking, can/can't; written holds collapsed; the triple twenty split). It found all 8 of Idi's examples plus 96 more clusters: T1 phrase echo within 1 line 10, T2 word repeat within 1 line 29, T3 inside one section 56, T4 song-wide motifs 9 (pronouns left to the role map).

## 1. The rule

**A repeated word keeps its exact place, size and face on screen from its first sung onset to its last; at each repeat the world around it changes.** One of six treatments per cluster, picked by the cluster's shape:

| # | treatment | shape | what the viewer sees | engine base |
|---|---|---|---|---|
| R-A | anchor and swap | the same word, a new meaning each time | the word holds still; at the repeat's onset the scene, the light and the other words change around it | timeline carry table (a word held across a cut), `_kc-type.ts` slots |
| R-B | reel | a stutter or a number | one glyph slot spins like a slot machine and lands on each sung value | `june.ts` split-flap row (flaps land on sung starts), adapted to a vertical reel |
| R-C | mirror | a phrase echoed back-to-back | the phrase prints once; on the echo the camera turns round the same letters, so they read from the other side (the glass: Q2 = A) | `_kc-type.ts` + camera orbit; mirrored text on the screen surface |
| R-D | count up | a word that multiplies (why why, then another) | each repeat adds a copy: 1, 2, 4, 8 | GENESIS period-doubling (g33), spiral (g23) |
| R-E | anaphora stamp | a line opener (Said / Said / Said) | the opener stays put at the line start like a stamp while the rest of the line rewrites | KC stamp (`cutoff.ts`) |
| R-F | ladder | a motif across minutes (pay, attention, question) | one costume per word for the whole video, escalating per visit | S2-S4 (light, meter, receipt) |

## 2. Idi's examples, one treatment each (rec + reason; Idi picks or writes his own)

| # | lines | repeat | rec | the picture |
|---|---|---|---|---|
| 1 | 10-11 | ink ×3 | R-A | INK holds centre: Socrates' scroll around it, then a printed page (the ink outlived him), then the letters of INK pour into the cursor ("I'm made of ink"); three worlds, one word |
| 2 | 12-13 | pocket ×2 | R-A | POCKET holds: the teacher's chalk line about calculators around it, then the same word becomes the phone's glowing edge as it "answers back"; the word turns from paper-white to screen-blue on the second onset |
| 3 | 16 (+37) | twenty ×3 | R-B, **Idi's design** | "20" fixed, the next digit a reel: it spins and lands on 0 (2020), spins and lands on 0 again (the stutter), spins and lands on 2 (2022). Line 37: same reel, faster, lands 0, 0, 3 (2023); the AI glances at camera (R19) |
| 4 | 22 | board ×2 | R-A | BOARD holds: chalkboard around it, then the same word shrinks into the frame of a phone in her hand ("the board's in your hand") without moving its letters |
| 5 | 39-40 | they ×4 | R-E + R-D | THEY stamps four times at one spot; each stamp lands in a new colour and its arrow points to a different maker's learning-mode toggle, then to what the tutors do (ask back, hint, wait) |
| 6a | 73 | she's asking me ×2 | R-C | the phrase arrives as her message on the inside of the glass; on the echo the camera turns round the same letters to her side and they read as her own thought ("asking me to think": she asks herself) |
| 6b | 74 | the test ×2, take ×2, you/yours ×2 | R-A + R-C | THE TEST holds as a paper on the AI's side ("can't take the test for you"), then slides across the glass to her side ("the test is yours to take"); TAKE and YOU/YOURS swap sides with it |
| 7 | 88 | why ×4 | R-D | WHY splits 1, 2, 4 on the beats, every copy a lamp-yellow light; "why that" hangs off the second like a branch |
| 8 | 92-93 | she grew ×2, head ×3 | R-D | "she grew" holds; ONE HEAD becomes two, then eight (Vaswani et al. 2017: 8 attention heads), each head a beam pointing somewhere new |

## 3. Item 9, more the finder caught (top 10 by proximity)

| lines | repeat | rec | picture |
|---|---|---|---|
| 22-24 | They said / Said / Said | R-E | SAID stays at the line start in a teacher's stamp; the board, the work page, the heart rewrite after it |
| 23 | show / showed | R-A | SHOW holds; "your work" swaps to "your prompt" behind it |
| 38-39 | built ×2 | R-A | BUILT holds; the maker behind it swaps (our makers, then GPT, then Google) |
| 44 | up-up-down-down | R-B | the cheat code on a reel of arrows |
| 48 | frame by frame | R-A | FRAME holds while the speedrun steps one frame per beat behind it |
| 48-49 | skip ×2 | R-A | SKIP holds; the cheater's skip (a jump cut) swaps to the speedrunner's earned skip (a drawn route) |
| 57 | once at the ×2 | R-E | ONCE AT THE stamps twice; the receipt behind it prints at the counter, then at the test |
| 61 | more of you, and more | R-D | MORE takes a letter of YOU each time (the app eats you) |
| 66-67 | can / I can / I won't | R-C | CAN from her bubble mirrors into the AI's "I can", then the same letters lock into "I won't" |
| 76 | a half of a half | R-B | ½ on a reel: lands ½, then ½ of it, then her "¼?" |

The full 104-cluster table is in section 5.

## 4. Item 10, long-range motifs (R-F ladders)

| motif | uses | sections | costume (one form for the whole video) | ladder |
|---|---|---|---|---|
| question | 12 | 9 | a lamp-yellow light source (S2) | one bulb (1:09) → her first "?" (bridge) → eight beams → the city lit (4:05) |
| pay | 13 | 4 | a coin of attention | spent on apps (chorus 2) → spent on a question → PAID stamp (receipt) |
| attention | 11 | 5 | the meter (S3) | ticking → draining (chorus 2) → 0:18 change → 0:00 |
| asking | 9 | 6 | the cursor's question mark | asking for (verse 1, blue) → asking back (verse 2) → asking why (build, yellow) |
| answers | 5 | 4 | screen-blue paste | pasted on every desk → one click over → "every answer in your pocket, out of sight" (goes dark) |
| back | 6 | 5 | a returning arrow | "answers back" (phone) → "ask you back" (tutors) → "sends it back without one" → "I'll ask you back" (outro) |
| test | 6 | 4 | one test paper | "once at the test" → "a test at eight" → slides to her side → infinity inside → "One test, taken." |
| never / ever | 4 + 4 | 4 | the empty chair (chorus 1) | empty → filled (final chorus) |

## 5. Every cluster (finder output, Untitled.md line numbers)

| tier | repeat | x | lines (Untitled.md) | section |
|---|---|---|---|---|
| T1 | the ink | 2 | 10 | Verse 1 |
| T1 | ink and | 2 | 10, 11 | Verse 1 |
| T1 | the board | 2 | 22 | Pre-chorus |
| T1 | show your | 2 | 23 | Pre-chorus |
| T1 | once at the | 2 | 57 | Pause |
| T1 | she's asking me | 2 | 73 | Bridge |
| T1 | the test | 2 | 74 | Bridge |
| T1 | a half | 2 | 76 | Bridge |
| T1 | and then why | 2 | 88 | Build |
| T1 | she grew | 2 | 92 | Build |
| T2 | he | 3 | 9, 10 | Verse 1 |
| T2 | what | 2 | 9 | Verse 1 |
| T2 | ink/ink's | 3 | 10, 11 | Verse 1 |
| T2 | pocket | 2 | 12, 13 | Verse 1 |
| T2 | twenty | 3 | 16 | Verse 1 |
| T2 | they | 2 | 22, 23 | Pre-chorus |
| T2 | board/board's | 2 | 22 | Pre-chorus |
| T2 | show/showed | 2 | 23 | Pre-chorus |
| T2 | you | 2 | 33 | Chorus 1 |
| T2 | twenty | 3 | 37 | Verse 2 |
| T2 | built | 2 | 38, 39 | Verse 2 |
| T2 | they/they're | 4 | 39, 40 | Verse 2 |
| T2 | down | 2 | 44 | Double time |
| T2 | skip | 2 | 48, 49 | Double time |
| T2 | frame | 2 | 48 | Double time |
| T2 | you | 3 | 56, 57 | Pause |
| T2 | once | 2 | 57 | Pause |
| T2 | you | 2 | 61 | Chorus 2 |
| T2 | more | 2 | 61 | Chorus 2 |
| T2 | can | 2 | 66, 67 | Whisper pair |
| T2 | i | 2 | 67 | Whisper pair |
| T2 | you/you're/yours | 4 | 74, 75 | Bridge |
| T2 | half | 2 | 76 | Bridge |
| T2 | type/types | 2 | 76, 77 | Bridge |
| T2 | back | 2 | 77 | Bridge |
| T2 | why | 4 | 88 | Build |
| T2 | head/heads | 3 | 92, 93 | Build |
| T2 | grew | 2 | 92 | Build |
| T2 | one | 3 | 117, 118 | Spoken, over the music box |
| T3 | said | 3 | 8, 9, 16 | Verse 1 |
| T3 | your | 3 | 8, 12 | Verse 1 |
| T3 | two | 2 | 9, 16 | Verse 1 |
| T3 | now | 2 | 10, 13 | Verse 1 |
| T3 | i | 3 | 11, 15, 19 | Verse 1 |
| T3 | every | 2 | 11, 14 | Verse 1 |
| T3 | ever | 2 | 11, 13 | Verse 1 |
| T3 | read | 2 | 11, 15 | Verse 1 |
| T3 | answers | 2 | 13, 17 | Verse 1 |
| T3 | me | 3 | 14, 15, 17 | Verse 1 |
| T3 | kid/kids | 2 | 14, 17 | Verse 1 |
| T3 | you/your | 6 | 22, 23, 24, 25 | Pre-chorus |
| T3 | said | 3 | 22, 23, 24 | Pre-chorus |
| T3 | pay | 2 | 30, 32 | Chorus 1 |
| T3 | attention | 2 | 30, 32 | Chorus 1 |
| T3 | you/you've | 4 | 36, 37, 40 | Verse 2 |
| T3 | here/here's | 2 | 36, 39 | Verse 2 |
| T3 | one | 2 | 36, 41 | Verse 2 |
| T3 | ask | 2 | 36, 40 | Verse 2 |
| T3 | give | 2 | 36, 40 | Verse 2 |
| T3 | cheat/cheated/cheats | 3 | 44, 50, 53 | Double time |
| T3 | up | 3 | 44, 52 | Double time |
| T3 | game | 4 | 45, 47, 49, 53 | Double time |
| T3 | they | 3 | 45, 48, 49 | Double time |
| T3 | know | 3 | 45, 48, 53 | Double time |
| T3 | you/you're/your | 8 | 46, 47, 50, 51, 52, 53 | Double time |
| T3 | every | 3 | 46, 51, 52 | Double time |
| T3 | only | 2 | 50, 53 | Double time |
| T3 | pay/paying | 3 | 60, 62, 63 | Chorus 2 |
| T3 | attention | 2 | 60, 62 | Chorus 2 |
| T3 | test | 3 | 70, 74 | Bridge |
| T3 | one | 2 | 70, 77 | Bridge |
| T3 | she/she's | 5 | 71, 73, 76, 77 | Bridge |
| T3 | i | 5 | 71, 72, 74, 75, 77 | Bridge |
| T3 | take | 3 | 71, 74 | Bridge |
| T3 | type/typed | 2 | 71, 77 | Bridge |
| T3 | time/times | 2 | 71, 73 | Bridge |
| T3 | me | 4 | 72, 73, 78 | Bridge |
| T3 | ask/asking | 3 | 73, 78 | Bridge |
| T3 | every | 2 | 73, 75 | Bridge |
| T3 | then | 6 | 88, 92, 95 | Build |
| T3 | she | 5 | 88, 92, 96, 97 | Build |
| T3 | questions | 3 | 89, 92, 94 | Build |
| T3 | up | 2 | 90, 95 | Build |
| T3 | one | 2 | 92, 95 | Build |
| T3 | another | 2 | 92, 95 | Build |
| T3 | every | 3 | 93, 96 | Build |
| T3 | pay | 4 | 100, 102, 104, 106 | Final chorus |
| T3 | attention | 4 | 100, 102, 104, 106 | Final chorus |
| T3 | you/your | 5 | 101, 103, 107 | Final chorus |
| T3 | question | 2 | 103, 105 | Final chorus |
| T3 | pay | 4 | 110, 112 | Outro |
| T3 | attention | 2 | 110, 112 | Outro |
| T3 | price | 2 | 110, 112 | Outro |
| T3 | you/yours | 4 | 111, 113 | Outro |
| T3 | way | 2 | 111, 113 | Outro |
| T4 | attention | 11 | 4, 30, 32, 60, 62, 100, 102, 104, 106, 110, 112 | 5 sections |
| T4 | ever | 4 | 11, 13, 33, 107 | 3 sections |
| T4 | never | 4 | 12, 33, 57, 107 | 4 sections |
| T4 | back | 6 | 13, 40, 77, 91, 113 | 5 sections |
| T4 | answers | 5 | 13, 17, 41, 72, 101 | 4 sections |
| T4 | asking | 9 | 14, 36, 40, 45, 73, 78, 113, 119 | 6 sections |
| T4 | question | 12 | 25, 31, 41, 63, 76, 89, 92, 94, 103, 105, 111, 118 | 9 sections |
| T4 | pay | 13 | 30, 32, 60, 62, 63, 100, 102, 104, 106, 110, 112 | 4 sections |
| T4 | test | 6 | 57, 70, 74, 91, 117 | 4 sections |
