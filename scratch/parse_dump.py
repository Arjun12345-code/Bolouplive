import json

for name in ['p648', 'h1743', 'f1719']:
    with open(f'scratch/{name}_el_data.json', 'r', encoding='utf-8') as f:
        meta = json.load(f)
        el_data = json.loads(meta['_elementor_data'])
        print(f"=== {name} ===")
        print("Root elements:", len(el_data))
        print("Root element keys:", el_data[0].keys())
        # Inspect inner elements
        inner = el_data[0].get('elements', [])
        print("Inner elements count:", len(inner))
        for item in inner:
            print("  Widget:", item.get('widgetType'), "id:", item.get('id'), "settings keys:", item.get('settings', {}).keys())

with open('scratch/k7_meta.json', 'r', encoding='utf-8') as f:
    k7_meta = json.load(f)
    settings = k7_meta.get('_elementor_page_settings', {})
    print("=== Kit 7 ===")
    print("Page settings keys:", list(settings.keys()))
    print("custom_css length:", len(settings.get('custom_css', '')))

