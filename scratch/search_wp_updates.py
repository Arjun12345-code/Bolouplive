import json

with open(r'C:\Users\asus\.gemini\antigravity\brain\b4654497-67d4-47ac-8248-d09b340acdc1\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if any(term in line for term in ['1743', '1719', 'custom_css', 'elementor_ajax']):
            d = json.loads(line)
            if d.get('type') == 'PLANNER_RESPONSE':
                for tc in d.get('tool_calls', []):
                    args = tc.get('args', tc.get('Arguments', {}))
                    print(f"Step {d.get('step_index')}: {tc.get('name') or tc.get('ToolName')}")
                    content = args.get('Content', args.get('CommandLine', ''))
                    if content:
                        print("Snippet:", content[:200])

