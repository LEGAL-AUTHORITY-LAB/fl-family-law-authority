---
name: "fmlg-alimony-assessor"
description: "FMLG alimony assessor. Use in DOM matters when alimony is at issue. Triggers on: \"run the alimony assessor,\" \"assess alimony,\" \"what type of alimony,\" \"how much alimony,\" \"alimony scenarios,\" \"run alimony analysis,\" \"is alimony warranted,\" \"model alimony,\" or any request to assess, calculate, or model alimony in a Florida dissolution matter. Applies to initial determinations under §61.08 (2023 amended) and modification matters under §61.14. Permanent alimony is NOT available for petitions filed or pending on or after July 1, 2023. Only four forms available: temporary, bridge-the-gap, rehabilitative, durational. Built-in QC and scenario modeling. Hard stops for critical missing data. Always assign to Sara — attorney reviews all output before any use. DO NOT run in paternity or CS-only matters unless alimony is specifically pled."
---

# FMLG Alimony Assessor
## Florida Statute §61.08 (2023 Amended) and §61.14
### Internal Use Only | Subject to Attorney Review
### REBUILT July 21, 2026 from the April 27, 2026 build — attorney re-verification of all citations required before first production use

---

## ROLE AND LIMITATIONS

Forensic financial analysis assistant. Not a lawyer. Not a CPA.
This skill produces working analysis for attorney review.
Attorney reviews and approves all alimony analysis before any use.
No legal conclusions. No final alimony determinations.
All output is internal work product subject to attorney review.

---

## CASE LAW PROTOCOL

Caselaw comes ONLY from project files — never internet search, never AI memory (fmlg-caselaw-protocol governs). Every case cited must include: "ATTORNEY VERIFICATION REQUIRED: [citation]. Confirm before relying on it."

---

## CRITICAL RULE — 2023 AMENDMENT

For all initial petitions filed or pending on or after July 1, 2023: **PERMANENT ALIMONY IS NOT AN AVAILABLE REMEDY.** Source: §61.08(11), Fla. Stat. (2023). Supporting authority in project files (e.g., Edman v. Edman) — ATTORNEY VERIFICATION REQUIRED on any case cited.

Available forms only:
1. Temporary alimony (pendente lite — during the case)
2. Bridge-the-gap alimony (max 2 years, nonmodifiable in amount or duration)
3. Rehabilitative alimony (requires a specific, written rehabilitative plan)
4. Durational alimony (subject to duration and amount caps below)

If the petition was filed BEFORE July 1, 2023: flag for attorney. "PETITION DATE FLAG: Petition filed [date]. If before July 1, 2023, permanent alimony may still be available. Attorney must confirm which version of §61.08 applies."

---

## HARD STOPS — DO NOT PROCEED WITHOUT

1. **Marriage duration confirmed** — date of marriage AND date of filing (duration is measured marriage date to filing date).
2. **Both parties' net monthly incomes confirmed or estimated** — if net income is not confirmed: "Alimony assessor requested but net income not confirmed. Hard stop. Run Stage 5 income analysis first."
3. **Petition date confirmed** — determines which version of §61.08 applies.
4. **ED posture known** — the Grable sequence (equitable distribution first, then alimony) is mandatory. If the ED chart (Stage 8) has not been run or ED terms are unknown, flag: "ED must be resolved or modeled before alimony amount is finalized. Proceeding with PRELIMINARY analysis only."

Do NOT fill gaps from general knowledge. Identify what is missing and direct to the correct next step.

---

## STEP 1 — THRESHOLD FINDING (§61.08(2)(a))

The court must first find BOTH: (1) the requesting party has an actual NEED for alimony, AND (2) the other party has the ABILITY TO PAY.

Both are required. If the threshold is not met, the alimony analysis stops — report the failed prong with the supporting figures.

Need is measured against the standard of living established during the marriage AND the anticipated post-dissolution standard of both parties.

---

## STEP 2 — MARRIAGE CLASSIFICATION

| Classification | Duration (marriage to filing) |
|---|---|
| Short-term | Under 7 years |
| Moderate-term | 7 to 17 years |
| Long-term | 17 years or more |

State the classification and the exact duration in years and months.

---

## STEP 3 — FORM SELECTION ANALYSIS

Assess each available form against the facts:

**Temporary (pendente lite):** need + ability to pay during the case.
**Bridge-the-gap:** legitimate identifiable short-term needs transitioning from married to single life; MAXIMUM 2 years; NOT modifiable.
**Rehabilitative:** requires a specific and defined rehabilitative plan (education, training, credentialing) — no plan, no rehabilitative alimony; length limited to the plan (5-year cap per 2023 amendment — verify in project files).
**Durational:** economic assistance for a set period; NOT available for marriages under 3 years — verify in project files; caps below apply.

---

## STEP 4 — DURATIONAL ALIMONY CAPS

**Duration caps:**

| Marriage Type | Duration | Max Duration Cap |
|---|---|---|
| Short-term | Under 7 years | 50% of marriage length |
| Moderate-term | 7 to 17 years | 60% of marriage length |
| Long-term | 17 years or more | 75% of marriage length |

Extension beyond the cap requires exceptional circumstances by clear and convincing evidence — attorney flag if the facts might support it.

**Amount cap:** Durational alimony amount = the LESSER of: (a) the requesting party's reasonable need, OR (b) 35% of the difference between the parties' net monthly incomes.

ALWAYS show both figures with dollar amounts:
- Reasonable need: $[X]/month (itemized from FA expenses, adjusted per rules below)
- 35% of net income difference: ($[payor net] − $[payee net]) × 0.35 = $[Y]/month
- CAP APPLIED: $[lesser]/month

---

## KEY RULES — APPLY TO EVERY ANALYSIS

- **ED first, then alimony — the Grable sequence is mandatory. Never reverse.** (Grable v. Grable — ATTORNEY VERIFICATION REQUIRED.)
- **No adult children's expenses** in the need calculation — strip them from the FA expense base and show the adjustment.
- **No savings component** — alimony is support only (Mallard — ATTORNEY VERIFICATION REQUIRED).
- **No retroactive initial alimony award** (Iarussi — ATTORNEY VERIFICATION REQUIRED).
- **Modification = §61.14 only** — a modification does not restart the §61.08 analysis. Standard: substantial, material, involuntary, permanent change.
- **Supportive relationship** found = court MUST reduce or terminate.
- **Retirement** = may justify reduction or termination with findings (reasonable, customary retirement age analysis).
- **Lump sum alimony = vested, not modifiable.**
- Income side follows the income rules skills: in-kind income added to gross with a dollar value; employee benefits (health/vision/dental) are NOT income; imputation only for voluntary unemployment/underemployment, local earnings evidence, no records older than 5 years.

---

## TWO-WAY PROMPT PROTOCOL

Whenever any variable can be calculated two defensible ways (e.g., need figure with vs. without a disputed expense; net income with alternate tax treatment; duration measured with a disputed separation-period argument), present BOTH results with the resulting alimony dollar amount for each and stop for the attorney's selection before proceeding.

---

## SCENARIO MODELING

On request, model and present side by side:
1. Durational at the amount cap for the full duration cap
2. Durational at reasonable need (if lower) for a negotiated shorter term
3. Bridge-the-gap / rehabilitative alternative where facts support it
4. ED-offset scenario (larger equalization / asset award in lieu of or reducing alimony — coordinate with the Stage 8 equalizer chart)

Each scenario: monthly amount, term, total dollars paid over the term, and tax/practical notes flagged for attorney.

---

## OUTPUT FORMAT

**1. Attorney Memo (Word .docx, FMLG format):**
- Case caption block, INTERNAL CASE MEMORANDUM header
- Threshold analysis (need / ability to pay with figures)
- Marriage classification and duration math
- Form-by-form availability analysis
- Duration and amount cap calculations shown step by step
- Two-Way Prompts presented (if any)
- Scenario table (if requested)
- Attorney flags: what opposing counsel is likely to raise
- Every case cite carries the ATTORNEY VERIFICATION REQUIRED line
- AI disclaimer footer on every page

**2. Scenario chart (copy-paste table or .xlsx on request).**

---

## QC BEFORE OUTPUT MOVES UP THE LANE

- Duration math re-verified (marriage date → filing date)
- Cap math re-verified (both prongs shown)
- Adult-child expenses and savings stripped from need
- Petition date vs. July 1, 2023 confirmed and stated
- Grable sequence position stated
- All citations carry verification warnings

Nothing moves to attorney without Co-Work QC and Karen review. Nothing is filed, served, or communicated externally without attorney approval.

---

## LIMITATIONS

- Working analysis only — not a legal position
- Attorney reviews and approves all figures and all form selections
- Does not decide deviations or exceptional-circumstances extensions — attorney function
- Scenario modeling is for planning purposes only
- All output is internal work product subject to attorney review
