# Existing Project Mode

You are helping the user add the AI context layer to a project folder that already has work in it.

**Guiding principle: read first, ask second, never touch existing files.**

---

## Phase 1: Point to the Folder

Ask:
> "Where's the project folder? Give me the path and I'll take a look."

Once you have the path:
1. Read the directory structure (top-level and one level deep)
2. Scan for any existing AI config (CLAUDE.md, AGENTS.md, .cursorrules, etc.)
3. Look at key files: READMEs, any markdown summaries, project docs
4. Identify what look like workstreams (folders with analytical work)
5. Identify source material locations (data, raw docs, downloads)

---

## Phase 2: Quick Summary + Confirm

Share what you found:
> "Here's what I see in your project:
> - [folder structure summary]
> - [what looks like workstreams]
> - [where source materials seem to live]
>
> I'll add a `.context/` folder and `CLAUDE.md` alongside your existing files. Nothing gets moved or deleted.
>
> Before I do — what's the core business question or objective for this project?"

Get the one-liner on the project objective, then move to Phase 3 immediately.

---

## Phase 3: Create the Context Layer

Add these files to the existing project root:

```text
existing-project/
  CLAUDE.md                          # ← NEW
  .context/                          # ← NEW folder
    Project Context.md
    TODO & Ideas.md
    Writing & Slide Standards.md
    Folder Map.md
```

### What to write:

**CLAUDE.md** — Tailored to the existing project. This is the most important file — it tells the AI how to behave across every future session. Must include:
- Reference the actual folder structure and key files
- Note which existing files contain valuable context
- Instruct the AI to check existing work before starting new analysis
- **Session start protocol:** read `.context/` files first, then read the `WORKSTREAM.md` for whichever workstream you're about to work on
- **Workstream discipline:** each workstream folder has a `WORKSTREAM.md` — read it before doing work in that area, and update it as findings, status, or next steps change during the session
- **Context maintenance:** periodically update `.context/` files — `TODO & Ideas.md` as priorities shift, `Project Context.md` when durable understanding evolves, `Folder Map.md` when new folders or files appear
- Standard behavioral rules: thought partner, business question first, challenge weak logic, storyline-first for decks
- **Session-end rule:** before ending, update `TODO & Ideas.md`, the active workstream's `WORKSTREAM.md`, and any `.context/` file that changed. Run `/strategy-project:update` periodically for a deeper refresh.
- If there's an existing CLAUDE.md or AGENTS.md, ask the user whether to merge or replace

**`.context/Project Context.md`** — Synthesize from what you found:
- Pull context from existing docs, READMEs, or summaries
- Note what you inferred vs. what the user confirmed
- Flag gaps with "[To be refined]"

**`.context/TODO & Ideas.md`** — Reflect actual current state:
- What's in progress based on folder contents
- Known next steps if you can infer them
- Open questions

**`.context/Writing & Slide Standards.md`** — Sensible defaults (same as new project)

**`.context/Folder Map.md`** — Map the real folder structure:
- What each top-level folder contains
- Where the freshest work lives
- Where source material vs. compiled output belongs

Tell the user: **"Context layer is in place. You can start working now, or we can add workstream files to specific folders."**

---

## Phase 4: Workstream Files (optional)

Ask:
> "Want me to add a WORKSTREAM.md to any of these folders? This gives the AI a summary of each workstream's current state. Or skip — you can add these later."

If yes:
- Create `WORKSTREAM.md` in each workstream folder following this structure (see `examples/WORKSTREAM.md`):
  - **Purpose** — what this workstream is about and what decision it feeds
  - **Current Priorities** — checklist of what's in flight and what's done (seeded from existing work)
  - **Key Questions To Answer** — inferred from existing analysis or asked
  - **Potential Outputs** — what deliverables this workstream will produce
  - **Findings** — summarize existing work found in the folder
  - **Important Source Files** — reference actual files found in the folder
  - **Next Steps** — inferred from current state
- Summarize existing work found in that folder
- Note what analysis exists and what gaps remain
- Update Folder Map accordingly

If they skip: that's fine.

---

## Phase 5: Depth (optional)

Same as new project — offer to add:
- Key tensions → update Project Context.md
- Stakeholder map → create `.context/Stakeholder Map.md` (see `examples/Stakeholder Map.md`)
- Competitive landscape → create `.context/Competitive Landscape.md` (see `examples/Competitive Landscape.md`)
- Output standards → refine Writing & Slide Standards.md

Each is independent and skippable.

---

## Important Rules

- **NEVER modify, move, rename, or delete existing files**
- **Only add new files** — `.context/` folder, `CLAUDE.md`, and optional `WORKSTREAM.md` files
- **Read before writing** — base content on what actually exists in the folder
- **Be honest about gaps** — "I didn't find details on X, you may want to add this"
- **If there's already a CLAUDE.md** — ask before replacing. Offer to merge.
- **Keep it proportional** — a small project gets a small context layer
