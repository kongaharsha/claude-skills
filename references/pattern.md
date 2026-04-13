# Consulting Project Context Pattern — Reference

This is the full pattern specification. Skills reference this when generating project files.

## Operating Model

1. Keep raw source materials in the project folders
2. Summarize durable context into a small number of markdown files
3. Let the LLM use those markdown files as the first layer of context
4. Feed durable insights, clarified definitions, and refined guidance back into the markdown layer over time

## Root Structure

```text
project-root/
  CLAUDE.md                          # AGENTS.md if using Codex
  .context/
    Project Context.md
    Competitive Landscape.md        # optional
    TODO & Ideas.md
    Writing & Slide Standards.md
    Folder Map.md
  workstreams/
    example-workstream/
      WORKSTREAM.md
      Findings.md
```

## File Specifications

### CLAUDE.md (root) — or AGENTS.md for Codex

The main instruction file for the AI assistant. Must define:

- Who the assistant is in the project
- How it should think (top-tier management consultant, independent thought partner)
- What files it must read first
- How it supports analysis and slide work
- Session-end behavior

Key behavioral rules:
- Think like a top-tier management consultant or strategic analyst
- Be an independent thought partner, not a passive assistant
- Start with the business question, not the file
- Share early analysis in chat instead of defaulting to markdown artifacts
- Never build slides directly; brainstorm storyline and page structure inline
- Recommend chart type and provide copy-paste-ready data when helpful
- Check for workstream-local summaries before doing detailed work

### .context/Project Context.md

Durable project-level context:
- Why the project exists
- What decision or objective it supports
- Major workstreams
- Key strategic tensions
- Core operating principles

NOT for: meeting notes, detailed task tracking, temporary working notes.

### .context/Competitive Landscape.md

External threat or market context (only when competition matters):
- Competitor or market themes
- What is changing structurally
- Why it matters and implications
- What to monitor

Should be a threat model, not a long fact dump.

### .context/TODO & Ideas.md

Live working memory (keep short and crisp):
- Current status
- Top priorities
- Open questions
- Storyline ideas in motion
- Blockers or key data needed

Must NOT become an exhaustive backlog.

### .context/Writing & Slide Standards.md

Communication and output quality rules:
- Writing style
- Slide brainstorming rules (storyline-first)
- Lede standards
- Visualization guidance
- What to avoid

Key rules:
- Decision support over page production
- No fixed slide structure for every page
- Align on storyline before slide-level drafting
- Respond inline so user can build the slide
- Challenge weak framing or logic

### .context/Folder Map.md

Project navigation guide:
- What top-level folders are for
- Where the freshest direction usually lives
- Where outputs and scratch work belong
- How root context differs from local workstream context

## Workstream-Level Pattern

Most workstreams need:
- One or two markdown files summarizing current state
- Examples: WORKSTREAM.md, Summary.md, Findings.md

These summarize: current findings, key open questions, next steps, local decisions or caveats.

## Session Protocol

### Start of session
1. Read root CLAUDE.md (or AGENTS.md)
2. Read .context/ files
3. Identify relevant workstream
4. Check workstream for local markdown summaries
5. Check for optional local AGENTS.md
6. Begin work

### During work
- Read the active workstream's WORKSTREAM.md before diving in
- Update WORKSTREAM.md as findings, status, or next steps change
- Begin with the business question
- Share early insights in chat
- Avoid creating artifacts too early
- Distinguish facts from inference and working hypotheses
- Recommend analytical cuts and chart types
- Provide copy-paste-ready data when useful

### During deck/slide work
- Never build slides directly
- Align on storyline first
- Help define slide purpose, lede, structure, evidence
- Keep work inline in chat

### Periodically
- Update .context/TODO & Ideas.md as priorities shift
- Update .context/Project Context.md when durable understanding evolves
- Update .context/Folder Map.md when new folders or files appear
- Run a full update scan when the project feels out of sync

### End of session
Update durable files that changed:
- .context/TODO & Ideas.md for priorities and blockers
- The active workstream's WORKSTREAM.md
- .context/Project Context.md only if durable understanding changed

## Anti-Patterns

- Duplicating context across many places
- Turning .context/ into a dump of raw notes
- Forcing every workstream to have full local context
- Letting TODO files become giant backlogs
- Making the assistant a passive note-taker
