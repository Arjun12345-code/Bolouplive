import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Login
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

# Fetch widget edit page
widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
with opener.open(urllib.request.Request(widget_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    page_html = resp.read().decode('utf-8', errors='ignore')

# Extract form action="options.php"
form_m = re.search(r'<form[^>]*action=["\']options\.php["\'][^>]*>([\s\S]*?)</form>', page_html)
if not form_m:
    print("Form not found!")
    exit(1)

form_html = form_m.group(1)

# Extract all input fields (text, hidden, radio, checkbox, etc.)
fields = []

# Inputs
for tag in re.finditer(r'<input([^>]+)>', form_html):
    attrs = tag.group(1)
    name_m = re.search(r'name=["\']([^"\']+)["\']', attrs)
    if not name_m:
        continue
    name = name_m.group(1)
    type_m = re.search(r'type=["\']([^"\']+)["\']', attrs)
    itype = type_m.group(1).lower() if type_m else 'text'
    val_m = re.search(r'value=["\']([^"\']*)["\']', attrs)
    val = val_m.group(1) if val_m else ''
    
    if itype in ['radio', 'checkbox']:
        if 'checked' in attrs:
            fields.append((name, val))
    else:
        fields.append((name, val))

# Selects
for tag in re.finditer(r'<select[^>]+name=["\']([^"\']+)["\'][^>]*>([\s\S]*?)</select>', form_html):
    name = tag.group(1)
    opts = tag.group(2)
    selected_m = re.search(r'<option[^>]+selected[^>]*value=["\']([^"\']*)["\']', opts)
    if selected_m:
        fields.append((name, selected_m.group(1)))
    else:
        first_m = re.search(r'<option[^>]*value=["\']([^"\']*)["\']', opts)
        if first_m:
            fields.append((name, first_m.group(1)))

# Textareas
for tag in re.finditer(r'<textarea[^>]+name=["\']([^"\']+)["\'][^>]*>([\s\S]*?)</textarea>', form_html):
    name = tag.group(1)
    val = tag.group(2)
    fields.append((name, val))

print(f"Total fields extracted: {len(fields)}")

# Now replace the value in fields
updated_fields = []
replaced_count = 0
for name, val in fields:
    if '8212868780' in val:
        new_val = val.replace('8212868780', '82371383705')
        print(f"Replacing {name}: '{val}' -> '{new_val}'")
        updated_fields.append((name, new_val))
        replaced_count += 1
    else:
        updated_fields.append((name, val))

print(f"Replaced fields count: {replaced_count}")

# Encode and POST to options.php
post_data = urllib.parse.urlencode(updated_fields).encode('utf-8')
post_req = urllib.request.Request(
    'https://bolouplive.com/wp-admin/options.php',
    data=post_data,
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': widget_url
    }
)

with opener.open(post_req) as resp:
    print("options.php response code:", resp.status)
    print("Final URL:", resp.geturl())

# Verify on widget page again
with opener.open(urllib.request.Request(widget_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    check_html = resp.read().decode('utf-8', errors='ignore')
    print("Verified on widget page:")
    print("  Has 8212868780:", '8212868780' in check_html)
    print("  Has 82371383705:", '82371383705' in check_html)

