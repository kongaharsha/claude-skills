# IRS Tax Rules Reference

Key rules, limits, and thresholds used in tax preparation. **Always verify against the current tax year** — these values change annually. This file contains the rules and where to find them, not hard-coded numbers.

---

## Where to Look Up Current-Year Values

| What | Where |
|------|-------|
| Tax brackets, standard deduction, QDCG thresholds | https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-YEAR |
| 1040 line-by-line instructions | https://www.irs.gov/instructions/i1040gi |
| SALT cap and OBBBA updates | https://www.irs.gov (search "SALT deduction YEAR") |
| Additional Medicare Tax | https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax |
| NIIT | https://www.irs.gov/newsroom/net-investment-income-tax |
| AMT | https://www.irs.gov/taxtopics/tc556 |

---

## SALT Deduction

**Standard rule (TCJA 2017–2025)**: State and local tax (income + property) deduction capped at $10,000 per return ($5,000 MFS).

**OBBBA update (check current year)**: The One Big Beautiful Bill Act raised the base cap for 2025. Key parameters:
- Base cap amount (MFJ): look up for current year
- Phase-out threshold (MFJ): look up for current year
- Phase-out rate: look up for current year (was 30% in 2025)
- Formula: `Allowed SALT = base_cap − (max(0, AGI − threshold) × rate)`
- The allowed SALT cannot go below $10,000

**What counts toward SALT**:
- State income tax withheld (W-2 Box 17)
- State estimated tax payments made
- Real property taxes (primary and secondary residences)
- Local income taxes

**What doesn't count**: Sales taxes (cannot deduct both income and sales taxes), foreign taxes (use Form 1116 for those), utility fees and assessments.

---

## Additional Medicare Tax (Form 8959)

**Rate**: 0.9% on wages and self-employment income above the threshold.

**Thresholds**:
- MFJ: $250,000
- Single, Head of Household, Qualifying Surviving Spouse: $200,000
- MFS: $125,000

**How it works**: Employers withhold 0.9% on wages above $200k for any individual employee, regardless of filing status. At tax time, the return reconciles the total — MFJ filers often owe additional tax because the $250k threshold is per household, but withholding was done per-person at $200k each.

**What's included**: W-2 wages, railroad retirement, self-employment income. Does NOT include investment income (that's NIIT).

---

## Net Investment Income Tax / NIIT (Form 8960)

**Rate**: 3.8%

**Applies when**: MAGI exceeds the threshold AND there is positive net investment income (NII).

**Thresholds** (same as Additional Medicare Tax):
- MFJ / QSS: $250,000
- Single / HOH: $200,000
- MFS: $125,000

**What's NII**:
- Interest, dividends, capital gains
- Rental income (if not from an active trade or business)
- Royalties
- Passive activity income

**Tax is on lesser of**: total NII OR (MAGI − threshold). So if MAGI barely exceeds the threshold, only the excess amount is taxed, not all NII.

---

## Qualified Dividends and Long-Term Capital Gains (QDCG)

These are taxed at preferential rates (0%, 15%, 20%) rather than ordinary income rates.

**Rate thresholds** (based on taxable income, not AGI — look up current year):
- 0% rate: up to a threshold (single and MFJ have different thresholds)
- 15% rate: between 0% and 20% thresholds
- 20% rate: above the 20% threshold (roughly top bracket incomes)
- 3.8% NIIT may also apply on top for high-income filers

**Use the QDCG worksheet** (in the 1040 instructions) to compute tax when a filer has qualified dividends or long-term capital gains. Don't just apply regular brackets to the full taxable income.

**Qualified dividends**: Must be held the required holding period (>60 days for common stock) and paid by a qualifying corporation. Qualified dividends are reported in Box 1b of Form 1099-DIV.

---

## Alternative Minimum Tax (AMT)

The AMT is a parallel tax system with a larger exemption but no deduction for SALT or personal exemptions. Filers pay whichever is higher — regular tax or AMT.

**Who it hits**: Historically affected high-income filers with large SALT deductions, ISO stock option exercises, or large depreciation deductions. Under TCJA 2017+, higher exemptions significantly reduced AMT exposure.

**Key items that trigger AMT preference/adjustment**:
- ISO exercise spread (not NQSOs)
- Accelerated depreciation
- Percentage depletion
- Private activity bond interest
- Some passive activity losses

**How to check**: Compute AMT income (AMTI) = regular taxable income + preference items + adjustments. Subtract AMT exemption (look up current year). Multiply by AMT rate (26% / 28%). Compare to regular tax.

---

## Child Tax Credit (CTC)

**Maximum credit**: Per qualifying child (under 17 at year end) — look up current-year amount.

**Phase-out**: Begins at AGI above $400,000 (MFJ) / $200,000 (others). Reduces by $50 per $1,000 of AGI over the threshold.

**Refundable portion (ACTC)**: If CTC exceeds tax liability, a portion may be refundable — look up current-year Additional Child Tax Credit rules.

---

## Child and Dependent Care Credit (CDCC)

**Covers**: Childcare, daycare, or dependent care expenses enabling both spouses (MFJ) to work.

**Maximum qualifying expenses**: $3,000 for one qualifying person, $6,000 for two or more.

**Credit rate**: Percentage of qualifying expenses, ranging from 20%–35% based on AGI. At higher incomes, the rate is 20%.

**Note**: If an employer-provided Dependent Care FSA ($5,000) is used, it reduces the qualifying expenses for this credit. The FSA is almost always more valuable at high income.

---

## Mortgage Interest Deduction

**Deductible on**: Loans used to buy, build, or substantially improve a qualified residence (primary + one secondary home).

**Debt limit**: Interest deductible on up to $750,000 of qualifying mortgage debt (for loans taken out after Dec. 15, 2017). Older loans grandfather at $1,000,000.

**If over the limit**: The deductible interest must be prorated. Use Form 1098:
- Box 1: Mortgage interest paid during the year
- Box 2: Outstanding mortgage principal (beginning of year or origination date)

```
Deductible interest = Box 1 × ($750,000 / Box 2)
```

Example: If Box 1 = $50,192 and Box 2 = $762,078:
  Deductible = $50,192 × ($750,000 / $762,078) = $50,192 × 0.9842 = $49,399

Note: Filing platforms (FreeTaxUSA, TurboTax) compute this limitation using their own worksheets, which may use average balance rather than beginning-of-year balance. Expect small differences ($100-500) between your manual calculation and the platform's. The platform's number is authoritative for filing purposes.

**What's deductible**: Interest on acquisition debt. Points paid at purchase may be deductible in the year paid.

**What's not**: PMI deductibility — check whether currently in effect for the tax year.

---

## Foreign Tax Credit (FTC) vs. Deduction

Taxes paid to foreign governments on investment income can either be deducted on Schedule A or taken as a credit on Schedule 3 (via Form 1116).

**The credit is almost always better** — a dollar-for-dollar reduction in U.S. tax beats a deduction at the marginal rate.

**De minimis exception**: If foreign taxes paid were $300 or less ($600 MFJ) and all foreign income is passive, Form 1116 is not required — the credit can be claimed directly on Schedule 3.

---

## Capital Loss Rules

**Annual deduction limit**: Net capital losses can offset capital gains. Any excess can deduct up to $3,000 of ordinary income per year.

**Carryover**: Unused capital losses carry forward indefinitely. Maintain records.

**Short-term vs. long-term netting order**:
1. Net ST gains against ST losses
2. Net LT gains against LT losses
3. If one side has a net loss, apply against the net gain of the other side
4. If still a net loss, deduct up to $3,000 against ordinary income; carry forward the rest

**Wash-sale rule**: Cannot recognize a loss if you buy the same or substantially identical security within 30 days before or after the sale. The disallowed loss adds to the basis of the replacement shares.

---

## RSU / Equity Compensation

**W-2 income at vest**: When RSUs vest, the FMV on the vest date is ordinary income, reported in W-2 Box 1 (and usually Box 14). This is also the cost basis for the shares.

**1099-B reporting risk**: Many brokers report the sale of RSU shares on a 1099-B with a $0 cost basis (or only the amount paid — usually $0 for RSUs). This would result in the full sale proceeds being taxed as capital gains, causing double taxation. Always confirm basis = FMV at vest, not $0.

**Same-day sales**: When shares are sold immediately at vest, the gain above vest-date FMV is typically $0 or a small rounding difference. If 1099-B shows $0 basis, the taxpayer must manually adjust in Form 8949 (Box B or E, with code B for basis not reported to IRS).

---

## Safe Harbor for Estimated Taxes

To avoid underpayment penalties, total tax payments (W-2 withholding + estimated payments) must be at least:
- **100% of the prior year's tax liability** (the safer option for high-income filers), OR
- **110% of prior year liability** if prior year AGI > $150,000 (MFJ), OR
- **90% of the current year's actual tax liability**

The penalty applies on the shortfall per quarter — it's computed quarterly, not just on the annual balance.

---

## Precise Computation Sources

When computing tax_profile.json, use the most precise sources available rather than approximate rate schedules. The numbers in the tax profile get compared against the filing platform's exact computations, so precision matters.

**Federal income tax**: Always use the QDCG worksheet from the 1040 instructions when qualified dividends or LTCG exist. The worksheet splits income into ordinary and preferential components and applies the correct rates to each. Don't simply apply bracket rates to all taxable income.

**NIIT (Form 8960)**: Follow the Form 8960 instructions line by line. Common mistakes:
- Including tax-exempt interest in NII (it's not investment income)
- Forgetting to subtract investment expenses from NII
- Using AGI instead of MAGI for the threshold comparison

**State tax tables**: Look up the actual published tables for the filing year:
- NY: https://www.tax.ny.gov → search "tax rate schedule" or "tax computation worksheet" for the year
- NJ: https://www.state.nj.us/treasury/taxation/ → "NJ-1040 instructions" for the year, contains rate tables
- CA: https://www.ftb.ca.gov → "Tax Rate Schedules" for the year

State tax computations are the most common source of discrepancy between manual calculations and platform outputs. If exact tables aren't available yet for the current year, note the uncertainty explicitly.

**Additional Medicare Tax (Form 8959)**: Remember that the withholding credit on line 25c of Form 1040 is: total Medicare tax withheld (W-2 box 6, both filers) minus the regular 1.45% × Medicare wages. This credit is often overlooked.
