import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def check_site(url, name):
    print(f"\n==========================================")
    print(f"VERIFYING {name} ({url})")
    print(f"==========================================")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    # 1. Title & Meta Desc
    title_m = re.search(r'<title>(.*?)</title>', html)
    print("Title:", title_m.group(1) if title_m else "None")
    desc_m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html)
    print("Meta Desc:", desc_m.group(1) if desc_m else "None")
    
    # 2. Header
    header_m = re.search(r'(<header[\s\S]*?</header>)', html)
    if header_m:
        h = header_m.group(1)
        print("\n--- Header ---")
        links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', h)
        for href, text in links:
            print(f"  Nav: {text.strip()} -> {href}")
        img_m = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', h)
        print("  Logo img:", img_m)
    
    # 3. Footer
    footer_m = re.search(r'(<footer[\s\S]*?</footer>)', html)
    if footer_m:
        f = footer_m.group(1)
        print("\n--- Footer ---")
        cols = re.findall(r'<h3>(.*?)</h3>', f)
        print("  Columns:", cols)
        f_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', f)
        for href, text in f_links:
            print(f"  Footer link: {text.strip()} -> {href}")
        f_img = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', f)
        print("  Footer logo img:", f_img)
        print("  Has 'Join with Agency ID 2527626' in footer:", '2527626' in f)
    
    # 4. Check Key Brief Sections (Hero, Table, Benefits, Steps, FAQs, CTA)
    print("\n--- Content Checks ---")
    print("  'Start Your Live Journey' in HTML:", 'Start Your Live Journey' in html)
    print("  'What Does It Mean to Be a BoloUp Go Host?' in HTML:", 'What Does It Mean to Be a BoloUp Go Host?' in html)
    print("  'How the BoloUp Go Host Experience Compares' in HTML:", 'How the BoloUp Go Host Experience Compares' in html)
    print("  'Why Become a BoloUp Go Host?' in HTML:", 'Why Become a BoloUp Go Host?' in html)
    print("  'How to Register as a BoloUp Go Host' in HTML:", 'How to Register as a BoloUp Go Host' in html)
    print("  'Frequently Asked Questions' in HTML:", 'Frequently Asked Questions' in html)
    print("  'Ready to Become a BoloUp Go Host?' in HTML:", 'Ready to Become a BoloUp Go Host?' in html)
    print("  'boloup.onelink.me/PDV4/bd52e5xj' count in HTML:", html.count('boloup.onelink.me/PDV4/bd52e5xj'))
    print("  'share.bololinks.com/home/scode/47282' count in HTML:", html.count('share.bololinks.com/home/scode/47282'))

check_site('https://boloupgo.live/', 'boloupgo.live')
check_site('https://bolouplive.com/', 'bolouplive.com')

