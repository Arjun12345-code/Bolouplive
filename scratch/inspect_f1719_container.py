import json

with open('scratch/f1719_el_data.json', 'r', encoding='utf-8') as f:
    meta = json.load(f)
    el_data = json.loads(meta['_elementor_data'])
    print("f1719 root container settings:")
    print(json.dumps(el_data[0].get('settings', {}), indent=2))
    print("f1719 root container keys:")
    print(el_data[0].keys())
