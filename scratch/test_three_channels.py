import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

nonce = re.search(r'name=["\']_wpnonce["\']\s+value=["\']([^"\']+)["\']', r_widget.text).group(1)

# Extract only channel fields and required options
fields = [
    ('option_page', 'chaty-app'),
    ('action', 'update'),
    ('_wpnonce', nonce),
    ('_wp_http_referer', '/wp-admin/admin.php?page=chaty-app&widget=0'),
    ('cht_numb_slug', 'Telegram,Whatsapp,Link,'),
    ('widget', '0'),
]

for ch in ['Telegram', 'Whatsapp', 'Link']:
    ch_inputs = re.findall(rf'name=["\'](cht_social_{ch}\[[^\]]+\])["\']\s+value=["\']([^"\']*)["\']', r_widget.text)
    for k, v in ch_inputs:
        if k == 'cht_social_Link[value]':
            v = 'http://+6282371383705'
        fields.append((k, v))

# Also extract textareas for these 3 channels
for ch in ['Telegram', 'Whatsapp', 'Link']:
    ch_textareas = re.findall(rf'<textarea[^>]+name=["\'](cht_social_{ch}\[[^\]]+\])["\'][^>]*>([\s\S]*?)</textarea>', r_widget.text)
    for k, v in ch_textareas:
        fields.append((k, v.strip()))

# Also general settings that chaty expects
general_keys = [
    'cht_widget_size', 'cht_close_button', 'cht_position', 'cht_color', 'cht_custom_color',
    'cht_cta', 'cht_cta_switcher', 'cht_cta_action', 'cht_cta_text_color', 'cht_cta_bg_color',
    'cht_pending_messages', 'cht_active', 'cht_created_on', 'chaty_updated_on', 'save_button'
]
for k in general_keys:
    val_m = re.search(rf'name=["\']{k}["\'][^>]*value=["\']([^"\']*)["\']', r_widget.text)
    if val_m:
        fields.append((k, val_m.group(1)))

print(f"Total fields to send: {len(fields)}")
r = session.post('https://bolouplive.com/wp-admin/options.php', data=fields, headers={'Referer': widget_url})
print("Status:", r.status_code)
print("URL:", r.url)
if r.status_code == 500:
    print("500 text:", r.text[:500])

