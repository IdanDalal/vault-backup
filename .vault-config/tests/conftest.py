"""Shared fixtures for contract tests."""

from pathlib import Path

import pytest
import yaml


WORKSPACE = Path("/workspace")


@pytest.fixture
def workspace():
    """Root workspace path."""
    return WORKSPACE


@pytest.fixture
def manifest():
    """Load the integration manifest."""
    manifest_path = WORKSPACE / "config" / "integration-manifest.yaml"
    assert manifest_path.exists(), "Integration manifest missing — run governance setup first"
    with open(manifest_path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def decisions_dir():
    """ADR directory."""
    return WORKSPACE / "data" / "decisions"
