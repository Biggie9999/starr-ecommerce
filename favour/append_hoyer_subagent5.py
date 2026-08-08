import csv
import dns.resolver

new_entries = [
    {"company": "Nordelektro A/S", "name": "Michael Saxtoft", "email": "msa@nordelektro.dk"},
    {"company": "Jens S. Transmissioner A/S", "name": "Thomas Klausen", "email": "thomas.klausen@jens-s.dk"},
    {"company": "TPI El & Automation ApS", "name": "Henrik Nielsen", "email": "hni@tpi-ea.dk"},
    {"company": "O&J Energy A/S", "name": "Claus Boel", "email": "clb@o-j.dk"}
]

out_csv = "/Users/alt/Desktop/starr/favour/hoyermotors_distributors_3col.csv"

existing = []
seen_emails = set()

with open(out_csv, "r") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if row:
            existing.append({"company": row[0], "name": row[1], "email": row[2]})
            seen_emails.add(row[2].lower().strip())

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '1.1.1.1']
resolver.timeout = 3
resolver.lifetime = 4

for item in new_entries:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        dom = em.split('@')[-1]
        try:
            recs = resolver.resolve(dom, 'MX')
            if len(recs) > 0:
                seen_emails.add(em)
                existing.append(item)
                print(f"✅ VERIFIED & APPENDED: {item['company']} ({em})")
        except Exception:
            print(f"❌ FAILED MX: {item['company']} ({em})")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in existing:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"\nUpdated Hoyer Motors CSV with new verified leads. Total: {len(existing)} entries in {out_csv}")
