import urllib.request
import urllib.parse
import re
import json
import dns.resolver
import csv

# Crawl beckerpumps.com and becker-international.com locations
urls = [
    "https://www.beckerpumps.com/find-a-rep/",
    "https://www.beckerpumps.com/contact-us/",
    "https://www.becker-international.com/en/contact/worldwide/",
    "https://www.becker-international.com/en/contact/germany/",
    "https://www.becker-international.com/en/contact/usa/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

raw_content = []

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        raw_content.append({"url": u, "html": html})
        print(f"Successfully retrieved {u}")
    except Exception as e:
        print(f"Error retrieving {u}: {e}")

# Save raw HTML snippets for analysis
with open('/Users/alt/Desktop/starr/favour/becker_raw_site_scrape.json', 'w') as f:
    json.dump(raw_content, f, indent=2)

print("Saved raw scrape data to becker_raw_site_scrape.json")
