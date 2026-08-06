import urllib.request
import urllib.parse
import re
import json
import dns.resolver
import concurrent.futures
import csv
import time

search_terms = [
    '"Becker Pumps" "territory manager"',
    '"Becker Pumps" "area manager"',
    '"Becker Pumps" authorized distributor',
    '"Becker vacuum" distributor Alabama',
    '"Becker vacuum" distributor Alaska',
    '"Becker vacuum" distributor Arizona',
    '"Becker vacuum" distributor Arkansas',
    '"Becker vacuum" distributor California',
    '"Becker vacuum" distributor Colorado',
    '"Becker vacuum" distributor Connecticut',
    '"Becker vacuum" distributor Delaware',
    '"Becker vacuum" distributor Florida',
    '"Becker vacuum" distributor Georgia',
    '"Becker vacuum" distributor Hawaii',
    '"Becker vacuum" distributor Idaho',
    '"Becker vacuum" distributor Illinois',
    '"Becker vacuum" distributor Indiana',
    '"Becker vacuum" distributor Iowa',
    '"Becker vacuum" distributor Kansas',
    '"Becker vacuum" distributor Kentucky',
    '"Becker vacuum" distributor Louisiana',
    '"Becker vacuum" distributor Maine',
    '"Becker vacuum" distributor Maryland',
    '"Becker vacuum" distributor Massachusetts',
    '"Becker vacuum" distributor Michigan',
    '"Becker vacuum" distributor Minnesota',
    '"Becker vacuum" distributor Mississippi',
    '"Becker vacuum" distributor Missouri',
    '"Becker vacuum" distributor Montana',
    '"Becker vacuum" distributor Nebraska',
    '"Becker vacuum" distributor Nevada',
    '"Becker vacuum" distributor New Hampshire',
    '"Becker vacuum" distributor New Jersey',
    '"Becker vacuum" distributor New Mexico',
    '"Becker vacuum" distributor New York',
    '"Becker vacuum" distributor North Carolina',
    '"Becker vacuum" distributor North Dakota',
    '"Becker vacuum" distributor Ohio',
    '"Becker vacuum" distributor Oklahoma',
    '"Becker vacuum" distributor Oregon',
    '"Becker vacuum" distributor Pennsylvania',
    '"Becker vacuum" distributor Rhode Island',
    '"Becker vacuum" distributor South Carolina',
    '"Becker vacuum" distributor South Dakota',
    '"Becker vacuum" distributor Tennessee',
    '"Becker vacuum" distributor Texas',
    '"Becker vacuum" distributor Utah',
    '"Becker vacuum" distributor Vermont',
    '"Becker vacuum" distributor Virginia',
    '"Becker vacuum" distributor Washington',
    '"Becker vacuum" distributor West Virginia',
    '"Becker vacuum" distributor Wisconsin',
    '"Becker vacuum" distributor Wyoming',
    '"Becker vacuum" distributor Canada',
    '"Becker vacuum" distributor Ontario',
    '"Becker vacuum" distributor Quebec',
    '"Becker vacuum" distributor Alberta',
    '"Becker vacuum" distributor British Columbia',
    '"Becker vacuum" distributor UK',
    '"Becker vacuum" distributor England',
    '"Becker vacuum" distributor Scotland',
    '"Becker vacuum" distributor Ireland',
    '"Becker vacuum" distributor Germany',
    '"Becker vacuum" distributor France',
    '"Becker vacuum" distributor Italy',
    '"Becker vacuum" distributor Spain',
    '"Becker vacuum" distributor Netherlands',
    '"Becker vacuum" distributor Belgium',
    '"Becker vacuum" distributor Switzerland',
    '"Becker vacuum" distributor Austria',
    '"Becker vacuum" distributor Poland',
    '"Becker vacuum" distributor Czech Republic',
    '"Becker vacuum" distributor Sweden',
    '"Becker vacuum" distributor Norway',
    '"Becker vacuum" distributor Denmark',
    '"Becker vacuum" distributor Finland',
    '"Becker vacuum" distributor Australia',
    '"Becker vacuum" distributor New Zealand',
    '"Becker vacuum" distributor Japan',
    '"Becker vacuum" distributor China',
    '"Becker vacuum" distributor India',
    '"Becker vacuum" distributor Singapore',
    '"Becker vacuum" distributor South Korea',
    '"Becker vacuum" distributor Brazil',
    '"Becker vacuum" distributor Mexico',
    '"Becker vacuum" distributor Chile',
    '"Becker vacuum" distributor Argentina',
    '"Becker vacuum" distributor South Africa',
    '"Becker vacuum" distributor UAE',
    '"Becker vacuum" distributor Saudi Arabia'
]

bad_domains = [
    'beckerpumps.com', 'becker-international.com', 'becker-canada.com', 'becker-mexico.mx',
    'becker.co.uk', 'becker-india.com', 'duckduckgo.com', 'google.com', 'amazon.com',
    'ebay.com', 'wikipedia.org', 'linkedin.com', 'facebook.com', 'youtube.com',
    'twitter.com', 'instagram.com', 'yelp.com', 'yellowpages.com', 'mapquest.com',
    'chamberofcommerce.com', 'scribd.com', 'dnb.com', 'bloomberg.com', 'zoominfo.com',
    'glassdoor.com', 'indeed.com', 'zippia.com', 'thomasnet.com', 'directindustry.com', 'radwell.com'
]

def search_ddg(q):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': q}).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=8)
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a class="result__url" href="([^"]+)">\s*([^<]+)\s*</a>', html)
        out = []
        for u, t in matches:
            out.append((u.strip(), t.strip()))
        return out
    except Exception:
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
print(f"Scanning everywhere across {len(search_terms)} queries for Becker Pumps distributors...")

for i, q in enumerate(search_terms):
    results = search_ddg(q)
    for u, t in results:
        m = re.search(r'https?://(?:www\.)?([^/]+)', u)
        if m:
            dom = m.group(1).lower()
            if not any(bd in dom for bd in bad_domains):
                clean_t = re.sub(r'<[^>]+>', '', t)
                clean_t = re.sub(r'\s+', ' ', clean_t).strip()
                if dom not in discovered:
                    discovered[dom] = clean_t
    if i % 10 == 0:
        print(f"Progress: {i}/{len(search_terms)} queries scanned. Discovered {len(discovered)} candidate domains.")
    time.sleep(0.5)

print(f"Scan complete. Discovered {len(discovered)} total potential distributor domains.")

valid_domains = {}
for dom, title in discovered.items():
    if check_mx(dom):
        valid_domains[dom] = title

print(f"Validated {len(valid_domains)} domains with active MX records.")

with open('/Users/alt/Desktop/starr/favour/becker_deep_scan_raw.json', 'w') as f:
    json.dump(valid_domains, f, indent=2)

print("Saved raw scan to becker_deep_scan_raw.json")
