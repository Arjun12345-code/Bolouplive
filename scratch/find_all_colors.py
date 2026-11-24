with open('c:/Users/asus/Desktop/WordPress/Bolouplive/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['19, 192, 145', '13, 148, 182', '13C091', '0D94B6', 'emerald', '00E5FF']):
        print(f'{i+1}: {l.strip()}')

