# strategy-project

> Turn any consulting or strategy project into an AI-native workspace. Works with Claude Code and Codex.

## Why this exists

I've been using markdown files for the last few months to make sure my AI never loses project context between sessions. Instead of re-explaining the project every time, I keep a small set of `.md` files that the AI reads first — and it just works.

My setup has evolved. It started as one big note with constant project context. Then I split it into living documents that I'd update as the project progressed. Then I moved everything into structured markdown files inside the project folder — and that's when it clicked. The AI went from being a generic chatbot to something closer to a sharp project teammate that remembers where we left off.

I commented on a friend's post about this workflow and got 30+ inbound messages asking me to share more. So I thought I'd turn it into something the broader community can use.

This is not perfect. It's a pattern that works well for me — take it, make it yours, adapt it to your projects. If you find a better structure, open a PR.

Inspired by [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the idea that LLMs should maintain persistent, compounding knowledge artifacts rather than re-deriving answers from raw sources every time.

## What it does

The skill creates a `.context/` folder and a `CLAUDE.md` file that give the AI:

- **Project context** — why the project exists, the core business question, key tensions
- **Workstream awareness** — each workstream gets a living `WORKSTREAM.md` with purpose, findings, priorities, and source files
- **Stakeholder map** — who cares about what, so the AI tailors output to the right audience
- **Output standards** — how to brainstorm slides, structure memos, challenge weak logic
- **Session discipline** — read context first, update workstream files during work, refresh everything at the end

The AI reads these files before each session and works from your compiled knowledge — not from scratch every time.

## Quick start

### Install

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

**Option 1: Download the `.skill` file (fastest)**

Download [`strategy-project.skill`](strategy-project.skill) → in Claude Code, go to Settings → Skills → Add Skill → drop the file. Done.

**Option 2: Clone the full repo**

```bash
git clone https://github.com/kongaharsha/claude-skills.git ~/.claude/skills/claude-skills
```

**Option 3: Any LLM**

Copy the content of [`strategy-project.skill`](strategy-project.skill) into your conversation as context. The pattern is tool-agnostic — works with ChatGPT, Codex, Gemini, or anything that reads markdown.

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
    Stakeholder Map.md                 # who cares about what (optional)
    Competitive Landscape.md           # threat model (optional)
  workstreams/
    market-sizing/
      WORKSTREAM.md                    # purpose, findings, priorities, sources
    competitive-analysis/
      WORKSTREAM.md
```

Every file is written specific to your project — not generic templates. Workstreams are optional and can be added later.

## What a good WORKSTREAM.md looks like

Each workstream gets a living document that the AI reads before working and updates as it goes:

```markdown
# Workstream: Market Sizing

## Purpose
What this workstream is about and what decision it feeds.

## Current Priorities
Checklist of what's in flight and what's done.

## Key Questions To Answer
The 3-5 questions this workstream needs to resolve.

## Potential Outputs
What deliverables this workstream will produce.

## Findings
What's been learned so far — with sources and caveats.

## Important Source Files
Links to the raw documents, data, and analysis this workstream uses.

## Next Steps
What happens next.
```

See [`examples/WORKSTREAM.md`](examples/WORKSTREAM.md) for a fully worked example.

## Examples

The [`examples/`](examples/) folder has sanitized, fully worked templates for every file the skill creates:

| File | What it shows |
|---|---|
| [`CLAUDE.md`](examples/CLAUDE.md) | How to instruct the AI for your project |
| [`Project Context.md`](examples/Project%20Context.md) | Durable project framing — the "why" and strategic tensions |
| [`WORKSTREAM.md`](examples/WORKSTREAM.md) | A living workstream document with findings and sources |
| [`TODO & Ideas.md`](examples/TODO%20%26%20Ideas.md) | Live working memory — priorities, open questions, blockers |
| [`Writing & Slide Standards.md`](examples/Writing%20%26%20Slide%20Standards.md) | Output quality rules — ledes, storylines, chart guidance |
| [`Folder Map.md`](examples/Folder%20Map.md) | Navigation guide for the project structure |
| [`Stakeholder Map.md`](examples/Stakeholder%20Map.md) | Who cares about what — tailoring output to audience |
| [`Competitive Landscape.md`](examples/Competitive%20Landscape.md) | Threat model — not a fact dump |

These are meant as inspiration. Take what's useful, skip what isn't.

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
6. **Living context** — the knowledge base evolves with the project, not just at setup

## Contributing

This is a pattern, not a finished product. If you find a better structure for your projects, a missing file type, or a workflow improvement — open a PR.

## License

MIT
