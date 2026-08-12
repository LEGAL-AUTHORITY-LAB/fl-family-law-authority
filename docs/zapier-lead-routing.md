# FMLG Lead Routing — Zapier Build Sheet

**For:** Henry (Zapier build)
**Prepared:** 2026-08-11
**Scope:** Wire the 10 WordPress (Jetpack) intake forms → Smokeball Lead + Slack `#leads` + SharePoint LEADS folder.

The forms are built as native **Jetpack Form blocks** on `familymatterslawgrouplaw.wpcomstaging.com` (draft pages, IDs 30–39). Each currently emails `lwintz@fmlgpa.com`. This sheet defines the automation that replaces/augments that email.

---

## 1. Trigger

Use Jetpack Forms' built-in Zapier connection (preferred) — in each form's block editor: **Form settings → Connect → Zapier**. That exposes a Zapier trigger **"New Jetpack Form submission"** per form.
(Alternative: Webhooks *Catch Hook* + Jetpack form webhook — the Webhooks app is already connected on this account.)

**Recommendation:** one Zap per form (10 total), matching the existing Zap-per-purpose pattern — keeps the `description`/`referralType` mapping simple.

## 2. Actions, in order (every Zap)

1. **Smokeball → Create Lead** (§3)
2. **Slack → Send Channel Message** to `#leads` (§4)
3. **Microsoft SharePoint → Create File** in the LEADS folder (§5)

---

## 3. Smokeball · Create Lead — field mapping

**Fixed on every form:**

| Field | Value |
|---|---|
| `contactType` | `Person` |
| `location` | `FL` |
| `matterTypeId` | `Family - FL`  (id `bbfcb853-a5a5-4892-9863-2d0fe9125019_FL`) |
| `isExistingClient` | `false` |

**From the form:** `firstName`, `lastName` ← name fields · `email` ← email · `mobilePhoneNumber` ← phone/cell.

**Per-form `referralType` + `description` + `notes`:** (`referralType` values below are all REAL Smokeball values — do not invent new ones.)

| Form (page id) | referralType | description (composed string) | notes |
|---|---|---|---|
| **Get Started** (30) | the visitor's "How did you hear about us?" value (or UTM source) | `CASE TYPE: {service} \| FILED: {case_filed} \| SERVED: {served} \| SUMMARY: {summary}` | `Consultation: {consultation} \| Contact: {contact_method} \| For: {who_for} {who_for_detail} \| Policy ack: {policy_ack}` |
| **Document Prep & Review** (31) | `Website Form Inquiry` | `CASE TYPE: {matter} \| COUNTY: {county} \| ASSISTANCE: {assistance} — via Document Prep/Review` | `Text consent: {ok_to_text} \| Other party: {other_first} {other_last} ({other_email})` |
| **Form Package Request** (32) | `Website Form Inquiry` | `FORM PACKAGE REQUEST \| CASE TYPE: {matter} \| KNOWS FORMS: {knows_forms} \| FORMS: {which_forms} \| SITUATION: {situation} \| CHOICE: {package_choice} \| COUNTY: {county}` | `Tutorial videos: {tutorial} \| Text consent: {ok_to_text}` |
| **DIY Coaching** (33) | the visitor's "How did you hear about us?" value | `CASE TYPE: {matter} \| COUNTY/CITY: {county} \| HELP WANTED: {help_text} — via DIY Coaching` | `Text consent: {ok_to_text} \| Other party: {other_party}` |
| **Get in Touch / General** (35) | `Web` | `WEB LEAD — GENERAL \| STATE: {state} \| SUMMARY: {summary}` | `Preferred contact: {contact_method}` |
| **Submit Files for Review** (36) | `Website Form Inquiry` | `Submitted files for review — see attachment in the form notification email.` | — |
| **Book a Free Consultation** (34) | `Website Form Inquiry` | `Requested free consultation with senior paralegal.` | `Cell: {phone}` |
| **Mediation Intake** (37) | `Website Form Inquiry` | `MEDIATION INTAKE \| NEEDS: {needs} \| OTHER PARTY: {other_party} \| ATTORNEY REP: {atty_rep} {atty_name} {atty_email} \| COUNTY: {county} \| CASE: {case_desc} \| MEDIATOR PREF: {mediator_pref}` | `Client phone: {phone}` |
| **Guardian ad Litem Referral** (38) | the visitor's value — typically `Attorney` or `Court` | `GAL REFERRAL \| STATUS: {case_status} \| CASE #: {case_number} \| FILING: {filing_date} \| COUNTY: {county} \| CASE: {case_desc}` | `Parent 1: {p1_name} ({p1_phone}, {p1_email}) \| Parent 2: {p2_name} ({p2_phone}, {p2_email}) \| Attorneys: {atty_rep} {atty_name}` |
| **Domestic Violence / Injunction** (39) | the visitor's value | `URGENT — DV/INJUNCTION INTAKE \| POSTURE: {posture} \| SERVED: {served} \| TYPE: {injunction_type} \| COUNTY: {county} \| POLICE: {police} \| EVIDENCE: {evidence} \| ALLEGATIONS: {narrative}` | `Address: {address} \| Marital: {marital_status} \| Other party: {other_party} ({relationship}) \| Children: {has_children} {children_detail}` |

> Rationale: Smokeball's Create Lead action has no per-case-type field — the only Lead Type is `Family - FL`. So the specific case type and all detail live in `description`, formatted to be scannable when Angie converts Lead → Matter. (Worth a 5-min check with Smokeball support on whether the API exposes a sub-type field Zapier isn't surfacing.)

---

## 4. Slack · Send Channel Message → `#leads`

- **Channel:** `#leads`
- **Message text (template):**
  ```
  :inbox_tray: *New lead — {Form Name}*
  *{lastName}, {firstName}*  ·  {email}  ·  {phone}
  {first line of description}
  _via {referralType}_
  ```
- **Domestic Violence form:** prefix with `:rotating_light: *URGENT — DV / Injunction*` and (recommended) also post to / @-mention the case-management channel. Decision for Leisa: add a "someone will call you within X hours" auto-reply on this form (Jetpack custom response).

## 5. Microsoft SharePoint · Create File → LEADS folder

- **Connector:** Microsoft SharePoint → *Create File* (or *Create Text File* / *Upload File*).
- **Site:** `FAMILYMATTERSLAWGROUPMATTERS`
- **Folder:** `Shared Documents / OPEN FILES / LEADS - OPEN`
  (link: https://slgpa2013.sharepoint.com/:f:/r/sites/FAMILYMATTERSLAWGROUPMATTERS/Shared%20Documents/OPEN%20FILES/LEADS%20-%20OPEN )
- **File name:** `{lastName}, {firstName} - {Form Name} ({MM-DD-YYYY}).txt`
  e.g. `Doe, Jane - Mediation Intake (08-11-2026).txt`
- **File contents:** the full lead detail (all submitted fields, one per line) so the loose file is self-contained.
- **Important:** create ONLY this single loose file per lead. **Do NOT** create a full matter folder/structure — that happens later, and only when a paid consult is actually booked (per Leisa).

---

## 6. Special cases / filters

- **General form (Web Lead) — Florida-only gate:** add a Zapier **Filter** after the trigger: *only continue if `State` = FL* (case-insensitive). If not FL, skip Smokeball and instead send a "we're not licensed in your state" auto-reply.
- **Get Started — paid consult → LawPay:** if `Consultation preference` = *Paid $250 strategy session*, the visitor should get the LawPay link `secure.lawpay.com/pages/familymatterslawgroup/strategy-session`. Jetpack can't show it conditionally on the thank-you screen, so add a Zap **Filter + Email** step: when paid is chosen, email the LawPay link. (Free-consult picks get the normal thank-you.)
- **De-dup / attribution:** the Get Started form can carry UTM source/campaign, landing URL, and timestamp — map these into `notes` or a Zapier de-dup step if desired.

## 7. Real Smokeball `referralType` values (reference)

`Website Form Inquiry`, `Web`, `Direct`, `Existing Client`, `Previous Client`, `Word of Mouth`, `Attorney`, `Court`, `Friend`, `Facebook`, `INSTAGRAM`, `GOOGLE`, `Seminar`, `Radio Ad`, `Billboard`, `Walk-in`, `Other`.
