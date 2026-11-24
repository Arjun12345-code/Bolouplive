import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for save-button in all script tags
scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
for s in scripts:
    if 'save-button' in s:
        print("Script with save-button:")
        lines = s.splitlines()
        for idx, line in enumerate(lines):
            if 'save-button' in line:
                for j in range(max(0, idx-5), min(len(lines), idx+20)):
                    print(f"  {lines[j]}")

