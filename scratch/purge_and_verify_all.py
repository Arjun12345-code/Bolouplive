import requests
import re
import time

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Purge LiteSpeed
r_admin = session.get('https://bolouplive.com/wp-admin/')
purge_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all["\'])', r_admin.text)
if purge_m:
    purge_url = purge_m.group(1)[:-1].replace('&#038;', '&')
    r_purge = session.get(purge_url)
    print("LiteSpeed cache purge all status:", r_purge.status_code)

purge_cssjs_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all_cssjs["\'])', r_admin.text)
if purge_cssjs_m:
    p_url = purge_cssjs_m.group(1)[:-1].replace('&#038;', '&')
    r_purge_css = session.get(p_url)
    print("LiteSpeed CSS/JS purge status:", r_purge_css.status_code)

time.sleep(2)

# Check anonymous live requests
print("\n=== CHECKING ANONYMOUS LIVE REQUESTS ===")
for path in ['/', '/contact-us/', '/bio/', '/blog/']:
    url = 'https://bolouplive.com' + path
    r_anon = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    has_old = '8212868780' in r_anon.text
    has_new = '82371383705' in r_anon.text
    print(f"URL {path}: has_old_number={has_old}, has_new_number={has_new}")

