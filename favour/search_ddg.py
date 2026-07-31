from duckduckgo_search import DDGS
import csv
import time
from urllib.parse import urlparse

companies = [
    "A Plus Vacuum & Home Systems",
    "AAA Vacuum Centre",
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
    "Beam Of Windsor",
    "Clearbrook Vacuum",
    "Vacuum Specialists",
    "Don's Heating & Cooling Ltd"
]

results = []
with DDGS() as ddgs:
    for comp in companies:
        if len(results) >= 20: break
        
        try:
            res = list(ddgs.text(comp + " vacuum website", max_results=3))
            domain = "Unknown"
            for r in res:
                link = r['href']
                if "facebook.com" not in link and "yelp.com" not in link and "yellowpages" not in link and "411.ca" not in link and "canpages.ca" not in link and "mapquest" not in link:
                    parsed = urlparse(link)
                    domain = parsed.netloc.replace('www.', '')
                    break
            
            if domain != "Unknown":
                results.append((comp, 'CEO', domain))
                print(f"Found: {comp} -> {domain}")
            time.sleep(1)
        except Exception as e:
            print(f"Error on {comp}: {e}")

with open('canavac_dealers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company', 'CEO/Contact Name', 'Domain'])
    for r in results:
        writer.writerow(r)
print(f"Saved {len(results)} to canavac_dealers.csv")
