---
type: research
created: 2026-11-11
author: jep
project: workshop
---

# Worktree audit, 2026-11-11

Read-only. 23 worktrees under `.claude/worktrees`: **18 safe to remove, 3 to keep, 2 live.** Safe ones hold 10985 files, 1247 MB. Nothing was removed.

A worktree is a second working copy of the vault on its own branch; every background job makes one.

## How each was judged

- **Remote**: the branch's last commit compared with git ls-remote --heads origin (live).
- **In main**: the branch's last commit is an ancestor of `main` (8feeaeb).
- **Only here**: commits reachable from neither `main` nor the remote branch. Removing the folder keeps the local branch, so these commits survive until the branch itself is deleted.
- **Modified / untracked / ignored**: files on disk compared with the branch's committed tree by content hash; ignore status from the vault's own ignore rules.
- **Nowhere else**: modified, untracked or ignored files with no byte-identical file at the same path in the main vault. These are what a removal would destroy.
- **SAFE** = removing the folder destroys nothing: no file nowhere else, untouched for 36 hours. **KEEP** = at least one file nowhere else. **LIVE** = a file changed within 36 hours, or this session's own.
- The same 31 tracked files hash differently from their commit in every worktree, this one included. Each is byte-identical to the main vault's copy, so none counts as nowhere else; the cause was not investigated.

## Verdicts

| # | Worktree | Verdict | Last commit | Last file change | Remote | In main | Only here | Modified | Untracked | Ignored | Nowhere else | Files | MB |
|--:|---|---|---|---|---|---|--:|--:|--:|--:|--:|--:|--:|
| 1 | `aimv-posse-cut` | SAFE | 2026-10-14 | 2026-10-14 | same | no | 0 | 31 | 0 | 1 | 0 | 535 | 65 |
| 2 | `aimv-kc-prompt-v4` | SAFE | 2026-10-15 | 2026-10-15 | absent | no | 20 | 31 | 0 | 1 | 0 | 539 | 65 |
| 3 | `kc-video-build` | SAFE | 2026-10-16 | 2026-10-16 | same | no | 0 | 31 | 0 | 1 | 0 | 543 | 65 |
| 4 | `aimv-engine-probe` | SAFE | 2026-10-17 | 2026-10-17 | absent | no | 6 | 31 | 0 | 1 | 0 | 551 | 66 |
| 5 | `kc-video-v5` | SAFE | 2026-10-17 | 2026-10-17 | absent | no | 3 | 31 | 0 | 1 | 0 | 546 | 66 |
| 6 | `aimv-phase0` | SAFE | 2026-10-18 | 2026-10-18 | same | no | 0 | 31 | 0 | 1 | 0 | 555 | 66 |
| 7 | `aimv-notes` | SAFE | 2026-10-19 | 2026-10-19 | absent | no | 6 | 31 | 0 | 1 | 0 | 557 | 67 |
| 8 | `aimv-typography` | SAFE | 2026-10-21 | 2026-10-21 | absent | no | 4 | 31 | 0 | 1 | 0 | 560 | 68 |
| 9 | `local-agents-research` | SAFE | 2026-10-22 | 2026-10-22 | same | no | 0 | 31 | 0 | 1 | 0 | 572 | 69 |
| 10 | `social-activities-research` | SAFE | 2026-10-22 | 2026-10-22 | absent | yes | 0 | 31 | 4 | 1 | 0 | 576 | 69 |
| 11 | `aimv-escalation-pass` | SAFE | 2026-10-27 | 2026-10-27 | absent | no | 14 | 31 | 0 | 1 | 0 | 584 | 69 |
| 12 | `aimv-polish-pass` | SAFE | 2026-10-31 | 2026-10-31 | same | no | 0 | 31 | 0 | 1 | 0 | 585 | 69 |
| 13 | `kc-release` | SAFE | 2026-10-31 | 2026-10-31 | same | no | 0 | 31 | 0 | 1 | 0 | 598 | 70 |
| 14 | `pa-round4` | SAFE | 2026-11-04 | 2026-11-04 | same | no | 0 | 31 | 0 | 1 | 0 | 780 | 76 |
| 15 | `repo-scout-2026-11-04` | SAFE | 2026-11-04 | 2026-11-04 | differs | no | 4 | 31 | 0 | 1 | 0 | 684 | 75 |
| 16 | `pa-proof-fixes` | SAFE | 2026-11-05 | 2026-11-05 | same | no | 0 | 31 | 0 | 1 | 0 | 784 | 76 |
| 17 | `pa-wave4-research` | SAFE | 2026-11-07 | 2026-11-07 | same | no | 0 | 31 | 0 | 1 | 0 | 791 | 76 |
| 18 | `xcom-slot-rules-1029` | SAFE | 2026-11-09 | 2026-11-09 | same | no | 0 | 31 | 0 | 1 | 0 | 645 | 71 |
| 19 | `cash-console-v3` | KEEP | 2026-09-14 | 2026-10-05 | absent | no | 3 | 34 | 0 | 10 | 13 | 342 | 45 |
| 20 | `cash-sale-2026-10-20` | KEEP | 2026-10-23 | 2026-10-23 | absent | no | 2 | 31 | 0 | 2 | 1 | 570 | 68 |
| 21 | `aimv-video2-infra` | KEEP | 2026-11-04 | 2026-11-04 | same | no | 0 | 31 | 0 | 2 | 1 | 679 | 74 |
| 22 | `pa-v2-notes` | LIVE | 2026-11-10 | 2026-11-10 | same | no | 0 | 31 | 0 | 14 | 13 | 807 | 225 |
| 23 | `workshop-2026-11-11` | LIVE | 2026-11-11 | 2026-11-11 | absent | no | 3 | 54 | 14 | 1 | 37 | 883 | 78 |

## Notes per worktree

- `aimv-kc-prompt-v4` (SAFE): its branch holds 20 commit(s) that are neither on the remote nor in main; the branch stays.
- `aimv-engine-probe` (SAFE): its branch holds 6 commit(s) that are neither on the remote nor in main; the branch stays.
- `kc-video-v5` (SAFE): its branch holds 3 commit(s) that are neither on the remote nor in main; the branch stays.
- `aimv-notes` (SAFE): its branch holds 6 commit(s) that are neither on the remote nor in main; the branch stays.
- `aimv-typography` (SAFE): its branch holds 4 commit(s) that are neither on the remote nor in main; the branch stays.
- `aimv-escalation-pass` (SAFE): its branch holds 14 commit(s) that are neither on the remote nor in main; the branch stays.
- `repo-scout-2026-11-04` (SAFE): its branch holds 4 commit(s) that are neither on the remote nor in main; the branch stays.
- `cash-console-v3` (KEEP): 13 file(s) found nowhere else; its branch holds 3 commit(s) that are neither on the remote nor in main; the branch stays.
  - `projects/Cash/dashboard/data/probe/companies.png` (2209.3 KB)
  - `projects/Cash/dashboard/data/probe/overview.png` (1978.6 KB)
  - `projects/Cash/dashboard/data/probe/analysis.png` (1799.1 KB)
  - `projects/Cash/dashboard/data/probe/odds.png` (1516.3 KB)
  - `projects/Cash/dashboard/data/probe/lab.png` (1474.4 KB)
  - and 8 more
- `cash-sale-2026-10-20` (KEEP): 1 file(s) found nowhere else; its branch holds 2 commit(s) that are neither on the remote nor in main; the branch stays.
  - `projects/Cash/dashboard/__pycache__/transition.cpython-314.pyc` (16.6 KB)
- `aimv-video2-infra` (KEEP): 1 file(s) found nowhere else.
  - `projects/AIMV/kit/lexicon/__pycache__/lexicon.cpython-314.pyc` (31.8 KB)
- `pa-v2-notes` (LIVE): a file changed 18 h ago.
  - `review-room-clips/06-games.mp4` (16772.4 KB)
  - `review-room-clips/08-kitchen.mp4` (16755.2 KB)
  - `review-room-clips/12-outro.mp4` (16280.4 KB)
  - `review-room-clips/10-verse4.mp4` (14981.0 KB)
  - `review-room-clips/02-class.mp4` (12927.9 KB)
  - and 8 more
- `workshop-2026-11-11` (LIVE): this session.
  - `projects/workshop/tools/hub_check.py` (8.3 KB)
  - `projects/workshop/research/worktree-audit-2026-11-11.md` (6.2 KB)
  - `projects/workshop/sources/No Boilerplate - Obsidian for Learning II Process.md` (2.8 KB)
  - `projects/workshop/sources/No Boilerplate - Obsidian for Learning III Projects.md` (2.7 KB)
  - `projects/workshop/sources/Odysseas - Obsidian The King of Learning Tools.md` (2.6 KB)
  - and 32 more

## What removal would be

For the SAFE rows, on Idi's word: `git worktree remove <path>` per row, run by jep from the hq session. Every branch stays; only the folders go. The KEEP rows wait until their files are copied out or ruled disposable.
