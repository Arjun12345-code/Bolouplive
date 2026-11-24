with open('c:/Users/asus/Desktop/WordPress/Bolouplive/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<stop[^>]+>', text)
print('Count of stop elements:', len(matches))
for m in set(matches):
    print(m)

