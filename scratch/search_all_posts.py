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

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)

# Check all post types in WP REST API
types = ['posts', 'pages', 'elementor_library']
for t in types:
    url = f'https://bolouplive.com/wp-json/wp/v2/{t}?per_page=100&context=edit'
    try:
        with opener.open(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})) as resp:
            items = json.loads(resp.read().decode('utf-8'))
            for item in items:
                item_str = json.dumps(item)
                if '8212868780' in item_str or '0821' in item_str:
                    print(f"FOUND in {t} ID {item.get('id')} ({item.get('slug')}):")
                    for m in re.finditer(r'.{0,40}(?:8212868780|0821).{0,40}', item_str):
                        print("   ", m.group(0))
    except Exception as e:
        print(f"Error checking {t}:", e)

