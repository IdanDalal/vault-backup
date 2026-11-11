---
type: research
created: 2026-11-11
author: Agent asset-map
status: active
project: workshop
---

# Asset map: where Idi's files, lists and links live (2026-11-11)

Read-only pass. Counts from PowerShell on 2026-11-11. Media never opened. `lesson-transcripts\` skipped. "Archive" = `D:\work\laptop-archive\CORPUS-June-2026`.

## 0. What an index must know first

1. jep sees one side of the machine. `C:\Users\Idi` and 11 `D:\` root folders (`KEEP`, `Post`, `RSD`, `Drive`, `MEMES`, `Memories`, ...) list as empty to jep (access-denied per `projects\laptop-retirement\laptop-retirement-2026-09-25.md`). Browser bookmarks: none found where jep can read.
2. The only readable Idiverse is a June 2026 laptop snapshot. PKMS holds 56 files absent from it, so a newer source exists on Idi's side (location unverified).
3. Idiverse notes carry meaning in filename + folder. 6 of 287 have frontmatter. 77 are empty or under 200 B (title = whole note).
4. `vault\.claude\worktrees\` = 23 vault copies, 14,252 files. Every crawl must exclude it.

## 1. D:\work, first level

| Folder | Files | Size | Newest | What it is |
|---|--:|--:|---|---|
| `aimv-lab` | 157,975 | 162.8 GB | 2026-11-10 | AI music video lab: scripts, ComfyUI logs, renders, venv; `kc*\` (video 1), `pa*\`, `pay-attention\` (video 2) |
| `AIMVs` | 1,221 | 35.7 GB | 2026-11-11 | 43 reference videos/mp3 at root, `Refs.md` (14 links), `lyrics\` (44), `ours\` (1,133 own takes, renders) |
| `captures` | 66 | <1 MB | 2026-10-05 | Phone-capture git repo + Obsidian config; 2 md files |
| `comfy-models` | 0 | 0 | - | Empty |
| `drop` | 0 | 0 | - | Empty `reddit\` |
| `laptop-archive` | 3,304 | 0.10 GB | 2026-09-25 | Laptop copy: `CORPUS-June-2026\` (2,974; every old vault), `kitchen-nexus-extras\` (292), `home\` (35), `config\` (2). Its `README.md` counts are stale (says 3,812 files, 424 MB) |
| `pixel-root` | 4 | 7.47 GB | 2026-10-07 | Pixel phone factory image + patched boot image |
| `PKMS` | 89 | 0.05 GB | 2026-11-11 | Idi's context pack for this job (section 3) |
| `screens` | 136 | 0.10 GB | 2026-11-09 | Screenshots: `9GAG\` 111 + `index.csv`, `AIMVs\` 8, `Poker\` 8, `XCOM\` 4; `BIOS\`, `one-zero\` empty |
| `studio` | 28,349 | 0.99 GB | 2026-10-01 | `kidstudio\` live app (server, venv, outputs) |
| `tutoring-kit` | 10 | 2.9 MB | 2026-09-25 | De-identified salvage: 2 game templates, 4 pipeline tools, 1 report |
| `vault` | 15,401 | 1.80 GB | 2026-11-11 | The vault. `.claude\` 14,252 files / 1.66 GB; `.git` 302; real content about 850 files (`projects\` 662, `daily\` 63, `telos\` 42, `inbox\` 24) |
| (loose files) | 6 | 17 MB | 2026-10-29 | 3 `aml-settings-*.json` (XCOM launcher snapshots), `XCOM-archive-2026-09-11.zip` + manifest + delete script |

Duplicates and near-duplicates:

- **Vault copies**: 23 worktrees in `vault\.claude\worktrees\` (12 `aimv-*`/`kc-*`, 4 `pa-*`, 2 `cash-*`, 5 other). Same paths, drifting contents.
- **Idiverse, 4 forms**: canonical `Vaults BACKUPS\Idiverse` (287 md); reprocessed `NEXUS BACKUP\vault\atomic_notes` (261); 8 drifted forks in `_forks\NEXUS-Idiverse`; 28 hash-identical files in `D:\work\PKMS`. Receipt: `_CORPUS-MAP\REDUNDANCY-MANIFEST.md`.
- **Inside PKMS**: `How To Systemize Writing.md` in `Ideas\` and `Fan Theories\`; `The Champion Moment.md` twice (779 B with a DRAFT line, 696 B without); `Fan Theories 09 - WALL-E.md` is hash-identical to `10 - Star Wars.md` (both hold the Star Wars text; the WALL-E text is missing).
- **Telescope essay, 3 versions**: `vault\atomic-notes\The Telescope Metaphore.md` (2,092 B), Idiverse `Mini-Essays\` (2,068 B), fork (2,041 B).
- **XCOM, 5 places**: `vault\projects\XCOM`, `XCOM-archive-2026-09-11.zip`, `aml-settings-*.json`, `Vaults BACKUPS\XCOM` (134), `NEXUS BACKUP\projects\XCOM` (165).
- **Kid Studio**: `vault\projects\kidstudio` (11 files, code as of 09-07) vs `D:\work\studio\kidstudio` (live; `allow.txt` 10-01).
- **DECADEnts**: `vault\projects\decadents\DECADEnts*.md` (4) = Idiverse root notes, plus 3 reprocessed `2025-12-30-*.md` twins.
- **Templates**: `vault\inbox\DAILY-TEMPLATE-EXAMPLES\` (6) hash-identical to Idiverse `00 Posterity\Templates\`.
- **Smaller**: `wins-jar.md` at vault root (8,132 B) and in `projects\` (8,738 B); `PIPELINE.md` in `tutoring-salvage\` and `tutoring-kit\tools\`; Tolle "A New Earth" epub in PKMS, Idiverse, vault root; `kitchen-nexus-extras\.claude.archived` and `NEXUS BACKUP\.claude` (232 files each, hashes unchecked).

## 2. The Idiverse

- **Readable canonical copy**: `Vaults BACKUPS\Idiverse\` in the archive. 391 files, 39.5 MB: 287 md, 15 epub, 14 images, 1 pdf, 1 canvas, rest `.obsidian`. `_CORPUS-MAP\MAP.md` counts 266 notes after removing 21 internal copies; span 2024-09-09 to 2026-04-22. Per-note index with first lines: `_CORPUS-MAP\strata\MAP-idiverse.md`.
- **Live copy**: location unknown. Evidence: PKMS has 11 split fan-theory files where the archive has one 47.5 KB `Fan Theories (Sometimes A Cigar Is Just A Cigar).md`, plus `The Human Transformer.md` (2026-01-13), absent from the archive. Candidates `D:\KEEP`, `C:\Users\Idi`. Confidence: medium.
- **Structure**: folders only. 3 tiers, 20 numbered pillar folders: `00 A. Patterns - 01-09`, `00 B. Potential, Possibilities, & Prospects - 07-14`, `00 C. Proof, Presentation, & Pinging - 15-20`, plus `00 Posterity` (templates), 31 root notes, and 9 empty folder trees from an older P-scheme (`Passions`, `Payments`, `People`, ...).
- **Frontmatter**: 6 of 287 (the templates: `Type`, `Date`, `Weekday`). Tags: none. Wikilinks: 16 notes. URLs: 64 notes. 0 bytes: 21. Under 200 B: 56 more.
- **Kinds** (folder-based estimate, plus or minus 10): list ~130, idea ~75, literature/review ~35, identity/self ~20, admin ~25.

| Kind | 5 representative files |
|---|---|
| List | `Film\Film Backlog.md` (31.8 KB); `TV Shows\TV Show Backlog.md`; `Video Game Lists\Video Games I Played Since 2015.md`; `Categories\Funny YouTube Channels.md`; `Music\Karaoke Options (Lyrics I Know...Mostly).md` |
| Idea | `Mini-Essays\The Telescope, The Sun, And The Flame.md`; `Mini-Essays\The Glass Tribe.md`; `Mini-Essays\Treat Your Brain Like A Large Language Model.md`; `Half-baked Script Ideas\Script 5.md`; `Cinema Degrees.md` |
| Literature / review | `Film Reviews\11. Everything Everywhere All At Once (2022) 2022-07-11.md`; `B.O.O.T.Y.s\The 2022 BOOTYs - 2023-07-01.md`; `Journeys\1 - The Marvel-IMAX Journey.md`; `Finished\Albert Camus - The Myth Of Sisyphus.md` (0 B); `Mini-Essays\True Love According To Eckhart Tolle.md` |

- 13 of 14 `Finished\` book notes are 0 B: the title is the record, no literature note exists yet.
- **Derived layer**: `NEXUS BACKUP\vault\atomic_notes\`, 261 notes written by a machine on 2026-01-16; filenames `YYYY-MM-DD-slug.md` (140 from 2024-09, 18 from 2026-01). All carry `id`, `created_date`, `updated_date`, `status` (`#child` 256, `#baby` 5), `pillar` (20 values; `06-publish-post` 83), `type` (`idea` 183, `people` 40, `admin` 38), `confidence`, `tags` (wikilink to one of 25 pillar tag notes), `source_channel: idiverse-migration`. `type` has no `list` value: `actors-who-worked-with-leo` is typed `people`.
- **Other vaults** (`.obsidian` in 9 places under `D:\work`, 0 under `C:\Users\jep`): archive `jep` (17 md), `TemporarilyTitleless` (194), `Espionage Inc` (6), `Curtains` (1), `NEXUS BACKUP` (1,256); `D:\work\captures` (2); `D:\work\vault` (570).
- **Inside `D:\work\vault` today**: under 15 notes. `atomic-notes\` 1; `inbox\seed-telescope-x-bowstring.md`; 6 templates; 4 DECADEnts notes; root strays `IMDb_EDA.ipynb`, `Untitled.md` (song lyric draft), one epub. `Library\` empty.

## 3. D:\work\PKMS

89 files in 6 folders: 16 epubs + 73 others.

| Class | n | Files |
|---|--:|---|
| Idea stub | 10 | `Ideas\`: `0) One must imagine Sisyphus happy` (0 B), `Ichigo-Ichi + Sonder` (0), `The opportunity that is concealed...` (12), `The 5 Elements` (27), `Prompt Engineering Made Me Understand Life` (37), `The Thoughtless Consciousness Paradox` (42), `What Is Intelligence` (127). Also `eBooks\The Metamorphosis of Prime Intellect...txt` (0), `TagStudio.txt` (41, one URL), `Prompts\Tutor URLS.txt` (95, one URL) |
| Developed idea | 19 | `Ideas\` 10; `Fan Theories\`: `Drama Is Deception`, `How To Systemize Writing`, `I Shall Rule`, `The Limits Of Traditional Computers...`; `I3\`: `Emotion, Grief, & Choice`, `Free Will, Existence, & Schizophrenia`, `The Champion Moment`, `The Machine - Life, Death, And Meaning`; `Prompts\Overcoming Fear of Failure...` |
| List | 6 | root: `Add to my IMDB Watchlist.txt`, `Classics I Want To Watch`, `Franchises Where A Sequel Is Better...`, `Marvel Cinematic Universe Content I Haven't Watched`, `Movies That Fail The Bechdel Test...`, `Movies With Sad Moments` |
| Fan theory | 15 | `Fan Theories - Fight Club`, `Fan Theories 01` to `10`; `I3\`: `Inception - Unified Theory v2`, `Inception PDT - Video Essay Script` (15 KB), `Inception PDT Deep Dive 2` (34 KB), `My Personal Inception Theory` (Hebrew) |
| Prompt | 6 | `Prompts\jep.txt`, `metaprompt.txt`, `Tutor prompt.txt`, `TELOS\telos_prompt.md`; `I3\Inception - Listener Profile v2`, `Inception - NotebookLM Focus Prompt` |
| Reference / how-to | 9 | `Implementing Relational Architectures...md` (23.6 KB), `Obsidian Plugins & Features.md`, `PKM.txt`, `eBooks\How to Remember Everything You Read.txt`, `eBooks\How To Take Book Notes.txt`, `Ideas\Change Framework Organizational Elements.txt`, `Prompts\SYSTEM PROMPTS.txt`, `Prompts\TELOS\problems.md` (11.8 KB), `Fan Theories\devcontainer.json` (misfiled Nexus config) |
| Image / pdf | 8 | `Ideas\`: `ACE.png`, `AQAL.png`, `SELF-MAX.png`, `ChangeFramework.png`, `1 Ikigai.jpg`, `1 The Cult Of Done PNG.png`, `flow-flywheel.pdf`; `Fan Theories\5 The-Drama-Triangle-v1.jpg` |

Gists, text under 6 KB:

- `PKM.txt`: the brief. "Have one or more local reasoning LLM to cooperate with me on writing and managing literature notes and atomic notes." Tags `#baby\#child\#adult`, `#quote`; 4 links.
- `Obsidian Plugins & Features.md`: 3 items; "links in properties (possibly the key to this PKMS)".
- `Add to my IMDB Watchlist.txt`: ~190 titles (90s TV, cartoons, MCU, 2023-25 films), 4 IMDb links.
- `Classics...` 31 films; `Franchises...` 21; `Marvel...` 13 + 1 link; `Bechdel...` 5; `Sad Moments` 37.
- `A.I. And Power...`: quoted comment. Too dangerous to democratize means too dangerous to centralize.
- `Choice.md`: quoted comment. Only the confused mind chooses.
- `The Champion Moment.md`: the real moment is unseen, after giving everything. Marked DRAFT, "must be expanded, refined, and connected to other notes".
- `The Option To Live In Isolation...`: Reddit quote + "My Take": technology kept him in his room 30 years.
- `Fan Theories 01` to `07`: one theory per `##` heading (Bond is a code name; Gadget became Dr. Claw; Fury wanted Coulson dead; Rose is Titanic's villain; Neville as Chosen One; Cipher was the first "One"; Cobb knows he dreams).
- `Drama Is Deception.md`: drama runs on characters holding different beliefs about one situation.
- `The Limits Of Traditional Computers...`: excerpt on what automation cannot do (source unnamed).
- `I3\`: `Emotion, Grief, & Choice` 3 definitions; `Free Will...` sanity as orderly surrender of free will; `The Machine...` comic link + thread on continuity of consciousness; the 2 prompts brief a podcast-style stress test of the Permanent Dream Theory.
- `Prompts\jep.txt` (edited today): mission text for jep. "27 pragmatic progressive prime pillars"; consume, critique, create; creation order Canon / Communication / Cycle.
- `Prompts\Tutor prompt.txt`: spec for a local offline tutor on the 4090 + "Absolute Mode" style block + About Me.
- `Prompts\Overcoming Fear of Failure...`: YouTube comment + reply + Gemini link + next question (why XCOM demands perfection).

Distilled, the 12 named files:

1. **How to Remember Everything You Read** (notes on YouTube `okHkUIW46ks`): consumption must be matched by digestion. PACER: Procedural - practice at once or stop reading. Analogous - critique the analogy (alike, different, where it breaks). Conceptual - map the network while reading. Evidence - store, then rehearse (which concept it proves). Reference - store, flashcards, least time. For the workshop: note type decides the processing step.
2. **How To Take Book Notes**: gist in a few sentences (comprehension test), key concepts, top quotes (links to quote notes), main ideas (atomic notes), raw passages, 7 questions (meaning, importance, use, reminds me of, what I add, criticism, good or bad). Twin in Idiverse.
3. **Internal Family Systems** (quoted Reddit comment): each part pursues one goal to keep the system safe; suffering = parts in disagreement; the job is mediation; trauma = a part stuck in one moment.
4. **Principles for a Purposeful Life**: AI-written overview + 23 maxims. Useful over successful; who you become over what you accomplish; passion project 30 min a day compounds; 12 min a day of reflection.
5. **The Human Transformer**: AI-written overview + Idi's text. In the moment, training decides, so train beforehand (knowledge, limits, incentives, habits, reflection); plan before, learn after; failure is feedback. Closes on "What are you prompting yourself with?"
6. **Change Framework Organizational Elements**: Vision (global why), Skills (how), Incentives (local why), Resources (people, tools, time), Action Plan (timing; without it, false starts). Caption for `ChangeFramework.png`.
7. **PLE Podcast**: transcript excerpt on work that survives automation (care, creative, experience providers, judgment, teaching as coaching), then Idi: "I want to prepare for an economy of meaning, attention, and emotion", then keyword lists. Twin: `Vaults BACKUPS\jep\PLE Podcast.md`.
8. **NON-DUALITY**: comment fragments. Union of subject and object; ego is a story; awareness with no entity behind it; separation = categorization, needed for reasoning, overused in language. Twin: Idiverse `Mini-Essays\Non-Duality.md`.
9. **metaprompt.txt**: Hard mode = Prompt Coach builds a blueprint section by section (Purpose, Instructions, Reference, Output), waits for every answer. Easy mode = AI Tutor, one diagnostic question at a time (max 5), harder only above 80%, commands `/batch` `/compact` `/checkpoint`. Twin: `Vaults BACKUPS\jep\Meta Prompt.md`.
10. **SYSTEM PROMPTS.txt**: 5 GitHub URLs of system-prompt collections. Pure link list.
11. **telos_prompt.md**: TELOS Coach interview: Problems, Missions, Narratives, Goals + Metrics, Challenges, Strategies, Projects, History, Log; fixed template with ID links (P1 to M1 to G1). Ancestor of `vault\telos\`.
12. **How To Systemize Writing**: every word, scene and character is a tool with an objective; a script is fixed, so it can be arranged like a jigsaw and tuned by experiment.

## 4. Scattered lists and URLs

Scan: 2,625 md/txt (`D:\work` depth 3 + whole archive; worktrees, `.git`, venv excluded). **171 files hold 3+ URLs; 9,454 URLs.** Browser bookmark exports 0. `.url` files 0. OPML 0. jep's `Desktop`, `Documents`, `Downloads`, `Favorites`: 0 user files.

| # | Cluster | Where | Files | URLs / size |
|--:|---|---|--:|---|
| 1 | XCOM mod lists | archive `Vaults BACKUPS\XCOM\Mods` (twin in `NEXUS BACKUP\projects\XCOM\data\orphans`; `specs\mods` 1 file) | 3 (+4) | 2,924 (+1,061) |
| 2 | Reprocessed Idiverse | archive `NEXUS BACKUP\vault\atomic_notes` | 28 of 261 | 469 |
| 3 | jep's research source lists | `vault\projects` root 7; `social-activities-2026-10-22` 3; `daily-note-research` 1 | 11 | 472 |
| 4 | AIMV research + docs | `aimv-lab` root 8; `kc-engine\reports`; `pa-video\research`; `acestep-docs`; `yt` | 17 | 406 |
| 5 | YouTube channel lists | Idiverse `YouTube - Education`, `YouTube - Entertainment`, `Spirituality YouTube Channels.md` | 19 | ~220 |
| 6 | Idiverse root notes | Idiverse root (`Prompts.md`, quotes); fork `_forks\NEXUS-Idiverse` | 6 (+1) | 121 (+50) |
| 7 | Investment research | archive `NEXUS BACKUP\projects\investment-research-system` | ~13 | ~95 |
| 8 | Persona business | archive `Vaults BACKUPS\TemporarilyTitleless` | 3 of 194 | 81 |
| 9 | Vault inbox | `vault\inbox` (2 link-rich; 3 YouTube transcripts in `TUTORING\`) | 24 | 65 |
| 10 | Film + TV lists | Idiverse `Film & TV` | 9 | `Film Backlog` 31.8 KB, `TV Show Backlog` 11 KB |
| 11 | Video game lists | Idiverse `Video Games` | 18 | 35; `Video Game Backlog` 24 KB |
| 12 | Social + partner lists | Idiverse pillars 18, 19 | ~26 | 34 |
| 13 | Books | Idiverse 15 epub + 15 stubs; PKMS 16 epub (6 twins); vault root 1 | 47 | 33 MB + 39 MB |
| 14 | AIMV references | `AIMVs\Refs.md`; 43 media at `AIMVs\` root; `lyrics\official` | 65 | 14 + 22 |
| 15 | PKMS lists + link stubs | `PKMS` root 6 lists; `PKM.txt`, `TagStudio.txt`, `Obsidian Plugins & Features.md`, `Prompts\SYSTEM PROMPTS.txt`, `Tutor URLS.txt` | 11 | ~20 |

Outside the table: `D:\` root holds 13 loose txt, 0 to 1,270 B, title-as-content (`Download eBooks.txt`, `Online streaming of films, tv shows & series, and more.txt`, `WORDS.txt`, `Civilization Ender.txt` dated today). `screens\9GAG` = 111 meme captures with `index.csv`.

## 5. Projects

| Project | Vault path (`D:\work\vault\`) | Outside vault | Newest | Entry point |
|---|---|---|---|---|
| AIMV video 2 "Pay Attention" | `projects\AIMV\` (245; `kit\` 192) | `D:\work\aimv-lab\` (`pa-video\`, `pa\`, `pay-attention\`); `D:\work\AIMVs\ours\pa-*`; `screens\AIMVs` | 2026-11-10 | `projects\AIMV\kit\v2-notes-rulings-2026-11-08.md`, then `aimv-lab\pa-video\briefs\plates-plan.md`. No status page |
| XCOM | `projects\XCOM\` (158, 49 MB; `Launch.log` 30 MB) | `D:\work\XCOM-archive-2026-09-11.zip`; `aml-settings-*.json`; `screens\XCOM`; archive (2 copies) | 2026-11-10 | `campaign-setup-2026-10-29.md` (state); `pick-sheet.md` (in play). No hub |
| Tutoring (closed 09-25) | 38 loose `projects\tutoring-*` and sim html; `tutoring-bakeoff\` (43); `tutoring-salvage\` (3) | `D:\work\tutoring-kit\` | 2026-10-05 | `projects\tutoring-salvage\tutoring-lessons-learned.md` |
| I4 | `projects\I4\` (5) | archive `NEXUS BACKUP\projects\I4\` (21; `i4-canon.md`); `PKMS\Fan Theories\I3\` (10) | 2026-10-04 | `projects\I4\i4-verdict-2026-09-27.md` |
| Curtains | `projects\Curtains\` (1) | archive `NEXUS BACKUP\projects\Curtains\` (171); `Vaults BACKUPS\Curtains\` (config only) | 2026-10-04 | None in vault. Archive root has `SYSTEM.md`, `backlog.json` (unread) |
| DECADEnts | `projects\decadents\` (20) + 2 loose `decadents-d1-*.md` | Idiverse root `DECADEnts*.md` | 2026-09-14 | `projects\decadents\decadents-bible.md` |
| Cash | `projects\Cash\` (91) | `screens\one-zero\` (empty); `D:\ONEZERO.txt`; archive `investment-research-system\` | 2026-11-11 | `projects\Cash\Cash Hub.md` (hub, last edit 09-11; `Money.md`, `Idi.md`, `Mom.md` edited today) |
| Kid Studio | `projects\kidstudio\` (11) + 4 loose `kidstudio-*.md` | `D:\work\studio\kidstudio\` (live) | vault 09-07; live 10-01 | `kidstudio\README.md` (in both) |
| Laptop retirement | `projects\laptop-retirement\` (7) | `D:\work\laptop-archive\` | 2026-09-26 | `laptop-retirement-2026-09-25.md`; next steps `handover-plan-2026-09-26.md` |
| PC stability | `projects\pc-instability-incident-2026-09-21.md`; `projects\pc-bios\` (4) | `screens\BIOS\` (empty) | 2026-09-21 | `projects\pc-instability-incident-2026-09-21.md` |

Pattern: 63 loose files sit at `projects\` root; project membership rides on filename prefix (`tutoring-`, `kidstudio-`, `decadents-`, `pc-`). Only Cash has a hub note that links its parts. Frontmatter `status` does not mark frozen work: `tutoring-lessons-learned.md` reads `status: active` although the chapter closed 09-25.

## 6. Gaps

- `C:\Users\Idi` and the `D:\` root folders: unread. Where Idi's live notes and bookmarks sit is unverified.
- `canonical-set.txt`: not grepped; `REDUNDANCY-MANIFEST.md` supplied its totals.
- Kind counts in section 2: estimates from folder names.
- `aimv-lab` below depth 3 and all worktrees: counted, unscanned.
- PKMS: 96 expected, 89 files found (+6 subfolders).
