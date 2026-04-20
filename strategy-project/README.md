# strategy-project

> Turn any consulting or strategy project into an AI-native workspace. Codex-first, with a documented Claude-compatible pattern.

## Why this exists

I've been using markdown files for the last few months to make sure my AI never loses project context between sessions. Instead of re-explaining the project every time, I keep a small set of `.md` files that the AI reads first — and it just works.

My setup has evolved. It started as one big note with constant project context. Then I split it into living documents that I'd update as the project progressed. Then I moved everything into structured markdown files inside the project folder — and that's when it clicked. The AI went from being a generic chatbot to something closer to a sharp project teammate that remembers where we left off.

I commented on a friend's post about this workflow and got 30+ inbound messages asking me to share more. So I thought I'd turn it into something the broader community can use.

This is not perfect. It's a pattern that works well for me — take it, make it yours, adapt it to your projects. If you find a better structure, open a PR.


## What it does

The skill creates a `.context/` folder and an `AGENTS.md` file that give the AI:

- **Project context** — why the project exists, the core business question, key tensions
- **Workstream awareness** — each workstream gets a living `WORKSTREAM.md` with purpose, findings, priorities, and source files
- **Stakeholder map** — who cares about what, so the AI tailors output to the right audience
- **Output standards** — how to brainstorm slides, structure memos, challenge weak logic
- **Session discipline** — read context first, update workstream files during work, refresh everything at the end

The AI reads these files before each session and works from your compiled knowledge — not from scratch every time.

## Quick start

### Install

**Option 1: Copy the skill into Codex**

```bash
git clone https://github.com/kongaharsha/claude-skills.git
cp -r claude-skills/strategy-project ~/.codex/skills/strategy-project
```

**Option 2: Any LLM**

Use the whole [`strategy-project/`](.) folder as the transferable skill package, not just [`SKILL.md`](SKILL.md). This skill depends on sibling files like `new/instructions.md`, `existing/instructions.md`, `update/instructions.md`, and `references/pattern.md`.

If your tool only accepts pasted markdown, start with [`SKILL.md`](SKILL.md) and also include the referenced instruction files for the mode you want to run.

### Use

**New project:**

```
You:    /strategy-project:new
Claude: I'll set up a new strategy project. Which folder should I create it in?
        Tell me about the project — what's the core business question? Do you have
        any scope docs or proposals I can read? What are the major workstreams?
You:    We're evaluating whether Acme should enter the European market. Here's the
        engagement letter. Main threads are market sizing, competitive positioning,
        and partnership options.
Claude: Here's what I'm planning to set up:
        Project: acme-europe-entry
        Core question: Should Acme enter European market, and what's the best path?
        Workstreams: market-sizing, competitive-positioning, partnerships
        Does this look right?
You:    Yes, go ahead
Claude: [creates everything at once — AGENTS.md, .context/, all workstream files]
```

**Existing project:**

```
You:    /strategy-project:existing
Claude: Point me to the project folder and I'll take a look.
You:    /path/to/my-diligence-project
Claude: Here's what I see — 3 workstream folders, source materials in /data,
        looks like a market entry assessment. Is my read right? A few questions...
You:    [answers in chat]
Claude: Here's what I'll add alongside your existing files: [summary].
        Does this look right?
You:    Yes
Claude: [creates context layer — nothing existing gets touched]
```

**Update (after working for a while):**

```
You:    /strategy-project:update
Claude: I've scanned the project. Here's what I found:
        - TODO & Ideas.md — 3 items done, 2 new priorities to add
        - market-sizing/WORKSTREAM.md — new analysis not captured
        - regulatory/ — folder exists but no WORKSTREAM.md. Is this a workstream?
        Want me to update all of these?
You:    Yes, and yes regulatory is a new workstream
Claude: [updates everything, shows what changed]
```

## What gets created

```text
project-root/
  AGENTS.md                            # AI instructions for this project
  .context/
    Project Context.md                 # why the project exists, key tensions
    TODO & Ideas.md                    # live working memory
    Writing & Slide Standards.md       # output quality rules
    Folder Map.md                      # navigation guide
    Stakeholder Map.md                 # who cares about what (optional)
  workstreams/
    market-sizing/
      WORKSTREAM.md                    # purpose, findings, priorities, sources
    competitive-analysis/
      WORKSTREAM.md
```

Every file is written specific to your project — not generic templates. Workstreams are optional and can be added later.

## Examples

The [`examples/`](examples/) folder has fully worked, sanitized templates for every file the skill creates — including both an `AGENTS.md` example for Codex and a `CLAUDE.md` example for Claude, plus Project Context, WORKSTREAM.md, TODO & Ideas, Writing & Slide Standards, Folder Map, and Stakeholder Map.

These are meant as inspiration. Take what's useful, skip what isn't.

## How it works in practice

**Start of a session:**
The AI reads `AGENTS.md` and `.context/` files first, then reads the `WORKSTREAM.md` for whichever workstream you're working on. It starts with your business question, not a blank slate.

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

## Using with Claude

1. The skill generates `AGENTS.md` by default — rename it to `CLAUDE.md`
2. Everything else stays the same — `.context/` folder, workstream files, the whole pattern
3. Point your Claude setup to read the `.context/` files on startup

The pattern is intentionally tool-agnostic. The main host-specific difference is the instruction filename convention.

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
