---
type: project
created: 2026-08-29
author: jep
status: active
---

# PC Base Migration - Laptop to Windows HQ

> [!warning] Pivot 2026-08-30
> Pi is out as the Claude agent: since 2026-04-04 third-party harnesses bill Claude subscriptions per-token as extra usage, server-enforced. The resident agent is now **Claude Code native on Windows** (plan-billed). Architecture, billing rules, and local-model stack: [[pc-hq-stack]]. [[pi-hq-bootstrap]] is archived; the collaboration layer now ports as files (see the port table in [[pc-hq-stack]] §4). P1 below is rewritten accordingly; Pi may remain installed only as a harness for local models, never signed into the Anthropic account.

Goal: the Windows 11 PC becomes the always-on HQ running Claude Code as resident agent; the laptop becomes an on-demand client. Governing rule: [[ADR-005-portability-tiers]] - pull on demand, never bulk. Nexus guard: nothing lands on the PC without a named destination and a live task pulling it. `D:\work` staying exactly `vault\` + studio outputs is the health metric; unsorted folders appearing there means this migration is failing.

## P0 - Laptop side (done 2026-08-29)

- [x] This checklist + [[pi-hq-bootstrap]] written to `projects/`
- [x] Pushed to GitHub (`IdanDalal/vault-backup`) - git is the delivery truck; no USB piles, no copy dumps

## P1 - Corpus onto the PC (as jep, ~20 min)

1. **Token** (on any browser, Idan's GitHub account): Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token. Name `pc-vault-ro`, expiration 90 days, Repository access: *Only select repositories* → `vault-backup`, Repository permissions → Contents: **Read-only**. Generate, copy once.
   - Read-only on purpose. The PC physically cannot push until P3, so single-writer is enforced by the credential rather than by discipline.
2. **Clone** (PC, signed in as `jep`, Git Bash): `cd /d/work` then `git clone https://github.com/IdanDalal/vault-backup.git vault`. Username `IdanDalal`, password = the token. Windows stores it after first use.
3. **Claude Code** (as `jep`, no admin needed): `winget install Anthropic.ClaudeCode`, plus Git for Windows if C1 didn't install it (gives Claude Code a real Bash tool). Launch `claude` inside `D:\work\vault`, sign in with the Claude account. Billing guards: in claude.ai settings keep extra usage / usage credits OFF; verify no `ANTHROPIC_API_KEY` exists (`echo %ANTHROPIC_API_KEY%` must print nothing).
4. **Verify**: in that session ask: *"List the live projects and this machine's write rules."* Correct answer = tutoring (K & D, initials only) / TELOS+IFS / Cash / studio, clone is read-only. `vault/CLAUDE.md` loads automatically; full collaboration context (memory, output style) arrives in P2.5.

## P2 - Remote access (laptop → PC, LAN first)

1. PC: Settings → System → Optional features → add **OpenSSH Server**. Services → OpenSSH SSH Server → Startup: Automatic → Start. (Needs admin, so done from Idan's account.)
2. `jep` is a Standard user, so keys go in plain `C:\Users\jep\.ssh\authorized_keys` (the `administrators_authorized_keys` quirk applies only to admin accounts).
3. Laptop: `ssh-keygen -t ed25519` if needed, append the `.pub` line to that file, test `ssh jep@<PC-LAN-IP>`.
4. After key login works: `PasswordAuthentication no` in `C:\ProgramData\ssh\sshd_config`, restart the service (admin again).
5. PC power: never sleep on AC; wired Ethernet preferred.
6. **P2.5 - collaboration layer** (added 2026-08-30, right after SSH works): from the laptop, `scp` the Idi output style, the adapted home CLAUDE.md, and the Claude Code memory directory to the PC per the port table in [[pc-hq-stack]] §4. Memory files travel by scp ONLY, never git: they contain full student names.
7. Access from outside home: separate later decision. WireGuard = self-hosted, no account; Tailscale = easier, requires signup (conflicts with the no-signup rule). LAN-only until decided.

## P3 - Write flip (per strand, each deliberate)

1. New fine-grained token, Contents: **Read and write**; replace the stored credential.
2. Port the pre-commit hook from laptop `~/tutoring-data/tools/hooks/` (runs under Git Bash). `blocklist.txt` never touches GitHub: carry by USB or retype. Until it exists on the PC the student-name check is dead; media/size checks still fire.
3. Single-writer per strand: one machine owns writes to a given project; pull before write. Laptop 30-min autocommit stays ON until the final strand flips.
4. Verify: a test commit from the PC appears on GitHub, and a bait commit containing a blocked name is refused by the hook.

## P4 - Tier 4 infrastructure (does not travel by default)

| Element | Verdict today |
|---|---|
| Cron digests / ping / loop-review | Stays laptop; any port needs its own decision doc |
| Telegram bot | Stays laptop; single-instance, two copies collide |
| Tutoring raw data + pipeline | Stays laptop, likely permanent: consent isolation (chmod 700 + hooks) is OS-level and absent on Windows |
| ComfyUI studio | Already PC-native per the Studio Preflight plan |

## Risks

1. Two writers → merge conflicts: prevented by the read-only token until P3.
2. PC pushing without the name-guard hook: prevented the same way; hook ports before the flip.
3. Always-on exposure: key-only SSH, LAN-only, Standard user = contained blast radius.
4. Nexus repeat: watch the `D:\work` health metric above, monthly.
