# FMLG WordPress build — staged video/social update

This folder holds the finished, ready-to-publish page content for the
Family Matters Law Group WordPress.com site (**site ID `256638014`**,
staging `familymatterslawgrouplaw.wpcomstaging.com`).

The site's 66 pages are already **live**. The files here carry the
**video + social enhancement layer** that still needs to be pushed:

- "Latest" tab added to the header nav (and to the Learn dropdown)
- YouTube + Instagram icons added to the footer of every page
- Topic-matched YouTube **playlists embedded** on 18 service/topic pages
- The `/latest/` hub page fully built (featured video + podcast player +
  all **20 public** playlists as cards; the private **GAL TRAINING**
  playlist is intentionally excluded)

## Contents

- `final/<slug>.html` — the complete page body for each slug. Each file is
  Gutenberg `wp:html` blocks with the full inline stylesheet baked in
  (this site can't use shared CSS, so every page self-contains its styles).
- `repush_plan.json` — the push manifest: one entry per page with
  `slug`, `id` (the existing WordPress page ID), `title`, `action`
  (`"update"`), and `file`.
- `repush1.json`..`repush6.json` — the same manifest split into 6 batches.
- `scripts/` — the generators (`build_socialvideo.py`, `gen_final.py`,
  `shell_edits.py`, `fix_gal.py`) and the split CSS (`css_p1.txt`,
  `css_p2.txt`) used to produce `final/`.

## How to finish the push (needs the WordPress.com MCP connector)

For each entry in `repush_plan.json`, call the WordPress content-authoring
tool:

```
operation: pages.update
wpcom_site: "256638014"
params: { id: <entry.id>, title: <entry.title>, slug: <entry.slug>,
          status: "publish", content: <raw text of final/<slug>.html>,
          user_confirmed: true }
```

Update **by id** (never create — creating would make duplicate `-2` slugs).
Content must be the exact raw file text.

## Homepage (page id 107)

The homepage already has the video strip. It still needs the same two shell
edits (Latest nav tab + footer socials). Apply `scripts/shell_edits.py`'s
three replacements to its current content, or re-run the edit there.
