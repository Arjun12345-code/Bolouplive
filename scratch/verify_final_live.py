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
header_m = re.search(r'<nav[^>]*class=["\']nav-menu["\'][^>]*>([\s\S]*?)</nav>', html)
if header_m:
    links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', header_m.group(1))
    print("Header nav links:")
    for href, text in links:
        print(f"  {text} -> {href}")

footer_m = re.search(r'<footer[\s\S]*?</footer>', html)
if footer_m:
    f_html = footer_m.group(0)
    print("Footer has Blog:", '/blog' in f_html)
    print("Footer columns count:", len(re.findall(r'<h3>', f_html)))
    print("Footer brand logo:", re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', f_html))

