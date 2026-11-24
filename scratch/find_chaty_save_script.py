import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check scripts for form submission
scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
for s in scripts:
    if 'save-button' in s or 'save_and_view' in s or 'options.php' in s:
        print("Found script matching save:")
        for line in s.splitlines():
            if any(k in line for k in ['save', 'submit', 'post', 'ajax', 'options']):
                print("  ", line.strip())

# Check all form tags and their exact attributes
forms = re.findall(r'<form([^>]+)>', html)
for f in forms:
    print("Form tag:", f)

