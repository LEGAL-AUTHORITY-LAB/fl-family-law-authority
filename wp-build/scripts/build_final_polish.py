import os, subprocess
BASE="/tmp/claude-0/-home-user-fl-family-law-authority/7ac3e289-c815-5f2d-9278-ecc0918a4dd6/scratchpad"
bodies=os.path.join(BASE,"bodies")
OLD="familymatterslawgrouplaw.wpcomstaging.com"
NEW="familymatterslaw.app"

# 1) Glossary redesign: color-accented cards
GTERMS=[
 ("var(--teal)","/uccjea/","UCCJEA","Which state decides your custody case"),
 ("var(--pink)","/best-interest-of-the-child/","Best Interest of the Child","The standard behind every custody decision"),
 ("var(--orange)","/timesharing/","Timesharing","Florida's word for the parenting schedule"),
 ("var(--chartreuse)","/equitable-distribution/","Equitable Distribution","How Florida divides property — fairly, not always evenly"),
 ("var(--teal)","/income-shares-model/","Income-Shares Model","How child support is actually calculated"),
 ("var(--pink)","/peace-plan/","P.E.A.C.E.","The framework behind a Florida parenting plan"),
]
gcards="".join(f'<a style="--ac:{c}" href="{h}"><div class="term">{t}</div><div class="def">{d}</div></a>' for c,h,t,d in GTERMS)
GSCOPED='<style>#glossgrid a{border-left:4px solid var(--ac,var(--pink))}#glossgrid a:hover{border-left-color:var(--ac,var(--pink))}#glossgrid .term{color:var(--ac,var(--pink))}</style>'
GMAIN=f'''<main>

<section class="page-hero tint-topic">
  <div class="wrap">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> Glossary</div>
    <span class="eyebrow">Legal glossary</span>
    <h1>Plain-language definitions that link to each other</h1>
    <p class="lede">Short, honest explainers for the Florida family-law terms that trip people up — built as an interlinked cluster, not a pile of orphan pages.</p>
  </div>
</section>
<section class="section paper">{GSCOPED}<div class="wrap">
  <div class="glossary-grid" id="glossgrid">{gcards}</div>
  <div class="notice mt-l center">More terms are on the way. Looking for something specific? Try the <a href="/blog/" style="color:var(--teal)">guides on the blog</a> or <a href="/get-started/" style="color:var(--teal)">ask us directly</a>.</div>
</div></section>

</main>'''
src=open(os.path.join(bodies,"glossary.html")).read()
head=src.split("<main>",1)[0]; tail=src.split("</main>",1)[1]
open(os.path.join(bodies,"glossary.html"),"w").write(head+GMAIN+tail)

# 2) Normalize image domain across ALL bodies
changed=0
for fn in os.listdir(bodies):
    if not fn.endswith(".html"): continue
    p=os.path.join(bodies,fn); t=open(p).read()
    if OLD in t:
        open(p,"w").write(t.replace(OLD,NEW)); changed+=1
print("domain normalized in",changed,"bodies")

subprocess.run(["python3",os.path.join(BASE,"gen_final.py")],capture_output=True)
# verify no old domain remains in finals
import glob
left=[os.path.basename(f) for f in glob.glob(BASE+"/final/*.html") if OLD in open(f).read()]
print("finals still with old domain:",left)
print("glossary final bytes:",os.path.getsize(BASE+"/final/glossary.html"))
