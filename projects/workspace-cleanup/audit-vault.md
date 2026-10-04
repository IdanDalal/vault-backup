---
type: audit
created: 2026-10-04
author: jep
status: done
---

# Vault audit - D:\work\vault (READ-ONLY pass, 2026-10-04)

Scope: whole vault minus `.claude/worktrees/` and `.git`. 527 files, 171 MB on disk, 510 tracked in git (pack 54 MB). Method: python walk (md5, size, mtime, frontmatter parse), wikilink resolver, `git ls-files` / `status --ignored`, scheduled-task query, spot reads. Nothing modified.
Note: this audit's own grep commands were logged by the write-guard into `.vault-config/audit/edits-pc-2026-10.jsonl` (untracked, next autocommit pushes it). One logged command line carries the K/D first names as search terms. Same names already sit in tracked files (finding S1), so no new exposure class, but the audit JSONL logs every command verbatim and goes to GitHub.

## Top findings (severity order)

- S1 STUDENT NAMES IN GIT: full first names of K and D (minors) in 4 tracked project files + 1 inbox file + 11 digests, pushed to GitHub. Files: `projects/tutoring-sisters-monday-cheatsheet.md` + `.txt`, `projects/tutoring-sisters-9-12.md`, `projects/emergent-system.html` (also a lead's adult name), `projects/sisters-first-contact-sim.html`, `inbox/parts-registry-draft.md`, `daily/digests/2026-07-27,07-30,07-31,08-01,08-03,08-11,08-12,08-14,08-17,08-18,08-21,08-23-loop-review`. Digests also quote raw-folder names `...-First-Lesson-<names>/`. `tutoring-salvage/delete-manifest-2026-09-25.md` claims "briefs, cheatsheets (initials-only by design)": false.
- S2 NAME GUARD ABSENT ON PC: no `core.hooksPath`, `.git/hooks` holds only `*.sample`. `C:\Users\jep\hq\vault-autocommit.sh` honours `_COMMIT-BLOCKED.md` but nothing creates it. Generic hook exists unused at `D:\work\tutoring-kit\tools\pre-commit-student-data.py`. Known as laptop-retirement R2, still open. Vault `CLAUDE.md` tutoring section describes enforcement that does not run here.
- S3 OTHER MINORS/LEADS BY FIRST NAME: `tutoring-a***-first-session.md` (9 y.o., title + body), `tutoring-cousin-son-9.md` (9 y.o., title + body), `o**-parent-brief.html` (Hebrew title carries the name), `tutoring-former-neighbor-3kids.md` (adult lead + sons). Leads, not session records, so outside the hook rule; flag for Idi's policy call.
- S4 DEAD LAPTOP MACHINERY: `.vault-config/scripts/*.sh` (all `$HOME/vault`, `systemctl syncthing@idan`), `write-deny.list` (`/home/jep/...`, `claude-vault`), `tests/` (`/workspace`, `~/vault`, `~/vault-agent`), `prompts/*` (Telegram chat id, laptop cron), `hooks/capture_hook*` (not wired in any settings.json). Live PC equivalents: `C:\Users\jep\hq\vault-autocommit.sh`, `vault-nightly-tag.sh`, `C:\Users\jep\.claude\hooks\vault-write-guard.py`. Digests stopped 2026-09-26 (last file `daily/digests/2026-09-26.md`).
- S5 FALSE CLAIMS IN LIVE DOCS: `pc-hq-stack.md` s6 says the Nexus `.env` is in the vault and on GitHub. False: `inbox/CORPUS-June-2026/` gitignored since 2026-06-10 (emissary-maintenance log) and verified never pushed 09-05; folder no longer exists in the vault (now `D:\work\laptop-archive\CORPUS-June-2026\`, `.env` not present there either). s3 paths `inbox/CORPUS-June-2026/NEXUS BACKUP/...` dead. s4 "read-only PAT (P1)" superseded (write flip done 09-26). `emissary-maintenance.md` (status active) still lists Telegram capture, 09:03 digest, evening ping as LIVE. `intent.md` puts the "Today" block in `Idi's Whiteboard.md`; daily-note system moved it to `daily/Today.md`. Vault `CLAUDE.md`: Unix group layer, `claude-vault` wrapper, `run-agent.sh` + cron, Telegram, `~/vault` paths, Syncthing/restic, `~/tutoring-data` pipeline: all laptop-era. User-level `C:\Users\jep\.claude\CLAUDE.md` still says vault "Read-only until P3" (flip done 09-26; outside vault scope, noted only).
- S6 STALE LIVE SURFACE: `daily/Today.md` headed Saturday 2026-09-19, 15 days stale (file touched 10-04, uncommitted). Its d1-d3 items are 09-19 era. Daily-note skill has not rolled since 09-19; dated archives exist only for 09-13 and 09-14.
- S7 GIT CHURN: Task "Cash Console refresh" rewrites `Cash-Console.html` (480 KB), `data/market.json` (156 KB) and ~20 company notes daily inside the vault; autocommit pushes each run. Contact sheets with inline base64 images (20 MB) and two 3.8 MB AML settings copies are tracked. Removing files now frees working tree only; history keeps them.
- S8 TRACKED CACHE: `__pycache__` tracked in `.vault-config/tests/` (2 pyc) and `projects/tutoring-bakeoff/` (2 pyc), committed before the 09-26 `__pycache__/` ignore rule. `projects/Cash/dashboard/__pycache__/` is ignored correctly.
- S9 AMBIGUOUS LINK TARGET: `wins-jar.md` exists at root (stale, Built 117/Received 102, 09-05) and `projects/wins-jar.md` (current, Built 204/Received 103, 09-14). Any `[[wins-jar]]` resolves ambiguously in Obsidian.
- S10 OBSIDIAN TRAPS: TELOS index link `[projects/](work/projects/)` resolves from vault root, so clicks created empty `work/projects.md` and `work/projects 1.md` (both 0 B, committed 09-26). Daily-notes core plugin uses `templates/daily-note.tpl` while Templater `trigger_on_file_creation: false`, so notes made from it keep raw `<% tp.date... %>` (see `daily/2026-04-05.md`, `2026-04-13.md`).

## Root

| path | what | state | action | reason |
|---|---|---|---|---|
| `CLAUDE.md` | vault governance, loads every session | live, partly false (S5) | ASK-IDI | root is outside jep write area; laptop enforcement, cron, Telegram, `~/vault`, pre-commit hook text no longer true on PC; needs a PC rewrite on his word |
| `IMDb_EDA.ipynb` (952 KB) | Idi's 2025-09 IMDb notebook, source of his EDA style (memory `idi-eda-style`) | reference, orphan at root | MOVE to `resources/` (Idi's area) | size is embedded chart outputs; root clutter; no note links it |
| `Idi's Whiteboard.md` (0 B) | release valve + jep "Today" block per intent.md | emptied by Idi's Obsidian edit, commit d80dce6 (09-26); 39-line word list recoverable at `d80dce6^` | ASK-IDI | intent.md still names it the Today surface; daily/Today.md replaced that; empty or retired? |
| `wins-jar.md` | wins jar, 09-05 copy | superseded | DELETE-CANDIDATE | second copy `projects/wins-jar.md` exists, newer (09-14), counts 204/103 vs 117/102; also in git history; fixes S9 |
| `.stignore` | Syncthing ignore list | dead (Syncthing never had peers; laptop retired) | DELETE-CANDIDATE | 103 B, disposable, in git history |
| `.gitattributes` | `*.md merge=union` | live, harmless | KEEP | still guards any future two-writer merge |
| `.gitignore` | ignore rules incl. student-media guardrails | live | KEEP | add nothing; `inbox/CORPUS-June-2026/` and `inbox/TUTORING/20*/` lines now point at absent paths, harmless |
| `work/projects.md`, `work/projects 1.md` (0 B each) | accidental Obsidian creations from the TELOS folder link | orphan, empty | DELETE-CANDIDATE | 0 bytes, identical (md5 of empty); cause = S10; recurs until TELOS link changes (Idi edits telos) |
| `.claude/skills/obsidian-*` (2) | vault-scoped skills, tracked before `.claude/` ignore | live | KEEP | no frontmatter needed (skill format) |
| `.claude/settings.local.json` | local settings | ignored | KEEP | n/a |

## daily/

| path | what | state | action | reason |
|---|---|---|---|---|
| `daily/Today.md` | fixed daily tab (daily-note skill) | live but stale since 09-19 (S6) | KEEP | run the daily-note rollover; uncommitted edit 10-04 may be Idi's typing under "Yours" |
| `daily/2026-09-13.md`, `2026-09-14.md` | dated archives, author jep | live archive | KEEP | 09-15 to 10-03 archives missing (no rollover ran) |
| `daily/2026-04-05.md` | byte-identical to `templates/daily-note.tpl.md`, unrendered Templater | empty placeholder, author Idi | ASK-IDI | author: Idi = read-only for jep; disposable by content |
| `daily/2026-04-13.md` | Idi daily with unrendered `created` | Idi-owned | KEEP | fix of `created` is Idi's |
| `daily/2026-07-05.md`, `2026-07-06.md` | Idi dailies | Idi-owned | KEEP | same stem as digests of same day; harmless |
| `daily/digests/*` (56 files, 06-29 to 09-26, ~540 KB) | laptop cron morning digests + 4 loop reviews | stale archive; producer dead since 09-26 | KEEP (11 need name redaction, S1) | history; frontmatter complete; 2 broken `[[ADR-005-portability-tiers]]` in 08-30 files (target only in `D:\work\laptop-archive\CORPUS-June-2026\NEXUS BACKUP\data\decisions\`) |

## inbox/ (routing is Idi's; actions are recommendations for his review)

| path | what | state | action | reason |
|---|---|---|---|---|
| `inbox/SELF-MAX/` (4 PNG 15.4 MB + 2 md 71 KB) | SELF-MAX framework material; `hoe_math LEVELS CHART.png` 10 MB is the largest tracked file | reference, tracked, md lack frontmatter | ASK-IDI (MOVE to `resources/self-max/`) | morning-digest prompt skipped it on purpose; long-term reference, not inbox |
| `inbox/TUTORING/` (3 md, 149 KB) | YouTube transcripts (Veritasium, myth, villager), tutoring philosophy sources | reference; two names start with a space | RENAME (strip leading/trailing spaces) + ASK-IDI on MOVE to `projects/tutoring-salvage/sources/` | no student data; leading-space filenames break shell tools |
| `inbox/DAILY-TEMPLATE-EXAMPLES/` (6 md) | third-party daily templates (2024) | research input to daily-note system, done 09-13 | ARCHIVE | daily-note v0 shipped; no frontmatter |
| `inbox/Guide.txt`, `inbox/Transcript.txt` (44 KB) | GitSync guide + video transcript for phone-capture quest | quest done 09-13 | DELETE-CANDIDATE | public web text, reproducible; result lives in `projects/phone-capture-sync-quest-2026-09-13.md` |
| `inbox/Studio Preflight.html` | Studio preflight page (referenced by decadents files) | likely live reference | ASK-IDI | is it still the preflight he uses, or superseded by `projects/decadents/` docs? |
| `inbox/parts-registry-draft.md` | Draft Zero of parts registry | superseded by `projects/parts-registry.md` (Draft Two) | ARCHIVE (status: archived) | also carries K/D first names (S1) |
| `inbox/standing-prompts-draft.md` | wiring draft for digest/evening prompts (06-10) | dead (prompts installed, evening retired, laptop gone) | ARCHIVE | status todo is false |
| `inbox/P4C-research.md` | Philosophy for Children research (07-06) | reference, untouched 3 months | ASK-IDI | keep for next-student playbook or archive? |
| `inbox/seed-telescope-x-bowstring.md` | jep seed note | idle, status todo | ASK-IDI | pairs with Idi's atomic note "The Telescope Metaphore" |
| `inbox/nate-b-jones-second-brain.md` | Idi idea stub, status todo | Idi-owned | KEEP | author Idi |
| `inbox/weekly-archive.bat` | robocopy Documents/Desktop/Pictures to G:\Backup | unknown if used; save-folder line still a placeholder | ASK-IDI | if live, MOVE to `C:\Users\jep\hq\` or Curtains; scripts do not belong in inbox |

## projects/ - tutoring (chapter closed 2026-09-25)

| path | what | state | action | reason |
|---|---|---|---|---|
| `tutoring-salvage/` (3 md) | lessons learned, PIPELINE, delete manifest | live | KEEP | `PIPELINE.md` byte-identical to `D:\work\tutoring-kit\tools\PIPELINE.md` (md5 3a2d269f); manifest "cheatsheets initials-only" claim false (S1) |
| `tutoring-operating-principles.md` | principles + contradictions 1-9 | live reference for next student | KEEP | vault CLAUDE.md requires it before tutoring work |
| `tutoring-session-skeleton.md`, `tutoring-session-tracker.md`, `tutoring-universal-baseline.md`, `lesson-one-field-guide.md` | generic session tools | live, student-agnostic | MOVE to `projects/tutoring-salvage/` (or a `tutoring/` folder) | reusable for next student; `lesson-one-field-guide.md` has broken `[[SUPPLIES.jpg]]` (image never in vault) |
| `tutoring-sisters-9-12.md` | K/D brief | closed chapter, contains names (S1) | ARCHIVE (status: archived) + redact names | chapter closed |
| `tutoring-sisters-monday-cheatsheet.md` + `.txt` | S1 cheat sheet, .txt is older spelling variant | superseded pair, names (S1) | DELETE-CANDIDATE (.txt) / ARCHIVE (.md) | .txt = same content minus frontmatter, older name spelling; .md is the kept copy; both in git history |
| `tutoring-session3-cheatsheet.md`, `session4-cheatsheet.md`, `tutoring-lesson-cheatsheet-2026-08-25.md` | per-session sheets | done | ARCHIVE | chapter closed; lessons extracted into salvage |
| `tutoring-session7.md`, `-quest.md`, `-verdicts.md`, `-handoff.md`, `-cheatsheet.md` | S7 prep (S7 cancelled 09-07) | stale, statuses todo/active | ARCHIVE (status: done or archived) | session never ran; open statuses pollute Bases |
| `tutoring-word-world-memo.md` | Word World memo | closed | ARCHIVE | template now in tutoring-kit |
| `tutoring-game-3d-*` (11 files) | Word World briefs, checkpoints, digests, playtest | closed; 6 still in-progress/todo | ARCHIVE (move into `projects/tutoring-salvage/word-world/`, status archived) | refs `~/game3d/` laptop paths (dead; source deleted in D6) |
| `tutoring-game-pedagogy-research.md` + `-digests.md` | pedagogy research | reference | MOVE to `projects/tutoring-salvage/` | reusable for next student |
| `tutoring-game-lab.html` (107 KB) | Game Lab master | superseded by `D:\work\tutoring-kit\games\game-lab-template.html` (placeholder config) | ARCHIVE | check: vault master may still carry K/D config; kit copy is the clean one |
| `tutoring-game-copies.py` | per-girl copy script | dead (`/home/jep/...` paths) | DELETE-CANDIDATE | superseded by `D:\work\tutoring-kit\tools\make_send_copies.py`; in git history |
| `tutoring-bakeoff/` README, VERDICT, 2 py | Heblish ASR bake-off | done (verdict reached) | ARCHIVE (status done) | README points at `~/tutoring-data` laptop paths |
| `tutoring-bakeoff/results*/` (30 md, 209 KB, no frontmatter) | ASR outputs of scripted test clips (07-16, adult speakers) | done | ARCHIVE | not student data; 10 run folders x 3, only VERDICT matters |
| `tutoring-bakeoff/lesson-transcripts/*.DISTILLED.md` (5) | S1, S2, S3, S4, S6 records, initials-only | live history | MOVE to `projects/tutoring-salvage/records/` | folder name says "transcripts", content is distillations; S5 distilled only in digest 08-30 |
| `tutoring-bakeoff/lesson-transcripts/LOG.txt` | PowerShell run log | disposable | DELETE-CANDIDATE | tracebacks + warnings only; no content beyond filenames |
| `tutoring-bakeoff/__pycache__/` (2 pyc) | bytecode | tracked cache (S8) | DELETE-CANDIDATE | regenerable |
| `tutoring-heblish-test-scripts.md` | bake-off clip scripts | done | ARCHIVE | bake-off closed |
| `tutoring-a***-first-session.md` | lead, paused, no author field | stale lead, name in title (S3) | ASK-IDI | missing `author`; keep as lead or archive? |
| `tutoring-cousin-son-9.md`, `o**-parent-brief.html` | lead, status active | lead (S3) | ASK-IDI | next-student candidate? names a minor |
| `tutoring-former-neighbor-3kids.md` | adult lead | status active, last touched 07 | ASK-IDI | still a lead? |
| `sisters-first-contact-sim.html`, `uab-first-contact-sim.html`, `emergent-system.html` | July first-contact sims / system page | closed, names (S1) | ARCHIVE | emergent-system also refs `vault-agent/` dead alias |

## projects/ - XCOM (118 MB on disk, ~10 MB tracked)

| path | what | state | action | reason |
|---|---|---|---|---|
| `XCOM/Launch.log` (30.1 MB) | copied game launch log 09-27 | ignored, disposable | DELETE-CANDIDATE | game rewrites it each launch in Documents\my games; not in git |
| `XCOM/XCOM2 AML 1.6.0-beta/AML.log` (6.3 MB) | launcher log 08-31 | ignored, stale | DELETE-CANDIDATE | live launcher at `C:\XCOM2 AML 1.6.0-beta\` |
| `XCOM/XCOM2 AML 1.6.0-beta/settings.json` (3.8 MB, tracked) | AML settings snapshot 09-11 | stale | DELETE-CANDIDATE | live copy `C:\XCOM2 AML 1.6.0-beta\settings.json` 3.85 MB dated 10-03 (verified); git history keeps the 09-11 state |
| `XCOM/fixes/settings.json.STALE-2026-09-11-do-not-restore` (3.8 MB, tracked) | pre-fix snapshot | superseded by its own name | DELETE-CANDIDATE | name forbids restore; git history holds it |
| `XCOM/fixes/XComEngine.ini.STALE-...` + `.bak-2026-09-12` (155 KB) | ini snapshots | superseded | DELETE-CANDIDATE | black-screen fix closed 09-12; in history |
| `XCOM/fixes/XComBattleChatter.ini.bak-...-1053` / `-1054` | identical backups (md5 e98175b0) | duplicate | DELETE-CANDIDATE (`-1053`) | `-1054` identical |
| `XCOM/fixes/jepFixes.STALE-2026-09-11-snapshot/` | old jepFixes | superseded | DELETE-CANDIDATE | `.XComMod` and `XComContent.ini` md5-identical to `XCOM/jepFixes/`; README identical to `jepFixes/README-2026-09-11.md` |
| `XCOM/jepFixes/README-2026-09-11.md` | old README | superseded by `README.md` (09-28) | DELETE-CANDIDATE | identical to STALE README; keep one copy at most |
| `XCOM/fixes/XComBattleChatter.ini`, `XComRustyCounter.ini` | applied fixes | live | KEEP | |
| `XCOM/screenshots/1-9.png` (71.7 MB) | 4K in-game shots 09-18, unnamed | ignored, unreferenced by name | ASK-IDI | likely playtest input for `playtest-fixes-2026-09-17.md`; not backed up anywhere (gitignored) |
| `XCOM/Character Pool/` (5.7 MB bin + Path.txt) | copy of Idi's soldier pool 08-31 | ignored backup, stale vs live pool | ASK-IDI | only value is as a backup; git does not back it up; Path.txt points at `C:\Users\Idan\...` |
| `XCOM/XCOM VAULT/`, `XCOM/specs/` | Idi's own campaign notes, name mods, naming rules | Idi-authored (commit d80dce6 "Idi's Obsidian edits") | KEEP | no frontmatter, his files; folder names with spaces are his |
| `XCOM/jepFixes/`, `jepGTSFilter/`, `jepNoCoverGrabs/`, `jepReusePCS/`, `amalgamation-tools/` | jep mod sources | live (09-26 to 09-28) | KEEP | build scripts are .sh in Git Bash; fine |
| `XCOM/amalgamation-exclusions-A.ini` / `-B.ini` | exclusion variants 09-16 | superseded by `jepFixes/Config/XComAmalgamation.ini` (09-28)? | ASK-IDI | unclear which variant shipped; check against amalgamation-curation-2026-09-16.md |
| `XCOM/mod-config-inventory.md` (257 KB) | mod config dump | reference 09-15 | KEEP | large but text; regenerable |
| `XCOM/*.md` reports (20) | crash, sitrep, playtest, research | live history | KEEP | dated names consistent; `xcom-` prefix on 6 files redundant inside `XCOM/` (RENAME optional) |
| `XCOM/xcom2-keep-crash-dumps*.reg` | dump switch | live (machine .reg applied 09-20) | KEEP | |

## projects/ - decadents (25 MB)

| path | what | state | action | reason |
|---|---|---|---|---|
| `decadents/d1-contact-sheet.html`, `d1-2020s-contact-sheet.html`, `-2`, `-3` (4.2 MB, tracked) | early selection rounds | superseded (D1 closed 09-14, picks recorded in quest) | DELETE-CANDIDATE | picks + seeds in `decadents-d1-quest-2026-09-10.md` (status done); git history keeps them |
| `decadents/d1-2020s-contact-sheet-4.html` (2 MB) | final 2020s round | done | ARCHIVE | holds his pick 4 |
| `decadents/d1-nine-decades-contact-sheet.html` (9.4 MB) | nine-decade round 1, ruled 09-14 | superseded by round 2? | ASK-IDI | rulings live in quest file; is round 1 still consulted? |
| `decadents/d1-nine-decades-round2.html` (4.4 MB) | round 2, awaiting eight numbers | live, pending since 09-14 | KEEP | Today.md d3 |
| `decadents/renders/` (4 PNG, 5.7 MB) | chosen D1 renders | live receipts | KEEP | |
| `decadents/DECADEnts 1.md` / `DECADEnts 2.md` | Dec-2025 docs, md5-identical (3eb05864) | duplicate, no frontmatter, Idi-era | DELETE-CANDIDATE (`DECADEnts 2.md`) | proof: identical content in `DECADEnts 1.md`; Idi's file, his word needed |
| `decadents/DECADEnts.md`, `DECADEnts 3.md`, `2025-12-30-*.md` (3) | Dec-2025 origin docs (Idiverse import) | reference; `type="idea"`, `status="#child"` off-enum | KEEP | 3 broken `[[profile-preferences]]` (target only in laptop-archive Nexus `vault/tags/`) |
| `decadents/decadents-bible.md`, `render.py`, `z-image-turbo.template.json` | bible + render tooling | live | KEEP | |
| `decadents-d1-quest-2026-09-10.md`, `decadents-d1-nine-decades-2026-09-14.md` | quests at projects root | live/done | MOVE to `projects/decadents/` | same project, two folders |

## projects/ - Cash

| path | what | state | action | reason |
|---|---|---|---|---|
| `Cash/companies/*.md` (24), `Idi.md`, `Mom.md`, `Money.md`, `Cash Hub.md` | Bases row notes, refreshed daily | live | KEEP | missing `type/created/author`; `status: bench` (6) breaks the closed enum (S7 churn) |
| `Cash/allocation.md` | locked allocation 07-24 | live reference | KEEP | no frontmatter |
| `Cash/transactions/*` | ledger rows | live | KEEP | `_template.md` fine |
| `Cash/console-v2/v3/v4-*.md` | build reports | done | KEEP | version chain; reports are history |
| `Cash/dashboard/Cash-Console.html` + `console_template.html` + py | live console | live, regenerated daily | KEEP | consider moving generated html/market.json out of git (S7) |
| `Cash/dashboard/Cash-Idi.html`, `Cash-Mom.html` | v1 per-person dashboards (09-11) | superseded by Console v2+ | ASK-IDI | still opened? |
| `Cash/dashboard/ledger_2026-09-10.py`, `recut.py` | one-off scripts | done | ARCHIVE | executed 09-10/11 |
| `Cash/dashboard/data/polymarket-watch.json` | watched markets | stale entries (`fed-decision-in-september` fails in refresh.log) | KEEP (prune expired markets) | |
| `Cash/proposal-sndk-2026-09-09.md` | SNDK proposal, waiting | deferred | KEEP | |

## projects/ - HQ, migration, other

| path | what | state | action | reason |
|---|---|---|---|---|
| `pc-hq-stack.md` | PC stack reference | live, s3/s4/s6 false (S5) | KEEP (fix s6: secrets never reached GitHub; repoint CORPUS paths to `D:\work\laptop-archive\`) | |
| `pc-base-migration.md` | migration P0-P3 | flip done 09-26, status still active | ARCHIVE (status done) | broken `[[ADR-005-portability-tiers]]` |
| `pi-hq-bootstrap.md` | Pi bootstrap | archived | KEEP | already status archived |
| `pc-hq-collaboration-environment.md` | 09-02 environment plan | superseded by flip; laptop/Telegram strands dead | ARCHIVE | |
| `pc-hq-cheatsheet.md`, `pc-hq-external-tools-2026-09-07.md` | HQ references | live | KEEP | |
| `sitrep-2026-09-03.md` | sitrep | stale snapshot | ARCHIVE | |
| `emissary-maintenance.md` | routing lens, <=15 min ratio | live doc, false LIVE claims (S5) | KEEP (rewrite status table) | |
| `laptop-retirement/` (7 md) | retirement maps, runbooks | active until wipe check (due 09-28) | ASK-IDI | wipe done? then ARCHIVE all 7 |
| `pc-bios/findings-*.md` (3) | photo-reconstruction findings | reference | KEEP | missing frontmatter (agent output) |
| `pc-instability-incident-2026-09-21.md`, `pc-bios/bios-fix-...md` | incident + fix | active | KEEP | |
| `Curtains/installed-apps-2026-09-21.md` | app inventory | live | KEEP | |
| `I4/` (5 md) | I4 research + rewatch quest | live | KEEP | |
| `constraints-single-multi-player.md` | thinking session | live | KEEP | |
| `daily-note-system-2026-09-13.md` + `daily-note-research/` (4) | system + sources | live | KEEP | |
| `phone-capture-sync-quest-2026-09-13.md` | quest, status active | done per memory 09-13 | ARCHIVE (status done) | |
| `identity-refresh-2026-09.md` | 61 T-items for telos | active until Idi pastes | KEEP | |
| `intent.md`, `intent-log.md` | intent layer | live | KEEP | Whiteboard reference stale (S5); Idi's word to edit |
| `parts-registry.md`, `projects/wins-jar.md` | registry + jar | live | KEEP | |
| `kidstudio/` (11 files) | Kid Studio snapshot 09-07 | stale: `index.html`, `server.py` differ from live `D:\work\studio\kidstudio\` (README identical) | ARCHIVE | live app outside vault; snapshot misleads an agent reader |
| `kidstudio-*-2026-09-0x.md` (4) | research/brief/build reports | done | KEEP | name/date convention good |

## Infrastructure folders

| path | what | state | action | reason |
|---|---|---|---|---|
| `.vault-config/PERMISSIONS.md` | permission doctrine | live intent, laptop mechanics | KEEP | 13 laptop refs; doctrine still valid |
| `.vault-config/write-deny.list` | laptop deny list | dead (S4) | ARCHIVE | PC guard lives in `C:\Users\jep\.claude\hooks\vault-write-guard.py` |
| `.vault-config/scripts/*.sh` (4) | laptop autocommit/tag/health/restic | superseded by `C:\Users\jep\hq\*.sh` | ARCHIVE | backup-health uses systemctl; restic never ran |
| `.vault-config/prompts/*.md` (3) | cron prompts, Telegram | dead | ARCHIVE | evening retired 08-16, laptop gone |
| `.vault-config/hooks/capture_hook.py` + install md | Telegram capture hook | not wired on PC | ARCHIVE | phone capture now GitSync -> `D:\work\captures` |
| `.vault-config/tests/` (py + 2 tracked pyc) | laptop contract tests | dead (`/workspace`, `~/vault`) | ARCHIVE; DELETE-CANDIDATE for `__pycache__` | |
| `.vault-config/audit/*.jsonl` | write-guard audit trail; `edits-pc-2026-09.jsonl` 1.37 MB | live, tracked | KEEP | logs full command text to GitHub; secret-pattern scan found only search patterns, no values |
| `.obsidian/` | config, Templater only | live | KEEP | S10: daily-notes template vs Templater trigger off |
| `bases/` (4 .base) | dashboards | live | KEEP | `projects.base` filters `type == "project"`: only 20 of ~100 project files match (types report/note/reference/quest dominate) |
| `templates/daily-note.tpl.md` | Templater daily template, author Idi | stale vs daily/Today.md scheme | KEEP | Idi's template |
| `atomic-notes/The Telescope Metaphore.md` | the only atomic note | Idi's | KEEP | "Metaphore" spelling is his call |

## telos/ (inventory only, read-only)

- 41 files: `TELOS.md` + core (6 incl. `pillars.md`), identity (5), body (3), mind (3), people (3), resources (3), system (4), work (2 + projects/ 3), `state/current.md`, history/ (3 jsonl, Jan 2026), signals/ (2 jsonl), upgrades/ (3 json caches, Jan tooling).
- Not in the TELOS.md index: `core/pillars.md`, `state/current.md`, `history/`, `signals/`, `upgrades/`, `work/projects/abandoned.md`. Two telos project files were deleted by Idi on 09-26 (investment-research-system, voice-input-stt).
- No frontmatter except `pillars.md` (no author). TELOS index link `work/projects/` causes S10.

## Questions for Idi

1. K and D first names sit in 16 tracked files and on GitHub. Redact to initials in the vault files (jep can do daily/projects/inbox), and decide whether a history purge is wanted. Recommendation: redact now, no purge.
2. Install the name guard on the PC now (kit hook exists), or wait for the next student? Recommendation: now.
3. Leads by first name (the 9-year-olds in `tutoring-a***-first-session.md`, `tutoring-cousin-son-9.md`, `o**-parent-brief.html`): initials too?
4. `Idi's Whiteboard.md` is empty since 09-26. Retire it in favour of `daily/Today.md`, or keep as the Dump valve?
5. `XCOM/screenshots/` 72 MB: keep, move outside the vault, or delete?
6. `decadents/d1-nine-decades-contact-sheet.html` (round 1, 9.4 MB): still needed next to round 2?
7. Laptop wiped (step 7, due 09-28)? Then `laptop-retirement/` archives.
8. Vault `CLAUDE.md` needs a PC rewrite (enforcement, cron, Telegram, paths). Go?
9. Move `IMDb_EDA.ipynb` and `inbox/SELF-MAX/` into `resources/`?

## Totals

Files reviewed: 527 (incl. 41 telos inventoried). Reclaimable working tree: ~48.5 MB definite DELETE-CANDIDATEs (Launch.log 30.1, AML.log 6.3, two AML settings copies 7.6, superseded contact sheets 4.2, pyc/baks/dups ~0.3), up to ~135 MB with ASK items (screenshots 71.7, nine-decades round 1 9.4, Character Pool 5.7). Git pack (54 MB) shrinks only with a history rewrite; ~37 MB of the definite set is gitignored and was never in git.
