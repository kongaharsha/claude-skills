# Folder Map — Project Atlas
*Last updated: 2026-04-10*

## Top-Level Structure

| Folder | Purpose |
|---|---|
| `.context/` | Compiled project knowledge — AI reads this first |
| `workstreams/market-sizing/` | TAM/SAM analysis, segment attractiveness, revenue scenarios |
| `workstreams/competitive-analysis/` | Competitor mapping, positioning, differentiation |
| `workstreams/partnerships/` | Partner evaluation, deal structures, build vs. buy vs. partner |
| `workstreams/financial-model/` | Unit economics, scenario analysis, investment case |
| `source-materials/` | Raw documents — analyst reports, data extracts, interview notes |
| `outputs/` | Deliverables — decks, memos, one-pagers sent to stakeholders |
| `scratch/` | Temporary analysis, working drafts, exploration (not durable) |

## Where To Look First

- **For broad context:** start with `.context/Project Context.md`
- **For current priorities:** check `.context/TODO & Ideas.md`
- **For the freshest direction:** check the most recently updated workstream `WORKSTREAM.md`
- **For a specific workstream:** go to `workstreams/<name>/WORKSTREAM.md`
- **For raw data or reports:** check `source-materials/`
- **For what's been shared with stakeholders:** check `outputs/`

## Usage Notes

- Prioritize workstream `WORKSTREAM.md` files over raw source documents when starting analysis
- Keep `scratch/` for throwaway work — don't let it accumulate context that should be in a WORKSTREAM.md
- Generated outputs go in `outputs/` — not in workstream folders
- Root `.context/` is for cross-project guidance; workstream `WORKSTREAM.md` files are for local context
