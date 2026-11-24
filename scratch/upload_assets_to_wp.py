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

files_to_upload = [
    'assets/images/boloup-go-brand.png',
    'assets/images/boloup-host-role.png',
    'assets/images/boloup-ecosystem.png',
    'assets/images/BoloUp-Host-Registration-Guide-Step-1.jpg',
    'assets/images/BoloUp-Host-Registration-Guide-Step-2.jpg',
    'assets/images/BoloUp-Host-Registration-Guide-Step-3.jpg',
    'assets/images/BoloUp-Host-Registration-Guide-Step-4.jpg'
]

mapping = {}

for filepath in files_to_upload:
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()
    mime = 'image/png' if ext == '.png' else 'image/jpeg'
    
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
            data = json.loads(resp.read().decode('utf-8'))
            source_url = data.get('source_url')
            print(f"Uploaded {filename} -> {source_url}")
            mapping[filepath] = source_url
    except Exception as e:
        print(f"Failed to upload {filename}: {e}")

with open('scratch/image_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(mapping, f, indent=2)

print("\nSaved image mapping to scratch/image_mapping.json")

