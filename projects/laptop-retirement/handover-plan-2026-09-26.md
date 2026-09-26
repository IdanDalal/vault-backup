---
type: project
created: 2026-09-26
author: jep
status: active
---

# Laptop → PC handover plan (proposal, 2026-09-26)

Done-state: the PC is the only vault writer, every laptop job is off or ported, 48 h of PC autocommits land on GitHub, and nothing depends on the laptop. Then the laptop can be wiped.

Nothing here is built yet. Idi rules on the three defaults in section 3; jep does the rest.

## 1. Where things stand (probed 2026-09-26)

| fact | value |
|---|---|
| Laptop is still the writer | autocommit pushed `6d13b13` today 09:30 |
| PC `main` | `3feb087` (09-02), 11 commits behind GitHub, 0 ahead |
| PC working tree | many uncommitted edits: Idi's Obsidian edits (Whiteboard, Cash, identity folder) + every deliverable jep copied into `projects/` |
| jep branches not on `main` | 11 (cash console v1-v3, intent layer, daily note, XCOM, DECADEnts, session 7, parts registry, laptop retirement); their files already sit in the PC working tree as copies |
| PC scheduled tasks | `psmux-hq`, `Cash Console refresh` (both registered by jep) |
| Name guard hook on PC | none (`core.hooksPath` unset) |

## 2. Laptop jobs and their fate

| laptop job | schedule | fate | PC form |
|---|---|---|---|
| autocommit + push | every 30 min | **port** | scheduled task, push failure written to a loud flag file at vault root + a line in `daily/Today.md` |
| nightly snapshot tag | 00:00 | **port** | scheduled task |
| backup-health | every 6 h | **replace** | folded into the autocommit task: "last push older than 2 h" → flag file (the laptop version never passed and checks the wrong Syncthing unit) |
| git gc monthly | 1st, 04:00 | **drop** | git runs its own gc automatically |
| morning digest | 09:00 | **retire** (default) | `daily/Today.md` replaced it on 09-13 |
| Sunday loop review | Sun 09:17 | **retire** (default) | the daily-note skill covers the review loop; port later if missed |
| Telegram bridge `kitchen-telegram` | always on | **retire** (default) | phone capture already runs through GitSync → `D:\work\captures` |
| restic, Syncthing | inert / peerless | drop | nothing depends on them |

## 3. Rulings for Idi (defaults marked)

| # | question | default | what it does |
|---|---|---|---|
| H-a | morning digest | retire | no more 09:00 digest files or Telegram digest; Today.md stays the daily entry |
| H-b | Sunday loop review | retire | no weekly review file; re-port later from `.vault-config/prompts/loop-review.md` if missed |
| H-c | Telegram bot | retire + revoke its token | no Telegram path to jep; phone captures keep flowing via GitSync. Porting it later = Claude Code channels on the PC, a separate decision |

## 4. Steps (jep runs them in this order)

| step | action | why this order | receipt |
|---|---|---|---|
| 1 | Laptop: one last autocommit + push, then comment out all 7 crontab lines, stop + disable `kitchen-telegram` | two writers on `main` collide; the Telegram bot is single-instance | `crontab -l` shows only comments; `systemctl --user is-active kitchen-telegram` = inactive |
| 2 | PC: bring `main` up to GitHub (11 laptop commits), then commit the PC working tree on top as one "PC takeover" commit | Idi's Obsidian edits and all copied deliverables land in history in one step | `git status` clean; `main` = `origin/main` + 1 |
| 3 | Push `main` from the PC | PC becomes the writer | GitHub head = PC commit |
| 4 | Register the PC autocommit (30 min, with the health check) and nightly-tag tasks | same behavior as the laptop, failures loud | task list + first two automatic commits on GitHub |
| 5 | Watch 48 h | proves the schedule survives reboots and idle | ≥ 90 autocommits, 2 nightly tags, 0 laptop commits |
| 6 | Laptop wipe (Idi) | after the secrets guide steps are done | see [[secrets-revocation-guide-2026-09-26]] |

Branches: after step 2 the 11 jep branches are history only. They stay on GitHub untouched; nothing to decide.

## 5. Risks

| risk | effect | guard |
|---|---|---|
| a jep scheduled task only runs while jep is logged on | autocommit silently stops after a reboot until the hq session starts | the `psmux-hq` boot task logs jep in; step 5 covers a reboot. If it fails, Idi types jep's password once in Task Scheduler ("run whether user is logged on or not") |
| autocommit pushes anything in the vault | a student file or name dropped into the vault goes to GitHub within 30 min | K/D raw data is gone (manifest closed 09-25). Install the generic name-guard hook from `D:\work\tutoring-kit\tools\` before the first new student's first session |
| step 2 conflicts | a file edited on both sides since 09-02 | only laptop digests changed on GitHub; jep resolves, Idi's text wins every tie |
| laptop blocked by the permission classifier in step 1 | jep cannot edit the laptop crontab | jep hands Idi a 2-line paste, same as the D1 deletion |
