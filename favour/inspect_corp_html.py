import json
import re

with open('/Users/alt/Desktop/starr/favour/anest_iwata_raw.json', 'r') as f:
    data = json.load(f)

for item in data:
    if "europe-africa" in item['url']:
        html = item['html']
        # Find all text sections with addresses/companies
        snippets = re.findall(r'ANEST IWATA[^\n<]+', html)
        for s in set(snippets):
            print(s.strip())
