# FA Intake — Form Spec (native build reference)

Source: `FA INTAKE` questionnaire (44-page firm form). This is the marquee intake form; it
feeds the Florida Family Law Financial Affidavit (Form 12.902(b)/(c)) and the Tier-1 FA-ready
flow. Rebuild as a NATIVE in-app fillable form (answers land in the matter record; can
auto-populate case info and the FA builder).

## Cross-cutting behaviors
- **Draft-then-lock:** answers auto-save as a persistent draft ("standing memory") so the
  client can leave and resume; on SUBMIT the form locks to view-only for the client.
- **Auto-populate from uploads:** several sections state "uploading your paychecks / bank
  statements will populate this for us" — an AI extraction pass over uploaded pay stubs / bank
  statements should pre-fill Payroll Deductions, Housing/Utilities, Food/Transport/Health, and
  Assets (staff/client-confirmable, never silently overwriting).
- **Field types:** short text, MM/DD/YYYY date, currency ($), single-select (radio),
  multi-select (checkbox), long text (textarea).
- **Required** fields marked `*` below.
- **Conditional** groups render only on a triggering answer.
- **Repeatable** groups have an "Add" control.
- **Petitioner/Respondent** terminology (see Role field).

## Sections & fields

### 1. Case & Personal Information
first name*, last name* (both "as on court documents"), date of birth*, current residential
address*, how long at this address*, best phone number, marital status (Single/Married/
Divorced/Widow/Widower), email*, role in case* (Petitioner/Respondent), children from a
previous/other relationship?* (Yes/No).
- **Conditional (Other Children, if Yes):** child-support order in place?*, case name*, state &
  county of order*, case no.*, pay or receive?* (Pay/Receive), monthly amount*.

### 2. Employment & Primary Employer Details
avg monthly commission income, avg monthly bonus income (last 3 yrs), are you employed?*,
income from >1 employer in last 12 months?*.
- **Employer #1 (and Additional Employers — repeatable):** employer name, job title, still
  employed?, employer address, employment type (Full/Part/Seasonal/Temporary), start date
  (MM/YYYY), hourly rate, how paid? (Salary/Hourly/Commission/Salary+Commission/Other), last
  date of work (if ended), annual salary (if salaried), avg hours/week (if hourly), avg monthly
  overtime (gross), bonuses last 3 yrs, avg monthly commission, other compensation? (Yes/No),
  overtime pay? (regular-expected/occasional/No), describe additional compensation.

### 3. Additional Employment & Self-Employment Income
additional employment/freelance/gig/side income?* (Yes/No), how paid (1099/W-2/Cash), do you
own a business? (Yes/No).
- **1099 – Contract (conditional):** employer/client name (or "Self-employed"), type of work.
- **Business Ownership (conditional):** business name & type (LLC/sole prop/S-Corp), % owned,
  gross monthly income from this source, gross monthly business revenue (pre-expenses), total
  ordinary & necessary monthly business expenses, net monthly income after expenses, pay
  yourself a salary? (Yes/No), use business account for personal expenses? (Yes/No/Sometimes),
  monthly salary amount, CPA/accountant name & contact, have a CPA/accountant? (Yes/No).

### 4. All Income Sources
rental property?* (Yes/No) → **Rental Property (repeatable):** address, gross monthly rental
income, ordinary monthly expenses.
disability & SS benefits?* (Yes/No) → **Disability Income:** monthly SS benefit, monthly SSI/SSDI.
dividend/trust/investment income?* (Yes/No) → monthly pension/retirement distribution, avg
monthly dividend income, monthly trust/annuity distribution.
alimony* (receive / pay / neither), monthly alimony from a prior/separate case.
receive any of* (checkbox): workers' comp / unemployment / royalty / None → amounts each
(workers' comp, royalty, unemployment), avg monthly gifts/support from family, avg monthly via
Venmo/PayPal/Zelle/CashApp.
other income sources?* (Yes/No) → describe + avg monthly amount; notes on income (irregular/
estimated/anything attorney should know).
investment income: avg monthly interest income (savings/CDs/bonds).

### 5. Payroll Deductions ("uploading paychecks populates this")
monthly federal income tax withheld, monthly state income tax withheld ($0 if none), monthly
FICA/Social Security (6.2%), monthly Medicare (1.45%), employer-required retirement contribution,
health insurance premium (your share), other mandatory deduction #1 (describe + amount), other
mandatory deduction #2 (describe + amount), 401(k)/403(b)/voluntary retirement? (Yes/No) +
monthly amount, FSA/HSA? (Yes/No) + monthly amount, other voluntary payroll deductions
(life/supplemental/union)? (Yes/No) + describe + total monthly amount.

### 6. Monthly Expenses — Housing & Utilities ("uploading bank statement populates")
rent, mortgage (P&I), real estate tax (monthly), homeowner's/renter's insurance, HOA fees,
condo fees, lawn/pest/maintenance, home repairs/upkeep, other housing? (Yes/No) + describe +
amount, electric, gas/propane, water/sewer, trash, internet, cable/streaming, home phone/
landline, cell phone (your line), any shared housing/utility expenses? (note which + your share).

### 7. Monthly Expenses — Food, Transportation & Health ("uploading bank statements populates")
groceries/food-at-home, dining out, household supplies, car payment Vehicle 1, car payment
Vehicle 2, car insurance (all vehicles), gas/fuel, car maintenance/repairs, parking/tolls,
rideshare, public transit, other transport? (Yes/No) + describe + amount, health insurance
premium (your share), dental premium (your share), vision premium (your share), out-of-pocket
medical, prescriptions, mental health/therapy, other health? (Yes/No) + describe + amount.

### 8. Monthly Expenses — Children, Personal & Insurance
child care/daycare/after-school, private/charter tuition, school supplies/fees/activities,
extracurriculars/sports/lessons, children's clothing, children's unreimbursed medical,
children's allowance, summer camp, other children's expenses? (describe + amount), your
clothing, personal care/haircuts/grooming, gym/fitness, entertainment/recreation, non-streaming
subscriptions, pet expenses, gifts, annual vacation/travel ÷12, life insurance premium,
disability insurance premium, long-term care insurance premium, other insurance premiums?
(describe + amount).

### 9. Monthly Expenses — Debt Payments & Other
total min monthly across all credit cards, student loan payment, personal loan payment, medical
debt payment, IRS/tax payment plan (monthly), other debt payments? (describe) + amount, alimony
paid from another case, child support paid from another case, religious/charitable donations,
professional dues/union/license fees, any other monthly expenses not covered? (describe +
amounts).

### 10. Assets — Bank Accounts, Real Property & Vehicles ("uploading bank statements populates")
checking accounts?* (Yes/No) → **Checking #1 / #2:** bank + last 4, current balance, sole/joint,
when opened/how acquired. savings accounts?* → **Savings #1 / #2** (same fields). money market/
CD/other?* → bank + last 4, balance, sole/joint. payment-app balances?* (Yes/No) → app name(s)
+ balance(s). other cash/financial accounts? (describe).
real property interest?* (Yes/No) → **Primary Residence:** street, est. market value, current
mortgage balance, approx. date purchased, sole/joint, owned before marriage or gift/inheritance?
(owned-before / gift-inheritance / No). **Second/Vacation Property:** address, value, mortgage
balance, date purchased, sole/joint. **Rental Property:** address, value, mortgage balance, date
purchased, sole/joint. **Vacant Land/Other:** description+address, value, sole/joint. any real
property owned before marriage or gift/inheritance? (describe).
own vehicles?* (Yes/No) → **Vehicle 1 / 2:** year/make/model, est. value (KBB), current loan
balance, sole/joint, approx. date acquired. other vehicles (boat/RV/motorcycle)?* (Yes/No) →
**Other Vehicle:** description, value, loan balance, sole/joint. anything else re accounts/
property/vehicles?

### 11. Assets — Retirement, Investments, Business & Other
deferred compensation plan value, brokerage/investment account? + institution + value + sole/
joint, stock options/RSUs? (employer + est. value) + value, cryptocurrency? (type(s) + value) +
value, other retirement/investment accounts? (describe), business ownership interest? (name/
type/% ) + value + sole/joint + when/how acquired, life insurance with cash value? (carrier +
policy #) + cash value, annuity? (carrier + value) + value, anyone owe you money? (describe) +
amount, inheritance received/expected? (describe) + value, valuable personal property (jewelry/
art/antiques/collections)? (describe) + value, any other asset? (describe) + value, for any
retirement/investment account — owned before marriage or gift/inheritance? (describe).

### 12. Liabilities & Debts (list ALL — individual and joint)
Per-debt fields: creditor/lender name, current balance owed, monthly payment amount, sole/joint
(some N/A). Debts enumerated: primary residence mortgage, second-property mortgage, home equity/
HELOC, vehicle loan 1, vehicle loan 2, credit card #1/#2/#3, student loan, personal loan,
medical debt, IRS/tax debt, business debt (personally guaranteed), any other debt. anything else
re debts/liabilities?

### 13. Additional Financial Information
anything about finances attorney should know? applied for any loan in last 24 months? (No/Yes) +
lenders/dates; filed financial aid app in last 24 months? (No/Yes); filed bankruptcy in last 7
years? (No/Yes) + year & chapter; transferred/gifted/sold significant asset in last 3 years?
(No/Yes) + describe; income changed significantly in last 2 years? (No/Yes) + explain; changed
jobs/reduced hours recently? (No/Yes) + describe; receiving financial support from family/new
partner? (No/Yes) + describe; pending inheritance? (No/Yes) + describe; party to any other legal
proceeding? (No/Yes) + describe.

### 14. Document Checklist & Certification
Availability checklist (Yes/No/N/A each), mostly overlapping the discovery collection set: last
3 pay stubs (+ explain if No), federal tax returns (most recent / prior / two years ago) +
explain if unavailable, W-2s/1099s, bank & checking statements (12 mo), savings statements (12
mo), investment/brokerage statements (12 mo), retirement statements (12 mo) + explain if
unavailable, most recent mortgage statement, vehicle loan statement(s), credit card statements
(3 mo), business tax returns / P&L (if self-employed), real property deeds, loan applications
(24 mo), life insurance policy / cash value statement, notes on any docs unable to provide.
- **Certification\*:** type full name to certify all info true/accurate, understanding it will
  be used to prepare a sworn Financial Affidavit and that false info may constitute perjury; +
  Date of Certification (MM/DD/YYYY). Treat as an attestation/e-sign event (timestamp + typed
  name); flag the "approval legal weight" open decision.

## Build notes
- The document-checklist section overlaps the discovery collection (Phase 2). Reconcile: the FA
  Intake availability answers can seed / cross-check the discovery checklist rather than
  duplicate it.
- The Tier-1 FA-critical items (pay stubs, bank statements, tax return, income characterization)
  map to sections 2–5 + the availability checklist — completing those should feed the FA-ready
  signal and the FA builder.
- Source of truth PDF lives with the firm's intake-forms SharePoint folder; this spec is the
  build reference.
