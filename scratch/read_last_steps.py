import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\763f91fd-b7b2-4f2c-8b26-e0bb738e71a7\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines) - 15, len(lines)):
    try:
        data = json.loads(lines[i])
        print(f"Step {data.get('step_index')}: {data.get('source')} | {data.get('type')}")
        if data.get('source') == 'USER_EXPLICIT':
            print("USER:", data.get('content'))
        elif data.get('thinking'):
            print("THINKING:", data.get('thinking')[:300])
    except Exception as e:
        print("Error:", e)

