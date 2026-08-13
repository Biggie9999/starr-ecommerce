import json
import sys

batch_idx = int(sys.argv[1])
start = batch_idx * 50
end = start + 50

with open('batch_names.txt', 'r') as f:
    lines = [line.strip().split('|') for line in f.readlines()]

subagents = []
for i in range(start, min(end, len(lines))):
    name, city = lines[i]
    prompt = f'Search Google using the query: "{name}" "{city}" CEO email site:zoominfo.com. Read the Google search result snippets to find the CEO\'s name and email address. DO NOT click into ZoomInfo (it blocks bots). Return ONLY a JSON object: {{"CEO_Name": "", "CEO_Email": ""}}.'
    subagents.append({
        "TypeName": "research_subagent",
        "Role": f"Researcher {i}",
        "Prompt": prompt
    })

print(json.dumps(subagents))
