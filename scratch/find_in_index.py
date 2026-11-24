with open('c:/Users/asus/Desktop/WordPress/Bolouplive/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,30}(?:emerald|teal|19, 192|13, 148).{0,30}', text, re.I)
for m in matches:
    print('Match in index.html:', m.strip())

