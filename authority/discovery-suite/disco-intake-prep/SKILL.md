---
name: fmlg-disco-intake-prep
description: >
  FMLG pre-discovery document intake skill for Sara. Use this skill immediately
  whenever a new matter is ready for discovery document processing, documents
  have arrived via Pipefile into SharePoint, or Sara needs to audit, rename, and
  organize client and opposing party documents before any discovery stage skill
  runs. Triggers on: "documents are in SharePoint," "Pipefile docs are ready,"
  "organize the disco folder," "documents came in," "prep the discovery folder,"
  "rename the client docs," "set up the DISCO folders," "documents need to be
  sorted," "what came in for this matter," "run the disco intake," or any
  request to audit, sort, rename, or organize incoming financial or discovery
  documents before Stage 2 fires. This skill MUST run before any fmlg-discovery
  workflow skill. It is the document prep gate — nothing goes to Karen or the
  discovery stages until this skill confirms the folders are clean, named
  correctly, and organized. Always assign to Sara.
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

# FMLG Discovery Document Intake Prep
## Staff Lane: Sara | Runs in: Claude Cowork (Desktop App)
## Triggers Before: All fmlg-discovery-scope-router and Stage workflow skills

This skill prepares incoming client and opposing party financial documents for
the FMLG discovery workflow. Sara runs this in Claude Cowork, pointing Claude
at the client's SharePoint matter folder. Claude audits what arrived, renames
every document to FMLG naming standards aligned with Florida Rule 12.285
mandatory disclosure categories, sorts documents into the correct DISCO
subfolders, flags anything missing, and saves everything ready for Stage 2.

No documents go to Karen or the discovery stage skills until this skill
produces a clean Intake Confirmation.

---

## BEFORE YOU START — COWORK SETUP

Sara, this skill runs in **Claude Cowork on the Desktop App**, not in the
browser. If you are reading this in the browser, switch to the Desktop app,
open Cowork, and start a new session there.

**In Cowork:**
1. Open a new Cowork session
2. When prompted for folder access, navigate to the client's SharePoint
   matter folder
3. Grant Claude access to the entire matter folder for this session
4. Paste the skill trigger phrase: **"Run DISCO intake prep for [Matter Name]"**

The matter folder in SharePoint mirrors Smokeball exactly:
```
[Matter Name]/
├── Billing, Retainer, ID, Notes
├── Correspondence
├── DISCO - CLIENT          ← client documents land here after this skill
├── DISCO - OP              ← opposing party documents land here after this skill
├── DRAFTS
├── FILED BUT NOT ACCEPTED
├── FILED DOCUMENTS - Client
├── FILED DOCUMENTS - OP
├── NOTES
├── NOTICES
├── ORDERS
├── REPORTS & AGREEMENTS
└── Research/Education
```

---

## STEP 1 — CONFIRM CASE IDENTITY

Before touching any documents, confirm the following with Sara:

- **Client first name** (used as party identifier in all file naming)
- **Opposing party first name** (used as party identifier in all file naming)
- **Which party is H and which is W** — confirm before sorting begins
- **Documents arrived for:** Client only / OP only / Both

If Sara is unsure which party is which, stop and confirm with Karen before
proceeding. Misrouting a document to the wrong DISCO folder creates errors
that are hard to catch downstream.

---

## STEP 2 — AUDIT INCOMING DOCUMENTS

Scan the SharePoint matter folder for all documents that have arrived via
Pipefile or are sitting unsorted in the matter root. Produce a raw inventory
list — document name as it currently exists, file type, and apparent content
based on filename or visible metadata.

Do not rename or move anything yet. Just report what is there.

Deliver the inventory in this format:

```
INCOMING DOCUMENT INVENTORY — [Matter Name] — [Date]

CLIENT DOCUMENTS FOUND: [#]
[Current filename] — [Apparent type] — [Readable? Y/N]

OPPOSING PARTY DOCUMENTS FOUND: [#]
[Current filename] — [Apparent type] — [Readable? Y/N]

UNIDENTIFIED / UNCLEAR: [#]
[Current filename] — [Why unclear]
```

Ask Sara to confirm the inventory before proceeding to renaming.

---

## STEP 3 — CONFIRM DISCO SUBFOLDER STRUCTURE EXISTS

Before sorting, verify that both DISCO - CLIENT and DISCO - OP contain
the required 12 subfolders. If any subfolder is missing, create it before
moving documents.

**Required subfolders inside both DISCO - CLIENT and DISCO - OP:**

| Subfolder Name | Florida Rule 12.285 Category |
|---|---|
| Brokerage Accounts | Investment accounts, securities |
| Business Tax Returns | Business returns, Schedule C, K-1 source docs |
| Checking Statements | All checking and savings account statements |
| Credit Cards | Credit card statements |
| Deeds | Real property ownership documents |
| Last 6 Months of Paychecks | Recent pay stubs, payroll records |
| Last Years W-2 K-1 1099 or Other Income | Annual income documents |
| Life and Health Insurance Documents | Insurance policies and statements |
| Loan Applications | Loan applications, financial statements submitted to lenders |
| Other Account Statements | Money market, CDs, HSA, retirement not covered above |
| Other Liabilities | Mortgage statements, auto loans, personal loans, all non-CC debt |
| Tax Returns | Personal federal and state returns, all years produced |

If a subfolder is missing from either DISCO - CLIENT or DISCO - OP, create
it using the exact name above before moving any documents.

---

## STEP 4 — RENAME ALL DOCUMENTS

Rename every document using the FMLG naming convention:

**`[FirstName]_[12.285Category]_[Institution]_[Period]`**

### Naming Rules

**FirstName** — Use the party's first name exactly as confirmed in Step 1.
Not last name. Not initials. First name only.

**12.285Category** — Use the standardized category names below. Match the
document to the correct category — do not invent new categories.

| Document Type | Use This Category Name |
|---|---|
| Checking or savings account statement | CheckingStatement |
| Brokerage or investment account statement | BrokerageStatement |
| Personal tax return (1040) | TaxReturn |
| Business tax return (1120, 1065, Schedule C) | BusinessTaxReturn |
| W-2 | W2 |
| 1099 (any type) | 1099 |
| K-1 | K1 |
| Pay stub / paycheck | Paystub |
| Life or health insurance document | InsuranceDoc |
| Deed or title | Deed |
| Loan application | LoanApplication |
| Credit card statement | CreditCardStatement |
| Mortgage statement | MortgageStatement |
| Auto or personal loan statement | LoanStatement |
| Other liability document | LiabilityDoc |
| Other account statement (HSA, CD, money market) | AccountStatement |

**Institution** — Name of the bank, employer, or issuer. Use a clean short
version — BofA not BankofAmerica, WellsFargo not Wells Fargo Bank NA.
If unknown from the filename, mark as Unknown and flag for Sara to confirm.

**Period** — Use MonYYYY for a single month (Jan2025) or
MonYYYY-MonYYYY for a range (Jan2025-Jun2025). For annual documents
like tax returns use the tax year (2024).

### Naming Examples

```
Jennifer_CheckingStatement_BofA_Jan2025-Jun2025
Jennifer_TaxReturn_Federal_2024
Jennifer_Paystub_AcmeCorp_Mar2025
Jennifer_W2_AcmeCorp_2024
Jennifer_CreditCardStatement_Chase_Jan2025
Robert_BrokerageStatement_Fidelity_2024
Robert_MortgageStatement_Quicken_Jan2025
Robert_BusinessTaxReturn_Federal_2023
```

---

## STEP 5 — SORT INTO CORRECT DISCO SUBFOLDERS

After renaming, move each document into the correct subfolder:

- Client documents → **DISCO - CLIENT** → correct subfolder
- Opposing party documents → **DISCO - OP** → correct subfolder

Match each renamed document to its subfolder using the 12.285 category
table in Step 3. If a document could fit two categories, use the more
specific one and note it in the Intake Confirmation.

If a document cannot be identified well enough to name or sort correctly,
do not guess. Place it in a **REVIEW NEEDED** holding folder inside the
matter root and flag it for Sara to review before the session closes.

---

## STEP 6 — PRODUCE THE INTAKE CONFIRMATION

Once all documents are renamed and sorted, deliver the Intake Confirmation
to Sara. This is what she sends to Karen to signal the file is ready for
Stage 2.

```
DISCO INTAKE CONFIRMATION — [Matter Name] — [Date]
Prepared by: Sara | Reviewed in: Claude Cowork

DISCO - CLIENT — [Total # documents]
  Brokerage Accounts: [#]
  Business Tax Returns: [#]
  Checking Statements: [#]
  Credit Cards: [#]
  Deeds: [#]
  Last 6 Months of Paychecks: [#]
  Last Years W-2 K-1 1099 or Other Income: [#]
  Life and Health Insurance Documents: [#]
  Loan Applications: [#]
  Other Account Statements: [#]
  Other Liabilities: [#]
  Tax Returns: [#]

DISCO - OP — [Total # documents]
  [Same subfolder breakdown]

MISSING / NOT YET RECEIVED:
  [List each 12.285 category with no documents — client and OP separately]
  [Flag any category required by Rule 12.285 that is empty]

REVIEW NEEDED (Sara to resolve before Stage 2):
  [List any documents placed in REVIEW NEEDED folder with reason]

READY FOR STAGE 2: YES / NO
  If NO — list what must be resolved first
```

Sara saves this confirmation to the **NOTES** folder in the matter and
sends a copy to Karen in Smokeball before closing the Cowork session.

---

## GUARDRAILS

Do not rename or move documents without Sara confirming the party
identity in Step 1. A misrouted document that reaches the FA crosscheck
skill under the wrong party name creates errors that are hard to catch.

Do not proceed to Step 5 without Sara confirming the document inventory
in Step 2. If something in the inventory looks wrong — extra documents,
wrong party name in a filename, documents that don't match the matter —
stop and flag it before sorting.

Do not create new subfolder names. The 12 subfolders are fixed. If a
document doesn't fit, use Other Account Statements or Other Liabilities
and note it in the Intake Confirmation.

Do not mark the file READY FOR STAGE 2 if there are unresolved items in
the REVIEW NEEDED folder. Karen needs a clean file before Stage 2 fires.

Time is tracked in Smokeball. Sara logs this task under the matter before
closing the session — document intake and organization, time spent.

---

## STAFF LANE SUMMARY

| Who | Does What |
|---|---|
| Sara | Runs this skill in Cowork, confirms inventory, saves Intake Confirmation to NOTES, logs time in Smokeball |
| Karen | Receives Intake Confirmation, clears Sara to move to Stage 2 |
| Leisa / Naz | Not involved until Stage 2 output is ready for review |
EOF

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

