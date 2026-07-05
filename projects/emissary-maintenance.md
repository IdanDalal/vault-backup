---
type: project
created: 2026-06-10
author: jep
status: active
priority: high
---

# Emissary Maintenance System — "Communication Between My Selves"

Purpose: externalize administrative load so Idi governs (Master/General) while jep administrates (Emissary/Adjutant). Scope: all of life, with tutoring as one live loop among several.

**The one design criterion, applied to every component:** *it must run even if Idi does nothing today.* Any component that fails this gets redesigned or cut. This is the single variable that separates this build from the three dead reincarnations (Jan / April / Sovereign Nexus) — same vault, opposite fuel source.

---

## The Ratio (the contract)

### Idi's side — the General (total budget: ≤ 15 min/day)

| When | What | Cost |
|---|---|---|
| Morning | Read the daily digest. Today's orders are already written. | ≤ 2 min |
| Anytime | Dump — thoughts via Telegram `c:`, files/links into `inbox/`. No sorting, no formatting. | ~0 willpower |
| Evening | Three numbers (sleep hrs, energy 1–5, one drift/win note) + any captures. | ≤ 3 min |
| Weekly | **The Loop Review** — one 30-min sitting. The only place orders get written. | 30 min/wk |
| Ad lib | Type ONE staged atomic note when it's ripe. Never bulk. | his call |

### jep's side — the Adjutant (standing, scheduled, willpower-free)

- Compile the **daily digest**: today's orders (calendar + kanban), overdue items, stale inbox, signal trends.
- **Stage atomic-note candidates** from Idi's dumps — one at a time, contextualized, into `inbox/`. Idi types the note; jep never does.
- Maintain **bases**: health/sleep trends, Eisenhower routing view, project kanban.
- Prep the **weekly Loop Review**: assemble the feedback (what was ordered vs. what happened, what the environment sent back) so the General sits down to *judge*, never to gather.

---

## Channels (the message bus between selves)

| Channel | Direction | Status |
|---|---|---|
| Capture hook (`c:` via Telegram → daily note) | Soldier → vault | **Built** (ADR-007) |
| Daily digest | Emissary → Master | **LIVE 2026-06-10** — daily 09:03, full digest to `daily/digests/`, compact version to Telegram. Harness cron (renews weekly); durable home = `.vault-config/prompts/`, draft staged in `inbox/`. |
| Evening ping (3 numbers: sleep / energy / drift-or-win line) | Emissary → Soldier → ledger | **LIVE 2026-06-10** — daily 21:53 via Telegram. Reply lands as captures; morning digest lifts numbers into frontmatter. |
| Health/sleep device data (Pixel 8 Pro + Pixel Watch 2 / Fitbit) | Body → ledger | Evening ping = daily signal. Device history = periodic **Google Takeout / Fitbit export dumped into `inbox/`**; jep parses into ledger + base (parser gets built against the first real export). Exports in, never cloud APIs. |
| Calendar (orders for future selves) | General → Soldiers | **LIVE 2026-06-10** — `bases/calendar.base` (Today's Orders / This Week / Overdue / All Dated). An order = any note with `due:` frontmatter + status enum. |
| Routing lens (modified Eisenhower) | inbox → calendar/kanban | **Active with the calendar:** dated dumps → jep creates a `type: task` note with `due:`; undated → kanban by `priority`. A lens, never a maintained file. |
| Weekly Loop Review (SELF-MAX zones 6–7) | Environment → Master | **The new ritual. The piece whose absence killed every prior system.** Cadence: pick the weekly 30-min slot. |
| Atomic-note staging (drip) | Corpus/dumps → Master's hand | Dormant — wake with **"stage one"** |

## The Loop (from SELF-MAX, stripped and generalized)

Desire (1) → Environment (2) → Mentality (3) → Behavior (4/5) → Situation (6) → Feedback (7) → back to 1.

The weekly review walks 6 → 7 → 1: *What did the environment send back? What does it change? What are next week's orders?* Consciousness inserted at the feedback step — the exact point where the loop historically breaks.

---

## Governance invariants (unchanged at any scope)

1. **Atomic notes: Idi types every character.** jep stages candidates with context; the transformation into a note happens in Idi's hands. Foundational, no exceptions.
2. **No bulk re-mining.** The Idiverse has been mined three times; the corpus map exists (`_CORPUS-MAP/`). Asset transformation is a *drip*: demand-driven, one staged candidate at a time, pulled when something live needs it or Idi reaches for it.
3. `telos/`, `atomic-notes/`, `templates/`, `resources/` stay read-only to agents.
4. **Drain-don't-chase:** dormant channels wake only on Idi's explicit word. The Emissary never pings uninvited.

## Data ownership (mostly already won)

Substrate is local markdown/JSONL under git + nightly tags + Syncthing + restic offsite (ADR-003). Remaining inflows to repatriate over time: NotebookLM sources, phone media, any cloud-resident lists. Rule: take *exports into the vault*, never build on cloud APIs.

---

## Switches

- ~~"wake the digest"~~ → **LIVE** (daily 09:03)
- ~~"wake the evening ping"~~ → **LIVE** (daily 21:53)
- ~~"calendar"~~ → **LIVE** (`bases/calendar.base`; substrate = `due:` frontmatter notes)
- ~~"stage one"~~ → **STAGED 2026-06-10**: candidate #1 = the Telescope × Bowstring second atomic note (substance fully crystallized in `inbox/seed-telescope-x-bowstring.md`, carving shape appended). Next: **"stage two"** after it's typed.
- ~~Loop Review slot~~ → **SUNDAY MORNING** (Idi's call 2026-06-10: Thu/Fri party nights make Sunday the felt week boundary — and the Hebrew calendar agrees). Prep packet lands 09:17 Sundays; the 30-min sitting follows at his pace.

## Maintenance log

- **2026-06-10 — backup layer found dead and repaired.** Crontab still pointed at `/home/idan/*` (nonexistent since the home-dir rename); autocommit, nightly tags, and backup-health had been silent since 2026-04-06. Fixed paths → `/home/jep`. `.gitignore` was corrupted (botched heredoc) → rewritten; `inbox/CORPUS-June-2026/` (446MB backup dump) excluded from git. Catch-up commit `3f7a52f`: 75 files, **including the first-ever commit of `telos/`**.
- **2026-06-10 (later) — runner BUILT, restic INSTALLED, drip STARTED.** `~/bin/run-agent.sh` created and tested end-to-end (fail-safe SKIP without a blessed prompt; full sudo→setpriv→headless-claude chain verified). Cron lines live for morning-digest / evening-ping / loop-review — all skipping silently until Idi saves the three prompt files into `.vault-config/prompts/` (the placement IS the approval; full instructions in `inbox/standing-prompts-draft.md`). Restic 0.19.0 installed to `~/bin` (had never been installed); weekly cron Sunday 02:47, self-gated on `~/.config/restic/env` existing — template at `~/.config/restic/env.template`, credentials are Idi's hand. Loop Review slot locked: **Sunday morning**, prep packet 09:17.
- **Remaining open:** (1) Idi fills restic `env` + runs `restic init` once. (2) Idi saves the 3 prompts → tells jep → jep deletes the interim harness jobs (else everything arrives twice). (3) Candidate #1 awaits carving. (4) Cron-level runner logs go to `~/.local/state/vault-agent/` (the write-guard rightly blocks jep from aiming redirects at `.vault-config/logs/`; the runner itself logs there at runtime, like autocommit — move the redirects if you want them unified).
