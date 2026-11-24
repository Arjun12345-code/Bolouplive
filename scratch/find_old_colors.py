with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
old_colors = [
    '#0d94b6', '#13c091', '#0b7a95', '#0a637a', '#065064',
    '#072828', '#061d1d', '#13C091', '#0D94B6', 'teal', 'emerald'
]

found = {}
for c in old_colors:
    matches = re.findall(rf'.{{0,40}}{re.escape(c)}.{{0,40}}', text, re.I)
    if matches:
        found[c] = matches

print("Old color matches found in style.css:")
for c, m in found.items():
    print(f"=== {c} ({len(m)} occurrences) ===")
    for item in m[:3]:
        print("  ", item.strip())
