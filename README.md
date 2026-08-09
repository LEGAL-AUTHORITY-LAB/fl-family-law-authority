# Family Matters Law Group — website rebuild

Rebuild of familymatterslawgroup.com. Informed by a full audit of the current
live site; not a template. This repo currently contains the **homepage (v1)**
and the shared design system.

## Brand

- **Colors → service lines** (confirmed): Pink = **Lawyers**, Teal = **Mediators**,
  Orange = **DIY Legal Coaches**, Chartreuse = **Guardians ad Litem**.
- **Type:** Archivo Black (display / wordmark), Inter (body/UI), Playfair Display
  italic (sparing script accent).
- **Voice:** warm but direct — "truth + context." States the honest answer, then
  the nuance. Self-selection over hard-sell.

## Structure

```
index.html              Homepage
assets/css/site.css     Design system + all homepage styles
assets/js/site.js       Header state, mobile nav, hero load-in, scroll reveal
assets/images/          Brand assets (wordmark, chevrons, attorney photography)
```

## Standing rules baked in from the audit

- **One CTA rule:** every service/pathway CTA links to that service's matching
  intake — no generic contact-page fallbacks.
- **One source of truth for pricing:** topic pages link to the flat-fee page,
  never restate numbers.
- **No placeholders live:** mandatory pre-launch content QC pass. Open TODOs are
  tracked in HTML comments (search `TODO(handoff)`), not shown to visitors.
- **Trust signals surfaced:** 4.5★ / 151 reviews, bilingual practice, since 2010.
- **Real photography** replaces stock throughout.

## Proposed sitemap (for the full build)

- **Ways We Help** — Lawyers · Mediators · DIY Legal Coaches · Guardians ad Litem
  (each → its own intake). Sub-pages: Coparenting Coaching, Paralegal Services,
  DIY Divorce Packages, Parenting Coordination, Collaborative Divorce.
- **Topics** (legal-education layer) — Divorce, Custody & Parenting, Child Support,
  Alimony, Paternity, **Adoption (new)**, Injunctions/DV, **LGBTQ+ Family Law**,
  Name Change, Prenup/Postnup. Each uses the "sub-audience / who this is for"
  template.
- **Pricing** — single canonical flat-fee page.
- **Learn** — Blog (194 posts via redirect map; 13 merged articles launch-ready)
  + interlinked Glossary cluster (UCCJEA, Best Interest of the Child, P.E.A.C.E., …)
  + DIY Legal Shop / courses.
- **About / Team / Bios** (Leisa Wintz, Nazarena Hauser — kept wholesale) / Reviews.
- **Current Clients** — gated hub with labeled links.
- **/es** — full Spanish track (interim: links to abogada-familiar.com).

## Handoff TODOs

- Swap service CTAs to the dedicated matter-intake.com deep links.
- Real phone / email / office address in the footer.
- Repoint topic/nav links to internal routes as those pages are built.
- Drop the full team/office photo set into `assets/images/` and wire specific shots.
