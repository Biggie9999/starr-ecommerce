import urllib.request
import urllib.parse
import re
import json

url = "https://www.anestiwata-corp.com/company/network/europe-africa"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=10)
    html = resp.read().decode('utf-8', errors='ignore')
    
    # Save Africa HTML section
    with open('/Users/alt/Desktop/starr/favour/anest_africa_page.html', 'w') as f:
        f.write(html)
    print("Fetched europe-africa page for Africa extraction.")
except Exception as e:
    print(f"Error fetching page: {e}")
