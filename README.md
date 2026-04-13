# Claude Skills

AI skills for consultants, strategy professionals, and anyone doing project-based analytical work. Built from real engagements — not theoretical prompts.

**Who this is for:** Consultants, corporate strategy teams, product strategists, and operators who want their AI to work like a sharp project teammate — not a generic chatbot.

---

## Skills

| Skill | What It Does | Best For | Install |
|-------|-------------|----------|---------|
| [Strategy Project](strategy-project/) | Set up any project folder as an AI-native workspace with persistent context, workstream tracking, and session discipline | Consulting engagements, strategy projects, diligence, cross-functional initiatives | [`.skill`](strategy-project/strategy-project.skill) |
| [Tax](/) | End-to-end U.S. personal income tax assistant — prepare returns from source docs, find optimization opportunities, file live in the browser | Anyone who files their own taxes, multi-state filers, people who want full audit trails | See [tax README](#tax) below |

---

## Quick Start

**Claude Code:** Clone this repo, skills auto-load when you work in the directory.

```bash
git clone https://github.com/kongaharsha/claude-skills.git ~/.claude/skills/claude-skills
```

**Claude.ai:** Download the `.skill` file from the table above → Settings → Skills → Add Skill.

**Any LLM:** Copy the `SKILL.md` content into your conversation as context. The pattern is tool-agnostic.

---

## Tax

> I filed my entire federal + multi-state tax return with an AI agent. No accountant. No $400 TurboTax upsell. Just source documents, Claude Code, and this skill.

I'm [Harsha Konga]. I built this skill after spending hours every April wrestling with tax software, lack of transparency. The skill was battle-tested on a real MFJ multi-state return — W-2s, 1099s, RSU sales, mortgage interest, SALT cap, NIIT, the works — and filed end-to-end on FreeTaxUSA.

**tax** turns Claude Code into a tax professional. Three modes: prepare your return from raw documents, find optimization opportunities you missed, and file it live in the browser — all slash commands, all Markdown, free.

### Quick start

1. Drop your tax documents (W-2s, 1099s, 1098s) into the conversation
2. Run `/tax:prepare` — get a complete tax summary with spreadsheet
3. Run `/tax:optimize` — find deductions and strategies you missed
4. Run `/tax:file` — fill out FreeTaxUSA in a real browser, hands-free

### See it work

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

### The three modes

| Mode | Command | What it does |
|------|---------|-------------|
| **Prepare** | `/tax:prepare` | Extract all source documents, compute the full federal + state tax picture, produce a summary spreadsheet and `tax_profile.json`. Start here. |
| **Optimize** | `/tax:optimize` | Surface unused tax savings strategies based on your specific situation. Requires prepare first. |
| **File** | `/tax:file` | Drive FreeTaxUSA live in Chrome — fill every field, verify against source docs, save checkpoints. Requires prepare first. |

### What it handles

- **Multi-state filing** — resident + nonresident returns with correct credit ordering
- **Itemized deductions** — mortgage interest (with $750K principal limit proration), SALT cap, charitable contributions
- **Investment income** — qualified dividends, capital gains/losses, RSU cost basis (Box B handling)
- **Additional taxes** — NIIT (Form 8960), Additional Medicare Tax, AMT awareness
- **Credits** — Child Tax Credit (with phase-out), Child & Dependent Care Credit
- **Forms** — Schedule A, B, D, Form 8949, 2441, 8960, 8283, and more
- **FBAR reminder** — flags foreign account reporting obligations after filing

### Design decisions

**Why FreeTaxUSA?** No particular reason. Found good reviews in reddit and it supports every form needed for complex returns. The React SPA is automatable with Chrome DevTools. The skill's patterns are documented in `references/platform_ui_patterns.md` — adding support for other platforms is straightforward.

**Why not generate PDFs directly?** Filing platforms handle e-filing, payment processing, error checking, and state integration. Paper returns are slower, riskier, and don't get e-file benefits.

**Why checkpoint files?** A single filing session can exhaust the context window. When the conversation compacts, state is lost. A JSON checkpoint lets the next session resume immediately.

**Why JS injection over mouse clicks?** React SPAs use synthetic event systems. A mouse click at coordinates may hit the element visually but miss React's handlers. Setting values via JS and dispatching change events speaks React's language.

---

## Background

I've been using markdown files for the last few months to make sure my AI never loses project context between sessions. The setup evolved — from one big context note, to living documents, to a structured `.context/` folder pattern that actually works.

I shared the approach and got 30+ inbound messages asking for more detail. So I'm turning these patterns into reusable skills that anyone can pick up.

These are not perfect. They're patterns that work well for me — take them, make them yours.

---

MIT License — use freely, modify, share.

[LinkedIn](https://www.linkedin.com/in/kongaharsha/) | Built with Claude
