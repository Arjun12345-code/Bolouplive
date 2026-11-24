with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'emerald' in line.lower():
        print(f"{i+1}: {line.strip()}")
