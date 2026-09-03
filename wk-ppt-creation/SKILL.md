---
name: wk-ppt-creation
description: Create, edit, or review Wolters Kluwer Corporate Strategy PowerPoint decks in the observed WK executive-update/readout style. Use when Codex is asked to make PPT/PPTX slides, synthesize strategy work into a deck, restyle slides to match WK, create executive updates, KPI dashboards, market maps, option/pathway comparisons, SteerCo/final readouts, next-step pages, or review PowerPoint typography/layout quality for Wolters Kluwer strategy work.
---

# WK PPT Creation

## Core Workflow

1. Start from an existing WK deck or template whenever available. Preserve the slide size, theme fonts, footer/date/client marks, title-slide layout, content-slide master geometry, and other template scaffolding. Build new visuals inside the body area, but do not hand-build replacement title pages or title bands unless explicitly asked.
2. Decide the deck type before drafting: executive update, KPI dashboard, strategy options/pathways, market/competitive deep dive, SteerCo/final readout, or appendix-heavy evidence pack.
3. Use the slide pattern library in `references/pattern-library.md` to choose page structures. Do not invent a new layout when one of the standard patterns fits.
4. Apply the style specifications in `references/style-spec.md` for typography, color, spacing, and density.
5. Use the operating procedure in `references/deck-operating-procedure.md` for storylining, slide construction, and QA.
6. Before final delivery, inspect slides visually or with extracted geometry. Check title hierarchy, alignment, table legibility, text overflow, consistent footers, and whether every page has a clear governing takeaway.
7. Run the designer polish gate in `references/deck-operating-procedure.md`: verify font-size floors, title/body hierarchy, grid alignment, text-box count, and whether the slide looks professionally designed at thumbnail size.

## Defaults

- Format: 16:9 widescreen, usually 13.333 x 7.5 inches.
- Font family: Fira Sans Light for most text; Fira Sans Medium for emphasis, labels, and key values.
- Page grammar: title at top, thin WK blue rule/anchor elements, dense but controlled evidence area, small footer/source band.
- Title style: a full-sentence takeaway beats a topic label. Topic pipes are acceptable for readouts, for example `Market entry | Partner/Buy | Priority targets`.
- Normal text sizes: 24 or 28 pt Fira Sans for lead-line/takeaway titles; 10-14 pt for slide body, table cells, labels, and callouts depending on content density; and 8 pt Fira Sans only for footnotes/source notes, page numbers, or true metadata. For presentation-ready executive decks, do not use 8.x or 9.x pt in the body just because a table is dense; shorten content or split the page instead.
- Color language: WK blue accents, black body text, light gray panels, pale blue fills for data/table structure, pale yellow for assumptions or callouts, green/orange/red only for status, financial impact, or risk signals.
- Density: WK strategy decks tolerate high density, but the reader must be able to scan the page in three passes: title, structure, evidence. Do not solve overcrowding by shrinking text; edit content down, split the page, or move detail to appendix.

## Reference Selection

- Read `references/pattern-library.md` when choosing slide types or building pages from scratch.
- Read `references/style-spec.md` when matching typography, color, grid, tables, charts, footnotes, or status colors.
- Read `references/deck-operating-procedure.md` when creating a full deck, converting notes into a deck, or doing final QA.

## Guardrails

- Avoid marketing-style hero pages, oversized decorative cards, generic stock imagery, and loose narrative prose.
- Avoid one-off colors outside the WK palette unless they encode meaning.
- Avoid centered paragraphs on analysis slides. Use structured boxes, tables, lanes, columns, or charts.
- Do not shrink slide body, table cells, labels, or callouts below 10 pt in presentation decks. Use 10 pt as the absolute body floor, 10.5-12 pt as the normal working range, and 12-14 pt for key messages or workshop prompts. Footnotes/source notes/page numbers may be 8 pt Fira Sans.
- Avoid building slides from many independent micro text boxes. If a slide has more than ~20 text-bearing objects, consolidate into a table, swimlane, or grouped evidence block.
- Test font size against the actual slide: start at 12 pt body where feasible, reduce to 10.5 or 10 pt only after shortening copy, and never solve fit by dropping body text into 8.x or 9.x pt.
- Do not deliver a deck without checking for cut-off text, inconsistent title bars, missing source notes, and crowded tables.
