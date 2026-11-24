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

tools_url = 'https://bolouplive.com/wp-admin/admin.php?page=elementor-tools'
with opener.open(urllib.request.Request(tools_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    tools_html = resp.read().decode('utf-8', errors='ignore')

# Search for regenerate css or clear cache buttons / forms
for m in re.finditer(r'<form[^>]*>([\s\S]*?)</form>', tools_html):
    f_html = m.group(0)
    if 'regenerate' in f_html.lower() or 'clear' in f_html.lower() or 'cache' in f_html.lower():
        print("Found form:")
        for line in f_html.splitlines():
            if any(k in line.lower() for k in ['input', 'button', 'action']):
                print("  ", line.strip())

