import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def check_images(url):
    print(f"\nChecking images on {url}:")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    imgs = set(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html))
    for src in sorted(imgs):
        try:
            ireq = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(ireq, context=ctx) as iresp:
                print(f"  [{iresp.status}] {src}")
        except Exception as e:
            print(f"  [ERROR] {src}: {e}")

check_images('https://boloupgo.live/')
check_images('https://bolouplive.com/')

