---
type: reference
created: 2026-09-26
author: jep
status: active
---

# Old Nexus secrets + laptop credentials: revocation guide (2026-09-26)

Source file: laptop `~/kitchen/_intake/raw/Sovereign-Nexus/.env` (only copy jep can see; the CORPUS copy has no `.env`). Values were checked by prefix and length only, never printed.

## What is live, what is not

| secret | verdict | action |
|---|---|---|
| `SLACK_BOT_TOKEN` (`xoxb-`, 59 chars) | real Slack format | **revoke, step 1** |
| `SLACK_APP_TOKEN` (`xapp-`, 98 chars) | real Slack format | **revoke, step 1** |
| `OPENAI_API_KEY` (`sk-du...`, 26 chars) + docker-compose `sk-` key | dummy, labeled "DUMMY KEY" for the local Agent Zero container | none |
| n8n password + n8n API key (the JWT, also in a January handoff note) | self-hosted n8n; not running on the PC or the laptop | none; never reuse that password anywhere |
| `WEBUI_SECRET_KEY`, `SEARXNG_SECRET` | self-hosted, not running anywhere | none |
| laptop GitHub key | live, can push to the vault | **remove, step 3** (at laptop wipe) |
| Telegram bot token | live | **revoke, step 4** (only if H-c = retire) |

## Step 1. Slack tokens (5 min)

1. Open https://api.slack.com/apps and sign in to the workspace the Nexus used.
2. Click the app listed there (the Nexus digest bot). If the list is empty, the app is already gone: skip to step 2.
3. Left menu → **Basic Information** → scroll to the bottom → **Delete App** → confirm. Deleting the app kills both tokens at once.
4. Check: the app no longer appears at https://api.slack.com/apps.
5. Tell jep "Slack done".

(Keep the app instead? Then: **OAuth & Permissions** → **Revoke All OAuth Tokens**; **Basic Information** → **App-Level Tokens** → revoke the token there.)

## Step 2. Delete the secret files (jep + Idi)

1. jep deletes laptop `~/kitchen/_intake/raw/Sovereign-Nexus/.env` after "Slack done" (or the laptop wipe removes it).
2. Idi: the Nexus backup on the PC at `D:\KEEP\NEXUS BACKUP\` probably holds the same `.env` (jep has no access to `D:\KEEP`). In File Explorer: open that folder → View → Show → Hidden items → delete `.env` if present.

## Step 3. Laptop GitHub key (at laptop wipe)

1. Open https://github.com/IdanDalal/vault-backup/settings/keys (Deploy keys).
2. Find the key whose fingerprint is `SHA256:Bjnyhdyl0kHDeqtdrb6X6a1plmTjuLbXdpS6+2CTfpA`. GitHub shows fingerprints under each key title.
3. Not there? Check https://github.com/settings/keys (account SSH keys) for the same fingerprint, and also for `SHA256:evF4Pc1jZh9xXxXqj3ISD9dPCtvrHAidjtxSKkd8eYA` (the laptop's `keyfile`).
4. **Delete** each match. Do NOT delete other keys: the PC pushes with its own key.
5. Check: jep runs a test push from the PC right after.

## Step 4. Telegram bot token (only if the bot retires)

1. Telegram → chat with **@BotFather** → send `/mybots` → pick the vault bot.
2. **API Token** → **Revoke current token**. The old token dies at once.
3. Optional: **Delete Bot** instead, if no future use.

## Step 5. Laptop logins (right before the wipe)

1. On the laptop terminal: `nordvpn logout` (frees the device slot).
2. Claude login and everything else on the disk dies with the wipe; no separate step.
