import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"', html)
print('Sections in Bolouplive/index.html:', sections)

# check last section before footer
last_section = re.findall(r'<section[^>]*class="([^"]+)"[^>]*id="([^"]+)"', html)
print('Last section details:', last_section[-1] if last_section else None)

