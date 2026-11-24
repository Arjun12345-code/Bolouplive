import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

tools_url = 'https://bolouplive.com/wp-admin/admin.php?page=elementor-tools'
r_tools = session.get(tools_url)

nonce_m = re.search(r'data-nonce="([^"]+)"[^>]*id="elementor-clear-cache-button"', r_tools.text)
if nonce_m:
    nonce = nonce_m.group(1)
    print("Clear cache nonce:", nonce)
    r_clear = session.post('https://bolouplive.com/wp-admin/admin-ajax.php', data={'action': 'elementor_clear_cache', '_nonce': nonce})
    print("Clear cache response:", r_clear.text)

# Also let's update page 1076 status to publish to trigger save hooks
r_admin = session.get('https://bolouplive.com/wp-admin/')
wp_nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', r_admin.text).group(1)

r_up = session.post('https://bolouplive.com/wp-json/wp/v2/pages/1076', json={'status': 'publish'}, headers={'X-WP-Nonce': wp_nonce})
print("Page 1076 touch status:", r_up.status_code)

# Check rendered content again
r_get = session.get('https://bolouplive.com/wp-json/wp/v2/pages/1076?context=edit', headers={'X-WP-Nonce': wp_nonce})
p = r_get.json()
print("Rendered content has 821 now:", '8212868780' in p['content']['rendered'])
print("Rendered content has 823 now:", '82371383705' in p['content']['rendered'])

