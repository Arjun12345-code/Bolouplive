import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Let's test posting different values for cht_social_Link[channel_type]
for val in ['test', 'whatsapp', 'Whatsapp', 'WhatsApp']:
    r = session.post('https://bolouplive.com/wp-admin/options.php', data={'cht_social_Link[channel_type]': val})
    print(f"Value '{val}': status {r.status_code}")

