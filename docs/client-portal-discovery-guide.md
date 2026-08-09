# Client Portal & Discovery Collection App — Master Build Guide
**Prepared for: New Lovable Build Project (Client Portal / Discovery Collection)**
**Prepared by: LAL Ops (Claude) for Leisa Wintz**
**Date: August 9, 2026**

> **Internal planning document — confidential.** Contains client names, retainer
> rates, and business strategy. This file lives under `docs/` and is excluded
> from the public GitHub Pages deploy. Do not move it into the web-served tree.

---

## 0. Why This Exists

Right now FMLG (and every LAL client firm) runs three things as if they were unrelated:

1. A client communication channel (email, Tiiny hub, phone)
2. A discovery collection/tracking process (SharePoint folders, spreadsheets, the `fmlg-disco-*` skill chain)
3. A pleadings/orders repository the client never sees (SharePoint, filed vs. draft folders)

They are not unrelated. The client's discovery IS the input to the Financial Affidavit. The FA IS the thing mediation and drafting depend on. The pleadings/orders ARE what the client needs to see to understand their own case. Splitting these into separate systems means re-explaining status to the client every time, manually re-keying what's already tracked in the disco tracker, and manually deciding what's "safe" to show them.

**The fix:** one client-facing portal, built in Lovable, that sits on top of the firm's existing OneDrive/SharePoint structure and existing skill-driven tracking — not a replacement for either, a front end for both.

This guide covers two related but separate builds. Read the distinction carefully before scoping either one.

---

## 1. Two Builds, Not One

### Build A — Litigation Client Portal & Discovery Collection App
**Who it's for:** FMLG's own family law clients first. If it works, this becomes a licensable LAL product for other firms (fits naturally as a Command Center portal module or a standalone add-on).
**What it replaces:** Nothing yet — this doesn't exist today. Clients currently get discovery requests and updates by email/phone with no self-service visibility.
**Core content:** Discovery collection, financial affidavit intake, deadline/event tracking, and read-only access to the four link categories (filed pleadings, OP's filed pleadings, notices/orders, client discovery).

### Build B — LAL Coaching Client Portal
**Who it's for:** LAL's own coaching clients (attorneys who bought systems + retainer), starting with 2–3 live ones as the test bed.
**What it replaces:** The Tiiny hub (single-file HTML per client) and, eventually, some of what Slack currently does.
**Core content:** Owner-attorney live tracker (suites owned, install progress), retainer balance, session history, resource library, Zoom booking links, and either a Slack hand-off or an embedded chat.

**Why build both at once, in one project:** they share the same Lovable + storage architecture, the same auth pattern (email-restricted access, no heavy account system), and Build B is the faster, lower-risk way to prove the Lovable pattern before betting Build A's complexity on it. Recommend scoping Build B first as the MVP, Build A second — see Section 6.

---

## 2. Build A in Detail — Litigation Client Portal & Discovery Collection

### 2.1 The four link categories (per matter)
Every matter gets four designated OneDrive link mappings, set by staff, invisible-but-referenced to the client as named sections in the portal:

| Category | Client sees | Client can |
|---|---|---|
| **Filed Pleadings (ours)** | Everything FMLG has filed on their behalf | View, download to own OneDrive |
| **Opposing Party Filed Pleadings** | Everything OC has filed | View, download to own OneDrive |
| **Notices & Orders** | Hearing notices, court orders | View, download to own OneDrive |
| **Client Discovery** | Their own produced discovery documents | View, download, AND upload new ones |

**Critical rule carried over from `fmlg-filing-status-rules`:** a document only appears in "Filed Pleadings" once it is actually in the filed folder — a draft is never shown to the client as filed. The portal should read folder location as the source of truth, exactly like the internal skill does. This means the portal's "filed" view should point at the SharePoint **Filed Documents** subfolder specifically, not the whole matter folder.

### 2.2 Discovery collection & tracking module
This is the part that has to mirror the existing 9-stage Rule 12.285 pipeline, not compete with it.

- **Scope gate first:** every matter is tagged Full 12.285 or Limited Discovery (attorney-selected at intake). The portal's discovery checklist generates from this tag — Limited matters see a shorter, attorney-curated list.
- **Category-based checklist:** one section per 12.285 category (income, real property, vehicles, financial accounts, business interests, debts, etc.), each with:
  - A plain-language explainer: what this is, why the court requires it, how to get a copy if they don't have one
  - Upload button (feeds the same OneDrive folder `fmlg-disco-organization` renames into `[Name]_[12.285Category]_[Institution]_[Period]`)
  - Status: Not Started / Uploaded / Reviewed / Flagged Missing
- **Progress tracker:** visual completion bar per category and overall, pulled from the same data the `fmlg-disco-tracker` skill maintains — this should be the same tracker, surfaced, not a second one.
- **Sequencing rule (important — this is what you flagged):** the portal should visibly prioritize the subset of discovery needed to get the Financial Affidavit moving fast — pay stubs, most recent tax return, and the bank accounts the client uses for direct deposit — as a "Start Here" mini-checklist ahead of the full 12.285 list. Everything else in 12.285 continues in parallel/behind it. This lets `fmlg-fa-builder` start on a preliminary FA while the rest of discovery is still coming in, matching how the firm actually works the file today.

### 2.3 Financial Affidavit intake
- A structured intake form (income, expenses, assets, debts) that maps directly to FA line items — this is the client-facing front end for what currently comes in as a Smokeball intake form and feeds `fmlg-fa-builder`.
- Should NOT ask the client to do math the firm's tools already do (e.g., don't ask them to calculate net income — collect the raw numbers, let the FA Builder skill calculate).
- Every field the client submits should be flagged in the internal FA draft as client-reported vs. document-confirmed, exactly like the FA Cross-Check skill already does — the portal is a new input channel into the same QC pipeline, not a shortcut around it.

### 2.4 Deadlines & events
- Pulls from the matter's command center (`fmlg-command-center`) — mediation dates, hearing dates, mandatory disclosure due dates, response deadlines.
- Client-visible subset only: no internal attorney-flag items, no strategy notes. Just: what's coming up, when, and what (if anything) is needed from them.

### 2.5 Document review/approval
- A simple approve/reject/comment flow for documents the firm wants client sign-off on before filing or sending (e.g., a draft MSA, a letter going to OC).
- Distinct from e-signature — this is "does this look right to you," not a signature capture tool. If actual e-signature is needed, that's Adobe Sign, not this portal.

### 2.6 Chat interface
- Start narrow: a message thread per matter, staff-to-client, not a general chatbot. This is a communication log, not an AI assistant talking to the client.
- Every message should be timestamped and exportable — it may need to be part of the file at close-out.

### 2.7 Client's own OneDrive
- "Download to own OneDrive" means generating a shareable/downloadable copy the client can save into their own account — it does not mean giving the client write access to the firm's OneDrive. The firm's OneDrive stays firm-controlled; the client gets copies out, uploads discovery in through a designated intake folder, and never browses the firm's raw folder tree.

---

## 3. Build B in Detail — LAL Coaching Client Portal

### 3.1 Two views, one app
- **Owner/attorney view:** live install tracker (which suites are owned, install status per suite), retainer balance with running draw-down history, session history, upcoming Zoom booking links, resource library filtered to what they own.
- **Firm staff view (their team, if applicable):** same resource library, no retainer/billing visibility unless the attorney grants it.

### 3.2 Retainer balance
This should read the same structure already used in `LAL_COACHING_MASTER_GUIDE.md` and the Feinstein & Mendez contract model: prepaid credit balance, drawn down at session rates ($600/2hr, $350/1hr, $150/30min) and between-session build rates ($350/hr Leisa, $450/hr Henry, in the increments already defined). The portal should show a running ledger, not just a current number — client should be able to see what each draw was for.

### 3.3 Replacing the Tiiny hub
The current Tiiny model (single HTML file, email-restricted, collapsible sections, regenerated after every session) is the right information architecture — client reference links at top, tracker, session notes, retainer balance, catalog link at bottom. Build B should carry that structure over into a real multi-page portal instead of regenerating a static file every session. That also removes the manual regenerate-and-reupload step currently required after every coaching session.

### 3.4 Slack decision
Two options, don't build both at once:
- **Option 1 (faster):** Portal has a "Join our Slack" card that links out to an invite for the client's dedicated channel in `familymatters-ze21660` (or a new client-facing workspace, if separating from FMLG's internal workspace matters). Zero build cost.
- **Option 2 (slower, more integrated):** Native chat inside Lovable, mirrored to/from Slack via API or Zapier. Only worth building once Option 1 proves clients actually want in-portal chat rather than just using Slack directly.

Recommend starting with Option 1 for the pilot.

### 3.5 Test plan
Pilot on 2–3 active coaching clients already in motion (e.g., B&J, Martha Mendez) before rolling to new signings. This gets Henry and the portal real user feedback fast, and lets Leisa validate the retainer-ledger and tracker views against real, messy, in-progress engagements rather than a clean demo case.

---

## 4. Shared Technical Architecture

### 4.1 Lovable + storage — the key constraint
Lovable's built-in `window.storage` API is **text/JSON only, values under 5MB, no file uploads**. That means:
- Actual documents (pleadings, discovery PDFs, bank statements) **cannot live inside Lovable's storage.** They live in OneDrive/SharePoint as they do today.
- Lovable's storage is for **metadata and state**: which links map to which matter, checklist completion status, retainer ledger entries, message log, tracker state.
- The portal is a **front end over the existing SharePoint structure**, connected via the Microsoft 365 connector (SharePoint search/folder tools), not a new document repository.

### 4.2 Per-matter/per-client link mapping
Recommend a simple mapping table (stored in Lovable storage, shared: false per firm/tenant) of the shape:
```
{
  matterId: "...",
  clientEmail: "...",
  discoveryScope: "full" | "limited",
  links: {
    filedPleadings: "onedrive-link",
    opFiledPleadings: "onedrive-link",
    noticesOrders: "onedrive-link",
    clientDiscoveryIntake: "onedrive-link"
  }
}
```
Staff sets these once per matter (probably during `fmlg-matter-folder-setup` or `fmlg-start-case`), the portal reads them to render the client's view.

### 4.3 Auth
Recommend carrying over the Tiiny pattern that's already working: email + verification code, no password. Lower friction than a full account system, and matches what coaching clients are already used to.

### 4.4 Ethics/compliance flag — do not skip this
Any self-service client-facing discovery or document tool touches unauthorized-practice-of-law exposure the moment it does anything beyond passive display — e.g., if the portal ever explains "what documents you need" in a way that could look like legal advice, or if a client-facing chat response could be read as legal guidance. Route this through `fmlg-ethics-workflow` before Build A goes live with real clients, not after. This was already flagged as an open item in the LAL roadmap (self-service portal UPL exposure) — this app is exactly that item made concrete.

---

## 5. Intake Forms Needed

| Form | Purpose | Feeds |
|---|---|---|
| **Matter Portal Setup (staff-facing)** | Sets discovery scope (full/limited), sets the four OneDrive links, sets client email(s) | Link mapping table (4.2) |
| **Client Discovery Intake** | Per-category upload + plain-language explainer | `fmlg-disco-organization`, `fmlg-disco-tracker` |
| **FA Intake Questionnaire (client-facing)** | Structured income/expense/asset/debt collection | `fmlg-fa-builder` |
| **Coaching Client Setup (staff-facing)** | Which suites owned, retainer amount, Slack channel link, Zoom booking links | Build B owner view |
| **Session Log Entry (staff-facing)** | Session date, duration, rate applied, notes | Retainer ledger (3.2) |

The existing `LAL_Coaching_Intake_JotForm.json` structure is a reasonable starting point for the Coaching Client Setup form — adapt rather than rebuild from scratch.

---

## 6. Recommended Build Order

1. **Build B, MVP first.** Owner dashboard (tracker + retainer ledger) + resource library + Zoom links + Slack card. Pilot on 2–3 live clients. This is the smaller, lower-risk build and proves the Lovable + Microsoft 365 connector pattern.
2. **Build A, discovery module only.** The category checklist + upload + progress tracker + "Start Here" FA-priority subset, wired to one real FMLG matter as the pilot.
3. **Build A, link categories.** The four-folder client-facing view (filed pleadings, OP pleadings, notices/orders, client discovery) — this is straightforward once the SharePoint connector pattern from step 2 is proven.
4. **Build A, FA intake + document approval + chat.** These layer on top once the base discovery flow is validated.
5. **Ethics review gate** before any of Build A goes live with a real client outside the pilot.

---

## 7. Open Decisions to Resolve Before Build Starts

Flag these explicitly to Henry before scoping either build — each one changes the architecture:

- **Single-firm tool vs. resellable product.** Is Build A an FMLG-internal tool first, or built from day one as a multi-tenant LAL product (Command Center module)? Multi-tenant changes the data model in Section 4.2 significantly (needs firm-level isolation, not just client-level).
- **Client account model.** Email+code (Tiiny pattern) vs. full account with password reset, etc. Recommend email+code for both builds initially.
- **Slack embedding vs. linking** (Section 3.4) — start with linking, revisit after pilot feedback.
- **Who owns the OneDrive connector auth** — is this the Microsoft 365 connector already available, or does Henry need a separate service-account integration for reliability at scale?
- **What "download to their own OneDrive" actually means technically** — a generated shareable link the client saves themselves, vs. an OAuth flow that pushes a copy into their account. The former is far simpler and is the recommended starting point.

---

## 8. What to Hand the New Claude Project

When starting the new project for this build, include:
- This guide
- `LAL_Coaching_Intake_JotForm.json` (adapt for Coaching Client Setup)
- The FMLG discovery skill chain reference (`LAL_Master_Skill_Suite_Map.html` / `claude_LAL_Suite_Skill_Catalog.html`) — so the new project understands what it's a front end for, not a replacement of
- `LAL_COACHING_MASTER_GUIDE.md` — retainer/session rate logic for Build B
- `LAL_Brand_Identity.pdf` — colors, voice, for the portal's visual design
- A note that Henry is the technical build owner and this document is the shared spec both Leisa and Henry are working from

---

*End of guide. This is a planning document, not a finished spec — Section 7's open decisions should be resolved (even briefly) before the new project starts writing Lovable code.*
