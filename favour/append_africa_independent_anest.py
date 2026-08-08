import csv

african_independents = [
    {"company": "Specialized Coating Systems (Pty) Ltd (Speccoats)", "name": "Mervyn Cohen", "email": "mervyn@speccoats.co.za"},
    {"company": "Directech (Pty) Ltd", "name": "Peter Erasmus", "email": "peter.erasmus@directech.co.za"},
    {"company": "Spray Tech SA (Pty) Ltd", "name": "Cassie du Preez", "email": "carina@spraytechsa.co.za"},
    {"company": "Surface Coating Technologies (Pty) Ltd (SCT)", "name": "Markus Mändlein", "email": "info@sct.co.za"},
    {"company": "City Paint & Abrasives (Pty) Ltd (CPA Group)", "name": "Gavin Kinnear", "email": "salesb@cpagroup.co.za"},
    {"company": "Braemar Paints", "name": "Simon Braemar", "email": "reception@braemar.co.za"},
    {"company": "Autoboys Automotive (Pty) Ltd", "name": "Filum Ho", "email": "info@autoboys.co.za"},
    {"company": "AIR VAC (Air Vacuum SARL)", "name": "Hamza Bougrine", "email": "contact@airvac.ma"},
    {"company": "Global Paint", "name": "Management Team", "email": "contact@globalpaint.dz"}
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

for item in african_independents:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        seen_emails.add(em)
        existing.append(item)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in existing:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully appended independent African distributors. Total independent Anest Iwata leads: {len(existing)} in {out_csv}")
