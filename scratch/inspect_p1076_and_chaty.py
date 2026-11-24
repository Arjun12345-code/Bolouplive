import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import json
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

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)

# Inspect Page 1076
req_p1076 = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages/1076?context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
with opener.open(req_p1076) as resp:
    p1076 = json.loads(resp.read().decode('utf-8'))
    with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/p1076.json', 'w', encoding='utf-8') as f:
        json.dump(p1076, f, indent=2)
    print("Saved p1076.json")
    
    # Check occurrences of 821 in p1076
    p_str = json.dumps(p1076)
    for m in re.finditer(r'.{0,40}(?:8212868780|0821).{0,40}', p_str):
        print("P1076 match:", m.group(0))

# Inspect Chaty options in wp_options or Chaty widget edit URL
# In Chaty, widget URL is usually admin.php?page=chaty-app&widget=... or admin.php?page=chaty-widget-settings
for path in ['/wp-admin/admin.php?page=chaty-app', '/wp-admin/admin.php?page=chaty-widgets']:
    try:
        with opener.open(urllib.request.Request('https://bolouplive.com' + path, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'href=["\']([^"\']*chaty[^"\']*)["\']', text)
            print(f"Chaty links in {path}:", set(urls))
    except Exception as e:
        print(f"Error {path}:", e)

