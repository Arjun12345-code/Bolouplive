import re

with open('scratch/find_elementor_tools.py', 'r') as f:
    pass

import urllib.request
import urllib.parse
import http.cookiejar
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

req = urllib.request.Request('https://bolouplive.com/wp-admin/admin.php?page=elementor-tools', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

matches = re.findall(r'(.{0,100}(?:clear_cache|regenerate_css|elementor-button).*?.{0,100})', html, re.I)
for m in matches[:10]:
    print("Match:", m.strip())

