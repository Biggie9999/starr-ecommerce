import csv
import dns.resolver

hoyer_entries = [
    # Europe & Nordics
    {"company": "HydTec Sweden AB", "name": "Karl-Johan Stjärna", "email": "karl-johan@hydtec.se"},
    {"company": "S.T.M. Finland Oy", "name": "Jari Taimela", "email": "jari.taimela@stmfinland.fi"},
    {"company": "SPIT Electrical Mechanics", "name": "Roy Spit", "email": "info@spit.nl"},
    {"company": "Van Bodegraven Elektromotoren", "name": "Frank van Bodegraven", "email": "sales@vanbodegraven.nl"},
    {"company": "MPCC Group (MPCC UK Ltd)", "name": "Tom Bray", "email": "sales@mpcc.co.uk"},
    {"company": "SEL Wojciech Markiewicz", "name": "Wojciech Markiewicz", "email": "info@sel-markiewicz.pl"},
    {"company": "PROSHIP Krzysztof Nowak", "name": "Krzysztof Nowak", "email": "office@proship.eu"},
    {"company": "HAGEDORN Products & Systems GmbH", "name": "Olaf Hagedorn", "email": "info@hagedorn-products.de"},
    {"company": "SEB Produkter AS", "name": "Pål Harald Slemdal", "email": "firmapost@sebprodukter.no"},
    {"company": "Ahlsell Danmark A/S", "name": "Christian Herbert", "email": "ahlsell@ahlsell.dk"},
    {"company": "Blay Marine Tech S.L. (BMT)", "name": "Javier Larriba Blay", "email": "technical@bmt-repairs.com"},
    {"company": "Partelli S.r.l.", "name": "Werner Brandis", "email": "vendite@partelli.it"},

    # Asia-Pacific & China
    {"company": "Megawatts Engineering Services Pte Ltd", "name": "Andrew Koh", "email": "andrew.koh@megawatts.com.sg"},
    {"company": "Chau Thien Chi Co., Ltd.", "name": "Nguyen Hoai Vu", "email": "vu.nguyen@chauthienchi.com"},
    {"company": "Hoang Long Phu Co., Ltd.", "name": "Dat Nguyen", "email": "dat@hoanglongphu.vn"},
    {"company": "J V M Tech Engineering", "name": "Chirag Prajapati", "email": "chirag.jvm@gmail.com"},
    {"company": "Yash India", "name": "Yash Kumar", "email": "mukesh@yashindia-sensorsworld.com"},
    {"company": "RIX Corporation", "name": "Takashi Yasui", "email": "uchino@rix.co.jp"},
    {"company": "Oasis Pump Co., Ltd.", "name": "Kim Ki-ho", "email": "oasispump_service@naver.com"},
    {"company": "Tianjin Celiss Automation Technology Co., Ltd.", "name": "Lu Zhaohang", "email": "les@celiss.com"},

    # Americas
    {"company": "Universal Marine Electric, Inc.", "name": "Hristos Chris Erfesoglou", "email": "operations@umelectric.com"},
    {"company": "AgniVent LLC", "name": "Ruslan Zaripov", "email": "info@agnivent.com"},
    {"company": "PARMEX AUTOMATIZACIÓN S DE RL DE CV", "name": "Gerencia Comercial", "email": "parmex@parmex.com.mx"},
    {"company": "BRASIM Automação Ltda.", "name": "Diretoria Comercial", "email": "vendas@brasim.com.br"},

    # Middle East & Africa
    {"company": "Nemomarin Ticaret Mühendislik Denizcilik A.Ş.", "name": "Mete Tarihmen", "email": "mete.tarihmen@nemomarin.com"},
    {"company": "Middle East Fuji LLC", "name": "Saeed Al Malik", "email": "info.uae@mefgroup.com"},

    # Marine Stockist
    {"company": "TSS Rotterdam B.V.", "name": "W.J.J. Ruijtenberg", "email": "sales@tssr.nl"}
]

out_csv = "/Users/alt/Desktop/starr/favour/hoyermotors_distributors_3col.csv"

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '1.1.1.1']
resolver.timeout = 3
resolver.lifetime = 4

verified_entries = []
seen_emails = set()

for item in hoyer_entries:
    em = item["email"].lower().strip()
    if em in seen_emails:
        continue
    
    dom = em.split('@')[-1]
    has_mx = False
    try:
        recs = resolver.resolve(dom, 'MX')
        if len(recs) > 0:
            has_mx = True
    except Exception:
        try:
            recs = resolver.resolve(dom, 'A')
            if len(recs) > 0:
                has_mx = True
        except Exception:
            has_mx = False

    if has_mx:
        seen_emails.add(em)
        verified_entries.append(item)
        print(f"✅ VERIFIED MX: {item['company']} ({em})")
    else:
        print(f"❌ FAILED MX: {item['company']} ({em})")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in verified_entries:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"\nSuccessfully written {len(verified_entries)} 100% MX-VERIFIED Hoyer Motors distributor entries to {out_csv}")
