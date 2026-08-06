import json
import urllib.request
import urllib.parse
import re
import dns.resolver
import concurrent.futures
import csv
import time

def check_mx(domain):
    try:
        res = dns.resolver.Resolver()
        res.nameservers = ['8.8.8.8', '1.1.1.1']
        res.timeout = 3
        res.lifetime = 5
        records = res.resolve(domain, 'MX')
        return True
    except Exception:
        return False

def search_ceo_for_domain(domain, company_name=""):
    url = "https://html.duckduckgo.com/html/"
    q = f'"{domain}" CEO OR President OR Founder OR Owner'
    data = urllib.parse.urlencode({'q': q}).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=8)
        html = resp.read().decode('utf-8', errors='ignore')
        # Extract title and snippets
        snippets = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL)
        text = " ".join(snippets)
        text = re.sub(r'<[^>]+>', '', text)
        return text
    except Exception:
        return ""

def process_company(item):
    domain, info = item
    title = info['title']
    
    # Check MX first
    if not check_mx(domain):
        return None
        
    text = search_ceo_for_domain(domain, title)
    
    # Try heuristic extraction of President / CEO
    m_ceo = re.search(r'([A-Z][a-z]+\s+(?:[A-Z]\.\s+)?[A-Z][a-z]+)\s*(?:,|\s+is|\s+-)?\s*(?:CEO|President|Founder|Owner|Managing Director)', text)
    ceo_name = m_ceo.group(1) if m_ceo else ""
    
    return {
        "domain": domain,
        "title": title,
        "ceo_extracted": ceo_name,
        "snippet": text[:300]
    }

def main():
    try:
        with open('/Users/alt/Desktop/starr/favour/becker_raw_distributors.json', 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading json: {e}")
        return

    print(f"Processing {len(data)} domains...")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_company, item) for item in data.items()]
        for fut in concurrent.futures.as_completed(futures):
            res = fut.result()
            if res:
                results.append(res)
                print(f"Processed: {res['domain']} -> {res['ceo_extracted']}")

    with open('/Users/alt/Desktop/starr/favour/becker_processed_ceos.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Done processing {len(results)} active MX domains.")

if __name__ == '__main__':
    main()
