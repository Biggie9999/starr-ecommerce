import csv

photo_dealers = [
    {"company": "Airdusco, Inc.", "ceo": "Scott Nease", "email": "snease@airdusco.com", "domain": "airdusco.com", "notes": "Official Busch Authorized Distributor (Memphis, TN; Arkansas/Mississippi/TN territory)."},
    {"company": "Anderson Process", "ceo": "Greg Domino", "email": "gdomino@andersonprocess.com", "domain": "andersonprocess.com", "notes": "Official Busch Authorized Distributor (Indianapolis, IN; Indiana/Kentucky territory). Already in list."},
    {"company": "Arizona Pneumatic Systems, Inc.", "ceo": "Mark Johnson", "email": "mjohnson@arizonapneumatic.com", "domain": "arizonapneumatic.com", "notes": "Official Busch Authorized Distributor (Tempe, AZ; Arizona/Nevada territory)."},
    {"company": "Braas Company", "ceo": "Matt Gallagher", "email": "FLSales@Braasco.com", "domain": "braasco.com", "notes": "Official Busch Authorized Distributor (Oldsmar, FL; Florida territory)."},
    {"company": "Brownlee Morrow Engineering Company, Inc.", "ceo": "Tim Morrow", "email": "tmorrow@bmeco.com", "domain": "bmeco.com", "notes": "Official Busch Authorized Distributor (Theodore, AL; Alabama/Florida Panhandle territory)."}
]

# Read existing Busch CSV
existing_busch = []
existing_domains = set()

with open("/Users/alt/Desktop/starr/favour/buschvacuum_dealers.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing_busch.append(row)
        existing_domains.add(row.get("Domain", "").strip().lower())

added_count = 0
for item in photo_dealers:
    if item["domain"] not in existing_domains:
        existing_busch.append({
            "Company": item["company"],
            "CEO/Contact Name": item["ceo"],
            "Email": item["email"],
            "Domain": item["domain"]
        })
        existing_domains.add(item["domain"])
        added_count += 1

print(f"Added {added_count} new official Busch distributors from screenshot.")

# Write updated buschvacuum_procurement.txt and buschvacuum_dealers.csv
out_txt = "/Users/alt/Desktop/starr/favour/buschvacuum_procurement.txt"
out_csv = "/Users/alt/Desktop/starr/favour/buschvacuum_dealers.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(existing_busch):
        f.write(f"Procurement Proposal for {item['Company']}\n")
        f.write(f'"{item["CEO/Contact Name"]}" <{item["Email"]}>\n')
        if i < len(existing_busch) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "CEO/Contact Name", "Email", "Domain"])
    for item in existing_busch:
        writer.writerow([item["Company"], item["CEO/Contact Name"], item["Email"], item["Domain"]])

print(f"Updated {len(existing_busch)} total entries in {out_txt} and {out_csv}")
