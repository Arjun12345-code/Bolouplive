import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        idx = d.get('step_index', 0)
        if idx in [2463, 2467]:
            print(f"=== STEP {idx} ===")
            for tc in d.get('tool_calls', []):
                args = tc.get('args', tc.get('Arguments', {}))
                print(args.get('Content', ''))

