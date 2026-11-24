import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/?t=1109', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Find elementor-location-footer
m = re.search(r'(.{0,300}class="[^"]*elementor-location-footer[^"]*".{0,300})', html)
if m:
    print(m.group(0))
