import csv
import json

# Load Busch domains
busch_domains = set()
try:
    with open("/Users/alt/Desktop/starr/favour/buschvacuum_dealers.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dom = row.get("Domain", "").strip().lower()
            if dom:
                busch_domains.add(dom)
            comp = row.get("Company", "").strip().lower()
            if comp:
                busch_domains.add(comp)
except Exception as e:
    print(f"Error reading Busch CSV: {e}")

print(f"Loaded {len(busch_domains)} Busch identifiers/domains to exclude.")

# Load Becker Master list
becker_master = []
with open("/Users/alt/Desktop/starr/favour/beckerpumps_procurement_master.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        becker_master.append(row)

unique_becker = []
excluded_count = 0

for item in becker_master:
    domain = item.get("Domain", "").strip().lower()
    company = item.get("Company / Entity", "").strip().lower()
    
    # Check if domain or company is in busch_domains
    if domain in busch_domains or company in busch_domains:
        excluded_count += 1
        print(f"Excluding duplicate from Busch: {item['Company / Entity']} ({domain})")
    else:
        unique_becker.append(item)

print(f"Total Becker entities before filter: {len(becker_master)}")
print(f"Excluded duplicates: {excluded_count}")
print(f"Unique Becker entities remaining: {len(unique_becker)}")

out_txt = "/Users/alt/Desktop/starr/favour/beckerpumps_unique_distributors.txt"
out_csv = "/Users/alt/Desktop/starr/favour/beckerpumps_unique_distributors.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(unique_becker):
        f.write(f"Procurement Proposal for {item['Company / Entity']}\n")
        f.write(f'"{item["CEO / President Name"]}" <{item["Executive Email"]}>\n')
        if i < len(unique_becker) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company / Entity", "CEO / President Name", "Executive Email", "Domain", "Title / Role"])
    for item in unique_becker:
        writer.writerow([item["Company / Entity"], item["CEO / President Name"], item["Executive Email"], item["Domain"], item["Title / Role"]])

print(f"Saved unique Becker procurement list to {out_txt} and {out_csv}")
