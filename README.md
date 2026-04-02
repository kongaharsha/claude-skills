# Tax Skill — Context & History

This README gives any new LLM the full context behind this skill: what it does, how it was battle-tested, what broke, and what we fixed. Read this before modifying the skill.

---

## What This Skill Does

End-to-end U.S. personal income tax assistant with three modes:

1. **tax:prepare** — Extract source documents (W-2s, 1099s, 1098s, etc.), compute the full federal and state tax picture, produce a summary spreadsheet + tax_profile.json
2. **tax:optimize** — Surface unused tax savings strategies (requires prepare first)
3. **tax:file** — Drive a tax filing platform (FreeTaxUSA) live in Chrome, filling in every field from the tax profile, then verify the return against source documents

---

## The User

Harsha Konga (Sreeharsha Konga). Ex-McKinsey engagement manager. Files MFJ with spouse Meenal Aggarwal. NJ resident, spouse works in NY (nonresident). High-income, multi-state, itemizes deductions, has FBAR requirement.

---

## Real-World Filing Session (April 2025, Tax Year 2025)

The skill was used end-to-end across multiple conversation sessions (context compacted several times) to file the Konga/Aggarwal 2025 tax return on FreeTaxUSA. Here's what happened:

### Filer Profile
- **Filing status**: MFJ
- **Primary**: Sreeharsha Konga, employed at Wolters Kluwer (NJ). W-2 box 1: $332,306
- **Spouse**: Meenal Aggarwal, employed at Amazon (NY). W-2 box 1: $191,300
- **Dependent**: Veda Aggarwal Konga (daughter, born 2024)
- **Address**: 601 Observer Hwy, Hoboken NJ
- **States**: NJ resident (NJ-1040) + NY nonresident (IT-203)
- **Key forms**: Schedule A (itemized), Schedule B, Schedule D, Form 8949, Form 2441 (CDCC), Form 8960 (NIIT), Form 8283 (noncash donations), FBAR

### Source Documents Processed
- 2x W-2 (Wolters Kluwer + Amazon)
- 2x 1099-DIV (Robinhood, both filers)
- 1x 1099-INT (Robinhood, spouse)
- 2x 1099-B (Robinhood + Morgan Stanley — RSU sales with basis not reported)
- 1x 1099-MISC (Hartford — short-term disability/maternity)
- 1x 1098 (PHH Mortgage — interest $50,192, principal $762,078)
- 1x Property tax statement (Hoboken — $11,056)

### Final Numbers (FreeTaxUSA)
- **Federal**: $295 owed
- **NY**: $2,050 refund
- **NJ**: $1,509 refund
- **Net**: ~$3,264 refund

### Key Tax Situations Encountered
- **SALT cap with OBBBA phase-out**: The 2025 SALT cap was raised from $10,000 by the One Big Beautiful Bill Act, with a phase-out for high AGI. Actual SALT paid was ~$47K, allowed was ~$29,529
- **Mortgage interest limitation**: Outstanding principal ($762K) exceeded the $750K cap, so interest was prorated. FreeTaxUSA computed $49,718 deductible vs 1098's $50,192
- **NIIT (Form 8960)**: 3.8% on net investment income. AGI ($534,903) exceeds $250K MFJ threshold. NIIT was $213
- **Additional Medicare Tax**: 0.9% on wages over $250K. $2,736 additional tax
- **Morgan Stanley RSU basis**: 1099-B reported as Box B (basis not reported to IRS). Had to ensure correct cost basis on Form 8949 to avoid double taxation
- **Multi-state credit**: NY allocated tax ($12,296) fed into NJ's credit for taxes paid to another state ($10,718). Dependency: NY must be completed before NJ
- **CTC phase-out**: Daughter Veda is under 17 and qualifies, but CTC fully phased out at AGI >$400K

---

## What Broke During Filing (Pain Points)

These issues directly informed the 8 skill improvements below.

### 1. FreeTaxUSA React SPA Quirks
Standard mouse clicks on dropdowns didn't register. Selects required JavaScript injection with `dispatchEvent(new Event('change', { bubbles: true }))` to work. This wasted significant time debugging during the session.

### 2. Slow Page-by-Page Navigation
To get to NJ's "Taxes Paid to Another State" page, we had to click "Save and Continue" through ~10 intermediate NJ pages (Residency, Basic Info, Health Care, Wages, etc.). Later discovered the State dropdown in the top nav lets you jump directly to any page.

### 3. Session Timeout Interruptions
FreeTaxUSA's "Are you still there?" dialog appeared multiple times, blocking page interactions. Had to detect and dismiss it before continuing.

### 4. Context Compaction (Multiple Times)
The filing session was so long that the conversation context was compacted several times. Each time, the new session had to re-derive where we were, what had been entered, and what was next. No checkpoint file existed.

### 5. Inaccurate Manual Tax Computations
The tax_profile.json numbers didn't match FreeTaxUSA's. Discrepancies:
- Federal: $415 (manual) vs $295 (FreeTaxUSA) — $120 off
- NY: $3,025 refund (manual) vs $2,050 (FreeTaxUSA) — $975 off
- NJ: $197 refund (manual) vs $1,509 (FreeTaxUSA) — $1,312 off

Root causes: mortgage interest proration used beginning-of-year balance vs FreeTaxUSA's average balance method; NIIT computation slightly different; NJ and NY tax tables were approximated rather than using exact published tables.

### 6. No Section-End Verification
Verification only happened at the very end when the user uploaded the federal PDF. Should have been done after each major section (federal, NY, NJ) to catch issues earlier.

### 7. State Return Order Mattered
NJ's credit for taxes paid to NY depends on the NY allocated tax number. If we'd done NJ first, the credit would have been wrong. The skill didn't explicitly document this dependency.

### 8. Manual Entry Was Slow
Every W-2 box and 1099 field was manually typed. FreeTaxUSA likely offers import features for W-2s from major payroll providers, which would have been dramatically faster.

---

## The 8 Consolidated Improvements

These were developed through conversation between the user and the assistant. The user specifically requested combining related items (e.g., JS filling + nav map + batch entry + session timeouts into one "Platform UI Automation Layer").

### 1. Section-End Verification with Saved Screenshots
**What**: After completing each major section (federal, NY, NJ), produce a source-doc-vs-return comparison table with check/fail verdicts AND save a screenshot of the summary page.
**Why**: Verification only happened once at the end. Should be continuous.
**Where**: `file/instructions.md` — new "Section-End Verification (Mandatory)" section

### 2. Use Platform Import/Upload First, Verify Second
**What**: Before manual entry, check if the platform offers W-2/1099 import. If so, import and switch to verification mode.
**Why**: Manual entry of every W-2 box is slow and error-prone.
**Where**: `file/instructions.md` — new "Check for platform import/upload features" in Before Starting

### 3. Platform UI Automation Layer
**What**: Unified section covering JS-first form filling, navigation menu jumping, batch entry by page, and session timeout handling. FreeTaxUSA-specific patterns documented in a separate reference file.
**Why**: Combines four related issues (JS dropdowns, slow navigation, scattered entry, timeout interruptions) into one coherent approach.
**Where**: `file/instructions.md` — new "Platform UI Automation Layer" section; `references/platform_ui_patterns.md` — new file with FreeTaxUSA-specific and general patterns

### 4. Context Compaction Resilience (Checkpoint Files)
**What**: Save `filing_progress.json` after each major section with: sections done, sections remaining, key values entered, current page.
**Why**: Sessions get compacted. Without a checkpoint, the new session has to re-derive everything.
**Where**: `file/instructions.md` — new "Checkpoint Files" section

### 5. Precise Tax Computation from IRS/State Sources
**What**: Use exact IRS worksheets and state tax tables rather than approximate rate schedules. Document the mortgage interest proration formula explicitly. Link to NY, NJ, CA state tax table sources.
**Why**: Manual calculations were off by $120-$1,312 from the platform's numbers. The tax_profile.json should be as close as possible to what the platform computes.
**Where**: `prepare/instructions.md` — new "Precise Computation Requirements" in Step 4; `references/tax_rules.md` — expanded mortgage interest section with formula + new "Precise Computation Sources" section

### 6. Pre-flight Document Checklist
**What**: Before touching the browser, verify: all source docs extracted, W-2 totals match, withholding totals match, daycare EIN confirmed, donation details ready, multi-state residency confirmed.
**Why**: Missing or unconfirmed data discovered mid-filing costs much more time than catching it upfront.
**Where**: `file/instructions.md` — new "Pre-flight document checklist" in Before Starting

### 7. State Return Dependency Ordering
**What**: Always complete nonresident state returns before resident state returns. The resident state's credit depends on the nonresident state's tax figure.
**Why**: NJ's credit for taxes paid to NY requires the NY allocated tax number. Wrong order = wrong NJ refund.
**Where**: `file/instructions.md` — new "State Return Dependency Ordering" section; `prepare/instructions.md` — updated Step 6

### 8. Ancillary Filing Reminders as Saved Checklist
**What**: After filing, save `filing_reminders.md` with: FBAR filing instructions + link, RSU basis documentation to keep, record retention periods, key dates.
**Why**: FBAR is filed separately (fincen.gov), not as part of the tax return. Users forget.
**Where**: `file/instructions.md` — new "Ancillary Filing Reminders" section

---

## File Structure

```
tax/
  SKILL.md                              — Top-level router (which mode to use)
  README.md                             — This file
  prepare/
    instructions.md                     — Document extraction + tax computation
  optimize/
    instructions.md                     — Tax savings strategies
  file/
    instructions.md                     — Browser automation for filing (MOST CHANGES HERE)
  references/
    tax_rules.md                        — IRS rules: SALT, AMT, NIIT, brackets, etc.
    federal_forms_guide.md              — Which federal forms are needed and when
    state_tax_agencies.md               — Official URLs for all 50 states + DC
    platform_ui_patterns.md             — NEW: Browser automation patterns for FreeTaxUSA etc.
  scripts/
    cross_foot_check.py                 — Verification script for math errors
    generate_audit_trail.py             — Audit trail generation
```

---

## Key Design Decisions

**Why FreeTaxUSA as the default platform?**
Free for federal filing, $15 for state. Supports all forms needed for this filer's situation. The SPA architecture is automatable with Chrome tools. User already had an account.

**Why not just generate PDF forms directly?**
Tax filing platforms handle e-filing, payment processing, state integration, and error checking. Filling PDFs would produce paper returns that need to be mailed and don't get the benefits of e-file (faster refunds, confirmation).

**Why checkpoint files instead of relying on conversation context?**
A single filing session can consume the entire context window. When compacted, the new session loses all state. A JSON checkpoint survives compaction and lets the next session resume immediately.

**Why JS injection over mouse clicks?**
React SPAs use synthetic event systems. A mouse click at coordinates (x, y) may hit the visual element but not trigger React's event handlers. Setting the value via JS and dispatching the change event directly speaks React's language.

---

## For Future Iterations

Things that could improve the skill further but weren't addressed in this round:

1. **Automated state tax table lookup** — A script that scrapes current-year state tax tables from official sites and caches them locally, so prepare mode doesn't need to manually search
2. **Multi-year support** — Tracking carryforward items (capital losses, AMT credits) across tax years
3. **TurboTax / H&R Block profiles** — The platform_ui_patterns.md has stubs for other platforms but needs real testing
4. **Estimated tax payment calculator** — After filing, compute whether estimated payments are needed for next year to avoid underpayment penalties
5. **Document OCR** — Some users photograph their W-2s instead of having PDFs. Adding OCR support would handle this
6. **Parallel state entry** — If states are independent (e.g., two nonresident states), they could theoretically be entered in parallel

---

## Version History

| Date | Change |
|------|--------|
| 2025-03-31 | Initial skill created with prepare, optimize, and file modes |
| 2025-04-01 | Battle-tested with real MFJ multi-state filing on FreeTaxUSA |
| 2025-04-01 | 8 improvements applied: verification tables, import-first, UI automation layer, checkpoints, precise computation, pre-flight checklist, state ordering, filing reminders |
