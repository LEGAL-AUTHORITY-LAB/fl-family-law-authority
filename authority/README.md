# FL Family Law Authority — Knowledge Base

Canonical sources, templates, and skill definitions for the FMLG / Legal Authority Lab
Florida family-law discovery practice. This is the reference corpus the Client Portal &
Discovery Engine draws on — the skills here are the source of truth for the app's staff
action buttons and its AI-driven document/deadline logic.

## `discovery-suite/` — the FMLG discovery skills

Each folder is a packaged skill (`SKILL.md` + any `references/`). These are the real,
canonical skill definitions; the portal's four staff buttons call these at runtime.

| Skill | Purpose | Portal use |
|---|---|---|
| `discovery-scope-router` | Entry point — assesses case context, recommends which discovery skills to run, in what order, assigned to which staff | Routing / "what's next" |
| `disco-intake-prep` | Pre-discovery document intake: audit, rename, organize incoming docs in SharePoint before any stage runs | Feeds document sync |
| `disco-organization` | Enforces the DISCO folder structure, 12 subfolders, and `[First]_[12.285Category]_[Institution]_[Period]` naming | Feeds document sync |
| `disco-tracker` | Running discovery tracker — what's been produced / still outstanding; lives in the matter's NOTES folder | **Button: Disco Tracker** |
| `discovery-gap` | Case-wide gap analysis across both parties → gap chart + pre-mediation readiness memo | **Button: Discovery Gap** |
| `cert-of-compliance` | Drafts the Rule 12.285 Certificate of Compliance after mandatory disclosure is served | **Button: Cert of Compliance** |
| `advanced-discovery-org` | Discovery strategy + drafting: interrogatories, RFPs, RFAs, subpoenas, deficiency letters, motions to compel (Rules 12.280/285/340/350/351/370/380) | Drafting support; deadline cues |
| `client-financial-intake` | Opens a new financial matter, produces the Stage 2 case summary memo; sets context all downstream skills depend on | Matter setup |

### Reference templates (under `advanced-discovery-org/references/`)
- `rule-12-285-checklist.md` — mandatory disclosure category checklist
- `interrogatories-rfa-template.md`, `rfp-template.md` — discovery request templates
- `deficiency-letter-template.md`, `motion-to-compel-template.md` — enforcement templates
- `rule-12-351-and-response-review.md` — response review guidance

## Non-negotiables baked into these skills
- SharePoint is the source of truth for hired-matter documents.
- Petitioner / Respondent terminology in anything client-facing.
- Attorney sign-off is required before anything drafted is served or filed — the app
  surfaces drafts for review, it does not file.

## Companion planning docs
- `../docs/fmlg-client-portal-master-guide.md` — the consolidated portal/command-center architecture.
