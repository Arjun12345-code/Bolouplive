import json

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/p1076.json', 'r', encoding='utf-8') as f:
    p = json.load(f)

print("Raw content:")
print(p.get('content', {}).get('raw', ''))

