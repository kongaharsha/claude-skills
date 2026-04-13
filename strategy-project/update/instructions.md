# Update Mode — Refresh the Project Context Layer

You are helping the user bring their project's `.context/` folder and workstream files up to date by scanning everything in the project.

**Guiding principle: read everything, then reconcile.** The context layer may have drifted from reality — new files added, workstreams that progressed, findings that were never captured, stale TODOs. Your job is to fix that.

---

## Step 1: Full Project Scan

Read the project systematically:

1. **CLAUDE.md** — understand the current instructions and project framing
2. **`.context/` files** — read every file in the context folder
3. **All workstream folders** — read every `WORKSTREAM.md`, plus scan for new files, analysis outputs, notes, or data that appeared since the last update
4. **Source materials** — scan for new documents, attachments, PDFs, spreadsheets, or data files anywhere in the project
5. **Conversation context** — if there's an active conversation, review what was discussed, decided, or discovered
6. **Orphan folders** — look for folders that exist but have no `WORKSTREAM.md` (may be new workstreams)

Build a mental inventory of:
- What the context layer says vs. what actually exists
- New work or files not reflected in the context
- Stale information that needs updating or removing
- Missing workstreams or workstream files
- Open questions that have been answered
- TODOs that are done or no longer relevant

---

## Step 2: Show the User What You Found

Present a concise diff — what's out of date and what you'll fix:

> **Context layer audit:**
> - `.context/Project Context.md` — [up to date / needs X updated]
> - `.context/TODO & Ideas.md` — [3 items done, 2 new priorities to add]
> - `.context/Folder Map.md` — [2 new folders not mapped]
> - `.context/Competitive Landscape.md` — [stale / missing / fine]
> - `workstreams/market-sizing/WORKSTREAM.md` — [findings not captured from new analysis]
> - `workstreams/financial-model/` — [folder exists but no WORKSTREAM.md]
> 
> Want me to update all of these, or pick specific ones?

---

## Step 3: Update the Files

For each file that needs updating:

### `.context/TODO & Ideas.md`
- Remove completed items
- Add new priorities discovered from the scan
- Update current status
- Refresh open questions — remove answered ones, add new ones
- Keep it short and crisp (this is the most common file to go stale)

### `.context/Project Context.md`
- Update if the project's durable understanding has changed
- Add new workstreams that were created since last update
- Refine strategic tensions based on new findings
- Don't rewrite what's still accurate — surgical updates only

### `.context/Folder Map.md`
- Add new folders and files
- Remove references to deleted folders
- Update descriptions of where the freshest work lives
- Note new source materials or data files

### `.context/Competitive Landscape.md`
- Update if new competitive intel appeared in any workstream
- Create this file if competition has become relevant and it doesn't exist yet
- Remove if no longer relevant (ask first)

### `.context/Writing & Slide Standards.md`
- Usually doesn't need updating unless the output format or audience changed
- Check if any new conventions emerged from recent work

### Workstream `WORKSTREAM.md` files
- Update findings with new analysis or data found in the folder
- Update status — what's done, what's in progress
- Refresh next steps
- Update open questions
- If a folder looks like a workstream but has no WORKSTREAM.md, create one

### CLAUDE.md
- Update the workstream list if new workstreams were added
- Update the project summary if the scope changed
- Don't touch behavioral rules unless something is broken

---

## Step 4: Handle New Content

If you find documents, attachments, or data files that aren't reflected anywhere:

1. **Identify what they are** — read or scan them
2. **Extract durable insights** — key findings, data points, decisions
3. **Route them** — update the relevant workstream's WORKSTREAM.md or the appropriate .context/ file
4. **Don't duplicate** — summarize into the context layer, don't copy raw content

For new folders that look like workstreams:
- Ask the user: "I see a `regulatory-analysis/` folder that doesn't have a WORKSTREAM.md. Is this a workstream? Want me to create one?"

---

## Step 5: Summary

After updating, show:

1. **What changed** — list each file updated and a one-line summary of the change
2. **What was added** — any new files created (new WORKSTREAM.md files, etc.)
3. **What's still open** — gaps you noticed but couldn't fill (e.g., "the financial model workstream has data files but no written findings — you may want to work on this next")

---

## Important Rules

- **Read before writing** — scan everything before changing anything
- **Surgical updates** — don't rewrite files that are mostly fine. Edit the parts that changed.
- **Ask about ambiguity** — if you're not sure whether something is a new workstream or just scratch files, ask
- **Don't inflate** — if the project is lean, the context layer should stay lean
- **Preserve the user's voice** — when updating, match the tone and style of what's already there
- **Show your work** — always present the audit before making changes so the user can steer
