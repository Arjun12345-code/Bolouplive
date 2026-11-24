import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 1150 <= i <= 1350:
            d = json.loads(line)
            if d.get('type') == 'PLANNER_RESPONSE':
                for tc in d.get('tool_calls', []):
                    name = tc.get('name') or tc.get('ToolName')
                    args = tc.get('args', tc.get('Arguments', {}))
                    cmd = args.get('CommandLine', '')
                    path = args.get('Path', '')
                    if cmd or path:
                        print(f"Step {d.get('step_index')}: {name} - {cmd[:150]} {path[:100]}")

