import urllib.request
import urllib.parse
import re
import json

urls = [
    "https://anestiwataamericas.com/find-a-distributor/",
    "https://www.anestiwata-corp.com/company/network/europe-africa"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

raw = []

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        raw.append({"url": u, "html": html})
        print(f"Retrieved {u} successfully.")
    except Exception as e:
        print(f"Error retrieving {u}: {e}")

with open('/Users/alt/Desktop/starr/favour/anest_iwata_raw.json', 'w') as f:
    json.dump(raw, f, indent=2)

print("Saved raw scrape to anest_iwata_raw.json")
