import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    print("Status:", resp.status)
    for k, v in resp.headers.items():
        if any(h in k.lower() for h in ['x-litespeed', 'cache', 'cf-', 'age', 'expires']):
            print(f"{k}: {v}")

