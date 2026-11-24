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

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

tools_url = 'https://bolouplive.com/wp-admin/admin.php?page=elementor-tools'
with opener.open(urllib.request.Request(tools_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    tools_html = resp.read().decode('utf-8', errors='ignore')

# Check script tags
scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', tools_html)
for s in scripts:
    if 'clear-cache' in s or 'elementor_clear_cache' in s or 'cef25f0c50' in s:
        print("Script snippet:", s[:300])

# Also check button data attributes
btn_match = re.search(r'<button[^>]*id="elementor-clear-cache-button"[^>]*>', tools_html)
if btn_match:
    print("Button HTML:", btn_match.group(0))

# Try clicking it via admin-ajax.php:
# In Elementor, action is often 'elementor_clear_cache' or 'elementor_ajax'
nonce_match = re.search(r'data-nonce="([^"]+)"[^>]*id="elementor-clear-cache-button"', tools_html)
if nonce_match:
    btn_nonce = nonce_match.group(1)
    print("Button data-nonce:", btn_nonce)
    
    # Try action elementor_clear_cache with this nonce
    ajax_url = 'https://bolouplive.com/wp-admin/admin-ajax.php'
    for act in ['elementor_clear_cache', 'elementor_reset_cache']:
        req_ajax = urllib.request.Request(
            ajax_url,
            data=urllib.parse.urlencode({'action': act, '_nonce': btn_nonce}).encode('utf-8'),
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        try:
            with opener.open(req_ajax) as resp:
                print(f"Action {act} result:", resp.read().decode('utf-8'))
        except Exception as e:
            print(f"Action {act} error:", e)

