import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\763f91fd-b7b2-4f2c-8b26-e0bb738e71a7\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    data = json.loads(line)
    idx = data.get('step_index')
    if 345 <= idx <= 360:
        print(f"=== Step {idx}: {data.get('source')} | {data.get('type')} ===")
        if data.get('source') == 'USER_EXPLICIT':
            print("USER:", data.get('content'))
        if data.get('tool_calls'):
            for tc in data.get('tool_calls'):
                print("TOOL:", tc.get('name'), tc.get('args'))
        if data.get('thinking'):
            print("THINKING:", data.get('thinking')[:500])

