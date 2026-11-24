import requests
import re
import time

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
})

# 1. Login
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
r_login = session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})
print("Login status:", r_login.status_code)
time.sleep(2)

# 2. Get widget page
widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)
print("Widget page status:", r_widget.status_code)
time.sleep(2)

form_html = re.search(r'<form[^>]*id=["\']cht-form["\'][^>]*>([\s\S]*?)</form>', r_widget.text).group(0)

# Extract inputs
data = []
for m in re.finditer(r'<input([^>]+)>', form_html):
    tag = m.group(1)
    name_m = re.search(r'name=["\']([^"\']+)["\']', tag)
    if not name_m:
        continue
    name = name_m.group(1)
    type_m = re.search(r'type=["\']([^"\']+)["\']', tag)
    itype = type_m.group(1).lower() if type_m else 'text'
    val_m = re.search(r'value=["\']([^"\']*)["\']', tag)
    val = val_m.group(1) if val_m else ''
    
    if itype in ['radio', 'checkbox']:
        if 'checked' in tag:
            data.append((name, val or '1'))
    elif itype in ['submit', 'button', 'file']:
        pass
    else:
        if name == 'cht_social_Link[value]':
            print(f"Old {name} = {val}")
            val = 'http://+6282371383705'
            print(f"New {name} = {val}")
        data.append((name, val))

for m in re.finditer(r'<select[^>]+name=["\']([^"\']+)["\'][^>]*>([\s\S]*?)</select>', form_html):
    name = m.group(1)
    opts = m.group(2)
    selected_m = re.search(r'<option[^>]+selected[^>]*value=["\']([^"\']*)["\']', opts)
    if selected_m:
        data.append((name, selected_m.group(1)))
    else:
        first_m = re.search(r'<option[^>]*value=["\']([^"\']*)["\']', opts)
        if first_m:
            data.append((name, first_m.group(1)))

for m in re.finditer(r'<textarea[^>]+name=["\']([^"\']+)["\'][^>]*>([\s\S]*?)</textarea>', form_html):
    name = m.group(1)
    val = m.group(2).strip()
    data.append((name, val))

action = 'https://bolouplive.com/wp-admin/options.php'
print(f"Submitting form to {action}...")

r_post = session.post(action, data=data, headers={'Referer': widget_url})
print("Submit status:", r_post.status_code)
print("Submit URL:", r_post.url)
if r_post.status_code != 200:
    print("Submit snippet:", r_post.text[:300])

time.sleep(2)
# 3. Check widget page again
r_check = session.get(widget_url)
print("Check widget page:")
print("  Contains 8212868780:", '8212868780' in r_check.text)
print("  Contains 82371383705:", '82371383705' in r_check.text)

