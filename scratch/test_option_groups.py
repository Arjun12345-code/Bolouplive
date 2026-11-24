import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Let's test different option_page values to see which one doesn't say "not in allowed options list"
test_pages = [
    'chaty-app', 'chaty', 'chaty_options', 'chaty_settings', 'chaty-settings',
    'chaty_widget', 'chaty-widget', 'cht_settings', 'cht_options', 'general'
]

for op in test_pages:
    r = session.post('https://bolouplive.com/wp-admin/options.php', data={'option_page': op, 'action': 'update'})
    is_not_allowed = 'not in the allowed options list' in r.text
    print(f"option_page '{op}': status {r.status_code}, not_allowed={is_not_allowed}")

