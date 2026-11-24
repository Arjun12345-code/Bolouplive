with open('c:/Users/asus/Desktop/WordPress/Bolouplive/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.search(r'/\*.*?CTA Section.*?\*/(.*?)(?:/\*|$)', css, re.DOTALL | re.I)
if m:
    print(m.group(0)[:1500])

