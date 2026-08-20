import os, re, json

BASE = "/tmp/claude-0/-home-user-fl-family-law-authority/7ac3e289-c815-5f2d-9278-ecc0918a4dd6/scratchpad"
BODIES = os.path.join(BASE, "bodies")
OUT = os.path.join(BASE, "final")
os.makedirs(OUT, exist_ok=True)

css = open(os.path.join(BASE,"css_p1.txt")).read() + open(os.path.join(BASE,"css_p2.txt")).read()

BLOCK0_STYLE = ".wp-site-blocks>*,.wp-block-post-content,.wp-block-post-content>*,.entry-content,.entry-content>*,main.wp-block-group,main.wp-block-group>*,.is-layout-constrained,.is-layout-constrained>*{max-width:none!important;width:auto!important}.wp-block-post-content,.entry-content{padding:0!important;margin:0!important}.wp-block-site-title,.wp-block-post-title,.wp-block-query-title,.wp-block-template-part,.wp-site-blocks>header,.wp-site-blocks>footer,.site-header,.site-footer,.entry-header{display:none!important}body{margin:0!important;padding:0!important}"

CLEAN_JS = """(function(){
function clean(){
  document.querySelectorAll('.wp-block-site-title,.wp-block-post-title,.wp-block-query-title').forEach(function(e){e.remove();});
  document.querySelectorAll('.wp-site-blocks > header, body > header, .wp-block-template-part').forEach(function(e){ if(e.id!=='siteHeader' && !e.querySelector('#siteHeader')) e.remove(); });
  document.querySelectorAll('.wp-site-blocks > footer, body > footer').forEach(function(e){ if(!e.classList.contains('site')) e.remove(); });
  var h=document.getElementById('siteHeader');
  if(h){ var n=h.parentElement; while(n && n!==document.body){ n.style.maxWidth='none'; n.style.width='auto'; n.style.marginLeft='0'; n.style.marginRight='0'; n.style.paddingLeft='0'; n.style.paddingRight='0'; n=n.parentElement; } }
}
if(document.readyState!=='loading') clean(); else document.addEventListener('DOMContentLoaded',clean);
document.addEventListener('DOMContentLoaded',function(){setTimeout(clean,400);});
})();"""

JETPACK = '.wp-block-jetpack-contact-form input:not([type=submit]):not([type=checkbox]):not([type=radio]),.wp-block-jetpack-contact-form textarea,.wp-block-jetpack-contact-form select{border:1.5px solid #ddd !important;border-radius:10px !important;padding:13px 14px !important;font-size:16px !important;background:#fff !important;box-sizing:border-box}.wp-block-jetpack-contact-form input:not([type=submit]):focus,.wp-block-jetpack-contact-form textarea:focus,.wp-block-jetpack-contact-form select:focus{border-color:#c40a78 !important;outline:none;box-shadow:0 0 0 3px rgba(196,10,120,.18) !important}.wp-block-jetpack-contact-form label{font-weight:600}.wp-block-jetpack-contact-form button,.wp-block-jetpack-contact-form input[type=submit]{background:#c40a78 !important;border:0 !important;border-radius:999px !important;padding:15px 34px !important;font-weight:700 !important;color:#fff !important;letter-spacing:.02em}.wp-block-jetpack-contact-form h1{font-family:"Archivo Black",sans-serif}'

HIDE = ".wp-block-site-title,.wp-block-post-title,.wp-block-template-part,.wp-site-blocks>header,.wp-site-blocks>footer,.entry-header,.wp-block-query-title{display:none!important}body{margin:0!important;padding:0!important}"

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,500;1,600&display=swap">'

PREFIX = ("<!-- wp:html -->\n<style>\n" + BLOCK0_STYLE + "\n</style>\n<script>\n" + CLEAN_JS +
          "\n</script>\n<!-- /wp:html --><!-- wp:html -->\n" + FONTS + "\n<style>\n" +
          css + JETPACK + HIDE + "\n</style>\n<!-- /wp:html --><!-- wp:html -->\n")
SUFFIX = "\n<!-- /wp:html -->"

def fixhrefs(b):
    # /../  -> /
    b = b.replace('href="/../"', 'href="/"')
    b = b.replace("href='/../'", 'href="/"')
    # bare ../../ or ../ -> /
    b = re.sub(r'''href=(['"])(?:\.\./)+\1''', r'href="/"', b)
    # ../../<any/path>/<last-slug>/  -> /<last-slug>/  (WP pages are flat)
    b = re.sub(r'''href=(['"])(?:\.\./)+(?:[a-z0-9\-]+/)*([a-z0-9\-]+)/\1''', r'href="/\2/"', b)
    return b

manifest = []
for fn in sorted(os.listdir(BODIES)):
    if not fn.endswith(".html"): continue
    slug = fn[:-5]
    body = open(os.path.join(BODIES, fn)).read()
    body = fixhrefs(body)
    page = PREFIX + body + SUFFIX
    open(os.path.join(OUT, fn), "w").write(page)
    manifest.append({"slug": slug, "bytes": len(page)})

# check for any remaining relative hrefs
import glob
leftover = {}
for f in glob.glob(os.path.join(OUT,"*.html")):
    m = re.findall(r'href=[\'"][^\'"]*\.\./[^\'"]*[\'"]', open(f).read())
    if m: leftover[os.path.basename(f)] = m[:3]

json.dump(manifest, open(os.path.join(OUT,"_manifest.json"),"w"), indent=1)
print("pages:", len(manifest))
print("prefix bytes:", len(PREFIX))
print("leftover relative hrefs:", json.dumps(leftover, indent=1) if leftover else "none")
print("sample sizes:", [ (m["slug"], m["bytes"]) for m in manifest[:5] ])
