import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        d = json.loads(line)
        idx = d.get('step_index', 0)
        if 320 <= idx <= 500:
            if d.get('type') == 'PLANNER_RESPONSE':
                for tc in d.get('tool_calls', []):
                    args = tc.get('args', tc.get('Arguments', {}))
                    content = args.get('Content', args.get('CommandLine', ''))
                    if 'requests' in content or 'POST' in content or 'elementor' in content or 'save' in content:
                        print(f"Step {idx}: {content[:150]}")

