  #!/bin/bash
  set -euo pipefail
  source "$HOME/.config/restic/env"
  restic backup "$HOME/vault" \
      --exclude '.obsidian/workspace*.json' \
      --exclude '.trash/' \
      --exclude '.vault-config/logs/' \
      --verbose
  restic forget \
      --keep-daily 30 \
      --keep-weekly 26 \
      --keep-monthly 12 \
      --keep-yearly 3 \
      --prune
  restic check --read-data-subset=10%
