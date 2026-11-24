import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import json
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

# Open Elementor editor for 1743 to get editor nonce and environment
editor_url = 'https://bolouplive.com/wp-admin/post.php?post=1743&action=elementor'
with opener.open(urllib.request.Request(editor_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    editor_html = resp.read().decode('utf-8', errors='ignore')

print("Editor HTML length:", len(editor_html))

# Search for elementorCommon.ajax or ElementorConfig
common_nonce = re.search(r'"ajax":\{"url":".*?","nonce":"([^"]+)"\}', editor_html)
print("Common ajax nonce:", common_nonce.group(1) if common_nonce else "None")

config_nonce = re.search(r'"nonces":\{.*?"save":"([^"]+)".*?\}', editor_html)
print("Config save nonce:", config_nonce.group(1) if config_nonce else "None")

# Check if there are any nonces in ElementorConfig
cfg_match = re.search(r'var\s+ElementorConfig\s*=\s*(\{.*?\});', editor_html)
if cfg_match:
    try:
        cfg = json.loads(cfg_match.group(1))
        print("ElementorConfig nonces:", cfg.get('nonces'))
        print("ElementorConfig post_id:", cfg.get('document', {}).get('id'))
    except Exception as e:
        print("Config parse error:", e)

