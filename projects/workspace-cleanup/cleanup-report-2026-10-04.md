---
type: report
created: 2026-10-04
author: jep
status: active
tags:
  - cleanup
  - hq
---

# D:\work cleanup - audit report (2026-10-04)

Read-only pass. Nothing moved, deleted or edited. Done-state: every folder classified, every action tagged, every unknown turned into a numbered ruling with a recommendation.

Detail tables: `workspace-cleanup/audit-vault.md` (527 vault files) and `workspace-cleanup/audit-outside.md` (everything outside the vault). This file is the decision layer.

## The picture in one table

| area | size | files | verdict |
|---|---|---|---|
| `studio/kidstudio/venv` | 1052 MB | 28,238 | Python packages for Kid Studio (venv = a private Python install for one app). 96 % of `studio/`. Keep while Studio lives |
| `vault/.claude/worktrees` | 631 MB | 4,922 | 14 old git worktrees (worktree = a full extra copy of the vault, one per past job). All work already on `main` except 2 items. **Biggest safe win** |
| `laptop-archive` | 427 MB | 4,142 | Laptop corpus, sole copy, no backup. 291 MB is derived junk (Linux binaries, embeddings, plugin code); ~100 MB is real authored material |
| `vault/projects` | 146 MB | 348 | 118 MB is XCOM (30 MB launch log, 72 MB screenshots, 3.8 MB settings copies) |
| `vault/.git` | 59 MB | - | git history. Shrinks only by a history rewrite. Leave |
| `screens` | 46 MB | 120 | Misnamed: holds 9GAG and Poker exports (wins-jar evidence), one 18 MB video |
| `vault` rest | ~20 MB | ~600 | inbox 16 MB (SELF-MAX images), daily, bases, config |
| root loose files | 9.4 MB | 4 | XCOM zip (only copy of 187 files) + AML settings snapshot |
| `tutoring-kit`, `captures`, `drop` | 4 MB | 76 | small, live |

Total ~2.4 GB. Reclaimable: **~975 MB with no ruling needed** (Batch 1), up to ~2.1 GB with rulings.

## Tier 0 - urgent, not about space

1. **Student names on GitHub.** Full first names of K and D (minors) sit in 16 tracked files pushed to `IdanDalal/vault-backup`: `projects/tutoring-sisters-monday-cheatsheet.md` + `.txt`, `projects/tutoring-sisters-9-12.md`, `projects/emergent-system.html`, `projects/sisters-first-contact-sim.html`, `inbox/parts-registry-draft.md`, 11 digests in `daily/digests/` (07-27 to 08-23). Verified by jep reading `tutoring-sisters-monday-cheatsheet.md` line 11 with masked output. `tutoring-salvage/delete-manifest-2026-09-25.md` claims the cheatsheets are initials-only: false.
2. **No name guard on the PC.** `core.hooksPath` unset, `.git/hooks` holds only samples. The vault `CLAUDE.md` describes a pre-commit name block that does not run here. A ready hook sits unused at `D:\work\tutoring-kit\tools\pre-commit-student-data.py`. Laptop-retirement item R2, still open.
3. **The audit trail leaks.** The write-guard logs every Bash command verbatim into `.vault-config/audit/*.jsonl`, which autocommit pushes. Today's audit agent searched for the names, and commit `306d737` (11:00) pushed that search line to GitHub. Same exposure class as item 1, one more copy.
4. **Secrets in the laptop corpus** (paths only, values never printed): `NEXUS BACKUP\config\google-service-account.json` (private key, missing from the README list), `NEXUS BACKUP\projects\investment-research-system\specs\2025-12-28-system-configuration\tasks.md` (JWT, missing from the list), `NEXUS BACKUP\docker-compose.yml` (API key). Local disk only, never on GitHub. Revocation = laptop-retirement R4, open.
5. **Kid Studio contradiction.** The 09-25 delete (manifest D5) removed `studio\kidstudio\archive\`, which also took the v5/v6 backups, so `swap-v6.bat` and `v6-build\build_v7.py` are now broken. Then on 10-01 the app ran again: 6 songs, 9 new words, `log\K.txt` + `log\D.txt`. Kid data is back on the PC after the chapter closed.

## Batch 1 - safe, lossless, ~975 MB (needs only "go")

Each row has its proof of a second copy or of being regenerable.

| #   | target                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | MB  | proof                                                                                                                |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------- |
| 1   | 14 worktrees under `vault/.claude/worktrees` (folders only; branches stay in git)                                                                                                                                                                                                                                                                                                                                                                                                   | 631 | every branch file checked by content hash: identical on `main` or older than `main`. Exceptions rescued first, row 2 |
| 2   | rescue before row 1: copy `pc-hq-stack.md` section 6 correction (branch `worktree-parts-registry-draft-two`, 09-05) onto `main`; move the S5 lesson record `24_Aug_at_9-03.DISTILLED.md` from that branch into `tutoring-salvage/records/`                                                                                                                                                                                                                                          | 0   | main still carries the false "secrets on GitHub" claim; S5 record exists only on that branch                         |
| 3   | laptop corpus derived files: Linux `llama-b7519` binaries, Obsidian vector-index embeddings, plugin code (keep each `data.json`)                                                                                                                                                                                                                                                                                                                                                    | 291 | binaries + plugins re-downloadable ungated; embeddings regenerate from notes                                         |
| 4   | `projects/XCOM/Launch.log`, `XCOM2 AML 1.6.0-beta/AML.log`                                                                                                                                                                                                                                                                                                                                                                                                                          | 36  | game rewrites both; gitignored                                                                                       |
| 5   | XCOM stale snapshots: AML `settings.json` copy, `settings.json.STALE-...-do-not-restore`, ini `.STALE`/`.bak`, BattleChatter `-1053`, `jepFixes.STALE-2026-09-11-snapshot/`, `jepFixes/README-2026-09-11.md`                                                                                                                                                                                                                                                                        | 8   | live copies verified (`C:\XCOM2 AML 1.6.0-beta\settings.json` dated 10-03); md5 twins; git history keeps them        |
| 6   | DECADEnts round 1-3 contact sheets for the 2020s head (`d1-contact-sheet.html`, `d1-2020s-contact-sheet.html`, `-2`, `-3`)                                                                                                                                                                                                                                                                                                                                                          | 4   | picks + seeds recorded in `decadents-d1-quest-2026-09-10.md`; git history                                            |
| 7   | small residue: root `wins-jar.md` (older twin of `projects/wins-jar.md`, also fixes an ambiguous link), `work/projects.md` + `work/projects 1.md` (0 B accidents), `.stignore`, 4 tracked `.pyc`, `tutoring-bakeoff/lesson-transcripts/LOG.txt`, `tutoring-sisters-monday-cheatsheet.txt` (older twin), `XCOM-archive-2026-09-11_delete.py` (spent), `kitchen-nexus-extras/.claude.archived` (sha1 twin), kidstudio `log/*.png`, `__pycache__`, `swap-v6.bat`, empty `screens/BIOS` | 5   | each listed with its twin in the detail files                                                                        |

## Rulings needed (numbered, each with jep's recommendation)

| #   | question                                                                                                                | options                                                                                                                 | jep recommends                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| R1  | Names in 16 files on GitHub                                                                                             | A redact to initials now, no history rewrite; B redact + rewrite history (as on 08-18); C leave                         | **A now**, B only if you want GitHub clean of every past copy. Rewrite costs: all branches, 18 tags, both machines' clones |
| R2  | Name guard on the PC                                                                                                    | A install the kit hook now; B wait for the next student                                                                 | **A**. Also stop the audit log from logging search patterns                                                                |
| R3  | Kid Studio future                                                                                                       | A keep for home use (keep venv, freeze a package list first); B retire (frees 1052 MB + 23 MB kid output)               | A if the girls still use it at home (10-01 says yes); either way delete 10-01 kid data only on your word                   |
| R4  | Laptop corpus backup                                                                                                    | A strip derived (Batch 1 row 3), then push the ~100 MB remainder to a new private GitHub repo; B second disk; C nothing | **A**. One disk, no backup today                                                                                           |
| R5  | NEXUS vs Vaults Idiverse copies (8 forked notes differ)                                                                 | A keep both fork versions in `_forks\`, drop NEXUS copy (41 MB); B keep both trees                                      | **A**                                                                                                                      |
| R6  | `XCOM/screenshots/1-9.png` 72 MB, 4K, 09-18, no backup                                                                  | A move to `D:\work\archive\xcom\`; B delete; C keep                                                                     | **A**                                                                                                                      |
| R7  | DECADEnts nine-decades round 1 (9.4 MB) next to round 2                                                                 | A delete (rulings live in the quest file); B keep                                                                       | **A**                                                                                                                      |
| R8  | `screens/DASHBOARD.mp4` 18.6 MB motion reference                                                                        | A delete; B keep for a v5 skin                                                                                          | **A**                                                                                                                      |
| R9  | `Idi's Whiteboard.md` empty since 09-26 (39-line list recoverable from git)                                             | A retire, `daily/Today.md` is the surface; B keep as Dump valve                                                         | your call; it drives `intent.md` wording                                                                                   |
| R10 | Laptop wiped (step 7, due 09-28)?                                                                                       | yes then archive `projects/laptop-retirement/`; no then reschedule                                                      | -                                                                                                                          |
| R11 | Child leads named by first name (`tutoring-a***-first-session.md`, `tutoring-cousin-son-9.md`, `o**-parent-brief.html`) | A initials like K/D; B keep                                                                                             | **A**, same rule as students                                                                                               |

## Batch 2 - hygiene after rulings (no space, clarity for agent readers)

1. Rewrite dead docs: vault `CLAUDE.md` (Unix group layer, `claude-vault`, cron, Telegram, `~/vault`, Syncthing, restic: all laptop-era), `emissary-maintenance.md` (Telegram + digests listed LIVE), `pc-hq-stack.md` s3/s4, user `CLAUDE.md` "read-only until P3" (flip done 09-26). `CLAUDE.md` + `intent.md` edits need your word.
2. Archive `.vault-config/scripts`, `prompts`, `tests`, `hooks/capture_hook*`, `write-deny.list` into `.vault-config/_laptop-era/` (live copies: `C:\Users\jep\hq\`, `vault-write-guard.py`). `.vault-config` is write-forbidden for jep: your move or your word.
3. Tutoring closed chapter: 23 files to `projects/tutoring-salvage/` (records, word-world, research) with `status: archived`; open statuses on S7 files pollute Bases.
4. Group by project: DECADEnts quests into `projects/decadents/`; `screens/` renamed `D:\work\exports\` (9GAG, Poker); root XCOM zip + manifest + AML snapshot into `D:\work\archive\xcom\`.
5. Kid Studio repairs: `index-v6.html` is a v7 twin (rename or drop), README points at dead `archive\` paths, vault `projects/kidstudio/` is a stale 09-07 mirror (mark stale or refresh).
6. Daily note stale since 09-19 (skill never rolled), digests stopped 09-26: one rollover run fixes `Today.md`.
7. `bases/projects.base` shows 20 of ~100 project files (filters `type == "project"`); 7 broken wikilinks; Cash company notes lack frontmatter and use off-enum `status: bench`.
8. `inbox/` items to route (your call by rule): SELF-MAX images (15 MB), `IMDb_EDA.ipynb` at root, `weekly-archive.bat`, two filenames with leading spaces.

## Assumptions (overrule any)

1. Git branches are kept when worktree folders go; refs cost bytes. Deleting branches is a separate, later ruling.
2. Anything in git history counts as a second copy for working-tree deletes.
3. The laptop is gone or going, so laptop-era scripts are reference only.
4. Kid Studio still runs at home (10-01 activity).
5. XCOM play continues, so live mod sources and reports stay.
6. Your own files (`author: Idi`, `XCOM VAULT/`, `specs/`, `telos/`, `atomic-notes/`) are untouched by any batch.

## Method and receipts

- Sizes: `du` per folder, two levels deep.
- Worktrees: per branch, every changed file's blob hash checked against `main`'s whole tree; non-matches compared by last-commit date. 3 branches never pushed (`d1-quest`, `decadents-d1-round4`, `xcom-chosen-missions-0926`): all content on `main`.
- Duplicates: md5 over 4,846 files (venv, .git, worktrees excluded): 880 groups, 132 MB wasted, 128 MB of it NEXUS vs Vaults inside the corpus.
- Names: agent grep over tracked files; jep spot-check masked.
- Secrets: classifier printing types and counts only.
- Not done: no file read inside `telos/` beyond inventory; no content judgement on your own notes; Docs on GitHub branches not audited.
