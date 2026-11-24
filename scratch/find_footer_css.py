with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_footer = False
for i, line in enumerate(lines):
    if '.footer' in line:
        in_footer = True
    if in_footer:
        print(f"{i+1}: {line}", end='')
        if line.strip() == '}' and i > 50 and all(k not in lines[min(i+1, len(lines)-1)] for k in ['.footer', 'footer']):
            # check next few lines
            if not any('.footer' in l for l in lines[i+1:i+10]):
                break
