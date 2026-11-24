import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

# Check if debug.log is accessible
for path in ['/wp-content/debug.log', '/debug.log']:
    r = session.get('https://bolouplive.com' + path)
    print(f"Path {path}: status {r.status_code}, len: {len(r.text)}")
    if r.status_code == 200 and len(r.text) > 0:
        print("Tail of debug.log:")
        print(r.text[-1000:])

