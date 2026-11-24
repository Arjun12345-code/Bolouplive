import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i in [1272, 1333, 1630]:
            d = json.loads(line)
            print(f"=== Line {i} ===")
            for tc in d.get('tool_calls', []):
                args = tc.get('args', tc.get('Arguments', {}))
                print(args.get('Content', ''))

