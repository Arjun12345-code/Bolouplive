import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<form[^>]*action=["\']options\.php["\'][^>]*>([\s\S]*?)</form>', html)
if m:
    form_html = m.group(0)
    print("Found options.php form, length:", len(form_html))
    
    # Extract all input fields
    inputs = re.findall(r'<input[^>]+name=["\']([^"\']+)["\'][^>]*>', form_html)
    print("Inputs count:", len(inputs))
    
    # Let's inspect the surrounding HTML of cht_social_Link
    idx = form_html.find('cht_social_Link')
    if idx != -1:
        print("Surrounding cht_social_Link:")
        print(form_html[max(0, idx-200):idx+400])
else:
    print("Form options.php not found")

