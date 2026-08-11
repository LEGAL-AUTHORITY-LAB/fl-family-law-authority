---
name: "fmlg-income-assessor"
description: "FMLG non-standard deposit income assessor. Rapid first-pass characterization of irregular deposits for support purposes — the light version of full Stage 5 income analysis. Use when bank statements show deposits that do not match the Financial Affidavit. Triggers on: \"assess these deposits,\" \"what are these deposits,\" \"run the income assessor,\" \"characterize the deposits,\" \"are these deposits income,\" \"unexplained deposits,\" \"cash deposits,\" \"Venmo income,\" \"his deposits don't match his FA,\" or any request to classify non-payroll deposits in a Florida family law matter. Produces the Deposit Characterization Chart with a support-inclusion flag per deposit stream. Escalates to fmlg-income-analysis when income is genuinely complex (self-employment, multiple businesses, disputed year-over-year variance). Always assign to Sara; attorney reviews before any figure is used."
---

# FMLG Income Assessor — Non-Standard Deposits

## FMLG Firm-Wide Conventions (apply to every run of this skill)

These six conventions govern all FMLG skills and override any narrower instruction below that conflicts with them.

1. **Environment-flexible.** Complete the task where you are; suggest a better environment in one line if warranted, and keep working.
2. **Identity over lanes.** Staff assignments are defaults. Attorneys self-approve.
3. **Just run it.** Soft checks, never hard gates.
4. **Read files first.** Search the whole matter file before declaring anything missing.
5. **Transcripts preferred, never required.**
6. **Write to the command center** before the run ends.

---

## Purpose

Fast, chartable characterization of deposits that are not routine payroll: what the stream is, how regular it is, what it annualizes to, and whether it appears includable as income for support under section 61.30(2), Florida Statutes. This is the first-pass tool. It does NOT replace full income analysis — it decides whether full analysis is needed and hands off cleanly.

## When to Use This vs. fmlg-income-analysis

| Situation | Skill |
|---|---|
| Deposits don't match the FA; need a quick characterization | THIS skill |
| Recurring P2P/cash/third-party deposits to classify | THIS skill |
| Self-employment or business income requiring Schedule C work | fmlg-income-analysis |
| Overtime/bonus/commission averaging across years | fmlg-income-analysis |
| Rental income with expense netting | fmlg-income-analysis |
| Court-ready income determination memo | fmlg-income-analysis |

## Workflow

**Step 1 — Isolate the streams.** From the produced bank statements, list every deposit that is not identified payroll. Group into streams by source pattern: same payer, same platform (Venmo/Zelle/PayPal/Cash App), same memo string, cash deposits, business-entity deposits, third-party recurring deposits.

**Step 2 — Characterize each stream.** For each: source (known/unknown), frequency (weekly/monthly/sporadic), period covered, count, total, monthly average, and annualized figure. Note whether the stream appears on the FA anywhere.

**Step 3 — Support-inclusion flag.** Tag each stream:
- LIKELY INCLUDABLE — recurring and income-like (regular payments for services, recurring business draws, rental-pattern receipts)
- POSSIBLY INCLUDABLE — recurring but source unknown; needs discovery follow-up
- LIKELY NOT INCOME — one-time transfers, refunds, reimbursements, account-to-account moves, gift-pattern single deposits
- NEEDS ATTORNEY CALL — in-kind support, recurring gifts, cohabitant contributions

Every tag is a **flag for attorney review, never a legal conclusion.**

**Step 4 — Reconcile to the FA.** One summary table: FA claimed monthly income vs. payroll deposits vs. non-standard streams (by tag), with the delta stated.

**Step 5 — Route.** If any stream is business-sourced, variable across years, or disputed → recommend fmlg-income-analysis by name and say exactly why. Discovery follow-ups route to fmlg-advanced-discovery; undisclosed-account leads route to fmlg-deep-scan.

## Output — Deposit Characterization Chart

Excel per fmlg-output-standards:

| Stream | Source | On FA? | Frequency | Months covered | Count | Total | Monthly avg | Annualized | Tag | Follow-up |

Plus a short memo section: what was assessed, the FA delta, the attorney-call items, and the routing recommendation.

## Hard Rules

- Numbers come only from the produced documents; every figure cites its statement and line. No estimates without labeling them as estimates.
- No support calculation here — guideline math belongs to fmlg-cs-worksheet with attorney-approved income figures.
- QC via fmlg-disco-qc before output moves to Karen. Save to NOTES via fmlg-sp-connector; update disco tracker and command center; log time in Smokeball.
