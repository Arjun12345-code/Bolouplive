import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i in [1598, 1600, 1630, 1636]:
            d = json.loads(line)
            print(f"=== Line {i} {d.get('type')} ===")
            content = str(d.get('content', ''))[:400]
            print(content)
            calls = d.get('tool_calls', [])
            if calls:
                print('Calls:', [(c.get('ToolName') or c.get('name'), str(c.get('Arguments'))[:100]) for c in calls])

