---
type: reference
created: 2026-09-03
author: jep
status: active
---

# PC HQ cheat sheet - three layers, who owns what

Window = Windows Terminal. Session keeper = psmux (tmux clone, prefix `Ctrl+b`). App = Claude Code. Each layer has its own settings and its own keys; a key goes to the innermost layer that claims it.

## Daily
- Open: Windows Terminal (default profile `hq`) → you land in the live session. `claude --continue` if Claude is not already running.
- Leave: just close the window. Session survives. `Ctrl+b d` = polite detach (same result).
- Reboot: session comes back on its own (Task Scheduler `psmux-hq`, 30 s after boot). If not: admin `schtasks /run /tn psmux-hq`.

## Scrolling
- Classic renderer (`/tui default`): output lives in psmux history (20k lines). Mouse wheel scrolls. Keyboard: `Ctrl+b` then `PgUp` → copy mode, `PgUp`/`PgDn`/arrows move, `q` exits.
- Fullscreen renderer (`/tui fullscreen`): Claude owns scrolling. `PgUp`/`PgDn`, `Ctrl+Home`/`Ctrl+End`, wheel. If keys are swallowed by the ssh→psmux chain: `Ctrl+o` = transcript mode, `j`/`k` lines, `Space`/`b` pages, `/` search, `q` back.
- `/tui` alone prints which renderer is active.

## Claude Code knobs
- `/config` = toggles (theme, auto-scroll, copy on select, notifications). `/model`, `/tui`, `/scroll-speed`, `/keybindings`, `/terminal-setup`.
- `Ctrl+o` transcript mode. `Ctrl+c` cancels current turn. `Esc` dismisses dialog. `/clear` new conversation. `/resume` pick an older one.
- Text selection inside fullscreen: click-drag copies on release. Native terminal selection: hold `Shift` while dragging.
- Env already set for jep: `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT=1` (fixes ConPTY fragments).

## psmux keys (prefix `Ctrl+b`, then)
- `d` detach. `[` copy/scroll mode (`q` exit). `c` new window, `n`/`p` next/prev window, `,` rename window. `%` split vertical, `"` split horizontal, arrows move between panes, `x` kill pane.
- `psmux ls` lists sessions. `psmux attach -t hq` reattach. Config: `C:\Users\jep\.psmux.conf` (tmux syntax; `mouse on`, pwsh7 shell).

## Windows Terminal knobs (admin side)
- `Ctrl+,` settings: Startup → default profile; Appearance; per-profile font/color scheme/opacity. `Ctrl+Shift+T` new tab, `Ctrl+Tab` switch, `Ctrl+Shift+F` find in terminal scrollback (sees only what psmux has painted).
- Profile `hq` = `"C:\Program Files\Git\usr\bin\ssh.exe" hq`; host `hq` defined in `C:\Users\Idi\.ssh\config`.

## When something is wrong
- Screen garbage: `Ctrl+l` repaint. Still bad: window resize by one column.
- Keys not reaching Claude: switch renderer (`/tui default` or `/tui fullscreen`), it relaunches with the conversation intact.
- Session missing (`psmux ls` empty): admin `schtasks /run /tn psmux-hq`, then reopen the tab.
- Git: PC is read-only (deploy key) until the flip; `git pull --ff-only` is safe anytime.
