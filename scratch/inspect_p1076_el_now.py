import requests
import json
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r_admin = session.get('https://bolouplive.com/wp-admin/')
nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', r_admin.text).group(1)

req = requests.get('https://bolouplive.com/wp-json/wp/v2/pages/1076?context=edit', headers={'X-WP-Nonce': nonce}, cookies=session.cookies)
p = req.json()
el = p.get('meta', {}).get('_elementor_data', '')

print("Has 821 in el:", '8212868780' in el)
print("Has 823 in el:", '82371383705' in el)

# Find where 821 is in el
if '8212868780' in el:
    for m in re.finditer(r'.{0,40}8212868780.{0,40}', el):
        print("  el match:", m.group(0))
else:
    print("821 is NOT in _elementor_data!")

