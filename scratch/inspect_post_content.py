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

for pid in [1743, 1719]:
    req = urllib.request.Request(f'https://bolouplive.com/wp-json/wp/v2/elementor_library/{pid}?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
    with opener.open(req) as resp:
        p = json.loads(resp.read().decode('utf-8'))
        content_raw = p.get('content', {}).get('raw', '')
        content_rendered = p.get('content', {}).get('rendered', '')
        print(f"=== POST {pid} ===")
        print("content raw has boloup-go-brand:", 'boloup-go-brand' in content_raw)
        print("content rendered has boloup-go-brand:", 'boloup-go-brand' in content_rendered)
        print("content raw has boloup-brand:", 'boloup-brand.png' in content_raw)
        print("content rendered has boloup-brand:", 'boloup-brand.png' in content_rendered)

