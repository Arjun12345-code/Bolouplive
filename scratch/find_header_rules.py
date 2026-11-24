with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.header' in line or 'header.' in line:
        for j in range(max(0, i-2), min(i+25, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
        print("===")
        break
