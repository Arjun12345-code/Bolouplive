import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/chaty_widget.html', 'r', encoding='utf-8') as f:
    html = f.read()

for channel in ['Telegram', 'Whatsapp', 'Link']:
    matches = re.findall(rf'name=["\']cht_social_{channel}\[([^\]]+)\]["\']\s+value=["\']([^"\']*)["\']', html)
    print(f"=== Channel {channel} ===")
    for k, v in matches:
        print(f"  {k} = {v}")

