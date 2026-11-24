import requests
import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Trigger init hook by accessing wp-admin or home
r_home = session.get('https://bolouplive.com/')
print("Home status:", r_home.status_code)

# Check Chaty widget page
widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)
print("Chaty widget page check:")
print("  Contains 8212868780:", '8212868780' in r_widget.text)
print("  Contains 82371383705:", '82371383705' in r_widget.text)

# Check Contact Us page
r_contact = session.get('https://bolouplive.com/contact-us/')
print("Contact Us page check:")
print("  Contains 8212868780:", '8212868780' in r_contact.text)
print("  Contains 82371383705:", '82371383705' in r_contact.text)

# Check Home page frontend
print("Home page frontend check:")
print("  Contains 8212868780:", '8212868780' in r_home.text)
print("  Contains 82371383705:", '82371383705' in r_home.text)

# Clear LiteSpeed cache
r_admin = session.get('https://bolouplive.com/wp-admin/')
purge_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all["\'])', r_admin.text)
if purge_m:
    purge_url = purge_m.group(1)[:-1].replace('&#038;', '&')
    r_purge = session.get(purge_url)
    print("LiteSpeed cache purge status:", r_purge.status_code)

# Clear CSS/JS
purge_cssjs_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all_cssjs["\'])', r_admin.text)
if purge_cssjs_m:
    p_url = purge_cssjs_m.group(1)[:-1].replace('&#038;', '&')
    r_purge_css = session.get(p_url)
    print("LiteSpeed CSS/JS purge status:", r_purge_css.status_code)

