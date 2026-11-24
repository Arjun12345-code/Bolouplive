import json

with open('scratch/p648_el_data.json', 'r', encoding='utf-8') as f:
    meta = json.load(f)
    el_data = json.loads(meta['_elementor_data'])
    html_widget_content = el_data[0]['elements'][0]['settings']['html']
    print("p648 HTML widget length:", len(html_widget_content))
    print("Start of HTML widget:")
    print(html_widget_content[:500])
    print("End of HTML widget:")
    print(html_widget_content[-500:])

