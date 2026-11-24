import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

import re
nonce = re.search(r'name=["\']_wpnonce["\']\s+value=["\']([^"\']+)["\']', r_widget.text).group(1)
print("Nonce:", nonce)

# Test 1: Just basic fields
d1 = {
    'option_page': 'chaty-app',
    'action': 'update',
    '_wpnonce': nonce,
    '_wp_http_referer': '/wp-admin/admin.php?page=chaty-app&widget=0'
}
r1 = session.post('https://bolouplive.com/wp-admin/options.php', data=d1, headers={'Referer': widget_url})
print("Test 1 status:", r1.status_code, "URL:", r1.url)

