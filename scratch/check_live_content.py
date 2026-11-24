import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Check keywords
checks = [
    'BoloUp Go',
    'About Agency',
    'boloupagency.com',
    'bd52e5xj',
    'Benefits',
    'BoloUp App',
    'boloup-host-role',
    'boloup-ecosystem',
    'BoloUp-Host-Registration-Guide',
    'Why Become a BoloUp App Host?',
    'How Can a BoloUp Host Earn?',
    'How to Register as a BoloUp App Host',
]

for c in checks:
    print(f"'{c}' in live site: {c in html}")

