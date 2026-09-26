---
type: quest
created: 2026-09-13
author: jep
status: active
priority: high
project: daily-note-system
---

# Quest: phone captures reach jep (Pixel 8 Pro → PC vault, free, git)

Revised 2026-09-13 15:30 after reading `inbox/Guide.txt` (the Medium guide) and `inbox/Transcript.txt` (the video). Two changes from the first version: the phone app is GitSync instead of the Obsidian Git plugin, and the repo is created with a README. Everything else stands.

Done-state of the quest: a line typed or spoken into Obsidian on the phone shows up on the PC within a minute of closing Obsidian, and the next morning's `daily/Today.md` cites it as "Your words <date>". Bounded scope: captures only, one tiny repo. The main vault never syncs to the phone.

Pre-tested by jep: 0 of 6 steps (phone steps need your hands; the PC key step was denied in the background job). Probed: the PC's GitHub key is bound to `vault-backup` alone (`ssh -T` output), the vault packs to 30 MB with 10 branches, the Obsidian Git wiki's mobile page, and now the guide and transcript in full.

## What the guide and video say, and how much of it applies

1. Their method syncs the whole vault: one repo = one vault, Obsidian Git plugin plus GitHub Desktop on the desktop, GitSync on the phone. Ours syncs captures only, so the desktop half is jep pulling with plain git; no plugin, no GitHub Desktop.
2. Both say to tick "Add a README" at repo creation: "a quote unquote empty repo can trip up both the plugin and GitSync" (transcript). Adopted.
3. Both send Android to GitSync because the Obsidian Git plugin "explicitly states that mobile is not stable" and runs a JavaScript git; GitSync runs a full git. This matches the plugin wiki jep read. Adopted. Bias to name: the guide's author wrote GitSync and runs a premium tier and a giveaway. The free tier covers one repo, which is all this quest needs; premium is for multiple synced vaults, Git LFS, git-crypt.
4. GitSync auth options: GitHub OAuth in the browser, ssh key, or HTTPS token. OAuth removes the token-management step from the first version. Adopted.
5. GitSync permissions on Android: "all files access" (the author says scoped storage was too slow to use) and, for sync-on-app-open/close, an accessibility service that sees which apps open and close. The author offers Tasker as the alternative trigger and a scheduled sync down to 15 minutes. Your call at step 6.
6. The author's reliability claim, "rock solid for me for about 2 years", is one user's anecdote, the author's own.

## Why a separate repo, in three lines

1. Obsidian Git on Android runs a JavaScript git: HTTPS token only, repo size capped by phone RAM, the wiki says large repos "won't work for you". GitSync removes that limit, and the next two reasons still hold.
2. This vault is 30 MB packed plus 10 branches, a pre-commit hook the phone would skip, and PC/laptop mains that already diverge. A third writer on that repo is a conflict machine.
3. A capture repo holds a handful of small text files. The phone is its only writer, the PC only reads. Zero merge conflicts by construction.

## Phone method: options

| | A. GitSync app | B. Obsidian Git plugin | C. Termux + real git |
|---|---|---|---|
| Install | Play Store, free tier, open source | inside Obsidian, community plugin | Termux from F-Droid, `pkg install git openssh` |
| Git | full implementation | JavaScript reimplementation, flagged unstable by its own docs | full implementation |
| Auth | GitHub OAuth in the browser | fine-grained PAT only | ssh key |
| Auto sync | on Obsidian open/close (accessibility service or Tasker), scheduled ≥15 min | interval + on app open, in-app | Termux:Boot or a widget script |
| Fit | recommended by the guide, the video, and the plugin's wiki | fallback if GitSync's permissions are unacceptable | most robust, most fiddly |

**jep recommends A.** Three independent sources converge on it, one of them the competing plugin's own documentation. Say the word to overrule.

## Steps (acceptance criterion per step)

1. **Idi, browser, ~3 min.** GitHub → New repository → name `vault-captures`, Private, tick "Add a README file". Accept = the repo page shows README.md. (Today.md d1.)
2. **jep, hq session, ~5 min.** Generate `C:\Users\jep\.ssh\id_ed25519_captures` (the interactive session asks you once). Print the public key into this file under a "Key" heading. Accept = the `.pub` line sits in this file.
3. **Idi, browser, ~2 min.** Repo → Settings → Deploy keys → Add → paste the key, leave "Allow write access" unchecked. Accept = key listed; green check after step 4.
4. **jep, hq session, ~3 min.** Clone to `D:\work\captures` with `core.sshCommand` pointing at the new key. Accept = `git pull` prints "Already up to date" and the deploy-key row on GitHub shows "last used".
5. **Idi, phone, ~10 min.** Play Store → GitSync (com.viscouspot.gitsync) → Let's Go → focus: Sync mode → skip premium → notifications (optional) → "all files access" (required) → auth: GitHub, OAuth, log in in the browser → author details: your GitHub username and email → select `vault-captures` from the list → Nested clone → Documents. Then Obsidian → Open folder as vault → `Documents/vault-captures`. Accept = README.md opens in Obsidian on the phone.
6. **Idi, phone, ~5 min.** GitSync → app-based sync: enable the accessibility service, add Obsidian, sync on opened and on closed; scheduled sync once per day as a safety net. If the accessibility permission is unwelcome: scheduled sync every 15 minutes instead, or Tasker. Obsidian, in the captures vault: core plugin Daily notes on, folder `captures`, format `YYYY-MM-DD`; add "Open today's daily note" to the mobile toolbar. Accept = type one line, close Obsidian, the line is on GitHub within a minute; on the PC, `git -C D:\work\captures pull` shows it.

Then, jep: the daily-note skill reads `D:\work\captures\captures\<yesterday>.md` and `<today>.md` as source 1 for dominoes. Accept = the next Today.md cites a phone line with its date.

## Key (step 2 done 2026-09-13, jep; paste the whole line at step 3)

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHfoiBjeysG7PWOVdcv3QNBbhviwH5kbpXdHa4/pxaeD jep-captures-pc
```

Public half only; the private half stays in `C:\Users\jep\.ssh\` and never enters the vault. Step 1 closed by your word ("repo up", terminal, 2026-09-13). Step 3 closed by your word ("key added", 2026-09-13). Step 4 done 2026-09-13 17:44: `D:\work\captures` cloned with the key pinned in that repo's `core.sshCommand`; README.md present; pull receipt in the terminal. Steps 5 and 6 closed 2026-09-13 18:11 by your word ("phone up") and by receipt: three mobile syncs (6caa4b4, 88e759e, 619a7e0), `2026-09-13.md` at the repo root holding your test line, pulled clean on the PC. You skipped the `captures` subfolder; jep adopted the root: the skill reads `D:\work\captures\<date>.md`. **Quest done.** Remaining, jep only: tomorrow's Today.md cites a phone line.

## Rules that ride along

- Captures land on GitHub too. Initials only for students, as in the vault; no names, no media.
- The phone is the only writer of `vault-captures`. On the PC you dump in the terminal or under Yours in Today.md.
- Never install the Obsidian Git plugin in the captures vault; if it ever appears there, its setting "Disable on this device" goes on (guide's warning: the two conflict).
- Speaking works through Gboard voice typing inside Obsidian; no extra app.

## Risks

1. Vendor bias: the recommendation traces to GitSync's author twice (guide and video) and to the plugin wiki once. If GitSync fails on the Pixel, fall back to B, then C.
2. Permissions: all-files access plus an accessibility service. The author says the source is open and touches only the chosen folder; unverified by jep. Tasker or scheduled sync avoids the accessibility grant.
3. Same-file edits on two devices in one interval: excluded by the phone-only-writer rule.
4. Android kills background sync: open/close-triggered sync fires when you use Obsidian, which is when it matters.

Cost: you ~20 min across steps 1, 3, 5, 6; jep ~8 min across 2 and 4.
