---
name: strategy-project
description: >
  Set up a consulting or strategy project for AI-assisted work.
  Run /strategy-project:new to create a new project — point to a folder and have a conversation about your project before any files are created.
  Run /strategy-project:existing to add AI context to an existing project folder — scans your folder and discusses what it finds before writing anything.
  Run /strategy-project:update to refresh an existing project's context layer — scans everything, shows what's stale, and fixes it.
---

# Strategy Project Setup

This skill helps consultants and strategy professionals set up project folders that make Claude Code or Codex work like a sharp strategic thought partner — not a passive assistant.

The core idea: create a small markdown knowledge base (`.context/` folder) inside your project folder. Raw source materials stay separate. The AI reads the compiled context layer first, then dives into specifics.

---

## Critical Behavioral Rules

**These apply to ALL modes:**

1. **NEVER use AskUserQuestion or any tool-based prompts.** All questions must be asked conversationally as regular chat messages. The user should never have to type in a separate input box.
2. **Conversation first, files last.** Build understanding through chat. Summarize what you plan to create. Get confirmation. THEN write files.
3. **Folder first.** Every mode starts by establishing which folder to work in.

---

## Which Mode?

Read the instructions file for the mode the user is asking for. If unclear, ask in chat.

| User says… | Mode | Instructions |
|---|---|---|
| "new project", "set up a project", "start fresh" | **New** | `new/instructions.md` |
| "existing project", "add context to this folder", "I already have a project" | **Existing** | `existing/instructions.md` |
| "update", "refresh", "sync", "clean up context" | **Update** | `update/instructions.md` |

---

## What Gets Created

New and Existing modes produce this structure, tailored to the user's specific project:

```text
project-root/
  CLAUDE.md                            # main AI instructions
  .context/
    Project Context.md                 # why the project exists, key tensions
    TODO & Ideas.md                    # live working memory
    Writing & Slide Standards.md       # output quality rules
    Folder Map.md                      # navigation guide
    Stakeholder Map.md                 # optional — who cares about what
  workstreams/
    <workstream-name>/
      WORKSTREAM.md                    # living doc: purpose, findings, priorities, sources
```

### WORKSTREAM.md Structure

Each workstream's `WORKSTREAM.md` should include:
- **Purpose** — what this workstream is about and what decision it feeds
- **Current Priorities** — checklist of what's in flight and what's done
- **Key Questions To Answer** — the 3-5 questions this workstream needs to resolve
- **Potential Outputs** — what deliverables this workstream will produce
- **Findings** — what's been learned so far, with sources and caveats labeled
- **Important Source Files** — links to raw documents, data, and analysis
- **Next Steps** — what happens next

See `examples/workstream-md.md` for a fully worked example.

---

## CLAUDE.md — What It Must Tell the AI

The generated `CLAUDE.md` is the most important file. It must instruct the AI to:

1. **On session start:** read `.context/` files, then check the relevant workstream's `WORKSTREAM.md`
2. **During work:** read and update the active workstream's `WORKSTREAM.md` as findings, status, or next steps change
3. **Periodically:** keep `.context/` files current — update `TODO & Ideas.md` as priorities shift, update `Project Context.md` when durable understanding changes
4. **On session end:** update `TODO & Ideas.md`, the active `WORKSTREAM.md`, and any `.context/` file that changed

The AI should treat `WORKSTREAM.md` as the living document for each workstream — not just a setup artifact.

---

## Design Principles

1. **Conversation first** — understand the project through dialogue before writing any files
2. **Small and high-signal** — a few well-maintained files beat many stale ones
3. **Compiled knowledge, not raw notes** — source material stays separate
4. **The AI is a thought partner** — it challenges weak logic, not just takes notes
5. **Decision support over documentation volume** — optimize for better decisions
6. **Living context** — the context layer evolves with the project, not just at setup

---

## Codex Instructions

If the user is setting up for OpenAI Codex instead of Claude Code:
- Replace `CLAUDE.md` with `AGENTS.md` (Codex convention)
- Everything else stays the same — `.context/` folder, workstream files, the whole pattern
- Note this in the generated files so the user knows

---

## Reference Material

The full pattern specification is in `references/pattern.md`. All modes reference it when generating files.
