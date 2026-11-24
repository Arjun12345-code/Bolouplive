import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

nonce = re.search(r'name=["\']_wpnonce["\']\s+value=["\']([^"\']+)["\']', r_widget.text).group(1)

# In test_regular_post, why did it give 503?
# Could it be the number of fields, or one specific field?
# Let's check which field causes 503 by adding fields incrementally!

