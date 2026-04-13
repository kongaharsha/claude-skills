# strategy-project

> Turn any consulting or strategy project folder into an AI-native workspace. Three commands — works with Claude Code and Codex.

Most AI tools are great at writing code. But if you're a consultant, strategy professional, or anyone doing project-based analytical work, the AI doesn't know your project context, your workstreams, or how you think about the problem.

**strategy-project** fixes this. It creates a lightweight markdown knowledge base inside your project folder so the AI acts like a strategic thought partner — not a generic chatbot.

## What it does

The skill creates a `.context/` folder and a `CLAUDE.md` file that give the AI:

- **Project context** — why the project exists, the core business question, key tensions
- **Workstream awareness** — what each thread of work is about, current state, open questions
- **Output standards** — how to brainstorm slides, structure memos, challenge weak logic
- **Session discipline** — read context first, update durable files at the end

The AI reads these files before each session and works from your compiled knowledge — not from scratch every time.

## Quick start

### Install

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

**Option 1: Download the skill file**

Download from the [latest release](../../releases/latest) and drop it into Claude Code.

**Option 2: Clone into your skills directory**

```bash
git clone --depth 1 https://github.com/kongaharsha/strategy-project.git ~/.claude/skills/strategy-project
```

Then add to your project's `CLAUDE.md`:

```markdown
## strategy-project
Available skills: /strategy-project:new, /strategy-project:existing, /strategy-project:update
```

### Use

**New project:**

```
You:    /strategy-project:new
Claude: Do you have a scope document or proposal? Or just tell me the goal.
You:    Here's the engagement letter [attaches doc]
Claude: [extracts context, creates .context/ folder and CLAUDE.md]
Claude: Core context layer is set up. Want to add workstreams now, or start working?
You:    Let's add workstreams
Claude: What are the major threads? e.g., market sizing, competitive analysis...
```

**Existing project:**

```
You:    /strategy-project:existing
Claude: Where's the project folder?
You:    /path/to/my-diligence-project
Claude: [reads folder structure, identifies workstreams and source materials]
Claude: I'll add a .context/ folder alongside your existing files. Nothing gets moved.
Claude: [creates context layer based on what's already there]
```

**Update (after working for a while):**

```
You:    /strategy-project:update
Claude: [scans all folders, workstream files, source materials, conversation context]
Claude: Context layer audit:
        - TODO & Ideas.md — 3 items done, 2 new priorities
        - market-sizing/WORKSTREAM.md — new analysis not captured
        - regulatory/ — folder exists but no WORKSTREAM.md
        Want me to update all of these?
You:    Yes, go ahead
Claude: [updates everything, shows what changed]
```

## What gets created

```text
project-root/
  CLAUDE.md                            # AI instructions for this project
  .context/
    Project Context.md                 # why the project exists, key tensions
    TODO & Ideas.md                    # live working memory
    Writing & Slide Standards.md       # output quality rules
    Folder Map.md                      # navigation guide
    Competitive Landscape.md           # when competition matters (optional)
  workstreams/
    market-sizing/
      WORKSTREAM.md                    # state, findings, next steps
    competitive-analysis/
      WORKSTREAM.md
```

Every file is written specific to your project — not generic templates. Workstreams are optional and can be added later.

## How it works in practice

**Start of a session:**
The AI reads `CLAUDE.md` and `.context/` files first, then reads the `WORKSTREAM.md` for whichever workstream you're working on. It starts with your business question, not a blank slate.

**During work:**
The AI updates the active workstream's `WORKSTREAM.md` as findings and status change. It shares early insights in chat, distinguishes facts from hypotheses, recommends analytical cuts, and provides copy-paste-ready data when useful.

**During deck work:**
The AI never builds slides directly. It helps you brainstorm storyline, define slide purpose and lede, suggest chart types — all inline so you build the actual slide.

**End of session:**
The AI updates `TODO & Ideas.md`, the active `WORKSTREAM.md`, and any `.context/` file that changed.

**Periodic refresh:**
Run `/strategy-project:update` to do a full scan — it reads every folder, every document and attachment, reconciles everything with the context layer, and shows you what's out of date before fixing it.

## Who this is for

- **Management consultants** — strategy, ops, org design, transformation projects
- **Corporate strategy teams** — internal consulting, strategic planning, M&A diligence
- **Product strategists** — competitive analysis, market entry, product roadmaps
- **Anyone doing project-based analytical work** where context accumulates across sessions

## Using with Codex

If you use OpenAI Codex:

1. The skill generates `CLAUDE.md` — rename it to `AGENTS.md` (Codex convention)
2. Everything else stays the same — `.context/` folder, workstream files, the whole pattern
3. Point your Codex system prompt to read the `.context/` files on startup

The pattern is tool-agnostic. Only the instruction file name changes.

## Design principles

1. **Get to value fast** — create the core context layer quickly, refine later
2. **Small and high-signal** — a few well-maintained files beat many stale ones
3. **Compiled knowledge, not raw notes** — source material stays separate
4. **The AI is a thought partner** — it challenges weak logic, not just takes notes
5. **Decision support over documentation** — optimize for better decisions, not more docs

## Contributing

Found a pattern that works well for your projects? Open a PR.

## License

MIT
