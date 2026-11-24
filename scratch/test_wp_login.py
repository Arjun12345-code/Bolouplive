import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Check live homepage first
req = urllib.request.Request('https://bolouplive.com', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with opener.open(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Live site homepage fetched, len={len(html)}")
        # Check title
        m = re.search(r'<title>(.*?)</title>', html, re.I)
        if m:
            print(f"Current live Title: {m.group(1)}")
        # Check if Elementor
        print(f"Elementor in HTML: {'elementor' in html}")
except Exception as e:
    print(f"Error fetching live site: {e}")

# Try login
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
login_req = urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = opener.open(login_req)
    print("Login response url:", resp.geturl())
    # Check if cookies set
    cookies = [c.name for c in cj]
    print("Cookies set:", cookies)
    is_logged_in = any('wordpress_logged_in' in c for c in cookies)
    print("Logged in successfully:", is_logged_in)
except Exception as e:
    print(f"Login error: {e}")

