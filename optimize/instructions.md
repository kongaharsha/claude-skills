# Tax Optimize — Step-by-Step Instructions

Surface tax-saving strategies the filer isn't currently using. Each strategy gets a plain-English explanation, an estimated annual savings, and a concrete next step.

**Prerequisite**: Load `output/tax_profile.json`. If it doesn't exist, stop and tell the user to run `tax:prepare` first.

---

## Before You Start

From `tax_profile.json`, extract the facts you'll need to evaluate each strategy:
- AGI, taxable income, filing status, marginal federal rate (compute from brackets)
- W-2 wages per filer, self-employment income (if any)
- Whether each filer has an employer retirement plan, and contribution amounts (Box 12 codes D/S/AA/BB)
- Presence and ages of dependents
- Whether an HSA-eligible health plan is in use
- Investment income (dividends, interest, capital gains) by filer
- States filing in
- FBAR requirement
- Capital loss carryover

---

## Evaluation Framework

For each strategy below: check whether it applies to this filer's profile. If yes, estimate savings and flag it. If no, skip it silently — don't list strategies that don't apply. Be honest about uncertainty: use "~$X" or "up to $X" when the savings depends on inputs you don't have.

---

## Strategy Categories

### Retirement Contributions

**Max 401(k)/403(b)**: Are they at the annual elective deferral limit? Each additional $1 pre-tax reduces federal taxable income at their marginal rate. Note catch-up contribution if age ≥ 50.

**IRA — Traditional or Backdoor Roth**: If AGI exceeds traditional IRA deductibility limits, a Backdoor Roth may be available. Warn if they have existing pre-tax Traditional IRA balances — the pro-rata rule may apply.

**Mega Backdoor Roth**: If the employer 401(k) plan allows after-tax contributions and in-service distributions, up to ~$43k of additional after-tax contributions can be converted to Roth. Only applies if plan documents permit it.

**SEP-IRA or Solo 401(k)**: If any self-employment income exists (`other_income` with type "1099-NEC" or similar), up to 25% of net SE income can go in pre-tax. Calculate the maximum allowed contribution.

**Spousal IRA**: For MFJ where one spouse has low or no earned income — a spousal IRA contribution may be available even if the working spouse's income exceeds deductibility limits.

### Health Accounts

**HSA**: If the filer has an HSA-eligible HDHP, are they maxing the HSA contribution? Triple tax advantage: deductible going in, tax-free growth, tax-free out for qualified medical expenses. Check current-year family/individual limit.

**Dependent Care FSA**: If there are children in childcare or dependents needing care, a dependent care FSA uses pre-tax dollars (up to $5,000/year) vs. taking the Dependent Care Credit. At high income, the FSA is almost always better — the credit phases to just 20% while the FSA saves at the full marginal rate.

### Investments

**Tax-loss harvesting**: If the filer has unrealized losses in taxable accounts, they can be sold to offset realized gains. Note the wash-sale rule (can't repurchase the same or substantially identical security within 30 days). Good candidates: individual stocks, sector ETFs where a comparable alternative exists.

**Asset location**: High-yield bonds, REITs, and dividend-heavy stocks in a taxable account generate ordinary income taxed at the full marginal rate. Moving them into tax-deferred accounts (and holding growth stocks in taxable) improves long-term after-tax returns without changing the portfolio's risk profile.

**Qualified Opportunity Zone (QOZ) funds**: If there are large capital gains, investing proceeds in a QOZ fund defers the gain (until 2026 or sale of the fund). Mention the significant illiquidity and complexity risk.

### Deductions & Giving

**Bunching charitable donations**: If total itemized deductions are close to the standard deduction threshold, bunching two years of planned donations into one year (then taking standard the next) can increase cumulative deductions. A Donor Advised Fund (DAF) makes this straightforward — fund it in a high-income year, grant out over time.

**Donate appreciated stock**: Instead of cash, donate stock held long-term directly to a charity or DAF. Avoids the capital gains entirely and takes the full FMV as a deduction. Only beneficial if itemizing.

**Home office deduction**: Available only to self-employed filers with a dedicated workspace used regularly and exclusively for business. Not available for W-2 employees under current law.

### Family & Education

**529 plan**: For filers with children (including infants), 529 contributions grow and distribute tax-free for qualified education expenses. Some states offer a state income tax deduction on contributions — check if the filer's state does.

**UTMA/Custodial account**: For filers with children who have investment income, a custodial account shifts some investment income to the child's lower tax rate (subject to kiddie tax rules — check child's age).

### Withholding Adjustment

**W-4 optimization**: If this year's return shows a large refund (>$2,000) or a balance owed (>$1,000), the W-4 is miscalibrated. A large refund is an interest-free loan to the IRS. A balance owed risks underpayment penalties if it exceeds the safe harbor (100% of prior year tax, or 110% if prior year AGI > $150k).

---

## Output Format

Present a prioritized list in the conversation — highest estimated impact first. For each applicable strategy:

```
### [Strategy Name]
**Estimated savings**: ~$X – $Y per year
**Why it applies to you**: [1-2 sentences grounded in their actual profile numbers]
**Concrete next step**: [specific action — e.g., "Increase your 401(k) contribution
to $23,500 (2025 limit) via your employer's benefits portal"]
**Caveats**: [anything material — lock-up, pro-rata rule, plan-document dependency, etc.]
```

Close with a 2-3 sentence prioritized summary: the top 3 moves by expected impact and ease of execution — what they should actually do first.

---

## What Not to Include

- Strategies they're already executing (visible in `tax_profile.json`)
- Strategies that don't apply to their situation (no kids → no 529)
- Aggressive or gray-area positions (inflated charitable valuations, abusive shelter structures)
- Generic advice that's identical regardless of their profile numbers
