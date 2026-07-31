import csv
import time
from urllib.parse import urlparse
try:
    from duckduckgo_search import DDGS
except ImportError:
    print("duckduckgo_search not found. Please install it.")
    exit(1)

def extract_domain(url):
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    return domain

def search_ceo(company_name):
    ceo_name = "Unknown"
    domain = "Unknown"
    email = "Not found"
    
    with DDGS() as ddgs:
        try:
            # Search for the website domain
            res = list(ddgs.text(company_name + " official website", max_results=3))
            for r in res:
                link = r['href']
                if not any(x in link for x in ['facebook.com', 'yelp.com', 'yellowpages', '411.ca', 'canpages.ca', 'linkedin.com', 'mapquest', 'bloomberg']):
                    domain = extract_domain(link)
                    break
                    
            time.sleep(1)
            
            # Search for the CEO
            res_ceo = list(ddgs.text(company_name + " CEO", max_results=3))
            for r in res_ceo:
                title = r['title']
                snippet = r['body']
                # basic heuristics: look for names near CEO
                if "CEO" in title or "CEO" in snippet or "President" in title or "President" in snippet:
                    # just extract a rough name or use the domain to construct a generic one for now
                    # We will output the snippet for manual review or try to parse
                    pass
            
            # We will use a generic format if we can't find it easily
            if domain != "Unknown":
                email = f"info@{domain}"
                
        except Exception as e:
            print(f"Error for {company_name}: {e}")
            
    return domain, ceo_name, email

def main():
    companies = []
    with open('/Users/alt/Desktop/starr/favour/thomaspumps_dealers.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            if row and row[0].strip():
                companies.append(row[0].strip())
                
    results = []
    print(f"Finding info for {len(companies)} companies...")
    for comp in companies:
        domain, ceo, email = search_ceo(comp)
        results.append([comp, ceo, email, domain])
        print(f"{comp} -> {domain} | {email}")
        
    with open('/Users/alt/Desktop/starr/favour/thomaspumps_ceo_emails.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Company', 'CEO/Contact Name', 'Estimated Email', 'Domain'])
        for r in results:
            writer.writerow(r)
            
    print("Done! Saved to thomaspumps_ceo_emails.csv")

if __name__ == "__main__":
    main()
