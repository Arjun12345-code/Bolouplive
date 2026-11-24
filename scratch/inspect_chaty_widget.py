import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

widget_url = 'https://bolouplive.com/wp-admin/admin.php?page=chaty-app&widget=0'
with opener.open(urllib.request.Request(widget_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    w_html = resp.read().decode('utf-8', errors='ignore')

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'w', encoding='utf-8') as f:
    f.write(w_html)

print("Saved chaty_widget.html, len:", len(w_html))

# Search for forms and inputs
forms = re.findall(r'<form[^>]*action=["\']([^"\']*)["\'][^>]*>', w_html)
print("Forms in chaty widget page:", forms)

# Search for the phone number 628212868780 in chaty_widget.html
matches = [m for m in re.finditer(r'.{0,50}(?:628212868780|08212868780|8212868780).{0,50}', w_html)]
print("Found matches in chaty widget page:")
for m in matches:
    print("  ", m.group(0))

