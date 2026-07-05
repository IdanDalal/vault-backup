#!/bin/bash
  set -euo pipefail
  VAULT="$HOME/vault"
  cd "$VAULT"
  if [[ -z $(git status --porcelain) ]]; then
      exit 0
  fi
  git add -A
  git commit -m "auto: $(date '+%Y-%m-%d %H:%M')"
  git push origin main 2>/dev/null || true
