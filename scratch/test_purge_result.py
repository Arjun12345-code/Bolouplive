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

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

purge_m = re.search(r'href=["\']([^"\']*LSCWP_CTRL=purge[^"\']*litespeed_type=purge_all["\'])', admin_html)
if purge_m:
    purge_url = purge_m.group(1)[:-1].replace('&#038;', '&')
    print("Purge URL:", purge_url)
    with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        print("Final URL:", resp.geturl())
        res_text = resp.read().decode('utf-8', errors='ignore')
        # Check for notices
        notices = re.findall(r'<div[^>]*class=["\'][^"\']*notice[^"\']*["\'][^>]*>(.*?)</div>', res_text, re.DOTALL)
        for n in notices:
            print("Notice:", re.sub(r'<[^>]+>', '', n).strip()[:100])

