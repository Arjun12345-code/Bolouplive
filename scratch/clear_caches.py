import urllib.request
import urllib.parse
import http.cookiejar
import ssl
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

# 1. Clear Elementor cache
ajax_nonce_m = re.search(r'var\s+elementorCommon\s*=\s*\{.*?"ajax":\{"url":".*?","nonce":"([^"]+)"\}', admin_html)
if ajax_nonce_m:
    nonce = ajax_nonce_m.group(1)
    clear_url = 'https://bolouplive.com/wp-admin/admin-ajax.php'
    clear_data = urllib.parse.urlencode({
        'action': 'elementor_clear_cache',
        '_nonce': nonce
    }).encode('utf-8')
    req_clear = urllib.request.Request(clear_url, data=clear_data, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req_clear) as resp:
        print("Elementor clear cache:", resp.read().decode('utf-8', errors='ignore'))

# 2. Clear LiteSpeed cache
purge_all_m = re.search(r'href=["\'](https://bolouplive\.com/wp-admin/index\.php\?LSCWP_CTRL=purge[^\'"]*litespeed_type=purge_all(?:_cssjs)?[^\'"]*)["\']', admin_html)
if purge_all_m:
    purge_url = purge_all_m.group(1).replace('&#038;', '&')
    print("Purging LiteSpeed via:", purge_url)
    with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        print("LiteSpeed purge status:", resp.status)

# Also purge CSS/JS
purge_cssjs_m = re.search(r'href=["\'](https://bolouplive\.com/wp-admin/index\.php\?LSCWP_CTRL=purge[^\'"]*litespeed_type=purge_all_cssjs[^\'"]*)["\']', admin_html)
if purge_cssjs_m:
    purge_cssjs_url = purge_cssjs_m.group(1).replace('&#038;', '&')
    print("Purging CSS/JS via:", purge_cssjs_url)
    with opener.open(urllib.request.Request(purge_cssjs_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        print("LiteSpeed purge CSS/JS status:", resp.status)

