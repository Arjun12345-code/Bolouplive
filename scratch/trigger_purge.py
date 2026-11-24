import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

# 1. Fetch elementor-tools page to get fresh nonce for clear cache
req_tools = urllib.request.Request('https://bolouplive.com/wp-admin/admin.php?page=elementor-tools', headers={'User-Agent': 'Mozilla/5.0'})
tools_html = opener.open(req_tools).read().decode('utf-8', errors='ignore')

nonce_match = re.search(r'id="elementor-clear-cache-button"[^>]*data-nonce="([^"]+)"', tools_html)
if not nonce_match:
    nonce_match = re.search(r'data-nonce="([^"]+)"[^>]*id="elementor-clear-cache-button"', tools_html)
clear_cache_nonce = nonce_match.group(1) if nonce_match else None
print("Elementor clear cache nonce:", clear_cache_nonce)

if clear_cache_nonce:
    ajax_data = urllib.parse.urlencode({
        'action': 'elementor_clear_cache',
        '_nonce': clear_cache_nonce
    }).encode('utf-8')
    ajax_req = urllib.request.Request('https://bolouplive.com/wp-admin/admin-ajax.php', data=ajax_data, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = opener.open(ajax_req).read().decode('utf-8')
        print("Elementor clear cache response:", res)
    except Exception as e:
        print("Elementor clear cache error:", e)

# 2. Get fresh LiteSpeed purge nonce from dashboard
dash_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
dash_html = opener.open(dash_req).read().decode('utf-8', errors='ignore')

lsc_match = re.search(r'LSCWP_NONCE=([a-f0-9]+)', dash_html)
if lsc_match:
    lsc_nonce = lsc_match.group(1)
    print("LiteSpeed nonce:", lsc_nonce)
    purge_url = f'https://bolouplive.com/wp-admin/index.php?LSCWP_CTRL=purge&LSCWP_NONCE={lsc_nonce}&litespeed_type=purge_all'
    try:
        purge_res = opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'}))
        print("LiteSpeed purge status:", purge_res.status)
    except Exception as e:
        print("LiteSpeed purge error:", e)

# 3. Check live site now
req_live = urllib.request.Request('https://bolouplive.com/?v=' + str(re.sub(r'\D', '', str(clear_cache_nonce))), headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req_live, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    print("boloup-go-brand.png in live site:", 'boloup-go-brand.png' in html)
    print("About Agency in live site:", 'About Agency' in html)
    print("bd52e5xj in live site:", 'bd52e5xj' in html)

