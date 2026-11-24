import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import json
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Login
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)

def get_post_details(pid, post_type='elementor_library'):
    url = f'https://bolouplive.com/wp-json/wp/v2/{post_type}/{pid}?context=edit'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
    with opener.open(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

kit_data = get_post_details(7)
meta = kit_data.get('meta', {})
print("Kit meta keys:", list(meta.keys()))
for k, v in meta.items():
    if isinstance(v, dict):
        print(f"Meta {k}: (dict with keys {list(v.keys())[:10]})")
    elif isinstance(v, str):
        print(f"Meta {k}: length {len(v)}, start: {v[:100]}")
    else:
        print(f"Meta {k}: type {type(v)}")

# Check custom css post in WP
css_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/custom_css', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
try:
    with opener.open(css_req) as resp:
        custom_css_posts = json.loads(resp.read().decode('utf-8'))
        print("custom_css posts:", len(custom_css_posts))
        for c in custom_css_posts:
            print("CSS post ID:", c['id'], "Content len:", len(c['content']['raw']))
except Exception as e:
    print("custom_css error:", e)

