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

# Fetch page 1076 current
req_get = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages/1076?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req_get) as resp:
    p1076 = json.loads(resp.read().decode('utf-8'))

raw_content = p1076.get('content', {}).get('raw', '')
el_data = p1076.get('meta', {}).get('_elementor_data', '')

# Replace old number with new number:
# 08212868780 -> 082371383705
# +628212868780 -> +6282371383705
# +62 8212 8687 80 -> +62 823 7138 3705
new_raw = raw_content.replace('https://wa.me/+628212868780', 'https://wa.me/+6282371383705')
new_raw = new_raw.replace('https://wa.me/628212868780', 'https://wa.me/+6282371383705')
new_raw = new_raw.replace('+62 8212 8687 80', '+62 823 7138 3705')
new_raw = new_raw.replace('08212868780', '082371383705')

new_el = el_data.replace('https://wa.me/+628212868780', 'https://wa.me/+6282371383705')
new_el = new_el.replace('https://wa.me/628212868780', 'https://wa.me/+6282371383705')
new_el = new_el.replace('+62 8212 8687 80', '+62 823 7138 3705')
new_el = new_el.replace('08212868780', '082371383705')

update_payload = {
    'content': new_raw,
    'meta': {
        '_elementor_data': new_el
    }
}

req_update = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/pages/1076',
    data=json.dumps(update_payload).encode('utf-8'),
    headers={
        'User-Agent': 'Mozilla/5.0',
        'X-WP-Nonce': nonce,
        'Content-Type': 'application/json'
    },
    method='POST'
)

with opener.open(req_update) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("Page 1076 updated! Status:", resp.status)
    print("Old number in updated raw:", '8212868780' in res.get('content', {}).get('raw', ''))
    print("New number in updated raw:", '82371383705' in res.get('content', {}).get('raw', ''))
    print("New number in updated el_data:", '82371383705' in res.get('meta', {}).get('_elementor_data', ''))

