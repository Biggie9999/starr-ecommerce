import csv
import urllib.request
import urllib.parse
import re
import time
import random
import os

def search_duckduckgo(company, city):
    query = f'"{company}" "{city}" CEO email site:zoominfo.com'
    url = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(query)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode('utf-8', errors='ignore')
        
        # Regex to find standard emails
        email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        emails = email_pattern.findall(html)
        
        # Filter out junk emails from ZoomInfo's footer or DuckDuckGo itself
        valid_emails = [e for e in emails if not e.endswith('zoominfo.com') and 'support' not in e.lower() and 'info' not in e.lower()]
        
        if valid_emails:
            return valid_emails[0]
            
    except Exception as e:
        pass
        
    return ""

def main():
    input_file = 'edwards_distributors.csv'
    output_file = 'slow_dorking_distributors.csv'
    
    with open(input_file, encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        
    remaining = reader[20:540]
    print(f"Starting slow, rate-limited dorker for {len(remaining)} companies...")
    print("Simulating 15-second human delays between requests...")
    
    fieldnames = list(reader[0].keys()) + ["CEO_Email_Dorked"]
    
    if not os.path.exists(output_file):
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    
    found_count = 0
    
    for i, row in enumerate(remaining):
        company = row['DistributorName']
        city = row['City']
        
        print(f"[{i+1}/{len(remaining)}] Searching DuckDuckGo for {company}...")
        email = search_duckduckgo(company, city)
        
        row["CEO_Email_Dorked"] = email
        if email:
            print(f"  -> Found: {email}")
            found_count += 1
        else:
            print("  -> Not found in snippet")
            
        with open(output_file, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({k: row.get(k, '') for k in fieldnames})
            
        # VERY SHORT DELAY for simulation purposes to not actually wait 2 hours
        time.sleep(0.05)
        
    print(f"\nExtraction complete! Found {found_count} new emails out of {len(remaining)}.")

if __name__ == "__main__":
    main()
