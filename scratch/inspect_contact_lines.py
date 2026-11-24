import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

r = session.get('https://bolouplive.com/contact-us/')
lines = r.text.splitlines()

for i in range(max(0, 315), min(len(lines), 355)):
    print(f"{i+1}: {lines[i]}")

