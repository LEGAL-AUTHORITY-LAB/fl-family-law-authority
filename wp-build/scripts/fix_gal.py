import os,re,subprocess,glob
BASE="/tmp/claude-0/-home-user-fl-family-law-authority/7ac3e289-c815-5f2d-9278-ecc0918a4dd6/scratchpad"
bodies=os.path.join(BASE,"bodies")
GAL="PLla9kEl3qwgiKkdUms6ph-DkmZdvt68YH"

def remove_section(text,needle):
    i=text.find(needle)
    if i<0: return text,False
    start=text.rfind("<section",0,i)
    end=text.find("</section>",i)
    if start<0 or end<0: return text,False
    end+=len("</section>")
    if start>0 and text[start-1]=="\n": start-=1
    return text[:start]+text[end:],True

for slug in ["guardians-ad-litem","guardian-ad-litem-guide"]:
    p=os.path.join(bodies,slug+".html")
    t=open(p).read()
    t2,ok=remove_section(t,GAL)
    open(p,"w").write(t2)
    print(slug,"section removed:",ok)

# latest: remove the GAL playlist card
p=os.path.join(bodies,"latest.html")
t=open(p).read()
m=re.search(r'\s*<a class="card"[^>]*'+re.escape(GAL)+r'.*?</a>',t,re.S)
print("latest GAL card found:",bool(m))
if m: t=t[:m.start()]+t[m.end():]
open(p,"w").write(t)

hits=[os.path.basename(f) for f in glob.glob(bodies+"/*.html") if GAL in open(f).read()]
print("bodies still with GAL:",hits)
subprocess.run(["python3",os.path.join(BASE,"gen_final.py")],capture_output=True)
hits2=[os.path.basename(f) for f in glob.glob(BASE+"/final/*.html") if GAL in open(f).read()]
print("finals still with GAL:",hits2)
