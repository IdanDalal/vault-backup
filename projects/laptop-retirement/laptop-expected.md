---
type: reference
created: 2026-09-25
author: jep
status: active
---

# Laptop expected inventory, pre-SSH checklist (2026-09-25)

Purpose: what the Ubuntu laptop SHOULD hold per vault docs + memory, so the live SSH inventory can tick each row. Read-only research; nothing on the laptop verified yet. Student initials only.

Status key (on-PC per docs): yes / no / partial / unknown. "Evidence" paths: vault-relative unless prefixed `mem/` (= `C:\Users\jep\.claude\projects\D--work-vault\memory\`).

## 0. Facts that change the plan

1. **Laptop activity on GitHub stops at 2026-09-12 09:30.** `origin/main` head = `1e8b4b5` (probed `git ls-remote` 09-25), last laptop autocommit, last digest `daily/digests/2026-09-12.md`. Since 08-31 only one autocommit per day (09:30, digest-only). Nothing reached GitHub for 13 days: laptop off, asleep, or push broken again. Check `uptime`, `journalctl --list-boots`, `~/.local/state/vault-agent/`, `.vault-config/logs/` first.
2. **PC local `main` is at `3feb087` (09-02)**, behind `origin/main` by 10 laptop autocommits (09-03 to 09-12 digests). Harmless, but digests 09-03..09-12 exist only on GitHub + laptop.
3. **PC has NO name-guard pre-commit hook**: `git config core.hooksPath` unset on the PC clone (probed 09-25). Laptop hook + `blocklist.txt` are the only student-name guard in existence.
4. **`/workspace` may be a Nexus-era path, possibly absent on the laptop.** Contract tests say "From the desktop, via SSH: ssh laptop" (`.vault-config/tests/test_second_brain.py:11-12`) with `WORKSPACE=/workspace` (`.vault-config/tests/conftest.py:9`), and the Nexus backup sits on THIS PC at `D:\KEEP\NEXUS BACKUP\` (`projects/decadents-d1-quest-2026-09-10.md:65`, jep gets Permission denied, reconfirmed 09-25). Memory claims laptop `/workspace/projects/Curtains/` (`mem/curtains-project.md:11`). Resolve on SSH: `ls -la /workspace`.
5. **`/home/idan` was renamed to `/home/jep`** before 2026-06-10 (`projects/emissary-maintenance.md:82`, crontab pointed at nonexistent `/home/idan/*`). Yet `backup-health.sh:18` and `test_second_brain.py:142` check `syncthing@idan`. Expect either no `/home/idan` or a separate `idan` login user; verify `getent passwd`.
6. **Retiring the laptop breaks the consent design.** Policy: tutoring raw data never comes to the PC (`CLAUDE.md` user file; `projects/pc-base-migration.md:52` "stays laptop, likely permanent"). Retirement forces a ruling from Idi: his delete pass, or a new consent-gated home off the PC.

## 1. Sovereign Nexus + /workspace projects

| item | expected laptop path | evidence (file:line) | on PC? | notes |
|---|---|---|---|---|
| Curtains (PC setup preservation, ~100 apps, wikilink docs) | `/workspace/projects/Curtains/` | `telos/work/projects/curtains.md:28`; `mem/curtains-project.md:11,15` | partial | PC has only the concept note + `projects/Curtains/installed-apps-2026-09-21.md` (87 apps). Real folder not in vault or GitHub. May also exist in `D:\KEEP\NEXUS BACKUP\projects\` (unreadable by jep). Top priority: Idi wants to reformat the PC |
| XCOM Nexus working files | `/workspace/projects/XCOM/` | `telos/work/projects/xcom.md:32`; `projects/sitrep-2026-09-03.md:49` | partial | "never ported". PC now has live install + `projects/XCOM/` (AML settings, XCOM VAULT, crash notes) rebuilt from the game. Old notes may hold outfit/soldier roster work |
| I4 "The Triple Inception Theory" video essay | unknown; likely `/workspace/projects/Idiverse/` or Nexus notes | `telos/TELOS.md:11,104`; `telos/core/missions.md:61`; `telos/work/projects/abandoned.md:12` | no | No vault project note, no path anywhere. Grep laptop + D:\KEEP for "Inception" |
| Idiverse (256-note Obsidian vault: values card, mini-essays, film reviews) | `/workspace/projects/Idiverse/` | `telos/identity/essence.md:13`; `telos/identity/history.md:12`; `projects/sitrep-2026-09-03.md:55` | partial | Copies on PC at `D:\KEEP\NEXUS BACKUP\projects\Idiverse\` and `D:\KEEP\Vaults BACKUPS\Idiverse\` (per `decadents-d1-quest-2026-09-10.md:65`), admin-only |
| investment-research-system | `/workspace/projects/investment-research-system/` | git HEAD `telos/work/projects/investment-research-system.md:40` | no | Superseded by `projects/Cash/` (`identity-refresh-2026-09.md:89`). Inventory only, do not pull |
| voice-input-stt | `/workspace/projects/voice-input-stt/` | git HEAD `telos/work/projects/voice-input-stt.md:28` | no | Discarded 09-08 (`identity-refresh-2026-09.md:93`). Inventory only |
| Bloody ConQuest, Cinema Degrees, DECADEnts sources, Espionage Inc, WittyWhims | Nexus / Idiverse tree | `telos/work/projects/abandoned.md:9-38`; `sitrep-2026-09-03.md:55` | partial | DECADEnts sources seen at `D:\KEEP\NEXUS BACKUP\projects\Idiverse\DECADEnts*.md`; rest unknown |
| Nexus v3 / Context Kernel / InterviewMachine / RiskGate handoffs (24 handoffs) | inside CORPUS or `/workspace` | `sitrep-2026-09-03.md:55`; `identity-refresh-2026-09.md:100` | no | Index file was in `telos/system/handoff-index.md` (deleted in PC working tree). Inventory only |
| Nexus repo: ADRs + deploy sources | `/workspace/data/decisions/`, `/workspace/data/deploy/vault-config/`, `/workspace/config/integration-manifest.yaml` | `.vault-config/tests/conftest.py:21-30`; `test_second_brain.py:179-192` | no | **ADR-002..005 files live here**, source of `claude-vault`, `claude-vault-helper`, sudoers, `vault-write-guard.sh`. ADR-005 is a broken wikilink in the vault (`sitrep-2026-09-03.md:19`) |
| ADR-005 portability tiers | `/workspace/data/decisions/ADR-005*` | `CLAUDE.md:171`; `projects/pc-base-migration.md:13,45-52` | partial | Only the tier table survives in `pc-base-migration.md:47-52` |
| CORPUS-June-2026 incl. NEXUS BACKUP (446 MB) | `~/vault/inbox/CORPUS-June-2026/` (+ `_CORPUS-MAP/`) | `.gitignore:7`; `projects/emissary-maintenance.md:82`; `projects/pc-hq-stack.md:37`; `mem/time-attention-system-project.md:138` | partial | Gitignored, never on GitHub; PC clone lacks it. Nexus copy may equal `D:\KEEP\NEXUS BACKUP\`. Diff before deciding |
| Nexus llama.cpp artifacts (build guide, `start-router.ps1`, `models.ini`, `deep_research.py`, longctx script, local-models analysis) | `~/vault/inbox/CORPUS-June-2026/NEXUS BACKUP/{docs,scripts,data}/...` | `projects/pc-hq-stack.md:39-43` | no | Summaries only on PC. Needed for the local model tier (llama-server `:8080` not yet installed) |
| **Cleartext secrets `.env`** (Slack bot/app tokens, 2 n8n JWT keys, SearXNG + WebUI secrets) | `~/vault/inbox/CORPUS-June-2026/NEXUS BACKUP/.env` | `projects/pc-hq-stack.md:73`; `mem/pc-hq-migration.md:15` | no | Never reached GitHub (verified 09-05). OPEN: Idi revokes Slack tokens, file leaves `~/vault`. Do NOT copy to PC. Check for sibling secret files |

## 2. Vault clone + backup machinery (laptop = writing authority)

| item | expected laptop path | evidence (file:line) | on PC? | notes |
|---|---|---|---|---|
| Vault working copy (main writer) | `/home/jep/vault` (`~/vault`) | `.vault-config/write-deny.list:11-23`; `mem/pc-hq-migration.md:21` | partial | PC clone `D:\work\vault`. Check laptop for **uncommitted/unpushed** work: `git status`, `git log origin/main..main` |
| Untracked/gitignored vault content | `~/vault/` (media, `*.LESSON.md`, `_COMMIT-BLOCKED.md`, `.obsidian/workspace*.json`, `.trash/`) | `mem/tutoring-data-pipeline.md:16`; `.gitignore:1-7` | no | `git status --ignored` on laptop. Any student media found = policy breach, stays off PC |
| `.vault-config/logs/` (agent-*.log) | `~/vault/.vault-config/logs/` | `mem/vault-scheduled-agents-live.md:34`; `daily/digests/2026-08-30-loop-review.md:50` | no | Runner logs; tells whether digests failed after 09-12 |
| Audit JSONL (laptop hook) | `~/vault/.vault-config/audit/edits-2026-09.jsonl`; also `~/.claude/vault-audit/` | `.vault-config/audit/` (Glob); `projects/*` mentions `~/.claude/vault-audit/edits-2026-09.jsonl` | partial | Committed copies on GitHub through 09-12 |
| `autocommit.sh` (L1, 30 min) | `~/vault/.vault-config/scripts/autocommit.sh` via crontab | `.vault-config/scripts/autocommit.sh:10`; `projects/pc-base-migration.md:42` | no | Push error swallowed `|| true` (`mem/vault-github-push-outage.md:13`). PC port planned as schtasks with LOUD failure (`pc-hq-collaboration-environment.md:33,69`) |
| `nightly-tag.sh` (L2 snapshot tags) | `~/vault/.vault-config/scripts/nightly-tag.sh` | `.vault-config/scripts/nightly-tag.sh:5-7` | no | Same swallowed push |
| `backup-health.sh` | `~/vault/.vault-config/scripts/backup-health.sh` | `.vault-config/scripts/backup-health.sh:1-28` | no | "Never passed (70/70)" (`pc-hq-collaboration-environment.md:40`) |
| `system-health.sh` | `~/vault/.vault-config/scripts/system-health.sh` | `test_second_brain.py:600-603` | no | Expected by tests, absent from PC clone: may not exist anywhere |
| restic L4 (binary, script, weekly cron Sun 02:47, env template) | `~/bin/restic`, `~/.config/restic/env.template`, `restic-backup.sh` | `inbox/standing-prompts-draft.md:42-44`; `CLAUDE.md:156` | no | Never activated; confirm `~/.config/restic/env` absent. Nothing to carry except the decision |
| Syncthing L3 (service, `.stignore`) | `syncthing@idan` systemd unit; `~/vault/.stignore` | `backup-health.sh:18`; `CLAUDE.md:155` | no | Zero peers. Note the `@idan` user mismatch (section 0.5) |
| Pre-purge safety bundle (OLD history containing student media) | `~/tutoring-data/vault-history-pre-purge-2026-08-18.bundle` | `mem/tutoring-data-pipeline.md:20` | no, must stay no | Contains raw student media. Idi's delete call. Never to PC |
| GitHub push key for vault | `~/.ssh/id_ed25519_github` + repo `core.sshCommand` | `mem/vault-github-push-outage.md:11,15` | no (PC uses own deploy key) | Revoke/remove from GitHub when laptop retires |
| Git remote / laptop `~/.gitconfig` identity ("Idi" author on autocommits) | `~/.gitconfig`, `~/vault/.git/config` | `git log origin/main --author=Idi` | n/a | Record hooksPath, sshCommand, upstream before shutdown |

## 3. Scheduled agents, cron, Telegram

| item | expected laptop path | evidence (file:line) | on PC? | notes |
|---|---|---|---|---|
| crontab (jep) | `crontab -l` | `inbox/standing-prompts-draft.md:34-36`; `mem/vault-scheduled-agents-live.md:13-16,24`; `projects/daily-note-research/env-vault.md:39` | no | Expected lines: autocommit */30, nightly-tag, backup-health, morning-digest `0 9`, evening-ping `0 21` (retired by order but spec possibly still present), loop-review `17 9 * * 0`, restic Sun 02:47. **Dump to file before shutdown** |
| `run-agent.sh` runner | `~/bin/run-agent.sh` | `inbox/standing-prompts-draft.md:32`; `projects/emissary-maintenance.md:83` | no | NOT in the repo (`pc-hq-collaboration-environment.md:40`). Copy source for the cron-port decision |
| Runner logs | `~/.local/state/vault-agent/` (cron-runner.log) | `projects/emissary-maintenance.md:84`; `daily/digests/2026-07-05.md:43` | no | Diagnose the 09-12 stop |
| Prompts (morning-digest, evening-ping, loop-review) | `~/vault/.vault-config/prompts/` | `.vault-config/prompts/*.md` (Glob) | yes | In git. Digest prompt sends Telegram (`prompts/morning-digest.md:1`) |
| `claude-vault` wrapper + root helper + sudoers (ADR-004 Layer 1) | `~/bin/claude-vault`, `/usr/local/bin/claude-vault-helper`, `/etc/sudoers.d/claude-vault`, `~/.bashrc:120` alias | `.vault-config/write-deny.list:26-32`; `mem/doctor-path-warning-false-positive.md:10-12` | no (by design) | Linux-only mechanism; PC has hook-only containment. Archive sources for reference |
| `vault-write` Unix group, `atomic-notes/` root:vault-write 2775 | laptop filesystem | `test_second_brain.py:238-248`; `CLAUDE.md:63` | no | Linux-only |
| Write-guard hook v1 | `~/.claude/hooks/vault-write-guard.sh` | `.vault-config/write-deny.list:35`; `CLAUDE.md:64` | yes (ported) | PC v2 = `C:\Users\jep\.claude\hooks\vault-write-guard.py` (`mem/pc-hq-migration.md:11`) |
| Telegram bot service | `kitchen-telegram.service` (systemd --user), env `~/.config/kitchen/env` (bot token, `KITCHEN_VAULT_PATH`) | `.vault-config/hooks/capture_hook-install.md:44-55`; `projects/pc-base-migration.md:51` | no | Single-instance; two copies collide (`mem/vault-scheduled-agents-live.md:29`). Holds a secret: do not scp blind |
| Claude Code Telegram channel plugin config | `~/.claude/channels/telegram/access.json` | `mem/time-attention-system-project.md:56`; `pc-hq-collaboration-environment.md:37` | no | Planned PC replacement = Claude Code Channels (Phase C, own decision doc, `pc-hq-collaboration-environment.md:74`) |
| Capture hook (UserPromptSubmit, ADR-007) | `~/vault/.vault-config/hooks/capture_hook.py` + `~/.claude/settings.json` entry | `.vault-config/hooks/capture_hook-install.md:23-40` | partial | Script in git; PC settings do not register it. Phone capture moved to GitSync `D:\work\captures` (`mem/daily-note-system-project.md:17`) |
| Linger / systemd user timers | `loginctl enable-linger jep`; any `~/.config/systemd/user/*` | `pc-hq-collaboration-environment.md:70` | no | Check `systemctl --user list-timers` and `list-units --type=service` |
| Sleep/lid config (24/7 box) | `/etc/systemd/logind.conf.d/no-suspend.conf`, masked sleep targets | `mem/vault-scheduled-agents-live.md:21-22` | n/a | Decommission only; no port |
| sshd hardening, fail2ban | `/etc/ssh/sshd_config`, fail2ban unit | `test_second_brain.py:605-613` | n/a | Relevant for today's SSH login (password auth may be off; key needed) |

## 4. Home dirs + dotfiles

| item | expected laptop path | evidence (file:line) | on PC? | notes |
|---|---|---|---|---|
| Home CLAUDE.md | `/home/jep/CLAUDE.md` | `projects/pc-hq-stack.md:64` | yes (adapted) | Holds the sandbox-rejected Bash construct list (`CLAUDE.md` vault, scheduled section). Diff for unported rules |
| Output style Idi | `~/.claude/output-styles/idi.md` | `projects/pc-hq-stack.md:62` | yes | Diff for drift after 08-30 |
| Claude memory dir (full student names inside) | `~/.claude/projects/-home-jep/memory/` | `projects/pc-hq-stack.md:63`; `projects/pc-base-migration.md:35` | partial | scp-only, never git. Diff laptop vs PC: laptop may hold entries written after P2.5 |
| Claude settings (hooks, deny rules, plugins) | `~/.claude/settings.json` | `test_second_brain.py:555-576`; `capture_hook-install.md:23` | partial | Layer-3 deny rules use `Write(...)`, never match (`pc-hq-collaboration-environment.md:40`) |
| Skill `process-tutoring` | `~/.claude/skills/process-tutoring/SKILL.md` | `.vault-config/audit/edits-2026-08.jsonl:156`; `CLAUDE.md:136` | no, must stay no | Tied to raw data; archive text only if Idi rules |
| Other laptop skills / scheduled-tasks / loop.md | `~/.claude/skills/`, `~/.claude/scheduled-tasks/`, `~/.claude/loop.md` | vault grep hits (`~/.claude/scheduled-tasks/`, `~/.claude/loop.md`) | unknown | List and diff vs PC `skills/` (daily-note, synced) |
| Claude session transcripts / jobs | `~/.claude/projects/-home-jep/*.jsonl`, `~/.claude/jobs/` | `mem/time-attention-system-project.md` (sessions referenced) | no | May contain student names; keep off PC unless ruled |
| Claude login for `claude-vault` (plan OAuth) | `~/.claude/.credentials.json` | `mem/vault-scheduled-agents-live.md:34` | n/a | Log out / revoke on retirement |
| Laptop render + probe rig (Playwright) | `~/render-tools/` (shoot.mjs, gauntlet3d.mjs, node_modules) | `projects/sitrep-2026-09-03.md:27`; `projects/tutoring-game-3d-session8-handoff.md:16`; `mem/game-lab-project.md:24` | no | PC uses headless Edge instead; scripts worth copying |
| Word World 3D master build | `~/game3d/` (`island.html`, `src/`, `tools/build.mjs`, `screenshots/`, `ref/mengto/`) | `projects/sitrep-2026-09-03.md:24,70`; `mem/tutoring-game-3d-project.md:11` | no | Code, no student data. Planned rsync after P2. Check screenshots for student-identifying content before copying |
| Design system doc | `~/DESIGN.md` | `mem/tutoring-project.md:25` | unknown | Referenced by tutoring HTML briefs |
| Podcast transcript file(s) in home | `/home/jep/Transcript of The Psychological Drivers of the Metacrisis...txt` | `mem/time-attention-system-project.md:75` | no | Source text, low priority |
| Tombstone | `~/vault-agent` (plain file) | `mem/tutoring-data-pipeline.md:17` | n/a | Expect a FILE; a directory there = regression |
| SSH keys + config | `~/.ssh/` (`id_ed25519_github`, laptop ed25519 used for PC login, no `config`) | `mem/vault-github-push-outage.md:11`; `projects/pc-base-migration.md:32` | partial | PC holds `laptop_ed25519` + `authorized_keys` (2 lines). Keys never travel; revoke on GitHub |
| Shell dotfiles | `~/.bashrc` (line 118 PATH, 120 alias), `~/.profile` | `mem/doctor-path-warning-false-positive.md:10-12` | n/a | Reference only |
| Obsidian on laptop (Templater only) | `~/vault/.obsidian/` | `pc-hq-collaboration-environment.md:40` | yes | `.obsidian/` in git |
| `/home/idan` | `/home/idan` | `projects/emissary-maintenance.md:82` | unknown | Expected absent after rename; if present, inventory fully (Syncthing config, Downloads, browser profiles) |
| Other `.env` / secret files | `~/.config/kitchen/env`, `~/.config/restic/`, NEXUS `.env`, any `*.env` in home | sections 1, 3 | no | `find ~ -name '*.env' -o -name '.env'` ; never scp secrets without a named destination |

## 5. Tutoring data (MUST NOT come to the PC)

Consent rules: raw audio, photos, transcripts live only in `~/tutoring-data/` (chmod 700), outside vault, git, every sync/backup layer. Raw deletion is Idi's, triggered by his use being finished, never by elapsed time. Vault gets initials-only distillations. Several students are minors. Sources: vault `CLAUDE.md:132-138`, `mem/tutoring-data-pipeline.md:14-18`, user CLAUDE.md "No raw tutoring data on this machine".

| item | expected laptop path | evidence (file:line) | on PC? | notes |
|---|---|---|---|---|
| Drop folder | `~/tutoring-data/drop/` | `mem/tutoring-data-pipeline.md:14` | no, must stay no | Inventory by count/size only, no content reads |
| Session raw (S1..S6 +, `YYYY-MM-DD-K-D/`, 07-16 Heblish clips) | `~/tutoring-data/sessions/` | `mem/tutoring-data-pipeline.md:14`; vault grep `sessions/2026-08-10-K-D/` .. `2026-08-20-K-D/` | no, must stay no | Idi's delete pass pending |
| Per-girl live game copies (single copy, no backup) | `~/tutoring-data/games/` (word-world-K/D, game-lab copies) | `mem/tutoring-data-pipeline.md:18`; `mem/game-lab-project.md:13` | no | Contain per-student config blocks; only copy anywhere. Idi rules: rebuild from master or keep |
| Send copies (name-titled) | `~/tutoring-data/send/` | `mem/tutoring-data-pipeline.md:18` | no, must stay no | Filenames contain first names |
| Tools: `process_tutoring.py`, `make_send_copies.py` | `~/tutoring-data/tools/` | `mem/tutoring-data-pipeline.md:14`; `mem/game-lab-project.md:13` | no | Code only; portable if the pipeline gets a new home |
| Pre-commit hook (name/media guard) | `~/tutoring-data/tools/hooks/pre-commit` | `projects/pc-base-migration.md:41`; `pc-hq-collaboration-environment.md:32,68` | no | **P3 blocker.** PC `core.hooksPath` unset. Hook code has no names, safe to copy |
| `blocklist.txt` (student full names, chmod 600) | `~/tutoring-data/blocklist.txt` | `projects/pc-base-migration.md:41`; `mem/tutoring-data-pipeline.md:14` | no | Plans conflict: P3 says USB or retype, Phase B names `C:\Users\jep\tutoring-data\blocklist.txt` with icacls. Needs Idi's ruling given "no raw tutoring data" rule (names are not raw media) |
| Pre-purge history bundle | `~/tutoring-data/vault-history-pre-purge-2026-08-18.bundle` | `mem/tutoring-data-pipeline.md:20` | no, must stay no | See section 2 |

## 6. Pending migration items (per plan) that the laptop gates

| item | evidence (file:line) | status | laptop dependency |
|---|---|---|---|
| P2.5 collaboration layer scp | `projects/pc-base-migration.md:35` | done (memory, style, CLAUDE.md on PC) | diff for post-08-30 laptop memory |
| P3 write flip / main flip | `projects/pc-base-migration.md:38-43`; `mem/pc-hq-migration.md:13` | pending (PC pushes branches only; main = laptop autocommit) | laptop autocommit must stop the moment PC owns main |
| Pre-commit hook + blocklist port | `projects/pc-base-migration.md:41` | pending | source lives only on laptop |
| Cron port (digests, loop review) | `projects/pc-base-migration.md:50`; `pc-hq-collaboration-environment.md:74` | pending, "own decision doc" | runner + prompts + login on laptop |
| Telegram port (Claude Code Channels) | `projects/pc-base-migration.md:51`; `pc-hq-collaboration-environment.md:37,74` | pending | single-instance: stop laptop bot before PC bot starts |
| Autocommit + nightly-tag as PC schtasks, loud push failure | `pc-hq-collaboration-environment.md:33,69` | pending | laptop copies must go OFF first (two writers) |
| Laptop pull-mirror timer | `pc-hq-collaboration-environment.md:70` | moot if laptop retires | n/a |
| Local model tier (llama-server router) | `projects/pc-hq-stack.md:37-45` | not installed | Nexus scripts in CORPUS on laptop |
| `.env` secret revocation | `mem/pc-hq-migration.md:15` | open | file on laptop |
| Word World rsync | `projects/sitrep-2026-09-03.md:70` | pending | `~/game3d/` |
| Tutoring pipeline new home | `projects/pc-base-migration.md:52` | "stays laptop, likely permanent" | retirement forces a ruling |
| Laptop-side GitHub key revoke | `mem/vault-github-push-outage.md:15` | not planned yet | `id_ed25519_github` |

## 7. What breaks when the laptop is switched off

1. **Vault main write authority**: 30-min autocommit + push to `origin/main` (L1). Already silent on GitHub since 09-12 09:30.
2. **Nightly snapshot tags** (L2) and `backup-health.sh`.
3. **Morning digest** 09:00 → `daily/digests/` + Telegram (last 09-12). Idi called it unread and replaced it with `daily/Today.md` on 09-13 (`mem/daily-note-system-project.md:9`), so the loss is small, but the cron should be retired on purpose.
4. **Sunday loop review** 09:17 → digest + Telegram.
5. **Telegram bot** (`kitchen-telegram` / channels plugin) and the ADR-007 capture path; phone captures now also flow via GitSync to `D:\work\captures`.
6. **Student-name pre-commit guard**: exists only on the laptop; PC commits run unguarded.
7. **Tutoring pipeline** (`process-tutoring`, drop folder, per-girl game copies): no other home, by design.
8. Not affected: restic (never ran), Syncthing (no peers), evening ping (retired 08-16).
