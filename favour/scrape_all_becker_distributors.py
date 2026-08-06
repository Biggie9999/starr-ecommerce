import urllib.request
import urllib.parse
import re
import time
import socket
import dns.resolver
import concurrent.futures
import csv
import json

queries = [
    '"Becker Pumps" distributor',
    '"Becker Pumps" authorized dealer',
    '"Becker vacuum pump" distributor California',
    '"Becker vacuum pump" distributor Texas',
    '"Becker vacuum pump" distributor Illinois',
    '"Becker vacuum pump" distributor Ohio',
    '"Becker vacuum pump" distributor Pennsylvania',
    '"Becker vacuum pump" distributor Florida',
    '"Becker vacuum pump" distributor New York',
    '"Becker vacuum pump" distributor North Carolina',
    '"Becker vacuum pump" distributor Michigan',
    '"Becker vacuum pump" distributor Georgia',
    '"Becker vacuum pump" distributor Washington',
    '"Becker vacuum pump" distributor Wisconsin',
    '"Becker vacuum pump" distributor Minnesota',
    '"Becker vacuum pump" distributor Missouri',
    '"Becker vacuum pump" distributor Indiana',
    '"Becker vacuum pump" distributor Tennessee',
    '"Becker vacuum pump" distributor Colorado',
    '"Becker vacuum pump" distributor Massachusetts',
    '"Becker vacuum pump" distributor New Jersey',
    '"Becker vacuum pump" distributor Canada',
    '"Becker vacuum pump" distributor UK',
    '"Becker vacuum pump" distributor Australia',
    '"Becker vacuum pump" distributor Germany',
    '"Becker vacuum pump" distributor France',
    '"Becker vacuum pump" distributor Spain',
    '"Becker vacuum pump" distributor Italy',
    '"Becker vacuum pump" distributor Netherlands',
    '"Becker vacuum pump" distributor Sweden',
    '"Becker vacuum pump" distributor South Africa',
    '"Becker vacuum pump" distributor Mexico',
    '"Becker vacuum pump" distributor India',
    '"Becker vacuum pump" representative',
    '"Becker vacuum" sales and service dealer',
    'authorized "Becker vacuum" supplier'
]

bad_domains = [
    'beckerpumps.com', 'becker-international.com', 'becker-canada.com', 'becker-mexico.mx',
    'becker.co.uk', 'becker-india.com', 'duckduckgo.com', 'google.com', 'amazon.com',
    'ebay.com', 'wikipedia.org', 'linkedin.com', 'facebook.com', 'youtube.com',
    'twitter.com', 'instagram.com', 'yelp.com', 'yellowpages.com', 'mapquest.com',
    'chamberofcommerce.com', 'scribd.com', 'dnb.com', 'bloomberg.com', 'zoominfo.com',
    'glassdoor.com', 'indeed.com', 'zippia.com', 'thomasnet.com', 'directindustry.com'
]

def search_ddg(q):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': q}).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a class="result__url" href="([^"]+)">\s*([^<]+)\s*</a>', html)
        snippets = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL)
        out = []
        for i, (u, t) in enumerate(matches):
            snip = snippets[i] if i < len(snippets) else ""
            out.append((u.strip(), t.strip(), snip.strip()))
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

discovered_domains = {}

print("Scraping search engines for Becker Pumps distributors globally...")
for q in queries:
    results = search_ddg(q)
    for u, t, snip in results:
        m = re.search(r'https?://(?:www\.)?([^/]+)', u)
        if m:
            dom = m.group(1).lower()
            if not any(bd in dom for bd in bad_domains):
                clean_t = re.sub(r'<[^>]+>', '', t)
                clean_t = re.sub(r'\s+', ' ', clean_t).strip()
                if dom not in discovered_domains:
                    discovered_domains[dom] = {"title": clean_t, "snippet": snip, "url": u}

print(f"Found {len(discovered_domains)} potential distributor domains.")

print("Verifying domain MX records...")
valid_domains = {}
for dom, info in discovered_domains.items():
    if check_mx(dom):
        valid_domains[dom] = info

print(f"Validated {len(valid_domains)} domains with active MX records.")

with open('/Users/alt/Desktop/starr/favour/becker_raw_distributors.json', 'w') as f:
    json.dump(valid_domains, f, indent=2)

print("Saved raw distributors to becker_raw_distributors.json")
