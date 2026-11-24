import requests
import re
import time

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
    val_m = re.search(r'value=["\']([^"\']*)["\']', tag)
    val = val_m.group(1) if val_m else ''
    data.append((name, val))

for m in re.finditer(r'<textarea[^>]+name=["\']([^"\']+)["\'][^>]*>([\s\S]*?)</textarea>', form_html):
    data.append((m.group(1), m.group(2).strip()))

print(f"Total fields: {len(data)}")

bad_fields = []
for idx, (k, v) in enumerate(data):
    try:
        r = session.post('https://bolouplive.com/wp-admin/options.php', data={k: v})
        if r.status_code == 503:
            print(f"[{idx}] 503 ERROR on field: {k} = {v[:50]}")
            bad_fields.append((k, v))
        time.sleep(0.1)
    except Exception as e:
        print(f"[{idx}] Exception on field {k}:", e)

print("Bad fields found:", len(bad_fields))

