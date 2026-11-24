import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Let's inspect options.php or wp-admin/options.php
# In WP, options-general.php or options.php?all=1 exists if admin
r = session.get('https://bolouplive.com/wp-admin/options.php')
print("options.php GET status:", r.status_code)
# Search for cht_ or chaty_ in options.php
options = re.findall(r'name=["\'](cht_[^"\']+|chaty_[^"\']*)["\']', r.text)
print("Chaty options found in wp options.php:", set(options))

