---
type: inventory
created: 2026-09-25
author: jep
---

# Laptop inventory (jep-Lenovo-V14-G3-IAP), read-only, 2026-09-25

Method: `ssh -o BatchMode=yes laptop`, listing and metadata commands only. Nothing written, moved or fetched on the laptop. Raw outputs: `C:\Users\jep\.claude\jobs\b67ccbd6\tmp\laptop-raw\` (1-du, 1-recent, 2-hits, 3-sizes, 4-more, 5-vault-svc, 6-claude).

Disk: 233 G, 41 G used, 181 G free. Home = 21 G; the rest is system (/var/lib/snapd 5.2 G, /var/log 1.1 G, /usr, /snap).
Uptime context: laptop was OFF from 2026-09-12 17:02 to 2026-09-25 11:39 (boot log). Every "stale since 09-12" finding below follows from that.

## 1. Home tree, biggest entries

| path | size | mtime | what it is | notes |
|---|---|---|---|---|
| ~/kitchen/_intake/raw/Sovereign-Nexus | 7.8 G | 2026-08-16 | full copy of the old Sovereign Nexus repo (Windows-era) | 5.9 G of it is `projects/voice-input-stt` venvs (venv311 5.2 G, venv 759 M); real content ~130 M |
| ~/Downloads | 4.5 G | 2026-09-25 | 27 files | 3.8 G `husky-cp2a...factory.zip` (Pixel 8 Pro factory image), 464 M clonezilla.iso, 191 M + 65 M Morphe (YouTube mod) zips, PNG charts, 2 phone photos (PXL_20260707, PXL_20260813), 2 m4a voice memos dated 16 Jul (not opened; predate tutoring start 08-10, still worth Idi's eye) |
| ~/root-work | 4.0 G | 2026-08-28 | Pixel rooting workbench | 3.9 G extracted factory image, Magisk/Shamiko/Zygisk zips, patched init_boot.img, probe scripts f2..f9.py, gs*.py |
| ~/snap | 1.2 G | 2026-04-12 | snap app data | firefox 1.1 G, obsidian 98 M |
| ~/.local | 854 M | 2026-03-25 | share 852 M (app data, claude binary), state 2.6 M | |
| ~/.cache | 690 M | 2026-08-28 | ms-playwright 656 M | disposable |
| ~/.claude | 657 M | 2026-09-25 | Claude Code config + transcripts | projects 365 M, jobs 175 M, plugins 108 M |
| ~/vault | 515 M | 2026-09-01 | vault git clone | inbox 472 M (CORPUS-June-2026 446 M, gitignored), .git 36 M, projects 1.5 M |
| ~/game3d | 389 M | 2026-08-23 | Word World 3D game workbench | screenshots 277 M, node_modules 57 M, ref 52 M, src 512 K, island.html 1.3 M |
| ~/tutoring-data | 291 M | 2026-08-24 | consent-gated (not listed deeper) | top level: blocklist.txt, drop/, games/, README.md, send/, sessions/, tools/, tutoring-game-D.html, tutoring-game-K.html, vault-history-pre-purge-2026-08-18.bundle |
| ~/.npm | 194 M | 2026-08-12 | npm cache | disposable |
| ~/bin | 30 M | 2026-08-17 | claude-vault (root-owned wrapper, 1.3 K), restic (30 M binary), run-agent.sh (1.9 K) | |
| ~/platform-tools (+ zip 9 M) | 22 M | 2026-08-27 | Android adb/fastboot | |
| ~/render-tools | 19 M | 2026-08-29 | Playwright probe scripts (audit, interact, gauntlet3d, _bgcheck .mjs) | |
| ~/Pictures/Screenshots | 5.6 M | 2026-08-19 | screenshots | not opened |
| ~/staging | 8 K | 2026-08-17 | morning-digest.md + .model | leftover staging |
| ~/Sync, Documents, Desktop, Videos, Music, Public, Templates | empty | 2026-03/04 | | Sync is Syncthing's default folder, empty |
| ~ loose files | <1 M | | CLAUDE.md (08-27), DESIGN.md (08-11), 4 stream_*.log / s25.log (09-09), Vervaeke/McGilchrist/Schmachtenberger transcript .txt (06-02) | |

Modified in the last 30 days (file counts): snap 10254, .npm 1707, .claude 1244, .cache 603, vault 421, .var 135, .local 60, .config 57, root-work 45, Downloads 8, .ssh 4, .android 4, .gnupg 3, render-tools 2, platform-tools 2, Pictures 2, .impeccable 2, plus loose logs (09-09), keyfile pair (09-01), .claude.json and .bash_history (09-25).

## 2. Sovereign Nexus project names on disk

Search: whole disk, excluding /proc /sys /snap /usr /var/lib, tutoring-data, node_modules, caches. 208 hits, zero inside any git object store. All hits collapse into four places:

| path | size | mtime | what it is | notes |
|---|---|---|---|---|
| ~/kitchen/_intake/raw/Sovereign-Nexus | 7.8 G | 2026-08-16 | old Nexus repo copy: projects/{Curtains, I4, XCOM, Idiverse, investment-research-system, voice-input-stt, daily-touchpoints}, data/, vault/, docs/, kernel/, nexus/, tests/ | holds a `.env` (2.2 K, not read) and `.bin/llama-b7519` binaries |
| ~/vault/inbox/CORPUS-June-2026/NEXUS BACKUP | 293 M | | second copy of the same Nexus repo, gitignored | Curtains here has 171 files vs 160 in kitchen (5+ extra phase notes: mpc-be, crystaldiskinfo, jdownloader-2, stacher7, peace.md); I4 identical |
| ~/vault/inbox/CORPUS-June-2026/Vaults BACKUPS | 152 M | | old Obsidian vault backups: Curtains/ (53 M, 162 files), XCOM/, Idiverse/ (DECADEnts 1-3, Sovereign Nexus, Inception Theory notes) | gitignored |
| ~/vault/inbox/CORPUS-June-2026/_CORPUS-MAP | 824 K | | maps: MAP-nexus-rig, -authored, -original, MAP-xcom | |
| ~/vault/projects/Cash | small | | Cash hub, Cash.base, dashboards | tracked in git |
| ~/vault/telos/work/projects/{curtains,xcom,investment-research-system,voice-input-stt}.md | small | | TELOS project stubs | tracked |
| ~/.claude/projects/-home-jep/memory/cash-portfolio-project.md | 2.5 K | 2026-08-21 | memory | |
| ~/game3d/ref/.../nexus-*.html | small | | false positive (three.js shader demos) | |

No hits for: "Kid Studio"/kidstudio, "Triple Inception", "workspace". Kid Studio does not exist on the laptop (PC-era project).

## Where are Curtains and I4?

- **Curtains**: three copies, none live, none in git.
  - `~/kitchen/_intake/raw/Sovereign-Nexus/projects/Curtains` 1.2 M, 160 files, last mtime 2025-12-27 (SYSTEM.md, backlog.json, docs, output/phases, plans, specs, truth, scripts).
  - `~/vault/inbox/CORPUS-June-2026/NEXUS BACKUP/projects/Curtains` 1.2 M, 171 files: the most complete Nexus copy (superset of kitchen by 5+ files).
  - `~/vault/inbox/CORPUS-June-2026/Vaults BACKUPS/Curtains` 53 M, 162 files: the Obsidian-vault version (different lineage, bigger, likely has media).
  - Related: ADR-008 / ADR-009 curtains-phase-0 in `.../data/decisions/`, `docs/guides/curtains-automation-protocol.md`, `tests/contracts/test_curtains_phase_0.py`, `data/state/curtains.yaml`.
  - `/workspace/projects/Curtains` (the path in memory) does not exist; memory is stale.
- **I4**: two identical copies, 316 K, 21 files, last mtime 2026-01-06: `.../Sovereign-Nexus/projects/I4` and `.../NEXUS BACKUP/projects/I4` (canon/core/i4-canon.md, presentation/concept/concept-05-fourth-inception-video-essay.md, README.md). Plus `data/i4-cycles/cycle-1.yaml` and `data/process/interesearch-2026-01-05-fourth-inception.yaml`, and "My Personal Inception Theory" notes in Idiverse / atomic_notes (2024-12-02).
- Risk: the CORPUS copies are gitignored, so they exist ONLY on the laptop disk (not on GitHub, Syncthing has no peers, restic never ran). The kitchen copy is the same disk. One disk failure loses every copy.

## 3. ~/vault git state

| item | value |
|---|---|
| branch | main, tracking origin/main |
| `git status --short` | 0 lines (clean) |
| HEAD | 1e8b4b5 2026-09-12 09:30:01 "auto: 2026-09-12 09:30" |
| unpushed (`@{u}..HEAD`) | 0 (against the local origin ref; no fetch done) |
| last autocommit | 2026-09-12 09:30 (laptop off since 09-12 17:02) |
| last nightly tag | snapshot-2026-09-12 |
| remote | git@github.com:IdanDalal/vault-backup.git |
| gitignored-but-present | inbox/CORPUS-June-2026/ (446 M), .impeccable/, .pytest_cache/, logs dir, .obsidian/workspace.json, `bunx` |
| other inbox (tracked or loose) | SELF-MAX 15 M, SUPPLIES.jpg 8.3 M, K-GAMEPLAY.png 1.3 M, K-MENU.png 864 K, MAGNA MOBSTA.jpeg, TUTORING/ 156 K, Studio Preflight.html, P4C-research.md, parts-registry-draft.md |

Note: the PC's D:\work\vault main is at 3feb087 (09-02) per session start, behind the laptop's 1e8b4b5 (09-12), with many uncommitted local edits. Relevant for the P3 write flip.

## 4. Services and schedules

| item | state | notes |
|---|---|---|
| crontab: autocommit.sh every 30 min | active | log last touched 09-12 09:30 |
| crontab: nightly-tag.sh 00:00 | active | last tag 09-12 |
| crontab: backup-health.sh every 6 h | active | 09-25 12:00 run: FAILED (L1 autocommit 18870 min old, L2 tag missing 09-24, L3 "Syncthing service is not running") |
| crontab: git gc monthly (1st, 04:00) | active | log empty |
| crontab: run-agent.sh morning-digest 09:00 daily | active | agent log last 09-12 09:01 |
| crontab: run-agent.sh loop-review Sun 09:17 | active | agent log last 09-06 |
| crontab: restic-backup Sun 02:47 | inert | guarded by ~/.config/restic/env, which is absent |
| user systemd: kitchen-telegram.service | running, enabled | `script -qfc "claude-vault --channels plugin:telegram@claude-plugins-official"`, WorkingDirectory ~/vault, Restart=on-failure; spawns bun telegram server |
| system: syncthing@jep.service | running | listens 127.0.0.1:8384 (GUI), *:22000; zero peers per CLAUDE.md. Health check's L3 "not running" is a false alarm (it checks the wrong unit) |
| system: docker.service | running | only a hello-world container (exited 6 months ago), image 25.9 kB |
| system: nordvpnd | running | nordfileshare listening on 100.67.174.198:49111 |
| system: ssh.service | running | *:22 (the PC's access path) |
| user timers | none relevant | launchpadlib, firmware-notifier only |
| llama / ollama / restic services | none | |
| kitchen/capture-hook | not installed | kitchen-capture.service + listener.py exist as files only (04-12), no such unit loaded |

## Running services that die with the laptop

1. **Telegram channel bridge** (kitchen-telegram.service): the only live Claude session on the laptop; phone capture and Telegram replies stop when it is off. Single-instance bot, collides with any second consumer.
2. **Vault autocommit + nightly tags + backup-health** (cron): only matters while the laptop is the vault writer.
3. **Morning digest (daily 09:00) and Sunday loop review** (cron via run-agent.sh): no run since 09-12 / 09-06. Not yet ported to the PC.
4. **Syncthing**: running but peerless, so nothing depends on it.
5. **ssh server**: the PC's only way in.
Already dead regardless: restic (no env), evening ping (retired 08-16), capture-hook listener (never installed), docker (idle).

## 5. Claude config on the laptop

| path | size | mtime | notes |
|---|---|---|---|
| ~/.claude/settings.json | 1.5 K | 2026-09-02 | keys: permissions, model, hooks, enabledPlugins, extraKnownMarketplaces, tui, agentPushNotifEnabled |
| hooks | | | UserPromptSubmit: `python3 ~/vault/<vault-config>/hooks/capture_hook.py`; PreToolUse: `~/.claude/hooks/vault-write-guard.sh` (5.7 K, 04-08) |
| plugins enabled | 108 M | 2026-09-25 | telegram, frontend-design, impeccable |
| settings.local.json | 1.2 K | 2026-08-27 | |
| skills | | 2026-08-18 | process-tutoring (only one) |
| output-styles | | 2026-08-27 | present |
| projects/-home-jep | 350 M | | transcripts + memory (15 files) |
| projects/-home-jep-vault | 15 M | | memory dir empty |
| jobs | 175 M | 2026-09-09 | 8 jobs |
| daemon, daemon.log | 20 K | 2026-09-09 | |
| CLAUDE.md.bak-2026-08-27 | 4.5 K | | |

Laptop memory files (mtime, size): MEMORY.md 08-30 3.9 K; cash-portfolio-project 08-21; doctor-path-warning 06-02; game-lab-project 08-21 8.9 K; idan-anonymous-downloads 07-22; idan-anti-llm-tics 06-04; parts-registry-project 08-18; pc-hq-migration 08-30; plan-only-billing 08-30; time-attention-system-project 06-10 74 K; tutoring-data-pipeline 08-20; tutoring-game-3d-project 08-23; tutoring-project 08-20 28 K; vault-github-push-outage 08-29; vault-scheduled-agents-live 07-05. All 15 already have same-named entries in the PC memory index (PC versions likely newer; mtimes not compared).

~/.local/state/vault-agent: only `cron-runner.log`, 0 bytes, 06-23. Real agent logs live in the vault's logs dir (agent-morning-digest.log 157 K 09-12, agent-loop-review.log 09-06, agent-evening-ping.log 08-16, autocommit.log, backup-health.log 09-25, nightly-tag.log 09-12).

## Secrets (path and size only, not read)

| path | size |
|---|---|
| ~/keyfile / keyfile.pub | 419 / 107 |
| ~/.ssh/id_ed25519_github (+ .pub), authorized_keys, known_hosts | 419, 107, 105, 2934 |
| ~/.config/kitchen/env | 101 |
| ~/.claude/channels/telegram/.env | 66 |
| ~/.claude/.credentials.json | 508 |
| ~/kitchen/_intake/raw/Sovereign-Nexus/.env | 2261 (old Nexus secrets; live or revoked unknown) |
| ~/.config/restic/env | absent |

## 6. ~/vault-agent

Regular file (not a symlink), 438 bytes, ASCII text, created and last modified 2026-08-18 18:28. Matches the expected dead tombstone. Not opened.

## 7. Docker

`docker ps -a`: boring_darwin (hello-world), Exited 6 months ago. `docker images`: hello-world:latest 25.9 kB. /var/lib/docker 4 K. Nothing to migrate.

## 8. Outside home

/opt: nordvpn-gui 29 M, containerd 4 K. /srv empty. /mnt/c-drive empty mount point (4 K). /media/jep empty. /home has only jep. /var/lib/snapd 5.2 G, /var/log 1.1 G (system, not content). Nothing over 500 M outside home except snapd and logs.

## Five biggest content folders (excluding venvs, caches, snaps)

1. ~/Downloads 4.5 G (mostly the 3.8 G Pixel factory zip)
2. ~/root-work 4.0 G (3.9 G extracted Pixel factory image)
3. ~/vault/inbox/CORPUS-June-2026 446 M (gitignored Nexus + vault backups, laptop-only)
4. ~/game3d 389 M (277 M screenshots)
5. ~/tutoring-data 291 M (consent-gated, stays on laptop by design)
Honorable: Sovereign-Nexus real content ~130 M once its 5.9 G of venvs are set aside.

## Open questions for Idi (not acted on)

- CORPUS-June-2026 is the only full Nexus/Curtains copy and lives on one disk, uncommitted. It needs a second home before any laptop reformat.
- ~/Downloads holds 2 July voice memos and 2 phone photos; content unknown.
- backup-health's Syncthing check reports a false failure.
