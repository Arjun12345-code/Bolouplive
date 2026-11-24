import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Check whatsapp accounts
r = session.get('https://bolouplive.com/wp-admin/edit.php?post_type=whatsapp-accounts')
print("whatsapp-accounts status:", r.status_code)
# Search for 821 or phone numbers
matches = re.findall(r'.{0,40}(?:8212868780|0821|82371383705).{0,40}', r.text)
print("Matches in whatsapp-accounts:", matches)

# Check floating widget
r_fw = session.get('https://bolouplive.com/wp-admin/admin.php?page=nta_whatsapp_floating_widget')
print("nta_whatsapp_floating_widget status:", r_fw.status_code)
matches_fw = re.findall(r'.{0,40}(?:8212868780|0821|82371383705).{0,40}', r_fw.text)
print("Matches in nta_whatsapp_floating_widget:", matches_fw)

