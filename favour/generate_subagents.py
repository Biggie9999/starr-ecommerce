import csv
import json

with open('edwards_distributors.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))
    
    batch = reader[20:70]
    
    subagents = []
    for r in batch:
        subagents.append({
            "TypeName": "research",
            "Role": "Lead Researcher",
            "Prompt": f'Search the web to find the name and direct email address of the CEO or President of the company \'{r["DistributorName"]}\' located in or near {r["City"]}. Their website is {r["Website"]}. Return ONLY a JSON object exactly like this: {{"CEO_Name": "John Doe", "CEO_Email": "johndoe@example.com"}}. If not found, use "". Do not explain your process.'
        })
        
    print(json.dumps(subagents, indent=2))
