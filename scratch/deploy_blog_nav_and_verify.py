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
print("Got nonce:", nonce)

brand_logo_url = 'https://bolouplive.com/wp-content/uploads/2026/11/boloup-brand.png'

# 1. Update Header (1743)
with open('c:/Users/asus/Desktop/WordPress/Bolouplive/header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

header_html = header_html.replace('assets/images/boloup-brand.png', brand_logo_url)
header_html = header_html.replace('assets/images/boloup-go-brand.png', brand_logo_url)

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/h1743_el_data.json', 'r', encoding='utf-8') as f:
    h_meta = json.load(f)
    h_el_data = json.loads(h_meta['_elementor_data'])

h_el_data[0]['elements'][0]['settings']['html'] = header_html

req_header = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/1743',
    data=json.dumps({'meta': {'_elementor_data': json.dumps(h_el_data)}}).encode('utf-8'),
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
    method='POST'
)
with opener.open(req_header) as resp:
    print("Header 1743 updated! Status:", resp.status)

# 2. Update Footer (1719)
with open('c:/Users/asus/Desktop/WordPress/Bolouplive/footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

footer_html = footer_html.replace('assets/images/boloup-brand.png', brand_logo_url)
footer_html = footer_html.replace('assets/images/boloup-go-brand.png', brand_logo_url)

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/f1719_el_data.json', 'r', encoding='utf-8') as f:
    f_meta = json.load(f)
    f_el_data = json.loads(f_meta['_elementor_data'])

f_el_data[0]['settings'] = {
    'content_width': 'full'
}
f_el_data[0]['elements'][0]['settings']['html'] = footer_html

req_footer = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/1719',
    data=json.dumps({'meta': {'_elementor_data': json.dumps(f_el_data)}}).encode('utf-8'),
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
    method='POST'
)
with opener.open(req_footer) as resp:
    print("Footer 1719 updated! Status:", resp.status)

# 3. Clear Elementor Cache via admin-ajax.php
tools_url = 'https://bolouplive.com/wp-admin/admin.php?page=elementor-tools'
with opener.open(urllib.request.Request(tools_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    tools_html = resp.read().decode('utf-8', errors='ignore')

nonce_match = re.search(r'data-nonce="([^"]+)"[^>]*id="elementor-clear-cache-button"', tools_html)
if nonce_match:
    btn_nonce = nonce_match.group(1)
    clear_url = 'https://bolouplive.com/wp-admin/admin-ajax.php'
    req_clear = urllib.request.Request(
        clear_url,
        data=urllib.parse.urlencode({'action': 'elementor_clear_cache', '_nonce': btn_nonce}).encode('utf-8'),
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with opener.open(req_clear) as resp:
        print("Elementor clear cache response:", resp.read().decode('utf-8'))

# 4. Clear LiteSpeed Cache
purge_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all["\'])', admin_html)
if purge_m:
    purge_url = purge_m.group(1)[:-1].replace('&#038;', '&')
    print("Purging LiteSpeed via:", purge_url)
    with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        print("LiteSpeed purge completed! Status:", resp.status)

# Purge CSS/JS
purge_cssjs_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all_cssjs["\'])', admin_html)
if purge_cssjs_m:
    p_url = purge_cssjs_m.group(1)[:-1].replace('&#038;', '&')
    with opener.open(urllib.request.Request(p_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        print("LiteSpeed CSS/JS purge completed! Status:", resp.status)

print("All updates deployed successfully!")

