---
type: guide
created: 2026-10-04
author: jep
status: active
tags:
  - cleanup
  - privacy
  - hq
---

# Name guard + rulings: guide (2026-10-04)

Built and verified today. Waiting on one word from Idi ("go A" or "go B") plus four steps only Idi can do. Names never appear in this file; the list lives at `C:\Users\jep\hq\private\name-blocklist.txt`, outside every repo.

## 1. Why the 08-2026 guard failed

| cause | proof | fix now |
|---|---|---|
| content scan covered only `lesson-transcripts/` + new `inbox/` files | old hook docstring, `tutoring-kit/tools/pre-commit-student-data.py` | every staged file, every folder, plus paths and commit messages |
| never installed on the PC; blocklist stayed on the laptop | `core.hooksPath` unset, `.git/hooks` samples only | hooks + list in `C:\Users\jep\hq\`, autocommit refuses to run without them |
| failures were silent; nothing tested the guard | none ran | self-test before every autocommit; nightly full-history scan; alerts at vault root |
| the 08-18 purge removed media, never names | 272 name hits across history on 10-04 | full rewrite to initials, all branches and tags |
| the guard's own audit log pushed search text | commit `306d737` | guard v3 stops logging read-only command text and redacts names |

## 2. The layers (all in `C:\Users\jep\hq\nameguard\`)

| # | layer | stops | state |
|---|---|---|---|
| L1 | write guard v3 (Claude hook) | jep or any agent writing a name into the vault or captures; `--no-verify`; hooksPath changes; names in the audit log | staged, 16/16 tests pass; needs I1 |
| L2 | `pre-commit` | name in any staged file or path; media, transcripts, files over 25 MB | built, self-test pass |
| L3 | `commit-msg` | name in a commit message | built, self-test pass |
| L4 | `pre-push` | any outgoing commit with a name, even one made with `--no-verify` | built, self-test pass |
| L5 | autocommit preflight | commits while any gate is broken; writes `_NAME-GUARD-DOWN.md` | wired, arms after go |
| L6 | nightly scan of every git object, vault + captures | anything the hooks missed, phone commits, names added to the list later; writes `_NAME-SCAN-HITS.md` | wired, arms after go |

Engine rules: whole-word match, Latin and Hebrew (with attached prefixes ו ה ב ל מ ש כ), case kept on the initial, binary files and embedded base64 images skipped, allow-phrases for non-students ("Ori and the Blind Forest", Daniel Miessler). Tests: `test_redact.py` 19/19, `test_guard.py` 16/16, `selftest.py` PASS.

## 3. History rewrite: done in a scratch clone, verified

- Clone: `C:\Users\jep\hq\private\rewrite\vault.git` (live vault untouched)
- 265 file versions redacted, 4 paths renamed (`tutoring-a-first-session.md`, `o-parent-brief.html`, and two old per-girl pages), 0 messages needed it
- Scan after: 0 hits in 3,156 objects, unreachable included
- 384 commits before = 384 after; 31 binary files byte-identical; current `main`: 56 files changed, every change a pure name-to-initial swap
- Also clean: captures repo (0 hits), jep memory (2 files redacted, rescan 0)

## 4. "go A" / "go B": what jep does on that word

A = delete and recreate the GitHub repo (recommended). B = force-push over the existing repo, then a GitHub Support ticket.

| | A recreate | B force-push |
|---|---|---|
| old history after | unreachable at once; restorable only by Idi's account for 90 days, then gone (GitHub docs, "Restoring a deleted repository") | reachable by commit ID in cached views until Support runs a cleanup (GitHub docs, "Removing sensitive data") |
| Idi's steps | I2 (3 clicks + paste a key) | a Support form with repo name + first changed commit |
| depends on a human at GitHub | no | yes |

jep's run, in order, after the word:
1. Pause autocommit (`hq\nameguard\PAUSE`), commit pending vault edits.
2. Re-prove each of the 14 worktrees redundant (content on `main`), then remove them and their local branches. One time, by hand, under this approval. The two rescues land first: `pc-hq-stack.md` s6 correction, Session 5 record.
3. Fresh mirror + rewrite + verify again (0 hits required, else stop).
4. Swap the live vault onto the clean history; expire old objects locally; scan live repo (0 hits required).
5. Push `main` + all tags (A: into the new empty repo; B: forced, old remote branches deleted).
6. Set `core.hooksPath` on vault + captures, create `ARMED`, run self-test, remove `PAUSE`, watch one autocommit push.
7. Delete the laptop's `~/vault` clone (0 unpushed, 0 dirty, checked 10-04; it holds the old named history).
8. Rulings that touch tracked files: R7 delete `d1-nine-decades-contact-sheet.html`; R9 delete `Idi's Whiteboard.md`, point `intent.md` at `daily/Today.md`.

## 5. Idi's steps (only where no other way exists)

**I1. Install guard v3** (the guard blocks every agent edit of itself, by design)
- File Explorer: copy `C:\Users\jep\hq\staging\vault-write-guard.py`
- paste into `C:\Users\jep\.claude\hooks\`, choose "Replace"
- tell jep "guard copied"; jep runs the 16 tests against the live file

**I2. GitHub, option A only** (no `gh` tool here; the PC key is a deploy key and cannot create or delete repos). Wait for jep's "ready for I2".
1. `github.com/IdanDalal/vault-backup` → Settings → General → bottom: "Delete this repository" → type the name
2. `github.com/new` → name `vault-backup` → Private → leave README, .gitignore, license unticked → Create
3. new repo → Settings → Deploy keys → Add deploy key → title `pc-hq` → paste the line below → tick "Allow write access" → Add
4. tell jep "repo ready"

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKatKva5uRCdnNdN4HE6hVjf3auR/oB6tpSVBvmJzndw pc-hq jep vault-backup deploy 2026-09-02
```

**I3. Laptop secrets** (R10): follow `projects/laptop-retirement/secrets-revocation-guide-2026-09-26.md`, plus 2 found today: Google service-account private key (`laptop-archive\...\NEXUS BACKUP\config\google-service-account.json`, revoke in Google Cloud console) and the JWT in `...\investment-research-system\specs\2025-12-28-system-configuration\tasks.md` (n8n, revoke or confirm dead).

**I4. Laptop wipe** (R10): after jep reports step 7 of section 4 done. Step-7 receipt from the takeover plan holds: 378 ok autocommits, 1 failed push, nightly tags pushed daily through 10-04. The laptop still holds `~/game3d` (389 MB; default player names of the girls per manifest D6), `~/kitchen` 7.8 GB, `~/root-work` 4 GB, `~/Downloads` 4.5 GB; the 09-25 map ruled everything beyond wave 1 disposable.

**I5. Phone captures:** initials only when typing about a student. The phone pushes straight to GitHub; no PC hook sees it first. The nightly scan flags it within a day.

**I6. New student or lead:** say the name once. jep adds it to the list the same day; the nightly scan then sweeps all history for it.

## 6. Blocked: the two scheduled deleters

The auto-mode safety classifier refused both schedules today. jep does not route around it. Each needs Idi's explicit word in chat, or a permission rule.

| deleter | built | blocked step | what it may delete |
|---|---|---|---|
| worktree pruner | design done, file write refused | writing `hq\janitor\prune_worktrees.py` | a worktree only when locked=no, idle 3 days, clean, every file on `main` byte-identical, every ignored file has a twin |
| media sweep | `hq\janitor\media_retention.py`, sandbox test PASS | adding it to the nightly task | only files jep marked processed (ledger + sha256 unchanged + receipt file exists); moves to `D:\work\_trash\`, purges after 14 days |

## 7. Rulings ledger

| # | ruling | state |
|---|---|---|
| R1 | B: history rewrite | built + verified (s3); push waits on go |
| R2 | A: guard + no search logging | built + tested; needs I1 + go |
| R3 | Kid Studio overhaul on hold | held; its local `allow.txt`, logs and 10-01 song files carry the names (never in git) |
| R4 | no binaries, embeddings, plugin code | DONE: 464 files, 290.9 MB deleted; `laptop-archive` 427 → 109 MB |
| R4b | backup of the remaining 109 MB (your own writing, D: only) | proposal: copy to `G:\Backup\laptop-archive\` (G: is a separate 699 GB drive, nearly empty); keeps the plaintext secrets off GitHub; say the word |
| R5 | A: forks kept, NEXUS Idiverse dropped | DONE: 13 fork files in `CORPUS-June-2026\_forks\NEXUS-Idiverse\`; twin proof passed before delete |
| R6 | B: delete XCOM screenshots | DONE: 9 PNG, 72 MB (findings live in `playtest-fixes-2026-09-17.md`) |
| R7 | A: delete nine-decades round 1 | waits on go (tracked file; lands on the clean history) |
| R8 | A: delete DASHBOARD.mp4 | DONE: 18.6 MB |
| R9 | A: retire the Whiteboard | waits on go |
| R10 | finish the laptop | I3 + I4 + section 4 step 7 |
| R11 | A: leads to initials | in the rewrite (s3) |

## 8. Residual risk, stated plainly

- A name the list does not hold (new spelling, nickname, surname) passes every gate until added. I6 is the control.
- Captures typed on the phone reach GitHub before any scan (I5).
- Kid Studio files and this session's local Claude transcripts hold names on this PC's disk; neither syncs anywhere.
- Option A: Idi's GitHub account can restore the old repo for 90 days. Option B: cached views until Support acts.
