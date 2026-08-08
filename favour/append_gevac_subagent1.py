import csv
import dns.resolver

new_entries = [
    {"company": "CONCES Przedsiębiorstwo Produkcyjno-Remontowe s.c.", "name": "Mariusz Mykicki", "email": "conces@conces.com.pl"},
    {"company": "Elettromeccanica Pierro S.r.l.", "name": "Salvatore Pierro", "email": "elpierro@hotmail.it"},
    {"company": "Impexron GmbH", "name": "Erdogan Karahan", "email": "info@impexron.de"},
    {"company": "FAMAGA Group GmbH & Co. KG", "name": "Emil Aghayev", "email": "info@famaga.de"}
]

out_csv = "/Users/alt/Desktop/starr/favour/gevac_distributors_3col.csv"

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
            try:
                recs = resolver.resolve(dom, 'A')
                if len(recs) > 0:
                    seen_emails.add(em)
                    existing.append(item)
                    print(f"✅ VERIFIED A-REC: {item['company']} ({em})")
            except Exception:
                print(f"❌ FAILED MX: {item['company']} ({em})")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in existing:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"\nUpdated GEV CSV with new verified leads. Total: {len(existing)} entries in {out_csv}")
