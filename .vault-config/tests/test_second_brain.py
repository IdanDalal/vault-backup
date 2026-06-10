"""
Contract tests for ADR-002 + ADR-003: Vault Architecture + Backup Strategy.

These tests define WHAT MUST BE TRUE when the second brain is operational.
Run on the laptop after each phase to verify success.

Usage:
    # From the laptop:
    python -m pytest tests/contracts/test_second_brain.py -v --capture=no

    # From the desktop, via SSH:
    ssh laptop 'cd ~/vault && python -m pytest tests/contracts/test_second_brain.py -v'
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VAULT = Path.home() / "vault"
VAULT_AGENT = Path.home() / "vault-agent"

READ_ONLY_DIRS = ["atomic-notes", "templates", "resources", "attachments"]
WRITABLE_DIRS = ["daily", "projects", "areas", "bases", "inbox"]
ALL_DIRS = READ_ONLY_DIRS + WRITABLE_DIRS


def run(cmd: str, timeout: int = 30) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd, shell=True, capture_output=True, text=True, timeout=timeout
    )


pytestmark = pytest.mark.skipif(
    not VAULT.exists(),
    reason="Vault not found at ~/vault — tests run on the laptop only"
)


# ===========================================================================
# Phase 1: Vault Structure
# ===========================================================================

class TestVaultStructure:
    """Verify the vault directory layout matches ADR-002."""

    def test_vault_is_git_repo(self):
        assert (VAULT / ".git").exists(), "~/vault must be a git repository"

    @pytest.mark.parametrize("dirname", ALL_DIRS)
    def test_directory_exists(self, dirname):
        assert (VAULT / dirname).is_dir(), f"Missing: ~/vault/{dirname}/"

    def test_vault_config_exists(self):
        assert (VAULT / ".vault-config").is_dir()

    def test_permissions_md_exists(self):
        assert (VAULT / ".vault-config" / "PERMISSIONS.md").is_file()

    def test_claude_md_exists(self):
        assert (VAULT / "CLAUDE.md").is_file()

    def test_gitignore_exists(self):
        gitignore = VAULT / ".gitignore"
        assert gitignore.is_file()
        content = gitignore.read_text()
        for entry in ["workspace.json", ".trash/", ".DS_Store"]:
            assert entry in content, f".gitignore missing: {entry}"

    def test_gitattributes_merge_union(self):
        gitattributes = VAULT / ".gitattributes"
        assert gitattributes.is_file(), ".gitattributes not found"
        content = gitattributes.read_text()
        assert "merge=union" in content, \
            ".gitattributes must set merge=union for markdown files"

    def test_digests_subdirectory(self):
        assert (VAULT / "daily" / "digests").is_dir()

    def test_vault_config_subdirectories(self):
        for sub in ["scripts", "prompts", "logs", "tests"]:
            assert (VAULT / ".vault-config" / sub).is_dir(), \
                f"Missing: .vault-config/{sub}/"


# ===========================================================================
# Phase 2: Backup System
# ===========================================================================

BACKUP_SCRIPTS = [
    "autocommit.sh",
    "nightly-tag.sh",
    "restic-backup.sh",
    "backup-health.sh",
]

CRON_KEYWORDS = {
    "autocommit":    "L1 — autocommit every 30 min",
    "nightly-tag":   "L2 — nightly snapshot tags",
    "restic-backup": "L4 — weekly encrypted offsite",
    "backup-health": "Health check every 6 hours",
    "git gc":        "Monthly history compression",
}


class TestBackupSystem:
    """Verify the four-layer backup is operational (ADR-003)."""

    # -- L1: Git Autocommit --

    @pytest.mark.parametrize("script", BACKUP_SCRIPTS)
    def test_backup_script_exists_and_executable(self, script):
        path = VAULT / ".vault-config" / "scripts" / script
        assert path.is_file(), f"Missing: .vault-config/scripts/{script}"
        assert os.access(path, os.X_OK), f"{script} must be executable"

    @pytest.mark.parametrize("keyword,description", CRON_KEYWORDS.items())
    def test_cron_entry_exists(self, keyword, description):
        result = run("crontab -l")
        assert keyword in result.stdout, \
            f"No cron entry for: {description}"

    def test_git_remote_configured(self):
        result = run(f"git -C {VAULT} remote -v")
        assert result.returncode == 0
        assert "origin" in result.stdout, "No git remote 'origin' configured"

    def test_git_push_dry_run(self):
        result = run(f"git -C {VAULT} push --dry-run 2>&1")
        assert result.returncode == 0, \
            f"git push --dry-run failed: {result.stderr}"

    # -- L3: Syncthing --

    def test_syncthing_service_active(self):
        result = run("systemctl is-active syncthing@idan")
        assert "active" in result.stdout.strip(), \
            "Syncthing service must be running"

    def test_stignore_exists(self):
        stignore = VAULT / ".stignore"
        assert stignore.is_file(), "~/vault/.stignore not found"
        content = stignore.read_text()
        for entry in [".git", "workspace.json", ".vault-config/logs"]:
            assert entry in content, f".stignore missing: {entry}"

    # -- L4: Restic --

    def test_restic_initialized(self):
        result = run("restic snapshots --no-lock 2>&1")
        assert result.returncode == 0, "Restic not initialized or not configured"

    def test_restic_credentials_not_in_vault(self):
        """Restic credentials must NOT live inside the vault."""
        env_in_vault = VAULT / ".config" / "restic" / "env"
        assert not env_in_vault.exists(), \
            "Restic credentials found inside vault — must be in ~/.config/restic/env"


# ===========================================================================
# Phase 3: Vault Write Enforcement (ADR-004)
# Three-layer defense — group+setpriv (Layer 1), PreToolUse hook (Layer 2),
# settings.json deny globs (Layer 3, advisory).
# ===========================================================================

import grp
import hashlib
import json
import shutil
import tempfile
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
DEPLOY = REPO_ROOT / "data" / "deploy" / "vault-config"

HOOK_INSTALLED = Path.home() / ".claude" / "hooks" / "vault-write-guard.sh"
HOOK_SOURCE = DEPLOY / "hooks" / "vault-write-guard.sh"

WRAPPER_INSTALLED = Path.home() / "bin" / "claude-vault"
WRAPPER_SOURCE = DEPLOY / "bin" / "claude-vault"

HELPER_INSTALLED = Path("/usr/local/bin/claude-vault-helper")
HELPER_SOURCE = DEPLOY / "bin" / "claude-vault-helper"

SUDOERS_INSTALLED = Path("/etc/sudoers.d/claude-vault")
SUDOERS_SOURCE = DEPLOY / "sudoers" / "claude-vault"

DENY_LIST_INSTALLED = VAULT / ".vault-config" / "write-deny.list"
DENY_LIST_SOURCE = DEPLOY / "write-deny.list"

REQUIRED_DENY_PATTERNS = [
    "/home/jep/vault/atomic-notes/**",
    "/home/jep/vault/.vault-config/**",
    "/home/jep/vault/.git/**",
    "/home/jep/vault/.obsidian/**",
]

ATOMIC_NOTES = VAULT / "atomic-notes"
AUDIT_DIR = VAULT / ".vault-config" / "audit"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class TestVaultWriteEnforcement:
    """Verify the three-layer write enforcement stack from ADR-004."""

    # ---- Layer 1: Unix group + setpriv wrapper ----

    def test_vault_write_group_exists(self):
        try:
            grp.getgrnam("vault-write")
        except KeyError:
            pytest.fail("Layer 1: 'vault-write' group must exist (groupadd vault-write)")

    def test_jep_in_vault_write_group(self):
        try:
            group = grp.getgrnam("vault-write")
        except KeyError:
            pytest.skip("vault-write group missing — covered by previous test")
        assert "jep" in group.gr_mem, \
            "Layer 1: user 'jep' must be a member of vault-write (usermod -aG vault-write jep)"

    def test_atomic_notes_ownership_and_mode(self):
        st = ATOMIC_NOTES.stat()
        owner_uid = st.st_uid
        group_gid = st.st_gid
        mode = st.st_mode & 0o7777
        # Owner must be root (uid 0) so jep falls through to group bits
        assert owner_uid == 0, \
            f"Layer 1: ~/vault/atomic-notes/ must be owned by root, got uid={owner_uid}"
        # Group must be vault-write
        try:
            vw_gid = grp.getgrnam("vault-write").gr_gid
        except KeyError:
            pytest.skip("vault-write group missing")
        assert group_gid == vw_gid, \
            f"Layer 1: ~/vault/atomic-notes/ group must be vault-write (gid {vw_gid}), got {group_gid}"
        # Mode must be 2775 (setgid + group rwx + other r-x)
        assert mode == 0o2775, \
            f"Layer 1: ~/vault/atomic-notes/ mode must be 2775, got {oct(mode)}"

    def test_claude_vault_wrapper_installed(self):
        assert WRAPPER_INSTALLED.is_file(), \
            f"Layer 1: {WRAPPER_INSTALLED} must exist (deploy from {WRAPPER_SOURCE})"
        assert os.access(WRAPPER_INSTALLED, os.X_OK), \
            "Layer 1: claude-vault must be executable"
        st = WRAPPER_INSTALLED.stat()
        assert st.st_uid == 0, \
            "Layer 1: claude-vault must be owned by root (chown root:root) so Claude can't overwrite it"

    def test_claude_vault_helper_installed(self):
        assert HELPER_INSTALLED.is_file(), \
            f"Layer 1: {HELPER_INSTALLED} must exist (deploy from {HELPER_SOURCE})"
        assert os.access(HELPER_INSTALLED, os.X_OK), \
            "Layer 1: claude-vault-helper must be executable"
        st = HELPER_INSTALLED.stat()
        assert st.st_uid == 0, \
            "Layer 1: claude-vault-helper must be owned by root"
        # Must NOT be world-writable
        assert (st.st_mode & 0o002) == 0, \
            "Layer 1: claude-vault-helper must not be world-writable"

    def test_claude_vault_helper_matches_source(self):
        if not HELPER_INSTALLED.is_file():
            pytest.skip("helper not installed")
        if not HELPER_SOURCE.is_file():
            pytest.skip(
                f"deploy source not present at {HELPER_SOURCE} — "
                "drift detection is only meaningful on the repo host (desktop)."
            )
        assert sha256_of(HELPER_INSTALLED) == sha256_of(HELPER_SOURCE), \
            f"Layer 1: claude-vault-helper drift detected. Redeploy from {HELPER_SOURCE}."

    def test_sudoers_rule_installed(self):
        assert SUDOERS_INSTALLED.is_file(), \
            f"Layer 1: sudoers rule missing at {SUDOERS_INSTALLED}"
        st = SUDOERS_INSTALLED.stat()
        # Sudoers files MUST be mode 0440 or sudo refuses them
        mode = st.st_mode & 0o777
        assert mode == 0o440, \
            f"Layer 1: {SUDOERS_INSTALLED} must be mode 0440, got {oct(mode)}"
        assert st.st_uid == 0, \
            f"Layer 1: {SUDOERS_INSTALLED} must be owned by root"
        # Content check: sudoers files are 0440 root:root so jep cannot read them
        # directly. Use sudo cat (the NOPASSWD grant doesn't cover cat, so this
        # will prompt or fail — use --non-interactive and skip content check if
        # it fails rather than hang the test suite). The structural check via
        # `visudo -c` in test_sudoers_rule_parses is the authoritative validator;
        # this content check is a nice-to-have for catching obvious drift.
        result = run(f"sudo --non-interactive cat {SUDOERS_INSTALLED} 2>/dev/null")
        if result.returncode != 0:
            pytest.skip(
                "Cannot read sudoers content without password; "
                "visudo -c validation covers parse correctness."
            )
        content = result.stdout
        assert "/usr/local/bin/claude-vault-helper" in content, \
            "Layer 1: sudoers rule must reference the exact helper path"
        assert "NOPASSWD" in content, \
            "Layer 1: sudoers rule must be NOPASSWD (passworded rule hangs --non-interactive sudo)"

    def test_sudoers_rule_parses(self):
        """visudo -c must accept the rule file."""
        if not SUDOERS_INSTALLED.is_file():
            pytest.skip("sudoers rule not installed")
        result = run(f"sudo visudo -c -f {SUDOERS_INSTALLED}")
        assert result.returncode == 0, \
            f"Layer 1: visudo rejected sudoers rule: {result.stdout}\n{result.stderr}"

    def test_claude_vault_wrapper_matches_source(self):
        if not WRAPPER_INSTALLED.is_file():
            pytest.skip("wrapper not installed")
        if not WRAPPER_SOURCE.is_file():
            pytest.skip(
                f"deploy source not present at {WRAPPER_SOURCE} — "
                "drift detection is only meaningful on the repo host (desktop), "
                "not on the deployed laptop. Installed artifact exists and is trusted."
            )
        installed = sha256_of(WRAPPER_INSTALLED)
        source = sha256_of(WRAPPER_SOURCE)
        assert installed == source, \
            f"Layer 1: claude-vault drift detected. Installed sha256={installed}, source={source}. " \
            f"Redeploy from {WRAPPER_SOURCE}."

    def test_layer1_helper_self_test_drops_vault_write(self):
        """Full Layer 1 round trip through sudo + helper + setpriv.

        Invokes the helper's --self-test mode via sudo, which exercises the
        ENTIRE privilege-drop chain (sudoers → root → setpriv → jep:jep).
        Parses the reported group list and verifies vault-write is absent.

        Hardened against false positives:
          - Explicit SELFTEST_OK marker must appear (proves the chain ran to completion)
          - Explicit SELFTEST_GROUPS line must be present and must NOT contain vault-write
          - Any failure of sudo/helper/setpriv causes the test to fail LOUD
        """
        if not HELPER_INSTALLED.is_file():
            pytest.skip("helper not installed")
        if not SUDOERS_INSTALLED.is_file():
            pytest.skip("sudoers rule not installed")
        try:
            grp.getgrnam("vault-write")
        except KeyError:
            pytest.skip("vault-write group missing")

        result = run(f"sudo --non-interactive -- {HELPER_INSTALLED} --self-test")
        combined = result.stdout + result.stderr

        assert "SELFTEST_OK" in combined, (
            f"Layer 1: helper self-test did not complete. The privilege-drop chain "
            f"(sudo → helper → setpriv) is broken somewhere. "
            f"Fix Layer 1 BEFORE trusting the system. Output: {combined}"
        )
        # Extract the reported group list
        import re
        m = re.search(r"SELFTEST_GROUPS=(.*)", combined)
        assert m, f"Layer 1: helper did not report SELFTEST_GROUPS. Output: {combined}"
        reported_groups = m.group(1).strip().split()
        assert "vault-write" not in reported_groups, (
            f"Layer 1 BREACH: vault-write still present in dropped process group list. "
            f"Reported groups: {reported_groups}"
        )
        # And verify the reported UID is jep's UID (not root)
        m_uid = re.search(r"SELFTEST_UID=(\d+)", combined)
        assert m_uid, f"Layer 1: helper did not report SELFTEST_UID. Output: {combined}"
        import pwd
        jep_uid = pwd.getpwnam("jep").pw_uid
        assert int(m_uid.group(1)) == jep_uid, (
            f"Layer 1: dropped process UID mismatch. Expected {jep_uid} (jep), "
            f"got {m_uid.group(1)}"
        )

    def test_layer1_kernel_blocks_write_from_dropped_process(self):
        """Second round-trip test: the kernel actually refuses the write.

        Even if the group-list check above passes, verify that the kernel's
        permission check on ~/vault/atomic-notes/ actually fires. This catches
        the scenario where groups are dropped correctly but the directory
        mode or ownership is wrong.

        We do this by running a small bash snippet through the helper's
        self-test path — but since --self-test only reports groups, we
        need a different approach: directly test the atomic-notes write
        using the same setpriv invocation the helper uses, but invoke it
        via sudo so setgroups() is permitted.
        """
        if not HELPER_INSTALLED.is_file():
            pytest.skip("helper not installed")
        if not SUDOERS_INSTALLED.is_file():
            pytest.skip("sudoers rule not installed")
        try:
            grp.getgrnam("vault-write")
        except KeyError:
            pytest.skip("vault-write group missing")

        target = ATOMIC_NOTES / ".layer1-kernel-test"
        # We cannot arbitrarily execute bash via the helper (it only runs
        # --self-test or claude). Instead we call sudo setpriv directly.
        # This requires that test runs with passwordless sudo to setpriv,
        # which the contract test host (the laptop) has for claude-vault-helper
        # but NOT for setpriv itself. So we test via the real helper path:
        # we temporarily create a test that uses --self-test with a side effect.
        #
        # Simpler: call setpriv via sudo. If no sudo rule allows it,
        # the test will fail-skip (not false-pass) because the sudo call
        # itself will fail.
        result = run(
            f"sudo --non-interactive -- setpriv "
            f"--reuid=jep --regid=jep --groups=jep --inh-caps=-all -- "
            f"bash -c 'echo MARKER_START; groups; echo test > {target} 2>&1; "
            f"echo EXIT=$?; echo MARKER_END'"
        )
        combined = result.stdout + result.stderr

        if "MARKER_START" not in combined:
            pytest.skip(
                "sudo does not allow direct setpriv invocation on this host. "
                "Layer 1 group drop still verified by the self-test path. "
                f"Sudo output: {combined}"
            )

        # Cleanup if file was created despite the drop
        if target.exists():
            try:
                target.unlink()
            except OSError:
                pass
            pytest.fail(
                f"Layer 1 BREACH: dropped process WROTE to {target}. "
                f"The kernel did not refuse the write. Check atomic-notes/ "
                f"ownership and mode. Output: {combined}"
            )
        assert "Permission denied" in combined or "EACCES" in combined, (
            f"Layer 1: expected 'Permission denied' from the kernel. Output: {combined}"
        )
        assert "EXIT=0" not in combined, (
            f"Layer 1 BREACH: write returned exit 0. Output: {combined}"
        )

    def test_layer1_allows_write_from_normal_session(self):
        """Idi's normal shell (with vault-write group) MUST still be able to write."""
        try:
            grp.getgrnam("vault-write")
        except KeyError:
            pytest.skip("vault-write group missing")
        if "vault-write" not in [grp.getgrgid(g).gr_name for g in os.getgroups()]:
            pytest.skip("test runner not in vault-write group — re-login or run as jep")
        target = ATOMIC_NOTES / ".write-test-allowed"
        try:
            target.write_text("test\n")
            assert target.exists(), "Normal session must be able to write to atomic-notes/"
        finally:
            if target.exists():
                target.unlink()

    # ---- Layer 2: PreToolUse hook ----

    def test_hook_script_installed(self):
        assert HOOK_INSTALLED.is_file(), \
            f"Layer 2: hook missing at {HOOK_INSTALLED} (deploy from {HOOK_SOURCE})"
        assert os.access(HOOK_INSTALLED, os.X_OK), \
            "Layer 2: hook script must be executable"

    def test_hook_script_matches_source(self):
        if not HOOK_INSTALLED.is_file():
            pytest.skip("hook not installed")
        if not HOOK_SOURCE.is_file():
            pytest.skip(
                f"deploy source not present at {HOOK_SOURCE} — "
                "drift detection is only meaningful on the repo host (desktop), "
                "not on the deployed laptop. Installed artifact exists and is trusted."
            )
        installed = sha256_of(HOOK_INSTALLED)
        source = sha256_of(HOOK_SOURCE)
        assert installed == source, \
            f"Layer 2: hook drift detected. Redeploy from {HOOK_SOURCE}."

    def test_deny_list_installed_and_complete(self):
        assert DENY_LIST_INSTALLED.is_file(), \
            f"Layer 2: deny list missing at {DENY_LIST_INSTALLED}"
        content = DENY_LIST_INSTALLED.read_text()
        for pattern in REQUIRED_DENY_PATTERNS:
            assert pattern in content, \
                f"Layer 2: deny list missing required pattern: {pattern}"

    def test_hook_blocks_denied_edit(self):
        if not HOOK_INSTALLED.is_file():
            pytest.skip("hook not installed")
        event = json.dumps({
            "session_id": "test-deny",
            "tool_name": "Edit",
            "tool_input": {"file_path": str(ATOMIC_NOTES / "fake-test.md")},
        })
        result = subprocess.run(
            [str(HOOK_INSTALLED)],
            input=event, capture_output=True, text=True, timeout=10
        )
        assert result.returncode == 2, \
            f"Layer 2: hook must exit 2 on denied path, got {result.returncode}. stderr={result.stderr}"
        assert "BLOCKED" in result.stderr, \
            f"Layer 2: hook must explain the block on stderr. stderr={result.stderr}"

    def test_hook_allows_writable_edit(self):
        if not HOOK_INSTALLED.is_file():
            pytest.skip("hook not installed")
        event = json.dumps({
            "session_id": "test-allow",
            "tool_name": "Edit",
            "tool_input": {"file_path": str(VAULT / "daily" / "fake-test.md")},
        })
        result = subprocess.run(
            [str(HOOK_INSTALLED)],
            input=event, capture_output=True, text=True, timeout=10
        )
        assert result.returncode == 0, \
            f"Layer 2: hook must exit 0 on allowed path, got {result.returncode}. stderr={result.stderr}"

    def test_hook_writes_audit_entry(self):
        if not HOOK_INSTALLED.is_file():
            pytest.skip("hook not installed")
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        audit_file = AUDIT_DIR / f"edits-{datetime.now(timezone.utc):%Y-%m}.jsonl"
        before_size = audit_file.stat().st_size if audit_file.exists() else 0
        event = json.dumps({
            "session_id": "test-audit",
            "tool_name": "Edit",
            "tool_input": {"file_path": str(VAULT / "daily" / "audit-test.md")},
        })
        subprocess.run(
            [str(HOOK_INSTALLED)],
            input=event, capture_output=True, text=True, timeout=10
        )
        assert audit_file.exists(), "Layer 2: audit log was not created"
        new_size = audit_file.stat().st_size
        assert new_size > before_size, "Layer 2: hook did not append to audit log"
        # Last line should be valid JSON with the expected fields
        last_line = audit_file.read_text().strip().split("\n")[-1]
        entry = json.loads(last_line)
        for field in ("ts", "tool", "path", "decision", "session"):
            assert field in entry, f"Audit entry missing field: {field}"
        assert entry["session"] == "test-audit"

    # ---- Layer 3: settings.json (advisory) ----

    def test_settings_json_has_layer3_deny_globs(self):
        settings = Path.home() / ".claude" / "settings.json"
        assert settings.is_file(), "Layer 3: ~/.claude/settings.json not found"
        config = json.loads(settings.read_text())
        deny = config.get("permissions", {}).get("deny", [])
        # Layer 3 patterns are in Claude Code's tool-call format: "Edit(path)" / "Write(path)"
        deny_str = " ".join(deny) if isinstance(deny, list) else str(deny)
        for pattern in REQUIRED_DENY_PATTERNS:
            # Just check the path fragment appears somewhere in a deny rule
            path_frag = pattern.replace("/**", "")
            assert path_frag in deny_str, \
                f"Layer 3: settings.json permissions.deny missing rule for {path_frag}"

    def test_settings_json_registers_pretooluse_hook(self):
        settings = Path.home() / ".claude" / "settings.json"
        if not settings.is_file():
            pytest.skip("settings.json not found")
        config = json.loads(settings.read_text())
        hooks = config.get("hooks", {})
        pre = hooks.get("PreToolUse", [])
        assert pre, "Layer 2: settings.json hooks.PreToolUse must register vault-write-guard.sh"
        registered = json.dumps(pre)
        assert "vault-write-guard.sh" in registered, \
            "Layer 2: PreToolUse must reference vault-write-guard.sh"

    def test_claude_vault_alias_in_bashrc(self):
        bashrc = Path.home() / ".bashrc"
        if not bashrc.exists():
            pytest.skip("~/.bashrc not present")
        content = bashrc.read_text()
        assert "alias claude='claude-vault'" in content or 'alias claude="claude-vault"' in content, \
            "Layer 1 backstop: ~/.bashrc must alias claude -> claude-vault"


# ===========================================================================
# Phase 7: Dual-Mode Hardening
# ===========================================================================

class TestDualMode:
    """Verify the laptop works headless (lid closed) and GUI (lid open)."""

    def test_lid_switch_ignored(self):
        result = run("grep HandleLidSwitch /etc/systemd/logind.conf")
        assert result.returncode == 0
        assert "ignore" in result.stdout, \
            "HandleLidSwitch must be 'ignore' for headless operation"

    def test_system_health_script_exists(self):
        script = VAULT / ".vault-config" / "scripts" / "system-health.sh"
        assert script.is_file()
        assert os.access(script, os.X_OK)

    def test_ssh_password_auth_disabled(self):
        result = run("grep -E '^PasswordAuthentication' /etc/ssh/sshd_config")
        if result.stdout.strip():
            assert "no" in result.stdout.lower(), \
                "SSH password auth should be disabled"

    def test_fail2ban_active(self):
        result = run("systemctl is-active fail2ban")
        assert "active" in result.stdout.strip(), "fail2ban must be running"
