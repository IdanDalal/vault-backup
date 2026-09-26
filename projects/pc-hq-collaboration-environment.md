---
type: project
created: 2026-09-02
author: jep
status: active
---

# PC HQ Collaboration Environment - research synthesis + plan, 2026-09-02

First PC session. Four research agents (Claude Code docs audit, Windows terminal/persistence, laptop-as-mirror/remote access, vault excavation). Builds on [[pc-hq-stack]] and [[pc-base-migration]]. Nothing below is built yet.

## 1. Ground truth found on this machine (verified by probe)

1. This session runs inside `ssh jep@localhost` (`SSH_CONNECTION=::1`). Windows OpenSSH wraps every SSH session in a Job object with kill-on-close: closing the terminal kills Claude Code and everything it spawned. `nohup`/`start`/`setsid` do not escape it ([Win32-OpenSSH #1642](https://github.com/PowerShell/Win32-OpenSSH/issues/1642), verified).
2. Git fetch/push fail from here: `Unable to persist credentials with the 'wincredman' credential store`. Git Credential Manager's Windows store cannot run over an SSH/network logon ([GCM credstores doc](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/credstores.md), verified). The `dpapi` store may fail the same way under key-auth logons (reported, unconfirmed). Clone is stuck at 2026-08-31 09:30.
3. `ANTHROPIC_API_KEY` absent in shell, User and Machine env. `D:\work` = `vault\` only. `jep` cannot write `Program Files` or `C:\Users`. `remoteControlAtStartup: true` is already set.
4. Vault write-guard (ADR-004 layers 1 and 2) does not exist on the PC. Only `.vault-config/write-deny.list` travelled. Permission mode is `auto`, so vault boundaries are currently discipline-only.
5. Not installed: Obsidian (under jep), Codex CLI, llama-server, tmux, WezTerm, WSL2 (unchecked), WireGuard. Present: Windows Terminal 1.24, Git Bash 5.3, Node, Python 3.14, RTX 4090 24 GB.

## 2. Research verdicts

| Question                   | Verdict                                                                                                                                                                                                                                                            | Confidence           | Source                                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Native Windows vs WSL2     | Native. Obsidian cannot reliably watch `\\wsl.localhost`; `/mnt/d` over 9p is 5-20x slower; hooks run fine under Git Bash                                                                                                                                          | high                 | [Obsidian forum Jul 2026](https://forum.obsidian.md/t/obsidian-windows-claude-code-wsl2-sharing-one-vault-best-filesystem-architecture/116078), [WSL #4401](https://github.com/microsoft/WSL/issues/4401) |
| Sandbox on native Windows  | unsupported, WSL2 only. `jep` account = containment                                                                                                                                                                                                                | high                 | [sandboxing doc](https://code.claude.com/docs/en/sandboxing.md)                                                                                                                                           |
| Terminal                   | Windows Terminal stays: 1.24 auto-creates SSH profiles from `ssh_config`. No multiplexer, no run-as-user (WT #4217 backlog since 2020)                                                                                                                             | high                 | [WT 1.24 notes](https://devblogs.microsoft.com/commandline/windows-terminal-preview-1-24-release/)                                                                                                        |
| Detach/reattach            | psmux: native Rust tmux clone, client/server, ConPTY per pane, MIT, winget, v3.3.8. Fallback: WezTerm mux server (its `--daemonize` dies with the logon session, #3103). tmux via MSYS2: fragile with native node. mosh/Eternal Terminal: no Windows server exists | medium (psmux young) | [psmux](https://github.com/psmux/psmux), [wezterm #3103](https://github.com/wezterm/wezterm/issues/3103), [mosh #1030](https://github.com/mobile-shell/mosh/issues/1030)                                  |
| Escaping the sshd kill job | start the mux server from Task Scheduler (`/ru jep`, ONSTART) or WMI `Win32_Process.Create`; then sessions live outside any SSH job                                                                                                                                | high                 | Win32-OpenSSH #1642                                                                                                                                                                                       |
| Alternate access point     | Remote Control: claude.ai/code web and the mobile app attach to the PC's live CLI session; plan-billed; cross-session `SendMessage` laptop to PC works through it                                                                                                  | high                 | [remote-control doc](https://code.claude.com/docs/en/remote-control.md), [cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging.md)                                            |
| Git auth for jep           | SSH remote + GitHub deploy key (one repo, read-only or read/write, no account reach, no DPAPI, no token file). Beats GCM dpapi (unconfirmed over SSH) and `gh` (silently falls back to plaintext `hosts.yml` over SSH)                                             | high                 | [deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys), [gh #10108](https://github.com/cli/cli/issues/10108)                                         |
| Vault sync model           | Single git writer per strand; laptop mirror = `git pull --ff-only` on a systemd user timer. Never git + Syncthing on one vault                                                                                                                                     | high                 | [obsidian-git #872](https://github.com/Vinzent03/obsidian-git/issues/872)                                                                                                                                 |
| Pre-commit hook port       | Git for Windows runs `#!/bin/sh` hooks via bundled MSYS2 sh; keep POSIX-basic, LF endings, forward slashes. Blocklist at `C:\Users\jep\tutoring-data\blocklist.txt`, `icacls /inheritance:r /grant:r jep:R`                                                        | high                 | [husky #334](https://github.com/typicode/husky/issues/334)                                                                                                                                                |
| Autocommit on PC           | `schtasks` as jep every 30 min; Standard users can schedule for their own account; push needs stored password (no `/np`)                                                                                                                                           | high                 | [schtasks doc](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create)                                                                                          |
| Always-on                  | `powercfg` AC timeouts 0; check `powercfg /a` for "S0 Low Power Idle" (Modern Standby overrides Never; registry `PlatformAoAcOverride=0`); lock keeps processes, sign-out of admin leaves jep's sshd/task sessions alone                                           | high / reported      | [powercfg](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options)                                                                                    |
| Outside-home access        | WireGuard as a Windows tunnel service (`wireguard /installtunnelservice`, boot-time, admin once). DDNS without account: router-tied (ASUS) or "PC commits its WAN IP to the private repo". Headscale = overkill for two hosts                                      | medium               | [wireguard-windows enterprise doc](https://git.zx2c4.com/wireguard-windows/about/docs/enterprise.md)                                                                                                      |
| Headless Claude on PC      | no service mode. `claude -p` + `claude setup-token` long-lived OAuth token (plan-billed) for scheduled tasks; cloud Routines cannot touch local files                                                                                                              | high                 | [headless](https://code.claude.com/docs/en/headless.md), [routines](https://code.claude.com/docs/en/routines.md)                                                                                          |
| Telegram                   | Claude Code Channels (`--channels plugin:telegram@claude-plugins-official`, research preview, plan-billed) can replace the laptop's `kitchen-telegram` bot later; single instance either way                                                                       | medium               | [channels doc](https://code.claude.com/docs/en/channels.md)                                                                                                                                               |
| Obsidian + Claude          | no official integration. Claudian / obsidian-claude-code-mcp are third-party, plan-billed if they wrap Claude Code. Rule of three applies                                                                                                                          | high                 | [obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)                                                                                                                        |

Laptop excavation deltas worth knowing: `claude-vault`, `vault-write-guard.sh`, `run-agent.sh` are NOT in the repo (only the deny list and audit JSONL are). Evening-ping cron dead since 2026-08-16. `backup-health.sh` has never passed (70/70). Layer-3 deny rules use `Write(...)` and never match. Only Obsidian plugin in use: Templater.

## 3. Target architecture

```
[Idan, admin desktop] --WT profile "hq" = ssh + psmux attach--> [psmux server, user jep, started by Task Scheduler at boot]
                                                                   +-- claude (resident, Remote Control on)
                                                                   +-- codex exec / llama-server (later)
[Obsidian, admin desktop] --edits D:\work\vault directly (NTFS inherit: jep Full)
[laptop] --ssh over LAN (later WireGuard)--> same psmux session
[laptop / phone browser] --claude.ai/code Remote Control--> same claude session
[GitHub vault-backup] <--deploy key, PC pushes (strand owner)-- PC ; --pull --ff-only timer--> laptop mirror
```

Strand ownership after the flip: PC owns `projects/ inbox/ areas/ bases/`; laptop keeps `daily/digests/` + Telegram until those crons get their own port decision (ADR-005 Tier 4). Both pull before write.

## 4. Phases

### Phase A - foundation (today, ~45 min; me except where marked ADMIN / IDAN)
1. Deploy key: I generate `C:\Users\jep\.ssh\vault-deploy` (ed25519), switch `origin` to `git@github.com:IdanDalal/vault-backup.git`, pin `core.sshCommand`. IDAN pastes the public key at GitHub > vault-backup > Settings > Deploy keys, read-only for now. Verify: `git fetch` works, `git push --dry-run` refused.
2. Write guard: PreToolUse hook (Git Bash script) in `C:\Users\jep\.claude\hooks\` enforcing `.vault-config/write-deny.list`, audit JSONL to `.vault-config/audit/`. Verify with a bait Write to `atomic-notes/`.
3. psmux: `winget install psmux` as jep (user scope). ADMIN: `schtasks /create /sc onstart /ru jep /rp <pw> /tn psmux-hq /tr "psmux new-session -d -s hq"`. Verify: close terminal, reattach, claude still running.
4. Windows Terminal: add `~/.ssh/config` host `hq` (`HostName localhost`, `User jep`, `RemoteCommand psmux attach -t hq`, `RequestTTY yes`); WT 1.24 auto-lists it. One click entry. Pin as default profile.
5. ADMIN: `powercfg -change -standby-timeout-ac 0 -hibernate-timeout-ac 0`; `powercfg /a` check for S0 idle; Fast Startup off.
6. Obsidian: ADMIN installs, opens `D:\work\vault`, `.gitignore` already excludes `workspace*.json`. Verify a file created by admin is writable by jep (ACL inheritance).

### Phase B - write flip (own session, after A holds for a few days)
1. Deploy key promoted to read/write on GitHub.
2. Pre-commit hook ported to `C:\Users\jep\tutoring-data\tools\hooks\`, blocklist by USB, `core.hooksPath` set. Bait commit with a blocked name must be refused.
3. Autocommit + nightly-tag as `schtasks` every 30 min as jep, push failure LOUD (`_PUSH-FAILED.md` at vault root, no `|| true`).
4. Laptop: autocommit OFF for PC-owned strands; systemd user timer `git pull --ff-only` every 30 min; `loginctl enable-linger jep`.
5. Laptop gets memory + output style by `rsync` PC to laptop over SSH, never git.

### Phase C - reach (each its own decision doc)
WireGuard tunnel service on PC; Telegram via Claude Code Channels replacing `kitchen-telegram`; digest crons as PC scheduled tasks with `claude -p` + setup-token; Codex CLI; llama.cpp router; Claudian.

## 5. Risks
1. psmux is young (single project, v3.x). Mitigation: `claude --resume` always works; WezTerm mux is the fallback with the same scheduled-task launch.
2. Deploy key on a shared PC: private key readable only by jep via `icacls`; an admin can take ownership. Blast radius = one repo. Accept.
3. No kernel-level layer 1 on Windows: an NTFS deny on `atomic-notes/` would also break `git pull` running as jep. Hook + audit is the ceiling here unless git runs as a fourth identity. Accept, document.
4. Two writers during Phase A to B: PC cannot push until the key is promoted, so none.
5. Modern Standby may ignore powercfg on this board. Verify with `powercfg /a` before trusting always-on.

## 6. Session server decision - psmux vs WezTerm mux (research 2026-09-02)

Two layers: display (window drawing text) and server (process keeping the session alive). GPU acceleration belongs to the display layer only. Measured: Windows Terminal and WezTerm both 66.7 ms input latency at 80x50, software rendering within 4 ms of GPU ([chadaustin.me, Feb 2024](https://chadaustin.me/2024/02/windows-terminal-latency/), verified). No benchmark exists where the GPU model changes text rendering; the 4090 buys nothing here.

| Row | D1 Windows Terminal + psmux | D2 WezTerm + wezterm-mux | D3 WezTerm + psmux |
|---|---|---|---|
| Survival outside SSH job | documented Task-Scheduler launch; code tries `CREATE_BREAKAWAY_FROM_JOB` (`src/platform.rs`) | `--daemonize` = DETACHED_PROCESS, dies with the logon session, [#3103](https://github.com/wezterm/wezterm/issues/3103) open since 2023-02 | as D1 |
| Cross-user attach on PC | loopback TCP + key file in `~\.psmux`; use `ssh jep@localhost` | AF_UNIX socket under ACL, docs say "not recommended on multi-user systems" | as D1 |
| Laptop attach | plain `ssh jep@pc` then `psmux attach`, any client | wezterm on both ends, identical version (codec check), stable release is 2024-02 so matched nightlies | as D1 |
| TUI fidelity | [#613](https://github.com/psmux/psmux/issues/613) mouse-wheel bit stripped under node raw mode (open 2026-08-28); ConPTY fragments, fix `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT=1` | mux corruption ([claude-code #37076](https://github.com/anthropics/claude-code/issues/37076)), paste >1024 chars truncated ([#7235](https://github.com/wezterm/wezterm/issues/7235) open) | psmux issues + WezTerm paste bug |
| Maturity | psmux 9 months old, v3.3.8, ~monthly releases, 10 contributors, 35 open issues | 2.5 years without a stable release, 1,833 open issues, single maintainer | worst of both |
| Recovery | `schtasks /run`; `claude --resume` | protocol pinning, mux unresponsive under load [#7692](https://github.com/wezterm/wezterm/issues/7692) | as D1 |

Decision pending Idan. Recommendation D1. psmux docs require PowerShell 7 for Claude Code panes (`docs/claude-code.md`).

## 7. Phase A log

2026-09-02 (session 1):
- DONE deploy key `~/.ssh/vault-deploy` (ed25519, ACL jep only), registered read-only on GitHub; `origin` = `git@github.com:IdanDalal/vault-backup.git`; fetch verified, push refused, clone fast-forwarded to `3feb087`.
- DONE `~/.claude/hooks/vault-write-guard.py` (Layer 2 port, reads `write-deny.list`, audit to `.vault-config/audit/edits-pc-YYYY-MM.jsonl`); 10 unit cases pass; wired into the user settings PreToolUse block; went live immediately. Fail-open on malformed input, by design. Known false positive v1: any write-shaped Bash command whose text mentions the settings file name or the hook file name; patch pending (path-fragment match instead of basename).
- DONE psmux 3.3.8 user-scope (winget `marlocarlo.psmux`), `~/.psmux.conf` (pwsh7 shell, mouse, 20k history); PowerShell 7.6.5 portable at `~/.local/pwsh7` (MSI failed under SSH, 0x80070002); user PATH += psmux, pwsh7, `~/.local/bin`; env `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT=1`.
- DONE launcher `~/.local/bin/hq-server.cmd` (`psmux new-session -A -d -s hq -c D:\workault`).
- WAITING on admin: boot task `psmux-hq`, admin `~/.ssh/config` host `hq`, powercfg, Obsidian ACL check, hook patch copy.
- Decisions: D1 (Windows Terminal + psmux); flip held a few days; laptop keeps digest + Telegram strands.
