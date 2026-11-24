import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/?t=1108', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Search for footer and its parents
m = re.search(r'(.{0,500}<footer.*?</footer>.{0,300})', html, re.DOTALL)
if m:
    print("Around footer:")
    print(m.group(1)[:1000])

# Also check elementor post 1719 wrapper
m2 = re.search(r'data-elementor-id="1719"[^>]*>(.*?)</footer>', html, re.DOTALL)
if m2:
    print("\nInside 1719:")
    print(m2.group(0)[:600])
