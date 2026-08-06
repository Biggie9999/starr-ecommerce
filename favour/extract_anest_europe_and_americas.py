import json
import re

with open('/Users/alt/Desktop/starr/favour/anest_iwata_raw.json', 'r') as f:
    data = json.load(f)

for item in data:
    if "europe-africa" in item['url']:
        html = item['html']
        print("=== EUROPE NETWORK ENTITIES ===")
        # Extract h3/h4 headings and paragraph contents
        blocks = re.findall(r'<(?:h2|h3|h4)[^>]*>(.*?)</(?:h2|h3|h4)>\s*<p[^>]*>(.*?)</p>', html, re.DOTALL)
        for heading, body in blocks:
            clean_heading = re.sub(r'<[^>]+>', '', heading).strip()
            clean_body = re.sub(r'<[^>]+>', ' ', body).strip()
            clean_body = re.sub(r'\s+', ' ', clean_body)
            # Skip Africa entities as requested
            if any(af in clean_heading.lower() or af in clean_body.lower() for af in ['africa', 'south africa', 'egypt', 'morocco', 'tunisia', 'algeria']):
                print(f"SKIPPING AFRICA: {clean_heading}")
                continue
            print(f"COMPANY: {clean_heading}")
            print(f"DETAILS: {clean_body}")
            print("-" * 50)
