import requests
import re

session = requests.Session()
r = session.get('https://bolouplive.com/wp-content/plugins/chaty/admin/assets/js/cht-scripts.min.js?ver=3.6.0')
print("cht-scripts.min.js len:", len(r.text))

# Search for submit or options.php or ajax
for m in re.finditer(r'options\.php|save_button|cht-form|admin-ajax\.php', r.text):
    start = max(0, m.start() - 100)
    end = min(len(r.text), m.end() + 100)
    print("Match in cht-scripts:", r.text[start:end])

