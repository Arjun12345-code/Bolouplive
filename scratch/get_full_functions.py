import requests
import re
import html

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r = session.get('https://bolouplive.com/wp-admin/theme-editor.php?file=functions.php')
m = re.search(r'<textarea[^>]+id="newcontent"[^>]*>([\s\S]*?)</textarea>', r.text)
raw_content = html.unescape(m.group(1))

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/original_functions.php', 'w', encoding='utf-8') as f:
    f.write(raw_content)

print("Saved original_functions.php, length:", len(raw_content))
print("File content:\n", raw_content)

