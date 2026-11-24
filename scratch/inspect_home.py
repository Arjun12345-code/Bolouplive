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

# Fetch page 648
p_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages/648?context=edit', headers={
    'User-Agent': 'Mozilla/5.0',
    'X-WP-Nonce': nonce
})
with opener.open(p_req) as resp:
    page_data = json.loads(resp.read().decode('utf-8'))
    print("Page 648 keys:", list(page_data.keys()))
    print("Page content length:", len(page_data.get('content', {}).get('raw', '')))
    print("Page raw content snippet:", page_data.get('content', {}).get('raw', '')[:500])
    print("Meta keys:", list(page_data.get('meta', {}).keys()))

# Check plugins or active theme
plugins_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/plugins', headers={
    'User-Agent': 'Mozilla/5.0',
    'X-WP-Nonce': nonce
})
try:
    with opener.open(plugins_req) as resp:
        plugins = json.loads(resp.read().decode('utf-8'))
        print("Active plugins:", [p.get('plugin') for p in plugins if p.get('status') == 'active'])
except Exception as e:
    print("Plugins error:", e)

