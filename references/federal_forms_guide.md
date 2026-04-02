# Federal Forms Guide

Which IRS forms are needed and when. Use this to populate `output/forms_required.md` — include only forms that apply to the filer's actual situation.

Always verify against the current year's IRS instructions. Form requirements and thresholds can change year to year.

---

## Core Return

| Form | Title | Required When |
|------|-------|---------------|
| Form 1040 | U.S. Individual Income Tax Return | Always — the main return |
| Form 1040-SR | U.S. Tax Return for Seniors | Alternative to 1040 for filers age 65+; same content, larger print |

---

## Schedules (attached to 1040)

| Form | Title | Required When |
|------|-------|---------------|
| Schedule A | Itemized Deductions | Itemized deductions exceed standard deduction |
| Schedule B | Interest and Ordinary Dividends | Taxable interest or ordinary dividends > $1,500; any foreign accounts |
| Schedule C | Profit or Loss from Business | Self-employment income or loss |
| Schedule D | Capital Gains and Losses | Any capital gain or loss transactions; also required if capital loss carryover |
| Schedule E | Supplemental Income and Loss | Rental property income; partnership/S-Corp K-1 income; royalties |
| Schedule F | Profit or Loss from Farming | Farm income |
| Schedule H | Household Employment Taxes | Paid household employees (nanny, housekeeper) over the annual threshold |
| Schedule SE | Self-Employment Tax | Net self-employment income > $400 |
| Schedule 1 | Additional Income and Adjustments | Other income not on main 1040 (alimony, gambling, HSA deduction, student loan interest, etc.) |
| Schedule 2 | Additional Taxes | AMT, Additional Medicare Tax, NIIT, self-employment tax, other taxes |
| Schedule 3 | Additional Credits and Payments | Foreign tax credit, education credits, child & dependent care credit, estimated tax payments, excess SS withholding |

---

## Common Supporting Forms

### Income

| Form | Title | Required When |
|------|-------|---------------|
| Form 8949 | Sales and Other Dispositions of Capital Assets | Any 1099-B transactions (brokerage sales, crypto); one for each category (Box A/B/C short-term; Box D/E/F long-term) |
| Form 4797 | Sales of Business Property | Sale of business property or Section 1231 assets |
| Form 8814 | Election to Report Child's Interest and Dividends | Parent chooses to include child's investment income on parent's return |

### Deductions & Adjustments

| Form | Title | Required When |
|------|-------|---------------|
| Form 8889 | Health Savings Accounts (HSAs) | Any HSA contributions or distributions |
| Form 1098 | Mortgage Interest Statement | Provided by lender; deductible on Schedule A (form itself not filed, but data used) |
| Form 8606 | Nondeductible IRAs | Any nondeductible Traditional IRA contribution; Backdoor Roth conversion |

### Additional Taxes

| Form | Title | Required When |
|------|-------|---------------|
| Form 6251 | Alternative Minimum Tax | AMT may apply — generally for high-income filers with large ISO exercises, large depreciation deductions, or other AMT preference items |
| Form 8959 | Additional Medicare Tax | Medicare wages or self-employment income over threshold ($200k single / $250k MFJ); required even if employer already withheld — reconciles total |
| Form 8960 | Net Investment Income Tax | MAGI over threshold ($200k single / $250k MFJ) AND positive net investment income |

### Credits

| Form | Title | Required When |
|------|-------|---------------|
| Form 2441 | Child and Dependent Care Expenses | Claiming the Child and Dependent Care Credit or excluding employer-provided dependent care |
| Form 8812 | Credits for Qualifying Children and Other Dependents | Additional Child Tax Credit (refundable portion) |
| Form 1116 | Foreign Tax Credit | Foreign taxes paid on investment income (dividends, interest) > $300 single / $600 MFJ; below that, can take the credit directly on Schedule 3 without filing the form |
| Form 8863 | Education Credits | American Opportunity Credit or Lifetime Learning Credit |
| Form 5695 | Residential Clean Energy and Energy Efficient Home Improvement Credits | Solar panels, energy-efficient windows, heat pumps, EVs, etc. |

### Retirement

| Form | Title | Required When |
|------|-------|---------------|
| Form 5329 | Additional Taxes on Qualified Plans | Early distribution from IRA/401k (under 59½) without exception; excess contributions |
| Form 8880 | Credit for Qualified Retirement Savings Contributions | Saver's Credit — lower income filers who contribute to IRAs or 401(k)s |

### Foreign / International

| Form | Title | Required When |
|------|-------|---------------|
| FinCEN 114 (FBAR) | Report of Foreign Bank and Financial Accounts | Aggregate value of foreign financial accounts > $10,000 at any point during the year. Filed separately with FinCEN (not the IRS), due April 15, automatic 6-month extension |
| Form 8938 | Statement of Specified Foreign Financial Assets | FATCA — foreign assets above threshold ($50k single / $100k MFJ at year end, or $75k / $150k at any point). Filed with the 1040 |
| Form 2555 | Foreign Earned Income Exclusion | U.S. citizen or resident living abroad with foreign earned income |
| Form 1116 | Foreign Tax Credit | (see Credits section above) |

### Miscellaneous

| Form | Title | Required When |
|------|-------|---------------|
| Form 8829 | Expenses for Business Use of Your Home | Home office deduction for self-employed (Schedule C); not for W-2 employees |
| Form 4868 | Application for Automatic Extension of Time | Extension request — extends filing deadline 6 months; does NOT extend payment deadline |
| Form 2210 | Underpayment of Estimated Tax | Underpayment penalty calculation; may be required if estimated payments fell short of safe harbor |

---

## Safe Harbor Reference

To avoid underpayment penalties, federal tax payments (withholding + estimated) must meet one of:
1. **90% of current year tax**, OR
2. **100% of prior year tax** (110% if prior year AGI > $150,000)

Whichever is smaller is the safe harbor. If payments don't meet either threshold, Form 2210 may be required and a penalty applies.

---

## Extension Notes

- **Federal extension** (Form 4868): extends filing to October 15. Tax owed is still due April 15 — the extension only covers the paperwork.
- **State extensions**: most states automatically accept a federal extension or require a separate state extension form. Check the filer's state(s).
- **FBAR extension**: automatic — no form needed, extends to October 15 automatically.
