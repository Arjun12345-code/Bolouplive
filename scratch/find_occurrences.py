import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

r = session.get('https://bolouplive.com/contact-us/')

print("Occurrences of 821:")
for m in re.finditer(r'.{0,40}8212868780.{0,40}', r.text):
    print("  821:", m.group(0))

print("\nOccurrences of 823:")
for m in re.finditer(r'.{0,40}82371383705.{0,40}', r.text):
    print("  823:", m.group(0))

