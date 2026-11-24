import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import json
import re
import os

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
print("Got nonce:", nonce)

filepath = 'c:/Users/asus/Desktop/WordPress/Bolouplive/assets/images/boloup-brand.png'
filename = os.path.basename(filepath)
mime = 'image/png'

with open(filepath, 'rb') as f:
    img_bytes = f.read()

upload_url = 'https://bolouplive.com/wp-json/wp/v2/media'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'X-WP-Nonce': nonce,
    'Content-Type': mime,
    'Content-Disposition': f'attachment; filename="{filename}"'
}

req = urllib.request.Request(upload_url, data=img_bytes, headers=headers, method='POST')
try:
    with opener.open(req) as resp:
        res_data = json.loads(resp.read().decode('utf-8'))
        source_url = res_data.get('source_url')
        print("Uploaded successfully! Live URL:", source_url)
        with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/uploaded_brand_logo.json', 'w') as out:
            json.dump(res_data, out, indent=2)
except Exception as e:
    print("Upload error:", e)

