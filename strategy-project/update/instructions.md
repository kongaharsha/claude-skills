# Update Mode — Refresh the Project Context Layer

You are helping the user bring their project's `.context/` folder and workstream files up to date.

**Guiding principle: scan everything, discuss in chat, then update.** Show the user what's stale before fixing it.

**NEVER use AskUserQuestion.** All questions go in regular chat messages.

---

## Step 1: Verify the Project Has Context

First, check that the current folder (or a folder the user points to) has a `.context/` folder and `CLAUDE.md`. If not:

> "This folder doesn't have a `.context/` folder yet. Want me to set one up? You can run `/strategy-project:new` for a fresh project or `/strategy-project:existing` to add context to what's already here."

Only proceed if the context layer exists.

---

## Step 2: Full Project Scan

Read the project systematically:

1. **CLAUDE.md** — understand the current instructions and project framing
2. **`.context/` files** — read every file in the context folder
3. **All workstream folders** — read every `WORKSTREAM.md`, plus scan for new files, analysis outputs, notes, or data that appeared since the last update
4. **Source materials** — scan for new documents, attachments, PDFs, spreadsheets, or data files anywhere in the project
5. **Conversation context** — if there's an active conversation, review what was discussed, decided, or discovered
6. **Orphan folders** — look for folders that exist but have no `WORKSTREAM.md` (may be new workstreams)

Build a mental inventory of what's current vs. what's stale.

---

## Step 3: Discuss What You Found

Present a concise audit in chat — what's out of date and what you'd fix:

> "I've scanned the project. Here's what I found:
>
> **Up to date:**
> - [files that look current]
>
> **Needs updating:**
> - `.context/TODO & Ideas.md` — 3 items are done, 2 new priorities should be added
> - `workstreams/market-sizing/WORKSTREAM.md` — new analysis in the folder isn't captured in findings
> - `.context/Folder Map.md` — 2 new folders not mapped
>
> **New stuff to add:**
> - `workstreams/regulatory/` — folder exists but has no WORKSTREAM.md. Is this a workstream?
>
> Want me to update all of these? Or pick specific ones?"

Wait for the user to respond before making changes.

---

## Step 4: Update the Files

For each file that needs updating:

### `.context/TODO & Ideas.md`
- Remove completed items
- Add new priorities discovered from the scan
- Update current status
- Refresh open questions — remove answered ones, add new ones
- Keep it short and crisp

### `.context/Project Context.md`
- Update if the project's durable understanding has changed
- Add new workstreams that were created since last update
- Refine strategic tensions based on new findings
- Surgical updates only — don't rewrite what's still accurate

### `.context/Folder Map.md`
- Add new folders and files
- Remove references to deleted folders
- Update descriptions of where the freshest work lives

### `.context/Competitive Landscape.md`
- Update if new competitive intel appeared in any workstream
- Create if competition has become relevant and it doesn't exist yet

### `.context/Writing & Slide Standards.md`
- Usually doesn't need updating unless the output format or audience changed

### Workstream `WORKSTREAM.md` files
- Update findings with new analysis or data found in the folder
- Update status — what's done, what's in progress
- Refresh next steps and open questions
- If a folder looks like a workstream but has no WORKSTREAM.md, create one (after confirming with user)

### CLAUDE.md
- Update the workstream list if new workstreams were added
- Update the project summary if the scope changed
- Don't touch behavioral rules unless something is broken

---

## Step 5: Handle New Content

If you find documents, attachments, or data files that aren't reflected anywhere:

1. Identify what they are — read or scan them
2. Extract durable insights — key findings, data points, decisions
3. Route them to the relevant workstream's WORKSTREAM.md or the appropriate .context/ file
4. Don't duplicate — summarize into the context layer, don't copy raw content

---

## Step 6: Summary

After updating, share in chat:

> "Here's what I updated:
> - [file] — [one-line summary of change]
> - [file] — [one-line summary of change]
>
> **Still open:** [any gaps you noticed but couldn't fill]"

---

## Important Rules

- **NEVER use AskUserQuestion** — all interaction happens in chat
- **Require existing context** — if there's no `.context/` folder, redirect to new/existing mode
- **Scan first, discuss, then update** — always show the audit before making changes
- **Surgical updates** — don't rewrite files that are mostly fine. Edit the parts that changed.
- **Ask about ambiguity in chat** — if unsure whether something is a new workstream, ask conversationally
- **Don't inflate** — if the project is lean, the context layer should stay lean
- **Preserve the user's voice** — match the tone and style of what's already there
