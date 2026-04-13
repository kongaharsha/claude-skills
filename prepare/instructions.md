# Tax Prepare — Step-by-Step Instructions

Build the complete tax picture from source documents. Produces a 4-section chat summary, a formatted Excel spreadsheet, a structured `tax_profile.json` for filing, and a forms-required list. Does **not** fill or download any PDF forms.

---

## Step 0: Initialize

Ask the user to confirm their tax documents folder. Create the working directory structure (source/, work/, output/) if it doesn't exist.

---

## Step 0.5: Scan, Stage & Confirm Documents

Before extracting anything, scan the folder for what's there, move files into `source/` with consistent names, and check for obvious gaps. Missing documents discovered now cost minutes; discovered after extraction cost hours.

### Scan and rename

List all files in the user's folder. For each file, peek at the first page with pdfplumber to detect the form type (look for "W-2", "1099-DIV", "1099-B", "1099-INT", "1099-MISC", "1099-NEC", "1098", "1098-T", "5498", "1099-SA", etc. in the document text). Rename and move to `source/` using the convention `{firstname}_{formtype}.{ext}`:

```bash
python3 -c "
import pdfplumber, os, shutil
# Quick peek — first page only, don't save to tax_data.txt yet
with pdfplumber.open('path/to/file.pdf') as pdf:
    text = pdf.pages[0].extract_text() or ''
    print(text[:500])
"
```

Present a table of what was found before doing anything else:

```
📂 Documents found (12 files):

  Filer          Form        File                         Detected as
  ─────────────────────────────────────────────────────────────────────
  Alex           W-2         alex_google_W2.pdf           ✓ W-2 (Employer: Google)
  Jordan         W-2         jordan_amazon_W2.pdf         ✓ W-2 (Employer: Amazon)
  Alex           1099-DIV    alex_robinhood_1099DIV.pdf   ✓ 1099-DIV
  Joint          1098        mortgage_phh_1098.pdf        ✓ 1098 (Lender: PHH)
  Unknown        statement.pdf                            ⚠ Unrecognized — please confirm type
  ...
```

Ask the user to confirm any unrecognized files and correct any misdetections before proceeding.

### Completeness check

After staging, run through the checks below. Ask only about gaps that are genuinely plausible given what you see — don't ask about forms that clearly don't apply. Group related questions into a single message rather than asking one at a time.

**Income gaps:**

| What you see | What to check |
|---|---|
| W-2 for one filer only (MFJ) | "Does [spouse] have employment income? If yes, I'd expect a second W-2." |
| W-2 for both but 1099-DIV for only one | "Does [filer] have any brokerage or investment accounts?" |
| W-2 with Box 12 code W (employer HSA) | "I see an employer HSA contribution. Do you have a 1099-SA for HSA distributions this year, or a 5498-SA year-end balance statement?" |
| W-2 with Box 12 code D/S/AA (retirement) | "Did either of you make any IRA contributions (traditional or Roth) this year outside of work?" |
| 1099-B present | "Did you have any cost basis adjustments — for example, RSU shares sold where the broker may have reported $0 basis?" |
| No 1099-INT but has brokerage accounts | "Do you have savings accounts, CDs, money market funds, or Treasury bonds? Those generate taxable interest on a 1099-INT." |
| No 1099-DIV but has W-2 income > $200k | "Do you have any brokerage or investment accounts with dividends?" |
| 1099-MISC / 1099-NEC present | "Is this freelance/self-employment income? If so, do you have any related business expenses to deduct?" |

**Deduction gaps:**

| What you see | What to check |
|---|---|
| No 1098 (mortgage interest) | "Do you own a home? If yes, your lender should have sent a Form 1098 for mortgage interest." |
| 1098 present but no property tax statement | "Do you have documentation of property taxes paid? (County tax bill, escrow statement, or Form 1098 if taxes are included)" |
| No charitable donation records | "Did you make any charitable donations this year? Cash, checks, or non-cash (clothing, goods)?" |
| High AGI, no state tax summary | "I'll pull state tax withholding from your W-2s, but did you make any estimated state tax payments during the year?" |

**Family & dependents:**

| What you see | What to check |
|---|---|
| Dependents confirmed (any age) | "Do you have any childcare or daycare expenses? (Form 2441 / Dependent Care Credit)" |
| Child under 18 | "Did you contribute to a 529 plan this year?" |
| Child in college | "Did you receive a 1098-T from their school? Any student loan interest (1098-E)?" |

**Other:**

| What you see | What to check |
|---|---|
| Prior year return present | "I'll use this for last year's AGI (needed for e-filing) and to check for capital loss carryovers." |
| No prior year return | "Do you know your prior year AGI? It's needed for e-filing identity verification. It's on line 11 of last year's 1040." |
| FBAR flagged | "For the FBAR, do you have a list of your foreign accounts with their maximum balances during the year?" |

### Confirm before proceeding

Once you've presented the gap questions, wait for the user's responses. If they upload additional files, scan and stage them too. Then confirm:

> "I have [N] documents staged in source/. Here's the final list: [table]. Does this look complete? I'll proceed with extraction once you confirm."

Only move to Step 1 after the user gives the go-ahead.

---

## Step 1: Extract Source Documents

All files are already staged in `source/` from Step 0.5. Now do the full extraction — every relevant number from every document. Use pdfplumber for PDFs, Read tool for CSVs/text:

```bash
python3 -c "
import pdfplumber
with pdfplumber.open('source/doc.pdf') as pdf:
    for p in pdf.pages: print(p.extract_text())
"
```

Save everything to `work/tax_data.txt` — one clearly labeled section per document with every relevant number. Never re-read source documents after this step.

### Step 1.5: Build the Source Data Extraction Ledger — MANDATORY

After reading ALL source documents, generate `work/extraction_ledger.json`. This is the single source of truth for every number used downstream. The most common tax prep error is misattributing income to the wrong filer — this ledger prevents it by requiring every value to be explicitly linked to a person and document.

```json
{
  "tax_year": 2025,
  "filers": {
    "primary": { "first_name": "...", "last_name": "...", "ssn_last4": "..." },
    "spouse":  { "first_name": "...", "last_name": "...", "ssn_last4": "..." }
  },
  "documents": [
    {
      "file": "source/alex_W2.pdf",
      "type": "W-2",
      "filer": "primary",
      "issuer": "Employer Name",
      "values": {
        "box_1_wages": 0.00,
        "box_2_fed_wh": 0.00,
        "box_3_ss_wages": 0.00,
        "box_4_ss_tax": 0.00,
        "box_5_medicare_wages": 0.00,
        "box_6_medicare_tax": 0.00,
        "box_12": { "D": 0.00 },
        "box_16_state_wages": { "NJ": 0.00 },
        "box_17_state_tax": { "NJ": 0.00 }
      }
    }
  ]
}
```

**Show this to the user as a readable table** — grouped by filer, then document type — and ask them to confirm it looks right before proceeding. This is the checkpoint where misreads and wrong-person attribution get caught before they cascade.

---

## Step 2: Confirm Filing Details — MANDATORY

Ask the user to confirm these before computing. Do not skip even if you think you know the answers from memory:

- Filing status (Single / MFJ / MFS / HOH / QSS)
- Dependents: names, relationship, approximate DOBs
- State(s) of residence, and any states where income was earned (nonresident filing)
- Deduction preference: standard, itemized, or "figure out which is better"
- Digital assets / crypto transactions (yes/no) — stock trades are NOT digital assets
- Health coverage: employer, ACA marketplace, or none
- Estimated tax payments made during the year
- Foreign financial accounts or assets (yes/no) — triggers FBAR/FinCEN 114 if yes
- Other income or situations: rental property, self-employment, HSA, IRA contributions or conversions, education credits, energy credits, alimony, gambling winnings

"Same as last year" counts as confirmation. Do not proceed until answered.

After confirmation, cross-check your documents against the stated income sources. Flag any gaps:
> "You mentioned rental income — I don't see a Schedule E or 1099-MISC from a property manager. Want to upload it, or continue without it?"

---

## Step 3: Look Up Current-Year Tax Values

Search `irs.gov` for the current tax year. Refer to `references/tax_rules.md` for what to look up and where to find it. Key items:

- Federal income tax brackets (for the confirmed filing status)
- Standard deduction
- QDCG thresholds (0%/15%/20%)
- Additional Medicare Tax threshold and rate
- NIIT threshold and rate
- SALT cap (check for OBBBA or current-year updates)
- Any other limits relevant to this filer's situation (CTC phase-out, AMT exemption, etc.)

For state taxes, use `references/state_tax_agencies.md` to find the official state URL, then navigate to the individual income tax section for brackets and credits.

Save all looked-up values to `work/computations.txt`.

---

## Step 4: Compute the Federal Return

Work through in order, annotating every step in `work/computations.txt`:

1. **Gross income by category and by filer**: W-2 wages, interest, ordinary dividends, qualified dividends, capital gains/losses, business income, other income
2. **Adjustments** (401k, HSA, student loan interest, etc.) → AGI
3. **Deduction comparison**: compute itemized total AND standard deduction; show which is larger and by how much
4. **Taxable income** = AGI − winning deduction
5. **Tax**: use QDCG worksheet if qualified dividends or long-term capital gains exist
6. **Additional Medicare Tax** (0.9% on Medicare wages over threshold — see `references/tax_rules.md`)
7. **Net Investment Income Tax** (3.8% on lesser of NII or MAGI over threshold)
8. **Credits**: CTC, CDCC, FTC, education — compute each; note phase-outs
9. **Total tax** → subtract withholding and estimated payments → refund or amount owed

### Precise Computation Requirements

The tax_profile.json numbers will be compared against the filing platform's exact computations during the `tax:file` step. To minimize discrepancies, use precise formulas rather than rough estimates:

**Mortgage interest limitation**: If outstanding mortgage principal exceeds $750K (post-Dec 2017 loans), prorate:
```
Deductible interest = Total interest × ($750,000 / outstanding principal)
```
Use the 1098 Box 2 (outstanding mortgage principal) for this calculation.

**NIIT (Form 8960)**: Follow the Form 8960 instructions exactly. Net Investment Income = interest + dividends + capital gains + other investment income − investment expenses. Tax = 3.8% × lesser of (NII, MAGI − $250K threshold for MFJ).

**State tax computation**: Look up the actual state tax tables or rate schedules for the filing year from the state agency website (see `references/state_tax_agencies.md`). Don't estimate state taxes from approximate brackets — use the published tables. NY and NJ both publish tax computation worksheets that should be followed step by step.

**Federal income tax**: Use the QDCG worksheet (from IRS 1040 instructions) when qualified dividends or LTCG exist — don't just apply bracket rates to all taxable income.

When a precise calculation isn't possible (e.g., state tax tables for the current year haven't been published yet), note the uncertainty explicitly in computations.txt rather than presenting an estimate as if it were exact.

For itemized deductions, always show the full SALT calculation explicitly:
```
SALT paid total: $X
Base cap: $Y
Excess AGI: AGI − threshold = $Z
Phase-out: $Z × rate% = $reduction
Allowed SALT: $Y − $reduction = $allowed
```

Refer to `references/tax_rules.md` for current SALT cap, phase-out threshold, and phase-out rate.

### Step 4.5: Cross-Foot Checks — MANDATORY

Run `scripts/cross_foot_check.py` after computing. This catches math errors and misattributions before they matter:

```bash
python scripts/cross_foot_check.py work/extraction_ledger.json work/results.json
```

Fix any failures. Show the pass/fail report to the user.

---

## Step 5: Capital Gains (if applicable)

If there are 1099-B transactions:
1. Group into short-term (held ≤1 year) and long-term buckets
2. Net gains and losses within each bucket
3. Apply $3,000 annual loss limitation; compute carryover for next year
4. Net result feeds into 1040 Line 7 and QDCG worksheet

**RSU same-day sale trap**: If the 1099-B shows $0 cost basis on RSU shares but the employer reported the full vest value as W-2 income, the actual cost basis is the FMV at vest. Flag this explicitly — it prevents double taxation.

---

## Step 6: State Returns

**Dependency ordering**: When filing in multiple states, always compute nonresident state returns first, then the resident state. The resident state's credit for taxes paid to other states depends on the nonresident state's tax figure being computed first.

For example: NJ resident who works in NY → compute NY IT-203 (nonresident) first, then NJ-1040 (resident) using the NY allocated tax for the NJ credit.

For each state (nonresident first, then resident):
1. Start from Federal AGI → apply state-specific additions and subtractions (e.g., NY adds back tax-exempt interest; NJ doesn't allow 401k deductions)
2. Look up the actual state tax tables or rate schedules for the filing year from the state agency website — don't approximate
3. Apply state brackets → gross state tax
4. Subtract credits (especially credit for taxes paid to other states for multi-state filers)
5. Subtract state withholding and estimated payments → refund or owed

Use `references/state_tax_agencies.md` for state agency URLs.

---

## Step 6.5: Build the Summary Spreadsheet

Produce `output/{YEAR} Tax Summary - {Filer Names}.xlsx` using openpyxl. The filer names in the filename come from the extraction ledger (`filers.primary.last_name` etc.).

**Column structure:**
- MFJ: [Primary first name] | [Spouse first name] | Combined | Commentary
- Single/HOH: Amount | Commentary
- Column headers use actual first names from the ledger — not generic "Filer 1"

**Sections:**
1. Income Summary (W-2, 1099-DIV, 1099-INT, 1099-B, 1099-MISC/NEC, other)
2. Adjustments to Income → AGI
3. Deductions (itemized vs standard comparison; SALT cap with full calculation shown)
4. Federal Tax Computation (brackets, QDCG, AMT check)
5. Additional Taxes (Additional Medicare Tax, NIIT)
6. Credits
7. Payments & Withholding (per-filer breakdown)
8. Federal Balance
9. State Returns (one sub-section per state)
10. Net Cash Position (total owed or refunded across all jurisdictions)
11. Key Rules Applied (plain-English row-by-row explanations)

**Commentary column**: explain why each number is what it is — the rule that applies, the limit that kicked in, what it means in plain English.

**Data integrity:**
- Dollar values must be numbers (`ws['B6'] = 332306.30`), never strings (`"$332,306.30"`)
- Combined column: `=B{row}+C{row}` formulas, not hardcoded totals
- Per-person columns reflect actual per-document amounts from the ledger
- After building, recalculate with LibreOffice headless:
  ```bash
  libreoffice --headless --calc --convert-to xlsx "output/summary.xlsx" --outdir /tmp/recalc
  cp /tmp/recalc/summary.xlsx output/summary.xlsx
  ```

---

## Deliverables

### 1. Chat Summary (4 sections — show in conversation AND save as .md)

After all computations, display this directly in the conversation. Labels use filer first names from the extraction ledger:

```
#### {YEAR} Tax Return Summary — {Filing Status} — {Filer Name(s)}

#### 1. Gross Income
- W-2 Wages ({Filer name}, {Employer}): ${amount}
  [one line per W-2 per filer]
- Investment Income ({Filer name}, {Brokerage}): ${amount} (ord div ${x}, qual div ${x})
  [one line per 1099-DIV per filer; omit if $0]
- Interest ({Filer name}, {Institution}): ${amount}
  [omit if $0]
- Capital Gains ({Filer name}): ${net} net (ST: ${st}, LT: ${lt}) — {brief note if basis adjusted}
  [omit if $0]
- Other Income ({Filer name}, {Source}): ${amount} [{form type}]
  [one line per 1099-MISC/NEC/other; omit if $0]
- **Total AGI: ${agi}**

#### 2. Itemized Deductions
Itemized (${itemized}) vs Standard (${standard}) — {which wins and by how much}
- {Deduction type} ({Provider/detail}): ${amount}
  [one line per deduction item; show SALT with full phase-out math]
  - SALT paid: ${salt_paid}. Cap: ${base_cap}. AGI ${agi} is ${excess} over ${threshold} →
    ${excess} × {rate}% = ${reduction} reduction → Allowed: ${allowed}
- **Total Itemized Deductions: ${total}**
- **Taxable Income: ${taxable_income}**

#### 3. Federal Tax
- Income Tax: ${tax} ({rate}% on ordinary income; {rate}% on qualified dividends/LTCG)
- Additional Medicare Tax: ${amt} (0.9% on wages over ${threshold})  [omit if $0]
- Net Investment Income Tax: ${niit} (3.8% on ${nii} of investment income)  [omit if $0]
- Credits: −${credits} ({breakdown})  [omit if $0]
- **Total Federal Tax: ${total_tax}**

#### 4. Federal Payments & Balance
- Federal Withholding ({Filer name}): ${amount}
  [one line per filer]
- Estimated Payments: ${est}  [omit if $0]
- **Total Paid: ${total_paid}**
- **FEDERAL BALANCE: {Owe / Refund} ${balance}**
  {1-2 sentence plain-English explanation of the main driver}
```

After displaying the summary, link to the spreadsheet:
> 📊 [View full Tax Summary](computer://{absolute_path_to_xlsx})

Save this summary to `output/{YEAR} Tax Summary - {Filer Names}.md`.

### 2. Forms Required

Save `output/forms_required.md`. Use `references/federal_forms_guide.md` to determine which forms apply, then list only those relevant to this filer's actual situation. Generic template:

```markdown
# Forms Required — {YEAR} Tax Return

## Federal
| Form | Title | Applies because |
|------|-------|-----------------|
| Form 1040 | U.S. Individual Income Tax Return | Always required |
| Schedule A | Itemized Deductions | Itemized deductions exceed standard |
...

## State
| State | Form | Residency | Applies because |
|-------|------|-----------|-----------------|
...

## Other
| Item | Description |
|------|-------------|
| FinCEN 114 (FBAR) | Foreign bank account with aggregate balance > $10,000 |
...
```

### 3. Tax Profile JSON

Save `output/tax_profile.json`. This is the handoff file — `tax:optimize` and `tax:file` both read it. Include everything needed to complete an online tax return without going back to source documents:

```json
{
  "tax_year": 0,
  "filing_status": "",
  "filers": {
    "primary": {
      "first_name": "", "last_name": "", "ssn": "", "dob": "",
      "occupation": "", "ip_pin": null
    },
    "spouse": { ... }
  },
  "address": { "street": "", "city": "", "state": "", "zip": "" },
  "dependents": [
    { "name": "", "ssn": "", "dob": "", "relationship": "", "months_in_home": 12,
      "qualifying_child": true }
  ],
  "income": {
    "primary": {
      "w2_wages": 0.00, "w2_fed_wh": 0.00,
      "w2_employers": [{ "name": "", "ein": "", "wages": 0.00, "fed_wh": 0.00,
                         "ss_wages": 0.00, "ss_tax": 0.00,
                         "medicare_wages": 0.00, "medicare_tax": 0.00,
                         "box_12": {}, "state_wages": {}, "state_tax": {} }],
      "ordinary_dividends": 0.00, "qualified_dividends": 0.00,
      "interest": 0.00, "foreign_tax_paid": 0.00,
      "capital_gains_net": 0.00, "st_gains": 0.00, "lt_gains": 0.00,
      "cap_loss_carryover": 0.00,
      "other_income": [{ "type": "", "payer": "", "amount": 0.00 }]
    },
    "spouse": { ... }
  },
  "adjustments": { "primary_401k": 0.00, "spouse_401k": 0.00, "hsa": 0.00, "other": 0.00 },
  "deductions": {
    "type": "itemized",
    "salt_paid": 0.00, "salt_allowed": 0.00,
    "salt_cap_base": 0.00, "salt_phase_out_reduction": 0.00,
    "mortgage_interest": 0.00, "mortgage_lender": "",
    "property_tax": 0.00,
    "charitable_cash": 0.00, "charitable_noncash": 0.00,
    "other_itemized": []
  },
  "federal": {
    "agi": 0.00, "taxable_income": 0.00,
    "income_tax": 0.00, "additional_medicare": 0.00, "niit": 0.00,
    "credits": { "ctc": 0.00, "cdcc": 0.00, "ftc": 0.00, "education": 0.00 },
    "total_tax": 0.00, "total_payments": 0.00, "owed": 0.00, "refund": 0.00
  },
  "state_returns": [
    { "state": "", "form": "", "residency": "resident",
      "taxable_income": 0.00, "tax": 0.00, "withholding": 0.00,
      "owed": 0.00, "refund": 0.00 }
  ],
  "banking": { "routing": null, "account": null, "account_type": null },
  "prior_year_agi": null,
  "digital_assets": false,
  "fbar_required": false,
  "cap_loss_carryover_to_next_year": 0.00
}
```
