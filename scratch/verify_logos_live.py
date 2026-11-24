import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("=== VERIFY LIVE HTML ON bolouplive.com ===")

# Check header logo
header_m = re.search(r'(<header[\s\S]*?</header>)', html)
if header_m:
    header_block = header_m.group(1)
    brand_logo_m = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', header_block)
    print("Header images found:", brand_logo_m)
else:
    print("Header not matched with regex, searching header area...")

# Check footer logo
footer_m = re.search(r'(<footer[\s\S]*?</footer>)', html)
if footer_m:
    footer_block = footer_m.group(1)
    footer_img_m = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', footer_block)
    print("Footer images found:", footer_img_m)
else:
    print("Footer not matched with regex")

print("boloup-brand.png count in entire page:", html.count('boloup-brand.png'))
print("boloup-go-brand.png count in entire page:", html.count('boloup-go-brand.png'))

# Check footer columns
print("Footer columns check:")
for col_title in ['Navigation', 'Host Program', 'BoloUp App']:
    print(f"- '{col_title}' present:", col_title in html)

# Check blog in navbar
print("'blog' in header check:", 'blog' in (header_block.lower() if header_m else ''))

