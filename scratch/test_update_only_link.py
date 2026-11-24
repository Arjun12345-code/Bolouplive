import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

nonce = re.search(r'name=["\']_wpnonce["\']\s+value=["\']([^"\']+)["\']', r_widget.text).group(1)

# Let's inspect what fields for cht_social_Link exist
link_fields = re.findall(r'name=["\'](cht_social_Link\[[^\]]+\])["\']\s+value=["\']([^"\']*)["\']', r_widget.text)
print("Link fields in form:")
d = {
    'option_page': 'chaty-app',
    'action': 'update',
    '_wpnonce': nonce,
    '_wp_http_referer': '/wp-admin/admin.php?page=chaty-app&widget=0',
    'cht_numb_slug': 'Telegram,Whatsapp,Link,',
}
for k, v in link_fields:
    if k == 'cht_social_Link[value]':
        v = 'http://+6282371383705'
    d[k] = v
    print(f"  {k} = {v}")

r = session.post('https://bolouplive.com/wp-admin/options.php', data=d, headers={'Referer': widget_url})
print("Status:", r.status_code)
print("URL:", r.url)

