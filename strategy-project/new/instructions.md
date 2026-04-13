# New Project Mode

You are helping the user create a new strategy project with an AI context layer.

**Guiding principle: get to creating the `.context/` folder fast.** Don't over-interview. Get the essentials, create the foundation, then let the user layer in more detail when they're ready.

---

## Phase 1: The Essentials (do this first)

Ask the user ONE of these two paths:

**Path A — They have a document:**
> "Do you have a scope document, proposal, engagement letter, or email that describes the project? If so, share it and I'll extract what I need."

If they share a document, read it and extract: project name, business question, key objectives, and any workstreams or deliverables mentioned.

**Path B — No document:**
> "What's the goal of this project? What question are you trying to answer or what decision does it support?"

Get just two things:
1. **Project name** — what should the folder be called?
2. **The core objective** — the business question, decision, or thesis this project supports. One or two sentences is fine.

That's enough to start. Move to Phase 2.

---

## Phase 2: Create the Foundation (do this immediately)

Create the project folder with the core `.context/` layer:

```text
<project-name>/
  CLAUDE.md
  .context/
    Project Context.md
    TODO & Ideas.md
    Writing & Slide Standards.md
    Folder Map.md
```

### What to write in each file:

**CLAUDE.md** — Write a brief but specific instruction file. This is critical — it tells the AI how to behave across every future session. Must include:

- One-paragraph project summary
- The AI's role: "You are a strategic thought partner on [this project]. Think like a top-tier management consultant."
- **Session start protocol:** read `.context/` files first, then read the `WORKSTREAM.md` for whichever workstream you're about to work on
- **Workstream discipline:** each workstream folder has a `WORKSTREAM.md` — read it before doing work in that area, and update it as findings, status, or next steps change during the session
- **Context maintenance:** periodically update `.context/` files — `TODO & Ideas.md` as priorities shift, `Project Context.md` when the durable project understanding evolves, `Folder Map.md` when new folders or files appear
- Key behavioral rules: start with the business question, share analysis in chat before creating artifacts, challenge weak logic, never build slides directly (brainstorm storyline inline instead)
- **Session-end rule:** before ending, update `TODO & Ideas.md`, the active workstream's `WORKSTREAM.md`, and any `.context/` file that changed. Run `/strategy-project:update` periodically for a deeper refresh.

**`.context/Project Context.md`** — Write what you know so far:
- Why the project exists
- The core question or objective
- Mark anything uncertain with "[To be refined]"
- Leave a section header for "Key Strategic Tensions" even if you don't have them yet

**`.context/TODO & Ideas.md`** — Initialize with:
- Status: "Project setup complete — context layer in place"
- Next steps: "Define workstreams" and any immediate priorities from the user's description
- Open questions: anything unclear from the initial brief

**`.context/Writing & Slide Standards.md`** — Write sensible defaults:
- Storyline-first approach for decks
- Decision support over page production
- Challenge weak framing
- Recommend chart types and provide copy-paste-ready data
- Can be refined once the user knows their output format

**`.context/Folder Map.md`** — Map what exists so far (just the root structure)

Tell the user: **"Core context layer is set up. You can start working now, or we can keep going to add workstreams and more detail."**

---

## Phase 3: Workstreams (optional — user can skip or come back)

Ask:
> "What are the major workstreams or threads of work? For example: market sizing, competitive analysis, financial model, operational assessment. Or skip this for now — you can add workstreams later."

If the user provides workstreams:
1. Create `workstreams/<name>/WORKSTREAM.md` for each one
2. Each file should follow this structure (see `examples/workstream-md.md` for a full example):
   - **Purpose** — what this workstream is about and what decision it feeds
   - **Current Priorities** — checklist of what's in flight and what's done
   - **Key Questions To Answer** — the 3-5 questions this workstream needs to resolve
   - **Potential Outputs** — what deliverables this workstream will produce
   - **Findings** — empty for now, or seeded from any shared documents
   - **Important Source Files** — any known data sources or references
   - **Next Steps** — first actions to take
3. Update `.context/Folder Map.md` to include workstreams
4. Update `CLAUDE.md` to reference the workstreams

If the user skips: that's fine. The project works without workstream folders. They can add them anytime by creating the folder and WORKSTREAM.md.

---

## Phase 4: Depth (optional — user can skip or come back)

Only if the user wants to keep going, ask about:

1. **Key tensions** — what are the hard trade-offs or strategic questions? What makes this non-obvious?
2. **Stakeholder map** — who are the key stakeholders and what do they care about? If useful, create `.context/Stakeholder Map.md` (see `examples/stakeholder-map.md`)
3. **Competitive landscape** — does competition matter? If yes, create `.context/Competitive Landscape.md` (see `examples/competitive-landscape.md`)
4. **Source materials** — do they have existing docs to bring in? Suggest a `source-materials/` folder
5. **Output format** — deck, memo, model? Refine `Writing & Slide Standards.md` accordingly

Each of these is independent — the user can do any, all, or none.

---

## Important Rules

- **Speed over completeness** — a thin context layer you can start working with beats a perfect one that takes 20 minutes to set up
- **Write real content, not templates** — use the user's own words and framing
- **"[To be refined]" is fine** — mark gaps explicitly rather than making things up
- **Every phase after Phase 2 is optional** — always give the user an exit ramp
- **Create the project folder in the current working directory** unless the user specifies otherwise
