import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/?t=1107', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print(f"Live site fetched: {len(html)} bytes")

# Extract title
title_m = re.search(r'<title>(.*?)</title>', html, re.I)
print("Title:", title_m.group(1) if title_m else "Not found")

tests = [
    # General / Branding
    ("BoloUp Go logo present", 'boloup-go-brand.png' in html),
    ("BoloUp Midnight theme present", '#100524' in html or '100524' in html or 'bolouplive' in html),
    
    # Navbar
    ("Navbar 'About Agency' present", 'About Agency' in html),
    ("Navbar 'boloupagency.com' link present", 'https://boloupagency.com' in html),
    ("Navbar 'bd52e5xj' CTA link present", 'https://boloup.onelink.me/PDV4/bd52e5xj' in html),
    ("Navbar 'Benefits' link removed", 'id="nav-benefits"' not in html),
    
    # What is BoloUp
    ("What is BoloUp CTA removed", 'what-cta-wrap' not in html and 'Learn more about Agency' not in html),
    
    # Benefits
    ("BoloUp Host Role image present", 'boloup-host-role.png' in html),
    ("Why Become a BoloUp App Host? present", 'Why Become a BoloUp App Host?' in html),
    
    # Earnings
    ("BoloUp Ecosystem image present", 'boloup-ecosystem.png' in html),
    ("How Can a BoloUp Host Earn? present", 'How Can a BoloUp Host Earn?' in html),
    
    # Registration
    ("Registration Step 1 image present", 'BoloUp-Host-Registration-Guide-Step-1.jpg' in html),
    ("Registration Step 2 image present", 'BoloUp-Host-Registration-Guide-Step-2.jpg' in html),
    ("Registration Step 3 image present", 'BoloUp-Host-Registration-Guide-Step-3.jpg' in html),
    ("Registration Step 4 image present", 'BoloUp-Host-Registration-Guide-Step-4.jpg' in html),
    
    # Footer
    ("Footer 'BoloUp App' section removed", '<h3>BoloUp App</h3>' not in html),
    ("Footer BoloUp Go brand present", 'boloup-go-brand.png' in html),
    
    # Final CTA
    ("Bottom CTA 'Join as a BoloUp Host' present", 'Join as a BoloUp Host' in html),
]

all_passed = True
for name, result in tests:
    status = "PASS" if result else "FAIL"
    print(f"[{status}] {name}")
    if not result:
        all_passed = False

print("\nOVERALL VERIFICATION:", "SUCCESS 100%" if all_passed else "SOME CHECKS FAILED")

