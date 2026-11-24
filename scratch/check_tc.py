import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i in [1598, 1600, 1630, 1636]:
            d = json.loads(line)
            print(f"=== Line {i} ===")
            for tc in d.get('tool_calls', []):
                print(tc.get('name'), json.dumps(tc.get('args', tc.get('Arguments', {})))[:300])

