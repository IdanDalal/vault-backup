# Phase 5.2: Deterministic Capture Hook — Install Recipe

**Goal**: Prefix-matched messages are captured to daily notes by Python, not by Claude prompt interpretation.

---

## Prerequisites

- Phase 5.1 complete (systemd service running)
- `~/vault/daily/` exists (or will be created by the hook on first capture)

## Steps

### 1. Copy the hook script to the laptop

```bash
# From the desktop, or via USB/scp:
cp capture_hook.py ~/vault/.vault-config/hooks/capture_hook.py
```

### 2. Add the hook to the laptop's settings.json

Edit `~/.claude/settings.json` on the laptop. Add a `UserPromptSubmit` entry:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/vault/.vault-config/hooks/capture_hook.py"
          }
        ]
      }
    ]
  }
}
```

If there are already other hooks in `settings.json`, merge — don't replace.

**Important**: The hook needs to know the vault path. Set `KITCHEN_VAULT_PATH` in `~/.config/kitchen/env`:

```bash
echo 'KITCHEN_VAULT_PATH=/home/jep/vault' >> ~/.config/kitchen/env
```

Or if it defaults to `~/vault` and that's correct, skip this step.

### 3. Restart the Telegram service

```bash
systemctl --user restart kitchen-telegram.service
```

### 4. Test from phone

Send these Telegram messages and verify each lands in today's daily note:

| Message | Expected in daily note |
|---|---|
| `idea: test the capture hook` | `- HH:MM test the capture hook` |
| `c: quick shorthand test` | `- HH:MM quick shorthand test` |
| `thought: does this work?` | `- HH:MM does this work?` |
| `what time is it?` | (should NOT be captured — Claude responds normally) |

### 5. Verify daily note

```bash
cat ~/vault/daily/$(date +%F).md | grep -A5 "## Captures"
```

---

## Supported prefixes

| Prefix | Example |
|---|---|
| `idea:` or `idea ` | `idea: build a health vault` |
| `thought:` or `thought ` | `thought: maybe split daily into sections` |
| `capture:` or `capture ` | `capture: meeting notes from call` |
| `note:` or `note ` | `note: dentist appointment Thursday` |
| `c:` or `c ` | `c: quick capture` |
| `ADD TO DAILY NOTE:` | `ADD TO DAILY NOTE: backward compat` |

Everything else passes through to Claude for normal conversation.

---

*Phase 5.2 of ADR-007. Authored 2026-04-13.*
