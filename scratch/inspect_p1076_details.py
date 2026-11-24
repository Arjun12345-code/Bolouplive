import json
import re

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/p1076.json', 'r', encoding='utf-8') as f:
    p = json.load(f)

print("Title:", p.get('title'))
raw = p.get('content', {}).get('raw', '')
el_data = p.get('meta', {}).get('_elementor_data', '')

print("\n--- Check raw content ---")
for line in raw.splitlines():
    if '821' in line:
        print("Raw:", line.strip())

print("\n--- Check _elementor_data ---")
if el_data:
    el_obj = json.loads(el_data)
    el_str = json.dumps(el_obj, indent=2)
    for line in el_str.splitlines():
        if '821' in line:
            print("Elementor:", line.strip())

