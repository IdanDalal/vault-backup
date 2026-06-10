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
| Capture hook (`c:` via Telegram → daily note) | Soldier → vault | **Built** (ADR-007), dormant |
| Daily digest | Emissary → Master | Designed; needs schedule |
| Health/sleep log (evening numbers → frontmatter → base) | Body → ledger | Daily template fields exist; needs the evening channel |
| Calendar (orders for future selves) | General → Soldiers | **Absent — the keystone.** "Biophysical contract where attention commits time." |
| Routing lens (modified Eisenhower) | inbox → calendar/kanban | Absent. Dated → calendar column; undated → kanban by priority. A lens, never a maintained file. |
| Weekly Loop Review (SELF-MAX zones 6–7) | Environment → Master | **The new ritual. The piece whose absence killed every prior system.** |
| Atomic-note staging (drip) | Corpus/dumps → Master's hand | New; governed below |

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

## Dormant switches — say the word and it goes live

- **"wake the digest"** → schedule the morning digest.
- **"wake the evening ping"** → schedule the evening 3-numbers prompt (Telegram).
- **"calendar"** → pick the substrate (plan-section in daily note vs. dedicated file) and the routing lens activates with it.
- **"stage one"** → first atomic-note candidate appears in `inbox/`, with context, awaiting your hands.
