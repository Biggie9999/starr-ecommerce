import csv

newly_added = [
    {
        "company": "Airdusco, Inc.",
        "name": "Scott Nease",
        "email": "snease@airdusco.com",
        "domain": "airdusco.com",
        "address": "4739 Mendenhall Road South, Memphis, TN 38141",
        "phone": "901-362-6610",
        "territory": "Arkansas, Mississippi, Western Tennessee"
    },
    {
        "company": "Arizona Pneumatic Systems, Inc.",
        "name": "Mark Johnson",
        "email": "mjohnson@arizonapneumatic.com",
        "domain": "arizonapneumatic.com",
        "address": "205 S River Drive, Tempe, AZ 85281",
        "phone": "480-894-9805",
        "territory": "Arizona, Nevada"
    },
    {
        "company": "Braas Company",
        "name": "Matt Gallagher",
        "email": "FLSales@Braasco.com",
        "domain": "braasco.com",
        "address": "230 E. Douglas Road, Oldsmar, FL 34677",
        "phone": "813-855-4425",
        "territory": "Florida"
    },
    {
        "company": "Brownlee Morrow Engineering Company, Inc.",
        "name": "Tim Morrow",
        "email": "tmorrow@bmeco.com",
        "domain": "bmeco.com",
        "address": "5465 Business Parkway, Building 2, Theodore, AL 36582",
        "phone": "800-624-7069",
        "territory": "Alabama, Florida Panhandle"
    }
]

out_txt = "/Users/alt/Desktop/starr/favour/buschvacuum_newly_added_distributors.txt"
out_csv = "/Users/alt/Desktop/starr/favour/buschvacuum_newly_added_distributors.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(newly_added):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["name"]}" <{item["email"]}>\n')
        if i < len(newly_added) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Executive Name", "Verified Email", "Domain", "Address", "Phone", "Territory"])
    for item in newly_added:
        writer.writerow([item["company"], item["name"], item["email"], item["domain"], item["address"], item["phone"], item["territory"]])

print(f"Saved {len(newly_added)} newly added distributors to {out_txt} and {out_csv}")
