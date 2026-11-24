import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

r = session.get('https://bolouplive.com/contact-us/')
for idx, line in enumerate(r.text.splitlines()):
    if '8212868780' in line:
        print(f"Line {idx+1}: {line[:200]}")

