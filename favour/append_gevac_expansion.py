import csv
import dns.resolver

new_entries = [
    # Europe
    {"company": "MAP Service S.r.l.", "name": "Mauro Maffeis", "email": "info@map-service.it"},
    {"company": "Copenhagen Pump", "name": "Executive Management", "email": "info@copenhagenpump.com"},

    # Americas
    {"company": "Air Compressor Services", "name": "Neal Shade", "email": "info@aircompressorservices.com"},
    {"company": "Endura Supply LLC", "name": "Executive Management", "email": "info@endurasupply.com"},

    # Asia
    {"company": "Melkev Machinery Impex", "name": "Kevin Horrace Gonsalvez", "email": "info@melkev.com"},
    {"company": "Nikkypore Filtration Systems Pvt. Ltd.", "name": "Mukul Chadha", "email": "sales@nikkypore.com"},

    # Middle East & Africa
    {"company": "ADUVAC Vakum Mühendislik Hizmetleri San. ve Tic. Ltd. Şti.", "name": "Executive Management", "email": "aduvac@aduvac.com"},
    {"company": "SVC Mühendislik Vakum Pompa Sistemleri", "name": "Executive Management", "email": "info@svcmuhendislik.com"},
    {"company": "Milano Mühendislik Danışmanlık Makina San. Ltd. Şti.", "name": "Executive Management", "email": "milano@milanomuhendislik.com.tr"},
    {"company": "Vacuum Services & Systems CC", "name": "Executive Management", "email": "info@vacuumservices.co.za"}
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

print(f"\nUpdated General Europe Vacuum (GEV) CSV with new verified leads. Total: {len(existing)} entries in {out_csv}")
