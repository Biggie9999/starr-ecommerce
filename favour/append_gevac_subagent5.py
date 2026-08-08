import csv
import dns.resolver

new_entries = [
    {"company": "SD Industrial Equipment Limited (AIR24)", "name": "Andrea Dobos", "email": "air24@air24.ie"},
    {"company": "Rotamec Engineering Ltd", "name": "Simon Brooks", "email": "sales@rotamec.co.uk"},
    {"company": "Summit Electronics A/S (Copenhagen Pump)", "name": "Henrik Steffensen", "email": "info@summit.dk"},
    {"company": "VAKUUM BOHEMIA s.r.o.", "name": "Ing. Vít Němec", "email": "info@vakuum-bohemia.cz"},
    {"company": "HES Tıbbi Cihazlar San. ve Tic. Ltd. Şti.", "name": "Executive Management", "email": "info@hestibbicihazlar.com.tr"},
    {"company": "Cemix Pro Nigeria Limited", "name": "Executive Management", "email": "sales@cemix-nigeria.com"}
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
