import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

r = session.get('https://bolouplive.com/contact-us/')
print("821 in contact-us:", '8212868780' in r.text)
print("823 in contact-us:", '82371383705' in r.text)

