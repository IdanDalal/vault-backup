---
type: project
created: 2026-09-25
author: jep
status: active
---

# K/D tutoring data: salvage receipts + delete manifest (2026-09-25)

Idi's ruling 2026-09-25: the K and D chapter closes; salvage everything useful from the raw data, then delete it. Next focus: new students. Nothing below is deleted until Idi says go.

## Salvage receipts

| salvaged | where | verified |
|---|---|---|
| Lessons learned S1-S6 (S5 + S6 raw mined; S1-S3 deltas; playbook for a single new student; K/D-specific items fenced off) | [[tutoring-lessons-learned]] (3,365 words) | blocklist check 0, em dashes 0 |
| Pipeline design (drop → process → distill → send copies → name guard), what broke, what to keep | [[PIPELINE]] + `D:\work\tutoring-kit\tools\PIPELINE.md` | blocklist check 0 |
| Word World template = master + 6 fixes that lived only in the girls' copies (journal rewrite, Enter re-fire, earn-flow keys, free cursor, Esc pause, probe API) | `D:\work\tutoring-kit\games\word-world-template.html` + `word-world-copy-only.patch` | blocklist 0; headless Edge loads title screen |
| Game Lab (2D) template, student config replaced by placeholder | `D:\work\tutoring-kit\games\game-lab-template.html` | blocklist 0; loads "MY GAME" start screen |
| Generic tools: `process_tutoring.py`, `make_send_copies.py`, `pre-commit-student-data.py` (names now from roster/blocklist files) | `D:\work\tutoring-kit\tools\` | compile; not run on live data |
| Word World source + build tools | `D:\work\laptop-archive\home\game3d\` (wave 1) | see D6 |

Gaps: S4 raw transcript not mined (the permission classifier stopped the read; S4 rests on its distillation). Gameplay and phone width of the templates untested.

## Delete manifest

| # | target | size | contents | salvage covers it? | jep default |
|---|---|---|---|---|---|
| D1 | laptop `~/tutoring-data/` (whole folder) | 464 M | S1-S4 audio (23), photos (10), records (7), S5 raw in `drop/`, per-girl games (4), `send/` (2), tools, `blocklist.txt`, pre-purge history bundle 119 M | yes, rows above | delete |
| D2 | PC `D:\work\vault\projects\tutoring-bakeoff\lesson-transcripts\*.LESSON.md` | 828 K | S5 + S6 raw transcripts (gitignored, never on GitHub) | yes, mined | delete; DISTILLED.md files stay |
| D3 | PC `C:\tutoring-bakeoff\` | 6.4 G | lesson audio, 1.3 G lesson transcripts, 4 photos (08-17), 4.9 G venv | scripts + results already in vault `projects/tutoring-bakeoff/` | delete |
| D4 | laptop `~/Downloads/` 2 voice memos (07-16) + 2 phone photos (07-07, 08-13) | small | unopened; 07-16 = Heblish test clip date | n/a | delete |
| D5 | PC `D:\work\studio\kidstudio\archive\` + `out\` | 35 M | the girls' Kid Studio creations: 47 voice clips, 20 mp3, 12 images | keepsake or nothing | delete (keepsake for the girls = Idi overrules) |
| D6 | default player names in 3 files of `D:\work\laptop-archive\home\game3d` | n/a | two names starting K and D, absent from the blocklist and from the vault (0 files) | template already clean | scrub to "Player 1/2"; the classifier blocked jep's scrub, needs Idi's explicit word |

Status 2026-09-25, after Idi's go: D2, D3, D5 DELETED by jep (paths verified absent). D1, D4 blocked by the auto-mode classifier, D6 blocked earlier: Idi did these by hand the same day (D6 by deleting the archived game3d). All six verified absent by jep. Manifest CLOSED.

Stays: vault DISTILLED.md S1-S6, `tutoring-operating-principles.md`, briefs, cheatsheets (initials-only by design); GitHub history (purged 08-18).
Later, with the laptop wipe: laptop `~/.claude` transcripts (may hold names).
