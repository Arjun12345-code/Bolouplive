import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for path in ['/blog/', '/blog']:
    try:
        req = urllib.request.Request('https://boloupgo.live' + path, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as resp:
            print(f"boloupgo.live{path} status:", resp.status)
    except Exception as e:
        print(f"boloupgo.live{path} error:", e)

