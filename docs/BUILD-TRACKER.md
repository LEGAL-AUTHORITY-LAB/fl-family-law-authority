# FMLG Client Portal & Discovery Engine — Build Tracker

Living status of the build. **App:** Lovable project `2695077c-f038-4ff7-8a8d-981f29965ce8`
(workspace **Family Matters Law Group**). Preview:
https://id-preview--2695077c-f038-4ff7-8a8d-981f29965ce8.lovable.app ·
Editor: https://lovable.dev/projects/2695077c-f038-4ff7-8a8d-981f29965ce8

Legend: ✅ done & tested · 🔨 in progress · ⏳ backlog · ⛔ blocked

---

## ✅ Built & live
| Area | What |
|---|---|
| Shell | Two-sided app (staff command center + client portal), one auth/data spine; client profile is the front door |
| Discovery inbound | Full 12.285 / Simplified checklist, drag-drop, N/A, green-on-submit, auto-save |
| FA-ready | Tier 1/Tier 2; `fa_ready` flips when all Tier 1 staff-cleared (accept or confirmed-N/A); FA-Ready badge + Run FA Builder seam |
| Document portal | 4 SharePoint categories, `client_visible` default-off, approve vs informational, lifecycle logged |
| Chat | Per-matter thread, client role-tagging (never attorneys); **Slack outbound live** |
| Deadlines (manual) | Staff CRUD + client plain-language mirror w/ disclaimer |
| SharePoint sync | Source of truth; connected as **lwintz@fmlgpa.com** (read-only) |
| Bulk import | **78 matters, 75 clients, 537 docs** (26 onboarded + 52 placeholders); idempotent "Import from SharePoint" |
| Discovery recursion + live tracker | Recurses nested disco folders (`SHARED - DISCO FROM CLIENT`); "Refresh tracker from SharePoint"; "Request Discovery" CTA |
| Deadline derivation (AI) | **On-demand** per matter ("Derive deadlines from documents"); reads Notices/Orders, staged proposals for Accept/Dismiss; Tolson verified |
| Case-info extraction | Auto-on-open + "Re-read file": pleadings → Petitioner/Respondent, filing date, case #, county, division, opposing counsel; intake folder → contact/family; header shows Petitioner v. Respondent + filing date; provenance + staff-lock |
| Representation type | From retainer doc → Full/Flat Fee/Limited/DIY badge (staff-editable) |
| Native FA Intake form | Framework (form_templates/assignments/responses) + FA Intake (14 sections, 285 fields), 9 field types, conditional + repeatable groups, autosave draft-then-lock |
| Intake send/track | Staff recommend/send/track; reset stale auto-assignments to draft; client Forms area (sent→viewed→completed) |
| Cases cleanup + Dashboard | Legacy DISCO Cases page removed (routes + 16 orphaned components); clients sorted by last name; Dashboard rebuilt on real schema (stats, upcoming deadlines, discovery queue, activity feed) |
| Staff-name attribution | `profiles.display_name` + resolution (display_name→full_name→email); real staff names on activity feed, chat (staff side), doc share, discovery accept, forms actions, dashboard; editable in Settings; client chat keeps "Your legal team" alias |
| Chat tab + Portal Messages inbox | Chat is its own tab on command center (deep-link `?tab=chat`); top-level `/messages` inbox aggregates all client threads (unread-first, snippet, relative time); `portal_thread_reads` per-staff unread; same `portal_messages` data |
| Client doc delivery + review/comments | Staff "Deliver for review" (attorney sign-off) → client "For your review" section; `document_comments` thread both sides w/ real names; status badge Delivered→Viewed→Commented→Approved; audit columns on `documents` |
| Scannable MD/discovery tracker | `DiscoveryTracker` grouped by 12.285 category; status chip (Complete/Partial/Outstanding/N/A) + produced/expected counts + latest date; collapsed by default; unmatched pooled in "Needs review"; summary strip. Tolson verified |
| Send for e-signature | Settings E-signature (PandaDoc + Adobe Catch-Hook URLs); doc "Send for signature" w/ prefilled signer + attorney sign-off; server-side POST to hook; `signature_requests` + badge (Sent→Viewed→Signed) + manual status; return webhook (auto-status + signed-PDF write-back) still to wire. Tolson verified |
| Transcript → Memo | Documents "Case memos" card; input paste/upload (txt/rtf/docx/pdf/image, server-side extract + OCR); Lovable AI → 9-section FMLG memo + Archie Smokeball list; branded on-screen review (Edit/Preview) + attorney sign-off gate → `pdf-lib` branded PDF → POST to `sharepoint_notes_webhook_url` (download-only fallback); `case_memos` table. Tolson verified |

| Transcript doc-link + Claude Cowork button | (a) "paste doc link" (SharePoint URL) transcript source; (b) per-matter/per-staff Claude button (`matter_claude_projects`): Set up → matter instruction block w/ SharePoint link → paste Cowork URL → Open in Claude. Tolson verified |

| Skill Launcher | `skill-registry.ts` (13 skills, 3 categories); per-matter "Launch a skill" dropdown, matter-type recommend; builds Cowork handoff prompt (shared `matter-instructions.ts`) + inputs (OP disco link etc.) → Copy prompt & open Claude; logs launch. No Gemini/GPT. Subsumes Draft (#18) + Advanced Discovery (#20). Tolson verified |

| OCR off Gemini (hybrid) | `document-text.server.ts`: native text → unpdf PDF text layer → tesseract WASM → "needs Claude" signal; no vision model, no `LOVABLE_API_KEY`. Verified network-disabled |
| AI migration COMPLETE | `claude-handoff.ts`; memo/case-info/deadline all Cowork-handoff; deleted case-info/intake/retainer/deadline `.server` + `ai-gateway.server` + legacy `.functions`; removed FloatingChat + `/api/chat`. **Zero non-Claude model calls over client data**; `LOVABLE_API_KEY` only for SharePoint/Slack connectors |

## 🔨 Planned — Leads module (new)
- **Leads section (#33)** — website lead form → lands in app → notify intake staff → manual conflict check / contact / decide (free consult / paid consult / reject) via check-off buttons → on consult scheduled, create a SharePoint lead file (Zapier) → notes/transcript → memo (reuse Transcript→Memo). Manual scheduling + payment link, just check-off toggles. Ingestion mechanism + leads SharePoint location TBD.

## ⏳ Backlog (prioritized)
1. **Intake → SharePoint save** — on submit, render completed form to PDF and upload to the matter `Intake` folder. Dep: Zapier SharePoint write.
5. **Four staff buttons / Advanced Discovery page** — dedicated OP-side surface: paste OP discovery SharePoint link → OP discovery-gap (`fmlg-discovery-gap`), income assessment (`fmlg-income-assessor` + `fmlg-fa-crosscheck`), CS/alimony/ED (`fmlg-cs-worksheet`/`fmlg-alimony-assessor`/`fmlg-ed-chart`), advanced-discovery drafting (`fmlg-advanced-discovery` + templates). Also Disco Tracker / Cert of Compliance buttons. All drafts → attorney review.
6. **Staff Draft button** — pick doc type (freeform or dropdown by case type) → AI draft from templates/skills → attorney review.
7. **Transcript → Memo button** — drop transcript → `fmlg-case-memo` → memo saved to matter NOTES folder. Dep: Zapier SharePoint write.
8. **Close File** — case-closing skill (⛔ file re-upload pending) + Finalize Closing = move matter folder OPEN → CLOSED FILES. Dep: Zapier SharePoint write (move).
9. **Slack inbound** — Slack replies → portal. Dep: custom Slack app + `SLACK_SIGNING_SECRET` + Events URL `…/api/public/slack/events`.
10. **Templates merge repoint** — Templates page merge dropdown still queries legacy `cases`; repoint to `matters`.
11. **Client-side OneDrive push** — only if wanted beyond simple download.

## Dependencies & mechanisms
- **AI (ETHICS-CRITICAL, migrating):** All FMLG skills and any AI reasoning over client data MUST run through **Claude on the firm's paid, restricted (no-training / zero-retention) plan** — **not** Lovable's built-in Gemini/GPT. Mechanism = **Claude Cowork handoff**: the app prepares inputs + a ready-to-paste prompt for the staff member's connected Cowork project (per-matter Claude button); the skill runs in Cowork; output returns to the app (paste-back or SharePoint sync) for attorney sign-off + save. ⚠️ Features currently still on Gemini/GPT and pending migration: case-info extraction, deadline derivation, case-memo generation, and vision-OCR. See "AI migration" backlog.
- **SharePoint reads:** Lovable Microsoft SharePoint connector (read-only, lwintz@fmlgpa.com).
- **SharePoint writes (saves/moves):** via **Zapier** Microsoft SharePoint actions (app → Zapier). No connector scope change.
- **Slack:** connected; outbound works via connector; inbound needs a custom Slack app + signing secret.
- **Smokeball:** connected via Zapier but not needed — deadlines come from filed SharePoint docs + manual entry.

## Authority KB (in this repo, `authority/`)
- `discovery-suite/`: scope-router, disco-intake-prep, disco-organization, **disco-tracker**, **discovery-gap**, **cert-of-compliance**, **advanced-discovery** (+ templates: interrogatories/RFA, RFP, deficiency letter, motion to compel, rule 12.285 checklist, rule 12.351), client-financial-intake
- `skills/case-memo/` — branded memo generator
- `skills/financial-suite/`: alimony-assessor, cs-worksheet, ed-chart, fa-crosscheck, income-assessor
- `forms/fa-intake-spec.md` — FA Intake field spec

## Open decisions
- Approval legal weight (informal vs SignNow/Adobe) · chat transcript export to Correspondence/ · four-button runtime (native prompts vs true skill calls).

## Non-negotiables
- SharePoint = source of truth for hired-matter docs. Petitioner/Respondent terminology client-facing. Nothing shows "filed" unless in a filed folder / file-stamped. Attorney sign-off before anything drafted is sent or filed. Portal ≠ substitute for attorney-client relationship or Slack internal comms.

## Key IDs
- SharePoint MATTERS - OPEN: site `49e98e9a-2a43-4729-9db4-2e479d1b4e49`, drive `b!mo7pSUMqKUedtC5HnRtOSe2abk1wPlVIoz9Qtbkr1gdRe9M_SWOCTp1yoL5thBbK`, folder item `01BXX2I4GYAF5AZP23CJGLRCSKMWFPELLV`
- CLOSED FILES: `d=wbce00ba3758d407e82d3642bfb60f5ec`
- LEADS folder: `https://slgpa2013.sharepoint.com/:f:/s/FAMILYMATTERSLAWGROUPMATTERS/IgCzkmF33hEDSK6FoY9blx_OAZPCj2Ji-sOPaJhnqByiXgY` (per-lead files created here via Zapier)
- Tolson test matter: `Tolson, Patricia - Pre Decree (401800)`; Slack channel `#matter-tolson-patricia` (`C0BP8GH9PV3`)
