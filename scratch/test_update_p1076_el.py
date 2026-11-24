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

req_get = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages/1076?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req_get) as resp:
    p1076 = json.loads(resp.read().decode('utf-8'))

el_data = p1076.get('meta', {}).get('_elementor_data', '')
print("Has 821 in el_data:", '8212868780' in el_data)
print("Has 823 in el_data:", '82371383705' in el_data)
if '8212868780' in el_data:
    # Let's inspect how it is formatted
    el_obj = json.loads(el_data)
    el_str = json.dumps(el_obj)
    el_str_new = el_str.replace('8212868780', '82371383705').replace('8212 8687 80', '823 7138 3705')
    
    # Update via REST API with meta
    req_update = urllib.request.Request(
        'https://bolouplive.com/wp-json/wp/v2/pages/1076',
        data=json.dumps({'meta': {'_elementor_data': el_str_new}}).encode('utf-8'),
        headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
        method='POST'
    )
    with opener.open(req_update) as uresp:
        ures = json.loads(uresp.read().decode('utf-8'))
        print("Updated el_data result:", '82371383705' in ures.get('meta', {}).get('_elementor_data', ''))

