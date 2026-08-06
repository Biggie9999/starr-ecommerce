import csv

becker_list = [
    {"company": "Pioneer Equipment", "ceo": "Steve Pioneer", "email": "sales@pioneerequip.com", "domain": "pioneerequip.com"},
    {"company": "HVH Industrial Solutions", "ceo": "Vladimir Harutyunyan", "email": "vladimir@hvhindustrial.com", "domain": "hvhindustrial.com"},
    {"company": "CNC Parts Dept, Inc.", "ceo": "Kevin O'Connor", "email": "sales@cncpd.com", "domain": "cncpd.com"},
    {"company": "Sherman Engineering Company", "ceo": "Mark Franklin", "email": "mfranklin@shermanengineering.com", "domain": "shermanengineering.com"},
    {"company": "Lewis Systems & Service, Inc.", "ceo": "Larry Lewis", "email": "llewis@lewissystemsinc.com", "domain": "lewissystemsinc.com"},
    {"company": "Tri-State Air Compressor", "ceo": "Lee Adams", "email": "tristate@tristateair.com", "domain": "tristateair.com"},
    {"company": "Carotek Inc.", "ceo": "Dave Webster", "email": "dave.webster@carotek.com", "domain": "carotek.com"},
    {"company": "Pye-Barker Engineered Solutions", "ceo": "Eric Lunsford", "email": "Eric@PyeBarker.com", "domain": "pyebarker.com"},
    {"company": "OTC Industrial Technologies", "ceo": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com", "domain": "otcindustrial.com"},
    {"company": "Anderson Process", "ceo": "Greg Domino", "email": "gdomino@andersonprocess.com", "domain": "andersonprocess.com"},
    {"company": "Air Compressor Engineering Co., Inc.", "ceo": "Russ Klaubert", "email": "rklaubert@aircompressoreng.com", "domain": "aircompressoreng.com"},
    {"company": "Total Equipment Company", "ceo": "Mike Weir", "email": "mweir@totalequipment.com", "domain": "totalequipment.com"},
    {"company": "Airline Hydraulics Corporation", "ceo": "Mark Steffens", "email": "msteffens@airlinehyd.com", "domain": "airlinehyd.com"},
    {"company": "Air Centers of Florida", "ceo": "Andrew J. Young", "email": "andrew.young@acfpower.com", "domain": "acfpower.com"},
    {"company": "J Herbert Corp", "ceo": "Mary Selbach", "email": "m.selbach@jherbertcorp.com", "domain": "jherbertcorp.com"},
    {"company": "Midway Industrial Supply", "ceo": "Paul Rockwell", "email": "prockwell@midwaycorp.com", "domain": "midwayindustrialsupply.com"},
    {"company": "JHFOSTER", "ceo": "Nicholas W. Martino", "email": "nicholas.martino@jhfoster.com", "domain": "jhfoster.com"},
    {"company": "Rogers Machinery Company, Inc.", "ceo": "Andrew Ragen", "email": "andrew.ragen@rogers-machinery.com", "domain": "rogers-machinery.com"},
    {"company": "C&B Equipment", "ceo": "Ben Brocker", "email": "bbrocker@cbeuptime.com", "domain": "cbeuptime.com"},
    {"company": "AAP Automation", "ceo": "Wes Brown", "email": "info@aapautomation.com", "domain": "aapautomation.com"},
    {"company": "CM Buck & Associates", "ceo": "Steven Hall", "email": "shall@cmbuck.com", "domain": "cmbuck.com"},
    {"company": "E.W. Klein & Company", "ceo": "Eddie Ostervold", "email": "eddieo@ewklein.com", "domain": "ewklein.com"},
    {"company": "CompreVac Inc.", "ceo": "Jonathan Snook", "email": "jonathan@comprevac.com", "domain": "comprevac.com"},
    {"company": "Aircom Technologies", "ceo": "Oliver Bohris", "email": "o.bohris@aircom.net", "domain": "aircom.net"},
    {"company": "Valley Compressor & Pump", "ceo": "Executive Management", "email": "service@valleycompressor.com", "domain": "valleycompressor.com"},
    {"company": "GTA Compressor Solutions", "ceo": "Steve Gray", "email": "steve@gtacompressorsolutions.ca", "domain": "gtacompressorsolutions.ca"},
    {"company": "HD Compression", "ceo": "Al Giffen", "email": "info@hdcompression.com", "domain": "hdcompression.com"},
    {"company": "Triark Pumps", "ceo": "David Rozee", "email": "david@tri-ark.com", "domain": "tri-ark.com"},
    {"company": "Protech International", "ceo": "Joseph Todd", "email": "joseph.todd@protech-international.com", "domain": "protech-international.com"},
    {"company": "Vakuum Bohemia", "ceo": "Ing. Vít Němec", "email": "vit.nemec@vakuum-bohemia.cz", "domain": "vakuum-bohemia.cz"},
    {"company": "Greenpeg Ltd", "ceo": "Bolaji Adekunle", "email": "bolaji.adekunle@greenpeg.com", "domain": "greenpegltd.com"},
    {"company": "Total Maintenance Solutions", "ceo": "Jeff Schmidt", "email": "jeff.schmidt@tmsvacuum.com", "domain": "tmsvacuum.com"},
    {"company": "Metzger-Technik", "ceo": "Gerd Metzger", "email": "g.metzger@metzger-technik.de", "domain": "metzger-technik.de"},
    {"company": "Ultra Controlo", "ceo": "Sabino de Pompéia", "email": "s.pompeia@ultra-controlo.com", "domain": "ultracontrolo.com"},
    {"company": "Raptor Supplies", "ceo": "Arjun Singh", "email": "arjun@raptorsupplies.com", "domain": "raptorsupplies.com"},
    {"company": "Cisco Air Systems", "ceo": "Kent Frkovich", "email": "kent.frkovich@ciscoair.com", "domain": "ciscoair.com"},
    {"company": "Blake & Pendleton", "ceo": "Allen King", "email": "allen.king@blakeandpendleton.com", "domain": "blakeandpendleton.com"},
    {"company": "Fluid Flow Products", "ceo": "David Patterson", "email": "davidpatterson@fluidflow.com", "domain": "fluidflow.com"},
    {"company": "Directair", "ceo": "Allan Dolby", "email": "allan.dolby@directair.co.uk", "domain": "directair.co.uk"},
    {"company": "Air Supply Ltd", "ceo": "George Jackson Wright", "email": "george.wright@airsupply.co.uk", "domain": "airsupply.co.uk"},
    {"company": "Pattons Inc.", "ceo": "Scott Sutton", "email": "scott.sutton@pattonsinc.com", "domain": "pattonsinc.com"},
    {"company": "Dearing Compressor & Pump Co.", "ceo": "Rebecca Dearing Wall", "email": "rwall@dearingcomp.com", "domain": "dearingcomp.com"},
    {"company": "Northwest Pump & Equipment", "ceo": "Bob Mathews", "email": "bob.mathews@nwpump.com", "domain": "nwpump.com"},
    {"company": "Tri-State Vacuum & Pump", "ceo": "Troy Massey", "email": "troy.massey@tristateoilfield.com", "domain": "tristatevac.com"},
    {"company": "Vacuum Pump Services Ltd", "ceo": "Peter Douglas Bowen", "email": "peter.bowen@vacpumpservices.co.uk", "domain": "vacuumpumpservices.co.uk"},
    {"company": "Air Power Products", "ceo": "Abbas Khan", "email": "akhan@airpowerproducts.com", "domain": "airpowerproducts.ca"},
    {"company": "Becker Pumps Corp USA Headquarters", "ceo": "Darren S. VanScyoc", "email": "info@beckerpumps.com", "domain": "beckerpumps.com"},
    {"company": "Becker Canada", "ceo": "Sales Department", "email": "info@becker-canada.com", "domain": "becker-canada.com"},
    {"company": "Becker UK Ltd", "ceo": "Sales Department", "email": "sales@becker.co.uk", "domain": "becker.co.uk"},
    {"company": "Becker Mexico", "ceo": "Sales Department", "email": "info@becker-mexico.mx", "domain": "becker-mexico.mx"}
]

out_txt = "/Users/alt/Desktop/starr/favour/beckerpumps_procurement.txt"
out_csv = "/Users/alt/Desktop/starr/favour/beckerpumps_dealers.csv"
out_ceos_txt = "/Users/alt/Desktop/starr/favour/beckerpumps_independent_distributors_ceos.txt"
out_ceos_csv = "/Users/alt/Desktop/starr/favour/beckerpumps_independent_distributors_ceos.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(becker_list):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(becker_list) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "CEO/President Name", "Email", "Domain"])
    for item in becker_list:
        writer.writerow([item["company"], item["ceo"], item["email"], item["domain"]])

indep_list = [x for x in becker_list if "becker" not in x["company"].lower() or "corp" not in x["company"].lower()]

with open(out_ceos_txt, "w") as f:
    for i, item in enumerate(indep_list):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(indep_list) - 1:
            f.write("\n")

with open(out_ceos_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "CEO/President Name", "Email", "Domain"])
    for item in indep_list:
        writer.writerow([item["company"], item["ceo"], item["email"], item["domain"]])

print(f"Generated {len(becker_list)} Becker Pumps procurement entries.")
