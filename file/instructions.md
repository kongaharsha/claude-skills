# Tax File — Step-by-Step Instructions

Navigate a tax filing platform (FreeTaxUSA, TurboTax, etc.) live in the user's Chrome browser, filling in each section from the tax profile. The user watches, corrects, and submits — this skill handles the data entry and verification.

**Prerequisite**: Load `output/tax_profile.json`. If it doesn't exist, stop and tell the user to run `tax:prepare` first.

**Platform**: FreeTaxUSA (https://www.freetaxusa.com) is the default. If the user wants a different platform, the same section-by-section approach applies but navigation steps and field names will differ. See `references/platform_ui_patterns.md` for platform-specific automation guidance.

---

## Before Starting

### 1. Load and validate tax_profile.json

Confirm it has filers, income, deductions, federal totals, and state returns.

### 2. Pre-flight document checklist

Before touching the browser, verify everything is ready. This catches problems that cost minutes now instead of hours later.

- [ ] Every source document in the extraction ledger has been verified by the user
- [ ] W-2 box 1 totals match expected combined wages
- [ ] All 1099-DIV, 1099-INT, 1099-B amounts sum correctly
- [ ] State withholding totals match per W-2 box 17
- [ ] Mortgage interest from 1098 is accounted for (including $750K debt limitation if applicable)
- [ ] FBAR status is noted (file separately at fincen.gov)
- [ ] Daycare provider name, address, and EIN are confirmed (if CDCC claimed)
- [ ] Noncash donation details are ready (org name, description, FMV, method)
- [ ] For multi-state filers: confirm which state is resident, which is nonresident

If anything is missing or unconfirmed, ask the user before proceeding.

### 3. Check for platform import/upload features

Many tax platforms let you import W-2s and 1099s directly from payroll providers or brokerages. This is dramatically faster than manual entry and less error-prone.

Before manually entering any W-2 or 1099:
1. Check whether the platform offers an import option (FreeTaxUSA: look for "Import W-2" or "Import 1099" buttons on the entry pages)
2. If import is available, ask the user: "FreeTaxUSA can import your W-2 directly from [employer's payroll provider]. Want to try that? It'll be much faster — I'll verify everything after it imports."
3. If the user imports, switch to **verification mode** — read each imported field against the extraction ledger and flag any mismatches, rather than entering from scratch

Only fall back to manual entry when import isn't available or doesn't work.

### 4. Tell the user the plan

"I'll navigate the platform section by section and fill in your information. Please open Chrome and log in. Tell me when you're ready and which tax year to file."

Wait for confirmation before starting.

---

## Platform UI Automation Layer

Read `references/platform_ui_patterns.md` for the full reference. The key principles:

### Use JavaScript-first form filling

Tax filing platforms are typically React/SPA apps where simulated mouse clicks don't always register. Default to JavaScript injection for setting field values:

```javascript
// Set an input field
const el = document.querySelector('input[name="fieldName"]');
el.value = 'new value';
el.dispatchEvent(new Event('input', { bubbles: true }));
el.dispatchEvent(new Event('change', { bubbles: true }));

// Set a dropdown/select
const select = document.querySelector('select[name="fieldName"]');
select.value = 'optionValue';
select.dispatchEvent(new Event('change', { bubbles: true }));
```

Fall back to mouse clicks only when JS doesn't work (e.g., custom non-native UI components).

### Jump directly via navigation menus

Don't click "Save and Continue" through 10+ intermediate pages to reach a specific section. Use the platform's navigation menu to jump directly. On FreeTaxUSA, the top nav bar has dropdown menus (Personal, Income, Deductions/Credits, Misc, Summary, State, Final Steps) that let you click straight to any page.

### Batch entry by page structure

Before entering data, map all source data to the platform's page structure. Then fill each page with all relevant data in one pass rather than navigating back and forth between pages and documents.

### Handle session timeouts proactively

Before any page interaction, check for and dismiss blocking modals (session timeout warnings, maintenance alerts, loading overlays). On FreeTaxUSA, look for the "Are you still there?" dialog and click "Continue" to dismiss it.

---

## Checkpoint Files — Context Compaction Resilience

Long filing sessions often exceed context limits and get compacted. To survive this gracefully, save a checkpoint file after completing each major section.

Save to `work/filing_progress.json`:
```json
{
  "platform": "FreeTaxUSA",
  "tab_id": 1645298232,
  "last_completed_section": "federal_deductions",
  "sections_done": ["personal", "income_w2", "income_investments", "income_other", "federal_deductions"],
  "sections_remaining": ["federal_credits", "federal_misc", "state_ny", "state_nj", "review"],
  "key_values_entered": {
    "total_wages": 523606,
    "agi": 534903,
    "itemized_deductions": 80747
  },
  "discrepancies_noted": [],
  "timestamp": "2026-04-01T14:30:00Z"
}
```

When resuming from a compacted session:
1. Read `filing_progress.json` to understand where you left off
2. Navigate directly to the next incomplete section (using the nav menu, not clicking through completed pages)
3. Continue from there

---

## State Return Dependency Ordering

When filing in multiple states, the order matters because the resident state's credit for taxes paid to another state depends on the nonresident state's tax being computed first.

**Always complete nonresident state returns before resident state returns.**

For example, if the user is a NJ resident who works in NY:
1. Complete NY IT-203 (nonresident) first → get the NY allocated tax figure
2. Then complete NJ-1040 (resident) → enter the NY tax as a credit on NJ Schedule A

If you do NJ first, you won't have the NY tax number for the credit, and the NJ refund/owed will be wrong.

---

## Navigation Principles

Work through the platform in the order of its menu structure. Before filling each section:
1. Navigate to it (using the nav menu to jump directly)
2. Tell the user which section you're filling and the key values about to go in
3. Fill the fields
4. Confirm with the user before clicking Continue past any section

**Never click "File" or "Submit"** — that's the user's action after their own final review.

If the platform's computed total for any section differs from `tax_profile.json` by more than $10, stop and tell the user before moving on.

---

## Section Order

### 1. Personal → Taxpayer Information

From `tax_profile.filers.primary`:
- First name, middle initial (if any), last name
- SSN (9 digits, no dashes)
- Date of birth
- Occupation
- IP PIN (if `ip_pin` is populated)

### 2. Personal → Spouse Information (MFJ only)

From `tax_profile.filers.spouse` — same fields.

### 3. Personal → Filing Status

Select the status from `tax_profile.filing_status`.

### 4. Personal → Address

From `tax_profile.address`.

### 5. Personal → Dependents

For each entry in `tax_profile.dependents`:
- Click "Add a Dependent"
- Name, SSN, date of birth, relationship
- Months lived in home
- Whether they qualify for Child Tax Credit (`qualifying_child: true`)

### 6. Income → Wages (W-2)

For each entry in `tax_profile.income.{filer}.w2_employers`, click "Add W-2" and fill:
- Employer name, EIN
- Box 1 wages, Box 2 federal withholding
- Box 3 SS wages, Box 4 SS tax, Box 5 Medicare wages, Box 6 Medicare tax
- Box 12 codes (e.g., D = traditional 401k, S = SIMPLE IRA, W = employer HSA)
- State wages and state tax for each state in `box_16_state_wages` / `box_17_state_tax`

Repeat for both filers (MFJ).

### 7. Income → Interest & Dividends

- Ordinary dividends (per filer from `income.{filer}.ordinary_dividends`)
- Qualified dividends (per filer from `income.{filer}.qualified_dividends`)
- Taxable interest (per filer from `income.{filer}.interest`)
- Foreign tax paid (from `income.{filer}.foreign_tax_paid`, if > $0 — feeds Schedule 3 FTC)

### 8. Income → Capital Gains (Schedule D / Form 8949)

For each 1099-B group:
- Enter by box category: Box A (ST covered), Box B (ST uncovered), Box D (LT covered), Box E (LT uncovered)
- If cost basis was adjusted (e.g., RSU shares where basis = $0 on 1099-B but actual basis = FMV at vest), make the adjustment here and note it with a brief explanation
- Verify the platform's Schedule D net totals match `tax_profile.federal.st_gains` and `lt_gains`

### 9. Income → Other Income

For each entry in `income.{filer}.other_income`:
- Select the appropriate form type (1099-MISC, 1099-NEC, etc.)
- Enter payer name and amount

### 10. Deductions → Itemized (Schedule A)

If `tax_profile.deductions.type == "itemized"`:
- State and local taxes: enter `deductions.salt_paid` (the actual amount paid — the platform applies the cap automatically; do not manually apply the cap)
- Property taxes: enter `deductions.property_tax` (included in SALT total — confirm the platform handles correctly)
- Mortgage interest: enter `deductions.mortgage_interest` from `deductions.mortgage_lender`
- Charitable cash: `deductions.charitable_cash`
- Charitable non-cash: `deductions.charitable_noncash`

If `deductions.type == "standard"`, confirm the platform has selected the standard deduction.

### 11. Credits

- **Child Tax Credit / Other Dependent Credit**: auto-calculated from dependent entries — verify it matches `federal.credits.ctc`
- **Child and Dependent Care Credit**: enter care provider(s), EIN/SSN, amounts paid per dependent. Verify total matches `federal.credits.cdcc`
- **Foreign Tax Credit**: enter foreign taxes paid (from dividends/interest). Verify matches `federal.credits.ftc`
- **Education Credits**: enter 1098-T details if applicable

### 12. Other Taxes

Navigate to the Other Taxes section:
- Additional Medicare Tax: auto-calculated from Medicare wages — verify it matches `federal.additional_medicare`
- NIIT: auto-calculated — verify it matches `federal.niit`

### 13. State Returns

**Follow the dependency ordering** described above: nonresident states first, then resident state.

For each state return:
- The platform pre-fills most fields from the federal return
- Review each screen and correct any pre-populated value that looks wrong
- For nonresident states, enter the in-state income amount when prompted
- For the resident state, enter the credit for taxes paid to other states

### 14. Review & Finalize

Navigate to the Review / Summary screen:
- Go through every flagged item. For missing entries that should exist, fill them in. For items that genuinely don't apply, dismiss them.
- Verify the platform's bottom-line totals match `tax_profile`:
  - Total Tax: `federal.total_tax`
  - Total Payments: `federal.total_payments`
  - Owed / Refund: `federal.owed` or `federal.refund`

### 15. Banking (Refund/Payment)

If refund: navigate to direct deposit and enter `tax_profile.banking` (routing, account number, account type).
If owed: confirm payment method (IRS Direct Pay or credit card) and remind the user of the April 15 deadline.

---

## Section-End Verification (Mandatory)

After completing each major section (federal, each state return), produce a verification summary and save a screenshot. This is the "close out" step — the analytical check plus the visual receipt.

### What to produce

**1. Source-doc-vs-return comparison table:**

Compare every key number on the return against the original source document in the extraction ledger. Format:

```
## Federal Return Verification

| Line Item | Return | Source | Source Doc | Verdict |
|-----------|--------|--------|------------|---------|
| Wages (1a) | $523,606 | $332,306 + $191,300 | W-2s | ✓ |
| Ordinary dividends | $4,163 | $2,878 + $1,285 | 1099-DIVs | ✓ |
| Mortgage interest | $49,718 | $50,192 (1098) | PHH Mortgage | ⚠ $474 diff — $750K debt limit |
...
```

Key items to always verify:
- All income lines against source W-2s and 1099s
- Itemized deductions against source 1098, property tax statements
- Withholding totals against W-2 box 2 (federal) and box 17 (state)
- Credits (CDCC, FTC) against source amounts
- AGI, taxable income, total tax, balance owed/refund

For state returns, also verify:
- State-specific income (nonresident allocation percentage, NY source income, NJ wages)
- State withholding matches W-2 box 17 for that state
- Credit for taxes paid to another state (if multi-state)

**2. Screenshot of the summary page:**

Take a screenshot of the platform's summary page for this section and save it to the working folder as an audit trail receipt:

```
work/screenshots/federal_summary.jpg
work/screenshots/ny_summary.jpg
work/screenshots/nj_summary.jpg
```

### When to produce

- After federal entry is complete and you're on the Federal Summary page
- After each state return is complete and you're on that state's Summary page
- At the very end, after the final review

### Discrepancies

If the platform's computation differs from tax_profile.json:
1. Note the field and both values in the verification table
2. Explain the likely reason (e.g., "the platform uses exact IRS tax tables while our estimate used rate schedules")
3. If the difference is small (<$200) and explainable, flag it as ⚠ but don't block
4. If the difference is large or unexplainable, stop and ask the user

---

## Ancillary Filing Reminders

After all sections are verified and the return is ready to file, save `work/filing_reminders.md`:

```markdown
# Filing Reminders — {YEAR} Tax Return

## Before submitting
- [ ] Review all flagged items on the Review page
- [ ] Confirm direct deposit / payment info is correct
- [ ] Both filers sign (if MFJ)

## After filing
- [ ] Save confirmation numbers for federal and each state
- [ ] FBAR: File FinCEN 114 at https://bsaefiling.fincen.treas.gov by April 15 (auto-extends to Oct 15)
- [ ] Keep documentation for items requiring proof (RSU basis, noncash donations, daycare provider EIN)
- [ ] Form 8938 (FATCA): Check whether foreign asset thresholds were exceeded

## Key dates
- April 15: Federal and state returns due; payment due even if extended
- April 15: FBAR due (auto-extends to October 15)
- June 15: Q2 estimated tax payment due (if applicable for next year)

## Records to retain
- W-2s and 1099s: 3 years minimum (7 years recommended)
- Property tax statements: keep while you own the property + 3 years after sale
- Mortgage interest (1098): keep while you have the mortgage + 3 years
- Noncash donation receipts: keep for 3 years (7 years if > $5,000)
- RSU cost basis documentation: keep until 3 years after you sell the shares
```

---

## Handling Discrepancies

When the platform's figure doesn't match `tax_profile.json`:
1. Note the field and both values
2. Check whether the platform is computing something correctly that differs from the estimate (it recalculates things like SALT cap, mortgage interest limitation, and AMT internally using exact IRS worksheets)
3. If it's a genuine discrepancy, tell the user: "The platform shows $X for [field] but our summary shows $Y. The difference appears to be [reason]. Which looks right?"
4. Resolve before continuing

---

## Key Gotchas

**SALT**: Enter the actual state taxes paid. The platform caps it automatically — entering the pre-capped amount would understate the deduction.

**Digital assets question**: "Did you receive, sell, exchange, or otherwise dispose of any digital assets?" — Digital assets = crypto only. Stocks, ETFs, RSUs are not digital assets. Answer based on `tax_profile.digital_assets`.

**Prior year AGI**: Required for e-file identity verification. Use `tax_profile.prior_year_agi`.

**FBAR**: If `tax_profile.fbar_required == true`, remind the user that FinCEN 114 (FBAR) must be filed separately at https://bsaefiling.fincen.treas.gov.

**1099-B adjusted basis**: If cost basis was $0 on the 1099-B but the actual basis is the FMV at vest (RSU case), adjust in Form 8949. Entering $0 basis causes double taxation.

**Session timeout**: The platform auto-saves. If the session times out, dismiss the dialog and navigate back using the nav menu.
