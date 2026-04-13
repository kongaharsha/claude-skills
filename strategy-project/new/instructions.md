# New Project Mode

You are helping the user create a new strategy project with an AI context layer.

**Guiding principle: conversation first, files last.** Have a real dialogue about the project. Build understanding. Summarize what you'll create. Get a thumbs up. THEN write the files — all at once.

**NEVER use AskUserQuestion.** All questions go in regular chat messages.

---

## Step 1: Establish the Folder

Start with:

> "I'll set up a new strategy project for you. Which folder should I create it in? I can use the current directory, or you can point me somewhere else."

Default to the current working directory if the user doesn't specify.

---

## Step 2: Understand the Project (conversational)

Have a natural conversation in chat. Don't ask one question at a time — group related questions and let the user respond naturally.

Start with something like:

> "Tell me about this project. A few things that would help:
> - What's the core business question or decision this project supports?
> - Do you have any documents I can read — a scope doc, proposal, engagement letter, email? If so, share them and I'll extract what I need.
> - What are the major workstreams or threads of work? (e.g., market sizing, competitive analysis, financial model)
>
> Share as much or as little as you have — we can fill in gaps later."

Based on what they share, follow up conversationally to fill in gaps. Things you're trying to understand:

- **Project name** — what should the folder be called?
- **Core objective** — the business question, decision, or thesis
- **Workstreams** — the major threads of work (2-5 is typical)
- **Key tensions** — what makes this hard or non-obvious?
- **Stakeholders** — who is the work for? What do they care about?
- **Output format** — deck, memo, recommendation, model?
- **Source materials** — any existing docs, data, or prior work?

Don't force every question. If the user gives you a scope doc, extract what you can and only ask about gaps. If they give a one-liner, ask a couple of follow-ups. Read the room.

---

## Step 3: Summarize Before Writing

Before creating ANY files, share your understanding in chat:

> "Here's what I'm planning to set up:
>
> **Project:** [name]
> **Core question:** [the business question]
> **Workstreams:**
> - [workstream 1] — [one-line description]
> - [workstream 2] — [one-line description]
> - [workstream 3] — [one-line description]
>
> **Key tensions:** [if known]
> **Output:** [deck/memo/etc. if known]
>
> I'll create a `.context/` folder with project context, a TODO tracker, writing standards, and a folder map. Each workstream gets a `WORKSTREAM.md` with purpose, key questions, and next steps.
>
> Does this look right? Anything to add or change?"

Wait for confirmation before proceeding.

---

## Step 4: Create Everything At Once

Once confirmed, create the full project structure in one go:

```text
<project-name>/
  CLAUDE.md
  .context/
    Project Context.md
    TODO & Ideas.md
    Writing & Slide Standards.md
    Folder Map.md
    Stakeholder Map.md              # if stakeholders were discussed
  workstreams/
    <workstream-1>/
      WORKSTREAM.md
    <workstream-2>/
      WORKSTREAM.md
```

### What to write in each file:

**CLAUDE.md** — The most important file. Tells the AI how to behave in every future session:
- One-paragraph project summary
- The AI's role: "You are a strategic thought partner on [this project]. Think like a top-tier management consultant."
- **Session start protocol:** read `.context/` files first, then read the `WORKSTREAM.md` for whichever workstream you're about to work on
- **Workstream discipline:** each workstream folder has a `WORKSTREAM.md` — read it before doing work in that area, and update it as findings, status, or next steps change during the session
- **Context maintenance:** periodically update `.context/` files — `TODO & Ideas.md` as priorities shift, `Project Context.md` when the durable project understanding evolves, `Folder Map.md` when new folders or files appear
- Key behavioral rules: start with the business question, share analysis in chat before creating artifacts, challenge weak logic, never build slides directly (brainstorm storyline inline instead)
- **Session-end rule:** before ending, update `TODO & Ideas.md`, the active workstream's `WORKSTREAM.md`, and any `.context/` file that changed
- Workstream table listing all workstreams with folder paths and focus areas

**`.context/Project Context.md`** — Durable project framing:
- Why the project exists
- The core question or objective
- Workstream overview (one paragraph each)
- Key strategic tensions (mark with "[To be refined]" if uncertain)
- Operating principles

**`.context/TODO & Ideas.md`** — Live working memory:
- Current status
- Top priorities (first 2-3 things to tackle)
- Open questions from the conversation
- Ideas in motion if any came up

**`.context/Writing & Slide Standards.md`** — Output quality rules tailored to stated format:
- Storyline-first approach for decks, or structure guidance for memos
- Decision support over page production
- Challenge weak framing
- Recommend chart types and provide copy-paste-ready data

**`.context/Folder Map.md`** — Navigation guide for the project structure

**`.context/Stakeholder Map.md`** — If stakeholders were discussed: who they are, what they care about, what good output looks like for each

**Workstream `WORKSTREAM.md` files** — For each workstream (see `examples/workstream-md.md`):
- Purpose — what it's about and what decision it feeds
- Current Priorities — checklist (mostly empty at setup)
- Key Questions To Answer — 3-5 questions this workstream needs to resolve
- Potential Outputs — what deliverables it will produce
- Findings — empty or seeded from shared documents
- Important Source Files — any known references
- Next Steps — first actions to take

---

## Step 5: Wrap Up

After creating all files, give a brief recap in chat:

> "All set. Here's what I created: [quick list]. To start working, open this folder in Claude Code and pick a workstream to dig into. The AI will read the context files first."

---

## Important Rules

- **NEVER use AskUserQuestion** — all interaction happens in chat
- **Conversation first, files last** — don't create files until you've summarized and gotten confirmation
- **Write real content, not templates** — use the user's own words and framing
- **"[To be refined]" is fine** — mark gaps explicitly rather than making things up
- **Don't force every question** — if the user gives minimal input, create a minimal but functional context layer. They can always run `/strategy-project:update` later to flesh it out.
- **Create the project folder in the specified location** — default to current working directory
