import requests
import json

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
r_login = session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})
print("Login status:", r_login.status_code)

cookies_list = []
for c in session.cookies:
    cookie_dict = {
        'name': c.name,
        'value': c.value,
        'domain': c.domain or 'bolouplive.com',
        'path': c.path or '/',
        'httpOnly': False,
        'secure': True,
        'sameSite': 'Lax'
    }
    cookies_list.append(cookie_dict)
    print("Cookie:", c.name)

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/wp_cookies.json', 'w') as f:
    json.dump(cookies_list, f, indent=2)

print("Saved wp_cookies.json with", len(cookies_list), "cookies")

