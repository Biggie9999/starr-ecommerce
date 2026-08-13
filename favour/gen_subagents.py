import json
import sys

def generate_subagents(start_idx, batch_size):
    import csv
    with open("edwards_distributors.csv", "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        batch = reader[start_idx : start_idx + batch_size]

    subagents = []
    for item in batch:
        prompt = f'Search Google using the query: "{item["DistributorName"]}" "{item["City"]}" CEO email site:zoominfo.com. Read the Google search result snippets to find the CEO\'s name and email address. DO NOT click into ZoomInfo (it blocks bots). Return ONLY a JSON object: {{"CEO_Name": "", "CEO_Email": ""}}.'
        subagents.append({
            "TypeName": "research",
            "Role": "Search for CEO",
            "Prompt": prompt
        })

    with open("subagents.json", "w") as f:
        json.dump(subagents, f)

if __name__ == "__main__":
    generate_subagents(int(sys.argv[1]), int(sys.argv[2]))
