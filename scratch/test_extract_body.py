import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract from <body ...> to </body>
m = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.I)
if m:
    body_inner = m.group(1).strip()
    print("Found <body> inner! Length:", len(body_inner))
    print("Start:", body_inner[:300])
    print("End:", body_inner[-300:])
else:
    print("No body tag found!")

