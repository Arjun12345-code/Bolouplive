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

req1743 = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/elementor_library/1743?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req1743) as resp:
    p1743 = json.loads(resp.read().decode('utf-8'))
    el1743 = p1743.get('meta', {}).get('_elementor_data', '')
    print("boloup-brand.png in 1743:", 'boloup-brand.png' in el1743)
    print("boloup-go-brand.png in 1743:", 'boloup-go-brand.png' in el1743)

req1719 = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/elementor_library/1719?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req1719) as resp:
    p1719 = json.loads(resp.read().decode('utf-8'))
    el1719 = p1719.get('meta', {}).get('_elementor_data', '')
    print("boloup-brand.png in 1719:", 'boloup-brand.png' in el1719)
    print("boloup-go-brand.png in 1719:", 'boloup-go-brand.png' in el1719)

