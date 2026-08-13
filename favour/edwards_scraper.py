import urllib.request
import urllib.parse
import json
import ssl
import csv
import time

def get_distributors(province_id):
    url = "https://myeddie.edwardsfiresafety.com/WhereToBuy/GetDistributorsForProvince"
    data = urllib.parse.urlencode({'provinceID': str(province_id)}).encode('utf-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://myeddie.edwardsfiresafety.com',
        'Referer': 'https://myeddie.edwardsfiresafety.com/WhereToBuy/WhereToBuyEdwards',
        'X-Requested-With': 'XMLHttpRequest',
    }
    
    req = urllib.request.Request(url, data=data, headers=headers)
    
    try:
        response = urllib.request.urlopen(req, context=ctx)
        if response.getcode() == 200:
            resp_data = response.read().decode('utf-8')
            try:
                data = json.loads(resp_data)
                if 'Distributors' in data and 'Items' in data['Distributors']:
                    return data['Distributors']['Items']
            except:
                pass
    except Exception as e:
        pass # Ignore errors like 500 for invalid state IDs
    
    return None

def main():
    all_distributors = {} # Use dict to deduplicate by DistributorID
    
    # Iterate through possible province IDs (US states and Canadian provinces)
    print("Extracting distributors by state/province ID...")
    for pid in range(1, 100):
        print(f"Fetching ID {pid}...", end=" ", flush=True)
        items = get_distributors(pid)
        if items:
            print(f"Found {len(items)}")
            for item in items:
                dist_id = item.get("DistributorID")
                if dist_id:
                    all_distributors[dist_id] = item
        else:
            print("None")
        time.sleep(0.1) # Be polite

    if not all_distributors:
        print("No distributors found. The state IDs might not be mapped 1-100.")
        return

    # Export to CSV
    csv_file = "edwards_distributors.csv"
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        fields = [
            "DistributorID", "DistributorName", "Contact", "Address", "City", 
            "StateCode", "StateName", "Zip", "CountryCode", "CountryName", 
            "Phone", "Email", "Website", "DistributorType", "ActiveStatus", "LastUpdated"
        ]
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        
        for dist_id, dist in all_distributors.items():
            writer.writerow(dist)
            
    print(f"Extraction complete! Saved {len(all_distributors)} unique distributors to {csv_file}")

if __name__ == "__main__":
    main()
