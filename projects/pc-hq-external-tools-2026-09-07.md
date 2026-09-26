---
type: project
created: 2026-09-07
author: jep
status: active
tags: [pc-hq, billing, codex, antigravity, claude-in-chrome]
---

# External AI tools wired into Claude Code at HQ (2026-09-07)

Rule that decides everything: **account login only, never API keys**. Plan-billed = OK. Metered = out.

## Installed today (as `jep`, no admin)

| Tool | Version | Path | Auth | State |
|---|---|---|---|---|
| Codex CLI | 0.153.4 | `%APPDATA%\npm\codex.cmd` | `codex login` (ChatGPT plan) | installed, NOT logged in |
| Codex MCP server | same | `claude mcp add --scope user codex -- codex mcp-server` | inherits `~/.codex/auth.json` | registered, Connected |
| Antigravity CLI `agy` | 1.1.23 | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Google.AntigravityCLI_*\agy.exe` | Google OAuth on first run | installed, NOT logged in |

Codex install gotcha: npm skipped the platform binary. Fix that worked: `npm install -g "@openai/codex-win32-x64@npm:@openai/codex@0.153.4-win32-x64"`. Repeat with the new version string after each `npm i -g @openai/codex@latest`.

Codex auth precedence: `preferred_auth_method = chatgpt` (default) → ChatGPT login wins over any API key. Source: developers.openai.com/codex/auth/ci-cd-auth.

## Use from Claude Code

- Codex tool: MCP tools `codex` (prompt, cwd, model, sandbox, approval-policy) and `codex-reply` (threadId). Multi-turn, stays alive.
- Codex shell: `codex exec "task"` in Bash. Bills ChatGPT plan.
- Antigravity headless: `agy -p "task" --output-format json --print-timeout 5m`. Weekly compute cap on the Google plan. Models "subject to plan": confirm after login with `agy models`.
- Both are separate budgets. Neither raises Claude's context. Only outputs read back cost context.

## Browser / screen / apps: theory PROVEN, one official path

1. **Claude in Chrome** (official Anthropic, GA on paid plans late Aug 2026, plan-billed). `claude --chrome` in an interactive session. Shares the logged-in browser state. Works on **Chrome and Edge** per code.claude.com/docs/en/chrome (blogs saying Chrome-only are stale). Edge 152 present at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`; Chrome absent. Pauses on login pages and CAPTCHAs. Visible window. Needs `/login` plan auth, not API key. Not in WSL. Reaches: perplexity.ai, gemini.google.com (Nano Banana), chatgpt.com, any web app.
2. **Computer use, Desktop app** (research preview, Pro/Max, Windows supported). Browsers view-only, terminals click-only, other apps full control. Only adds native apps. Not installed. Desktop app must be running.
3. **Computer use, CLI**: macOS only. Windows: not available.
4. Third-party: Windows-MCP, MCPControl, Comet-MCP, cookie-based Perplexity MCPs. Unofficial, cookie/ToS exposure. Not recommended while path 1 exists.

Dead ends confirmed: Perplexity Sonar API (card-only, $5 Pro credit ended Feb 2026), Nano Banana extension (needs GEMINI/NANOBANANA_API_KEY), every Gemini/OpenAI/Perplexity MCP that takes a key.

Risk flags: Google/Perplexity ToS on automated use of their web apps (unverified, medium). Prompt injection from pages Claude reads. Site permissions managed in the extension.

## Key guard (extend the ANTHROPIC_API_KEY rule)

Check, user + machine scope:
```powershell
foreach ($k in 'ANTHROPIC_API_KEY','OPENAI_API_KEY','GEMINI_API_KEY','GOOGLE_API_KEY','NANOBANANA_API_KEY','PERPLEXITY_API_KEY') { foreach ($s in 'User','Machine') { $v=[Environment]::GetEnvironmentVariable($k,$s); if ($v) { "LEAK $k ($s)" } } }; "guard done"
```
Proposed: SessionStart hook running this, fail loud. Needs a settings.json edit, which the write-guard blocks for jep. Idan's call.

## Idan's actions (in order)

1. `! codex login` then `! codex login status`.
2. `! agy` (no args) → sign in with the Google AI Pro account → `! agy models`.
3. In Edge: install "Claude" from the Chrome Web Store (id fcoeoabgfenejglbffodgkkbkcdhcgfn). Sign the extension in.
4. Log Edge into perplexity.ai, gemini.google.com, chatgpt.com.
5. In the `hq` terminal: `claude --chrome`, then `/chrome` → Enabled by default only if context cost is acceptable.

## Sources
- code.claude.com/docs/en/chrome, code.claude.com/docs/en/computer-use, code.claude.com/docs/en/desktop
- learn.chatgpt.com/docs/mcp-server, developers.openai.com/codex/auth/ci-cd-auth
- developers.googleblog.com "Transitioning Gemini CLI to Antigravity CLI", antigravity.google/docs/cli/headless
- github.com/gemini-cli-extensions/nanobanana, perplexity.ai help "API Payment and billing"
