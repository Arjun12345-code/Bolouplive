import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://boloupgo.live/', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("boloupgo.live status:", resp.status)
        # Check header nav links
        header_m = re.search(r'<nav[^>]*class=["\']nav-menu["\'][^>]*>([\s\S]*?)</nav>', html)
        if header_m:
            links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', header_m.group(1))
            print("boloupgo.live nav links:", links)
        # Check footer
        footer_m = re.search(r'<footer[\s\S]*?</footer>', html)
        if footer_m:
            f_html = footer_m.group(0)
            print("boloupgo.live footer length:", len(f_html))
            print("boloupgo.live has 'Blog':", 'blog' in f_html.lower())
            # Find footer columns
            cols = re.findall(r'<h3>(.*?)</h3>', f_html)
            print("boloupgo.live footer column headers:", cols)
except Exception as e:
    print("Error:", e)

