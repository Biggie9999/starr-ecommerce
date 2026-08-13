import urllib.request
import urllib.parse
import ssl
import re
import time
import csv
import html as html_lib

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def search_bing(query):
    url = 'https://www.bing.com/search?q=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    })
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        return html
    except Exception as e:
        print(f"Error searching {query}:", e)
        return ""

def extract_results(html):
    snippets = re.findall(r'<div class="b_caption"><p[^>]*>(.*?)</p></div>', html, re.DOTALL | re.IGNORECASE)
    urls = re.findall(r'<h2><a href="([^"]+)"', html, re.DOTALL | re.IGNORECASE)
    
    clean_snippets = [html_lib.unescape(re.sub(r'<[^>]+>', '', s)).strip() for s in snippets]
    clean_urls = [html_lib.unescape(re.sub(r'<[^>]+>', '', u)).strip() for u in urls]
    
    return clean_urls, clean_snippets

distributors = set()
queries = [
    '"vac-u-max" "line card"',
    '"vac-u-max" "distributor"',
    '"vac-u-max" "manufacturers represented"',
    '"vac-u-max" "proud to represent"',
    '"vac-u-max" "principals"',
    '"vac-u-max" "authorized representative"'
]

print("Phase 1: Finding Distributors")
for q in queries:
    print(f"Searching: {q}")
    page_html = search_bing(q)
    urls, snippets = extract_results(page_html)
    for u in urls:
        domain_match = re.search(r'https?://(?:www\.)?([^/]+)', u)
        if domain_match:
            d = domain_match.group(1).lower()
            exclude = ['vac-u-max.com', 'youtube.com', 'facebook.com', 'linkedin.com', 'thomasnet.com', 'iqsdirectory.com', 'directindustry.com', 'powderbulksolids.com', 'bing.com']
            if not any(ex in d for ex in exclude):
                distributors.add(d)
    time.sleep(2)
    if len(distributors) >= 50:
        break

distributors = list(distributors)[:50]
print(f"\nFound {len(distributors)} distributors. Moving to Phase 2 (ZoomInfo).")

results = []
for d in distributors:
    print(f"Checking CEO for {d}...")
    q = f'"{d}" CEO zoominfo'
    page_html = search_bing(q)
    urls, snippets = extract_results(page_html)
    
    ceo_info = "Unknown"
    for s in snippets:
        if 'CEO' in s or 'President' in s or 'Chief Executive' in s or 'Owner' in s:
            ceo_info = s
            break
    
    if ceo_info == "Unknown" and len(snippets) > 0:
        ceo_info = snippets[0]
        
    results.append({
        'Company Domain': d,
        'ZoomInfo CEO Snippet': ceo_info
    })
    time.sleep(2)

print("\nWriting to vacumax_50_zoominfo.csv...")
with open('vacumax_50_zoominfo.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Company Domain', 'ZoomInfo CEO Snippet'])
    writer.writeheader()
    writer.writerows(results)

print("Finished!")
