with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line.lower() for k in ['elementor-1743', 'elementor-1719', 'e-con-boxed', 'location-header', 'location-footer']):
        print(f"{i+1}: {line}", end='')
        for j in range(i+1, min(i+15, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
        print("---")
