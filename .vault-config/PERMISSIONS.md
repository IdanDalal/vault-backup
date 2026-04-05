# Vault Permissions

## Why Friction Exists

This vault is a second brain — a system where a human thinks, and AI agents augment that thinking. The value of the vault comes from one place: **Idi's own words, connections, and decisions**. Everything else is scaffolding.

An agent that writes freely is not helping. It is replacing the process that makes the vault worth having. The atomic notes directory exists because thinking happens in the act of writing — not in the output. An agent that generates an atomic note has stolen a rep from the gym. The note might look correct. The understanding never formed.

But an agent that *reads* atomic notes, *finds connections between them*, and *surfaces those connections* for Idi to act on — that agent is a force multiplier. It sees patterns across hundreds of notes that no human can hold in working memory simultaneously. It doesn't write the insight. It points at where the insight lives, and Idi writes it.

**The principle**: Every permission in this document is designed to maximize the agent's ability to *create, preserve, and add value* — while making it architecturally impossible to *devalue* the vault through careless or convenient writes.

Convenience is not a value here. The path of least resistance — generating content, auto-filling notes, writing where it's fastest — is precisely the path that hollows out a second brain over time. These constraints exist because both human and AI default to ease, and ease compounds into emptiness.

---

## Permission Boundaries

### Read-Only Directories

> [!danger] These directories are off-limits for all AI write operations.
> The write MCP server (`vault-write`) has no filesystem path to these directories. This is not a rule — it is a physical constraint enforced by the symlink architecture. See ADR-002.

| Directory | What Lives Here | Why It Is Sacred |
|---|---|---|
| `atomic-notes/` | Zettelkasten notes — one idea per note, in Idi's words | **Thinking happens in the writing.** Every character is typed by a human. AI-generated atomic notes are worthless — they bypass the cognitive process that creates understanding. |
| `templates/` | Templater templates for daily notes, projects, tasks | **Scaffolding defines workflow.** Templates shape how Idi thinks each day. An agent that modifies a template modifies the human's thinking pattern without consent. |
| `resources/` | Reference material — articles, book notes, clippings | **Curation is a human judgment.** What enters the reference shelf reflects what Idi considers worth preserving. Agents don't curate — they hoard. |
| `attachments/` | Images, PDFs, media files embedded in notes | **Binary files are not agent territory.** Modifications are irreversible and unauditable in git diff. |
| `.vault-config/` | Scripts, prompts, tests, logs, this file | **Operational infrastructure is not runtime-writable.** Agent prompts are pre-approved. Scripts are versioned. An agent that modifies its own governance has no governance. |

### Writable Directories

> [!tip] These directories are accessible via the write MCP server (`vault-write`), through symlinks in `~/vault-agent/`.

| Directory | What Lives Here | What Agents Should Do | What Agents Must Not Do |
|---|---|---|---|
| `daily/` | Daily notes, `digests/` subdirectory | Generate daily/weekly digests in `digests/`. Update task sections in daily notes. | Modify Morning Intentions or Evening Reflection sections — those are Idi's words. |
| `projects/` | Active efforts with deadlines | Create task notes, update `status` fields, add progress entries | Delete project notes. Change `priority` or `due` without explicit instruction. |
| `areas/` | Ongoing life domains (health, finance, career) | File relevant information, create task notes | Restructure areas. Rename or merge area notes. |
| `bases/` | `.base` view files + agent reports | Generate and maintain `.base` files. Write reports and analysis. | Modify `.base` files that Idi has manually customized (check `author` property). |
| `inbox/` | Quick capture landing zone | Create new inbox items from Telegram or scheduled prompts | Route items out of inbox — that's Idi's decision during review. |

### The Read MCP Server

> [!info] The read MCP server (`vault-read`) can access the **entire vault** — all directories, including read-only ones.

This is the agent's primary tool for creating value:

- **Search atomic notes** to find connections Idi hasn't seen yet
- **Read across directories** to build context for digests and reports
- **Surface patterns** — recurring themes, orphaned notes, clusters of related ideas
- **Reference templates** to understand the expected structure of new notes

Reading everything. Writing only where permitted. That is the model.

---

## Frontmatter Conventions

Every note has a `type` property. This is the primary filter for all Bases views.

### Rules for Agents

1. **Never omit `type` or `created`** — these are required on every note
2. **Never invent new `status` values** — the enum is closed: `todo`, `in-progress`, `waiting`, `done` for tasks; `active`, `paused`, `done`, `archived` for projects
3. **Always set `author`** — use `jep` for Claude Opus, `Agent <name>` for sub-agents
4. **Never fabricate wikilinks** — only link to notes that exist. Verify before linking.
5. **Respect `priority` semantics** — `high` and `low` only. These drive Eisenhower placement. Wrong priority = wrong quadrant = broken dashboard.

### The `author` Field

| Value | Meaning |
|---|---|
| `Idi` | Written by the human. **Agents never set this value.** |
| `jep` | Written by Claude Opus (the primary vault-keeper agent) |
| `Agent <name>` | Written by a named sub-agent |

If `author: Idi` exists on a note, the agent must treat it as read-only regardless of which directory it lives in. Idi's words in a writable directory are still Idi's words.

---

## Value Creation Guidelines

> [!important] Constraints are half the picture. The other half is what agents *should actively do* to make the vault more valuable.

### Connect

- When writing a digest or report, **link to relevant atomic notes** using `[[wikilinks]]`
- Surface connections between atomic notes that share themes but aren't yet linked
- Reference project notes from daily digests when progress was made that day

### Contextualize

- When filing an inbox item, add context: where it came from, why it might matter, which area or project it relates to
- In weekly reviews, note which areas received attention and which were neglected

### Preserve

- Never delete notes — set `status: archived` or `status: done` instead
- When updating a note, append rather than overwrite. History matters.
- If a conflict arises between convenience and data preservation, choose preservation.

### Illuminate

- Daily digests should highlight **what changed** and **what it connects to** — not just list files
- Flag orphaned notes (notes with zero inbound links) as candidates for Idi's review
- Surface overdue tasks and stale inbox items — make the invisible visible

---

## Enforcement Architecture

These permissions are not prompt instructions. They are enforced by the filesystem.

```
~/vault/                    Obsidian vault root + git repo
~/vault-agent/              Write MCP server root (contains ONLY symlinks)
    daily/      -> ~/vault/daily/
    projects/   -> ~/vault/projects/
    areas/      -> ~/vault/areas/
    bases/      -> ~/vault/bases/
    inbox/      -> ~/vault/inbox/
```

The write MCP server points at `~/vault-agent/`. It physically cannot traverse to `atomic-notes/`, `templates/`, `resources/`, `attachments/`, or `.vault-config/` because those paths do not exist in `~/vault-agent/`.

**This is not trust. This is architecture.** A well-intentioned agent with a bug is indistinguishable from a malicious one. The system does not rely on intentions.

---

## Verification

These boundaries are tested by `test_second_brain.py::TestMCPPrivilegeSeparation`:

- Every writable directory has a symlink in `~/vault-agent/`
- Every read-only directory is absent from `~/vault-agent/`
- No unexpected entries exist in `~/vault-agent/`
- No symlinks are broken

The backup system (ADR-003) provides rollback if any boundary is ever breached:
- **L1**: Git autocommit every 30 minutes — revert any change within minutes
- **L2**: Nightly snapshot tags — restore any day's exact state
- **L3**: Syncthing — real-time copy on desktop and phone
- **L4**: Restic to Backblaze B2 — encrypted offsite recovery

---

> [!quote] The measure of a system is not what it allows, but what it makes difficult for the right reasons.

---

*Governed by: ADR-002 (vault architecture), ADR-003 (backup strategy)*
*Contract test: `test_second_brain.py::TestMCPPrivilegeSeparation`*
*Last reviewed: 2026-04-04*
