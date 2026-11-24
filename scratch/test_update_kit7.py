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

# Get kit 7 current
req_get = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/elementor_library/7?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req_get) as resp:
    kit7 = json.loads(resp.read().decode('utf-8'))

ps = kit7['meta']['_elementor_page_settings']

with open('style.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

ps['custom_css'] = new_css

req_update = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/7',
    data=json.dumps({'meta': {'_elementor_page_settings': ps}}).encode('utf-8'),
    headers={
        'User-Agent': 'Mozilla/5.0',
        'X-WP-Nonce': nonce,
        'Content-Type': 'application/json'
    },
    method='POST'
)

try:
    with opener.open(req_update) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Kit 7 updated successfully! Modified:", res.get('modified'))
        updated_ps = res['meta']['_elementor_page_settings']
        print("Updated CSS length in Kit 7:", len(updated_ps.get('custom_css', '')))
        print("Has '#100524' (Midnight Purple):", '#100524' in updated_ps.get('custom_css', ''))
except Exception as e:
    print("Kit 7 update error:", e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8', errors='ignore'))

