import csv
import urllib.request
import urllib.parse
import re
import ssl
import time

def enrich_data(input_csv, output_csv, max_rows=None):
    # Regex to find emails
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    # Simple regex to try to find CEO/President names (e.g. "CEO John Doe")
    ceo_pattern = re.compile(r'(?:CEO|President|Owner)[\s:,-]+([A-Z][a-z]+ [A-Z][a-z]+)')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    results = []
    
    with open(input_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames + ['Found_CEO_Name', 'Found_Emails']
        rows = list(reader)

    if max_rows:
        rows = rows[:max_rows]

    print(f"Processing {len(rows)} companies...")

    for index, row in enumerate(rows):
        website = row.get('Website', '').strip()
        found_emails = set()
        found_ceo = ""

        # Use existing email if available as a baseline
        if row.get('Email'):
            found_emails.add(row.get('Email').strip())

        if website:
            if not website.startswith('http'):
                url = 'http://' + website
            else:
                url = website

            print(f"[{index+1}/{len(rows)}] Scraping {url}...")
            
            try:
                req = urllib.request.Request(url, headers=headers)
                response = urllib.request.urlopen(req, context=ctx, timeout=5)
                
                # Only read if it's HTML (to avoid downloading PDFs, etc.)
                content_type = response.headers.get('Content-Type', '')
                if 'text/html' in content_type:
                    html_content = response.read().decode('utf-8', errors='ignore')
                    
                    # Find emails
                    emails = email_pattern.findall(html_content)
                    for e in emails:
                        # Exclude some common false positives or image extensions
                        if not e.lower().endswith(('.png', '.jpg', '.gif', 'sentry.io')):
                            found_emails.add(e.lower())
                    
                    # Find CEO
                    ceo_matches = ceo_pattern.findall(html_content)
                    if ceo_matches:
                        # Just grab the first plausible match
                        found_ceo = ceo_matches[0]
            except Exception as e:
                print(f"  -> Error accessing {url}: {e}")
        
        row['Found_CEO_Name'] = found_ceo
        row['Found_Emails'] = ", ".join(list(found_emails))
        results.append(row)
        time.sleep(0.5) # Be polite

    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print(f"Enrichment complete! Saved to {output_csv}")

if __name__ == "__main__":
    import sys
    max_rows = None
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        max_rows = 10
    
    enrich_data('edwards_distributors.csv', 'edwards_distributors_enriched.csv', max_rows)
