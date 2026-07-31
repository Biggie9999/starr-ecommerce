import urllib.request
import urllib.parse
import re
import time

companies = [
    "A & J vacuum supplies",
    "A Plus Vacuum & Home Systems",
    "AAA Vacuum Centre",
    "ALL VICTORIA VACUUMS",
    "Al S Vacuum",
    "Alberta Vacuum Experts",
    "Amati Home Systems",
    "Armstrong Installers",
    "Aspirabec Inc.",
    "Aspirateur 2000 plus inc.",
    "Aspirateur Direct",
    "Aspirateur Dorion",
    "Aspirateur Mont-Tremblant",
    "Aspirateur Rp Vacuum",
    "Aspirateurs Mascouche Inc.",
    "Aspirateurs Picard",
    "Aspirateurs Samson",
    "Aspirateurs Valleyfield",
    "Aspiro Plus",
    "Austin's Appliance & Sleep Centre",
    "Automatic Switching Inc",
    "BLUE MOUNTAIN VACUUM CENTRE",
    "Beam Of Windsor"
]

import csv
with open('canavac_dealers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company', 'CEO/Contact Name', 'Domain'])
    
    count = 0
    for comp in companies:
        if count >= 20: break
        
        q = urllib.parse.quote(comp + " vacuum website")
        url = "https://html.duckduckgo.com/html/?q=" + q
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        domain = "Unknown"
        try:
            html = urllib.request.urlopen(req).read().decode("utf-8")
            urls = re.findall(r'class="result__url" href="//duckduckgo\.com/l/\?uddg=([^&]+)', html)
            for u in urls:
                decoded_u = urllib.parse.unquote(u)
                if "facebook.com" not in decoded_u and "yelp.com" not in decoded_u and "yellowpages" not in decoded_u and "411.ca" not in decoded_u and "canpages.ca" not in decoded_u:
                    domain = decoded_u
                    break
        except Exception as e:
            pass
        
        if domain != "Unknown":
            # Extract just the domain
            from urllib.parse import urlparse
            parsed = urlparse(domain)
            domain = parsed.netloc.replace('www.', '')
            
        writer.writerow([comp, 'CEO', domain])
        print(f"Processed: {comp} -> {domain}")
        count += 1
        time.sleep(2)
