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

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

# Request frontend home as logged in user
home_req = urllib.request.Request('https://bolouplive.com/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(home_req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Logged-in user view:")
print("boloup-brand.png in html:", 'boloup-brand.png' in html)
print("boloup-go-brand.png in html:", 'boloup-go-brand.png' in html)

