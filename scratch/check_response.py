import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 1640 <= i <= 1700:
            d = json.loads(line)
            if d.get('type') == 'PLANNER_RESPONSE':
                content = d.get('content', '')
                if content:
                    print(f"=== Line {i} ===")
                    print(content[:500])

