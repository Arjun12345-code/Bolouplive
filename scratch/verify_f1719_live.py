import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/?t=1110', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Check footer container classes in live site
m = re.search(r'data-elementor-id="1719"[^>]*>(.*?)<footer', html, re.DOTALL)
if m:
    print("Inside 1719 wrapper on live site:")
    print(m.group(0))
else:
    print("Could not find 1719 wrapper!")
