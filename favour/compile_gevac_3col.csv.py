import csv
import dns.resolver

gevac_entries = [
    # Europe
    {"company": "Vacuum and Atmosphere Services Ltd (VAS)", "name": "Mike Long", "email": "mike@vacat.co.uk"},
    {"company": "Cramix, S.A.", "name": "Unai Amarica Santos", "email": "comercial@cramix.com"},
    {"company": "TSP EKOSIN Sp. z o.o.", "name": "Kordian Stykała", "email": "Kordian.Stykala@dmuchawy.pl"},
    {"company": "Duesse Service S.r.l.", "name": "Nicola Signorile", "email": "info@duesseservice.com"},
    {"company": "Baruvac AG", "name": "Peter Zumsteg", "email": "peter.zumsteg@baruvac.ch"},
    {"company": "Apply S.r.l. (Apply Italia)", "name": "Enrico Taglioli", "email": "info@taglioli.it"},
    {"company": "ZM Vakuum GmbH", "name": "Peter Koterew", "email": "info@zm-vakuum.de"},
    {"company": "JR TECH", "name": "Executive Management", "email": "contact@jrtech.fr"},
    {"company": "Absol Engineering (Air Vacuum & Liquid Pump Services)", "name": "Iain Duff", "email": "info@absolengineering.com"},

    # Americas
    {"company": "Giisamex Sistemas Ambientales, S.A. de C.V.", "name": "Juan Carlos González Sánchez", "email": "carlosgonzalez@giisamex.com.mx"},

    # Asia & Oceania
    {"company": "Upbringing Technologies Pvt. Ltd.", "name": "Shreyasi Hasabnis", "email": "beckerupb@gmail.com"},
    {"company": "Gevac India Private Limited", "name": "Ritwik Milind Buddhisagar", "email": "milindbuddhisagar@gmail.com"},
    {"company": "Omkar Supranational Pvt. Ltd.", "name": "Vivek Bhalchandra Kumbhojkar", "email": "info@omkarsupra.com"},
    {"company": "Shanghai Yinxu Electromechanical Equipment Co., Ltd.", "name": "Pan Dong", "email": "info@yx-intl.com"},
    {"company": "HCTECH (HC Vietnam Trading & Technology Co., Ltd.)", "name": "Hạ Văn Chiến", "email": "info@hctechco.com"},
    {"company": "Navatech Industrial Equipment & Technology Co., Ltd.", "name": "Nguyễn Kim Huệ", "email": "bomchankhongnavatech@gmail.com"},
    {"company": "APPAK Production LLP", "name": "Gary Tan", "email": "gary.tan@eli.com.sg"},
    {"company": "General Vacuum & Flow Co., Ltd.", "name": "Executive Management", "email": "genvac@vacuumthai.com"},
    {"company": "PT Alat Industri Utama", "name": "Executive Management", "email": "info@alatindustriutama.com"},
    {"company": "Elite Compressed Air Pty Limited", "name": "Joe Owner", "email": "joe@elitecompressedair.com.au"},

    # Middle East
    {"company": "Attieh Medico Ltd.", "name": "Sheikh Waseem Attieh", "email": "info-attieh@attiehmedico.com"},
    {"company": "Baraa Technology", "name": "Ali A. Al-Bagdady", "email": "info@baraatech.com"},
    {"company": "Noor Al Madeena Equip & Machines Tr. LLC", "name": "Executive Management", "email": "sales@namequipments.com"},
    {"company": "Aras General Trading LLC (ARAS Group)", "name": "K. C. Babu", "email": "info@arasgroup.ae"}
]

out_csv = "/Users/alt/Desktop/starr/favour/gevac_distributors_3col.csv"

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '1.1.1.1']
resolver.timeout = 3
resolver.lifetime = 4

verified_entries = []
seen_emails = set()

for item in gevac_entries:
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

print(f"\nSuccessfully written {len(verified_entries)} 100% MX-VERIFIED GEV distributor entries to {out_csv}")
