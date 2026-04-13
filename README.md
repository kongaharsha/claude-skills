# tax

> I filed my entire federal + multi-state tax return with an AI agent. No accountant. No $400 TurboTax upsell. Just source documents, Claude Code, and this skill.

I'm [Harsha Konga]. I built this skill after spending hours every April wrestling with tax software, lack of transparency. The skill was battle-tested on a real MFJ multi-state return — W-2s, 1099s, RSU sales, mortgage interest, SALT cap, NIIT, the works — and filed end-to-end on FreeTaxUSA.

**tax** turns Claude Code into a tax professional. Three modes: prepare your return from raw documents, find optimization opportunities you missed, and file it live in the browser — all slash commands, all Markdown, free.

**Who this is for:**
- **Anyone who files their own taxes** — structured process instead of guessing which box goes where
- **multi-state filers** — handles itemized deductions, state credits, phase-outs, and forms most people get wrong
- **People who want to understand their taxes** — every number is traced back to a source document with full audit trail

## Quick start

1. Install the skill (see below)
2. Drop your tax documents (W-2s, 1099s, 1098s) into the conversation
3. Run `/tax:prepare` — get a complete tax summary with spreadsheet
4. Run `/tax:optimize` — find deductions and strategies you missed
5. Run `/tax:file` — fill out FreeTaxUSA in a real browser, hands-free

## Install

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

### Option 1: Download the `.skill` file

Download `tax.skill` from the [latest release](../../releases/latest) and drop it into Claude Code. That's it.

### Option 2: Clone into your skills directory

```bash
git clone --depth 1 https://github.com/kongaharsha/tax.git ~/.claude/skills/tax
```

Then add to your project's `CLAUDE.md`:

```markdown
## tax
Available skills: /tax:prepare, /tax:optimize, /tax:file
```

## See it work

```
You:    Here are my W-2, two 1099-DIVs, a 1099-B, and my mortgage 1098.
You:    /tax:prepare

Claude: [extracts every number from every document]
        [builds extraction ledger — each value traced to source doc + page]
        [computes federal: income, adjustments, deductions, credits, tax]
        [computes state: NJ resident + NY nonresident with credit ordering]
        [cross-foots all math — flags any discrepancies]

        Here's your 2025 tax summary:
        ┌─────────────────────────────────┐
        │ Federal AGI        $534,903     │
        │ Federal tax owed       $295     │
        │ NY refund            $2,050     │
        │ NJ refund            $1,509     │
        │ Net refund          ~$3,264     │
        └─────────────────────────────────┘
        [saves tax_profile.json + formatted spreadsheet]

You:    /tax:optimize

Claude: [reads your tax profile]
        Found 4 opportunities:
        1. Backdoor Roth IRA — saves ~$2,400/yr at your bracket
        2. Mega backdoor Roth — check if employer plan allows
        3. Donor-advised fund bunching — itemize $24K+ in donations
           every other year instead of $12K each year
        4. HSA via spouse's plan — triple tax advantage

You:    /tax:file

Claude: [opens FreeTaxUSA in Chrome]
        [pre-flight check: all docs extracted ✓, totals match ✓]
        [enters federal: W-2s, 1099s, deductions, credits]
        [checkpoint saved after federal ✓]
        [enters NY nonresident return — must complete before NJ]
        [checkpoint saved after NY ✓]
        [enters NJ resident return with credit for NY taxes]
        [verification: platform numbers match source docs ✓]
        Ready to submit. Review the summary and confirm.
```

Drop your documents, get your return. Three commands, end to end.

## The three modes

| Mode | Command | What it does |
|------|---------|-------------|
| **Prepare** | `/tax:prepare` | Extract all source documents, compute the full federal + state tax picture, produce a summary spreadsheet and `tax_profile.json`. Start here. |
| **Optimize** | `/tax:optimize` | Surface unused tax savings strategies based on your specific situation. Requires prepare first. |
| **File** | `/tax:file` | Drive FreeTaxUSA live in Chrome — fill every field, verify against source docs, save checkpoints. Requires prepare first. |

## What's inside

```
tax/
├── SKILL.md                        ← Skill entry point and mode router
├── README.md                       ← You are here
├── prepare/
│   └── instructions.md             ← Document extraction + tax computation
├── optimize/
│   └── instructions.md             ← Tax savings strategies
├── file/
│   └── instructions.md             ← Browser automation for filing
├── references/
│   ├── tax_rules.md                ← IRS rules: SALT, AMT, NIIT, brackets
│   ├── federal_forms_guide.md      ← Which federal forms and when
│   ├── state_tax_agencies.md       ← Official URLs for all 50 states + DC
│   └── platform_ui_patterns.md     ← FreeTaxUSA browser automation patterns
└── scripts/
    ├── cross_foot_check.py         ← Math verification script
    └── generate_audit_trail.py     ← Audit trail generation
```

## What it handles

The skill was built for and tested against real-world complexity:

- **Multi-state filing** — resident + nonresident returns with correct credit ordering
- **Itemized deductions** — mortgage interest (with $750K principal limit proration), SALT cap, charitable contributions
- **Investment income** — qualified dividends, capital gains/losses, RSU cost basis (Box B handling)
- **Additional taxes** — NIIT (Form 8960), Additional Medicare Tax, AMT awareness
- **Credits** — Child Tax Credit (with phase-out), Child & Dependent Care Credit
- **Forms** — Schedule A, B, D, Form 8949, 2441, 8960, 8283, and more
- **FBAR reminder** — flags foreign account reporting obligations after filing

## Battle-tested improvements

Eight improvements baked in from real filing experience:

1. **Section-end verification** — compares platform numbers to source docs after each section, not just at the end
2. **Import-first strategy** — checks for W-2/1099 import features before manual entry
3. **Platform UI automation** — JS-first form filling that works with React SPAs, navigation shortcuts, session timeout handling
4. **Checkpoint files** — survives context compaction; resume exactly where you left off
5. **Precise computation** — exact IRS worksheets and state tax tables, not approximations
6. **Pre-flight checklist** — catches missing data before you touch the browser
7. **State dependency ordering** — nonresident states before resident states, always
8. **Filing reminders** — FBAR deadlines, record retention, estimated payment dates

## Design decisions

**Why FreeTaxUSA?** No particular reason. Found good reviews in reddit and it supports every form needed for complex returns. The React SPA is automatable with Chrome DevTools. The skill's patterns are documented in `references/platform_ui_patterns.md` — adding support for other platforms is straightforward.

**Why not generate PDFs directly?** Filing platforms handle e-filing, payment processing, error checking, and state integration. Paper returns are slower, riskier, and don't get e-file benefits.

**Why checkpoint files?** A single filing session can exhaust the context window. When the conversation compacts, state is lost. A JSON checkpoint lets the next session resume immediately.

**Why JS injection over mouse clicks?** React SPAs use synthetic event systems. A mouse click at coordinates may hit the element visually but miss React's handlers. Setting values via JS and dispatching change events speaks React's language.

## Future ideas

- Automated state tax table lookup (scrape + cache current-year tables)
- Multi-year carryforward tracking (capital losses, AMT credits)
- TurboTax / H&R Block platform profiles
- Estimated tax payment calculator for next year
- Document OCR for photographed W-2s

## License

MIT. Free forever. Go file your taxes.
