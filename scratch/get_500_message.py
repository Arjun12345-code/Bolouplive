import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

nonce = re.search(r'name=["\']_wpnonce["\']\s+value=["\']([^"\']+)["\']', r_widget.text).group(1)

fields = [
    ('option_page', 'chaty-app'),
    ('action', 'update'),
    ('_wpnonce', nonce),
    ('_wp_http_referer', '/wp-admin/admin.php?page=chaty-app&widget=0'),
    ('cht_numb_slug', 'Telegram,Whatsapp,Link,'),
    ('widget', '0'),
]

r = session.post('https://bolouplive.com/wp-admin/options.php', data=fields, headers={'Referer': widget_url})
m = re.search(r'<div class="wp-die-message">(.*?)</div>', r.text, re.DOTALL)
if m:
    print("WP Die Message:", m.group(1).strip())
else:
    # Print body
    body_m = re.search(r'<body[^>]*>(.*?)</body>', r.text, re.DOTALL)
    if body_m:
        print("Body text:", re.sub(r'<[^>]+>', ' ', body_m.group(1)).strip())
    else:
        print("Full text:", r.text)
