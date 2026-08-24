# FMLG Portals — Build & Data-Load Log
**Companion to:** `client-portal-discovery-guide.md`
**Maintained by:** LAL Ops (Claude) for Leisa Wintz

> **Internal — confidential.** Excluded from the public GitHub Pages deploy
> (`docs/` is git-ignored from the site build). Contains app URLs, real client
> counts, and data-quality flags. Do not move into the web-served tree.

---

## The two live apps (FMLG Lovable workspace)

| App | Purpose | URL | Visibility |
|---|---|---|---|
| **FMLG Command Center** (`case-command-center-42`) | Internal staff case-management — matters, deadlines, discovery tracking, SharePoint/Slack | editor: lovable.dev/projects/2e66e743-d5f9-4266-b656-3a90e5ac3762 | private, not published |
| **FMLG Client Connect** (`fmlg-case-compass`) | Client-facing litigation portal — retainer→close lifecycle, discovery uploads, docs, invoices, deadlines | https://fmlg-case-compass.lovable.app | project set private; **deployment still published (public URL)** — see Open Items |

*(A third app, "Florida Family Navigator" / `florida-diy-legal`, is the public DIY self-help site — untouched by this work.)*

---

## Data load — August 23 reconciliation set (loaded 2026-08-24)

Source: three files Leisa produced from the SharePoint cleanup — Master Calendar
(95 events / 37 open matters), Master Discovery Tracker (19 requests / 18
matters, full Rule 12.285 checklists), and the SharePoint Reconciliation
Checklist (134 matter rows w/ folder URLs). Client emails/phones/opposing-party/
county were harvested from each matter's SharePoint intake form via the
Microsoft 365 connector.

### Command Center (internal) — all verified by SQL
- **83 matters** (was 78; added 5 active matters that were missing: Flora,
  Gutierrez, Morrill, Paul, Thompson-James).
- **51 real case refs** populated (`case_number` was empty before).
- **91 calendar events** (deadlines / hearings / mediations) — was 0.
- **251 discovery items** across 17 matters, with per-item 12.285 status
  (Provided / Outstanding / Rejected / N/A / Pending Review), dates, file counts,
  and the mis-filing notes from the tracker — was 3.
- **46 client emails, 42 opposing parties, 32 counties, + phones** backfilled.

### Client Connect (client-facing) — private data, RLS-protected
- **49 active litigation matters** loaded (52 total incl. 3 demo), each with real
  client email (the login key), matter type, `stage = active`, and case number.
- **46 real emails** from intake forms; **3 placeholders** for matters with no
  email on file — replace before inviting these clients:
  - Calbo, Robert (2024-5003) — no SharePoint folder found
  - Lyles, Erica (2026-1341) — intake file unreadable (Graph 400); cell on file
  - Montero, Michael (2025-0724) — Smokeball record had no email
- **Excluded as firm/internal** (not real client matters): Mendez, Diveana
  (2024-0310); Serrano, Angelica (2025-0898, empty folder).
- Auth = invite-only passwordless magic link; RLS confirmed: a client can read
  only their own matter (`client_email = login`), staff see all.

---

## Data-quality flags surfaced (for firm follow-up)

- **Duplicate matter rows in Command Center:** "Bernardin, Anne-Marie" **and**
  "Bernardin, Annemarie"; "DeMeyere, Natasha" ×2; **"Gamarra, Sergio" ×3** (no
  refs). Because Gamarra has 3 identical rows, its calendar events + MD checklist
  were **not** auto-attached — dedupe and tell us which is 2026-1281 (OOP) vs
  2026-1360.
- **Case-number mismatches:** Bernardin folder ref is 2026-1278 (not 1282);
  Lemes renamed from 2026-1287 → 2026-3000. Confirm the canonical refs.
- **Mis-filed discovery** (preserved in item notes): Chovert loan-applications
  uploaded as credit-card statements; Abbott "premarital agreement" is actually
  custody filings; Calbo brokerage marked N/A but has 9 files; Bathelemy pay
  stubs filed as a W-2.
- **Smokeball data anomaly:** Mora (2025-1026) opposing party slot duplicates the
  client's own contact.
- **~76 reconciliation rows not loaded** — almost all GAL matters + mediation-only
  entries not in the Command Center's scope. Say if you want GAL matters added.

---

## Open items

1. **Decide on the Client Connect public deployment.** The project is private but
   the deployed site (`fmlg-case-compass.lovable.app`) is still published/public.
   It only exposes a marketing landing + invite-only login (data is RLS-locked),
   but if you'd rather it not be reachable at all until go-live, unpublish it from
   the Lovable editor (there's no API to unpublish).
2. **Fill the 3 placeholder emails** (Calbo, Lyles, Montero) before inviting them.
3. **Discovery into Client Connect** — the client-facing 12.285 checklists aren't
   loaded into Client Connect yet (they're fully in Command Center). Next step if
   you want clients to see their own discovery status.
4. **SharePoint 4-category document links** per matter (Filed / OP / Notices /
   Client Discovery) — not yet mapped into either app; needs the subfolder URLs.
5. **Dedupe** the Bernardin / DeMeyere / Gamarra rows, then attach Gamarra's held
   events/discovery.
