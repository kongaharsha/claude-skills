# WK PPT Creation Operating Procedure

## 1. Diagnose the Assignment

Classify the request:
- Executive update: short, current-state, action-oriented, leadership scan.
- KPI dashboard: metrics-heavy, date-stamped, variance and trend focused.
- Strategy options/pathways: decision support with comparable choices.
- Market/competitive deep dive: evidence pack with maps, tables, and synthesis.
- SteerCo/final readout: storyline plus appendix, more formal and structured.

Then identify:
- Audience and decision needed.
- Required date/version label.
- Source material and confidence level.
- Whether a full narrative deck or a few inserted slides are needed.

## 2. Build the Storyline

Use this default arc:
1. Context: what changed or why we are here.
2. Insight: what the evidence says.
3. Implication: what it means for WK.
4. Options: what choices exist.
5. Recommendation: what to do next.
6. Next steps: owners, timing, asks.

For weekly updates, compress the arc into: current status, evidence, risks, next actions.

## 3. Select Slide Patterns

Map content to pattern:
- One-page answer: executive summary.
- Metrics or trend: KPI dashboard or chart analysis.
- Comparison across vendors/options/workflows: matrix/table.
- Strategic choice: options/recommendation.
- Ecosystem/workflow: dense market/system map.
- Evidence screenshot/product example: visual exhibit.
- Meeting navigation: agenda/section divider.
- Closeout: next steps/decision ask.
- Executive workshop or leadership session: workshop/session pattern from `pattern-library.md`, usually lighter than a final readout and built around 1-2 decisions per section.

## 4. Draft Each Slide

For each slide:
1. Use the closest WK master layout first: title slide for covers, standard content/title layouts for body pages, and existing footer/source geometry where available.
2. Write the takeaway title first.
3. Choose the simplest pattern that can carry the evidence.
4. Place the largest evidence object second: chart, table, map, or pathway.
5. Set body/table/callout text at 10-14 pt, starting near 12 pt where feasible and reducing only after editing copy. If the content cannot fit at 10 pt, split or cut it.
6. Add only supporting labels needed for interpretation.
7. Add source/notes/footer.
8. Re-read the title against the body. If the body does not prove the title, revise one of them.

## 5. Edit for WK Style

Use this edit pass:
- Replace paragraphs with structured boxes or table rows.
- Convert vague headings into answer-first titles.
- Normalize font sizes to the observed ranges.
- Align columns and object edges.
- Remove decorative elements that do not encode information.
- Use the color rules from `style-spec.md`.
- Reduce loose text boxes. If the slide is composed of many separate text objects, rebuild it as a table, 2-3 column structure, swimlane, or grouped exhibit.
- Edit content before shrinking type. Main storyline body, tables, labels, and callouts must stay at or above 10 pt. Footnotes/source notes/page numbers should stay 8 pt Fira Sans. If a table needs 8.x or 9.x pt to fit, it is too dense for the main deck: shorten, reduce columns, split the page, or move detail to appendix.
- Preserve master/template scaffolding. Do not rebuild WK title slides, title bands, footers, or slide-number structures on blank slides unless the user explicitly requests a custom design.

## 6. Appendix Discipline

- Keep main narrative slides decision-grade and selective.
- Move detailed data cuts, backup tables, methodology, and extra screenshots to appendix.
- Mark appendix with a simple divider.
- Keep appendix formatting consistent, but allow higher density.

## 7. Final QA

Before delivering a PPTX:
- Open or render the deck if tooling allows.
- Check every slide for text overflow and object overlap.
- Scan at thumbnail size: pattern, hierarchy, and title should still be clear.
- Check slide sorter flow: no duplicate or orphan section pages.
- Verify charts/tables cite sources and dates.
- Confirm file name, version, and date match the user request.
- Programmatically inspect font sizes where possible, separating body/table content from metadata. The main slide body should not contain 8.x or 9.x pt text in presentation decks.

## 7.1 Designer Polish Gate

Run this gate before delivery, especially for generated decks:

- **Font floor:** lead-line title is 24 or 28 pt Fira Sans; body/table/label/callout text is 10-14 pt depending on density, with 10 pt as the absolute main-body floor; footnotes/source notes/page numbers are 8 pt Fira Sans. Do not use 8.x or 9.x pt for main body tables in presentation decks.
- **Template fidelity:** title slides and standard title/content bands use the WK master layouts. Custom visuals may be built inside the body area, but the deck should not look like it was recreated on blank slides.
- **No microtype:** generated decks should never use 6.x pt text.
- **Hierarchy:** each slide has one dominant title and no more than 3 active text-size tiers excluding footer/source notes.
- **Grid:** major objects share left/right edges; avoid nearly aligned edges that differ by a few pixels.
- **Text-box count:** if a slide has more than ~20 text-bearing objects, consolidate into a table, lane, or grouped evidence block.
- **Density:** content reads in three passes: title, structure, evidence. If not, split the slide.
- **Professional finish:** no floating fragments, accidental whitespace holes, inconsistent box sizes, or arbitrary color use.
- **Thumbnail test:** at slide-sorter size, the page pattern should be obvious and the primary takeaway should still be identifiable.

If a slide fails the gate, revise before delivery. Do not describe the issue as a caveat; fix it.

## 8. When Editing Existing Decks

- Preserve the existing master and theme.
- Preserve the title-slide master, standard content-slide title geometry, footers, slide numbers, and logo/theme treatment unless explicitly asked to redesign the template.
- Match nearby slide geometry before adding new elements.
- Reuse an existing slide of the same pattern where possible.
- Do not restyle the whole deck unless explicitly asked.
- Keep user-provided content and speaker intent intact while improving clarity.
