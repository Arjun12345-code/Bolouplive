with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.footer[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
    print("---")
