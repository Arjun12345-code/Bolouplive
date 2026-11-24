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

def get_post_data(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
    with opener.open(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

h = get_post_data('https://bolouplive.com/wp-json/wp/v2/elementor_library/1743?context=edit')
f = get_post_data('https://bolouplive.com/wp-json/wp/v2/elementor_library/1719?context=edit')
p = get_post_data('https://bolouplive.com/wp-json/wp/v2/pages/648?context=edit')

for name, item in [('Header 1743', h), ('Footer 1719', f), ('Page 648', p)]:
    el_data = item.get('meta', {}).get('_elementor_data', '')
    print(f"=== {name} ===")
    img_srcs = re.findall(r'src=["\']([^"\']+)["\']', el_data)
    print("Images found:", set(img_srcs))

