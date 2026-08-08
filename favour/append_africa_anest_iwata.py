import csv

africa_anest = [
    {"company": "ANEST IWATA South Africa (Pty) Ltd.", "name": "Deon van der Merwe", "email": "d.vandermerwe@anest-iwata.co.za"},
    {"company": "Sprayquip (Pty) Ltd", "name": "Garth Rattray", "email": "sales@sprayquip.co.za"},
    {"company": "Air & Vacuum Technologies South Africa", "name": "Ian Robertson", "email": "ian@airvac.co.za"},
    {"company": "Air & Power Tools Africa", "name": "Executive Leadership", "email": "sales@airpower.co.za"},
    {"company": "Ashtechs (Antoine Ashba & Co.)", "name": "Antoine Ashba", "email": "cairo@ashtechs.com"},
    {"company": "Société Maghrébine d'Equipement (SME)", "name": "Karim Benjelloun", "email": "contact@sme.ma"}
]

out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

existing = []
seen_emails = set()

with open(out_csv, "r") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if row:
            existing.append({"company": row[0], "name": row[1], "email": row[2]})
            seen_emails.add(row[2].lower().strip())

for item in africa_anest:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        seen_emails.add(em)
        existing.append(item)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in existing:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully expanded Anest Iwata CSV with Africa leads to {len(existing)} entries in {out_csv}")
