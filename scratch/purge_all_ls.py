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

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

# Find all LSCWP purge links
matches = re.findall(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*)["\']', admin_html)
print("Purge URLs found:")
for m in set(matches):
    url = m.replace('&#038;', '&')
    print("Trying purge:", url)
    try:
        with opener.open(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
            print("Status:", resp.status)
    except Exception as e:
        print("Error:", e)

# Also let's touch the front page post 648 (save/update) to invalidate its cache
nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)
req_touch = urllib.request.Request(
    'https://bolouplive.com/wp-json/wp/v2/pages/648',
    data=json.dumps({'title': 'BoloUp Live Host - Live, Get Gifts, Grow & Earn'}).encode('utf-8'),
    headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': nonce, 'Content-Type': 'application/json'},
    method='POST'
)
try:
    with opener.open(req_touch) as resp:
        print("Page 648 touched/updated! Status:", resp.status)
except Exception as e:
    print("Page 648 touch error:", e)

