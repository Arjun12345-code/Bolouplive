import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/?t=1109', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Search for 'blog' case-insensitive
matches = re.findall(r'(.{0,50}blog.{0,50})', html, re.I)
print("Matches for 'blog' on live site:")
for m in matches:
    print("-", m.strip())
