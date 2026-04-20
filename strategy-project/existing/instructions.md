# Existing Project Mode

You are helping the user add the AI context layer to a project folder that already has work in it.

**Guiding principle: scan first, discuss in chat, write files last.** Never touch existing files. Have a conversation about what you found before creating anything.

**NEVER use AskUserQuestion.** All questions go in regular chat messages.

---

## Step 1: Get the Folder

Start with:

> "Point me to the project folder and I'll take a look. What's the path?"

If the user is already in the project directory, offer to use the current directory.

---

## Step 2: Scan the Folder

Once you have the path, read it systematically:
1. Directory structure (top-level and one level deep)
2. Any existing AI config (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, etc.)
3. Key files: READMEs, markdown summaries, project docs, proposals
4. What looks like workstreams (folders with analytical work)
5. Source material locations (data, raw docs, downloads)
6. Any documents or attachments that reveal project context

---

## Step 3: Discuss What You Found (conversational)

Share your findings in chat and have a conversation. Don't just list files — share what you think the project is about:

> "Here's what I see in your project:
>
> **Folder structure:** [summary of what's there]
> **What looks like workstreams:** [list folders that seem like workstreams]
> **Source materials:** [where raw docs and data seem to live]
> **What I think this project is about:** [your best read based on folder names, docs, and any files you read]
>
> A few questions:
> - Is my read on the project right? What's the core business question?
> - Are those workstreams correct, or should I group things differently?
> - Any key context I'm missing that's not in the files?
> - Who are the key stakeholders and what do they care about?"

Let the user respond naturally. Follow up conversationally to fill gaps. Don't ask one question at a time.

---

## Step 4: Summarize Before Writing

Before creating ANY files, share your plan in chat:

> "Here's what I'll add to your project (nothing existing gets touched):
>
> **New files:**
> - `AGENTS.md` — AI instructions tailored to this project
> - `.context/Project Context.md` — [one-line summary of what it'll say]
> - `.context/TODO & Ideas.md` — [current status you inferred]
> - `.context/Writing & Slide Standards.md` — output quality rules
> - `.context/Folder Map.md` — navigation guide for this folder structure
> - `workstreams/[name]/WORKSTREAM.md` — for each workstream: [list them]
>
> Does this look right? Anything to adjust?"

Wait for confirmation before proceeding.

---

## Step 5: Create the Context Layer

Once confirmed, create everything in one go. Base all content on what you found in the folder AND what the user told you in chat.

**`AGENTS.md`** — Tailored to this specific project:
- Reference the actual folder structure and key files
- Note which existing files contain valuable context
- Instruct the AI to check existing work before starting new analysis
- **Session start protocol:** read `.context/` files first, then read the `WORKSTREAM.md` for whichever workstream you're about to work on
- **Workstream discipline:** each workstream folder has a `WORKSTREAM.md` — read it before doing work in that area, and update it as findings, status, or next steps change during the session
- **Context maintenance:** periodically update `.context/` files — `TODO & Ideas.md` as priorities shift, `Project Context.md` when durable understanding evolves, `Folder Map.md` when new folders or files appear
- Standard behavioral rules: thought partner, business question first, challenge weak logic, storyline-first for decks
- **Session-end rule:** before ending, update `TODO & Ideas.md`, the active workstream's `WORKSTREAM.md`, and any `.context/` file that changed
- If there's an existing `AGENTS.md` or `CLAUDE.md`, ask the user whether to merge or replace

**`.context/Project Context.md`** — Synthesize from what you found + what the user said:
- Pull context from existing docs, READMEs, or summaries
- Note what you inferred vs. what the user confirmed
- Flag gaps with "[To be refined]"

**`.context/TODO & Ideas.md`** — Reflect actual current state:
- What's in progress based on folder contents
- Known next steps if you can infer them
- Open questions

**`.context/Writing & Slide Standards.md`** — Sensible defaults

**`.context/Folder Map.md`** — Map the real folder structure:
- What each top-level folder contains
- Where the freshest work lives
- Where source material vs. compiled output belongs

**Workstream `WORKSTREAM.md` files** — For each workstream folder (see `examples/workstream-md.md`):
- Purpose, current priorities, key questions
- Findings — summarize existing work found in that folder
- Important source files — reference actual files found
- Next steps — inferred from current state

**Optional files** — create if they came up in conversation:
- `.context/Stakeholder Map.md` (see `examples/stakeholder-map.md`)

---

## Step 6: Wrap Up

After creating all files, give a brief recap in chat:

> "Context layer is in place. Here's what I created: [quick list]. Your existing files are untouched. To start working, the AI will read the context files first, then dive into whichever workstream you pick."

---

## Important Rules

- **NEVER use AskUserQuestion** — all interaction happens in chat
- **NEVER modify, move, rename, or delete existing files**
- **Scan first, discuss, then write** — no files until you've talked it through
- **Base content on what actually exists** — read the folder before writing about it
- **Be honest about gaps** — "I didn't find details on X, you may want to add this"
- **If there's already an `AGENTS.md` or `CLAUDE.md`** — ask in chat before replacing. Offer to merge.
- **Keep it proportional** — a small project gets a small context layer
