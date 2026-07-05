---
type: reference
created: 2026-06-10
author: jep
status: todo
---

# Standing prompts — durable wiring draft (for Idi's blessing)

The morning digest (09:03) and evening ping (21:53) are live via the harness scheduler, which renews weekly with the session. To make them permanent the governance-correct way, these two prompt files belong in `.vault-config/prompts/` — write-forbidden to agents by design, so the move is yours:

```bash
# after reviewing the two prompts below, save them as:
#   .vault-config/prompts/morning-digest.md
#   .vault-config/prompts/evening-ping.md
```

## Prompt 1 — morning-digest.md

> Gather today's orders: search the vault (projects/, areas/, inbox/, daily/) for notes with `due:` frontmatter — due today, overdue (status != done), next 3 days; plus projects with status: active. Read yesterday's daily note; if its Captures hold the evening numbers (sleep hrs / energy 1–5), copy them into that note's frontmatter `sleep` / `energy`. Flag up to 3 inbox items untouched >7 days (skip CORPUS-June-2026, SELF-MAX). Write the full digest to `daily/digests/YYYY-MM-DD.md` (type: digest, author: jep). Send a compact version (≤12 lines) to Telegram chat 6139758667. Write only inside daily/. Clinical tone. If anything is ambiguous, do nothing destructive and say so in the message.

## Prompt 2 — evening-ping.md

> Send one short Telegram message to chat 6139758667: "🌙 Evening ledger — three numbers: sleep last night (hrs — the watch knows), energy today (1–5), and one line: drift or win? Anything else: prefix with c: to capture." Then stop; replies are handled by the capture protocol (ADR-007).

## Prompt 3 — loop-review.md (Sunday 09:17, the weekly sitting prep)

> Assemble the week's feedback packet for Idi's 30-minute Sunday sitting (SELF-MAX zones 6–7): read the last 7 daily notes and digests. Compile: (1) ordered vs happened — due items completed or slipped; (2) signals — sleep/energy trend from frontmatter; (3) his own words — 3–5 captures from the week, quoted verbatim; (4) environment reactions — anything inbound (student-search news, replies, family); (5) open items — stale inbox, open switches. Close with the three zone-7 questions: What did the environment send back? What does it change? What are next week's orders? Write to `daily/digests/YYYY-MM-DD-loop-review.md` (type: digest, author: jep), compact version to Telegram chat 6139758667. Write only inside daily/. Clinical; prefer his words over summaries of his words.

## The runner — BUILT 2026-06-10 ✅

`~/bin/run-agent.sh` (next to `claude-vault`, same thin-wrapper trust argument). Tested end-to-end: fail-safe SKIP when no prompt exists; full chain verified (`sudo → helper → setpriv group-drop → headless claude` answered correctly). Cron lines are **already live and skipping silently**:

- `3 9 * * *` → `run-agent.sh morning-digest`
- `53 21 * * *` → `run-agent.sh evening-ping`
- `17 9 * * 0` → `run-agent.sh loop-review`

**So "saving the prompts" is now literally the whole remaining act:** create the three files above in `.vault-config/prompts/` (named `morning-digest.md`, `evening-ping.md`, `loop-review.md`) and the durable system takes over from the next scheduled tick. Tell jep when you've done it so the interim harness jobs get deleted (otherwise you'll receive everything twice).

## Restic (L4 offsite) — binary installed, credentials are yours

- `restic 0.19.0` installed at `~/bin/restic` (static binary, no root). It had never been installed — L4 has never run on this machine.
- Weekly cron line live: Sunday 02:47, **self-gated** — it does nothing until `~/.config/restic/env` exists.
- Your move (5 min): fill in `~/.config/restic/env.template` → save as `env`, `chmod 600`, run `restic init` once. First backup fires the following Sunday (or run `restic-backup.sh` by hand to not wait).
