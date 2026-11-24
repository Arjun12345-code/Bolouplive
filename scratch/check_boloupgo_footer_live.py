import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://boloupgo.live/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("=== CHECK boloupgo.live ===")
footer_m = re.search(r'(<footer[\s\S]*?</footer>)', html)
if footer_m:
    print("Footer found on boloupgo.live!")
    f_block = footer_m.group(1)
    # Check parent container classes
    idx = html.find(f_block[:40])
    print("Preceding 200 chars before footer:")
    print(html[max(0, idx-200):idx])
else:
    print("Footer NOT found on boloupgo.live!")

