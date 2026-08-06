import urllib.request
import urllib.parse
import re
import dns.resolver
import json
import csv
import time

# Queries specifically aimed at finding independent distributors, repair centers, and sales agents for Becker Pumps
queries = [
    '"Becker vacuum" distributor Texas',
    '"Becker vacuum" distributor California',
    '"Becker vacuum" distributor Illinois',
    '"Becker vacuum" distributor Ohio',
    '"Becker vacuum" distributor Pennsylvania',
    '"Becker vacuum" distributor Florida',
    '"Becker vacuum" distributor North Carolina',
    '"Becker vacuum" distributor Georgia',
    '"Becker vacuum" distributor Michigan',
    '"Becker vacuum" distributor Washington',
    '"Becker vacuum" distributor Wisconsin',
    '"Becker vacuum" distributor Minnesota',
    '"Becker vacuum" distributor Missouri',
    '"Becker vacuum" distributor Indiana',
    '"Becker vacuum" distributor Colorado',
    '"Becker vacuum" distributor Massachusetts',
    '"Becker vacuum" distributor New Jersey',
    '"Becker vacuum" distributor Ontario',
    '"Becker vacuum" distributor Quebec',
    '"Becker vacuum" distributor UK',
    '"Becker vacuum" distributor Germany',
    '"Becker vacuum" distributor Australia',
    '"Becker vacuum pump" sales and service'
]

# Load Busch domains to strictly exclude
busch_domains = set()
try:
    with open("/Users/alt/Desktop/starr/favour/buschvacuum_dealers.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = row.get("Domain", "").strip().lower()
            if d: busch_domains.add(d)
            c = row.get("Company", "").strip().lower()
            if c: busch_domains.add(c)
except Exception as e:
    print(f"Error loading Busch domains: {e}")

bad_keywords = [
    'beckerpumps', 'becker-international', 'duckduckgo', 'google', 'amazon', 'ebay',
    'wikipedia', 'linkedin', 'facebook', 'youtube', 'twitter', 'instagram', 'yelp',
    'yellowpages', 'mapquest', 'chamberofcommerce', 'scribd', 'dnb', 'bloomberg',
    'zoominfo', 'glassdoor', 'indeed', 'zippia', 'thomasnet', 'directindustry', 'radwell'
]

def search_ddg(q):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': q}).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=8)
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a class="result__url" href="([^"]+)">\s*([^<]+)\s*</a>', html)
        out = []
        for u, t in matches:
            out.append((u.strip(), t.strip()))
        return out
    except Exception as e:
        return []

def check_mx(domain):
    try:
        res = dns.resolver.Resolver()
        res.nameservers = ['8.8.8.8', '1.1.1.1']
        res.timeout = 3
        res.lifetime = 5
        records = res.resolve(domain, 'MX')
        return len(records) > 0
    except Exception:
        return False

discovered = {}
print("Executing deep search for unique Becker Pumps distributors...")

for q in queries:
    res = search_ddg(q)
    for u, t in res:
        m = re.search(r'https?://(?:www\.)?([^/]+)', u)
        if m:
            dom = m.group(1).lower()
            if dom not in busch_domains and not any(bk in dom for bk in bad_keywords):
                clean_t = re.sub(r'<[^>]+>', '', t)
                clean_t = re.sub(r'\s+', ' ', clean_t).strip()
                if dom not in discovered:
                    discovered[dom] = clean_t
    time.sleep(1)

print(f"Discovered {len(discovered)} candidate domains for unique Becker distributors.")

# Verify MX
valid_unique = {}
for dom, title in discovered.items():
    if check_mx(dom):
        valid_unique[dom] = title

print(f"Validated {len(valid_unique)} unique domains with active MX records.")

with open('/Users/alt/Desktop/starr/favour/becker_unique_candidates.json', 'w') as f:
    json.dump(valid_unique, f, indent=2)

print("Saved to becker_unique_candidates.json")
