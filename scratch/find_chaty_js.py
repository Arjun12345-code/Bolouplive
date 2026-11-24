import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
for s in scripts:
    if 'chaty' in s:
        print("Chaty script:", s)

