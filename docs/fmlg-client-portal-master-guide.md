# FMLG Client Portal & Discovery Engine — Canonical Master Guide
**Consolidated:** 08-09-2026 · **Owner:** Leisa Wintz (FMLG / Legal Authority Lab)
**Status:** Founding reference for the Lovable build (Family Matters Law Group workspace)

---

## 0. What this document is, and what it merges

This is the **single source of truth** for the FMLG Client Portal & Discovery Engine. It consolidates the two planning passes that were drafted in parallel (in two separate Claude Code sessions) so there is one reference to hand the build — not two:

- **Source A — the 08-09 master guide.** Deep on storage architecture (SharePoint vs. OneDrive), the FA two-tier sequencing, the integration map, and the relationship to the existing FMLG skills.
- **Source B — the "Architecture Recap" artifact.** Stronger on the *organizing model*: the **client profile as the front door** on both sides, and the strategic direction that the staff side **eventually replaces Smokeball** rather than merely mirroring it.

Where the two differed, this document reconciles them explicitly (see §13, "What was reconciled"). The headline reconciliation — and the design change Leisa asked for on 08-09 — is that **the staff command center is pushed toward the portal concept**: it is not a read-only window onto other systems, it is a first-class application whose own data model is the eventual system of record.

**This is not a competing app.** It is one application, two faces, one shared spine, built by wiring into the infrastructure the firm already runs (SharePoint, Slack, Smokeball) and, over time, absorbing that infrastructure's system-of-record role.

Companion specs assumed as background: `fmlg-pipefile-replacement-build-instructions-2026-08-08.md`, `fmlg-discovery-portal-master-outline-for-henry-2026-08-08.md`, `FMLG_Command_Center_Build_Spec.md`, the Lovable **DISCO** app already in progress, and the Jotform discovery collector.

---

## 1. The organizing model: two faces, one spine, profile as front door

One application. One auth system, one client identity, one matter record — **the shared spine**. The client side and the staff side are two views onto that spine, and on **both** sides the **client profile is the front door**.

| | **Client side** (one login per client) | **Staff side** (launched from the profile) |
|---|---|---|
| Documents | Curated, grouped by category — never a raw file browse | The client's real SharePoint matter folder, inline |
| Communication | Chat with the firm | The same chat thread + the client's Slack channel, linked inline |
| Deadlines | Plain-language, read-only ("Your response is due by [date]") | Full deadline/event view |
| Discovery | FA-first checklist; Full or Simplified per matter | Discovery status, FA-ready signal, the four action buttons |

**Practical implication:** build **one data layer** and **two front ends** reading/writing against it — not two apps with a sync problem. The old "open a matter (paste a destination folder)" flow from the discovery-portal outline collapses into "**open the client profile**" — the SharePoint folder is already known from the profile.

---

## 2. Guiding principle — and the command-center → portal shift

**Integrate into the staff side; don't rebuild it — but architect so the portal can become the system of record.**

Every capability is built by wiring the portal into a system the firm already runs, surfaced from the client profile. Staff keep working where they already live (Slack, SharePoint). The payoff is not *a new inbox to learn* — it's *the client is now wired into our existing tools, and the profile is the front door.*

**The shift Leisa asked for (08-09):** the staff command center is meant to **eventually replace Smokeball**, not merely mirror it. This is roadmap, not v1 — but it changes how v1 is built:

- **For v1:** SharePoint stays source of truth for documents; the deadline view is a **read-only mirror** of Smokeball/Outlook. These hold.
- **But do not architect as if Smokeball is permanent.** Model **matters, deadlines, and events as first-class portal entities from day one**, with Smokeball/Outlook as an **import/sync source** — not throwaway pass-through views. That is the only way the portal can take over the system-of-record role later without a rebuild.

This is the concrete meaning of "improve the command center toward the portal concept": the command center owns its own data model; external systems feed it; over time it becomes primary.

**Relationship to the `fmlg-command-center` skill:** that skill is the source-of-truth *writer* (it logs stage completions, deadlines, and attorney flags from any FMLG skill's output). The portal's staff view is the *reader/owner* — a live UI over the same data. They must converge on **one shared data layer**, not run as two separately-maintained trackers (see open decision 6).

---

## 3. The capabilities

### 3.1 Document portal — outbound (firm → client)
- Staff mark SharePoint files client-visible in **four categories that map 1:1 to existing folders**: `Filed Documents - Client`, `Filed Documents - OP`, `Notices`, `Orders/Agreements/Reports`.
- Client sees them **grouped by category** — never the underlying folder structure, names, or anything outside those four categories.
- Per-document flag: **`requires approval`** vs. **`informational copy`**. Approval logs a timestamp and an explicit "I approve." (Legal weight is open decision 2.)
- Every push and every approval **logs back to the matter's activity center** (the shared data layer), so staff see "client has seen/downloaded the entered order" in one place.
- **Download for records:** v1 uses the simple **client-initiated "Save to OneDrive"** path (a normal download; the client's own browser session hands it off) — **not** a cross-tenant OAuth push into the client's personal account (open decision 1).

### 3.2 Chat — two-way (client ⇄ firm)
- **Per-client Slack channel.** Each client gets their own; the profile links to it. (This replaces the earlier "route everything to `#case-management`" idea.)
- **One thread, mirrored both ways.** A client message appears in their Slack channel *and* on the portal screen; a staff reply — sent from Slack *or* the portal inbox — flows back onto the client's portal screen.
- **Tagging is client-facing roles only — never attorneys.** The tag list is a curated, staff-defined set (paralegals, legal assistants, case managers) mapped to Slack @mentions. Clients cannot ping a lawyer directly.
- Asynchronous model with a stated SLA — not live chat. Set that expectation in the UI (six staff, one shared Slack workflow).
- **Recordkeeping is open (decision 3):** whether transcripts export to `Correspondence/` on a cadence, or the portal log satisfies file-completeness.

### 3.3 Deadline & event tracking
- **v1:** read-only mirror of Smokeball/Outlook, plain-language ("Your response is due by [date]," not a raw docket title). A lightweight mapping layer turns internal task/category names into client-safe labels.
- **Architected for the roadmap:** deadlines/events/matter data are first-class portal entities from day one, Smokeball as sync source (per §2).
- **Blocker (decision 5):** whether "Deadlines"/"Discovery" are real Smokeball modules or just Task Category tags is unconfirmed — resolve before building the feed.
- The portal view is a convenience, **never the client's only notice** of a deadline; court deadlines still go through the attorney/correspondence channel.

### 3.4 Discovery education + collection — inbound (client → firm)
- Checklist UX from the Pipefile-replacement spec, unchanged: drag-drop, not-applicable option, green-on-submit, auto-save. Uploads land in `MD or Discovery - Client/`.
- **Matter-level, staff-set flag:** `Full 12.285` vs. `Simplified/Limited` decides which checklist the client sees. This is not a client choice.
- Simplified is triggered by **case complexity** (no business, no real property, no virtual currency, no marital agreements) — **not** by dissolution type. Maps to the "Simplified" track in the DISCO app's seven document tracks.
- Education content explains **what mandatory disclosure is and why**, in plain language.

### 3.5 Financial affidavit — sequenced two-tier (inbound)
The FA has to move fast and can't wait for full disclosure, so intake is a deliberate two-tier order, not a flat checklist.

- **Tier 1 — FA-critical basics (collected first, fastest turnaround):** most recent pay stub(s), 2–3 months of primary bank statements, most recent tax return, and any income-characterization docs (non-W2). Foregrounded on first login — *"let's get your financial affidavit moving."*
- **Tier 2 — full Rule 12.285 (or the limited list):** everything else — retirement/investment, life insurance, business records, debt statements, etc. Visually secondary (collapsed/grayed) until Tier 1 shows submitted; then collects at the client's own pace.
- **FA-ready signal:** once Tier 1 is **staff-approved**, the app raises an internal **"FA-ready"** flag on the profile → staff trigger `fmlg-fa-builder`, independent of where the rest of discovery stands. `fmlg-fa-preliminary` / `fmlg-fa-crosscheck` follow.
- Education explains *why* the split exists: *"these first few documents let us file your financial affidavit quickly; everything else we gather as it comes in."*

---

## 4. Storage architecture — SharePoint (firm) vs. OneDrive (client)

**Firm side.** The entire staff view and the categorized outbound links are **SharePoint**, via `fmlg-sp-connector` — no new storage layer. The client-facing side is a **curated view** of that same folder: staff designate which files/folders in the four categories are client-visible; the portal surfaces them via Microsoft Graph share links (or a per-file "publish to portal" toggle) scoped to the client's portal session. The client never gets a SharePoint account or sees the underlying structure.

**Client side ("download to their own OneDrive").** Two paths, decision required (open decision 1):
- **(a) Client-initiated "Save to OneDrive"** — a normal download button; if the client is signed into their own Microsoft account, standard OneDrive "Save a copy" handles it. No firm-side integration with the client's personal cloud. **Recommended for v1.**
- **(b) True API push into the client's OneDrive** — requires the client to grant OAuth consent, firm-side token storage per client, and handling for clients with no Microsoft/OneDrive (Gmail/Apple users are common). Its own project; revisit only if clients ask for automatic sync.

---

## 5. Integration map

| Capability | Plugs into |
|---|---|
| Staff command center (filings, deadlines, discovery status) | `fmlg-command-center` skill + `fmlg-sp-connector` (shared data layer) |
| Document portal (outbound) | `fmlg-sp-connector` → the four SharePoint categories |
| Client discovery uploads (inbound) | `MD or Discovery - Client/`, `fmlg-disco-intake-prep`, `fmlg-disco-tracker` |
| Discovery education + collection | Pipefile-replacement spec + Jotform collector + DISCO seven-track model |
| FA sequencing | `fmlg-fa-builder`, `fmlg-fa-preliminary`, `fmlg-fa-crosscheck` |
| Chat | Per-client Slack channel (two-way bridge) |
| Deadlines | Smokeball / Outlook — v1 mirror; target: portal owns it |
| Staff four buttons (Disco Tracker, Gap, Cert of Compliance, FA Builder) | `fmlg-discovery-portal-master-outline-for-henry` — inside this same staff surface |
| Client SharePoint folder view | `fmlg-sp-connector`, surfaced from the profile |

---

## 6. Non-negotiables (carried forward, unchanged)

- SharePoint stays source of truth for hired-matter documents **in v1**. Nothing creates a second document source of truth.
- All SharePoint I/O routes through `fmlg-sp-connector` — no direct MCP calls from the portal.
- Petitioner / Respondent terminology in anything client-facing that references pleadings.
- Nothing shows as "filed" unless it's in a filed-documents folder or file-stamped.
- Attorney sign-off is required before anything the four buttons draft is sent or filed. The portal is a collection/communication/tracking layer, not a filing mechanism.
- The portal does not substitute for the attorney-client relationship or for Slack as internal comms.

---

## 7. Open decisions before the build

1. **Client-side OneDrive** — simple client-initiated download (*recommended v1*) vs. true OAuth push into the client's personal account.
2. **Approval legal weight** — informal "I have reviewed, no objection" vs. routing through SignNow / Adobe Sign for a real signature (changes whether e-sign is wired into the portal).
3. **Chat recordkeeping** — export transcripts to `Correspondence/` on a cadence, or does the portal log satisfy file-completeness? (Recordkeeping / ethics.)
4. **Four-button runtime** — call the real Claude skills at runtime vs. reimplement their logic natively (cost, latency, drift risk).
5. **Smokeball module confirmation** — are "Deadlines"/"Discovery" real modules or Task Category tags? Needed before the deadline mirror.
6. **Smokeball-replacement scope + command-center convergence** *(new 08-09)* — confirm (a) the "eventually replace Smokeball" ambition is real and in-scope (it raises the v1 data-model bar per §2), and (b) that the `fmlg-command-center` skill and this app's staff view converge on **one** shared data layer rather than two trackers.

None of these block starting the build — the shell, discovery checklist, document portal, and chat can all be built while they resolve.

---

## 8. Build order

1. **Client identity + portal shell** — the profile as the hub; first-class matter/deadline/event entities from day one.
2. **Discovery inbound** — Pipefile parity, unchanged.
3. **FA Tier 1 / Tier 2 flagging + FA-ready signal.**
4. **Document portal outbound** — publish-to-portal toggle; approve vs. download-only.
5. **Chat** — two-way Slack bridge + portal inbox, per-client channel, no-attorney tagging.
6. **Deadline mirror** — after the Smokeball module question (decision 5) resolves.
7. **Four staff action buttons** — after the runtime decision (decision 4); inside the staff command center.
8. **Client-side OneDrive push** — only if option (b) is confirmed worth building.

---

## 9. What was reconciled (Source A ↔ Source B)

| Topic | Source A (master guide) | Source B (recap) | Reconciled position |
|---|---|---|---|
| Command center | Live *reader* / window onto SharePoint; don't duplicate | First-class entities; portal eventually replaces Smokeball | **v1 mirrors, but the data model is first-class from day one** so the portal can become system of record without a rebuild (§2) |
| Organizing unit | "Open a matter" (+ destination folder) | **Client profile as front door** | Profile is the front door; the folder is known from the profile |
| Chat routing | Slack `#case-management` | **Per-client Slack channel** + two-way bridge | Per-client channel; two-way mirror; tagging client-facing roles only, never attorneys |
| Open decisions | 6 (incl. command-center convergence) | 6 (incl. Smokeball-replacement scope) | Merged into a single superset (§7); items combined as decision 6 |

---

## 10. Housekeeping note (repo placement)

This document lives in the `fl-family-law-authority` repo, which is also currently holding the **FMLG website rebuild**. Those are two different concerns (the authority/knowledge base + portal planning vs. the marketing site). Recommend, separately, deciding whether the website rebuild should move to its own repo so this repo is cleanly the FL Family Law Authority knowledge base + build specs. Not urgent; flagged so it isn't rediscovered later.
