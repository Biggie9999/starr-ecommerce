import csv

all_independent_becker = [
    # Initial Verified Batch
    {"company": "R.E. Morrison Equipment Inc.", "name": "Adam Ralph", "email": "a.ralph@remequip.com"},
    {"company": "HVH Industrial Solutions LLC", "name": "Vladimir Harutyunyan", "email": "vlad@hvhindustrial.com"},
    {"company": "Centennial Equipment", "name": "Jason Munzer", "email": "jmunzer@centennialequipment.com"},
    {"company": "CNC Parts Dept, Inc.", "name": "Roupen Merjanian", "email": "sales@cncpd.com"},
    {"company": "Smart Fluid and Vacuum Technologies", "name": "Executive Management Team", "email": "info@sfvtechnologies.com"},
    {"company": "Application Associates", "name": "Ed Murcia", "email": "info@applicationassociates.com"},
    {"company": "Pioneer Equipment", "name": "Scott Trammell", "email": "strammell@pioneerequip.com"},
    {"company": "Stateside Industrial Solutions", "name": "Dennis R. Hernandez", "email": "dhernandez@statesideindustrial.com"},
    {"company": "Powermatic Associates", "name": "Frank Nudo", "email": "fnudo@powermatic.net"},
    {"company": "YNNA spol. s r.o.", "name": "Ing. Štefan Nemčok", "email": "stefan.nemcok@ynna.cz"},
    {"company": "Metzger Technik GmbH", "name": "Gerd Metzger", "email": "gerd.metzger@metzger-technik.de"},
    {"company": "Directair", "name": "Allan Dolby", "email": "allan.dolby@directair.co.uk"},
    {"company": "Air Supply Ltd", "name": "George Jackson Wright", "email": "george.wright@airsupply.co.uk"},
    {"company": "Vacuum Pump Services Ltd", "name": "Peter Douglas Bowen", "email": "p.bowen@vacuumpumpservices.co.uk"},
    {"company": "Triark Pumps", "name": "David Rozée", "email": "david@tri-ark.com"},
    {"company": "Raptor Supplies", "name": "Arjun Singh", "email": "arjun@raptorsupplies.com"},
    {"company": "Ultra Controlo Projectos Industriais Lda", "name": "Sabino de Pompeia", "email": "sabino.pompeia@ultra-controlo.com"},
    {"company": "Vacuum Pumps NZ Ltd (VPNZ)", "name": "Lawrence David Walls", "email": "info@vpnz.co.nz"},
    {"company": "African Vacuum Tech Distribution (Pty) Ltd", "name": "Shaun David", "email": "shaun.david@africanvacuumpumps.com"},
    {"company": "Fluidtec Equipment Trading L.L.C.", "name": "Ehab Abu Shama", "email": "ceo@fluidtec.ae"},
    {"company": "Mechatronics Industrial Equipment", "name": "Stanley C. J. Daniel", "email": "mechtron@mechatronics.ae"},
    {"company": "Vacuum Tech Máquinas e Equipamentos Ltda. (Robmaq)", "name": "Rafael Robmaq", "email": "rafael@robmaq.com.br"},
    {"company": "W&F Ingeniería y Máquinas S.A.", "name": "Roberto Wendler Apel", "email": "rwendler@wyf.cl"},
    {"company": "CompVac - Sistemas de Aire Comprimido y Vacío", "name": "Guillermo Quintin", "email": "guillermo.quintin@compvac.com.ar"},

    # Swarm Discovered Batch - Europe
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

    # Swarm Discovered Batch - US East & Midwest
    {"company": "Kerr Pump & Supply", "name": "Rob Kalfs", "email": "rob@kerrpump.com"},
    {"company": "Atlantic Compressors, Inc.", "name": "Bill Rimer", "email": "bill@atlanticcompressors.com"},
    {"company": "Control Specialties, Inc.", "name": "Margie Moschetti", "email": "margie@control-specialties.com"},
    {"company": "Brehob Corporation", "name": "Bryan Smither", "email": "bsmither@brehob.com"},
    {"company": "Combined Fluid Products Company", "name": "Randall Kist", "email": "rkist@cfpco.com"},
    {"company": "WSI Machinery", "name": "Rob Howell", "email": "rhowell@wsimachinery.com"},

    # Swarm Discovered Batch - US South & West
    {"company": "Cascade Machinery & Electric, Inc.", "name": "Michael Spring", "email": "mspring@cascade-machinery.com"},
    {"company": "Advanced Air & Vacuum", "name": "Joseph Vanderbilt", "email": "joseph@aavsales.com"},
    {"company": "LACO Technologies", "name": "Paul Chamberlain", "email": "paulc@lacotech.com"},
    {"company": "Associated Compressor & Equipment LLC", "name": "Steve Strah", "email": "sstrah@associatedcompressor.com"},
    {"company": "Lans Company, Inc.", "name": "Stuart Silverman", "email": "ssilverman@lanscompany.com"},

    # Swarm Discovered Batch - Asia Pacific & Oceania
    {"company": "Pump Solutions Australasia", "name": "Mike Hurlbatt", "email": "mike@pumpsolutions.com.au"},
    {"company": "VABS Ltd (Vacuum & Blowing Solutions)", "name": "Brendan Walker", "email": "brendan.walker@vabs.co.nz"},
    {"company": "Air Vacuum Automation Vietnam Co., Ltd.", "name": "Roland Lim", "email": "roland@airvacuum.com.vn"},
    {"company": "Jupp & Company, Inc.", "name": "Joseph V. Ascutia", "email": "joseph.ascutia@jupp.com.ph"},
    {"company": "Yuan Machinery Industrial Co., Ltd.", "name": "Yeh Che-Chia", "email": "sales@ecovac.com.tw"},
    {"company": "ABS Engineering & Trading Sdn Bhd", "name": "Roger Ang Eng Beng", "email": "abs-mt@abset.com"},
    {"company": "Airvac System Technology Co., Ltd.", "name": "Pathompong Sukawatcharanon", "email": "pathompong.s@airvacsystemth.com"},
    {"company": "PT Intidaya Dinamika Sejati", "name": "Jonathan Kartawijaya", "email": "sales@intidayads.com"},
    {"company": "Azuma Technos Co., Ltd.", "name": "Hiroshi Seki", "email": "recruiter@azumatec.co.jp"},

    # Swarm Discovered Batch - LATAM, Middle East & Africa
    {"company": "Just Pumps (Pty) Ltd", "name": "Jaco Venter", "email": "jaco@justpumps.co.za"},
    {"company": "Corporación Erazo S.A.C.", "name": "Juan Erazo", "email": "erazo@corporacionerazo.com"},
    {"company": "VPC Ingeniería S.A.S.", "name": "Ricardo José Rodríguez Corsi", "email": "rrodriguez@vpcingenieria.co"},
    {"company": "FullVac", "name": "Lucas Javier Montañía", "email": "comercial@fullvac.com.ar"},
    {"company": "Ashtechs (Antoine Ashba & Co.)", "name": "Antoine Ashba", "email": "cairo@ashtechs.com"},
    {"company": "UES Teknik Makina Ltd.", "name": "Hakan Taştemür", "email": "info@uesteknik.com"},
    {"company": "Masader Multi Ltd. Co.", "name": "Executive Management", "email": "info@masadermulti.com"},
    {"company": "Dunamis Engineering Trading W.L.L.", "name": "Executive Management", "email": "info@dunamisetc.com"}
]

out_csv = "/Users/alt/Desktop/starr/favour/becker_distributors_3col.csv"

# Remove duplicates based on company domain/email
seen_emails = set()
unique_entries = []

for item in all_independent_becker:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        seen_emails.add(em)
        unique_entries.append(item)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in unique_entries:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully compiled {len(unique_entries)} unique independent Becker distributors to {out_csv}")
