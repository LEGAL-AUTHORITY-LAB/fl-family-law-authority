import os, json, subprocess
BASE="/tmp/claude-0/-home-user-fl-family-law-authority/7ac3e289-c815-5f2d-9278-ecc0918a4dd6/scratchpad"
bodies=os.path.join(BASE,"bodies")
IMG="https://cdn.lawlytics.com/law-media/uploads/4669/329246/large/DIY-APP.jpg?1746750629"
JOT="https://form.jotform.com/262314050185044"

MAIN='''<main>

<section class="page-hero tint-coaches">
  <div class="wrap">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> DIY Legal</div>
    <span class="eyebrow">DIY Legal &middot; Coming soon</span>
    <h1>The DIY Legal app is almost here</h1>
    <p class="lede">A self-serve platform from Family Matters Law Group that helps Florida family-law litigants learn the law, navigate the process, and prepare their own paperwork &mdash; with live chat or a full attorney review whenever you want backup. Your case, your pace, our tools.</p>
    <div class="hero-ctas">
      <a href="'''+JOT+'''" target="_blank" rel="noopener" class="btn btn-solid">Join the waitlist</a>
      <a href="tel:9549041020" class="btn btn-outline-light">Call or text 954.904.1020</a>
    </div>
  </div>
</section>

<section class="feature-band"><div class="wrap"><div class="fb-frame" style="background-image:url('''+IMG+''')"><img class="fb-img" src="'''+IMG+'''" alt="DIY Legal app preview" loading="lazy"></div></div></section>

<section class="section tight"><div class="wrap"><div class="notice center"><strong>You can do this &mdash; but you shouldn&rsquo;t have to do it alone.</strong> Every visitor gets the full educational side of DIY Legal free. Add a person in the loop whenever you want one.</div></div></section>

<section class="section paper" id="tiers">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--orange)">Three ways to use it</span><h2 class="display">Start free. Add live help or a full review.</h2></div>
      <p>Everyone gets full access to the educational side at no cost. When you want backup, two upgrades are there &mdash; a quick live chat, or a full document review from a real paralegal or attorney.</p></div>
    <div class="subpaths">
      <div class="subpath">
        <h3>Educational access</h3><div class="who" style="color:var(--teal)">Free</div>
        <p>Everything you need to understand your matter and prepare your own documents.</p>
        <ul class="lead-list">
          <li>Plain-language statutes &amp; case law</li>
          <li>Guided intake to personalize what you see</li>
          <li>Self-help pleading &amp; template generator</li>
          <li>Child support estimate calculator</li>
          <li>AI-guided assistant for general questions</li>
        </ul>
      </div>
      <div class="subpath">
        <h3>Live paralegal &amp; attorney chat</h3><div class="who" style="color:var(--orange)">Paid upgrade</div>
        <p>Stuck mid-form or unsure what a term means? Chat live with a real paralegal or attorney.</p>
        <ul class="lead-list">
          <li>Real-time chat during business hours</li>
          <li>Ask quick, matter-specific questions as you go</li>
          <li>Escalates to an attorney when the question calls for it</li>
          <li>Draws down from your credit balance as you chat</li>
          <li>Conflict check &amp; signed agreement required</li>
        </ul>
      </div>
      <div class="subpath">
        <h3>Attorney &amp; paralegal draft review</h3><div class="who">Paid upgrade</div>
        <p>When your paperwork is ready, have a professional review it before you file.</p>
        <ul class="lead-list">
          <li>Written feedback on your drafts</li>
          <li>Live Zoom review with an attorney or paralegal</li>
          <li>Flat-fee options for common requests</li>
          <li>Conflict check &amp; signed agreement required</li>
          <li>Transparent, pay-as-you-go credits</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section dim" id="features">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--pink)">What&rsquo;s inside</span><h2 class="display">Everything a self-represented litigant needs</h2></div></div>
    <div class="cards">
      <div class="card"><span class="sw" style="background:var(--pink)"></span><h3>Statute &amp; case law library</h3><p>Florida family-law statutes and key cases explained in plain English &mdash; no jargon required.</p></div>
      <div class="card"><span class="sw" style="background:var(--orange)"></span><h3>How family court actually works</h3><p>Practical, statewide guidance on hearings, service of process, mediation, and court decorum.</p></div>
      <div class="card"><span class="sw" style="background:var(--teal)"></span><h3>Template &amp; pleading generator</h3><p>Generate a self-help pleading shell for your matter, clearly marked as a self-prepared document.</p></div>
      <div class="card"><span class="sw" style="background:var(--chartreuse)"></span><h3>Child support calculator</h3><p>A guided walkthrough of Florida&rsquo;s child support factors that produces a clear, labeled estimate.</p></div>
      <div class="card"><span class="sw" style="background:var(--pink)"></span><h3>AI-guided assistant</h3><p>Ask general questions and get educational answers built from real family-law guidance.</p></div>
      <div class="card"><span class="sw" style="background:var(--teal)"></span><h3>Search everything</h3><p>One search box across statutes, guides, forms, and frequently asked questions.</p></div>
    </div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--teal)">Built for your matter</span><h2 class="display">A short intake personalizes what you see</h2></div>
      <p>Answer a few questions and DIY Legal shows the content that actually applies &mdash; while everything else stays a search away.</p></div>
    <div class="chips" style="justify-content:center">
      <span class="chip">Divorce</span><span class="chip">Paternity</span><span class="chip">Modification</span><span class="chip">Injunction / DV</span><span class="chip">Relocation</span><span class="chip">Name change</span><span class="chip">Adoption</span><span class="chip">Grandparent visitation</span>
    </div>
  </div>
</section>

<section class="section dim">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow" style="color:var(--orange)">How it works</span><h2 class="display">From questions to a filed document</h2></div></div>
    <div class="steps">
      <div class="step"><h3>Tell us about your case</h3><p>A short questionnaire on matter type, kids, and key issues.</p></div>
      <div class="step"><h3>Learn what applies to you</h3><p>Statutes, guides, and FAQs tailored to your situation &mdash; everything else always searchable.</p></div>
      <div class="step"><h3>Prepare your paperwork</h3><p>Use the calculators and template generator to draft your own documents.</p></div>
      <div class="step"><h3>Bring in help if you want it</h3><p>After a conflict check and signed agreement, chat live or send your draft in for a full review.</p></div>
    </div>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="cta-band orange">
      <div><h2>Be first in line</h2><p>Join the waitlist and we&rsquo;ll reach out the moment DIY Legal is ready &mdash; plus early access to launch pricing on the chat and review upgrades.</p></div>
      <a href="'''+JOT+'''" target="_blank" rel="noopener" class="btn btn-solid">Join the waitlist</a>
    </div>
  </div>
</section>

<section class="section tight"><div class="wrap measure">
  <div class="notice"><strong>Educational content, not legal advice.</strong> DIY Legal provides general information about Florida family law. Using the free tier does not create an attorney-client relationship with Family Matters Law Group. That relationship begins only once a conflict check is complete and a representation agreement is signed for the live chat or document-review upgrades. Questions? Call or text <a href="tel:9549041020" style="color:var(--teal)">954.904.1020</a> or email <a href="mailto:info@fmlgpa.com" style="color:var(--teal)">info@fmlgpa.com</a>.</div>
</div></section>

</main>'''

# compose body from an existing (already shell-edited) body's header + footer/js
src=open(os.path.join(bodies,"learn.html")).read()
head=src.split("<main>",1)[0]
tail=src.split("</main>",1)[1]
open(os.path.join(bodies,"diy-legal.html"),"w").write(head+MAIN+tail)

# add "DIY Legal" to the "Also offered" nav dropdown across ALL bodies (idempotent)
NAV_ANCHOR='<a href="/collaborative-divorce/">Collaborative Divorce</a>'
NAV_ADD=NAV_ANCHOR+'\n          <a href="/diy-legal/">DIY Legal (App)</a>'
edited=0
for fn in os.listdir(bodies):
    if not fn.endswith(".html"): continue
    p=os.path.join(bodies,fn); t=open(p).read()
    if '<a href="/diy-legal/">DIY Legal (App)</a>' not in t and NAV_ANCHOR in t:
        t=t.replace(NAV_ANCHOR,NAV_ADD,1); open(p,"w").write(t); edited+=1
print("nav link added to",edited,"bodies")

subprocess.run(["python3",os.path.join(BASE,"gen_final.py")],capture_output=True)
print("diy-legal final bytes:",os.path.getsize(os.path.join(BASE,"final/diy-legal.html")))

# add diy-legal (create) to a standalone plan + append to repush_plan
plan=json.load(open(os.path.join(BASE,"repush_plan.json")))
if not any(p["slug"]=="diy-legal" for p in plan):
    plan.append({"slug":"diy-legal","id":None,"action":"create",
      "title":"DIY Legal — Coming Soon | Family Matters Law Group",
      "file":os.path.join(BASE,"final","diy-legal.html")})
    json.dump(plan,open(os.path.join(BASE,"repush_plan.json"),"w"),indent=1)
json.dump([{"slug":"diy-legal","id":None,"action":"create",
  "title":"DIY Legal — Coming Soon | Family Matters Law Group",
  "file":os.path.join(BASE,"final","diy-legal.html")}],
  open(os.path.join(BASE,"repush_diylegal.json"),"w"),indent=1)
print("plan entries:",len(plan))
