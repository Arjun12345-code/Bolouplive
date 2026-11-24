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
print("Got nonce:", nonce)

# Prepare updated header HTML
with open('header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

# Replace local image with uploaded live URL
header_html = header_html.replace('assets/images/boloup-go-brand.png', 'https://bolouplive.com/wp-content/uploads/2026/11/boloup-go-brand.png')

# Load previous structure of 1743
with open('scratch/h1743_el_data.json', 'r', encoding='utf-8') as f:
    h_meta = json.load(f)
    h_el_data = json.loads(h_meta['_elementor_data'])

h_el_data[0]['elements'][0]['settings']['html'] = header_html

update_payload = {
    'meta': {
        '_elementor_data': json.dumps(h_el_data)
    }
}

req = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/1743',
    data=json.dumps(update_payload).encode('utf-8'),
    headers={
        'User-Agent': 'Mozilla/5.0',
        'X-WP-Nonce': nonce,
        'Content-Type': 'application/json'
    },
    method='POST'
)

try:
    with opener.open(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Updated Header 1743 successfully! Modified:", res.get('modified'))
except Exception as e:
    print("Update error:", e)
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8', errors='ignore'))

