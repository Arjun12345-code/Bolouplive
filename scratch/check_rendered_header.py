import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Find elementor-location-header or <header
m = re.search(r'(<header.*?</header>)', html, re.DOTALL)
if m:
    print("Found header tag:")
    print(m.group(1)[:1000])
else:
    print("No header tag found, searching for boloup-header-logo:")
    m2 = re.search(r'(.{0,200}boloup-header-logo.{0,200})', html, re.DOTALL)
    if m2:
        print("Around logo:")
        print(m2.group(1))

# Check elementor data post ids in HTML
post_ids = re.findall(r'data-elementor-id=["\'](\d+)["\']', html)
print("Elementor post IDs on page:", post_ids)

