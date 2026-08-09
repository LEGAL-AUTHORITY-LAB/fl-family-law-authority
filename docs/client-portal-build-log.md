# Client Portal — Build Log & Handoff
**Companion to:** `client-portal-discovery-guide.md`
**Built by:** LAL Ops (Claude) for Leisa Wintz — **Date:** August 9, 2026

> **Internal — confidential.** Excluded from the public GitHub Pages deploy
> (lives under `docs/`). Contains demo logins and infrastructure notes.

---

## What was built

A working Lovable app — **"Client Compass"** (FMLG / Legal Authority Lab client
portal) — implementing **both** builds from the master guide in **one project**,
per Section 1's "two builds, one project" recommendation.

- **Workspace:** Family Matters Law Group (Lovable, Pro)
- **Editor:** https://lovable.dev/projects/5e95deef-7767-468e-882f-a0296cda8531
- **Live app:** https://fmlg-client-portal.lovable.app
- **Preview:** https://id-preview--5e95deef-7767-468e-882f-a0296cda8531.lovable.app
- **Stack:** TanStack Start (TS) + Tailwind + shadcn/ui, **Lovable Cloud
  (Supabase/Postgres)** backend with **Row-Level Security**.

### Demo logins (passwordless — enter email, then use the on-screen code)
| Role | Email |
|---|---|
| Staff / admin | `leisa@fmlg.example` (also `henry@fmlg.example`) |
| Coaching client | `owner@riveracole.example`, `owner@delgadolaw.example`, `owner@northbendfamily.example` |
| Litigation client | `owner@harper.example` (matter: *Harper v. Harper*, Full 12.285) |

The app is in **DEMO MODE**: the 6-digit code is shown on screen. Adding a
`RESEND_API_KEY` secret flips it to real emailed codes (see Open Items).

---

## Feature coverage vs. the guide

**Shared architecture (§4)** — ✅
- Passwordless email + 6-digit code auth; staff-managed allowlist (§4.3).
- Metadata-only data layer: documents are labeled external SharePoint/OneDrive
  links, never uploaded binaries (§4.1). Per-matter/per-client link mapping (§4.2).
- Row-Level Security: each client sees only their own record; staff see all.

**Build B — Coaching Portal (§3)** — ✅
- Staff: manage clients, suites + install status, session-log form that
  draws down the retainer at the guide's rates ($600/2hr, $350/1hr, $150/30min;
  build $350/hr Leisa, $450/hr Henry), plus top-up entries.
- Client: install tracker (per-suite + overall bars), running retainer **ledger**
  (§3.2), session history, suite-filtered resource library, Zoom "Book a session"
  card, "Join our Slack" card (Option 1 link-out per §3.4).

**Build A — Litigation Portal (§2)** — ✅
- Matter setup: scope gate Full 12.285 vs Limited (§2.2), four external link
  mappings (Filed Pleadings → *Filed Documents* subfolder, OP Filed, Notices &
  Orders, Client Discovery Intake) (§2.1).
- Discovery module: category checklist across the 12.285 categories with
  plain-language explainers, status (Not Started/Uploaded/Reviewed/Flagged
  Missing), per-category + overall progress bars, and the **"Start Here"**
  FA-priority subset up top (§2.2 sequencing rule).
- Upload flow respects the metadata-only rule: routes the client to the firm's
  OneDrive intake folder and tracks status only (§2.7).
- The four read-only link categories with the filing-status rule surfaced
  ("filed = actually in the Filed Documents folder") (§2.1).
- FA intake questionnaire — raw numbers only, no client-side math; every field
  flagged **client-reported vs document-confirmed** for the firm's QC (§2.3).
- Deadlines & events with a per-event **client-visible** toggle (§2.4).
- Document review/approval — Approve / Request Changes / Comment, explicitly
  **not** e-signature (§2.5).
- Per-matter staff-to-client message thread, timestamped + exportable (§2.6).

**Ethics / UPL pass (§4.4)** — ✅ (first-pass guardrails, not a substitute for
the formal review — see Open Items)
- Persistent "not legal advice" disclaimer in every client view.
- One-time "How this portal works" acknowledgement modal per user.
- Discovery/FA copy kept descriptive/procedural, not advice-giving.

---

## Open items before real-client use (from guide §6 & §7)

1. **Ethics review gate (§6.5, §4.4).** Route through `fmlg-ethics-workflow`
   before Build A goes live with any real client outside the pilot. The in-app
   disclaimers are a starting point, not the sign-off.
2. **Email delivery.** Add `RESEND_API_KEY` in Lovable to switch codes from
   on-screen demo to real email.
3. **Microsoft 365 / SharePoint connector.** Links are staff-pasted today; wire
   the M365 connector to auto-populate the four link categories and (later) real
   uploads (§7 "who owns the OneDrive connector auth").
4. **Single-firm vs multi-tenant (§7).** Built single-firm first. Multi-tenant
   (LAL resell / Command Center module) needs firm-level isolation added to the
   data model — decide with Henry before that step.
5. **Pilot (§3.5, §6).** Test Build B on 2–3 live coaching clients and Build A on
   one real FMLG matter before wider rollout.

## Build turns (for reference)
1. Shell + brand + passwordless auth + full Build B coaching portal (seeded).
2. Migrated localStorage → Lovable Cloud (Postgres + RLS + real auth).
3. Build A: litigation matters, discovery module, four link categories.
4. Build A: FA intake, deadlines, document approval, chat + UPL/ethics pass.
