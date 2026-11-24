import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r = session.get('https://bolouplive.com/wp-admin/options.php')

# Search for cht_social_Link in r.text
idx = r.text.find('cht_social_Link')
if idx != -1:
    print(r.text[max(0, idx-100):idx+300])
else:
    print("cht_social_Link not found in options.php page")

