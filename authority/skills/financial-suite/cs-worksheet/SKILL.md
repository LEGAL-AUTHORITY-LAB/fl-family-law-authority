---
name: fmlg-cs-worksheet
description: >
  Florida § 61.30 Child Support Guidelines Worksheet calculator for FMLG mediation
  and litigation matters. Use this skill IMMEDIATELY whenever anyone asks to run,
  calculate, produce, or update a child support worksheet, guidelines calculation,
  or support obligation — whether for mediation prep, trial prep, settlement
  negotiation, or any other purpose. Also triggers on: "run child support," "what's
  the support number," "calculate CS," "run the guidelines," "how much support,"
  "what would he/she pay," "run it at X income," "what does the worksheet show," or
  any scenario testing of support amounts. Always produces TWO outputs: (1) a
  narrative worksheet Word doc with full methodology and flags, and (2) a landscape
  PDF matching the Family Law Software (FLS) one-page guidelines layout exactly.
  Never produce only one without the other. Never run numbers without first asking
  the mandatory pre-calculation questions defined in this skill.
---

## FMLG Firm-Wide Conventions (apply to every run of this skill)

These six conventions govern all FMLG skills and override any narrower instruction
below that conflicts with them.

1. **Environment-flexible.** Complete the task in the environment you are already in
   — chat, Desktop, or Cowork. If a different environment would be materially better,
   say so in one line and keep working. Never block, never redirect, never hand off
   instead of doing the work.
2. **Identity over lanes.** Staff assignments in this skill are defaults, not gates.
   Anyone may run any skill. **Attorneys self-approve** — if the person running this
   skill is Naz or Leisa, they *are* the approving attorney. Never tell an attorney to
   route their own work to an attorney for approval. Approval gates mean an approving-
   attorney action is recorded, not that the user must go find someone.
3. **Just run it.** Prerequisite stages are soft checks, never hard gates. Pause only
   for a physically necessary input, and ask for that specific item by name — never
   "complete Stage X first."
4. **Read files first.** Search the entire matter file — including misnamed and
   misfoldered documents — before declaring anything missing. If the file is
   disorganized, offer a file-organizer cleanup rather than reporting a gap.
5. **Transcripts preferred, never required.** A typed memo or rough notes always
   suffice as input.
6. **Write to the command center.** Every stage completion, deadline, lifecycle move,
   and attorney flag is written to the matter's command center before the run ends.

---

# FMLG Child Support Guidelines Worksheet — § 61.30 Florida Statutes

## Purpose

Calculate Florida child support per § 61.30 and produce two required outputs every
single time, no exceptions:

1. **Narrative worksheet** — full methodology, income analysis, flags, open items
   → Landscape PDF, FLS-style one-pager (primary deliverable)
2. **Word doc** — detailed narrative with assumptions, flags, and mediator notes
   → Portrait .docx (secondary deliverable for file)

---

## STEP 1 — MANDATORY PRE-CALCULATION QUESTIONS

**Before running any numbers**, Claude MUST confirm the following. If any answer
is not already established in the current session, STOP and ask. Do not assume.
Do not default to zero without asking. Group all questions into one message.

---

### QUESTION BLOCK — Ask every time unless already confirmed:

**Q1 — Work-Related Child Care**

> "Does [Mother / primary parent] currently pay for any work-related child care?
> This includes after-school programs, before-school programs, babysitters,
> daycare, or any paid supervision that allows her to work.
> If yes — what is the monthly amount she pays?"

**SKILL RULE — FA LINE MAPPING:**
- **Line 36** (Nursery/babysitting/day care) AND **Line 39** (After school
  activities) — BOTH must be checked and treated as potential child care costs.
- Line 39 labeled "after school activities" on the FA form IS used for after-school
  care / after-school programs in FMLG practice. Do NOT treat it as zero simply
  because the label says "activities." Always confirm with the attorney or staff
  what Line 39 represents in this specific case.
- If Line 36 = $0 but Line 39 has a value, ASK whether Line 39 is child care or
  extracurricular activities — never assume.
- Only confirmed work-related child care qualifies as a § 61.30(7) addition to the
  basic obligation.

**Q2 — Summer Camp / Seasonal Child Care (Line 54)**

> "Does [Mother / primary parent] pay for summer camp or seasonal programs?
> If yes — is that amount on the FA already annualized (divided by 12),
> or is it the full seasonal cost? Should it be included in the worksheet
> or left out by agreement?"

**SKILL RULE — LINE 54:**
- Line 54 (Camp/summer activities) may be a seasonal lump sum, not a monthly cost.
- If the FA shows a Line 54 amount, ALWAYS ask whether it is:
  (a) Already annualized (÷12) and ready to use monthly, OR
  (b) A seasonal total that needs to be annualized before use, OR
  (c) To be excluded from the worksheet by party agreement.
- Never include Line 54 without confirming treatment. Never exclude it without
  asking. Default = ASK.

**Q3 — Child Health Insurance**

> "Which parent carries [child's name] on their health insurance plan?
> What is the monthly premium attributable to the child only
> (not the parent's own coverage)?"

**SKILL RULE — HEALTH INSURANCE:**
- Use FA Line 45 (child health insurance under child expenses section) as the
  starting figure, but confirm the amount — Line 45 is frequently illegible
  or estimated.
- Do NOT use Line 23 (parent's own health insurance deduction) for this figure.
  Line 23 covers only the parent's own coverage and is a deduction from income,
  not an addition to the child support obligation.
- The confirmed child health insurance amount is added to the basic obligation
  per § 61.30(7) and split proportionally.

**Q4 — Time-Sharing / Overnights**

> "What time-sharing schedule are we calculating for?
> Specifically, how many overnights per year does [Father / non-primary parent]
> have with [child's name]? (365 total)
> Common scenarios: Standard (~73 nights / 20%), 30% (~110), 35% (~128),
> 50/50 (~182-183), or other."

**SKILL RULE — OVERNIGHTS:**
- If parties have not agreed on a schedule, run MULTIPLE scenarios (see Step 4).
- The § 61.30(11)(b) substantial time-sharing adjustment applies at 73+ overnights.
- Below 73 overnights: no adjustment; obligor pays full proportionate share.
- At or above 73: apply the 1.5x multiplier formula.

**Q5 — Uncovered Medical / Dental**

> "Is there a known monthly amount for unreimbursed medical or dental expenses
> for [child's name]? If yes, what is the monthly figure?"

---

## STEP 2 — INCOME INPUTS

### Source Priority (use the highest-quality available source):

1. Confirmed agreement between parties
2. Most recent pay stubs (last 3 months)
3. Most recent tax return (W-2 or Schedule C)
4. Financial Affidavit as filed
5. Bank statement 12-month average (imputed)
6. Earning capacity / market rate (last resort)

### FA Line Mapping for Income:

| FA Line | Description | CS Treatment |
|---|---|---|
| Line 1 | Wages/salary | Social Security Taxable Income (W-2) |
| Line 3 | Business income (net) | Self Employment Taxable Income |
| Lines 4–8 | Other income types | Other Taxable or Non-Taxable as applicable |
| Line 13 | In-kind / reimbursed expenses | Add back as income if business pays personal expenses |

### Deduction Line Mapping:

| FA Line | Description | CS Treatment |
|---|---|---|
| Line 18 | Federal/state income tax | Deduction — use as filed or recalculate |
| Line 19 | FICA | Use W-2 rate (6.2% SS + 1.45% Med) or 0 if SE |
| Line 20 | Medicare | Use W-2 rate or 0 if SE (covered by SE tax) |
| Line 22 | Mandatory retirement | Deduction if truly mandatory |
| Line 23 | Parent health insurance | Deduction — self only, NOT child |
| SE Tax | Self-employment tax | If SE: 15.3% on 92.35% of gross; deduct 50% for fed tax calc |

**CRITICAL:** If a party is self-employed or LLC owner, apply SE tax instead of
FICA/Medicare. The bank statement pattern of direct client payments + irregular
business-to-personal transfers is strong evidence of self-employment status.
Flag for attorney confirmation but use SE tax treatment in the calculation.

---

## STEP 3 — BASIC OBLIGATION (FL SCHEDULE)

1. Calculate each party's net monthly income per § 61.30(3)
2. Sum to combined net monthly income
3. Look up basic obligation from the Florida Guidelines Schedule (1 child, 2 children, etc.)
4. Interpolate if combined net falls between schedule rows
5. Above $10,000 combined net: continue schedule proportionally
6. Split obligation by each parent's percentage of combined net

---

## STEP 4 — ADDITIONS (§ 61.30(7))

Add to basic obligation:
- Confirmed work-related child care (Lines 36 + 39 as applicable — see Q1 above)
- Child health insurance premium (Line 45 confirmed amount)
- Confirmed uncovered medical/dental costs

Split each addition proportionally by income percentage.
The parent who pays the cost receives credit; the other parent owes their share.

---

## STEP 5 — TIME-SHARING ADJUSTMENT (§ 61.30(11))

**Below 73 overnights with obligor:** No adjustment. Obligor pays full
proportionate share of total obligation to obligee.

**73+ overnights (substantial time-sharing):**
1. Multiply each parent's total obligation share by 1.5
2. Multiply Father's adjusted obligation by Mother's overnight percentage
3. Multiply Mother's adjusted obligation by Father's overnight percentage
4. Subtract smaller from larger → net payment direction

**If time-sharing is unresolved:** Run and present ALL of these scenarios:
- Standard / Father <20% (73 nights)
- Father 30% (110 nights)
- Father 35% (128 nights)
- 50/50 (182/183 nights)
- Include any scenario specifically requested by attorney or mediator

---

## STEP 6 — REQUIRED OUTPUTS (BOTH REQUIRED EVERY TIME)

### Output A — FLS-Format Landscape PDF (PRIMARY)

**This is the primary deliverable.** Produce using Python (reportlab) as a
landscape PDF. Format must match Family Law Software output as closely as possible.

**Layout specifications:**
- Page: US Letter landscape (11" × 8.5"), margins 0.5" all sides
- Font: Courier New or equivalent monospace, 9pt body
- Two-column structure:
  - LEFT HALF: Income amounts + deductions table (label | COMBINED | Mother | Father)
  - RIGHT HALF: Results summary (% shares, min need, shared need, overnights,
    payment shares, costs breakdown, presumed amount, adjusted guidelines)
- Column headers: dark gray fill (#333333), white bold text
- Alternating row shading: white / light gray (#F5F5F5)
- Section dividers: thin top border, slightly darker fill (#EEEEEE), bold label
- Summary rows (GROSS INCOME, TOTAL DEDUCTIONS, NET MONTHLY INCOME): blue-gray
  fill (#DDEEFF or #AACCDD), bold
- PRESUMED AMOUNT and ADJUSTED GUIDELINES rows: highlighted fill, bold, bordered
- Header block: case name, case number, "Guidelines (SHARED)", date, "DRAFT —
  MEDIATION USE ONLY — NOT A COURT ORDER" in red
- Footer: assumptions block listing all imputation notes, income sources,
  confirmed vs. estimated figures, flags for attorney review
- File name: `[CaseName]_CSW_[YYYY-MM-DD].pdf`

**FLS column structure (left side):**
```
Income Amounts              COMBINED    Mother    Father
Self Employment Taxable         X          X         X
Social Security Taxable         X          X         X
Other Taxable Income            0          0         0
Taxable Spousal Support         0          0         0
Non-Taxable Sp Support          0          0         0
Other Non Taxable Income        0          0         0
GROSS INCOME                    X          X         X
[section] Deductions from Income
[section] Taxes
FICA - Social Security          X          X         X
FICA - Medicare                 X          X         X
Self Employment Tax             X          X         X
Federal Income Tax              X          X         X
State/Local/Other Income Tax    0          0         0
[section] Other Net Income Deductions
Mandatory Union Dues            0          0         0
Mandatory Retirement Payment    0          0         0
Parent's Health Insurance Pmts  X          X         X
Child Support Ordered and Paid  0          0         0
TOTAL DEDUCTIONS                X          X         X
NET MONTHLY INCOME              X          X         X
```

**FLS right-side summary block:**
```
% of Shared Support     100.00%  XX.XX%  XX.XX%
Minimum Child Support Need   XXX     XXX     XXX
  Mother share / Father share
Shared Support Need        X,XXX   X,XXX   X,XXX
  Mother share / Father share
Overnights              365.0   XXX.0   XXX.0
Overnight Percentage    100.00  XX.XX   XX.XX
Payment Share to Other
  Mother to Father         XXX
  Father to Mother         XXX
Pre Adjustment Transfer    XXX
COSTS
Child Care Costs Paid      XXX     XXX     XXX
Children's Health Insurance XXX    XXX     XXX
Uncovered Med/Dental        XXX    XXX     XXX
TOTAL COSTS PAID            XXX    XXX     XXX
  Mother paid / Father paid
Day Care/Ins/Med/Dental Costs Share  XXX
  Mother share / Father share
Day Care/Ins/Med/Dental Share Adjust
  Mother adjustment / Father adjustment
[highlighted] Presumed Amount To Be Paid  SHARED   XXX
Deviation Factors                                    0
[highlighted] Adjusted Guidelines                  XXX
Manual Child Support Amount
```

### Output B — Narrative Word Doc (SECONDARY)

Portrait .docx with:
- Section 1: Income inputs and source documentation
- Section 2: Deduction methodology and flags
- Section 3: Combined net and basic obligation
- Section 4: Additions (child care, health ins, medical)
- Section 5: Time-sharing adjustment table (all scenarios if unresolved)
- Section 6: Alternative income scenarios if applicable
- Section 7: Open items checklist for session/hearing
- Footer: DRAFT — MEDIATOR'S WORK PRODUCT — CONFIDENTIAL

---

## STEP 7 — FLAGS TO ALWAYS CHECK

Before finalizing output, run through this checklist and note any flags in the
footnote/assumptions block of the PDF:

- [ ] Income imputed vs. FA as filed — note source and basis
- [ ] SE tax applied vs. FICA — note which and why
- [ ] Line 39 confirmed as child care OR extracurricular (not assumed)
- [ ] Line 54 annualized, excluded, or seasonal — note treatment
- [ ] Line 45 (child health ins) confirmed amount vs. estimated
- [ ] Line 23 (parent health ins) correctly excluded from child support addition
- [ ] Time-sharing confirmed vs. scenario only
- [ ] Retroactive support dispute noted if present
- [ ] Any deviation factors identified
- [ ] Net income math verified: gross − deductions = net; net × % = share

---

## STEP 8 — SKILL MEMORY (update after each confirmed run)

After each worksheet is confirmed by Leisa or staff, note in session memory:
- Income figures used and their source
- Child care amount confirmed and basis
- Health insurance amount confirmed
- Time-sharing scenario used for final number
- Final presumed amount / adjusted guidelines figure
- Any deviations agreed

---

## QUICK REFERENCE — § 61.30 FORMULA SUMMARY

```
GROSS INCOME
- Allowable Deductions (tax, FICA/SE, mandatory retirement, parent health ins)
= NET MONTHLY INCOME

Mother Net + Father Net = COMBINED NET

Combined Net → Schedule → BASIC OBLIGATION (1 or more children)

BASIC OBLIGATION
+ Child Care (work-related, confirmed)
+ Child Health Insurance (confirmed monthly premium)
+ Uncovered Medical (if any)
= TOTAL OBLIGATION

Each parent's share = Total Obligation × (their net / combined net)

IF Father nights ≥ 73 (substantial time-sharing):
  Father adj = Father share × 1.5 × (Mother nights / 365)
  Mother adj = Mother share × 1.5 × (Father nights / 365)
  Net payment = larger − smaller → direction to obligee

PRESUMED AMOUNT = Pre-adjustment transfer + obligor's share of costs
ADJUSTED GUIDELINES = Presumed Amount ± Deviations
```

---

## AMBIENT STANDARD — FMLG PLEADING FORMAT & DRAFT-STATE RULES

`fmlg-pleading-standard` governs every court-bound document this skill produces.
Two rules, from the first keystroke:

1. **Format correctly immediately** — portrait, Times New Roman 12 black, single
   spacing 0pt before/after, left aligned, 1" margins, FMLG caption (court centered ·
   case/division right · parties left · rule line ending in `/` · title centered
   bold ALL CAPS), numbering I. → 1. → a. → i. continuous. No bullets, no dividers.
   There is no rough-format stage that gets fixed later.
2. **Drafts show their work, highlighted** — attorney notes 🟨, outstanding facts 🟨,
   alternative provisions 🟩 drafted in full. When unclear what the pleading should
   contain, present highlighted ALTERNATIVES — never assume and draft one version
   as if decided. Never strip flags at draft stage; only `fmlg-finalize-draft`
   strips, after the attorney resolves them.

---

## MANDATORY HANDOFF — PRE-FILING QC GATE

Any document this skill produces that will be **filed with a court, served on a
party, or sent outside the firm** goes to `fmlg-prefiling-qc` before it reaches
an attorney. This handoff is not optional and is not skippable for urgency.

```
THIS SKILL  →  fmlg-prefiling-qc  →  ATTORNEY SIGN-OFF  →  FILE / SERVE / SEND
```

- Do not present a draft as "ready for Naz" or "ready to file" until the gate has run.
- A **BLOCKED** verdict returns the draft here for correction. Fix and re-run the gate.
- A **CONDITIONAL** verdict goes to the attorney with the findings attached.
- Never resolve a flagged item by deleting the language to make the gate pass.

- After the gate clears, hand the document to `fmlg-finalize-draft` to produce the
  filing-ready Word file and PDF. That skill enforces portrait, Times New Roman 12,
  all black, single spacing, the FMLG caption layout, strips every internal artifact,
  and checks `fmlg-judicial-procedures` for the assigned judge before output.

**Approval behavior:** if the person in the session is an FMLG attorney (Leisa or
Naz), her instruction IS the sign-off — do not ask her to approve what she just
directed. If staff, every attorney-gated item routes to Naz or Leisa and waits.

---

## OUTPUT DELIVERY — FIRM STANDARD (v2, SharePoint-native)

All output from this skill is delivered through `fmlg-sp-connector` (Operation 4).

**Destination:** `Notes/` in the SharePoint matter folder
`Last, First - [Matter Type] (####-####)`. There is no `CLAUDE OUTPUT` folder and
no Dropbox path. (`GAL Notes/` on GAL matters.)

**Filename:** `MM.DD.YY - LastName - DocTitle - v1.ext` — versioned, never overwritten.

**Delivery depends on where this skill is running:**

- **Claude.ai (chat / Projects)** — Claude cannot write to SharePoint. Present the file
  as a **download** and print the destination block: matter folder → `Notes/`, filename,
  version. Never write "saved to SharePoint."
- **Cowork (desktop)** — write to the folder designated for the session (ask once at
  first delivery, reuse thereafter), confirm the **actual path written**, and state
  where the file belongs in SharePoint.

Nothing is filed or sent without attorney sign-off. Time is tracked in Smokeball,
including Claude-assisted work.

