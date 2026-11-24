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

# Check elementor features
exp_url = 'https://bolouplive.com/wp-admin/admin.php?page=elementor'
with opener.open(urllib.request.Request(exp_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    exp_html = resp.read().decode('utf-8', errors='ignore')

tabs = re.findall(r'<a[^>]*class=["\'][^"\']*nav-tab[^"\']*["\'][^>]*>(.*?)</a>', exp_html)
print("Elementor tabs:", tabs)

