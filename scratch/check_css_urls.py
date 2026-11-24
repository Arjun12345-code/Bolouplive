import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

urls = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', css)
print("URLs in style.css:", urls)

