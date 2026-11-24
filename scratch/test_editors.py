import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

r_theme = session.get('https://bolouplive.com/wp-admin/theme-editor.php')
print("theme-editor status:", r_theme.status_code)
r_plugin = session.get('https://bolouplive.com/wp-admin/plugin-editor.php')
print("plugin-editor status:", r_plugin.status_code)

