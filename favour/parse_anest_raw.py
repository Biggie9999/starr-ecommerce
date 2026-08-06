import json
import re

with open('/Users/alt/Desktop/starr/favour/anest_iwata_raw.json', 'r') as f:
    data = json.load(f)

for item in data:
    url = item['url']
    html = item['html']
    print(f"=== URL: {url} (Length: {len(html)}) ===")
    
    # Extract emails
    emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html))
    print(f"Found {len(emails)} emails: {list(emails)[:15]}")
    
    # Extract text blocks with company names or addresses
    text_clean = re.sub(r'<[^>]+>', '\n', html)
    lines = [l.strip() for l in text_clean.split('\n') if l.strip()]
    
    # Print sample lines containing company keywords
    relevant = [l for l in lines if any(k in l.lower() for k in ['ltd', 'inc', 'gmbh', 'sarl', 'srl', 'corp', 'sl', 'distributor', 'company', 'address'])]
    print(f"Sample relevant lines ({len(relevant)}):")
    for r in relevant[:15]:
        print("  -", r)
