import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/', headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'})
with urllib.request.urlopen(req, context=ctx) as resp:
    print("Response headers:")
    for k, v in resp.headers.items():
        if 'litespeed' in k.lower() or 'cache' in k.lower():
            print(f"  {k}: {v}")
    html = resp.read().decode('utf-8', errors='ignore')
    print("boloup-brand.png in html:", 'boloup-brand.png' in html)
    print("boloup-go-brand.png in html:", 'boloup-go-brand.png' in html)

