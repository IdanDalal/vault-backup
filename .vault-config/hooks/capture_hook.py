#!/usr/bin/env python3
"""
Deterministic Capture Hook — Phase 5.2 of ADR-007.

UserPromptSubmit hook that intercepts capture-prefixed messages and appends
them directly to today's daily note. The write happens in Python before
Claude processes the message. Claude then confirms instead of acting.

Zen: Explicit is better than implicit. Simple is better than complex.
     Errors should never pass silently.

Prefixes (case-insensitive):
    idea: / idea     → capture
    thought: / thought → capture
    capture: / capture → capture
    note: / note     → capture
    c: / c           → capture (shorthand)
    ADD TO DAILY NOTE: → capture (backward compat)

Hook contract:
    stdin:  {"prompt": "...", "cwd": "..."}
    stdout: guidance text (shown to Claude as hook output)
    exit 0: always (hook must not block the message)
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Prefixes: order matters — longest match first to avoid partial hits.
# Each tuple is (pattern, group index for captured text).
# Zen: There should be one obvious way to do it — one list, one loop.
PREFIXES = [
    re.compile(r"^add\s+to\s+daily\s+note:\s*(.*)", re.IGNORECASE | re.DOTALL),
    re.compile(r"^idea[:\s]\s*(.*)", re.IGNORECASE | re.DOTALL),
    re.compile(r"^thought[:\s]\s*(.*)", re.IGNORECASE | re.DOTALL),
    re.compile(r"^capture[:\s]\s*(.*)", re.IGNORECASE | re.DOTALL),
    re.compile(r"^note[:\s]\s*(.*)", re.IGNORECASE | re.DOTALL),
    re.compile(r"^c[:\s]\s*(.*)", re.IGNORECASE | re.DOTALL),
]

# Vault path: explicit env var, no guessing.
DEFAULT_VAULT_PATH = Path.home() / "vault"


# ---------------------------------------------------------------------------
# Prefix matching
# ---------------------------------------------------------------------------

def match_capture(message: str) -> str | None:
    """
    Match message against capture prefixes.

    Returns the captured text (prefix stripped) or None.
    Zen: Explicit is better than implicit — returns the exact text to store.
    """
    stripped = message.strip()
    if not stripped:
        return None

    for pattern in PREFIXES:
        m = pattern.match(stripped)
        if m:
            text = m.group(1).strip()
            if text:  # Prefix alone with no content is not a capture
                return text
            return None

    return None


# ---------------------------------------------------------------------------
# Daily note operations
# ---------------------------------------------------------------------------

def _get_vault_path(vault_path: Path | None = None) -> Path:
    """Resolve vault path: explicit arg > env var > default."""
    if vault_path is not None:
        return vault_path
    env = os.environ.get("KITCHEN_VAULT_PATH")
    if env:
        return Path(env)
    return DEFAULT_VAULT_PATH


def _get_daily_note_path(vault_path: Path) -> Path:
    """Path to today's daily note. Zen: flat is better than nested."""
    today = datetime.now().strftime("%Y-%m-%d")
    return vault_path / "daily" / f"{today}.md"


def _create_minimal_daily_note(path: Path) -> None:
    """
    Create a minimal daily note with just the Captures section.

    Zen: Simple is better than complex. We don't replicate the full
    Templater template — that's Obsidian's job. We create just enough
    structure for the capture to land safely.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    weekday = datetime.now().strftime("%A")
    content = f"""---
type: daily
date: {today}
weekday: {weekday}
---

# {today} {weekday}

## Captures

"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _format_bullet(text: str) -> str:
    """
    Format capture as a daily note bullet.

    Multiline → single line (semicolon-separated).
    Zen: Readability counts.
    """
    now = datetime.now().strftime("%H:%M")
    # Collapse multiline to single bullet
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    collapsed = "; ".join(lines)
    return f"- {now} {collapsed}"


def append_capture(text: str, vault_path: Path | None = None) -> str:
    """
    Append a capture bullet to today's daily note.

    Returns the formatted bullet that was appended.
    Raises on failure — errors should never pass silently.
    """
    vault = _get_vault_path(vault_path)
    daily_path = _get_daily_note_path(vault)

    # Create daily note if it doesn't exist
    if not daily_path.exists():
        _create_minimal_daily_note(daily_path)

    content = daily_path.read_text()
    bullet = _format_bullet(text)

    # Find ## Captures section
    captures_match = re.search(
        r"(## Captures\n(?:<!--.*?-->\n)*\n?)",
        content,
    )

    if captures_match:
        # Insert after the section header (and any HTML comments)
        insert_pos = captures_match.end()
        # Skip the bare "-" placeholder if present
        remaining = content[insert_pos:]
        if remaining.startswith("-\n") or remaining.startswith("- \n"):
            insert_pos += remaining.index("\n") + 1

        new_content = content[:insert_pos] + bullet + "\n" + content[insert_pos:]
    else:
        # No Captures section — append at EOF
        # Zen: Errors should never pass silently — leave a visible marker
        warning = "\n<!-- WARNING: ## Captures section was missing, added by capture hook -->\n"
        new_content = content.rstrip() + warning + "\n## Captures\n\n" + bullet + "\n"

    daily_path.write_text(new_content)
    return bullet


# ---------------------------------------------------------------------------
# Hook interface
# ---------------------------------------------------------------------------

def process_hook(stdin_data: str) -> str | None:
    """
    Process a UserPromptSubmit hook invocation.

    Returns guidance text for Claude, or None if not a capture.
    Zen: Explicit is better than implicit — the return value IS the contract.
    """
    try:
        data = json.loads(stdin_data)
    except (json.JSONDecodeError, TypeError):
        return None

    prompt = data.get("prompt", "")
    if not prompt:
        return None

    captured_text = match_capture(prompt)
    if captured_text is None:
        return None

    # Do the write — deterministic, before Claude sees the message
    try:
        bullet = append_capture(captured_text)
        return (
            f"CAPTURED: {bullet}\n"
            f"The capture has already been written to today's daily note.\n"
            f"Reply with a brief confirmation only (e.g. 'captured'). "
            f"Do not elaborate, research, or act on the content."
        )
    except Exception as e:
        # Zen: Errors should never pass silently.
        return (
            f"CAPTURE FAILED: {e}\n"
            f"The user tried to capture: {captured_text!r}\n"
            f"Tell the user the capture hook failed and offer to write it manually."
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    stdin_data = sys.stdin.read()
    result = process_hook(stdin_data)
    if result:
        print(result)
    sys.exit(0)


if __name__ == "__main__":
    main()
