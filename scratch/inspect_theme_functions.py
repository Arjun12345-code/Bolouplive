import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r = session.get('https://bolouplive.com/wp-admin/theme-editor.php?file=functions.php')
print("theme-editor functions.php status:", r.status_code)

# Check textarea content
m = re.search(r'<textarea[^>]+id="newcontent"[^>]*>([\s\S]*?)</textarea>', r.text)
if m:
    content = m.group(1)
    print("functions.php content length:", len(content))
    print("Head:\n", content[:300])
    print("Tail:\n", content[-300:])
    
    # Check nonce for updating
    nonce_m = re.search(r'id="_wpnonce"\s+name="_wpnonce"\s+value="([^"]+)"', r.text)
    print("Nonce:", nonce_m.group(1) if nonce_m else "None")

