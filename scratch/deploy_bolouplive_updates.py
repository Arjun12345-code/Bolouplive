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

# 1. Login to WordPress
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)
print("Got WP REST Nonce:", nonce)

# Load image mapping
with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/image_mapping.json', 'r', encoding='utf-8') as f:
    img_map = json.load(f)

# 2. Update Elementor Kit 7 Custom CSS (sitewide stylesheet)
with open('c:/Users/asus/Desktop/WordPress/Bolouplive/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

# Replace any local asset paths in style.css if any
for local_path, live_url in img_map.items():
    style_css = style_css.replace(local_path, live_url)

req_kit_get = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/7?context=edit',
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce}
)
with opener.open(req_kit_get) as resp:
    kit7 = json.loads(resp.read().decode('utf-8'))

ps = kit7['meta']['_elementor_page_settings']
ps['custom_css'] = style_css

req_kit_update = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/elementor_library/7',
    data=json.dumps({'meta': {'_elementor_page_settings': ps}}).encode('utf-8'),
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
    method='POST'
)
with opener.open(req_kit_update) as resp:
    print("Kit 7 Custom CSS updated! Status:", resp.status)

# 3. Update Footer Template (Post 1719) with 4 columns and full-width container
with open('c:/Users/asus/Desktop/WordPress/Bolouplive/footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

for local_path, live_url in img_map.items():
    footer_html = footer_html.replace(local_path, live_url)

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/f1719_el_data.json', 'r', encoding='utf-8') as f:
    f_meta = json.load(f)
    f_el_data = json.loads(f_meta['_elementor_data'])

# Set container to full width
f_el_data[0]['settings'] = {
    'content_width': 'full',
    'boxed_width': {'unit': 'px', 'size': ''},
    'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
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

# 4. Clear Elementor CSS cache
req_tools = urllib.request.Request('https://bolouplive.com/wp-admin/admin.php?page=elementor-tools', headers={'User-Agent': 'Mozilla/5.0'})
tools_html = opener.open(req_tools).read().decode('utf-8', errors='ignore')
nonce_match = re.search(r'data-nonce="([^"]+)"[^>]*id="elementor-clear-cache-button"', tools_html) or re.search(r'id="elementor-clear-cache-button"[^>]*data-nonce="([^"]+)"', tools_html)
if nonce_match:
    clear_cache_nonce = nonce_match.group(1)
    ajax_data = urllib.parse.urlencode({'action': 'elementor_clear_cache', '_nonce': clear_cache_nonce}).encode('utf-8')
    ajax_req = urllib.request.Request('https://bolouplive.com/wp-admin/admin-ajax.php', data=ajax_data, headers={'User-Agent': 'Mozilla/5.0'})
    print("Elementor clear cache response:", opener.open(ajax_req).read().decode('utf-8'))

# 5. Purge LiteSpeed Cache
dash_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
dash_html = opener.open(dash_req).read().decode('utf-8', errors='ignore')
purge_match = re.search(r'href="([^"]*litespeed-purge=all[^"]*)"', dash_html)
if purge_match:
    purge_url = purge_match.group(1).replace('&amp;', '&')
    r_purge = opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'}))
    print("LiteSpeed purge all status:", r_purge.status)
else:
    print("LiteSpeed purge link not in dashboard, trying generic purge...")
    matches = [m for m in re.findall(r'href="([^"]+)"', dash_html) if 'purge' in m.lower()]
    for m in matches:
        opener.open(urllib.request.Request(m.replace('&amp;', '&'), headers={'User-Agent': 'Mozilla/5.0'}))
        print("Triggered purge URL:", m)

print("Deploy finished successfully!")

