import requests
import re
from html.parser import HTMLParser

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

# Login
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
r_login = session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})
print("Login status:", r_login.status_code)

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)
print("Widget page status:", r_widget.status_code)

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

# Extract selects
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

# Extract textareas
for m in re.finditer(r'<textarea[^>]+name=["\']([^"\']+)["\'][^>]*>([\s\S]*?)</textarea>', form_html):
    name = m.group(1)
    val = m.group(2).strip()
    data.append((name, val))

action = 'https://bolouplive.com/wp-admin/options.php'
print(f"Submitting {len(data)} fields as multipart...")

# Form multipart files dict
# In requests, multipart/form-data is triggered when `files` parameter is provided.
# Each non-file data item can be passed in `files` or `data`.
# When passing in files: {key: (None, value)}
multipart_payload = {}
for k, v in data:
    multipart_payload[k] = (None, str(v))

r_post = session.post(action, files=multipart_payload, headers={'Referer': widget_url})
print("Submit status:", r_post.status_code)
print("Final URL:", r_post.url)

# Verify on widget page
r_check = session.get(widget_url)
print("Has 8212868780:", '8212868780' in r_check.text)
print("Has 82371383705:", '82371383705' in r_check.text)
