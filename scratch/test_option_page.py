import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

# Let's see what whitelist options are in option_page: chaty-app
# Let's inspect options.php response when sending invalid nonce
r_test = session.post('https://bolouplive.com/wp-admin/options.php', data={'option_page': 'chaty-app', 'action': 'update'})
print("Status with option_page chaty-app:", r_test.status_code)
print("Snippet:", r_test.text[:300])

