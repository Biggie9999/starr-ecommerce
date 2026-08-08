import urllib.request
import urllib.parse
import re
import json

urls = [
    "https://hoyermotors.com/",
    "https://hoyermotors.com/contact/",
    "https://hoyermotors.com/about/hoyer-offices/",
    "https://hoyermotors.com/partners/",
    "https://hoyermotors.com/distributors/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

scraped = []

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        scraped.append({"url": u, "html": html})
        print(f"Retrieved {u} successfully.")
    except Exception as e:
        print(f"Error retrieving {u}: {e}")

with open('/Users/alt/Desktop/starr/favour/hoyer_raw.json', 'w') as f:
    json.dump(scraped, f, indent=2)

print("Saved raw Hoyer Motors scrape to hoyer_raw.json")
