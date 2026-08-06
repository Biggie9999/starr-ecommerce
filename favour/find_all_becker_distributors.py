import urllib.request
import urllib.parse
import re
import json
import socket
import dns.resolver
import concurrent.futures

def search_ddg(query):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': query}).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        # Extract snippets and URLs
        results = []
        matches = re.findall(r'<a class="result__url" href="([^"]+)">\s*([^<]+)\s*</a>', html)
        for u, t in matches:
            results.append((u.strip(), t.strip()))
        return results
    except Exception as e:
        print(f"Error searching '{query}': {e}")
        return []

# Test query
res = search_ddg('"Becker pumps" distributor Texas')
print(f"Found {len(res)} results for test query.")
for u, t in res[:5]:
    print(t, u)
