# Frameworks

*Reference: The architectural patterns powering jep and the second brain.*

---

## The 8 Building Blocks (Source 24)

*Complete personal AI infrastructure requires all 8.*

| # | Block | Purpose | Implementation |
|---|-------|---------|----------------|
| 1 | **Dropbox** | Frictionless capture | Slack DM to self |
| 2 | **Sorter** | AI classifier | IntentClassifier in nexus |
| 3 | **Form** | Schema/contract | VaultProcessor Note dataclass |
| 4 | **Filing Cabinet** | Source of truth | vault/main-notes/ |
| 5 | **Receipt** | Audit trail | JSONL with UUID |
| 6 | **Bouncer** | Confidence filter | Thread review system |
| 7 | **Tap on Shoulder** | Proactive digest | Daily/weekly Slack summary |
| 8 | **Fix Button** | Trivial correction | Thread reply corrections |

**All 8 are implemented in the Slack → Vault pipeline.**

---

## Context Engineering

*The highest-leverage skill in LLM systems.*

### The Context Window Map

```
┌─────────────────────────────┐
│    CONTEXT WINDOW           │
├─────────────────────────────┤
│  System Prompt  ← Stable    │  SMART ZONE
│  Retrieved Context ← Smart  │  (high value/token)
│  Recent History ← Smart     │
├─────────────────────────────┤
│  Old History ← Dumb         │  DUMB ZONE
│  Verbose Outputs ← Dumb     │  (low value/token)
└─────────────────────────────┘
```

### Techniques

| Technique | Application |
|-----------|-------------|
| Progressive Disclosure | Start minimal, add on demand |
| Context Compaction | Summarize old turns |
| Retrieval Augmentation | Pull relevant docs at query time |
| Structured Prompts | Markdown sections > wall of text |
| Few-Shot Priming | Examples > explanations |

**Key Metric:** If you can't articulate what's in context and WHY, you're not doing it right.

---

## Thread-Based Engineering

*Six types for different workloads.*

| Thread | Characteristics | Use Case |
|--------|-----------------|----------|
| **P-Thread** | Parallel, independent | Research 3 libraries simultaneously |
| **C-Thread** | Chained, sequential (A→B→C) | Research → Design → Implement |
| **F-Thread** | Fusion, converging | 3 research threads → unified recommendation |
| **B-Thread** | Big, heavyweight (hours) | Full codebase refactoring |
| **L-Thread** | Long, extended temporal scope | Continuous monitoring |
| **Z-Thread** | Zero-touch, fully autonomous | Automated CI/CD |

---

## Zettelkasten Principles

*The knowledge management foundation.*

### Core Principles
- **Atomic Notes:** One idea per note, 200-500 words, self-contained
- **Hyperlinks over Folders:** Links = organic network; folders = rigid hierarchy
- **Bottom-Up Organization:** Don't plan upfront; let structure emerge
- **Combinatorial Explosion:** 1000 notes = 499,500 possible connections

### Note Types
1. **Fleeting Notes:** Quick captures, temporary
2. **Literature Notes:** From sources, referenced
3. **Permanent Notes:** Your synthesized thoughts
4. **Index Notes:** Navigation hubs for topics

---

## DSPy Framework

*Declarative AI programming.*

### Three Core Concepts

**1. Signatures (Declarative Intent)**
```python
signature = "question, context -> answer: str"
```

**2. Modules (Logical Structure)**
```python
class MyAnalyzer(dspy.Module):
    def forward(self, text: str):
        return self.analyze(text=text)
```

**3. Optimizers (Auto-Improve Prompts)**
```python
optimizer = dspy.MIPROv2(metric=accuracy_metric)
```

---

## Domain Memory Pattern

*Externalizing agent knowledge.*

```
┌─────────────────────────────┐
│     DOMAIN MEMORY           │
│  (Obsidian Vault)           │
└─────────────┬───────────────┘
              ↓
┌─────────────────────────────┐
│  Initializer Agent          │
│  (Load context, prime)      │
└─────────────┬───────────────┘
              ↓
┌─────────────────────────────┐
│  Worker Agent               │
│  (Execute, report)          │
└─────────────────────────────┘
```

**Principle:** Externalize goals, internalize skills. System tells WHAT; agent knows HOW.

---

## Systems Thinking (5 + 3 Pillars)

### Five Extroverted Pillars (External Focus)
1. **People:** Who are the actors? What do they want?
2. **Communication:** How does information move?
3. **Measurements:** What metrics drive behavior?
4. **Outcomes:** What actually happens vs. intended?
5. **Networks:** Connection topology

### Three Introverted Skills (Internal Focus)
1. **Structure:** Decomposition & composition
2. **Clarity:** Precise definitions
3. **Purpose:** What is this FOR?

---

## Pedagogical Techniques (jep Tutor Design)

| Technique | Description | Application |
|-----------|-------------|-------------|
| **Scaffolding** | Just enough support, no more | Remove as competence builds |
| **Cognitive Friction** | Intentional difficulty | Prevents brain atrophy |
| **Socratic Questioning** | Questions > answers | Forces articulation |
| **Chunking** | Pattern compression | Accelerates expertise |
| **Crappy Elf** | AI writes draft, human edits | Preserves agency |
| **Pedagogy of Struggle** | Learning requires struggle | Sweet spot = "desirable difficulty" |

---

## Materialized Views

*Compile vault data into smart-zone context.*

```yaml
job: daily_context_compilation
schedule: "0 6 * * *"
steps:
  - compile: recent_notes
    source: "vault/**/*.md modified:>24h"
    output: "views/recent_activity.md"
  - compile: active_projects
    source: "projects/**/status.md"
    output: "views/project_states.json"
retention: 7_days
```

---

*Created: 2026-01-19*
*Source: Deep-dive extraction from 37 NotebookLM transcripts*
