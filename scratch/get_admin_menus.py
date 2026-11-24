import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r = session.get('https://bolouplive.com/wp-admin/')

# Find all admin menu links
links = re.findall(r'<a[^>]+href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r.text)
print("Admin menu links:")
for href, text in links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    if clean_text and any(k in href for k in ['php', 'page=']):
        print(f"  {clean_text} -> {href}")

