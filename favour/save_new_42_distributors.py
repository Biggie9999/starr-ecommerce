import csv

new_42_distributors = [
    # Europe
    {"company": "Low2High Vacuum AB", "name": "Pontus Bengtsson", "email": "pontus.bengtsson@low2high.se"},
    {"company": "Vacuum-Tech s.c.", "name": "Marcin Brzozowski", "email": "marcin@vacuum-tech.pl"},
    {"company": "Noviebro, S.L.", "name": "Sofía Cabrerizo Pérez", "email": "sofia.cabrerizo@noviebro.com"},
    {"company": "Krull GmbH", "name": "Sven Krull", "email": "s.krull@krull-gmbh.de"},
    {"company": "Schwarzer GmbH & Co. KG", "name": "Christian Schwarzer", "email": "christian.schwarzer@schwarzer-emb.de"},
    {"company": "R.D. MEC S.r.l.", "name": "Roberto Boscariol", "email": "direzione@rdmec.it"},
    {"company": "Pneumatics & Sensors Ireland", "name": "Michael Murphy", "email": "info@psireland.ie"},
    {"company": "Greger GmbH", "name": "Norbert Greger", "email": "greger-pumpen@t-online.de"},
    {"company": "TENBA SAS", "name": "Thierry Toussaint", "email": "tenba@tenba.fr"},
    {"company": "DS Industriale SAS", "name": "Devis Dal Soglio", "email": "info@dsrappresentanze.com"},
    {"company": "Graafinen Kunnossapito Grönkvist & Co", "name": "Jorma Grönkvist", "email": "graafinen.kunnossapito@co.inet.fi"},
    {"company": "Turoteknikk AS", "name": "Magne Klemmet Løseth", "email": "mail@turoteknikk.no"},
    {"company": "VacAir Superstore Limited", "name": "Graham Moorby", "email": "sales@vacair-superstore.com"},
    {"company": "DOVAC B.V.", "name": "Ferry Jansen", "email": "info@dovac.nl"},

    # US East & Midwest
    {"company": "Kerr Pump & Supply", "name": "Rob Kalfs", "email": "rob@kerrpump.com"},
    {"company": "Atlantic Compressors, Inc.", "name": "Bill Rimer", "email": "bill@atlanticcompressors.com"},
    {"company": "Control Specialties, Inc.", "name": "Margie Moschetti", "email": "margie@control-specialties.com"},
    {"company": "Brehob Corporation", "name": "Bryan Smither", "email": "bsmither@brehob.com"},
    {"company": "Combined Fluid Products Company", "name": "Randall Kist", "email": "rkist@cfpco.com"},
    {"company": "WSI Machinery", "name": "Rob Howell", "email": "rhowell@wsimachinery.com"},

    # US South & West
    {"company": "Cascade Machinery & Electric, Inc.", "name": "Michael Spring", "email": "mspring@cascade-machinery.com"},
    {"company": "Advanced Air & Vacuum", "name": "Joseph Vanderbilt", "email": "joseph@aavsales.com"},
    {"company": "LACO Technologies", "name": "Paul Chamberlain", "email": "paulc@lacotech.com"},
    {"company": "Associated Compressor & Equipment LLC", "name": "Steve Strah", "email": "sstrah@associatedcompressor.com"},
    {"company": "Lans Company, Inc.", "name": "Stuart Silverman", "email": "ssilverman@lanscompany.com"},

    # Asia Pacific & Oceania
    {"company": "Pump Solutions Australasia", "name": "Mike Hurlbatt", "email": "mike@pumpsolutions.com.au"},
    {"company": "VABS Ltd (Vacuum & Blowing Solutions)", "name": "Brendan Walker", "email": "brendan.walker@vabs.co.nz"},
    {"company": "Air Vacuum Automation Vietnam Co., Ltd.", "name": "Roland Lim", "email": "roland@airvacuum.com.vn"},
    {"company": "Jupp & Company, Inc.", "name": "Joseph V. Ascutia", "email": "joseph.ascutia@jupp.com.ph"},
    {"company": "Yuan Machinery Industrial Co., Ltd.", "name": "Yeh Che-Chia", "email": "sales@ecovac.com.tw"},
    {"company": "ABS Engineering & Trading Sdn Bhd", "name": "Roger Ang Eng Beng", "email": "abs-mt@abset.com"},
    {"company": "Airvac System Technology Co., Ltd.", "name": "Pathompong Sukawatcharanon", "email": "pathompong.s@airvacsystemth.com"},
    {"company": "PT Intidaya Dinamika Sejati", "name": "Jonathan Kartawijaya", "email": "sales@intidayads.com"},
    {"company": "Azuma Technos Co., Ltd.", "name": "Hiroshi Seki", "email": "recruiter@azumatec.co.jp"},

    # LATAM, Middle East & Africa
    {"company": "Just Pumps (Pty) Ltd", "name": "Jaco Venter", "email": "jaco@justpumps.co.za"},
    {"company": "Corporación Erazo S.A.C.", "name": "Juan Erazo", "email": "erazo@corporacionerazo.com"},
    {"company": "VPC Ingeniería S.A.S.", "name": "Ricardo José Rodríguez Corsi", "email": "rrodriguez@vpcingenieria.co"},
    {"company": "FullVac", "name": "Lucas Javier Montañía", "email": "comercial@fullvac.com.ar"},
    {"company": "Ashtechs (Antoine Ashba & Co.)", "name": "Antoine Ashba", "email": "cairo@ashtechs.com"},
    {"company": "UES Teknik Makina Ltd.", "name": "Hakan Taştemür", "email": "info@uesteknik.com"},
    {"company": "Masader Multi Ltd. Co.", "name": "Executive Management", "email": "info@masadermulti.com"},
    {"company": "Dunamis Engineering Trading W.L.L.", "name": "Executive Management", "email": "info@dunamisetc.com"}
]

out_csv = "/Users/alt/Desktop/starr/favour/becker_new_distributors_3col.csv"

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in new_42_distributors:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully generated NEW 42 distributors 3-column CSV file: {out_csv}")
