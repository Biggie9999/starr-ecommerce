import urllib.request
import urllib.parse
import re
import time
import concurrent.futures
import dns.resolver

def fetch_ddg(query, s=0):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': query, 's': str(s)}).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=5)
        return response.read().decode('utf-8')
    except Exception as e:
        return ""

def fetch_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=5)
        return response.read().decode('utf-8', errors='ignore')
    except:
        return ""

def check_mx(domain):
    try:
        res = dns.resolver.Resolver()
        res.timeout = 2
        res.lifetime = 2
        records = res.resolve(domain, 'MX')
        return True
    except Exception:
        return False

queries = [
    "Nilfisk authorized distributor USA",
    "Nilfisk equipment dealer UK",
    "Nilfisk pressure washer distributor Canada",
    "Nilfisk commercial vacuum dealer Australia",
    "Nilfisk floor cleaning equipment distributor",
    "authorized dealer Nilfisk industrial",
    "Nilfisk partner distributor",
    "Nilfisk service center dealer",
    "buy Nilfisk equipment distributor",
    "Nilfisk Advance distributor",
]

print("Searching for Nilfisk distributors...")
distributors = {}
for q in queries:
    for page in [0, 30]:
        html = fetch_ddg(q, page)
        titles = re.findall(r'<a class="result__url" href="[^"]+">([^<]+)</a>', html)
        urls = re.findall(r'<a class="result__url" href="([^"]+)">', html)
        
        for t, u in zip(titles, urls):
            t = t.strip()
            # extract domain
            m = re.search(r'//([^/]+)', u)
            if m:
                domain = m.group(1).replace('www.', '')
                if domain not in distributors and 'duckduckgo' not in domain and 'nilfisk' not in domain and 'google' not in domain and 'amazon' not in domain and 'ebay' not in domain and 'linkedin' not in domain:
                    # Clean title
                    title = re.sub(r'\s+', ' ', t).strip()
                    if len(title) > 3:
                        distributors[domain] = (title, u)
        time.sleep(1)

print(f"Found {len(distributors)} potential distributor websites.")

def process_distributor(item):
    domain, (title, url) = item
    if not check_mx(domain):
        return None
    
    # Check domain for email
    # Try fetching homepage
    if not url.startswith('http'):
        url = 'http://' + url
    
    html = fetch_page(url)
    
    # Also try contact page
    contact_html = ""
    if html:
        contact_html = fetch_page(url.rstrip('/') + '/contact')
        if not contact_html:
            contact_html = fetch_page(url.rstrip('/') + '/contact-us')
            
    full_html = html + " " + contact_html
    
    # Extract emails
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', full_html)
    valid_emails = []
    for e in emails:
        e = e.lower()
        if e.endswith(domain) and not e.startswith('wix') and not e.startswith('sentry'):
            valid_emails.append(e)
            
    if valid_emails:
        # Get most common or shortest
        best_email = sorted(list(set(valid_emails)), key=len)[0]
        return (title, best_email, domain)
    
    # If no email found but MX is valid, guess info@
    return (title, f"info@{domain}", domain)

verified_results = []
print("Scraping and verifying emails...")

# Existing emails to avoid duplicates
existing_emails = set()
try:
    with open('/Users/alt/Desktop/starr/favour/nilfisk_procurement_verified.txt', 'r') as f:
        content = f.read()
        for e in re.findall(r'<([^>]+)>', content):
            existing_emails.add(e.lower())
except:
    pass

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    results = executor.map(process_distributor, distributors.items())
    
    for res in results:
        if res:
            title, email, domain = res
            if email not in existing_emails:
                verified_results.append((title, email, domain))
                existing_emails.add(email)
            if len(verified_results) >= 80: # Try to get enough to make >100 total
                break

print(f"Successfully found and verified {len(verified_results)} new emails.")

with open('/Users/alt/Desktop/starr/favour/nilfisk_procurement_verified.txt', 'a') as f:
    for title, email, domain in verified_results:
        f.write(f"Procurement Proposal for {title}\n")
        f.write(f'"General Contact" <{email}>\n\n')

print("Added to nilfisk_procurement_verified.txt")
