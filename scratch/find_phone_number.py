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

# Login to WordPress
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)
print("Logged in, nonce:", nonce)

# 1. Check rendered pages: /, /contact-us/, /bio/
for path in ['/', '/contact-us/', '/bio/', '/blog/']:
    url = 'https://bolouplive.com' + path
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with opener.open(req) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            found = [m for m in re.finditer(r'.{0,30}(?:08212868780|8212868780|0821-2868-780).{0,30}', text)]
            if found:
                print(f"FOUND in URL {url}:")
                for f in found:
                    print("  ", f.group(0))
            else:
                print(f"Not found in HTML of {url}")
    except Exception as e:
        print(f"Error checking {url}:", e)

# 2. Check all pages via REST API
req_pages = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages?per_page=50&context=edit', headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce})
try:
    with opener.open(req_pages) as resp:
        pages = json.loads(resp.read().decode('utf-8'))
        for p in pages:
            raw_c = p.get('content', {}).get('raw', '')
            el_data = p.get('meta', {}).get('_elementor_data', '')
            if '8212868780' in raw_c or '8212868780' in el_data or '0821' in raw_c or '0821' in el_data:
                print(f"FOUND in Page ID {p['id']} ({p['slug']})!")
except Exception as e:
    print("Pages error:", e)

# 3. Check Chaty plugin admin page
chaty_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app'
try:
    with opener.open(urllib.request.Request(chaty_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        c_html = resp.read().decode('utf-8', errors='ignore')
        print("Chaty admin status 200, length:", len(c_html))
        if '8212868780' in c_html or '0821' in c_html:
            print("FOUND in Chaty admin page!")
            for m in re.finditer(r'.{0,40}(?:8212868780|0821).{0,40}', c_html):
                print("  Chaty snippet:", m.group(0))
        else:
            print("Chaty admin page doesn't directly show 8212868780, let's inspect widgets / settings")
except Exception as e:
    print("Chaty error:", e)

