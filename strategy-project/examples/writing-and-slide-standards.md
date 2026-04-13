# Writing & Slide Standards
*Last updated: 2026-04-10*

---

## Document Preferences

1. Prefer markdown files instead of docx.
2. Never create PowerPoint files. Default to writing a markdown file instead of pptx. For each slide in the markdown file have a **lede**, **slide content**, and **format**. `format` could be LHS vs. RHS or top box, bottom callout, etc.

---

## When Asked To Build Slides

Never build the slide directly. First align on the slide structure (lede line, actual slide content, takeaways, etc.).
Once aligned, share the output directly in the chat vs. creating a slide.
When doing multiple slides or the full storyline, adopt the same methodology of sharing it in the chat vs. creating ppts.
If you are doing multiple slides, align on the storyline first, and then do one slide at a time. Once a slide is completed, align with the user for changes before creating the next slide.

---

## Analysis In Chat

For early-stage analytical work, prefer sharing insights in chat before creating files.

- Start by making sure the analysis is answering the right business question.
- If the goal is exploratory, align with the user on the most useful cuts before going deep.
- Lead with the business implication, then the supporting evidence.
- Use rounded, executive-readable numbers by default.
- Prefer:
  - `$6.2B` over `6207.903774`
  - `$92M` over `91.747965`
  - `~15%` over `15.178392%`
- Always label the source file and source sheet for important metrics.
- If a metric uses a working definition or proxy, label it clearly.
- Prefer a short business readout over raw diagnostic tables unless the user asks for the detail.
- When helpful, use simple tables or chart-like summaries directly in chat before building formal outputs.

A good early-stage analysis response should usually include:
1. What question the analysis answers
2. What cuts or lenses are being used
3. What the data says
4. Why it matters
5. What needs validation
6. What we should do next

---

## Slide Structure

### Lede (Title / Headline)
- Written as a **specific, quantified assertion** — not a label
- Must contain: direction + magnitude + where concentrated
- Format: `[Subject] [verb] [direction] [by how much] [where / when]`

**Good:**
> "US new sales down ~24% YoY, concentrated in Q3-Q4 and accelerating into Q1"

> "Renewal rate declining 2pp YoY; TCV stability is masking subscriber erosion"

**Bad:**
> "New Sales Trends" *(label, not insight)*

> "Renewal rates are declining" *(direction without magnitude or concentration)*

### Right-Hand Side Takeaways (3-5 bullets)
- Do **not** restate chart labels or describe what the chart shows
- Bullets should be 1-2 sentences, exec-readable
- Lead with the implication, not the observation

**Good:**
> "Decline is concentrated in US/Canada — international rates are flat — pointing to a competitive driver, not a global product issue."

> "At current trajectory, ~$45M in TCV could disappear by 2028 with no intervention."

**Bad:**
> "US renewal rate is 73%" *(restates chart data)*

> "There are multiple drivers of churn" *(vague, no implication)*

### "Big Number" Callout
- Include **one prominent callout** per slide where it aids scanability
- Format: large-font number + short label
- Examples: `$40M at risk`, `-24% US new sales YoY`, `40% annual lapse rate`

### Questions To Confirm Box
- Every substantive slide should end with 2-4 specific questions
- These should be questions that, **if answered, would change a decision or the chart itself**
- Label data owner where known

---

## Chart And Visualization Standards

**Prefer:**
- **Waterfall charts** when explaining a delta (revenue change, subscriber movement)
- **Cohort retention curves** for renewal health over time
- **Simple line charts** for trend (YoY, QoQ)
- **Bar + delta annotations** for comparisons (FY25 vs FY24)
- **Bar + dot combo** for showing totals vs. a threshold (e.g., families needed to reach 80% of revenue)
- **100% stacked bar** when the story is about concentration or composition

**Avoid:**
- Dense tables as primary diagnostic (move to appendix if needed)
- Charts where the "so what" requires the reader to do the math
- Demographic slices that don't point to a commercial lever

**Always define the metric in the chart footnote:**
- What counts
- What doesn't count
- Known caveats

---

## Working Style For Analysis

- Optimize first for a preliminary business read, not a perfect data model.
- Start by identifying the business question the file or dataset can answer.
- Think like a strategist, not just a data extractor.
- If the user asks to "analyze this file," first check the relevant project and workstream context and understand what decision the analysis should support.
- If the goal is not clear from context, check with the user briefly before going deep.
- If the goal is broad or exploratory, suggest the most useful analytical cuts and test them with the user before going deeper.
- Default first output to insights in chat, not files.
- Before creating dashboards or Excel outputs, first share:
  - the question being answered
  - the source file or sheet being used
  - the cuts or lenses being applied
  - the 3-7 most important findings
  - the key caveats or assumptions
  - the suggested next step
- Use working assumptions where needed to produce a preliminary read, but label them clearly.
- Be explicit about the difference between:
  - what the data directly shows
  - what is a working proxy or approximation
  - what still needs validation
- Prefer one clear business narrative over exhaustive tab-by-tab reporting.

### Default Workflow For Exploratory Analysis
1. Read the relevant context and source files.
2. Identify the business question the material can answer.
3. Align with the user on the most useful analytical cuts or lenses.
4. Share a preliminary read in chat with rounded numbers and source labels.
5. Use simple tables, charts, or structured summaries directly in chat where helpful.
6. Discuss with the user what is worth formalizing.
7. Only then offer to build a dashboard, markdown output, or Excel file.

---

## Data Presentation Rules

- Prioritize executive readability.
- Always round numbers unless precision is necessary for a decision.
- Lead with the implication first, then the supporting number.
- Always cite the source file and, where relevant, the source sheet for important statistics.
- If a number is illustrative, approximate, or based on a working definition, say so explicitly.

---

## Excel Output Rules

- Keep numeric cells as numeric format.
- Keep percentages as percentage format.
- Keep dates as date format.
- Keep text labels as text.
- Avoid exporting messy workbook dumps.
- Prefer a small number of clean, decision-useful sheets over many tabs.

---

## Tone And Voice

**Write for a time-constrained executive reader.**
- Lead with the conclusion, support with evidence
- One idea per slide
- Use plain English — avoid jargon unless defined on first use
- No hedging without labeling: if a number is uncertain, say so explicitly

**Be direct about uncertainty.**
- If data is missing or unvalidated, say: "Data needed: [what, from whom]"
- Do not present illustrative numbers as fact — label them: "(Illustrative — for validation)"

**Challenge the narrative.**
- If a slide is descriptive with no implication, flag it
- Recommend cuts or rewrites, not just additions
- If a question is poorly framed, say so and reframe it before answering
