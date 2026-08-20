import os, json, subprocess, sys
BASE="/tmp/claude-0/-home-user-fl-family-law-authority/7ac3e289-c815-5f2d-9278-ecc0918a4dd6/scratchpad"
bodies=os.path.join(BASE,"bodies")
sys.path.insert(0,BASE)
import shell_edits

EMBED='https://www.youtube-nocookie.com/embed/videoseries?list='

# ---- all playlists (title, id, count) ----
PLAYLISTS=[
 ("Family Matters Law — The Podcast","PLla9kEl3qwgjuAow2UMti3c0S-ND5VkWN","24 episodes"),
 ("Family Matters on Sundays — Live with Leisa & Naz","PLla9kEl3qwgiyiPXCeYeDHyZwFhT-Ybto","9 episodes"),
 ("Divorce in Florida","PLla9kEl3qwgiggtJ6HkN3XK-k1bGd-puL","14 videos"),
 ("Child Support in Florida","PLla9kEl3qwgh8NC-dlmjToahsuOHwV221","12 videos"),
 ("FL Family Courts & Rules","PLla9kEl3qwgidTWPt6oUXfxuLNnaBLwBH","11 videos"),
 ("Guardian ad Litem Training","PLla9kEl3qwgiKkdUms6ph-DkmZdvt68YH","11 videos"),
 ("Parenting & Timesharing","PLla9kEl3qwgjN_A1h1vLVZY_xqdyIuHMw","7 videos"),
 ("Family Matters on Sundays — Live on Instagram","PLla9kEl3qwgiblv2_-xafJqJumCyRpyKt","7 videos"),
 ("DIY Legal","PLla9kEl3qwgizRjb4NCzSpSw6hCUW_d6z","5 videos"),
 ("Discovery & Finances in Florida Family Law","PLla9kEl3qwggC2aka7A5j-EqEjJth9wBk","5 videos"),
 ("Alimony in Florida","PLla9kEl3qwgiOI-YBwXXUH6Ucn9xkwS-l","4 videos"),
 ("Cheaper to Keep Her? Alimony in FL","PLla9kEl3qwgjVDeCPLPmkkLKqbextNZ3W","4 videos"),
 ("Prenuptial Agreements in Florida","PLla9kEl3qwgjJHnz81A5Rq5RSxdR8tce1","4 videos"),
 ("Family Matters Podcast (archive)","PLla9kEl3qwgjQ6ds27sjSIOJjOYWI_8op","4 videos"),
 ("Equitable Distribution in Florida","PLla9kEl3qwgjwur9bVCJlsISzSBQQgriN","3 videos"),
 ("Domestic Violence in Family Court","PLla9kEl3qwgi3wMnvv1sXM0PbGXn9sq3N","3 videos"),
 ("Mediation in Florida Family Law","PLla9kEl3qwgj1arv-R-i940dufRUO5I7n","3 videos"),
 ("Name Changes in Florida","PLla9kEl3qwggZ8Z8g1mr8AV_pSRSGvrTL","2 videos"),
 ("Modifications in Florida Family Court","PLla9kEl3qwghToN1L0qjcaiy24Js0zuY4","2 videos"),
 ("Business Owners & Divorce","PLla9kEl3qwggMHXGvcKuXTyW7TL7wwZ8G","1 video"),
 ("Collaborative Family Law in FL","PLla9kEl3qwgha56lUTugpImt57H7BEHvR","1 video"),
]
PODCAST_ID="PLla9kEl3qwgjuAow2UMti3c0S-ND5VkWN"
COLORS=["var(--pink)","var(--teal)","var(--orange)","var(--chartreuse)"]

def iframe(src,title):
    return ('<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;'
      'border-radius:var(--radius);box-shadow:0 18px 48px rgba(22,19,15,.18);background:#000">'
      f'<iframe src="{src}" title="{title}" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" '
      'allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture;web-share" '
      'allowfullscreen loading="lazy"></iframe></div>')

# ---- topic/service page -> playlist mapping ----
TOPICVID={
 "divorce":("Divorce in Florida","PLla9kEl3qwgiggtJ6HkN3XK-k1bGd-puL"),
 "alimony":("Alimony in Florida","PLla9kEl3qwgiOI-YBwXXUH6Ucn9xkwS-l"),
 "alimony-complete-guide":("Alimony in Florida","PLla9kEl3qwgiOI-YBwXXUH6Ucn9xkwS-l"),
 "child-support":("Child Support in Florida","PLla9kEl3qwgh8NC-dlmjToahsuOHwV221"),
 "child-support-complete-guide":("Child Support in Florida","PLla9kEl3qwgh8NC-dlmjToahsuOHwV221"),
 "custody-and-parenting":("Parenting & Timesharing","PLla9kEl3qwgjN_A1h1vLVZY_xqdyIuHMw"),
 "name-change":("Name Changes in Florida","PLla9kEl3qwggZ8Z8g1mr8AV_pSRSGvrTL"),
 "name-changes":("Name Changes in Florida","PLla9kEl3qwggZ8Z8g1mr8AV_pSRSGvrTL"),
 "prenup-postnup":("Prenuptial Agreements in Florida","PLla9kEl3qwgjJHnz81A5Rq5RSxdR8tce1"),
 "equitable-distribution":("Equitable Distribution in Florida","PLla9kEl3qwgjwur9bVCJlsISzSBQQgriN"),
 "collaborative-divorce":("Collaborative Family Law in FL","PLla9kEl3qwgha56lUTugpImt57H7BEHvR"),
 "mediators":("Mediation in Florida Family Law","PLla9kEl3qwgj1arv-R-i940dufRUO5I7n"),
 "injunctions-domestic-violence":("Domestic Violence in Family Court","PLla9kEl3qwgi3wMnvv1sXM0PbGXn9sq3N"),
 "domestic-violence-injunctions":("Domestic Violence in Family Court","PLla9kEl3qwgi3wMnvv1sXM0PbGXn9sq3N"),
 "guardians-ad-litem":("Guardian ad Litem Training","PLla9kEl3qwgiKkdUms6ph-DkmZdvt68YH"),
 "guardian-ad-litem-guide":("Guardian ad Litem Training","PLla9kEl3qwgiKkdUms6ph-DkmZdvt68YH"),
 "diy-legal-coaches":("DIY Legal","PLla9kEl3qwgizRjb4NCzSpSw6hCUW_d6z"),
 "modify-parenting-plan":("Modifications in Florida Family Court","PLla9kEl3qwghToN1L0qjcaiy24Js0zuY4"),
 "business-owner-income":("Business Owners & Divorce","PLla9kEl3qwggMHXGvcKuXTyW7TL7wwZ8G"),
 "jurisdiction-venue":("Florida Family Courts & Rules","PLla9kEl3qwgidTWPt6oUXfxuLNnaBLwBH"),
}

def topic_section(title,plid):
    return ('\n<section class="section dim">\n  <div class="wrap">\n'
      '    <div class="section-head reveal">\n'
      '      <div><span class="eyebrow" style="color:var(--pink)">Watch</span>'
      f'<h2 class="display">{title} — on video</h2></div>\n'
      '      <p>From our YouTube channel. <a href="/latest/" style="color:var(--teal);font-weight:600">See all playlists &rarr;</a></p>\n'
      '    </div>\n    ' + iframe(EMBED+plid, title+" — Family Matters Law Group") +
      '\n  </div>\n</section>\n')

# ---- rebuild the /latest/ body with playlists ----
cards=[]
for i,(t,pid,cnt) in enumerate(PLAYLISTS):
    c=COLORS[i%4]
    cards.append(f'<a class="card" href="https://www.youtube.com/playlist?list={pid}" target="_blank" rel="noopener">'
      f'<span class="sw" style="background:{c}"></span><h3>{t}</h3><p>{cnt}</p>'
      f'<p class="go">Watch on YouTube &rarr;</p></a>')
grid="\n      ".join(cards)

LATEST_MAIN=f'''
<section class="page-hero tint-topic">
  <div class="wrap">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> Latest from FMLG</div>
    <span class="eyebrow">Latest from FMLG</span>
    <h1>Watch, read, and follow along</h1>
    <p class="lede">Everything we&rsquo;re putting out &mdash; video explainers and a weekly show on YouTube, in-depth guides on the blog, and quick updates on Instagram. Plain-English Florida family law, in English and Spanish.</p>
    <div class="hero-ctas">
      <a href="https://www.youtube.com/@Familymatterslaw" target="_blank" rel="noopener" class="btn btn-solid">Subscribe on YouTube</a>
      <a href="https://www.instagram.com/familymatterslawgroup/" target="_blank" rel="noopener" class="btn btn-outline-light">Follow on Instagram</a>
    </div>
  </div>
</section>

<section class="section paper" id="watch">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow" style="color:var(--pink)">Watch</span><h2 class="display">Featured</h2></div>
      <p>Start here, then dive into any of our playlists below.</p>
    </div>
    {iframe('https://www.youtube-nocookie.com/embed/azuM-47UHwk','Family Matters Law Group — featured video')}
  </div>
</section>

<section class="section dim">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow" style="color:var(--teal)">The show</span><h2 class="display">Family Matters — The Podcast</h2></div>
      <p>Our full podcast series &mdash; {'24 episodes'} on Florida family law, mediation, and life in the middle of it.</p>
    </div>
    {iframe(EMBED+PODCAST_ID,'Family Matters Law — The Podcast')}
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow" style="color:var(--orange)">Browse by topic</span><h2 class="display">All playlists</h2></div>
      <p>Every series we&rsquo;ve published &mdash; pick the topic that fits your case.</p>
    </div>
    <div class="cards">
      {grid}
    </div>
  </div>
</section>

<section class="section dim" id="read">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow" style="color:var(--teal)">Read</span><h2 class="display">From the blog</h2></div>
      <p>In-depth, current guides on the Florida law behind your case. <a href="/blog/" style="color:var(--teal);font-weight:600">See all guides &rarr;</a></p>
    </div>
    <div class="blog-list">
      <a class="blog-card" href="/alimony-complete-guide/"><div class="cat">Alimony</div><h3>The Complete Guide to Alimony in Florida</h3><p>How alimony works after the 2023 reform &mdash; types, caps, duration, and modification.</p><span class="go">Read the guide &rarr;</span></a>
      <a class="blog-card" href="/child-support-complete-guide/"><div class="cat">Child Support</div><h3>The Complete Guide to Child Support in Florida</h3><p>The income-shares model, how the number is actually calculated, and when it changes.</p><span class="go">Read the guide &rarr;</span></a>
      <a class="blog-card" href="/modify-parenting-plan/"><div class="cat">Custody</div><h3>How to Modify a Parenting Plan in Florida</h3><p>The &ldquo;substantial change&rdquo; standard and what it takes to change a timesharing order.</p><span class="go">Read the guide &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section ink" id="follow">
  <div class="wrap split">
    <div class="prose" style="color:rgba(251,250,247,.85)">
      <div class="kicker">Follow</div>
      <h2 style="color:var(--paper)">On Instagram &mdash; @familymatterslawgroup</h2>
      <p style="color:rgba(251,250,247,.8)">Quick tips, firm updates, and a look behind the scenes at how we help South Florida families &mdash; in English and Spanish.</p>
      <div class="hero-ctas" style="margin-top:24px"><a href="https://www.instagram.com/familymatterslawgroup/" target="_blank" rel="noopener" class="btn btn-solid">Open Instagram</a></div>
    </div>
    <aside class="aside-card">
      <h4>Find us</h4>
      <ul>
        <li><a href="https://www.youtube.com/@Familymatterslaw" target="_blank" rel="noopener">YouTube &mdash; @Familymatterslaw</a></li>
        <li><a href="https://www.instagram.com/familymatterslawgroup/" target="_blank" rel="noopener">Instagram &mdash; @familymatterslawgroup</a></li>
        <li><a href="/blog/">Blog &amp; Guides</a></li>
        <li><a href="/glossary/">Legal Glossary</a></li>
      </ul>
    </aside>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="cta-band pink">
      <div><h2>Have a question we haven&rsquo;t covered?</h2><p>Tell us what&rsquo;s going on &mdash; your intake goes straight to our team.</p></div>
      <a href="/get-started/" class="btn btn-solid">Get started</a>
    </div>
  </div>
</section>
'''

learn=open(os.path.join(bodies,"learn.html")).read()
head,rest=learn.split("<main>",1); _,tail=rest.split("</main>",1)
open(os.path.join(bodies,"latest.html"),"w").write(head+"<main>\n"+LATEST_MAIN+"\n</main>"+tail)

# ---- apply shell edits + topic videos to ALL bodies ----
report={"shell":0,"topicvid":[]}
for fn in sorted(os.listdir(bodies)):
    if not fn.endswith(".html"): continue
    slug=fn[:-5]
    t=open(os.path.join(bodies,fn)).read()
    before=t
    t=shell_edits.apply(t)
    if t!=before: report["shell"]+=1
    if slug in TOPICVID and 'embed/videoseries?list=' not in t:
        title,plid=TOPICVID[slug]
        t=t.replace("\n</main>", topic_section(title,plid)+"</main>",1)
        report["topicvid"].append(slug)
    open(os.path.join(bodies,fn),"w").write(t)

print("shell edited bodies:",report["shell"])
print("topic-video bodies:",len(report["topicvid"]),sorted(report["topicvid"]))

# regenerate final/
out=subprocess.run(["python3",os.path.join(BASE,"gen_final.py")],capture_output=True,text=True)
print(out.stdout.strip().splitlines()[0] if out.stdout else out.stderr[-400:])

# ---- build re-push plan (all live pages -> update by id) ----
id_map={'lawyers':150,'about':1,'mediators':152,'coparenting-coaching':153,'divorce':154,
'domestic-violence-injunctions':155,'modify-parenting-plan':156,'diy-legal-coaches':157,
'paralegal-services':158,'custody-and-parenting':159,'unmarried-fathers-rights':160,
'business-owner-income':161,'guardians-ad-litem':162,'diy-divorce-packages':163,
'child-support':164,'paternity-testing':165,'legal-representation-options':166,'pricing':167,
'parenting-coordination':168,'alimony':169,'guardian-ad-litem-guide':170,'name-changes':171,
'collaborative-divorce':172,'get-started':173,'paternity':174,'peace-plan':175,
'summer-camp-parenting':176,'learn':177,'timesharing':178,'team':179,'adoption':180,
'jurisdiction-venue':181,'income-shares-model':182,'leisa-wintz':184,
'injunctions-domestic-violence':185,'imputed-income':186,'uccjea':187,'glossary':188,
'nazarena-hauser':189,'lgbtq-family-law':190,'child-support-complete-guide':191,
'best-interest-of-the-child':192,'reviews':193,'name-change':195,'equitable-distribution':196,
'alimony-complete-guide':197,'es':198,'current-clients':199,'prenup-postnup':200,
'blog':2,'shop':14,'latest':202}
titles={x['slug']:x['title'] for x in json.load(open(os.path.join(BASE,'wp_pages/_manifest.json')))}
titles['latest']="Latest from FMLG — Videos, Guides & Instagram | Family Matters Law Group"
plan=[]
for slug,pid in id_map.items():
    plan.append({"slug":slug,"id":pid,"action":"update",
      "title":titles.get(slug,slug),"file":os.path.join(BASE,"final",slug+".html")})
json.dump(plan,open(os.path.join(BASE,"repush_plan.json"),"w"),indent=1)
# split into 6 batches
import math
n=6; per=math.ceil(len(plan)/n)
for i in range(n):
    chunk=plan[i*per:(i+1)*per]
    if chunk: json.dump(chunk,open(os.path.join(BASE,f"repush{i+1}.json"),"w"),indent=1)
print("repush plan:",len(plan),"pages; batches of",per)
