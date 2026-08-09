#!/usr/bin/env python3
"""
Family Matters Law Group — static site generator.

Renders every page from a shared header/footer so navigation and chrome stay
consistent and all internal links resolve. Pages are written as folder/index.html
for clean URLs; asset and nav links use a per-page relative `root` prefix so the
site is portable (works via file://, GitHub Pages, or the root domain).

Run:  python3 build.py
"""
import os, re, html

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BLOG_SRC = os.path.join(ROOT_DIR, "content", "blog-src")

# ---- External CTA targets: the current live site's intake links -------------
# (Per direction "use links on current site" until dedicated matter-intake.com
#  deep links are supplied.)
CUR = "https://www.familymatterslawgroup.com"
SPANISH = "https://www.abogada-familiar.com"
CTA = {
    "get_started": CUR + "/get-started",
    "lawyers":     CUR + "/legal-representation",
    "mediators":   CUR + "/mediation",
    "coaches":     CUR + "/diy-legal-individualized-coaching",
    "gal":         CUR + "/guardian-ad-litem",
    "reviews_ext": CUR + "/recommendations",
}

SVC_COLOR = {"lawyers": "var(--pink)", "mediators": "var(--teal)",
             "coaches": "var(--orange)", "gal": "var(--chartreuse)"}

PAGES = []  # (relpath, html)


# ---- Photo slots: use a dedicated file if present, else fall back -----------
# Upload the real shots into assets/images/ with these names and rebuild — every
# portrait below picks them up automatically. See PHOTOS.md.
def photo(*names, default):
    for n in names:
        if os.path.exists(os.path.join(ROOT_DIR, "assets", "images", n)):
            return n
    return default

HERO_DUO  = photo("hero-duo.jpg", "team-duo.jpg", default="team-laptop.jpg")
LEISA_IMG = photo("leisa.jpg", default="portrait-seated-1.jpg")
NAZ_IMG   = photo("nazarena.jpg", default="team-laptop.jpg")
TEAM_TRIO = photo("team-trio.jpg", "team-three.jpg", default="")

# Feature photos for service / about / coparenting pages (fall back to nothing).
FEAT_LAWYERS   = photo("svc-lawyers.jpg", default="")
FEAT_MEDIATORS = photo("svc-mediators.jpg", default="")
FEAT_COACHES   = photo("svc-coaches.jpg", default="")
FEAT_GAL       = photo("svc-gal.jpg", default="")
FEAT_ABOUT     = photo("about-duo.jpg", default="")
FEAT_COPARENT  = photo("coparenting.jpg", default="")

def feature(root, fn, pos="center 22%"):
    if not fn:
        return ""
    return (f'<section class="section paper" style="padding-top:0;padding-bottom:0">'
            f'<div class="wrap"><img src="{root}assets/images/{fn}" alt="Family Matters Law Group" '
            f'style="width:100%;max-height:540px;object-fit:cover;object-position:{pos};'
            f'border-radius:var(--radius);display:block"></div></section>')


def add(relpath, html_str):
    PAGES.append((relpath, html_str))


def root_for(relpath):
    depth = relpath.count("/")
    return "../" * depth


# ---------------------------------------------------------------- header/footer
def header(root, active=""):
    def top(label, href, key):
        cls = ' style="color:var(--chartreuse)"' if active == key else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    ways = f"""
      <div class="has-menu">
        <button class="menu-btn" aria-haspopup="true">Ways we help <span class="caret"></span></button>
        <div class="submenu wide">
          <div class="submenu-title">Four ways in</div>
          <a href="{root}ways-we-help/lawyers/"><span class="sw" style="background:var(--pink)"></span>Lawyers<small>Full &amp; flat-fee representation</small></a>
          <a href="{root}ways-we-help/mediators/"><span class="sw" style="background:var(--teal)"></span>Mediators<small>Neutral settlement, English or Spanish</small></a>
          <a href="{root}ways-we-help/diy-legal-coaches/"><span class="sw" style="background:var(--orange)"></span>DIY Legal Coaches<small>Represent yourself, not alone</small></a>
          <a href="{root}ways-we-help/guardians-ad-litem/"><span class="sw" style="background:var(--chartreuse)"></span>Guardians ad Litem<small>An independent voice for the kids</small></a>
          <div class="submenu-title">Also offered</div>
          <a href="{root}ways-we-help/coparenting-coaching/">Coparenting Coaching &amp; Education</a>
          <a href="{root}ways-we-help/paralegal-services/">Paralegal Document Services</a>
          <a href="{root}ways-we-help/diy-divorce-packages/">DIY Divorce Packages</a>
          <a href="{root}ways-we-help/parenting-coordination/">Parenting Coordination</a>
          <a href="{root}ways-we-help/collaborative-divorce/">Collaborative Divorce</a>
        </div>
      </div>"""
    topics = f"""
      <div class="has-menu">
        <button class="menu-btn" aria-haspopup="true">Topics <span class="caret"></span></button>
        <div class="submenu wide">
          <a href="{root}topics/divorce/">Divorce</a>
          <a href="{root}topics/custody-and-parenting/">Custody &amp; Parenting</a>
          <a href="{root}topics/child-support/">Child Support</a>
          <a href="{root}topics/alimony/">Alimony</a>
          <a href="{root}topics/paternity/">Paternity</a>
          <a href="{root}topics/adoption/">Adoption</a>
          <a href="{root}topics/injunctions-domestic-violence/">Injunctions &amp; DV</a>
          <a href="{root}topics/lgbtq-family-law/">LGBTQ+ Family Law</a>
          <a href="{root}topics/name-change/">Name Change</a>
          <a href="{root}topics/prenup-postnup/">Prenup &amp; Postnup</a>
        </div>
      </div>"""
    learn = f"""
      <div class="has-menu">
        <button class="menu-btn" aria-haspopup="true">Learn <span class="caret"></span></button>
        <div class="submenu">
          <a href="{root}blog/">Blog &amp; Guides</a>
          <a href="{root}glossary/">Legal Glossary</a>
        </div>
      </div>"""
    about = f"""
      <div class="has-menu">
        <button class="menu-btn" aria-haspopup="true">About <span class="caret"></span></button>
        <div class="submenu">
          <a href="{root}about/">About the firm</a>
          <a href="{root}team/">Our team</a>
          <a href="{root}attorneys/leisa-wintz/">Leisa Wintz</a>
          <a href="{root}attorneys/nazarena-hauser/">Nazarena Hauser</a>
          <a href="{root}reviews/">Reviews</a>
        </div>
      </div>"""
    return f"""<header class="site" id="siteHeader">
  <div class="wrap nav-row">
    <a href="{root}" class="nav-logo" aria-label="Family Matters Law Group — home">
      <img class="logo-white" src="{root}assets/images/wordmark-white.png" alt="Family Matters Law Group">
      <img class="logo-black" src="{root}assets/images/wordmark-black.png" alt="Family Matters Law Group">
    </a>
    <nav class="links" id="navLinks">{ways}{topics}
      <a href="{root}pricing/">Pricing</a>{learn}{about}
      <a class="nav-lang" href="{root}es/" hreflang="es" lang="es">ES</a>
      <a href="{CTA['get_started']}" class="nav-cta">Get started</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>"""


def footer(root):
    return f"""<footer class="site">
  <div class="footer-chev" aria-hidden="true"><img src="{root}assets/images/chevrons.png" alt=""></div>
  <div class="wrap footer-cta">
    <span class="script">Ready when you are.</span>
    <h2 class="display">Let's talk.</h2>
    <a href="{CTA['get_started']}" class="btn btn-solid">Get started</a>
  </div>
  <div class="wrap footer-grid">
    <div>
      <img class="footer-logo" src="{root}assets/images/wordmark-white.png" alt="Family Matters Law Group">
      <p>Florida family law — lawyers, mediators, DIY legal coaches, and guardians ad litem, under one roof. Bilingual practice, se habla español.</p>
    </div>
    <div>
      <h4>Ways we help</h4>
      <a href="{root}ways-we-help/lawyers/">Lawyers</a>
      <a href="{root}ways-we-help/mediators/">Mediators</a>
      <a href="{root}ways-we-help/diy-legal-coaches/">DIY Legal Coaches</a>
      <a href="{root}ways-we-help/guardians-ad-litem/">Guardians ad Litem</a>
      <a href="{root}pricing/">Flat-fee pricing</a>
    </div>
    <div>
      <h4>Learn</h4>
      <a href="{root}topics/divorce/">Divorce</a>
      <a href="{root}topics/custody-and-parenting/">Custody &amp; Parenting</a>
      <a href="{root}blog/">Blog &amp; Guides</a>
      <a href="{root}glossary/">Legal Glossary</a>
    </div>
    <div>
      <h4>Firm</h4>
      <a href="{root}about/">About &amp; team</a>
      <a href="{root}reviews/">Reviews</a>
      <a href="{root}current-clients/">Current clients</a>
      <a href="{SPANISH}" hreflang="es" lang="es">En español</a>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© 2026 Family Matters Law Group, P.A. All rights reserved.</span>
    <span>Serving Broward &amp; South Florida — in English and Spanish.</span>
  </div>
</footer>"""


def page(relpath, title, desc, body, active="", is_home=False):
    root = root_for(relpath)
    cls = ' class="home"' if is_home else ""
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,500;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/site.css">
</head>
<body{cls}>
{header(root, active)}
<main>
{body}
</main>
{footer(root)}
<script src="{root}assets/js/site.js"></script>
</body>
</html>"""
    add(relpath, doc)


# ------------------------------------------------------------------- fragments
def page_hero(eyebrow, h1, lede, root, crumbs, tint="tint-topic", ctas=None):
    cb = ' <span>/</span> '.join(
        [f'<a href="{root}">Home</a>'] +
        [f'<a href="{root}{href}">{label}</a>' for label, href in crumbs[:-1]] +
        [crumbs[-1][0]]
    )
    ctahtml = ""
    if ctas:
        ctahtml = '<div class="hero-ctas">' + "".join(ctas) + "</div>"
    return f"""<section class="page-hero {tint}">
  <div class="wrap">
    <div class="breadcrumb">{cb}</div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    {ctahtml}
  </div>
</section>"""


def cta_band(root, color, h, p, label, href):
    return f"""<section class="section {'tight' if True else ''}">
  <div class="wrap">
    <div class="cta-band {color}">
      <div><h2>{h}</h2><p>{p}</p></div>
      <a href="{href}" class="btn btn-solid">{label}</a>
    </div>
  </div>
</section>"""


def faq(items):
    rows = "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items
    )
    return f'<div class="faq">{rows}</div>'


def subpaths(cards):
    out = []
    for c in cards:
        price = f'<div class="price">{c["price"]}</div>' if c.get("price") else ""
        out.append(f"""<div class="subpath">
  <h3>{c['h']}</h3><div class="who">{c['who']}</div>
  <p>{c['p']}</p>{price}
</div>""")
    return '<div class="subpaths">' + "".join(out) + "</div>"


# =============================================================================
#  SERVICE-LINE PAGES
# =============================================================================
def svc_hero_ctas(key, root, secondary_label="See pricing", secondary_href_rel="pricing/"):
    return [
        f'<a href="{CTA[key]}" class="btn btn-solid">Start your { "" }intake</a>'.replace("your intake", "intake"),
        f'<a href="{root}{secondary_href_rel}" class="btn btn-outline-light">{secondary_label}</a>',
    ]


# --- Lawyers -----------------------------------------------------------------
root = "../../"
add_body = f"""
{page_hero("Lawyers · Full representation", "When you want someone to carry the whole case",
  "Full and flat-fee representation for divorce, custody, paternity, support, and enforcement — from the first filing through settlement or trial. You get a licensed Florida family lawyer running your case, not a form and a phone tree.",
  root, [("Ways we help", "ways-we-help/lawyers/"), ("Lawyers", "")], tint="tint-lawyers",
  ctas=[f'<a href="{CTA["lawyers"]}" class="btn btn-solid">Start your intake</a>',
        f'<a href="{root}pricing/" class="btn btn-outline-light">See flat-fee pricing</a>'])}
{feature(root, FEAT_LAWYERS)}
<section class="section paper">
  <div class="wrap split">
    <div class="prose">
      <div class="kicker">Three ways to be represented</div>
      <h2>Pick the level of representation that fits the case</h2>
      <p>Not every case needs the same thing. Some need a lawyer on every hearing; some need a fixed price for a known, uncontested outcome; some need a lawyer for one specific hearing and nothing more. We offer all three, and we'll tell you honestly which one your situation actually calls for.</p>
    </div>
    <aside class="aside-card">
      <h4>On this page</h4>
      <ul>
        <li><a href="#full">Full representation</a></li>
        <li><a href="#flat">Flat-fee representation</a></li>
        <li><a href="#limited">Limited appearance</a></li>
        <li><a href="#gal-vs">GAL vs. Attorney ad Litem</a></li>
        <li><a href="{root}pricing/">Full pricing menu</a></li>
      </ul>
    </aside>
  </div>
</section>

<section class="section dim">
  <div class="wrap">
    {subpaths([
      {"h":"Full Representation","who":"Best for contested cases","p":"We handle everything — filings, discovery, negotiation, hearings, and trial if it comes to that. The right call when the other side has a lawyer, when there's real conflict over money or the kids, or when the facts are complicated.","price":"Retainer-based · <a href='" + root + "pricing/'>see rates</a>"},
      {"h":"Flat-Fee Representation","who":"Best for known, uncontested outcomes","p":"A single fixed price for matters with a predictable path: uncontested divorce, uncontested modifications, enforcement, prenups and postnups, step-parent adoption, and final-judgment reviews. No hourly meter, no surprise bill.","price":"Flat fee · <a href='" + root + "pricing/'>see the menu</a>"},
      {"h":"Limited Appearance","who":"Best for one specific hearing","p":"We appear for a single defined event — a case-management conference, an emergency motion, a specific hearing — and step out when it's done. Real representation for the moment that matters, without retaining us for the whole case.","price":"Priced per hearing · <a href='" + root + "pricing/'>see rates</a>"},
    ])}
  </div>
</section>

<section class="section paper" id="flat">
  <div class="wrap measure prose">
    <h2 id="full">What we get flat-fee</h2>
    <p>These are the matters where the path is clear enough to quote a single price up front:</p>
    <ul class="lead-list">
      <li>Uncontested divorce (with or without children)</li>
      <li>Uncontested modifications of support or timesharing</li>
      <li>Enforcement of an existing order</li>
      <li>Prenuptial and postnuptial agreements</li>
      <li>Step-parent adoption</li>
      <li>Final-judgment reviews</li>
    </ul>
    <p>Every flat fee lives on one page — our <a href="{root}pricing/">flat-fee pricing menu</a> — so you never have to reconcile two different numbers from two different pages.</p>

    <h2 id="gal-vs">Guardian ad Litem vs. Attorney ad Litem</h2>
    <p>People mix these up constantly, and most firm websites never explain the difference. A <strong>Guardian ad Litem</strong> investigates and reports to the court on what's in the child's best interest — they are not the child's lawyer. An <strong>Attorney ad Litem</strong> actually represents the child and advocates for the child's stated position, the way any lawyer represents a client. We serve in both roles, and we'll tell you which one a given case needs.</p>
    <div class="callout pink"><strong>Truth + context:</strong> a lawyer isn't always the cheapest path, and it isn't always the right one. If mediation or DIY coaching fits your case better, we'll say so — see <a href="{root}ways-we-help/mediators/">Mediators</a> and <a href="{root}ways-we-help/diy-legal-coaches/">DIY Legal Coaches</a>.</div>
  </div>
</section>

{cta_band(root,"pink","Ready to have a lawyer in your corner?","Your intake goes straight to our full-representation team — no generic contact form.","Start your intake",CTA["lawyers"])}
"""
page("ways-we-help/lawyers/index.html",
     "Lawyers — Full & Flat-Fee Family Law Representation | Family Matters Law Group",
     "Full, flat-fee, and limited-appearance family law representation in South Florida: divorce, custody, paternity, support, and enforcement.",
     add_body, active="ways")

# --- Mediators ---------------------------------------------------------------
body = f"""
{page_hero("Mediators · Neutral settlement", "A settlement both sides can live with — in English or in Spanish",
  "Mediation is faster and less costly than litigation, and the agreements are built to hold up in court. Both of our attorneys are Florida Supreme Court certified mediators, serving parties with or without their own lawyers — including mediation conducted entirely in Spanish.",
  root, [("Ways we help","ways-we-help/mediators/"),("Mediators","")], tint="tint-mediators",
  ctas=[f'<a href="{CTA["mediators"]}" class="btn btn-solid">Book mediation</a>',
        f'<a href="{root}pricing/" class="btn btn-outline-light">See mediation rates</a>'])}
{feature(root, FEAT_MEDIATORS)}
<section class="section paper">
  <div class="wrap measure prose">
    <div class="kicker">Two ways to use a mediator</div>
    <h2>Mediator-only, or your lawyer at the table</h2>
    <p>Mediation isn't one thing. You can hire us as the <strong>neutral mediator</strong> for both parties, or — if we're representing you — have your attorney <strong>at the table with you</strong> at someone else's mediation. Same skill set, two very different roles. We'll make sure you're in the right one.</p>
    <div class="callout"><strong>Bilingual by design.</strong> This is a South Florida firm. We mediate in English or entirely in Spanish — se habla español — so no one at the table is negotiating in their second language on the biggest decisions of their life.</div>
    <h2>Why mediation works</h2>
    <ul class="lead-list">
      <li>Faster and less expensive than a contested trial</li>
      <li>You keep control of the outcome instead of handing it to a judge</li>
      <li>Agreements you help build have a higher rate of compliance than orders imposed from the bench</li>
      <li>Private — what's said in mediation stays in mediation</li>
    </ul>
    <p>Mediation is billed hourly on a sliding scale based on combined household income — the exact rates live on our <a href="{root}pricing/">pricing page</a>, in one place, so you know before you book.</p>
    <p class="mt-s">New to it? Read <a href="{root}blog/mediation-prep/">how to walk into mediation ready</a> and the difference our <a href="{root}attorneys/leisa-wintz/">family-systems background</a> makes at the table.</p>
  </div>
</section>

<section class="section dim">
  <div class="wrap">
    <div class="kicker center">For referring attorneys</div>
    <h2 class="h2 center" style="margin-bottom:14px;">A neutral your clients will actually settle with</h2>
    <p class="measure center" style="margin:0 auto;color:var(--muted);">We take referrals from other family lawyers who want a certified, bilingual mediator with real trial perspective — including a recommendation on record from a referring attorney. Send us the case; we'll handle the neutral role and get both sides to a durable agreement.</p>
  </div>
</section>

{cta_band(root,"teal","Ready to settle instead of fight?","Book directly with our mediation team — English or Spanish.","Book mediation",CTA["mediators"])}
"""
page("ways-we-help/mediators/index.html",
     "Mediators — Certified, Bilingual Divorce Mediation | Family Matters Law Group",
     "Florida Supreme Court certified divorce and family mediation in English or Spanish, for parties with or without their own attorneys.",
     body, active="ways")

# --- DIY Legal Coaches -------------------------------------------------------
body = f"""
{page_hero("DIY Legal Coaches · Represent yourself, not alone", "Handle your own case with a lawyer coaching you through it",
  "Represent yourself with a licensed Florida attorney coaching you on strategy, paperwork, and courtroom prep — at a fraction of full representation. Transparent flat fees for individual tasks, plus monthly subscription plans for ongoing support.",
  root, [("Ways we help","ways-we-help/diy-legal-coaches/"),("DIY Legal Coaches","")], tint="tint-coaches",
  ctas=[f'<a href="{CTA["coaches"]}" class="btn btn-solid">Start coaching</a>',
        f'<a href="{root}pricing/" class="btn btn-outline-light">See coaching prices</a>'])}
{feature(root, FEAT_COACHES)}
<section class="section paper">
  <div class="wrap measure prose">
    <div class="kicker">How it works</div>
    <h2>You run the case. We make sure you don't run it into a wall.</h2>
    <p>Plenty of people can handle their own Florida family case — they just shouldn't do it blind. DIY Legal Coaching gives you a licensed attorney to review documents, plan strategy, prep you for hearings, and catch the mistakes that quietly sink pro se cases: bad time-sharing language, missed disclosures, unenforceable terms.</p>
    <h2>Pay per task, or subscribe</h2>
    <p>Flat fees by service — document review, parenting-plan prep, child-support strategy, MSA review, evidentiary-hearing prep, and more — so you only pay for the help you need. Prefer ongoing support? Our <strong>Essentials</strong> and <strong>Plus</strong> monthly plans (3-, 6-, and 12-month terms) give you a standing coaching relationship. Every price is on the <a href="{root}pricing/">pricing page</a>.</p>
    <div class="callout orange"><strong>$250 consultation, credited.</strong> Your initial consult fee is credited toward any retainer over $2,500. Fees are non-refundable but flexible for upgrades, a conflict check is required before we start, and plans carry a simple 30-day cancellation notice — no fine-print surprises.</div>
    <h2>Pair it with paralegal drafting</h2>
    <p>Our <a href="{root}ways-we-help/paralegal-services/">paralegals prepare your documents. Coaching teaches you what they mean.</a> Together they're a genuinely affordable way to get a Florida case done right without full representation.</p>
  </div>
</section>

<section class="section dim">
  <div class="wrap">
    <div class="kicker">DIY Legal Shop</div>
    <h2 class="h2" style="margin-bottom:20px;">Courses, templates &amp; toolkits</h2>
    <div class="cards">
      <div class="card"><span class="sw" style="background:var(--orange)"></span><h3>On-demand courses</h3><p>Self-paced walkthroughs of Florida divorce, custody, and discovery.</p></div>
      <div class="card"><span class="sw" style="background:var(--teal)"></span><h3>Document templates</h3><p>Attorney-built forms and checklists you can actually use.</p></div>
      <div class="card"><span class="sw" style="background:var(--pink)"></span><h3>Coaching subscription</h3><p>Ongoing access to a licensed attorney, month to month.</p></div>
    </div>
    <div class="mt-m"><a href="{CTA['coaches']}" class="btn btn-solid" style="background:var(--orange);box-shadow:0 12px 28px rgba(251,92,14,.34);">Browse the shop</a></div>
  </div>
</section>

{cta_band(root,"orange","Do it yourself — just not blind.","Start with a coaching consult and we'll map your whole case.","Start coaching",CTA["coaches"])}
"""
page("ways-we-help/diy-legal-coaches/index.html",
     "DIY Legal Coaches — Attorney-Coached Self-Representation | Family Matters Law Group",
     "Represent yourself in your Florida family case with a licensed attorney coaching you: flat-fee tasks and monthly subscription plans.",
     body, active="ways")

# --- Guardians ad Litem ------------------------------------------------------
body = f"""
{page_hero("Guardians ad Litem · A voice for the kids", "An independent voice for the children in the case",
  "A Guardian ad Litem is a court-appointed advocate focused on the children's best interests when parents can't find common ground. We serve as GAL with a rare thing on a firm website: an honest account of what the role can — and can't — do for your family.",
  root, [("Ways we help","ways-we-help/guardians-ad-litem/"),("Guardians ad Litem","")], tint="tint-gal",
  ctas=[f'<a href="{CTA["gal"]}" class="btn btn-solid">Request a GAL</a>',
        f'<a href="{root}blog/guardian-ad-litem-guide/" class="btn btn-outline-light">Read the full guide</a>'])}
{feature(root, FEAT_GAL)}
<section class="section paper">
  <div class="wrap split">
    <div class="prose">
      <div class="kicker">The role, honestly</div>
      <h2>What a Guardian ad Litem actually does</h2>
      <p>A GAL investigates and reports to the court on what's in the child's best interest. That means interviews with both parents and the children, a review of records, and — where appropriate — a written report and recommendation. A GAL is not the child's lawyer and does not simply repeat what the child wants; the job is the child's <em>interests</em>, which are not always the same thing.</p>
      <h3>The investigation, step by step</h3>
      <ul class="lead-list">
        <li>Interviews with each parent and the children</li>
        <li>Review of school, medical, and case records</li>
        <li>A hearsay-waiver process so the GAL can consider what others report</li>
        <li>A best-interest recommendation to the court</li>
      </ul>
    </div>
    <aside class="aside-card">
      <h4>Honest trade-offs</h4>
      <ul>
        <li><strong>Cost</strong> — a GAL is an added expense in an already expensive process.</li>
        <li><strong>Loss of control</strong> — you're inviting a neutral third party to weigh in on your family.</li>
        <li><strong>Possible disagreement</strong> — the recommendation may not match what you wanted.</li>
      </ul>
      <p style="margin-top:12px;font-size:13.5px;color:var(--muted);">We list these on purpose. If a GAL isn't right for your case, you should know that before you ask for one.</p>
    </aside>
  </div>
</section>

<section class="section dim">
  <div class="wrap measure prose">
    <h2>Expertise where it's needed most</h2>
    <p>Our GAL work draws on real depth in high-conflict parenting and substance-abuse dynamics, plus a family-therapy background that helps a neutral read a family accurately rather than just reading the file. For the full walkthrough — including how appointment and reporting work — see the <a href="{root}blog/guardian-ad-litem-guide/">complete GAL guide</a>.</p>
    <div class="callout chartreuse"><strong>Already appointed to your case?</strong> Active-client tools — evidence upload, the client portal, and your order of appointment — live in the <a href="{root}current-clients/">Current Clients</a> area, kept separate from this public page.</div>
  </div>
</section>

{cta_band(root,"chartreuse","Considering a Guardian ad Litem?","Tell us about the case and we'll walk you through whether a GAL fits.","Request a GAL",CTA["gal"])}
"""
page("ways-we-help/guardians-ad-litem/index.html",
     "Guardians ad Litem — Court-Appointed Child Advocacy | Family Matters Law Group",
     "Court-appointed Guardian ad Litem services in South Florida, with an honest account of the benefits and the trade-offs.",
     body, active="ways")

print("service pages queued")

# =============================================================================
#  DIY SUB-PAGES  (ways-we-help/*)  depth 2
# =============================================================================
root = "../../"

# --- Coparenting Coaching & Education (from provided draft) -------------------
body = f"""
{page_hero("Coparenting Coaching &amp; Education", "Raising kids together doesn't stop when the case does",
  "Whether you're mid-divorce, already final, or never set foot in a courtroom at all — if coparenting is hard, we can help. This service is built around your family, not a script. It isn't therapy, and it isn't legal advice: it's practical coaching for real conflict, real transitions, and real communication problems.",
  root, [("Ways we help","ways-we-help/diy-legal-coaches/"),("Coparenting Coaching","")], tint="tint-mediators",
  ctas=[f'<a href="{CTA["coaches"]}" class="btn btn-solid">Schedule a consult</a>'])}
{feature(root, FEAT_COPARENT)}
<section class="section paper">
  <div class="wrap measure prose">
    <div class="kicker">What it is</div>
    <h2>Customized, one-on-one coparenting support</h2>
    <p>Coparenting Coaching &amp; Education is one-on-one support for parents trying to raise kids with someone they're not married to — or married to, but struggling to coparent with. No two families get the same plan. We build yours around what's actually happening in your house.</p>
  </div>
</section>

<section class="section dim">
  <div class="wrap">
    <div class="kicker">Who this is for</div>
    <h2 class="h2" style="margin-bottom:22px;">Three moments this helps most</h2>
    {subpaths([
      {"h":"During active litigation","who":"Lower the temperature","p":"Tensions run high while a case is open. Coaching here is about working through parenting disagreements as they come up — so they don't turn into more filings, more fees, and more damage to the kids in the middle."},
      {"h":"Post-litigation","who":"After the judgment","p":"The judgment is entered, but the hard part — actually coparenting — is just starting. We help with exchanges, holidays, new partners, school decisions, and the hundred small handoffs a parenting plan can't fully cover."},
      {"h":"Completely outside litigation","who":"No case required","p":"No court, no lawyer needed. If you and your coparent are stuck and want outside help sorting it out, you don't have to be a legal client to work with us."},
    ])}
  </div>
</section>

<section class="section paper">
  <div class="wrap measure">
    <div class="kicker">How it works</div>
    <h2 class="h2" style="margin-bottom:22px;">A plan built for your family — and someone to work it with you</h2>
    <div class="steps">
      <div class="step"><div><h3>We start with your family</h3><p>A conversation about what's not working — communication, transitions, decision-making, a difficult coparent, a difficult ex.</p></div></div>
      <div class="step"><div><h3>We build a plan</h3><p>Specific to your kids' ages, your custody arrangement, and where the conflict actually lives.</p></div></div>
      <div class="step"><div><h3>We coach through it</h3><p>Ongoing sessions to work the plan, adjust it, and handle what comes up next.</p></div></div>
    </div>
    <div class="prose mt-l">
      <h2>Why Family Matters Law Group</h2>
      <p>We've sat across from thousands of parents mid-conflict. We know what coparenting looks like when it's going wrong — and what it takes to get it working — without you needing to be in active litigation to access that experience.</p>
      <ul class="lead-list">
        <li><strong>Clarity.</strong> Straight answers about what's realistic for your family — no fog.</li>
        <li><strong>Options.</strong> Real strategies for your specific conflict, not a generic script.</li>
        <li><strong>Control.</strong> You and your coparent are the ones raising these kids. We help you do it on your terms.</li>
      </ul>
    </div>
  </div>
</section>

{cta_band(root,"teal","Coparenting is hard. You don't have to figure it out alone.","Schedule a free consult, book a paid strategy session, or skip the consult and move forward.","Schedule a consult",CTA["coaches"])}
"""
page("ways-we-help/coparenting-coaching/index.html",
     "Coparenting Coaching & Education | Family Matters Law Group",
     "One-on-one coparenting coaching for Florida parents — during litigation, after it, or entirely outside of court. Practical tools, not a script.",
     body, active="ways")

# --- Paralegal Services ------------------------------------------------------
body = f"""
{page_hero("Paralegal Document Services", "Paralegals prepare your documents. Coaching teaches you what they mean.",
  "Itemized, flat-fee document preparation for Florida family cases — very few firms publish this level of detail. Pair it with DIY Legal Coaching and you get documents done right plus an attorney to explain them.",
  root, [("Ways we help","ways-we-help/diy-legal-coaches/"),("Paralegal Services","")], tint="tint-coaches",
  ctas=[f'<a href="{CTA["coaches"]}" class="btn btn-solid">Get started</a>',
        f'<a href="{root}pricing/" class="btn btn-outline-light">See document pricing</a>'])}
{feature(root, photo("page-paralegal.jpg", default=""))}
<section class="section paper">
  <div class="wrap measure prose">
    <div class="kicker">Who this is for</div>
    <h2>You know what you need drafted — you just want it done right</h2>
    <p>Our paralegals prepare individual family-law documents at flat rates (generally $350–$500 each), itemized by document type on the <a href="{root}pricing/">pricing page</a>. It's the affordable middle path between a blank form and full representation.</p>
    <div class="callout orange"><strong>Honest limit:</strong> paralegals cannot give legal advice. They prepare documents; they don't tell you what legal strategy to pursue. That's exactly why we pair document prep with <a href="{root}ways-we-help/diy-legal-coaches/">DIY Legal Coaching</a> — the paralegals prepare your documents, and the attorney coaching teaches you what they mean and whether they're right for your case.</div>
    <p>Considering a full uncontested divorce package instead? Compare the tiers on <a href="{root}ways-we-help/diy-divorce-packages/">DIY Divorce Packages</a>.</p>
  </div>
</section>

{cta_band(root,"orange","Documents done right, without the full retainer.","Start with paralegal prep, add coaching whenever you want an attorney's read.","Get started",CTA["coaches"])}
"""
page("ways-we-help/paralegal-services/index.html",
     "Paralegal Document Services | Family Matters Law Group",
     "Flat-fee family-law document preparation in Florida, itemized by document type and paired with attorney coaching.",
     body, active="ways")

# --- DIY Divorce Packages ----------------------------------------------------
body = f"""
{page_hero("DIY Divorce Packages", "You can DIY your divorce. Don't do it alone.",
  "Three honest tiers for an uncontested Florida divorce — from paralegal-drafted documents to a full-service package — so you can choose the level of help you actually want at a glance.",
  root, [("Ways we help","ways-we-help/diy-legal-coaches/"),("DIY Divorce Packages","")], tint="tint-coaches",
  ctas=[f'<a href="{CTA["coaches"]}" class="btn btn-solid">Start your divorce</a>',
        f'<a href="{root}pricing/" class="btn btn-outline-light">Compare all pricing</a>'])}
{feature(root, photo("page-diy-divorce.jpg", default=""))}
<section class="section paper">
  <div class="wrap">
    <div class="kicker">Choose your tier</div>
    <h2 class="h2" style="margin-bottom:22px;">Three uncontested-divorce packages</h2>
    {subpaths([
      {"h":"Paralegal-Drafted","who":"Most affordable","p":"Our paralegals prepare your uncontested divorce documents. You handle the filing and the process; you get correctly prepared paperwork instead of a guess.","price":"From $499 · <a href='"+root+"pricing/'>details</a>"},
      {"h":"DIY + Attorney Drafting","who":"Most popular","p":"You run the case, but an attorney drafts and reviews the documents that matter — so your marital settlement agreement and parenting plan are actually enforceable.","price":"From $2,500 · <a href='"+root+"pricing/'>details</a>"},
      {"h":"Full-Service Divorce","who":"Hands-off","p":"We handle the uncontested divorce end to end. You show up, sign, and get to the finish line.","price":"From $3,500 · <a href='"+root+"pricing/'>details</a>"},
    ])}
  </div>
</section>

<section class="section dim">
  <div class="wrap measure prose">
    <h2>Why "don't do it alone" isn't a scare tactic</h2>
    <p>People don't usually blow up their own divorce with drama — they do it with small, technical mistakes: vague time-sharing language a judge won't enforce, missed financial disclosures, or terms that sound fine and turn out to be unenforceable two years later. Every tier above exists to close a specific one of those gaps. Pick the one that matches how much of this you want to run yourself.</p>
    <div class="callout"><strong>One price, one place.</strong> All three tiers — and everything else — live on the single <a href="{root}pricing/">flat-fee pricing page</a>, so two pages never quote you two different numbers.</div>
  </div>
</section>

{cta_band(root,"orange","Ready to start your uncontested divorce?","Tell us your situation and we'll point you to the right tier.","Start your divorce",CTA["coaches"])}
"""
page("ways-we-help/diy-divorce-packages/index.html",
     "DIY Divorce Packages | Family Matters Law Group",
     "Three flat-fee tiers for an uncontested Florida divorce: paralegal-drafted, DIY with attorney drafting, or full service.",
     body, active="ways")

# --- Parenting Coordination --------------------------------------------------
body = f"""
{page_hero("Parenting Coordination", "Staying out of court on the day-to-day conflicts",
  "Parenting coordination is a structured, out-of-court process to help high-conflict coparents resolve the ongoing disputes a parenting plan can't fully cover — with a transparent sliding-scale rate stated plainly.",
  root, [("Ways we help","ways-we-help/diy-legal-coaches/"),("Parenting Coordination","")], tint="tint-mediators",
  ctas=[f'<a href="{CTA["get_started"]}" class="btn btn-solid">Get started</a>'])}
{feature(root, photo("page-parenting-coord.jpg", default=""))}
<section class="section paper">
  <div class="wrap measure">
    <div class="kicker">The process</div>
    <h2 class="h2" style="margin-bottom:22px;">Five steps, clearly defined</h2>
    <div class="steps">
      <div class="step"><div><h3>Intake &amp; conflict check</h3><p>We confirm there's no conflict and gather the history of the dispute.</p></div></div>
      <div class="step"><div><h3>Initial sessions</h3><p>Meet each parent, understand the recurring flashpoints, set ground rules.</p></div></div>
      <div class="step"><div><h3>Joint coordination meetings</h3><p>Work the actual disagreements — schedules, exchanges, decisions — with a neutral in the room.</p></div></div>
      <div class="step"><div><h3>Issue resolution</h3><p>Reach and document workable resolutions the parents can live with.</p></div></div>
      <div class="step"><div><h3>Court reports, if authorized</h3><p>Where the order authorizes it, report to the court on unresolved issues.</p></div></div>
    </div>
    <div class="prose mt-l">
      <div class="callout"><strong>Transparent rate:</strong> parenting coordination is billed on a sliding scale of <strong>$375–$450/hour</strong> based on combined household income. Related family services and their rates are on the <a href="{root}pricing/">pricing page</a>.</div>
    </div>
  </div>
</section>

{cta_band(root,"teal","Stuck in the same fight every other week?","A parenting coordinator can break the loop — without another trip to court.","Get started",CTA["get_started"])}
"""
page("ways-we-help/parenting-coordination/index.html",
     "Parenting Coordination | Family Matters Law Group",
     "Out-of-court parenting coordination for high-conflict Florida coparents, with a transparent $375–$450/hr sliding-scale rate.",
     body, active="ways")

# --- Collaborative Divorce ---------------------------------------------------
body = f"""
{page_hero("Collaborative Divorce", "Divorce doesn't have to be ugly",
  "Collaborative divorce is a structured, out-of-court process where both spouses and their professionals commit to reaching a settlement without litigation. It can be thoughtful, strategic, and peaceful — without sacrificing fairness.",
  root, [("Ways we help","ways-we-help/collaborative-divorce/"),("Collaborative Divorce","")], tint="tint-mediators",
  ctas=[f'<a href="{CTA["get_started"]}" class="btn btn-solid">See if it fits</a>'])}
{feature(root, photo("page-collaborative.jpg", default=""))}
<section class="section paper">
  <div class="wrap measure prose">
    <div class="kicker">Honest first question</div>
    <h2>Is collaboration realistic for your case?</h2>
    <p>Collaborative divorce works beautifully for some couples and not at all for others. Rather than sell you the option, we help you assess whether it's realistic <em>before</em> you commit — because a collaborative process that collapses halfway is more expensive than starting in the right lane. If it fits, few paths are calmer or more private. If it doesn't, we'll tell you and point you to <a href="{root}ways-we-help/mediators/">mediation</a> or <a href="{root}ways-we-help/lawyers/">full representation</a>.</p>
    <blockquote>Divorce doesn't have to be ugly. It can be thoughtful, strategic, and peaceful — without sacrificing fairness.</blockquote>
  </div>
</section>

{cta_band(root,"teal","Want a calmer way through?","We'll help you decide whether collaborative divorce is realistic for your family.","See if it fits",CTA["get_started"])}
"""
page("ways-we-help/collaborative-divorce/index.html",
     "Collaborative Divorce | Family Matters Law Group",
     "Collaborative divorce in Florida — a structured, out-of-court path to a fair settlement, with an honest read on whether it fits your case.",
     body, active="ways")

print("diy subpages queued")

# =============================================================================
#  TOPIC PAGES  (topics/*)  depth 2
# =============================================================================
root = "../../"

TOPIC_FEAT = {
  "divorce": "topic-divorce.jpg", "custody-and-parenting": "topic-custody.jpg",
  "child-support": "topic-child-support.jpg", "alimony": "topic-alimony.jpg",
  "paternity": "topic-paternity.jpg", "adoption": "topic-adoption.jpg",
  "injunctions-domestic-violence": "topic-injunctions.jpg", "lgbtq-family-law": "topic-lgbtq.jpg",
  "name-change": "topic-name-change.jpg", "prenup-postnup": "topic-prenup.jpg",
}
def build_topic(slug, mtitle, mdesc, eyebrow, h1, lede, main_html, faqs, related, tint="tint-topic"):
    feat = TOPIC_FEAT.get(slug, "")
    rel = "".join(f'<a href="{root}{href}">{label}</a>' for label, href in related)
    faq_html = ""
    if faqs:
        faq_html = f"""<section class="section dim"><div class="wrap measure">
          <div class="kicker">Common questions</div>
          <h2 class="h2" style="margin-bottom:18px;">Straight answers</h2>{faq(faqs)}</div></section>"""
    body = f"""
{page_hero(eyebrow, h1, lede, root, [("Topics","topics/"+slug+"/"),(h1.split("—")[0].strip(),"")], tint=tint,
  ctas=[f'<a href="{CTA["get_started"]}" class="btn btn-solid">Get started</a>',
        f'<a href="{root}pricing/" class="btn btn-outline-light">See pricing</a>'])}
{feature(root, photo(feat, default=""))}
{main_html}
{faq_html}
<section class="section paper"><div class="wrap">
  <div class="kicker">Related</div>
  <h2 class="h2" style="margin-bottom:16px;">Keep reading</h2>
  <div class="related">{rel}</div>
</div></section>
{cta_band(root,"pink","Not sure which way in fits your case?","Tell us your situation and we'll route you to the right level of help — no hard sell.","Get started",CTA["get_started"])}
"""
    page("topics/"+slug+"/index.html", mtitle, mdesc, body, active="")

# --- Divorce -----------------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap">
  <div class="kicker">Five ways to divorce in Florida</div>
  <h2 class="h2" style="margin-bottom:20px;">Not every divorce is the same divorce</h2>
  {subpaths([
    {"h":"Uncontested","who":"You mostly agree","p":"You and your spouse agree on the major terms. The fastest, cheapest path — done right so the agreement actually holds.","price":"Flat-fee · <a href='"+root+"ways-we-help/diy-divorce-packages/'>packages</a>"},
    {"h":"Mediated","who":"You're close, not there yet","p":"A neutral mediator helps you close the remaining gaps and build an enforceable agreement — in English or Spanish.","price":"<a href='"+root+"ways-we-help/mediators/'>Mediation</a>"},
    {"h":"Contested / Litigated","who":"There's real conflict","p":"When money or the kids are genuinely disputed, you want a lawyer running the whole case.","price":"<a href='"+root+"ways-we-help/lawyers/'>Full representation</a>"},
    {"h":"Collaborative","who":"You want it calm","p":"A structured, out-of-court process where both sides commit to settling without litigation.","price":"<a href='"+root+"ways-we-help/collaborative-divorce/'>Collaborative</a>"},
    {"h":"DIY with support","who":"You'll run it yourself","p":"Handle your own case with attorney coaching and paralegal drafting behind you.","price":"<a href='"+root+"ways-we-help/diy-legal-coaches/'>DIY coaching</a>"},
  ])}
</div></section>
<section class="section dim"><div class="wrap measure prose">
  <h2>What a Florida divorce actually decides</h2>
  <p>Whatever path you take, a divorce resolves four things. Understanding them up front is the difference between signing something you understand and signing something you'll fight about later:</p>
  <ul class="lead-list">
    <li><strong>Equitable distribution</strong> — how marital property and debt are divided (see the glossary on <a href="{root}glossary/equitable-distribution/">equitable distribution</a>).</li>
    <li><strong>Alimony</strong> — whether spousal support is owed, and which of Florida's four types applies (<a href="{root}topics/alimony/">more on alimony</a>).</li>
    <li><strong>Parental responsibility &amp; timesharing</strong> — decision-making and the parenting schedule (<a href="{root}topics/custody-and-parenting/">custody &amp; parenting</a>).</li>
    <li><strong>Child support</strong> — calculated under Florida's income-shares model (<a href="{root}topics/child-support/">child support</a>).</li>
  </ul>
</div></section>
"""
build_topic("divorce",
  "Divorce in Florida — Every Path Explained | Family Matters Law Group",
  "The five ways to divorce in Florida — uncontested, mediated, contested, collaborative, and DIY — and the four things every divorce decides.",
  "Topic · Divorce", "Divorce", 
  "Uncontested, mediated, contested, collaborative, or DIY-with-support — Florida gives you more than one way to divorce. Here's how each works, and the four issues every divorce has to resolve.",
  main,
  [("Does adultery affect a Florida divorce?","Adultery doesn't get you a \"better\" divorce — Florida is a no-fault state. But financial misconduct tied to an affair (spending marital money on it) can matter to equitable distribution."),
   ("How long does an uncontested divorce take?","Once the paperwork is correct and both spouses agree, an uncontested divorce can move quickly. The delays are almost always missing disclosures or unenforceable language — exactly what our packages prevent."),
   ("Do we each need our own lawyer?","Not always. If you agree on most terms, mediation or DIY coaching may be enough. If there's real conflict, full representation protects you. We'll tell you honestly which fits.")],
  [("Custody &amp; Parenting","topics/custody-and-parenting/"),("Alimony","topics/alimony/"),("DIY Divorce Packages","ways-we-help/diy-divorce-packages/"),("Divorce &amp; alimony guide","blog/alimony-complete-guide/")])

# --- Custody & Parenting -----------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">Florida, post-2023</div>
  <h2>Timesharing starts from 50/50 — then the facts move it</h2>
  <p>Since 2023, Florida law begins from a <strong>presumption that equal (50/50) timesharing</strong> is in the child's best interest. That's a starting point, not a guarantee: the court can move off it based on the statutory best-interest factors. What decides real cases is the <em>parenting plan</em> — and the details people skip.</p>
  <h2>Don't guess on the details</h2>
  <p>A parenting plan that only covers the schedule is a plan that sends you back to court. The ones that hold up spell out:</p>
  <ul class="lead-list">
    <li>Communication rules between coparents (and with the kids)</li>
    <li>Medical and educational decision-making</li>
    <li>Travel and relocation</li>
    <li>Screen-time and technology expectations</li>
    <li>Expense reimbursement and how it's handled</li>
    <li>Right of first refusal for childcare</li>
  </ul>
  <div class="callout"><strong>Pricing, plainly:</strong> uncontested plans and modifications generally start around $2,500; contested matters through mediation from about $6,000; individual DIY drafting pieces are priced separately. Everything is on the <a href="{root}pricing/">pricing page</a>.</div>
</div></section>
"""
build_topic("custody-and-parenting",
  "Custody & Parenting Plans in Florida | Family Matters Law Group",
  "Florida's 2023 move toward a 50/50 timesharing presumption, and the parenting-plan details that actually keep you out of court.",
  "Topic · Custody", "Custody &amp; Parenting Plans",
  "Florida now starts from a 50/50 timesharing presumption — but the parenting-plan details decide your real life. Here's what to get right, and what it costs.",
  main,
  [("Is Florida really 50/50 now?","The law presumes equal timesharing is in the child's best interest, but a judge can adjust based on the statutory factors. It's a starting point, not an automatic outcome."),
   ("Can we modify a parenting plan later?","Yes, with a substantial, material, and unanticipated change in circumstances. See our guide on <a href='"+root+"blog/modify-parenting-plan/'>modifying a parenting plan</a>.")],
  [("Child Support","topics/child-support/"),("Paternity","topics/paternity/"),("Coparenting Coaching","ways-we-help/coparenting-coaching/"),("Modifying a parenting plan","blog/modify-parenting-plan/")])

# --- Child Support -----------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">How it's calculated</div>
  <h2>Florida uses an income-shares model</h2>
  <p>Florida calculates child support under the <a href="{root}glossary/income-shares-model/">income-shares model</a>: both parents' incomes are combined, the state's guidelines set the total support obligation for the children, and each parent pays a share proportional to their income (adjusted for overnights, health insurance, and childcare).</p>
  <h2>When support isn't paid: enforcement</h2>
  <p>Florida has real teeth for enforcement:</p>
  <ul class="lead-list">
    <li>Wage garnishment</li><li>Tax-refund interception</li>
    <li>Driver's-license and professional-license suspension</li><li>Contempt of court</li>
  </ul>
  <h2>When circumstances change: modification</h2>
  <p>Support can be modified on a substantial, involuntary change — a job loss, a big income change, or a change in the children's needs. If someone is deliberately under-earning, courts can <a href="{root}blog/imputed-income/">impute income</a> to what they could earn.</p>
</div></section>
"""
build_topic("child-support",
  "Child Support in Florida — How It's Calculated | Family Matters Law Group",
  "Florida's income-shares child-support model, enforcement remedies, and when support can be modified.",
  "Topic · Support", "Child Support",
  "How Florida's income-shares model actually calculates support, the enforcement tools behind it, and when a change in your life can change the number.",
  main,
  [("Can child support be lowered if I lose my job?","A genuine, involuntary income drop can support a modification. Voluntary under-earning can backfire — courts may impute income to what you could earn."),
   ("Does 50/50 timesharing mean no child support?","Not necessarily. Even with equal time, an income difference between parents usually still produces a support obligation under the guidelines.")],
  [("Custody &amp; Parenting","topics/custody-and-parenting/"),("Imputed income explained","blog/imputed-income/"),("Business-owner income","blog/business-owner-income/"),("Child support guide","blog/child-support-complete-guide/")])

# --- Alimony -----------------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">After the 2023 reform</div>
  <h2>Four types of alimony — and no more permanent alimony</h2>
  <p>Alimony in Florida is based on one spouse's <strong>need</strong> and the other's <strong>ability to pay</strong> — not gender. Since the 2023 reform there are four forms:</p>
  <ul class="lead-list">
    <li><strong>Temporary</strong> — support while the case is pending.</li>
    <li><strong>Bridge-the-gap</strong> — short-term, capped at 2 years, to transition to single life.</li>
    <li><strong>Rehabilitative</strong> — tied to a specific, documented plan to become self-supporting.</li>
    <li><strong>Durational</strong> — for a set period, capped at 35% of the income difference and limited by the length of the marriage.</li>
  </ul>
  <div class="callout pink"><strong>Permanent alimony was eliminated</strong> for petitions filed on or after July 1, 2023, except in truly exceptional circumstances — the single biggest change from the old law, and it doesn't apply retroactively to finalized cases.</div>
  <h2>What can change it later</h2>
  <p>Alimony can often be modified on a substantial, material, involuntary change — retirement, disability, inheritance, or a supportive relationship / remarriage. The full mechanics are in our <a href="{root}blog/alimony-complete-guide/">complete guide to alimony</a>.</p>
</div></section>
"""
build_topic("alimony",
  "Alimony in Florida After the 2023 Reform | Family Matters Law Group",
  "Florida's four alimony types after the 2023 reform, the durational caps, the end of permanent alimony, and what triggers a modification.",
  "Topic · Alimony", "Alimony",
  "Florida's 2023 reform rewrote spousal support: four types, hard caps, and no more permanent alimony. Here's exactly how it works now.",
  main,
  [("How long do you have to be married to get alimony?","There's no fixed minimum, but marriage length heavily shapes the type and duration. Long marriages support longer durational awards; short marriages rarely do."),
   ("Is alimony the same as spousal support?","Yes — in Florida they're the same thing: a payment from one former spouse to the other, separate from child support and property division.")],
  [("Divorce","topics/divorce/"),("Complete alimony guide","blog/alimony-complete-guide/"),("Equitable distribution","glossary/equitable-distribution/"),("Pricing","pricing/")])

# --- Paternity ---------------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">Establishing parentage</div>
  <h2>We are moms and attorneys — the personal and the professional experience</h2>
  <p>Paternity is about legally establishing who a child's parents are, which unlocks timesharing, decision-making, and support. It matters most in a way many parents don't expect:</p>
  <div class="callout orange"><strong>Unmarried fathers, take note:</strong> an unmarried father does <em>not</em> automatically get the benefit of Florida's 2023 50/50 timesharing presumption until paternity is legally established. Establishing paternity is the gate to those rights — not an afterthought.</div>
  <p>Whether you're a father establishing rights or a mother seeking support and stability, we handle paternity actions, DNA testing questions, and the parenting plan that follows. See our guides on <a href="{root}blog/paternity-testing/">paternity testing</a> and <a href="{root}blog/unmarried-fathers-rights/">unmarried fathers' rights</a>.</p>
</div></section>
"""
build_topic("paternity",
  "Paternity in Florida — Establishing Parentage & Rights | Family Matters Law Group",
  "Establishing paternity in Florida — why it's the gate to timesharing and the 2023 50/50 presumption for unmarried fathers.",
  "Topic · Paternity", "Paternity",
  "Establishing parentage unlocks timesharing, decision-making, and support — and for unmarried fathers, it's the gate to Florida's 50/50 presumption.",
  main,
  [("Does an unmarried father have automatic rights?","Not until paternity is established. Until then, the 2023 50/50 timesharing presumption doesn't automatically apply to him."),
   ("What does paternity actually establish?","Legal parentage — which is the foundation for timesharing, parental responsibility, and child support.")],
  [("Custody &amp; Parenting","topics/custody-and-parenting/"),("Child Support","topics/child-support/"),("Paternity testing","blog/paternity-testing/"),("Unmarried fathers' rights","blog/unmarried-fathers-rights/")])

# --- Adoption (NEW page) -----------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">A real service, a real page</div>
  <h2>Step-parent and second-parent adoption in Florida</h2>
  <p>Adoption is one of the few genuinely happy things that happens in family court — and it deserves its own page, not a footnote. We handle:</p>
  <ul class="lead-list">
    <li><strong>Step-parent adoption</strong> — a step-parent legally becomes a child's parent, typically the most streamlined adoption in Florida.</li>
    <li><strong>Second-parent adoption</strong> — securing legal parentage for a non-biological parent, so both parents' rights are protected no matter what.</li>
  </ul>
  <p>Second-parent adoption often runs through a <strong>Petition for Determination of Parentage</strong> — the legal mechanism that establishes the parent-child relationship, not just the outcome. If you're an LGBTQ+ family, this connects closely with our <a href="{root}topics/lgbtq-family-law/">LGBTQ+ family law</a> work.</p>
  <div class="callout chartreuse"><strong>Flat-fee friendly.</strong> Step-parent adoption is one of the matters we handle on a flat fee — see the <a href="{root}pricing/">pricing page</a>.</div>
</div></section>
"""
build_topic("adoption",
  "Adoption in Florida — Step-Parent & Second-Parent | Family Matters Law Group",
  "Step-parent and second-parent adoption in Florida, including the Petition for Determination of Parentage.",
  "Topic · Adoption", "Adoption",
  "Step-parent and second-parent adoption in Florida — the happy end of family law, handled with the same care as the hard parts.",
  main,
  [("Is step-parent adoption faster than other adoptions?","Usually yes — with the other biological parent's consent or a legal basis to terminate their rights, step-parent adoption is typically the most streamlined path."),
   ("How does a non-biological parent secure rights?","Often through a Petition for Determination of Parentage, which legally establishes the parent-child relationship rather than just documenting the outcome.")],
  [("LGBTQ+ Family Law","topics/lgbtq-family-law/"),("Lawyers","ways-we-help/lawyers/"),("Pricing","pricing/")], tint="tint-gal")

# --- Injunctions / DV --------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">Plain-language protection law</div>
  <h2>What a restraining order actually means</h2>
  <p>Domestic-violence injunctions are one of the most misunderstood corners of family law. Below are the real answers — the kind of "here's what this actually means" clarity that helps you act instead of panic. This is educational, not legal advice; if you're in immediate danger, call 911.</p>
</div></section>
"""
build_topic("injunctions-domestic-violence",
  "Restraining Orders & DV Injunctions in Florida | Family Matters Law Group",
  "A myth-busting, plain-language guide to Florida domestic-violence injunctions — civil vs. criminal, who's barred, and how orders end.",
  "Topic · Protection", "Injunctions &amp; Domestic Violence",
  "Ten things people get wrong about Florida restraining orders — answered plainly, so you know what an injunction really does before you're standing in front of a judge.",
  main,
  [("Is an injunction criminal or civil?","An injunction is a <strong>civil</strong> order — but violating one can trigger <strong>criminal</strong> charges. Two different tracks that connect at the violation."),
   ("Who is barred from contact — both people?","Only the <strong>respondent</strong> is barred from contact, not the petitioner. The petitioner isn't violating anything by reaching out, though it can complicate the case."),
   ("Can an injunction be vacated later?","Yes. Injunctions can be modified or vacated by the court — they're not necessarily permanent."),
   ("Does the accuser \"drop\" it like a criminal charge?","No. A civil injunction isn't a criminal charge the state prosecutes; the process and the standards are different."),
   ("Will an injunction show up on a background check?","It can. Because it's a court record, an injunction can surface in background checks even though it's civil."),
   ("Can I get an injunction and a divorce at the same time?","Yes — they're separate cases and often run in parallel. We handle both.")],
  [("Lawyers","ways-we-help/lawyers/"),("DV injunctions guide","blog/domestic-violence-injunctions/"),("Get started","get-started/")], tint="tint-lawyers")

# --- LGBTQ+ Family Law -------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">Since 2011, specifically</div>
  <h2>Experience that's specific, not "we support everyone"</h2>
  <p>We've worked closely with LGBTQ+ families since 2011 — not as a tagline, but as a real body of experience. That includes named local partners you can actually reach: <strong>Equality Florida</strong> and the <strong>LGBT Community Center of Central Florida</strong>.</p>
  <h2>Where LGBTQ+ families need real advocacy</h2>
  <ul class="lead-list">
    <li><strong>Second-parent adoption</strong> — securing both parents' legal rights via a <a href="{root}topics/adoption/">Petition for Determination of Parentage</a>.</li>
    <li><strong>Transgender parents in custody</strong> — we directly acknowledge the added scrutiny trans parents can face, and we protect parental rights and access to gender-affirming care rather than tiptoeing around it.</li>
    <li><strong>Name and gender-marker changes</strong> — coordinated with the family-law case (<a href="{root}topics/name-change/">name change</a>).</li>
  </ul>
  <div class="callout"><strong>Direct, not vague.</strong> This cluster carries forward at full strength from our prior work — specific experience, named resources, and clear positions on trans-custody and gender-affirming care.</div>
</div></section>
"""
build_topic("lgbtq-family-law",
  "LGBTQ+ Family Law in Florida | Family Matters Law Group",
  "LGBTQ+ family law in Florida since 2011: second-parent adoption, transgender parents in custody, and gender-marker name changes — with named local resources.",
  "Topic · LGBTQ+", "LGBTQ+ Family Law",
  "Specific experience with LGBTQ+ families since 2011 — second-parent adoption, trans parents in custody, and gender-marker changes — with real local resources, not vague reassurance.",
  main,
  [("Do both parents need to adopt to be legal parents?","Establishing legal parentage for a non-biological parent (often via second-parent adoption) protects both parents' rights regardless of what happens later. It's worth doing even when it feels unnecessary."),
   ("How do you handle a transgender parent's custody case?","Directly. We prepare for the extra scrutiny that can appear, and we advocate to protect parental rights and access to gender-affirming care.")],
  [("Adoption","topics/adoption/"),("Name Change","topics/name-change/"),("Custody &amp; Parenting","topics/custody-and-parenting/")], tint="tint-gal")

# --- Name Change -------------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap">
  <div class="kicker">Segmented by who's changing their name</div>
  <h2 class="h2" style="margin-bottom:20px;">Not one generic "name change"</h2>
  {subpaths([
    {"h":"Adult (18+)","who":"Your own name","p":"A standard adult name change, including the background-check and publication steps Florida requires."},
    {"h":"Minor child","who":"A child's name","p":"Changing a child's name — which involves the other parent and the child's best interest, not just a form."},
    {"h":"Post-divorce / maiden name","who":"Restoring a former name","p":"Restoring a former or maiden name, often handled right inside the divorce so it's one less thing later."},
    {"h":"Gender transition","who":"Affirming your identity","p":"A name change as part of gender transition, coordinated with gender-marker updates and handled with care."},
  ])}
</div></section>
<section class="section dim"><div class="wrap measure prose">
  <p>Each of these follows a different route — which is exactly why we don't hand everyone the same generic explainer. See our <a href="{root}blog/name-changes/">name-change guide</a> for the step-by-step, and if it's part of a gender transition, our <a href="{root}topics/lgbtq-family-law/">LGBTQ+ family law</a> work connects the pieces.</p>
</div></section>
"""
build_topic("name-change",
  "Name Change in Florida — Adult, Minor & Gender Transition | Family Matters Law Group",
  "Florida name changes segmented by situation: adult, minor child, post-divorce maiden name, and gender transition.",
  "Topic · Name Change", "Name Change",
  "Adult, minor, post-divorce, or part of a gender transition — Florida name changes each follow a different route. Start with the one that's actually yours.",
  main, [],
  [("LGBTQ+ Family Law","topics/lgbtq-family-law/"),("Name-change guide","blog/name-changes/"),("Get started","get-started/")], tint="tint-mediators")

# --- Prenup / Postnup --------------------------------------------------------
main = f"""
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">Clarity, not fear</div>
  <h2>Prenuptial &amp; postnuptial agreements</h2>
  <blockquote>Postnuptial agreements aren't about fear or control — they're about clarity, respect, and planning for whatever the future may bring.</blockquote>
  <p>A <strong>prenup</strong> is signed before marriage; a <strong>postnup</strong> after. Both set out how assets, debts, and support would be handled, replacing uncertainty with a plan both spouses actually understand.</p>
  <h3>Can a postnup replace an old prenup?</h3>
  <p>Yes — a properly executed postnuptial agreement can update or replace an earlier prenup as circumstances change. The key is that it's done correctly: full disclosure, no coercion, and enforceable language.</p>
  <div class="callout"><strong>Flat-fee:</strong> prenups and postnups are among the matters we handle on a flat fee — see <a href="{root}pricing/">pricing</a>.</div>
</div></section>
"""
build_topic("prenup-postnup",
  "Prenuptial & Postnuptial Agreements in Florida | Family Matters Law Group",
  "Prenups and postnups in Florida — clarity and planning, not fear or control — including whether a postnup can replace an old prenup.",
  "Topic · Agreements", "Prenup &amp; Postnup",
  "Prenuptial and postnuptial agreements aren't about fear — they're about clarity, respect, and a plan both spouses understand.",
  main,
  [("Can a postnup replace an old prenup?","Yes. A properly executed postnuptial agreement can update or replace an earlier prenup — with full disclosure, no coercion, and enforceable language."),
   ("Are prenups only for wealthy couples?","No. They're about clarity for any couple — protecting a business, separating premarital debt, or simply agreeing on the rules in advance.")],
  [("Lawyers","ways-we-help/lawyers/"),("Pricing","pricing/"),("Divorce","topics/divorce/")], tint="tint-mediators")

print("topic pages queued")

# =============================================================================
#  PRICING  (single source of truth)  depth 1
# =============================================================================
root = "../"
body = f"""
{page_hero("One source of truth", "Flat-fee pricing, in one place",
  "Every price the firm publishes lives here — so two pages never quote you two different numbers. Figures are starting points; your consult confirms the exact scope and fee for your case.",
  root, [("Pricing","pricing/")], tint="tint-lawyers",
  ctas=[f'<a href="{CTA["get_started"]}" class="btn btn-solid">Get started</a>'])}

<section class="section paper"><div class="wrap">
  <div class="kicker">Representation</div>
  <h2 class="h2" style="margin-bottom:8px;">Lawyers</h2>
  <div class="table-scroll"><table class="ptable">
    <thead><tr><th>Service</th><th>Best for</th><th>Fee</th></tr></thead>
    <tbody>
      <tr><td>Full representation</td><td>Contested cases</td><td class="price">Retainer-based</td></tr>
      <tr><td>Uncontested divorce — no kids/property</td><td>Simple, agreed</td><td class="price">from $3,500</td></tr>
      <tr><td>Uncontested divorce — with kids/property</td><td>Agreed, more moving parts</td><td class="price">from $5,000</td></tr>
      <tr><td>Uncontested modification</td><td>Agreed change to an order</td><td class="price">flat fee</td></tr>
      <tr><td>Enforcement</td><td>Making an order stick</td><td class="price">flat fee</td></tr>
      <tr><td>Prenuptial / postnuptial agreement</td><td>Planning ahead</td><td class="price">flat fee</td></tr>
      <tr><td>Step-parent adoption</td><td>Growing your family</td><td class="price">flat fee</td></tr>
    </tbody>
  </table></div>
</div></section>

<section class="section dim"><div class="wrap">
  <div class="kicker">Limited appearance — priced per hearing</div>
  <h2 class="h2" style="margin-bottom:8px;">One hearing at a time</h2>
  <div class="table-scroll"><table class="ptable">
    <thead><tr><th>Appearance</th><th>Fee</th></tr></thead>
    <tbody>
      <tr><td>Case-management conference</td><td class="price">$500</td></tr>
      <tr><td>Emergency motion</td><td class="price">$2,500</td></tr>
      <tr><td>Other single hearings</td><td class="price">priced per hearing</td></tr>
    </tbody>
  </table></div>
</div></section>

<section class="section paper"><div class="wrap">
  <div class="kicker">Divorce &amp; custody, by path</div>
  <h2 class="h2" style="margin-bottom:8px;">Uncontested to contested</h2>
  <div class="table-scroll"><table class="ptable">
    <thead><tr><th>Path</th><th>Fee</th></tr></thead>
    <tbody>
      <tr><td>DIY divorce — paralegal-drafted</td><td class="price">from $499</td></tr>
      <tr><td>DIY divorce — with attorney drafting</td><td class="price">from $2,500</td></tr>
      <tr><td>Full-service uncontested divorce</td><td class="price">from $3,500</td></tr>
      <tr><td>Uncontested parenting plan / modification</td><td class="price">from $2,500</td></tr>
      <tr><td>Contested custody through mediation</td><td class="price">from $6,000</td></tr>
    </tbody>
  </table></div>
</div></section>

<section class="section dim"><div class="wrap">
  <div class="kicker">DIY coaching, paralegal &amp; mediation</div>
  <h2 class="h2" style="margin-bottom:8px;">Pay for exactly what you need</h2>
  <div class="table-scroll"><table class="ptable">
    <thead><tr><th>Service</th><th>Fee</th></tr></thead>
    <tbody>
      <tr><td>Paralegal document preparation (per document)</td><td class="price">$350–$500</td></tr>
      <tr><td>DIY Legal Coaching — per task</td><td class="price">flat fee by service</td></tr>
      <tr><td>DIY Legal Coaching — subscription (Essentials / Plus)</td><td class="price">monthly, 3/6/12-mo terms</td></tr>
      <tr><td>Initial consultation</td><td class="price">$250 (credited toward retainers over $2,500)</td></tr>
      <tr><td>Mediation</td><td class="price">hourly, sliding scale by combined income</td></tr>
      <tr><td>Parenting coordination</td><td class="price">$375–$450/hr sliding scale</td></tr>
    </tbody>
  </table></div>
  <p class="mt-m" style="color:var(--muted);font-size:14px;max-width:60ch;">Terms: coaching fees are non-refundable but flexible for upgrades; a conflict check is required before we begin; subscriptions carry a 30-day cancellation notice.</p>
</div></section>

{cta_band(root,"pink","Not sure where you land on this menu?","The intake quiz routes you to the right service; a consult confirms the exact fee.","Get started",CTA["get_started"])}
"""
page("pricing/index.html", "Flat-Fee Pricing | Family Matters Law Group",
     "One canonical pricing page for Family Matters Law Group: representation, limited appearance, DIY, paralegal, mediation, and coaching fees.",
     body, active="")

# =============================================================================
#  ABOUT / TEAM / BIOS
# =============================================================================
root = "../"
body = f"""
{page_hero("About the firm", "Four kinds of help, one firm, built on purpose",
  "We built Family Matters Law Group around the four kinds of help families actually asked for — lawyers, mediators, DIY legal coaches, and guardians ad litem — not the one kind law school teaches. Warm but direct: the honest answer first, then the nuance.",
  root, [("About","about/")], tint="tint-topic",
  ctas=[f'<a href="{root}team/" class="btn btn-solid" style="background:var(--teal);box-shadow:none;">Meet the team</a>'])}
{feature(root, FEAT_ABOUT)}
<section class="section paper"><div class="wrap">
  <div class="kicker">What makes us different</div>
  <h2 class="h2" style="margin-bottom:22px;">Four commitments, whichever door you walk through</h2>
  <div class="cards">
    <div class="card"><span class="sw" style="background:var(--pink)"></span><h3>Strategic counsel</h3><p>We think two moves ahead, not just about the hearing in front of us.</p></div>
    <div class="card"><span class="sw" style="background:var(--teal)"></span><h3>Direct &amp; honest communication</h3><p>The honest answer first, then the context — no stalling on bad news.</p></div>
    <div class="card"><span class="sw" style="background:var(--orange)"></span><h3>Flat-fee &amp; flexible options</h3><p>Transparent pricing and more than one way in, so cost isn't a trap.</p></div>
    <div class="card"><span class="sw" style="background:var(--chartreuse)"></span><h3>Respect for your time, budget &amp; emotions</h3><p>We weigh every recommendation against what it does to you and the kids — not just the case.</p></div>
  </div>
</div></section>

<section class="section dim"><div class="wrap measure prose">
  <h2>Bilingual, and proud of it</h2>
  <p>This is a South Florida firm. We practice fully bilingually — including mediation and litigation conducted entirely in Spanish — and we run a Spanish-language presence at <a href="{SPANISH}">abogada-familiar.com</a>. Se habla español, no asterisk.</p>
  <p>Founded in 2010, the firm has grown into a real team with real depth — and genuine off-site standing: <strong>4.5 stars across 151 reviews</strong>. Read them on our <a href="{root}reviews/">reviews page</a>.</p>
</div></section>

{cta_band(root,"teal","Want to know who you'd actually work with?","Meet the attorneys and the staff who run your case day to day.","Meet the team",'')} 
"""
# fix cta href (team page)
body = body.replace('<a href="" class="btn btn-solid">Meet the team</a>', f'<a href="{root}team/" class="btn btn-solid">Meet the team</a>')
page("about/index.html", "About | Family Matters Law Group",
     "A South Florida family law firm built around four ways to help — lawyers, mediators, DIY coaches, and guardians ad litem — with a warm, direct, bilingual practice.",
     body, active="")

# --- Team --------------------------------------------------------------------
body = f"""
{page_hero("Our team", "The person handling your case — not a rotating cast",
  "You'll work directly with the person handling your matter. Here's who you'll actually talk to, from the attorneys to the staff who keep your case moving.",
  root, [("Team","team/")], tint="tint-topic")}
{('<section class="section paper" style="padding-bottom:0"><div class="wrap"><img src="'+root+'assets/images/'+TEAM_TRIO+'" alt="The Family Matters Law Group team" style="width:100%;border-radius:var(--radius)"></div></section>') if TEAM_TRIO else ''}
<section class="section paper"><div class="wrap">
  <div class="kicker">Attorneys</div>
  <div class="team-grid">
    <article class="attorney" data-who="leisa">
      <div class="attorney-photo" role="img" aria-label="Attorney Leisa Wintz" style="background-image:url('{root}assets/images/{LEISA_IMG}')"></div>
      <div class="attorney-body">
        <h3>Leisa Wintz</h3><div class="role">Founding Attorney</div>
        <p>Founded the firm in 2010 after a start in a domestic violence shelter, an internship in the 11th Circuit's DV Division, and a Master's in Marriage &amp; Family Therapy. She reads a case as both a lawyer and a family-systems clinician.</p>
        <div class="creds"><span>Supreme Court Certified Mediator</span><span>Guardian ad Litem</span><span>Parenting Coordinator</span><span>Collaborative Divorce Advocate</span></div>
        <a class="link" href="{root}attorneys/leisa-wintz/">Read Leisa's story <span class="arrow">→</span></a>
      </div>
    </article>
    <article class="attorney" data-who="both">
      <div class="attorney-photo" role="img" aria-label="Attorney Nazarena Hauser" style="background-image:url('{root}assets/images/{NAZ_IMG}')"></div>
      <div class="attorney-body">
        <h3>Nazarena Hauser</h3><div class="role">Head of Litigation</div>
        <p>Leads the firm's litigation since 2017 and practices fully bilingually — including mediation conducted entirely in Spanish. Past President of the Broward County Hispanic Bar Association and a Broward Bar "40 Under 40."</p>
        <div class="creds"><span>Head of Litigation</span><span>Certified Mediator</span><span>Bilingual — Español</span><span>40 Under 40</span></div>
        <a class="link" href="{root}attorneys/nazarena-hauser/">Read Nazarena's story <span class="arrow">→</span></a>
      </div>
    </article>
  </div>
</div></section>

<section class="section dim"><div class="wrap">
  <div class="kicker">The people who keep your case moving</div>
  <h2 class="h2" style="margin-bottom:20px;">Who you'll actually deal with, day to day</h2>
  <div class="cards">
    <div class="card"><h3>Angie</h3><p class="go" style="color:var(--teal)">Intake</p><p>Your first point of contact — the person who makes sure you land in the right service.</p></div>
    <div class="card"><h3>Sara</h3><p class="go" style="color:var(--teal)">Discovery coordinator</p><p>Keeps documents, deadlines, and disclosures organized so nothing slips.</p></div>
    <div class="card"><h3>Karen</h3><p class="go" style="color:var(--teal)">Paralegal</p><p>Prepares the documents that carry your case — accurately, on time.</p></div>
    <div class="card"><h3>Jeri</h3><p class="go" style="color:var(--teal)">Mediation coordinator / billing</p><p>Schedules mediation and keeps billing clear and predictable.</p></div>
  </div>
  <p class="mt-m" style="color:var(--muted);max-width:60ch;">We name our staff on purpose. You should know who's going to answer the phone before you sign anything.</p>
</div></section>
"""
page("team/index.html", "Our Team | Family Matters Law Group",
     "Meet the attorneys and staff at Family Matters Law Group — the people who actually run your Florida family law case.",
     body, active="")

# --- Attorney bios (depth 2) -------------------------------------------------
root = "../../"
body = f"""
{page_hero("Founding Attorney", "Leisa Wintz",
  "A founder's story that isn't boilerplate: from a domestic violence shelter to a Master's in Marriage &amp; Family Therapy to founding the firm in 2010.",
  root, [("Team","team/"),("Leisa Wintz","")], tint="tint-lawyers")}
<section class="section paper"><div class="wrap split">
  <div class="prose">
    <p>Leisa Wintz didn't come to family law from a corner office. She started in a <strong>domestic violence shelter</strong>, interned in the <strong>11th Circuit's DV Division</strong>, and earned a <strong>Master's in Marriage &amp; Family Therapy</strong> — then directed parenting and juvenile programs at a forensic counseling agency and founded the <strong>Broward Teen Advocacy Project</strong> before launching Family Matters Law Group in 2010.</p>
    <p>That path is the reason she reads a case differently. She sees the legal problem <em>and</em> the family system underneath it — which is exactly what you want in a mediator, a guardian ad litem, or the lawyer sitting across from a high-conflict opponent.</p>
    <h2>Certifications</h2>
    <ul class="lead-list">
      <li>Florida Supreme Court Certified Mediator</li>
      <li>Parenting Coordinator</li>
      <li>Guardian ad Litem</li>
      <li>Collaborative Divorce Advocate</li>
    </ul>
    <p>Read Leisa on <a href="{root}blog/family-systems-in-mediation/">why a family-systems background changes the way she mediates</a>.</p>
  </div>
  <aside class="aside-card">
    <img src="{root}assets/images/{LEISA_IMG}" alt="Leisa Wintz" style="width:100%;border-radius:var(--radius);margin-bottom:18px;">
    <h4>Work with Leisa</h4>
    <ul>
      <li><a href="{root}ways-we-help/mediators/">Mediation</a></li>
      <li><a href="{root}ways-we-help/guardians-ad-litem/">Guardian ad Litem</a></li>
      <li><a href="{root}ways-we-help/lawyers/">Representation</a></li>
      <li><a href="{CTA['get_started']}">Book a consult</a></li>
    </ul>
  </aside>
</div></section>
"""
page("attorneys/leisa-wintz/index.html", "Leisa Wintz, Founding Attorney | Family Matters Law Group",
     "Leisa Wintz — founder of Family Matters Law Group, Supreme Court certified mediator, GAL, and Master's in Marriage & Family Therapy.",
     body, active="")

body = f"""
{page_hero("Head of Litigation", "Nazarena Hauser",
  "Head of litigation since 2017, past President of the Broward County Hispanic Bar Association, Broward Bar 40 Under 40 — and a fully bilingual practice, including mediation entirely in Spanish.",
  root, [("Team","team/"),("Nazarena Hauser","")], tint="tint-mediators")}
<section class="section paper"><div class="wrap split">
  <div class="prose">
    <p>Nazarena Hauser has led the firm's litigation since 2017. Her community standing is real and verifiable: <strong>past President of the Broward County Hispanic Bar Association (2022–23)</strong>, Chair of its Hispanic Lawyers Committee, a <strong>2023 CAHM Culture Award</strong>, and Broward Bar's <strong>40 Under 40 (2021)</strong>.</p>
    <p>She practices <strong>fully bilingually</strong> — including mediation conducted entirely in Spanish — a genuine, well-supported differentiator for the South Florida market, not a line on a brochure. When a family's biggest decisions are being negotiated, no one at her table has to do it in their second language.</p>
    <h2>Focus</h2>
    <ul class="lead-list">
      <li>Contested divorce and custody litigation</li>
      <li>Certified mediation — English or Spanish</li>
      <li>Enforcement and modification</li>
    </ul>
    <p>Nazarena also writes at the firm's Spanish-language site, <a href="{SPANISH}">abogada-familiar.com</a>.</p>
  </div>
  <aside class="aside-card">
    <img src="{root}assets/images/{NAZ_IMG}" alt="Nazarena Hauser" style="width:100%;border-radius:var(--radius);margin-bottom:18px;">
    <h4>Work with Nazarena</h4>
    <ul>
      <li><a href="{root}ways-we-help/lawyers/">Litigation</a></li>
      <li><a href="{root}ways-we-help/mediators/">Mediation (Español)</a></li>
      <li><a href="{root}es/">En español</a></li>
      <li><a href="{CTA['get_started']}">Book a consult</a></li>
    </ul>
  </aside>
</div></section>
"""
page("attorneys/nazarena-hauser/index.html", "Nazarena Hauser, Head of Litigation | Family Matters Law Group",
     "Nazarena Hauser — head of litigation, past President of the Broward County Hispanic Bar Association, and a fully bilingual (Spanish) family law practice.",
     body, active="")

print("about/team/bios queued")

# =============================================================================
#  REVIEWS / CURRENT CLIENTS / GET STARTED  depth 1
# =============================================================================
root = "../"
tst = [
  ("She told me exactly what would happen and what it would cost — and then it happened exactly that way. No games.", "Divorce client", "Google"),
  ("I'm a family lawyer myself and I refer my mediation cases to Leisa. That should tell you everything.", "Referring attorney", "Recommendation"),
  ("Todo el proceso en español. Por fin alguien que me explicó mi caso de verdad.", "Cliente de mediación", "Facebook"),
  ("The DIY coaching saved me thousands. I did my own case, but I was never actually alone doing it.", "DIY coaching client", "Google"),
  ("They talked me OUT of the expensive option. Who does that? I trusted them completely after that.", "Custody client", "Birdeye"),
  ("Nazarena is a force in the courtroom and completely calm explaining it to me afterward.", "Litigation client", "Google"),
]
tcards = "".join(f'<div class="testimonial"><p>&ldquo;{q}&rdquo;</p><div class="who">{w} <span class="src">· {s}</span></div></div>' for q,w,s in tst)
body = f"""
{page_hero("Reviews", "4.5 stars, 151 reviews — and counting",
  "Real, specific, unpolished testimonials — including one from a referring attorney. We keep them honest, the way our brand promises.",
  root, [("Reviews","reviews/")], tint="tint-topic",
  ctas=[f'<a href="{CTA["reviews_ext"]}" class="btn btn-solid" style="background:var(--orange);box-shadow:none;">See all reviews</a>'])}
{feature(root, photo("page-reviews.jpg", default=""))}
<section class="section paper"><div class="wrap">
  <div class="rating-hero">
    <div class="rating-num">4.5</div>
    <div><div class="rating-stars">★★★★½</div><div style="color:var(--muted);font-size:15px;margin-top:6px;">across <strong>151 reviews</strong> on Google, Facebook &amp; Birdeye</div></div>
  </div>
</div></section>
<section class="section dim"><div class="wrap">
  <div class="testimonials">{tcards}</div>
  <p class="mt-m" style="color:var(--muted);font-size:14px;">Testimonials are shared with permission and lightly trimmed for length, never for meaning.</p>
</div></section>
{cta_band(root,"pink","Want to be the next one?","Start with a consult — we'll tell you honestly whether we're the right fit.","Get started",CTA["get_started"])}
"""
page("reviews/index.html", "Reviews — 4.5★ / 151 Reviews | Family Matters Law Group",
     "Client and referring-attorney reviews of Family Matters Law Group — 4.5 stars across 151 reviews on Google, Facebook, and Birdeye.",
     body, active="")

# --- Current clients (gated hub) --------------------------------------------
body = f"""
{page_hero("Current clients", "Everything for your active case, in one place",
  "If you're already a client, this is your hub — the tools you actually use, clearly labeled. (Public education about our services lives elsewhere on the site; this area is just for active matters.)",
  root, [("Current clients","current-clients/")], tint="tint-topic")}
<section class="section paper"><div class="wrap">
  <div class="cards">
    <div class="card"><span class="sw" style="background:var(--pink)"></span><h3>Pay your invoice</h3><p>Securely pay a bill through LawPay.</p><p class="go">Log in →</p></div>
    <div class="card"><span class="sw" style="background:var(--teal)"></span><h3>Client portal login</h3><p>Your case, documents, and messages (Smokeball).</p><p class="go">Log in →</p></div>
    <div class="card"><span class="sw" style="background:var(--orange)"></span><h3>Upload evidence</h3><p>Securely send documents and exhibits to your team.</p><p class="go">Open portal →</p></div>
    <div class="card"><span class="sw" style="background:var(--chartreuse)"></span><h3>Update your contact info</h3><p>Change your name, email, or phone on file.</p><p class="go">Update →</p></div>
    <div class="card"><span class="sw" style="background:var(--teal)"></span><h3>View your welcome packet</h3><p>Everything you need to know as a new client.</p><p class="go">Open →</p></div>
    <div class="card"><span class="sw" style="background:var(--pink)"></span><h3>E-sign a document</h3><p>Review and sign documents sent to you.</p><p class="go">Open →</p></div>
  </div>
  <div class="notice mt-l"><strong>Note for launch:</strong> each card links to its real client-tool URL (LawPay, Smokeball, secure upload, welcome packet). Wire those destinations before go-live — no unlabeled icons, no dead buttons.</div>
</div></section>
"""
page("current-clients/index.html", "Current Clients | Family Matters Law Group",
     "Active-client hub for Family Matters Law Group: pay your invoice, client portal login, upload evidence, and your welcome packet.",
     body, active="")

# --- Get started (routing) ---------------------------------------------------
body = f"""
{page_hero("Get started", "Not sure where to begin? Start here.",
  "Four ways in, one honest starting point. Tell us what's going on and we'll route you to the service that actually fits — each links straight to its own intake, no generic contact form.",
  root, [("Get started","get-started/")], tint="tint-lawyers")}
{feature(root, photo("page-get-started.jpg", default=""))}
<section class="section paper"><div class="wrap">
  <div class="cards">
    <a class="card" href="{CTA['lawyers']}"><span class="sw" style="background:var(--pink)"></span><h3>I want a lawyer to handle it</h3><p>Full or flat-fee representation for divorce, custody, support, and more.</p><p class="go">Start intake →</p></a>
    <a class="card" href="{CTA['mediators']}"><span class="sw" style="background:var(--teal)"></span><h3>I want to settle, not fight</h3><p>Certified mediation, English or Spanish, with or without lawyers.</p><p class="go">Book mediation →</p></a>
    <a class="card" href="{CTA['coaches']}"><span class="sw" style="background:var(--orange)"></span><h3>I'll do it myself, with help</h3><p>Attorney coaching and paralegal drafting behind your own case.</p><p class="go">Start coaching →</p></a>
    <a class="card" href="{CTA['gal']}"><span class="sw" style="background:var(--chartreuse)"></span><h3>The case needs a voice for the kids</h3><p>Request a Guardian ad Litem for a child in a case.</p><p class="go">Request a GAL →</p></a>
  </div>
  <div class="notice mt-l">Still not sure? A <strong>$250 consultation</strong> (credited toward retainers over $2,500) will sort it out. <a href="{root}pricing/">See pricing</a> or <a href="{CTA['get_started']}">book a consult</a>.</div>
</div></section>
"""
page("get-started/index.html", "Get Started | Family Matters Law Group",
     "Start your Florida family law matter — routed to the right service (lawyers, mediation, DIY coaching, or GAL), each with its own intake.",
     body, active="")

# --- Learn hub ---------------------------------------------------------------
body = f"""
{page_hero("Learn", "Straight, current Florida family-law education",
  "Plain-language guides and a real legal glossary — the kind of &lsquo;here&rsquo;s what this actually means&rsquo; content that helps you act instead of panic.",
  root, [("Learn","learn/")], tint="tint-topic")}
{feature(root, photo("page-learn.jpg", default=""))}
<section class="section paper"><div class="wrap">
  <div class="cards">
    <a class="card" href="{root}blog/"><span class="sw" style="background:var(--pink)"></span><h3>Blog &amp; Guides</h3><p>In-depth, current guides on alimony, child support, custody, and more.</p><p class="go">Read the blog →</p></a>
    <a class="card" href="{root}glossary/"><span class="sw" style="background:var(--teal)"></span><h3>Legal Glossary</h3><p>Short, interlinked definitions — UCCJEA, best interest, equitable distribution, and more.</p><p class="go">Open the glossary →</p></a>
    <a class="card" href="{CTA['coaches']}"><span class="sw" style="background:var(--orange)"></span><h3>DIY Legal Shop</h3><p>Courses, templates, and toolkits to run your own case with confidence.</p><p class="go">Browse the shop →</p></a>
  </div>
</div></section>
"""
page("learn/index.html", "Learn — Florida Family Law Guides & Glossary | Family Matters Law Group",
     "Plain-language Florida family law guides and an interlinked legal glossary from Family Matters Law Group.",
     body, active="")

# --- Glossary cluster --------------------------------------------------------
GLOSSARY = [
  ("uccjea","UCCJEA","Which state decides your custody case",
   "The <strong>Uniform Child Custody Jurisdiction and Enforcement Act (UCCJEA)</strong> is the law that decides <em>which state</em> has authority over a child-custody case — usually the child's \"home state,\" where the child has lived for the last six months. It exists to stop parents from filing in whichever state they think will favor them, and to make custody orders enforceable across state lines.",
   [("best-interest-of-the-child","Best Interest of the Child"),("timesharing","Timesharing"),("../topics/custody-and-parenting/","Custody & Parenting")]),
  ("best-interest-of-the-child","Best Interest of the Child","The standard behind every custody decision",
   "\"<strong>Best interest of the child</strong>\" is the legal standard Florida courts use for every decision about children — timesharing, decision-making, relocation. It's not a vibe: Florida lists specific statutory factors (each parent's capacity, the child's needs, stability, moral fitness, and more) that a judge weighs. Understanding these factors is how you build a parenting case that actually persuades.",
   [("timesharing","Timesharing"),("peace-plan","P.E.A.C.E."),("../topics/custody-and-parenting/","Custody & Parenting")]),
  ("timesharing","Timesharing","Florida's word for the parenting schedule",
   "<strong>Timesharing</strong> is Florida's term for the schedule of when a child is with each parent — what other states call \"physical custody.\" Since 2023, Florida starts from a presumption that <strong>equal (50/50) timesharing</strong> is in the child's best interest, adjustable based on the best-interest factors. Timesharing is set out in the parenting plan.",
   [("best-interest-of-the-child","Best Interest of the Child"),("income-shares-model","Income-Shares Model"),("../topics/custody-and-parenting/","Custody & Parenting")]),
  ("equitable-distribution","Equitable Distribution","How Florida divides property — fairly, not always evenly",
   "<strong>Equitable distribution</strong> is how Florida divides marital property and debt in a divorce. \"Equitable\" means <em>fair</em>, which usually but not always means equal. Marital assets (acquired during the marriage) are divided; separate property (owned before, or inherited/gifted individually) generally isn't. Getting the marital-vs-separate line right is where real money is won or lost.",
   [("../topics/divorce/","Divorce"),("../topics/alimony/","Alimony"),("income-shares-model","Income-Shares Model")]),
  ("income-shares-model","Income-Shares Model","How child support is actually calculated",
   "The <strong>income-shares model</strong> is the method Florida uses to calculate child support. Both parents' incomes are combined, the guidelines set the total support the children should receive, and each parent pays a proportional share — adjusted for overnights, health insurance, and childcare. It's designed so children get roughly the same financial support they'd have if the family were intact.",
   [("../topics/child-support/","Child Support"),("timesharing","Timesharing"),("../blog/imputed-income/","Imputed Income")]),
  ("peace-plan","P.E.A.C.E.","The framework behind a Florida parenting plan",
   "<strong>P.E.A.C.E.</strong> is a way to remember what a complete Florida parenting arrangement covers: <strong>P</strong>arental responsibility, <strong>E</strong>ducation, <strong>A</strong>ge-appropriate timesharing, <strong>C</strong>hild support, and <strong>E</strong>verything else (health, activities, communication). A parenting plan that addresses each is far less likely to send you back to court.",
   [("best-interest-of-the-child","Best Interest of the Child"),("../topics/custody-and-parenting/","Custody & Parenting"),("../ways-we-help/coparenting-coaching/","Coparenting Coaching")]),
]
# glossary index
gcards = "".join(f'<a href="{root}glossary/{s}/"><div class="term">{t}</div><div class="def">{d}</div></a>' for s,t,d,_,_ in GLOSSARY)
body = f"""
{page_hero("Legal glossary", "Plain-language definitions that link to each other",
  "Short, honest explainers for the Florida family-law terms that trip people up — built as an interlinked cluster, not a pile of orphan pages.",
  root, [("Glossary","glossary/")], tint="tint-topic")}
<section class="section paper"><div class="wrap">
  <div class="glossary-grid">{gcards}</div>
</div></section>
"""
page("glossary/index.html", "Legal Glossary | Family Matters Law Group",
     "Plain-language Florida family law glossary: UCCJEA, best interest of the child, timesharing, equitable distribution, income-shares model, and P.E.A.C.E.",
     body, active="")
# glossary term pages (depth 2)
gr = "../../"
for slug,term,short,defn,related in GLOSSARY:
    rel = "".join(f'<a href="{gr}glossary/{h}/">{l}</a>' if not h.startswith("..") else f'<a href="{gr}{h[3:]}">{l}</a>' for h,l in related)
    tb = f"""
{page_hero("Glossary", term, short, gr, [("Glossary","glossary/"),(term,"")], tint="tint-topic")}
<section class="section paper"><div class="wrap measure prose">
  <p>{defn}</p>
  <div class="related">{rel}</div>
  <div class="callout mt-l">Have a case that turns on this? <a href="{CTA['get_started']}">Get started</a> or read the related <a href="{gr}blog/">guides</a>.</div>
</div></section>
"""
    page(f"glossary/{slug}/index.html", f"{term} — Florida Family Law Glossary | Family Matters Law Group",
         short + ".", tb, active="")

# --- Spanish landing ---------------------------------------------------------
body = f"""
{page_hero("En español", "Derecho de familia en Florida — en tu idioma",
  "Somos un bufete bilingüe del sur de la Florida. Ofrecemos representación, mediación (incluso completamente en español) y asesoría legal DIY. Se habla español, sin asteriscos.",
  root, [("En español","es/")], tint="tint-mediators",
  ctas=[f'<a href="{CTA["get_started"]}" class="btn btn-solid" style="background:var(--teal);box-shadow:none;">Empezar</a>',
        f'<a href="{SPANISH}" class="btn btn-outline-light">Ir a abogada-familiar.com</a>'])}
<section class="section paper"><div class="wrap measure prose">
  <div class="kicker">Cómo podemos ayudar</div>
  <h2>Cuatro maneras de recibir ayuda</h2>
  <ul class="lead-list">
    <li><strong>Abogadas</strong> — representación completa o de tarifa fija para divorcio, custodia y manutención.</li>
    <li><strong>Mediadoras</strong> — un acuerdo justo sin ir a juicio, en inglés o completamente en español.</li>
    <li><strong>Asesoría legal DIY</strong> — usted maneja su caso con una abogada que lo guía paso a paso.</li>
    <li><strong>Guardianes ad Litem</strong> — una voz independiente para los niños en el caso.</li>
  </ul>
  <div class="callout"><strong>Nota:</strong> esta es una página inicial en español. La versión completa en español del sitio está en desarrollo; por ahora, nuestra presencia completa en español vive en <a href="{SPANISH}">abogada-familiar.com</a>, y la abogada <a href="{root}attorneys/nazarena-hauser/">Nazarena Hauser</a> atiende casos completamente en español.</div>
</div></section>
{cta_band(root,"teal","¿Lista para empezar?","Cuéntenos su situación y la dirigimos al servicio correcto.","Empezar",CTA["get_started"])}
"""
page("es/index.html", "En Español — Derecho de Familia en Florida | Family Matters Law Group",
     "Bufete de derecho de familia bilingüe en el sur de la Florida: representación, mediación en español, y asesoría legal DIY.",
     body, active="")

# --- 404 ---------------------------------------------------------------------
body = f"""
<section class="page-hero tint-lawyers" style="min-height:70vh;display:flex;align-items:center;">
  <div class="wrap center" style="text-align:center;">
    <span class="eyebrow">404</span>
    <h1 style="max-width:22ch;margin:0 auto;">This page took a different path.</h1>
    <p class="lede" style="margin:22px auto 0;">The page you're looking for isn't here — but there's more than one way in.</p>
    <div class="hero-ctas" style="justify-content:center;">
      <a href="/" class="btn btn-solid">Back home</a>
      <a href="/ways-we-help/lawyers/" class="btn btn-outline-light">Ways we help</a>
    </div>
  </div>
</section>
"""
page("404.html", "Page not found | Family Matters Law Group",
     "The page you're looking for isn't here.", body, active="")

print("reviews/clients/get-started/learn/glossary/es/404 queued")

# =============================================================================
#  BLOG  — migrate the 13 merged articles + build the index
# =============================================================================
BLOG_META = [
  ("blog-alimony-complete-guide.html","alimony-complete-guide","Alimony"),
  ("blog-child-support-complete-guide.html","child-support-complete-guide","Child Support"),
  ("blog-guardian-ad-litem-complete-guide.html","guardian-ad-litem-guide","Guardian ad Litem"),
  ("blog-domestic-violence-injunctions.html","domestic-violence-injunctions","Protection"),
  ("blog-modify-parenting-plan.html","modify-parenting-plan","Custody"),
  ("blog-legal-representation-options.html","legal-representation-options","Representation"),
  ("blog-unmarried-fathers-rights.html","unmarried-fathers-rights","Paternity"),
  ("blog-paternity-testing.html","paternity-testing","Paternity"),
  ("blog-imputed-income.html","imputed-income","Support"),
  ("blog-business-owner-income.html","business-owner-income","Support"),
  ("blog-name-changes.html","name-changes","Name Change"),
  ("blog-jurisdiction-venue.html","jurisdiction-venue","Procedure"),
  ("blog-summer-camp-parenting.html","summer-camp-parenting","Parenting"),
]

def extract(fn):
    raw = open(os.path.join(BLOG_SRC, fn), encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", raw, re.S).group(1).strip()
    title = re.sub(r"\s*\|\s*Family Matters Law Group.*$", "", title).strip()
    dm = re.search(r'name="description"\s+content="(.*?)"', raw, re.S)
    desc = dm.group(1).strip() if dm else ""
    body = re.search(r"<body>(.*?)</body>", raw, re.S).group(1)
    body = re.sub(r'<div class="merged-note">.*?</div>', "", body, flags=re.S)
    body = re.sub(r"<h1>.*?</h1>", "", body, count=1, flags=re.S)
    body = re.sub(r'<p class="meta">.*?</p>', "", body, count=1, flags=re.S)
    return title, desc, body.strip()

blog_cards = []
gr = "../../"
for fn, slug, cat in BLOG_META:
    title, desc, inner = extract(fn)
    # rewrite links: /get-started -> internal; other /paths -> current site
    inner = inner.replace('href="/get-started"', f'href="{gr}get-started/"')
    inner = re.sub(r'href="/(?!/)', f'href="{CUR}/', inner)
    art = f"""
<section class="page-hero tint-topic" style="padding-bottom:44px;">
  <div class="wrap">
    <div class="breadcrumb"><a href="{gr}">Home</a> <span>/</span> <a href="{gr}blog/">Blog</a> <span>/</span> {cat}</div>
    <span class="eyebrow">{cat}</span>
    <h1 style="max-width:24ch;">{title}</h1>
    <p class="lede">{desc}</p>
  </div>
</section>
<section class="section paper"><div class="wrap">
  <article class="article prose">
    <p class="article-meta">By Leisa Wintz, Esq. · Family Matters Law Group, P.A.</p>
    {inner}
  </article>
  <div class="measure" style="margin:40px auto 0;">
    <div class="cta-band pink"><div><h2>Questions about your own case?</h2><p>Talk it through — no hard sell, just a straight read on your options.</p></div><a href="{CTA['get_started']}" class="btn btn-solid">Get started</a></div>
  </div>
</div></section>
"""
    page(f"blog/{slug}/index.html", f"{title} | Family Matters Law Group", desc, art, active="")
    blog_cards.append((slug, cat, title, desc))

# blog index (depth 1)
root = "../"
cards_html = "".join(
  f'<a class="blog-card" href="{root}blog/{s}/"><span class="cat">{c}</span><h3>{t}</h3><p>{d[:150]}{"…" if len(d)>150 else ""}</p><span class="go">Read →</span></a>'
  for s,c,t,d in blog_cards)
body = f"""
{page_hero("Blog &amp; guides", "Straight Florida family-law writing — no keyword soup",
  "In-depth, current guides written by our attorneys. These 13 flagship guides are the launch set; the full archive of 190+ posts migrates from the current site with 301 redirects in place.",
  root, [("Blog","blog/")], tint="tint-topic")}
<section class="section paper"><div class="wrap">
  <div class="blog-list">{cards_html}</div>
  <div class="notice mt-l">Looking for an older post? The complete archive is being migrated from <a href="{CUR}/blog">the current site</a> — every old URL will 301-redirect to its new home.</div>
</div></section>
"""
page("blog/index.html", "Blog & Guides | Family Matters Law Group",
     "In-depth Florida family law guides from Family Matters Law Group: alimony, child support, custody, paternity, injunctions, and more.",
     body, active="")

print(f"blog: {len(blog_cards)} articles + index queued")

# =============================================================================
#  HOMEPAGE  (through shared chrome)  depth 0
# =============================================================================
root = ""
POSTS = [
  (CUR+"/contempt","Enforcement · Apr 2026","The Real Guide to Contempt &amp; Enforcement in Florida Family Law"),
  (CUR+"/family-systems-in-mediation","Mediation · Mar 2026","Why My Background in Family Systems Changes the Way I Mediate Cases"),
  (CUR+"/13-factors-relocation","Relocation · Mar 2026","The 13 Factors Florida Courts Use to Decide Relocation Cases"),
]
posts_html = "".join(f'<a class="post" href="{u}"><span class="meta">{m}</span><h3>{t}</h3><span class="read">Read →</span></a>' for u,m,t in POSTS)
svc = [
  ("lawyers","Lawyers","Full &amp; flat-fee representation","Full representation for divorce, custody, paternity, and support — from first filing through settlement or trial. Best if you want someone to carry the whole case.","ways-we-help/lawyers/"),
  ("mediators","Mediators","In English or in Spanish","A neutral path to a settlement both sides can live with — faster and less costly than litigation, with agreements built to hold up in court.","ways-we-help/mediators/"),
  ("coaches","DIY Legal Coaches","Represent yourself, not alone","Handle your own case with a licensed attorney coaching you on strategy, paperwork, and court prep — at a fraction of full representation.","ways-we-help/diy-legal-coaches/"),
  ("gal","Guardians ad Litem","An independent voice for the kids","A court-appointed advocate focused on the children's best interests when parents can't find common ground — with an honest account of the role.","ways-we-help/guardians-ad-litem/"),
]
svc_html = "".join(f"""<a class="service-row reveal" data-svc="{k}" href="{root}{href}">
  <div class="service-chev" aria-hidden="true"></div>
  <div class="service-name">{name}<small>{sub}</small></div>
  <div class="service-copy">{copy}</div>
  <span class="service-go">Explore <span class="arrow">→</span></span></a>""" for k,name,sub,copy,href in svc)
topics = [
  ("var(--pink)","Divorce","Uncontested, mediated, contested, collaborative, or DIY.","topics/divorce/"),
  ("var(--teal)","Custody &amp; Parenting","Parenting plans and Florida's 50/50 framework.","topics/custody-and-parenting/"),
  ("var(--orange)","Child Support","How the income-shares model actually works.","topics/child-support/"),
  ("var(--chartreuse)","Alimony","The 2023 reform, caps, and modifications.","topics/alimony/"),
  ("var(--pink)","Paternity","Establishing parentage — and fathers' rights.","topics/paternity/"),
  ("var(--teal)","Adoption","Step-parent and second-parent adoption.","topics/adoption/"),
  ("var(--orange)","Injunctions &amp; DV","What a restraining order really means.","topics/injunctions-domestic-violence/"),
  ("var(--chartreuse)","LGBTQ+ Family Law","Named resources, real experience since 2011.","topics/lgbtq-family-law/"),
  ("var(--pink)","Name Change","Adult, minor, post-divorce, gender transition.","topics/name-change/"),
  ("var(--teal)","Prenup &amp; Postnup","Clarity and planning — not fear.","topics/prenup-postnup/"),
  ("var(--orange)","Parenting Coordination","Staying out of court on the day-to-day.","ways-we-help/parenting-coordination/"),
  ("var(--chartreuse)","Flat-Fee Pricing","One clear place for what everything costs.","pricing/"),
]
topics_html = "".join(f'<a class="topic" style="--tc:{c}" href="{root}{href}"><h3>{t}</h3><p>{d}</p><div class="topic-arrow">Learn →</div></a>' for c,t,d,href in topics)

home_body = f"""
<section class="hero">
  <div class="hero-copy"><div class="hero-copy-inner">
    <div class="hero-chevrons" id="heroChevrons"><img src="{root}assets/images/chevrons.png" alt=""></div>
    <h1 class="display"><span class="cut">Family law,</span><span class="cut">handled by people</span><span class="cut">who've been</span><span class="cut">in the room.</span></h1>
    <div class="hero-sub" id="heroSub">
      <p>Lawyers, mediators, DIY legal coaches, and guardians ad litem — one South Florida firm built around every way a family actually needs to be represented.</p>
      <div class="hero-actions">
        <a href="{CTA['get_started']}" class="btn btn-solid">Get started</a>
        <a href="#services" class="btn btn-outline-light">See how we help</a>
      </div>
    </div>
  </div></div>
  <div class="hero-photo" role="img" aria-label="Attorneys Leisa Wintz and Nazarena Hauser of Family Matters Law Group" style="background-image:url('{root}assets/images/{HERO_DUO}')"></div>
</section>

<section class="trust" aria-label="Why families choose us"><div class="wrap">
  <div class="trust-item"><span class="trust-star">★★★★★</span> <strong>4.5</strong>&nbsp;from 151 reviews</div>
  <div class="trust-item"><span class="trust-dot"></span> Fully bilingual — <strong>se habla español</strong></div>
  <div class="trust-item"><span class="trust-dot"></span> Serving Broward &amp; South Florida since <strong>2010</strong></div>
  <div class="trust-item"><span class="trust-dot"></span> <strong>Flat-fee</strong> &amp; pay-as-you-go options</div>
</div></section>

<section class="statement"><div class="wrap reveal">
  <p>Divorce, custody, and family court don't run on your schedule or your budget — <span class="hl">so we built four ways in</span>, instead of forcing every family through the same $400-an-hour door.</p>
</div></section>

<section class="services" id="services"><div class="wrap">
  <div class="section-head reveal"><div><span class="eyebrow">How we help</span><h2 class="display">Four ways in</h2></div>
    <p>Pick the level of support that fits your case, your budget, and how much of this you want to run yourself. Each one routes straight to its own intake — no runaround.</p></div>
  <div class="service-list">{svc_html}</div>
</div></section>

<section class="topics" id="topics"><div class="wrap">
  <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--pink)">Areas we work in</span><h2 class="display">Start with your situation</h2></div>
    <p>Plain-language guides on the Florida law behind your case — each one points you to the way in that fits.</p></div>
  <div class="topic-grid reveal">{topics_html}</div>
</div></section>

<section class="editorial"><div class="editorial-bg"></div><div class="wrap editorial-inner">
  <blockquote class="reveal">"Most people don't need to be talked into a lawsuit. They need someone to tell them, plainly, what happens next — and what it's going to cost to get there."</blockquote>
  <cite>— Leisa Wintz, Founding Attorney</cite>
</div></section>

<section class="approach" id="approach"><div class="wrap">
  <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--teal)">Our approach</span><h2 class="display">Plain terms. Real options.</h2></div>
    <p>The same three commitments, whichever of the four doors you walk through.</p></div>
  <div class="approach-grid reveal">
    <div class="approach-card"><div class="mark" aria-hidden="true"></div><h3>Straight answers</h3><p>The honest answer first, then the nuance. No jargon, no stalling on bad news — you'll always know where your case stands and what it's likely to cost.</p></div>
    <div class="approach-card"><div class="mark" aria-hidden="true"></div><h3>Options, not one path</h3><p>Litigation is sometimes the answer. Mediation, coaching, or a hybrid is often faster and cheaper — we'll tell you which fits instead of selling the most expensive one.</p></div>
    <div class="approach-card"><div class="mark" aria-hidden="true"></div><h3>The kids come first</h3><p>Every recommendation is weighed against what it does to the children in the middle of it — not just what it does to the case. We're moms and attorneys both.</p></div>
  </div>
</div></section>

<section class="shop" id="shop"><div class="wrap">
  <div><span class="eyebrow">DIY Legal Shop</span><h2 class="display">Do it yourself. Just not blind.</h2>
    <p>On-demand courses, templates, and toolkits to navigate Florida family court with confidence — paired with coaching whenever you want a licensed attorney in your corner.</p>
    <div class="shop-list"><span class="shop-tag">Courses</span><span class="shop-tag">Document templates</span><span class="shop-tag">Toolkits &amp; guides</span><span class="shop-tag">Monthly subscription</span></div></div>
  <div class="shop-cta"><div class="shop-mug" role="img" aria-label="DIY Legal Coaching"><span><span class="m1">DIY Legal</span><span class="m2">Coaching</span></span></div></div>
</div><div class="wrap" style="margin-top:34px;position:relative;z-index:2;">
  <a href="{root}ways-we-help/diy-legal-coaches/" class="btn btn-solid" style="background:var(--orange);box-shadow:0 12px 28px rgba(251,92,14,.34);">Browse the shop</a>
</div></section>

<section class="team" id="team"><div class="wrap">
  <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--teal)">The team</span><h2 class="display">Attorneys who've sat<br>where you're sitting.</h2></div>
    <p>You'll work directly with the person handling your case — not a rotating cast of associates.</p></div>
  <div class="team-grid reveal">
    <article class="attorney" data-who="leisa"><div class="attorney-photo" role="img" aria-label="Attorney Leisa Wintz" style="background-image:url('{root}assets/images/{LEISA_IMG}')"></div>
      <div class="attorney-body"><h3>Leisa Wintz</h3><div class="role">Founding Attorney</div>
        <p>Founded the firm in 2010 after a start in a domestic violence shelter, an internship in the 11th Circuit's DV Division, and a Master's in Marriage &amp; Family Therapy. She reads a case as both a lawyer and a family-systems clinician.</p>
        <div class="creds"><span>Supreme Court Certified Mediator</span><span>Guardian ad Litem</span><span>Parenting Coordinator</span><span>Collaborative Divorce Advocate</span></div>
        <a class="link" href="{root}attorneys/leisa-wintz/">Read Leisa's story <span class="arrow">→</span></a></div></article>
    <article class="attorney" data-who="both"><div class="attorney-photo" role="img" aria-label="Attorney Nazarena Hauser" style="background-image:url('{root}assets/images/{NAZ_IMG}')"></div>
      <div class="attorney-body"><h3>Nazarena Hauser</h3><div class="role">Head of Litigation</div>
        <p>Leads the firm's litigation since 2017 and practices fully bilingually — including mediation conducted entirely in Spanish. Past President of the Broward County Hispanic Bar Association and a Broward Bar "40 Under 40."</p>
        <div class="creds"><span>Head of Litigation</span><span>Certified Mediator</span><span>Bilingual — Español</span><span>40 Under 40</span></div>
        <a class="link" href="{root}attorneys/nazarena-hauser/">Read Nazarena's story <span class="arrow">→</span></a></div></article>
  </div>
</div></section>

<section class="posts"><div class="wrap">
  <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--pink)">From the blog</span><h2 class="display">Recent reading</h2></div>
    <p>Straight, current Florida family-law explainers — no keyword soup. <a href="{root}blog/" style="color:var(--teal);font-weight:600;">See all guides →</a></p></div>
  <div class="post-grid reveal">{posts_html}</div>
</div></section>
"""
page("index.html", "Family Matters Law Group — Florida Family Law, Mediation, DIY Coaching & Guardians ad Litem",
     "A South Florida family law firm with four ways in: lawyers, mediators, DIY legal coaches, and guardians ad litem. Warm, direct, flat-fee options. Bilingual — se habla español.",
     home_body, active="", is_home=True)

# =============================================================================
#  WRITE
# =============================================================================
EXTERNAL_FIX = {
  "../../blog/mediation-prep/": CUR + "/mediation-prep-in-florida-how-to-walk-in-ready-and-walk-out-settled",
  "../../blog/family-systems-in-mediation/": CUR + "/family-systems-in-mediation",
}
written = 0
for relpath, doc in PAGES:
    for a, b in EXTERNAL_FIX.items():
        doc = doc.replace(a, b)
    full = os.path.join(ROOT_DIR, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)
    written += 1
print(f"\nWROTE {written} pages.")
