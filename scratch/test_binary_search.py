import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
r_widget = session.get(widget_url)

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
            val = 'http://+6282371383705'
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

# Add save_button
data.append(('save_button', 'Save Changes'))

# Test with 10 fields, 20 fields, etc. to see when 503 happens
for count in [5, 10, 20, 40, 60, 80, 100, len(data)]:
    sub_data = data[:count]
    r = session.post('https://bolouplive.com/wp-admin/options.php', data=sub_data, headers={'Referer': widget_url})
    print(f"Count {count}: status {r.status_code}")
    if r.status_code == 503:
        print("First failure at count:", count)
        break

