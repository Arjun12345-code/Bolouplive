import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<form[^>]*action=["\']options\.php["\'][^>]*>([\s\S]*?)</form>', html)
if m:
    form_html = m.group(0)
    # Find all buttons / submit inputs
    submits = re.findall(r'<(?:input|button)[^>]+type=["\']submit["\'][^>]*>', form_html)
    print("Submit elements:", submits)
    
    # Also find hidden inputs
    hidden = re.findall(r'<input[^>]+type=["\']hidden["\'][^>]*>', form_html)
    print("Hidden inputs count:", len(hidden))
    for h in hidden:
        print("  Hidden:", h)

