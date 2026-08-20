"""Shared site-wide shell edits: add 'Latest' nav tab + Learn-dropdown entry + footer socials.
Idempotent — safe to run twice (checks before inserting)."""

NAV_ANCHOR = '<a class="nav-lang" href="/es/" hreflang="es" lang="es">ES</a>'
NAV_INSERT = '<a href="/latest/">Latest</a>\n      ' + NAV_ANCHOR

LEARN_ANCHOR = '<a href="/blog/">Blog &amp; Guides</a>\n          <a href="/glossary/">Legal Glossary</a>'
LEARN_INSERT = LEARN_ANCHOR + '\n          <a href="/latest/">Latest from FMLG</a>'

FOOTER_ANCHOR = '<img class="footer-logo" src="https://familymatterslawgrouplaw.wpcomstaging.com/wp-content/uploads/2026/08/wordmark-white.png" alt="Family Matters Law Group">'
SOCIAL = ('<div style="display:flex;gap:10px;margin:14px 0 4px">'
 '<a href="https://www.youtube.com/@Familymatterslaw" target="_blank" rel="noopener" aria-label="Family Matters Law Group on YouTube" style="display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;border:1px solid var(--line-on-dark);color:rgba(251,250,247,.85)">'
 '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6-6.2 3.6z"/></svg></a>'
 '<a href="https://www.instagram.com/familymatterslawgroup/" target="_blank" rel="noopener" aria-label="Family Matters Law Group on Instagram" style="display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;border:1px solid var(--line-on-dark);color:rgba(251,250,247,.85)">'
 '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2c-.1-1.3-.1-1.7-.1-4.9s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4 1.3-.1 1.7-.1 4.9-.1zm0 1.8c-3.1 0-3.5 0-4.8.1-1.1.1-1.7.2-2.1.4-.5.2-.9.4-1.3.8-.4.4-.6.8-.8 1.3-.2.4-.3 1-.4 2.1-.1 1.2-.1 1.6-.1 4.8s0 3.5.1 4.8c.1 1.1.2 1.7.4 2.1.2.5.4.9.8 1.3.4.4.8.6 1.3.8.4.2 1 .3 2.1.4 1.3.1 1.7.1 4.8.1s3.5 0 4.8-.1c1.1-.1 1.7-.2 2.1-.4.5-.2.9-.4 1.3-.8.4-.4.6-.8.8-1.3.2-.4.3-1 .4-2.1.1-1.3.1-1.7.1-4.8s0-3.5-.1-4.8c-.1-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.3-.4-.4-.8-.6-1.3-.8-.4-.2-1-.3-2.1-.4-1.3-.1-1.7-.1-4.8-.1zm0 3.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8zm0 8.1a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4zm6.3-8.3a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0z"/></svg></a></div>')
FOOTER_INSERT = FOOTER_ANCHOR + '\n      ' + SOCIAL


def apply(text):
    # 1) top-level Latest tab
    if '<a href="/latest/">Latest</a>' not in text and NAV_ANCHOR in text:
        text = text.replace(NAV_ANCHOR, NAV_INSERT, 1)
    # 2) Learn dropdown entry
    if '<a href="/latest/">Latest from FMLG</a>' not in text and LEARN_ANCHOR in text:
        text = text.replace(LEARN_ANCHOR, LEARN_INSERT, 1)
    # 3) footer socials
    if 'aria-label="Family Matters Law Group on YouTube"' not in text and FOOTER_ANCHOR in text:
        text = text.replace(FOOTER_ANCHOR, FOOTER_INSERT, 1)
    return text
