import csv
import dns.resolver

new_entries = [
    # Europe
    {"company": "AMO Group OÜ", "name": "Alar Maarend", "email": "alar.maarend@amogroup.ee"},
    {"company": "EB-groep (Elektromotoren Bracke BV)", "name": "Joris Bracke", "email": "info@eb-groep.nl"},
    {"company": "ADD Marine", "name": "Dimitris Koliaroudakis", "email": "koliaroudakis@addmarine.gr"},
    {"company": "Florijn Ship Spares", "name": "Floor Florijn", "email": "info@florijnshipspares.com"},

    # Americas
    {"company": "Einpart LLC", "name": "Jan Poulsen", "email": "einpart@einpart.com"},
    {"company": "ONRION LLC", "name": "Erdogan Karahan", "email": "sales@onrion.com"},
    {"company": "Scardana Corporation", "name": "Philip Rink", "email": "sales@scardana.com"},
    {"company": "Enapart LLC", "name": "Executive Sales Management", "email": "sales@enapart.com"},

    # Asia & China
    {"company": "Shanghai Yinxu Electromechanical Equipment Co., Ltd.", "name": "Pan Dong", "email": "info@yx-intl.com"},
    {"company": "Shanghai Hangou Electromechanical Equipment Co., Ltd.", "name": "Dou Yanchao", "email": "dengchao@shhangou.com"},
    {"company": "Shenzhen Gchane Technology Co., Ltd.", "name": "Chen Ni", "email": "sales@gchane.com"},
    {"company": "Lam Tue Duc Automation Technical Services Co., Ltd.", "name": "Mai Thuy Trinh", "email": "sales@ltdautomation.com.vn"},
    {"company": "Eurododo Co., Ltd", "name": "Pham Quang Tan", "email": "info@eurododo.com"},
    {"company": "Anh Nghi Son Service Trading Co., Ltd. (ANS Vietnam)", "name": "Bui Thi Vu Yen", "email": "lien.ans@ansvietnam.com"},
    {"company": "MPCC Group Singapore", "name": "Thomas Bray", "email": "sales@mpcc.com.sg"},
    {"company": "Drishti Electricals", "name": "Uday Patel", "email": "drishtielectricals@gmail.com"},

    # Middle East & Turkey
    {"company": "İmtek Mühendislik", "name": "Executive Management", "email": "info@imtekmuhendislik.gen.tr"}
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

print(f"\nUpdated Hoyer Motors CSV with new verified leads. Total: {len(existing)} entries in {out_csv}")
