import csv
import json
import sys

def get_batch(start_row, batch_size):
    subagents = []
    with open('edwards_distributors.csv', 'r') as f:
        reader = csv.reader(f)
        for _ in range(start_row - 1):
            next(reader, None)
        
        for i in range(batch_size):
            row = next(reader, None)
            if not row:
                break
            
            company = row[1]
            city = row[4]
            state = row[6]
            website = row[12]
            
            prompt = f'Search the web to find the CEO name and direct email of \'{company}\' near {city}. Website: {website}. Return ONLY a JSON object: {{"CEO_Name": "", "CEO_Email": ""}}.'
            
            subagents.append({
                "TypeName": "research",
                "Role": f"CEO Research {start_row + i}",
                "Prompt": prompt,
                "Model": "flash"
            })
            
    print(json.dumps(subagents, indent=2))

if __name__ == "__main__":
    start = int(sys.argv[1])
    size = int(sys.argv[2])
    get_batch(start, size)
