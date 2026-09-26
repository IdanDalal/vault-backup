---
type: project
created: 2026-09-26
author: jep
status: active
---

# HQ takeover runbook (handover steps 2-4)

For the interactive hq session (jep in `D:\work\vault`, not a worktree). Idi's trigger: "run the takeover runbook". Ruled by Idi 2026-09-26 (defaults: retire digest, loop review, Telegram). Plan: [[handover-plan-2026-09-26]].

Already done 2026-09-26 by the background job:
- Laptop frozen: 0 active cron lines (backup `~/crontab-backup-2026-09-26.txt` on the laptop), `kitchen-telegram` stopped + disabled, laptop vault clean at `6d13b13`, 0 unpushed.
- Secrets: Slack app deleted (Idi), `D:\KEEP\NEXUS BACKUP\.env` deleted (Idi), laptop kitchen `.env` deleted (jep).
- Scripts in `C:\Users\jep\hq\`: `vault-autocommit.sh`, `vault-nightly-tag.sh`, `register-vault-tasks.ps1`. Dry-run passed on a throwaway repo: commit + push, push failure writes `_PUSH-FAILED.md`, recovery removes it, flag never enters history, tag pushed once.

## Steps

| # | action | done when |
|---|---|---|
| 1 | Add two lines to `.gitignore`: `.claude/` and `_PUSH-FAILED.md` | without `.claude/`, autocommit would sweep in worktrees + settings |
| 2 | `git fetch origin`; commit the whole working tree on local `main` as `PC takeover 2026-09-26: Idi's Obsidian edits + jep deliverables` (author jep) | `git status` clean |
| 3 | Merge `origin/main` (11 laptop commits, digests only since 09-02); on any conflict Idi's text wins | `git log origin/main..main` shows the takeover + merge |
| 4 | `git push origin main` | GitHub head = PC |
| 5 | `pwsh -File C:\Users\jep\hq\register-vault-tasks.ps1` | both tasks listed, State Ready |
| 6 | Wait for the first scheduled run (top of the next hour), check `C:\Users\jep\hq\logs\autocommit.log` shows `ok` | receipt line in `laptop-retirement-2026-09-25.md` |
| 7 | 48 h later: ≥ 90 `ok` lines, 2 tags, 0 laptop commits → tell Idi the laptop can be wiped (guide step 3 GitHub key, step 5 `nordvpn logout`) | handover closed |

If a scheduled run is missing after a reboot: Idi opens Task Scheduler → "Vault autocommit" → Properties → "Run whether user is logged on or not" → types jep's password once.
