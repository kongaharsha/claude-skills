# WK PPT Style Specification

## Empirical Baseline

Observed across source decks:
- Slide size: 13.333 x 7.5 inches, 16:9.
- Primary fonts: Fira Sans Light, with Fira Sans Medium for emphasis. Some placeholders appear as `+mj-lt` / `+mn-lt` theme fonts; keep the active deck theme rather than forcing replacements.
- Most common explicit font sizes: 10, 9, 12, 11, 8, 10.5, 14, 7, 16, 18, 24, 28 pt.
- Common title sizes: 24 and 28 pt in full readouts; compact update pages may use tighter title bands only when inherited from the template.
- Common body/table sizes: presentation-ready body copy and table cells should target 10-12 pt, with 12-14 pt for key messages, discussion prompts, and short callouts. Footnotes/source notes should be 8 pt Fira Sans. Do not use 8.x or 9.x pt for body/table text in executive presentation decks unless the slide is explicitly appendix/evidence-pack material.

Recent self-evaluation note:
- A generated Berlin session deck looked shabby because it used too many tiny text boxes, several 6.2-6.8 pt text runs, weak hierarchy between title/body/labels, and too many independently placed objects. Treat this as a failure pattern to avoid: do not shrink text to fit content and do not assemble pages from many loose fragments when a table, lane, or grouped exhibit would be cleaner.
- A later Berlin refinement still failed presentation-readiness because body tables used 8.8 pt text and the cover was rebuilt on a blank slide rather than the WK title-slide master. Treat this as a second failure pattern: body/table text must stay 10-14 pt, and the WK master/template must remain intact outside the slide-body exhibit area.

## Typography

- Use Fira Sans Light as the default text face.
- Use Fira Sans Medium for section labels, table headers, key metric labels, and emphasized numbers.
- Use sentence-case titles.
- Use compact prose. A title can be long if it is the slide takeaway, but body copy should be clipped to the minimum needed.
- Use bullets sparingly; WK pages more often use boxes, tables, and label strips than bullet lists.

Recommended sizes:
- Lead-line / takeaway title: 24 or 28 pt Fira Sans. Use 24 pt for longer lead lines and 28 pt for shorter high-emphasis titles.
- Cover title: 24-28 pt depending on template.
- Compact executive update title: 18-24 pt only when the template requires a tighter title band.
- Section/table header: 12-14 pt.
- Body text: 10-12 pt by default; 14 pt is acceptable for short body blocks, major messages, or workshop discussion prompts.
- Table text and body labels: 10-12 pt for presentation decks. Use 10 pt as the floor only after shortening text; do not use 8.x or 9.x pt for normal body tables.
- Chart annotations and exhibit labels: 10-12 pt when they need to be read in presentation mode. Tiny axis labels or secondary chart labels may be smaller only when inherited from a native chart and not part of the main message.
- Footnotes/source notes: 8 pt Fira Sans.

Hard floors:
- Main body text, callouts, table cells, and body labels: minimum 10 pt in presentation-ready decks.
- Dense appendix tables or backup evidence labels: may use 8-9 pt only when explicitly appendix/evidence-pack material, not in the main executive storyline.
- Footers/source notes: 8 pt Fira Sans.
- Never use 6.x pt text in generated decks. If body or table content does not fit at 10 pt, shorten it, split it, or move it to appendix.

Hierarchy rules:
- A standard analysis slide needs one dominant lead-line title, usually 24 or 28 pt Fira Sans or the active template title placeholder.
- Body and table text should usually sit 10-12 pt, with 14 pt reserved for short message blocks or discussion prompts.
- Avoid mixing large titles with 8.x or 9.x body text on main narrative slides; it reads unfinished in presentation mode.
- Large numbers or section labels may use 14-20 pt, but avoid mixing 18 pt mini-headlines with tiny body text on the same slide unless the layout clearly supports that hierarchy.
- Do not use more than 3 text-size tiers on a normal analysis slide: title, header/metric, body/label. Footer/source notes are exempt.

## Color Palette

Core:
- WK blue: #007AC3.
- Dark blue: #003D62 or #005C92.
- Black: #000000.
- White: #FFFFFF.

Structure and background:
- Light gray: #F6F6F6, #DADADA.
- Pale blue: #A6D1EA, #CAE3F2, #CCE4F3, #EDF6FB, #BDD7EE.

Meaning colors:
- Yellow/assumption: #F9F2BD, #E5CD69.
- Green/positive: #648D18, #364F0E, #E7F2D2.
- Orange/watch item: #EA8F00.
- Red/risk: use sparingly.

Rules:
- Blue is the structural and brand color.
- Gray is for grouping and neutral scaffolding.
- Yellow is for assumptions, notes, hypotheses, or callouts.
- Green/orange/red must encode meaning; do not use them decoratively.

## Layout Geometry

- Keep a consistent top title band across the deck.
- Preserve the WK master/template outside the content exhibit area. Title slides should use the deck's title-slide master, and standard pages should use the closest matching content-slide master. Custom visuals belong inside the body area, not by replacing the master title structure with blank-slide approximations.
- Preserve the small bottom footer/source band.
- Align objects to a visible grid. Edges should line up across columns, tables, and charts.
- Use thin outlines and light fills rather than heavy borders.
- Leave more whitespace around the title and footer than inside dense evidence areas.
- Prefer full-width evidence zones over floating card clusters.
- Prefer 2-4 major content zones per slide. If a slide needs more, use a table, swimlane, or appendix split.
- Avoid many independently positioned micro-boxes. A slide with ~20+ text-bearing objects should be treated as a warning sign and consolidated.
- Reuse consistent x positions across columns. If many boxes have slightly different left edges, snap them to a shared grid.

## Tables

- Use table headers in WK blue, dark blue, pale blue, or gray.
- Keep header text concise and criteria parallel.
- Keep table text at 10 pt or larger in main presentation pages. If a cell cannot fit at 10 pt with reasonable wrapping, shorten the wording, reduce columns, split the page, or move detail to appendix.
- Use row fill only for grouping or emphasis.
- Avoid wrapping every word. If a cell wraps to more than 3 lines, shorten it or split the table.
- Put the implication/priority column at the right where possible.

## Charts

- Use blue for base series.
- Use contrast color only for an exception, selected option, forecast, or risk.
- Directly label the most important data where possible.
- Include source, base, and date for survey/customer charts.
- Keep chart labels and annotations at 10 pt or larger when they carry the message. Only secondary native axis labels may sit below 10 pt.

## Images and Screenshots

- Use product screenshots, actual market maps, or real exhibits when they add evidence.
- Crop tightly and label clearly.
- Do not use generic decorative images.
- Add a caption or callout if the reason for the image is not obvious.

## QA Checklist

- Titles are aligned and written as takeaways.
- Font family matches the active deck theme.
- No main body text, table cell text, body labels, or callouts are below 10 pt on main presentation slides; footnotes/source notes/page numbers are 8 pt Fira Sans.
- The cover/title slide and standard page title bands use the WK master layouts rather than blank-slide rebuilds, unless the user explicitly asks for a custom theme.
- No slide relies on 6.x pt text.
- Normal slides use a clear title/header/body hierarchy with no more than 3 active text-size tiers.
- Text boxes and evidence objects are snapped to a consistent grid.
- Slides avoid fragmented construction from many loose text boxes.
- Tables fit without cramped unreadable wrapping.
- Color meanings are consistent.
- Source/date/footer elements are present where needed.
- Every slide has one clear primary read.
- Appendix slides are clearly marked and need not be as sparse as main narrative slides.
