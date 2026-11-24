import re

images = set()
for fname in ['header.html', 'footer.html', 'index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        for src in re.findall(r'src=["\']([^"\']+)["\']', content):
            images.add(src)

print("Images referenced in local files:")
for img in sorted(images):
    print("-", img)

