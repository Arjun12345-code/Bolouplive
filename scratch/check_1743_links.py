import json

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/h1743_el_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

el_data = json.loads(data['_elementor_data'])
html = el_data[0]['elements'][0]['settings']['html']
print('Has blog in 1743 html:', 'blog' in html.lower())
print('Links in 1743 html:')
import re
for href in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html):
    print(href)

