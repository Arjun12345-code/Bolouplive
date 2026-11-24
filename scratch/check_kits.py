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

req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/elementor_library/7?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req) as resp:
    kit = json.loads(resp.read().decode('utf-8'))
    ps = kit['meta']['_elementor_page_settings']
    print("Page settings keys:", list(ps.keys()))
    if 'custom_css' in ps:
        print("custom_css in Kit 7! Length:", len(ps['custom_css']))
        print("Snippet:", ps['custom_css'][:300])

# Check Kit 6 as well
req6 = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/elementor_library/6?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req6) as resp:
    kit6 = json.loads(resp.read().decode('utf-8'))
    ps6 = kit6['meta']['_elementor_page_settings']
    print("Kit 6 page settings keys:", list(ps6.keys()))
    if 'custom_css' in ps6:
        print("custom_css in Kit 6! Length:", len(ps6['custom_css']))
        print("Snippet:", ps6['custom_css'][:300])

