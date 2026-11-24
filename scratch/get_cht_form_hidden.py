import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

form_m = re.search(r'<form[^>]*id=["\']cht-form["\'][^>]*>([\s\S]*?)</form>', html)
if form_m:
    form_html = form_m.group(1)
    hidden = re.findall(r'<input[^>]+type=["\']hidden["\'][^>]*>', form_html)
    for h in hidden[:10]:
        print("Hidden in cht-form:", h)

