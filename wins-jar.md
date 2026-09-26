---
type: note
created: 2026-09-04
updated: 2026-09-05
author: jep
status: active
built: 117
received: 102
jar_last_accepted: 2026-09-05
---

# Wins Jar - the Ledger's W-column

Source: `parts-registry.md` item 1 (the Ledger) + tutoring principle P6 applied to Idi. Built 2026-09-04 on Idi's word; rulings of 2026-09-05 applied.

## Rules (scan, don't read)

- **W** = a self-generated list that reached its done state, with a receipt. Mirror of the L (an abandoned self-generated list).
- **Two columns, both monotonic, never a demotion** (jep's proposal 2026-09-05, from Idi's C1/C2 reasoning; overrule with one word):
  - **Built** = done by Idi's own standard. His judgement, his receipt. Nobody else's behaviour can touch this number. **Threshold (Idi, 2026-09-05):** creation, "things I didn't have: trying them, judging, deciding, iterating, adding parts, removing parts, changing approaches, doing more outside research." Transcription is below the line: organizing what he already had ("like writing a note in Obsidian is simply transferring ephemeral words in my mind to eternal words on my screen") is no W. His shorthand: qualitative counts, quantitative does not.
  - **Received** = reality answered: follow-up, return visits, likes, "they waited for it." The only column where other people enter the jar. Idi's C1 rule ("nothing is a W if it doesn't cause people to follow up") lives here.
  - Built minus Received = on probation (Idi's C2 word). Probation never expires into an L; it either lands or stays built.
- **Not a W**: finished crafted lists (games completed, films watched). Those stay in the Idiverse lists. Activity volume, streaks, commit counts: jep's layer only, never shown as a score.
- **Receipt** = file path, commit hash, date, or a named audience. No receipt, no W. Overwatch's rule: receipts over trust.
- **Idi performs the update.** jep stages candidates with receipts; Idi accepts by index ("W C4", "R C4" for received) on the whiteboard or Telegram; jep moves the line and bumps the frontmatter. No reply = still N.
- **Language stays informational.** "Built 117 / Received 102, still since 09-05." No prizes, no targets, no comparison to any other person or to a past rate.
- **Granularity** (R1, Idi 2026-09-05: yes): one W per done-state reached; a ritual counts once per instance (each session, each recap). "It feels dishonest/unfair if I imagine a day where I have multiple sessions and the counter stays still." **"Session" = a student session.** A 3PM student and a 6PM student are two Ws. jep sessions are never Ws; only what gets built inside them can be.
- **Ordered deliverables count as Idi's** (R3, Idi 2026-09-05): jep occupies the empty chair on the Dreamer's hire, so what the chair builds on orders is the system's W. jep's own ledger is `git log`.

## The jar: Built 117 / Received 102

| # | W | Receipt | Built | Received |
|---|---|---|---|---|
| 1 | Hollywood film reviews, Facebook | `telos/work/creations.md` (12 listed), re-typed by Idi into the Idiverse | 12 | 0 ("virtually no engagement", Idi 09-05) |
| 2 | Humorous yearly awards posts, Facebook | `telos/work/creations.md` | 2 | unknown |
| 3 | 9GAG memes | 87 uploads 2013-02-15 → 2024-03-03 per the 9GAG data export; all 87 media files recovered to `D:\work\screens\9GAG\media\` (index.csv); count stays 1 until ruling R4 (creation vs repost) | 1 | 1 (sample: 3.3K upvotes, 121 comments on the 2021-03-13 Ghost of Tsushima post; per-post counts pending the console script) |
| 4 | Poker recaps, WhatsApp, Hebrew, 2019-07-21 → 2023-03-15; 29 live, 65 online (49 with attachments) | `D:\work\screens\Poker\poker_recaps_index.md`, built from the chat export; every recap opens "סיכום הפוקר"; 94 is a floor (the first found is headed "the 11th of 2019") | 94 | 94 (median 21.5 replies within 12h, 13.5 within 2h; peak 150 replies on 2020-04-11) |
| 5 | Game-store Instagram deal: logos, memes, videos, daily Hebrew posts on news/deals/hype | `parts-registry.md` item 2, Idi's 08-17 words; the deal ran daily | 1 | 1 |
| 6 | Game Lab 2D, shipped and played S4 (K 46 → 497, 2h42m) | `projects/tutoring-game-lab.html`, commit `9c86dc8` 08-20 | 1 | 1 |
| 7 | Tutoring sessions S1–S5 ran (08-10, 08-13, 08-17, 08-20, 08-24) | `session_date:` in `projects/tutoring-bakeoff/lesson-transcripts/*.DISTILLED.md` (S1–S4); S5 in `daily/digests/2026-08-30-loop-review.md:72-108` | 5 | 5 (the girls came back each time) |
| 8 | Word World 3D v9 | commit `5feec28` 08-23, 13 probe suites green; "meets (and exceeds) my standards", "writing down a story" (Idi 09-05) | 1 | 0 (girls bored almost instantly, S5; on probation) |

Removed 2026-09-05 on Idi's ruling: personal command center ("a crumbling mess", W someday), Cash allocation ("not a W whatsoever"; no money moved), parent brief for the cousin's son ("writing down a thought", transcription of what he already had, "certainly not a W"). PC HQ Phase A: not yet; counts when constant smooth work runs.

## Candidates and rulings pending

- **R4** 9GAG memes: 87 uploads, media recovered. Count all 87 as Built, or prune reposts first? Titles flag only one repost ("credit to @GOOFYGODSCOMICS"); the rest are indistinguishable from the export. jep's recommendation: 87 Built, and Received per post once the counts land.

## Reception sources (R2)

| Source | State 2026-09-05 | Reception data | Next |
|---|---|---|---|
| 9GAG memes | Export done (title, time, link per upload). All 87 media files pulled from `img-9gag-fun.9cache.com` anonymously, no Cloudflare on the CDN. `D:\work\screens\9GAG\media\index.csv` | Not in the export. The v1 API still serves upVoteCount / commentsCount from inside a logged-in browser (yt-dlp's extractor uses it). Script at `D:\work\screens\9GAG\fetch_counts.js`: paste into DevTools console on 9gag.com while logged in, saves `9gag_counts.json` | Idi runs the console script once |
| Poker recaps | Export done: 31,897 messages, 2019-03-29 → 2024-03-12, 10 senders. 94 recaps indexed with reply counts at `D:\work\screens\Poker\poker_recaps_index.md`. Screen recordings and csv logs are on Idi's own storage, separate | In hand (replies within 2h / 12h per recap) | Idi's call whether the Hebrew recaps (friends' nicknames) enter the Idiverse, which reaches the private GitHub repo |
| Game-store Instagram (voxel__gaming) | No login. Meta refuses recovery without the registered email or a linked Facebook (help page). Anonymous download dead since mid-2023 (instaloader #2427); a logged-in session is required | Post likes and comment counts come with instaloader metadata | Route: `instaloader --load-cookies` from Idi's personal account, one profile, default rate limits; risk = temporary action block on the personal account, his call |
| Facebook posts | Meta's export "does not contain data that someone else shared", so reactions received are absent (help 930396167085762); a "comments on your posts" option is claimed by one vendor, unverified | Artifacts yes, reception mostly no | One-month JSON test export to check the comments claim |

Landing zone for media: outside the vault (vault git ignores media). Text indexes go in the Idiverse notes.

## Digest wiring (Idi's hand; jep cannot write the prompt file)

Append this sentence to `.vault-config/prompts/morning-digest.md`:

`Read projects/wins-jar.md; report one line "Built N / Received M, still since <jar_last_accepted>" using the frontmatter values, then list pending candidates by index with their receipts; never compute rates, streaks, or gaps for the jar.`

Runs on the laptop until the cron port lands on the PC.

## Log

- 2026-09-04 seeded at 25 (jep). Awaiting R1–R3 and C1–C3.
- 2026-09-05 Idi's rulings applied: R1 yes, R2 exports in motion, R3 yes; C2 built/unreceived (probation), C3 not yet; command center, Cash and (after his context) the parent brief removed. Built/Received split proposed and applied: Built 24 / Received 9.
- 2026-09-05 (later) exports processed: 94 poker recaps indexed with reply counts (Built 94 / Received 94); 87 memes recovered from the 9GAG CDN, count pending R4. Jar: Built 117 / Received 102.
