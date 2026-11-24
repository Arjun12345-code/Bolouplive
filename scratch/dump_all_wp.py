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

p648 = get_post_data('https://bolouplive.com/wp-json/wp/v2/pages/648?context=edit')
h1743 = get_post_data('https://bolouplive.com/wp-json/wp/v2/elementor_library/1743?context=edit')
f1719 = get_post_data('https://bolouplive.com/wp-json/wp/v2/elementor_library/1719?context=edit')
k7 = get_post_data('https://bolouplive.com/wp-json/wp/v2/elementor_library/7?context=edit')

with open('scratch/p648_el_data.json', 'w', encoding='utf-8') as out:
    json.dump(p648['meta'], out, indent=2)

with open('scratch/h1743_el_data.json', 'w', encoding='utf-8') as out:
    json.dump(h1743['meta'], out, indent=2)

with open('scratch/f1719_el_data.json', 'w', encoding='utf-8') as out:
    json.dump(f1719['meta'], out, indent=2)

with open('scratch/k7_meta.json', 'w', encoding='utf-8') as out:
    json.dump(k7['meta'], out, indent=2)

print("Saved all raw meta to scratch!")

