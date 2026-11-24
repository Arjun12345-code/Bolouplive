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

def get_post_details(pid, post_type='elementor_library'):
    url = f'https://bolouplive.com/wp-json/wp/v2/{post_type}/{pid}?context=edit'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
    with opener.open(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

header_data = get_post_details(1743)
footer_data = get_post_details(1719)
kit_data = get_post_details(7)

print("=== HEADER 1743 ===")
print("Meta keys:", list(header_data.get('meta', {}).keys()))
h_el = header_data.get('meta', {}).get('_elementor_data', '')
print("Header _elementor_data snippet:", h_el[:300])

print("=== FOOTER 1719 ===")
f_el = footer_data.get('meta', {}).get('_elementor_data', '')
print("Footer _elementor_data snippet:", f_el[:300])

print("=== DEFAULT KIT 7 ===")
kit_page_settings = kit_data.get('meta', {}).get('_elementor_page_settings', '')
print("Kit settings snippet:", kit_page_settings[:300])
if kit_page_settings:
    settings = json.loads(kit_page_settings)
    custom_css = settings.get('custom_css', '')
    print("Kit custom_css length:", len(custom_css))
    print("Kit custom_css snippet:", custom_css[:300])

