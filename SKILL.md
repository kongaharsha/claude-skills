---
name: tax
description: >
  Complete U.S. personal income tax assistant with three modes. Use this skill whenever someone
  says "do my taxes", "prepare my tax return", "file my taxes", "what do I owe", "tax summary",
  "tax optimization ideas", "navigate FreeTaxUSA", "figure out my AGI", "analyze my W-2s and
  1099s", or hands you any collection of tax documents (W-2, 1099-DIV, 1099-B, 1099-MISC, 1098,
  prior return). Also use when the user wants to understand any specific part of their tax
  situation — deductions, capital gains, SALT, Medicare tax, NIIT, etc.

  Three modes — read the relevant sub-folder before starting:
  - **tax:prepare** → extract docs, compute return, produce 4-section chat summary + xlsx + tax_profile.json. Start here.
  - **tax:optimize** → surface unused savings strategies (requires tax:prepare first)
  - **tax:file** → navigate FreeTaxUSA live in Chrome to complete filing (requires tax:prepare first)
---

# Tax Assistant

This skill handles U.S. personal income tax returns end-to-end: from raw source documents through a complete tax summary, optimization ideas, and live online filing.

**Year-agnostic** — always look up current-year brackets, deductions, and thresholds. Never reuse prior-year values.

---

## Which Mode?

Read the instructions file for the mode the user is asking for. If unclear, start with `prepare`.

| User says… | Mode | Instructions |
|---|---|---|
| "do my taxes", "prepare my return", "figure out what I owe", "tax summary" | **Prepare** | `prepare/instructions.md` |
| "tax optimization", "what am I missing", "ways to reduce my tax bill" | **Optimize** | `optimize/instructions.md` |
| "file my taxes", "fill out FreeTaxUSA", "submit my return" | **File** | `file/instructions.md` |

> `tax:optimize` and `tax:file` both require `tax:prepare` to have run first. If `output/tax_profile.json` doesn't exist, tell the user to run the prepare mode first.

---

## Shared Folder Structure

All modes use the same working directory layout:

```
working_dir/
  source/                          ← user's tax documents (W-2, 1099s, 1098, prior return)
  work/                            ← intermediate files (never delete these)
    tax_data.txt                   ← extracted text from all source documents
    extraction_ledger.json         ← source-of-truth: every number mapped to its document + filer
    computations.txt               ← all tax math with annotations
    results.json                   ← structured computation results
    cross_foot_report.json         ← verification check results
  output/                          ← final deliverables (share these with the user)
    {YEAR} Tax Summary - {Names}.xlsx   ← formatted spreadsheet
    {YEAR} Tax Summary - {Names}.md     ← 4-section summary (also shown in conversation)
    tax_profile.json               ← structured handoff for optimize and file modes
    forms_required.md              ← list of required forms with reasons
```

---

## Shared Rules (all modes)

**Context budget:**
- Never use the Read tool on PDFs — use pdfplumber via bash
- Never read the same document twice — save extracted text to `work/tax_data.txt` on first read
- Never re-read source documents after the extraction ledger is built; always read from the ledger

**Data integrity:**
- All dollar values in JSON and Excel must be **numbers**, not strings — downstream code sums them arithmetically
- In MFJ spreadsheets, the Combined column uses `=B{row}+C{row}` formulas, not hardcoded totals
- Income belongs to whoever owns the account. Never split a combined 1099 50/50 unless the actual tax rule requires it

**References available:**
- `references/state_tax_agencies.md` — official state tax agency URLs for all 50 states + DC
- `references/federal_forms_guide.md` — which federal forms are needed and when
- `references/tax_rules.md` — IRS rules reference: SALT cap, AMT, NIIT, Additional Medicare Tax, bracket thresholds, key limits
