import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Let's test a simple GET or POST to options.php or test what is in 503 response
r = session.post('https://bolouplive.com/wp-admin/options.php', data={'test': '1'})
print("Status:", r.status_code)
print("Text snippet:", r.text[:500])

