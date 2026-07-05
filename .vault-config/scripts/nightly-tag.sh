#!/bin/bash
  set -euo pipefail
  VAULT="$HOME/vault"
  cd "$VAULT"
  TAG="snapshot-$(date '+%Y-%m-%d')"
  git tag -f "$TAG"
  git push origin "$TAG" --force 2>/dev/null || true

  prune_old_tags() {
      local now_epoch
      now_epoch=$(date +%s)
      git for-each-ref --format='%(refname:short) %(creatordate:unix)' refs/tags/snapshot-* | \
      while read -r tag epoch; do
          local age_days=$(( (now_epoch - epoch) / 86400 ))
          local date_part="${tag#snapshot-}"
          local dow
          dow=$(date -d "$date_part" +%u 2>/dev/null || echo "0")
          local dom
          dom=$(date -d "$date_part" +%d 2>/dev/null || echo "00")
          [[ $age_days -le 7 ]] && continue
          if [[ $age_days -le 30 ]]; then
              [[ "$dow" == "7" ]] && continue
              git tag -d "$tag" 2>/dev/null
              git push origin --delete "$tag" 2>/dev/null || true
              continue
          fi
          [[ "$dom" == "01" ]] && continue
          git tag -d "$tag" 2>/dev/null
          git push origin --delete "$tag" 2>/dev/null || true
      done
  }
  prune_old_tags
