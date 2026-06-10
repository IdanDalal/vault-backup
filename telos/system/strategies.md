# Strategies

*Habits, routines, methods — now understood as frameworks.*

---

## The Reframe (2026-01-19)

**Previous state:** "I don't understand them."

**New understanding:** Strategies ARE frameworks. The deep-dive research revealed that effective strategies are externalized systems, not internal willpower. The question isn't "what strategy should I use?" but "what system generates the signals I need?"

---

## Core Pattern: Signal-Generating Systems

From TELOS Core Insight: The variable isn't discipline — it's **external signal**.

**Therefore:** Good strategies create forcing functions, not motivation.

| Willpower-Based (Fails) | Signal-Based (Works) |
|-------------------------|----------------------|
| "I will exercise daily" | Gym buddy expects me at 7am |
| "I will write every day" | Daily progress shared with dad |
| "I will learn Spanish" | No signal → abandoned |

---

## The PDAC Loop

*Compounding Engineering — never do the same task twice.*

```
    ┌─────────┐
    │  PLAN   │ ← Define task, success criteria, constraints
    └────┬────┘
         ↓
    ┌─────────┐
    │DELEGATE │ ← Hand to agent/tool
    └────┬────┘
         ↓
    ┌─────────┐
    │ ASSESS  │ ← Evaluate against criteria
    └────┬────┘
         ↓
    ┌─────────┐
    │ CODIFY  │ ← Extract reusable patterns
    └────┴────┘
```

**Each Phase:**
- **PLAN:** Clear success criteria, explicit constraints, input/output spec
- **DELEGATE:** Choose agent/tool, provide context, set boundaries
- **ASSESS:** Compare output to criteria, identify gaps, note surprises
- **CODIFY:** Extract patterns that worked, document failures, update skills

**Goal:** Each task builds capability for next task.

---

## The Flow Loop (Lighten / Level / Lean)

*Diagnosing and fixing stuck states.*

### Phase 1: LIGHTEN
- Reduce resistance & friction
- Question: "What's heavier than needed?"
- Actions: Remove, delegate, automate obstacles

### Phase 2: LEVEL
- Find appropriate challenge
- Not too easy (boredom) ↔ too hard (anxiety)
- Question: "What challenge fits my skill?"

### Phase 3: LEAN
- Apply minimum effective effort
- Don't force, guide
- Question: "Where can I do less and achieve more?"

**Laminar Flow (Desired):** Smooth, efficient, sustainable
**Turbulent Flow (Failure):** Chaotic, wasteful, burnout risk

---

## 12-Factor Agents (Reliability Principles)

*Software engineering for AI agents.*

| Factor | Principle | Application |
|--------|-----------|-------------|
| 1 | Natural Language → Tool Calls | Convert intent to function |
| 2 | Own Your Prompts | Make prompts visible/editable |
| 3 | Own Context Window | Debug context fully |
| 4 | Tools as Structured Output | Decouple intent from execution |
| 5 | Unified Execution State | Single source of truth |
| 6 | Launch/Pause/Resume | Serialize state for interruptibility |
| 7 | Contact Humans as Tools | `ask_human(q)` pattern |
| 8 | Own Control Flow | Explicit loops, not framework magic |
| 9 | Compact Errors into Context | Error → model learns, retries |
| 10 | Small Focused Agents | One agent, one job |
| 11 | Trigger from Anywhere | CLI, API, cron, webhook |
| 12 | Observability | Log everything |

---

## The 80/20 Rule

*Code-first, prompts-second.*

**80% Deterministic Code** (Python, CLI tools, logic)
**20% Prompts** (for genuinely fuzzy parts)

Principle: "If you can write it in Python, don't write it in English."

---

## Cult of Done (Execution Philosophy)

1. Three states only: Not knowing → Action → Completion
2. Everything is a draft
3. No editing stage
4. Pretend you know → almost same as knowing
5. Abandon if > 1 week old with no progress
6. Done unlocks other things
7. Failure counts as done
8. Done is engine of more

**Application:** Ship first, refine via feedback loop.

---

## Proactive Agency Levels

| Level | Definition | Trust Required |
|-------|------------|----------------|
| 1: Observation | Notice patterns without being asked | Low |
| 2: Personalization | Adapt based on observed patterns | Medium |
| 3: Timeliness | Act at right moment without prompting | High |

**Progression:** Start at 1, earn trust, graduate to 3.

---

## Personal Strategy Stack

1. **Capture:** Slack DM (zero friction)
2. **Route:** IntentClassifier (automatic)
3. **Store:** Obsidian vault (single source of truth)
4. **Review:** Daily digest (Tap on Shoulder)
5. **Execute:** Claude Code sessions with TELOS priming
6. **Codify:** Session insights → vault notes

---

## Applied: Current Projects

| Project | Strategy | Signal |
|---------|----------|--------|
| jep | PDAC loop + vault integration | Session completion |
| investment-research-system | External accountability | Dad reviews progress |
| Curtains | Documentation-first | Published artifact |

---

## Red Team Protocol

*Weekly self-verification — "Penetration test your soul."*

### Purpose

From Deep Dive Tutor 11: "The AI looked at his file and basically said: 'Hey, you claim your narrative is about spiritual impact and artistry, but your logs show you obsessively checking your YouTube analytics every single hour. You're measuring your success by a metric that directly contradicts your stated values.'"

**The Problem:** Human friends are too polite. The AI doesn't care about your feelings — it cares about data consistency.

### Schedule

**When:** Sunday evening (weekly)
**Duration:** 30-60 minutes
**Output:** `system/audit.md` updated

### Inputs

1. `TELOS.md` (stated identity)
2. `system/challenges.md` (daily battles)
3. Week's session logs / activity data
4. Any captured notes from the week

### The Prompt

```markdown
## Red Team Analysis Request

**Context Files Attached:**
- TELOS.md (my stated vision, values, reputation)
- This week's logs/activity

**Task:**
Analyze the discrepancy between:
1. What I CLAIM to value (narratives)
2. What I ACTUALLY did (logs)

**Output Required:**
1. **Contradictions Found** — Where behavior contradicts stated values
2. **Blind Spots Identified** — What am I avoiding seeing?
3. **Drift Percentage** — How far from stated mission this week? (0-100%)
4. **One Uncomfortable Truth** — The thing I don't want to hear
5. **Recommended Correction** — One specific action for next week

**Constraint:** Do not soften the feedback. Clinical analysis only.
```

### Anti-Sycophancy Architecture

The AI is trained to be agreeable. Counter this by:

1. **Objective Metrics** — "Did I ship the artifact? Yes/No." Not "I felt productive."
2. **External Validation** — Audience retention rate, not self-assessment
3. **Explicit Anti-Softening** — "Do not hedge. State probability or gap directly."
4. **Cold Hard Feedback Loop** — Environment feedback > self-reported feelings

### Red Team Questions (Manual Backup)

If AI unavailable, ask yourself:

1. What am I avoiding right now by doing what I'm doing?
2. If someone filmed the last week, what would they conclude I actually want?
3. What's the most embarrassing reason I haven't changed?
4. What would my 10-year-older self say about this week?
5. What's the elephant I'm not naming?

### Integration with PDAC

```
Red Team (Sunday) → Identify gaps
    ↓
PLAN (Monday) → Adjust week's focus
    ↓
DELEGATE → Execute with agents
    ↓
ASSESS → Compare to criteria
    ↓
CODIFY → Extract patterns
    ↓
Red Team (Next Sunday) → Verify codified patterns actually applied
```

### Execution Mode (Codified 2026-01-22)

**Hybrid approach** (validated in first run):

| Step | Actor | Action |
|------|-------|--------|
| 1 | AI | Gather data (git commits, session logs) |
| 2 | AI | Run Red Team prompt against TELOS |
| 3 | Human | Validate findings (accept/adjust) |
| 4 | AI | Populate `audit.md` with validated data |

**Why hybrid:**
- AI catches patterns human might miss
- Human validates uncomfortable truths land correctly
- Codifies via `audit.md` template

**Frequency:** Weekly (Sunday evening). Confirmed.

---

## Simulated Student Testing

*Formal verification for teaching — test curricula before recording.*

### The Pattern

From Deep Dive Tutor 11: "She can create a simulated student, a digital twin of a total beginner. She can then feed her lesson plan to this sim student and ask the AI: 'Based on this lesson, what specific misconceptions is this student likely to form?'"

### Protocol

```
1. Define lesson plan / explanation
2. Create simulated student profile:
   - Level: Apprentice (0-30% understanding)
   - Background: [specific gaps]
   - Learning style: [visual/verbal/kinesthetic]

3. Feed lesson → Ask AI:
   "Given this lesson and this student profile:
   - What misconceptions will form?
   - Where will confusion occur?
   - What prerequisite is missing?
   - Confidence that student reaches 80% understanding: X%"

4. Iterate lesson based on predictions
5. Only then: record/publish
```

### Application to jep

Before any tutor session:
1. Simulate the student's current state
2. Predict where the conversation will get stuck
3. Pre-load alternative explanations for predicted sticking points

**Shifts teaching from guessing game to science.**

---

## Session vs Always-On Trade-off

*Two modes for second brain operation.*

| Mode | Description | Pros | Cons |
|------|-------------|------|------|
| **Always-On** | Zapier/n8n watches inbox, processes automatically | Mental load offloaded, async, never forget | Less control, can't shape during processing |
| **Session-Based** | Claude Code session processes inbox on demand | Full control, can query and iterate | Requires sitting down, manual trigger |

### Recommendation: Hybrid

- **Always-On** for: Capture, initial routing, low-confidence flagging
- **Session-Based** for: Synthesis, deep thinking, weekly review, Red Team

### Implementation

```
Slack capture → Always-On bouncer (routes, flags low-confidence)
                    ↓
              Obsidian vault (storage)
                    ↓
         Session-Based synthesis (when you sit down)
                    ↓
              Materialized Views (daily digest)
```

---

*Expanded from "I don't understand" to actionable frameworks: 2026-01-19*
*Red Team Protocol added: 2026-01-22*
*Original: 2026-01-01*
