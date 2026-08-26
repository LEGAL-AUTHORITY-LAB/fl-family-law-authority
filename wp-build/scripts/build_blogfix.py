import os, subprocess
BASE="/tmp/claude-0/-home-user-fl-family-law-authority/7ac3e289-c815-5f2d-9278-ecc0918a4dd6/scratchpad"
bodies=os.path.join(BASE,"bodies")

# (color, category, href, title, clean-description)
POSTS=[
 ("var(--chartreuse)","Alimony","/alimony-complete-guide/","The Complete Guide to Alimony in Florida","Everything Florida spouses need to know: the types of alimony, how courts weigh need and ability to pay, and exactly what the 2023 reform changed."),
 ("var(--orange)","Child Support","/child-support-complete-guide/","The Complete Guide to Child Support in Florida","How Florida calculates support, what it covers, whether it's taxable, how to enforce it, and what happens if you stop receiving or paying."),
 ("var(--chartreuse)","Guardian ad Litem","/guardian-ad-litem-guide/","Working With a Guardian ad Litem in Florida","What a GAL does, how one gets appointed, who pays, and how to prepare for and work with a Guardian ad Litem in your case."),
 ("var(--orange)","Protection","/domestic-violence-injunctions/","Domestic Violence & Injunctions in Florida","What domestic-violence injunctions (restraining orders) are in Florida, how to file for one, and what happens if one is violated."),
 ("var(--teal)","Custody","/modify-parenting-plan/","How to Modify a Parenting Plan in Florida","Can you change custody in Florida? What counts as a substantial change in circumstances, and how the modification process actually works."),
 ("var(--pink)","Representation","/legal-representation-options/","Your Legal Representation Options in Florida","Full representation, flat-fee through mediation, DIY legal coaching, and limited-scope help — how to choose the right option for your family."),
 ("var(--pink)","Paternity","/unmarried-fathers-rights/","Unmarried Fathers' Rights in Florida","Being on the birth certificate isn't enough. What unmarried fathers must do to establish legal timesharing and decision-making rights."),
 ("var(--pink)","Paternity","/paternity-testing/","Court-Ordered Paternity Testing in Florida","How court-ordered paternity testing works in Florida, your options if the alleged father won't participate, and what to do without a lawyer."),
 ("var(--orange)","Support","/imputed-income/","Imputed Income in Florida Family Law Cases","What happens when a parent is voluntarily unemployed or underemployed in a support or alimony case — and how courts impute income."),
 ("var(--orange)","Support","/business-owner-income/","Calculating Income for Business Owners","How Florida family courts determine income for self-employed spouses and business owners in divorce, support, and alimony cases."),
 ("var(--teal)","Name Change","/name-changes/","Name Changes in Florida: Adults & Children","How to legally change your name or your child's name in Florida, including a name change handled as part of a divorce."),
 ("var(--teal)","Procedure","/jurisdiction-venue/","Jurisdiction and Venue in Florida Family Law","The difference between jurisdiction and venue in Florida family law — and where you're actually required to file your case."),
 ("var(--chartreuse)","Parenting","/summer-camp-parenting/","Summer Camp & Shared Parental Responsibility","Who decides on summer camp when parents share parental responsibility, who pays for it, and how your parenting plan should address it."),
]

def cards():
    out=[]
    for ac,cat,href,title,desc in POSTS:
        out.append(f'<a class="blog-card" style="--ac:{ac}" href="{href}"><span class="cat">{cat}</span><h3>{title}</h3><p>{desc}</p><span class="go">Read the guide &rarr;</span></a>')
    return "\n      ".join(out)

SCOPED='''<style>
#bloglist{grid-template-columns:repeat(3,1fr);gap:20px}
#bloglist .blog-card{border-top:4px solid var(--ac,var(--pink));padding-top:22px}
#bloglist .blog-card .cat{color:var(--ac,var(--pink))}
#bloglist .blog-card h3{margin-bottom:12px}
#bloglist .blog-card .go{color:var(--ac,var(--pink))}
@media (max-width:900px){#bloglist{grid-template-columns:1fr 1fr}}
@media (max-width:600px){#bloglist{grid-template-columns:1fr}}
</style>'''

MAIN=f'''<main>

<section class="page-hero tint-topic">
  <div class="wrap">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> Blog</div>
    <span class="eyebrow">Blog &amp; guides</span>
    <h1>Straight Florida family-law writing — no keyword soup</h1>
    <p class="lede">In-depth, current guides written by our attorneys. These are the flagship launch set; the full archive of 190+ posts migrates from the current site with 301 redirects in place.</p>
  </div>
</section>

<section class="section paper">{SCOPED}
  <div class="wrap">
    <div class="blog-list" id="bloglist">
      {cards()}
    </div>
    <div class="notice mt-l center">Looking for an older post? The complete archive is migrating from <a href="https://www.familymatterslawgroup.com/blog" style="color:var(--teal)">the current site</a> — every old URL will 301-redirect to its new home. In the meantime, explore <a href="/glossary/" style="color:var(--teal)">the legal glossary</a> or <a href="/latest/" style="color:var(--teal)">our videos</a>.</div>
  </div>
</section>

</main>'''

src=open(os.path.join(bodies,"blog.html")).read()
head=src.split("<main>",1)[0]; tail=src.split("</main>",1)[1]
open(os.path.join(bodies,"blog.html"),"w").write(head+MAIN+tail)
subprocess.run(["python3",os.path.join(BASE,"gen_final.py")],capture_output=True)
print("blog final bytes:",os.path.getsize(os.path.join(BASE,"final/blog.html")))

# ---- standalone preview for an Artifact (text logo, no external images) ----
css=open(os.path.join(BASE,"css_p1.txt")).read()+open(os.path.join(BASE,"css_p2.txt")).read()
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,500;1,600&display=swap">'
prev=f'''<title>FMLG Blog — Redesign Preview</title>
{FONTS}
<style>{css}
.pvhead{{background:var(--charcoal);color:#fff;padding:16px 0;position:sticky;top:0;z-index:50}}
.pvhead .wrap{{display:flex;justify-content:space-between;align-items:center}}
.pvlogo{{font-family:'Archivo Black',sans-serif;text-transform:uppercase;letter-spacing:-.01em;font-size:16px}}
.pvlogo b{{color:var(--pink)}}
#bloglist{{grid-template-columns:repeat(3,1fr);gap:20px}}
#bloglist .blog-card{{border-top:4px solid var(--ac,var(--pink));padding-top:22px}}
#bloglist .blog-card .cat{{color:var(--ac,var(--pink))}}
#bloglist .blog-card h3{{margin-bottom:12px}}
#bloglist .blog-card .go{{color:var(--ac,var(--pink))}}
@media (max-width:900px){{#bloglist{{grid-template-columns:1fr 1fr}}}}
@media (max-width:600px){{#bloglist{{grid-template-columns:1fr}}}}
</style>
<header class="pvhead"><div class="wrap"><div class="pvlogo">Family <b>Matters</b> Law Group</div><div style="font-size:12px;opacity:.7">Blog redesign preview</div></div></header>
<section class="page-hero tint-topic" style="padding-top:64px">
  <div class="wrap">
    <div class="breadcrumb"><a href="#">Home</a> <span>/</span> Blog</div>
    <span class="eyebrow">Blog &amp; guides</span>
    <h1>Straight Florida family-law writing — no keyword soup</h1>
    <p class="lede">In-depth, current guides written by our attorneys. These are the flagship launch set; the full archive of 190+ posts migrates from the current site with 301 redirects in place.</p>
  </div>
</section>
<section class="section paper">
  <div class="wrap">
    <div class="blog-list" id="bloglist">
      {cards()}
    </div>
    <div class="notice mt-l center">Looking for an older post? The complete archive is migrating from the current site — every old URL will 301-redirect. In the meantime, explore the legal glossary or our videos.</div>
  </div>
</section>'''
open(os.path.join(BASE,"preview_blog.html"),"w").write(prev)
print("preview bytes:",len(prev))
