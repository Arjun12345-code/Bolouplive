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
login_req = urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
opener.open(login_req)

# Get wp-admin to fetch rest nonce
admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce_match = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html)
nonce = nonce_match.group(1) if nonce_match else None
print("REST Nonce:", nonce)

# Fetch pages
pages_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages?per_page=20', headers={
    'User-Agent': 'Mozilla/5.0',
    'X-WP-Nonce': nonce if nonce else ''
})
with opener.open(pages_req) as resp:
    pages = json.loads(resp.read().decode('utf-8'))
    for p in pages:
        print(f"ID: {p['id']}, Title: {p['title']['rendered']}, Slug: {p['slug']}, Status: {p['status']}")

