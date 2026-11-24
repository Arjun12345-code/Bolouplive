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

# Load image mapping
with open('scratch/image_mapping.json', 'r', encoding='utf-8') as f:
    img_map = json.load(f)

# 1. Prepare Footer HTML
with open('footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

for local_path, live_url in img_map.items():
    footer_html = footer_html.replace(local_path, live_url)

with open('scratch/f1719_el_data.json', 'r', encoding='utf-8') as f:
    f_meta = json.load(f)
    f_el_data = json.loads(f_meta['_elementor_data'])

f_el_data[0]['elements'][0]['settings']['html'] = footer_html

req_footer = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/1719',
    data=json.dumps({'meta': {'_elementor_data': json.dumps(f_el_data)}}).encode('utf-8'),
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
    method='POST'
)
res_footer = opener.open(req_footer)
print("Footer 1719 updated successfully! Status:", res_footer.status)

# 2. Prepare Home (Page 648) HTML
with open('index.html', 'r', encoding='utf-8') as f:
    index_raw = f.read()

m = re.search(r'<body[^>]*>(.*?)</body>', index_raw, re.DOTALL | re.I)
body_html = m.group(1).strip()

for local_path, live_url in img_map.items():
    body_html = body_html.replace(local_path, live_url)

with open('scratch/p648_el_data.json', 'r', encoding='utf-8') as f:
    p_meta = json.load(f)
    p_el_data = json.loads(p_meta['_elementor_data'])

p_el_data[0]['elements'][0]['settings']['html'] = body_html

payload_648 = {
    'title': 'BoloUp App Host – Go Live & Earn',
    'content': body_html,
    'meta': {
        '_elementor_data': json.dumps(p_el_data)
    }
}

req_home = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/pages/648',
    data=json.dumps(payload_648).encode('utf-8'),
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
    method='POST'
)
res_home = opener.open(req_home)
print("Home 648 updated successfully! Status:", res_home.status)

# 3. Elementor clear cache
req_tools = urllib.request.Request('https://bolouplive.com/wp-admin/admin.php?page=elementor-tools', headers={'User-Agent': 'Mozilla/5.0'})
tools_html = opener.open(req_tools).read().decode('utf-8', errors='ignore')
nonce_match = re.search(r'data-nonce="([^"]+)"[^>]*id="elementor-clear-cache-button"', tools_html)
if not nonce_match:
    nonce_match = re.search(r'id="elementor-clear-cache-button"[^>]*data-nonce="([^"]+)"', tools_html)
if nonce_match:
    clear_cache_nonce = nonce_match.group(1)
    ajax_data = urllib.parse.urlencode({'action': 'elementor_clear_cache', '_nonce': clear_cache_nonce}).encode('utf-8')
    ajax_req = urllib.request.Request('https://bolouplive.com/wp-admin/admin-ajax.php', data=ajax_data, headers={'User-Agent': 'Mozilla/5.0'})
    print("Elementor clear cache:", opener.open(ajax_req).read().decode('utf-8'))

# 4. LiteSpeed Cache purge all
dash_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
dash_html = opener.open(dash_req).read().decode('utf-8', errors='ignore')
lsc_match = re.search(r'LSCWP_NONCE=([a-f0-9]+)', dash_html)
if lsc_match:
    lsc_nonce = lsc_match.group(1)
    for ptype in ['purge_all', 'purge_all_cssjs']:
        purge_url = f'https://bolouplive.com/wp-admin/index.php?LSCWP_CTRL=purge&LSCWP_NONCE={lsc_nonce}&litespeed_type={ptype}'
        opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'}))
    print("LiteSpeed Cache purged all!")

print("\n--- ALL UPDATES COMPLETED ON LIVE WORDPRESS SITE ---")

