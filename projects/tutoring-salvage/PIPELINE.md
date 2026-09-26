---
type: reference
created: 2026-09-25
author: jep
---
# Tutoring data pipeline: how it ran, what broke, what to keep

Distilled from the 2026-08 laptop README + tools. Student-free. For future, unknown students.

## Shape
- Two places, never mixed: **landing zone** (private dir, mode 700, outside git/sync/backup) holds raw; **vault** (git-backed notes) holds initials-only distillations.
- Raw = recordings, `.LESSON.md` transcripts (from the local Whisper box), board photos, per-student game copies, send copies, name blocklist.
- Vault = lesson records by initials, game masters, research, cheat sheets.

## Flow
1. **Drop**: teacher drops every raw file from a lesson into `<zone>/drop/`.
2. **Verify**: `process_tutoring.py verify` proves isolation before touching anything: zone is a real dir (no symlink), mode 700, resolves outside the vault, no `.git` above it, no Syncthing folder covers it, restic inactive, vault `core.hooksPath` points at the guard, vault `.gitignore` blocks media + `*.LESSON.md`, blocklist present and outside the vault, vault tracks zero media. Any FAIL = stop.
3. **Organize**: `organize --dry-run` then `organize --label <initials>`: moves drop files into `sessions/<date>-<label>/` (date from file mtime unless `--date`), dirs 700, files 600.
4. **Distill**: the agent reads the session folder and writes initials-only lesson records into the vault (what was taught, what landed, next frontier words, game verdicts). No quotes that carry names, no media.
5. **Game copies**: master game lives in the vault; a copies script refreshes each student's copy in the zone with the new engine while PRESERVING that student's config block (GAME/MORE) and title. Embedded seeds only for first run.
6. **Send copies**: `make_send_copies.py` stamps name-titled copies with `password: "off"` into `<zone>/send/` for WhatsApp to the parent. Roster file maps initial to send name.
7. **Name guard**: vault pre-commit refuses R1 media, R2 transcripts, R3 camera/WhatsApp filenames, R4 files over 25 MB, R5 blocklisted names in any staged path + in content of session-record dirs and new inbox files. Refusal also blocks the 30-min autocommit, by design: the vault stops committing before it leaks. Marker `_COMMIT-BLOCKED.md` at vault root, gitignored.
8. **Delete**: raw deletion is the teacher's call, triggered by his use being finished, never by elapsed time. `status` lists what raw is still sitting in the zone.

## What broke (and the fix that stuck)
- **Symlink alias leak, 2026-04 to 08**: an alias path pointed into the vault; raw audio, photos, transcripts committed and pushed. Fix: history purge (git-filter-repo), alias replaced by a plain tombstone FILE so old paths fail loudly; `verify` checks it (`TUTORING_TOMBSTONE`).
- **Name-titled send copies committed from `projects/`, 2026-08-20**: R5 extended from content to staged FILE PATHS everywhere.
- **Broken phone copies, 2026-08-20**: game HTML had no doctype/charset/viewport; emoji mojibake + fps collapse on every phone; copies already sent were broken. Fix in engine: UTF-8 + viewport metas, DPR cap 2, auto fx-off rescue. Keep: probe on a throttled phone profile before any send.
- **Path drift**: send-copy script read `<zone>/games/` while the 2D copies lived at `<zone>/`; it printed SKIP and exited 0. Generic version exits 1 on a missing copy; keep ONE games dir.
- **Two hand-synced hook copies** (`hooks/pre-commit` + `pre-commit-student-data.py`, identical): keep one canonical file.
- **Hook echoed the matched name** into the marker file inside the vault folder and to stderr. Generic version cites the blocklist line number only.
- **Master edits never reached the copies**: the copies script overwrites config wholesale from each student's file, so teacher tweaks to the master config do not propagate. Intended, but surprising; say so in the script header.
- **Blocklist coverage gap**: the Word World master carried two default player first names that the blocklist did not match (see games-tools-report). A blocklist only guards the spellings it lists: add every spelling, nickname, and script.
- **Backups**: GitHub pushes failed silently 08-18 to 08-29 (`|| true` in autocommit); restic never activated; Syncthing had zero peers. The zone was correctly outside all of them; the vault's real backup was git only.

## Keep for new students
- Landing zone + verify-before-process + initials-only vault: unchanged.
- Blocklist + send roster as files in the zone, never in the vault; one line per spelling.
- Config-block-per-student games: master engine in the vault, per-student config preserved on refresh (templates in `../games/`).
- Guard hook with R1..R5, marker cites line numbers, autocommit blocked on refusal.
- Deletion by the teacher's decision; `status` as the reminder.
- Consent: several students were minors; record only under the consent protocol, extract then delete.

## Config knobs (generic tools)
- `TUTORING_ZONE` (default `~/tutoring-data`), `TUTORING_VAULT` (`~/vault`), `TUTORING_ROSTER` (`<zone>/blocklist.txt`), `TUTORING_LABEL` (`S`), `TUTORING_TOMBSTONE` (empty = skip), `TUTORING_GAMES_DIR` (`<zone>/games`), `TUTORING_SEND_ROSTER` (`<zone>/send-roster.txt`), `TUTORING_SCAN_DIRS` (colon list).
