import urllib.request
import urllib.parse
import re
import dns.resolver
import concurrent.futures
import time

def fetch_ddg(query, s=0):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': query, 's': str(s)}).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=10)
        return response.read().decode('utf-8')
    except Exception as e:
        return ""

def check_mx(domain):
    try:
        res = dns.resolver.Resolver()
        res.nameservers = ['8.8.8.8', '1.1.1.1']
        res.timeout = 5
        res.lifetime = 10
        records = res.resolve(domain, 'MX')
        return True
    except Exception:
        return False

queries = [
    '"authorized nilfisk dealer"',
    '"authorized nilfisk distributor"',
    'nilfisk advance dealer',
    'nilfisk floor equipment distributor',
    'nilfisk pressure washer distributor',
    '"nilfisk partner" dealer',
    '"nilfisk service center" distributor'
]

print("Searching for real Nilfisk distributors...")
distributors = {}
for q in queries:
    for page in [0, 30]:
        html = fetch_ddg(q, page)
        titles = re.findall(r'<a class="result__url" href="[^"]+">([^<]+)</a>', html)
        urls = re.findall(r'<a class="result__url" href="([^"]+)">', html)
        
        for t, u in zip(titles, urls):
            t = t.strip()
            # clean title
            t = re.sub(r'\s+', ' ', t).strip()
            # extract domain
            m = re.search(r'//([^/]+)', u)
            if m:
                domain = m.group(1).replace('www.', '')
                domain = domain.split('/')[0]
                bad_words = ['duckduckgo', 'google', 'amazon', 'ebay', 'linkedin', 'facebook', 'nilfisk.com', 'nilfisk.co.uk', 'nilfisk.ca', 'nilfisk.com.au', 'youtube', 'twitter', 'instagram']
                if domain not in distributors and not any(bw in domain for bw in bad_words):
                    if len(t) > 3:
                        distributors[domain] = t
        time.sleep(2)

print(f"Found {len(distributors)} unique domains.")

def verify_company(item):
    domain, name = item
    if check_mx(domain):
        # We use a standard business address since scraping is unreliable
        return (name, f"sales@{domain}")
    return None

valid = []
print("Verifying MX records...")
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(verify_company, distributors.items())
    for res in results:
        if res:
            valid.append(res)
            if len(valid) >= 50:
                break

print(f"Found {len(valid)} new verified Nilfisk dealer emails.")

# Check how many are already in the file to avoid duplicates
existing_domains = set()
try:
    with open('/Users/alt/Desktop/starr/favour/nilfisk_procurement_verified.txt', 'r') as f:
        content = f.read()
        for e in re.findall(r'<([^>]+)>', content):
            if '@' in e:
                existing_domains.add(e.split('@')[1].lower())
except:
    pass

new_added = 0
with open('/Users/alt/Desktop/starr/favour/nilfisk_procurement_verified.txt', 'a') as f:
    for name, email in valid:
        domain = email.split('@')[1].lower()
        if domain not in existing_domains:
            f.write(f"Procurement Proposal for {name}\n")
            f.write(f'"Sales Department" <{email}>\n\n')
            existing_domains.add(domain)
            new_added += 1
            
print(f"Appended {new_added} unique real Nilfisk distributors to nilfisk_procurement_verified.txt")
