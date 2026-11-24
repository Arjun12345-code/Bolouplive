import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for ajax actions
matches = re.findall(r'action\s*:\s*["\']([^"\']+)["\']', html)
print("Ajax actions found in chaty page:", set(matches))

