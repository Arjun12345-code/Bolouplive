import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        d = json.loads(line)
        idx = d.get('step_index', 0)
        if 282 <= idx <= 320:
            if d.get('type') == 'PLANNER_RESPONSE':
                for tc in d.get('tool_calls', []):
                    args = tc.get('args', tc.get('Arguments', {}))
                    content = args.get('Content', args.get('CommandLine', ''))
                    print(f"Step {idx}: {tc.get('name') or tc.get('ToolName')}")
                    if 'requests' in content or 'save' in content or 'post' in content or 'update' in content:
                        print("Content:", content[:300])

