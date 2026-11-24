import requests
import re

session = requests.Session()
r = session.get('https://bolouplive.com/wp-content/plugins/chaty/admin/assets/js/app.js?ver=3.6.0')
print("app.js status:", r.status_code, "len:", len(r.text))

# Search for submit
for m in re.finditer(r'save-button|submit|cht-form', r.text):
    start = max(0, m.start() - 100)
    end = min(len(r.text), m.end() + 100)
    print("Match:", r.text[start:end])
    print("---")

