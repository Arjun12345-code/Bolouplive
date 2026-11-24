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

editor_url = 'https://bolouplive.com/wp-admin/post.php?post=1743&action=elementor'
with opener.open(urllib.request.Request(editor_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    editor_html = resp.read().decode('utf-8', errors='ignore')

# Search for elements in initial_document
elem_m = re.search(r'"elements":(\[.*?\])\s*,\s*"widgets"', editor_html)
if elem_m:
    print("Found elements in initial_document:")
    s = elem_m.group(1)
    print("Has boloup-brand:", 'boloup-brand' in s)
    print("Has boloup-go-brand:", 'boloup-go-brand' in s)
else:
    print("elements not matched with regex, searching boloup in editor_html:")
    for m in re.finditer(r'boloup[^"\']*\.png', editor_html):
        print("Found:", m.group(0))

