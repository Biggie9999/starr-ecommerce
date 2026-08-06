import urllib.request
import urllib.parse
import re
import json
import dns.resolver
import time

queries = [
    '"Anest Iwata" distributor "Inc"',
    '"Anest Iwata" distributor "LLC"',
    '"Anest Iwata" distributor "GmbH"',
    '"Anest Iwata" distributor "Ltd"',
    '"Anest Iwata" authorized distributor USA',
    '"Anest Iwata" authorized distributor UK',
    '"Anest Iwata" authorized distributor Germany',
    '"Anest Iwata" authorized distributor France',
    '"Anest Iwata" authorized distributor Spain OR Italy',
    '"Anest Iwata" line card distributor'
]

known = set()
bad_keywords = ['amazon', 'ebay', 'wikipedia', 'linkedin', 'facebook', 'youtube', 'twitter', 'instagram', 'yelp', 'yellowpages', 'thomasnet', 'directindustry', 'anestiwataamericas.com', 'anestiwata-corp.com', 'anest-iwata.de', 'anest-iwata.fr', 'anest-iwata.it', 'anest-iwata.es', 'anest-iwata.co.uk']

def search_ddg(q):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': q}).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=8)
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a class="result__url" href="([^"]+)">\s*([^<]+)\s*</a>', html)
        return [(u.strip(), t.strip()) for u, t in matches]
    except Exception:
        return []

discovered = {}
print("Executing deep search for Anest Iwata distributors...")

for q in queries:
    res = search_ddg(q)
    for u, t in res:
        m = re.search(r'https?://(?:www\.)?([^/]+)', u)
        if m:
            dom = m.group(1).lower()
            if not any(bk in dom for bk in bad_keywords):
                clean_t = re.sub(r'<[^>]+>', '', t)
                clean_t = re.sub(r'\s+', ' ', clean_t).strip()
                if dom not in discovered:
                    discovered[dom] = clean_t
    time.sleep(0.5)

print(f"Discovered {len(discovered)} Anest Iwata candidate distributor domains.")

with open('/Users/alt/Desktop/starr/favour/anest_iwata_candidates.json', 'w') as f:
    json.dump(discovered, f, indent=2)

print("Saved to anest_iwata_candidates.json")
