#!/bin/bash
  set -euo pipefail
  VAULT="$HOME/vault"
  ERRORS=()

  last_commit_epoch=$(git -C "$VAULT" log -1 --format=%ct 2>/dev/null || echo 0)
  now_epoch=$(date +%s)
  age_min=$(( (now_epoch - last_commit_epoch) / 60 ))
  if [[ $age_min -gt 45 ]]; then
      ERRORS+=("L1: Last autocommit was ${age_min} minutes ago (expected < 45)")
  fi

  yesterday=$(date -d "yesterday" '+%Y-%m-%d')
  if ! git -C "$VAULT" tag -l "snapshot-${yesterday}" | grep -q .; then
      ERRORS+=("L2: Missing snapshot tag for ${yesterday}")
  fi

  if ! systemctl is-active --quiet "syncthing@idan"; then
      ERRORS+=("L3: Syncthing service is not running")
  fi

  if [[ ${#ERRORS[@]} -gt 0 ]]; then
      echo "BACKUP HEALTH: FAILED"
      printf '  - %s\n' "${ERRORS[@]}"
      exit 1
  fi

  echo "BACKUP HEALTH: OK (L1: ${age_min}m ago, L2: ${yesterday} tagged, L3: syncthing active)"
