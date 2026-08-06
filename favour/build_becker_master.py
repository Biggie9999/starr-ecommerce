import csv

master_list = [
    {"company": "Gebr. Becker GmbH Global Headquarters", "ceo": "Dr. Dorothee Becker", "email": "info@becker-international.com", "domain": "becker-international.com", "role": "Global CEO"},
    {"company": "Becker Pumps Corporation USA Headquarters", "ceo": "Jason Rathbun", "email": "jrathbun@beckerpumps.com", "domain": "beckerpumps.com", "role": "Managing Director / President Americas"},
    {"company": "Becker Vacuum Pumps Canada Inc.", "ceo": "Canadian Sales Management", "email": "info@becker-canada.com", "domain": "becker-canada.com", "role": "Regional Subsidiary"},
    {"company": "Becker Mexico S. de R.L. de C.V.", "ceo": "LATAM Sales Management", "email": "info@becker-mexico.mx", "domain": "becker-mexico.mx", "role": "Regional Subsidiary"},
    {"company": "Becker UK Ltd", "ceo": "Tim Martin", "email": "tim.martin@becker.co.uk", "domain": "becker.co.uk", "role": "Managing Director"},
    {"company": "Becker France S.A.R.L.", "ceo": "Frank Becker", "email": "info@becker-france.fr", "domain": "becker-france.fr", "role": "Managing Director"},
    {"company": "Becker Italia S.r.l.", "ceo": "Italian Sales Management", "email": "info@becker-italia.it", "domain": "becker-italia.it", "role": "Regional Subsidiary"},
    {"company": "Becker Ibérica de Bombas de Vacío S.L.", "ceo": "Iberian Sales Management", "email": "info@becker-iberica.com", "domain": "becker-iberica.com", "role": "Regional Subsidiary"},
    {"company": "Becker Druk- en Vacuümpompen B.V.", "ceo": "Dutch Sales Management", "email": "info@becker-nederland.nl", "domain": "becker-nederland.nl", "role": "Regional Subsidiary"},
    {"company": "Becker AG Switzerland", "ceo": "Swiss Sales Management", "email": "info@becker-ag.ch", "domain": "becker-ag.ch", "role": "Regional Subsidiary"},
    {"company": "Gebr. Becker India Vacuum Pumps Pvt. Ltd.", "ceo": "Indian Sales Management", "email": "info@becker-india.com", "domain": "becker-india.com", "role": "Regional Subsidiary"},
    {"company": "Becker Asia Pacific Pte. Ltd.", "ceo": "Asia Pacific Management", "email": "info@becker-asiapacific.com", "domain": "becker-asiapacific.com", "role": "Regional Subsidiary"},
    {"company": "Pioneer Equipment", "ceo": "Scott Trammell", "email": "strammell@pioneerequip.com", "domain": "pioneerequip.com", "role": "President & Owner"},
    {"company": "HVH Industrial Solutions", "ceo": "Vladimir Harutyunyan", "email": "vlad@hvhindustrial.com", "domain": "hvhindustrial.com", "role": "Founder & CEO"},
    {"company": "CNC Parts Dept, Inc.", "ceo": "Lynn Kramer", "email": "lkramer@cncpd.com", "domain": "cncpd.com", "role": "Owner & Founder"},
    {"company": "Sherman Engineering Company", "ceo": "Mark Franklin", "email": "mfranklin@shermanengineering.com", "domain": "shermanengineering.com", "role": "President"},
    {"company": "Lewis Systems & Service, Inc.", "ceo": "Larry Lewis", "email": "llewis@lewissystemsinc.com", "domain": "lewissystemsinc.com", "role": "President"},
    {"company": "Tri-State Air Compressor", "ceo": "Lee Adams", "email": "ladams@tristateair.com", "domain": "tristateair.com", "role": "President"},
    {"company": "Carotek Inc.", "ceo": "Dave Webster", "email": "dwebster@carotek.com", "domain": "carotek.com", "role": "President"},
    {"company": "Pye-Barker Engineered Solutions", "ceo": "Eric Lunsford", "email": "Eric@pyebarker.com", "domain": "pyebarker.com", "role": "President & CEO"},
    {"company": "OTC Industrial Technologies", "ceo": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com", "domain": "otcindustrial.com", "role": "CEO"},
    {"company": "Anderson Process", "ceo": "Greg Domino", "email": "gdomino@andersonprocess.com", "domain": "andersonprocess.com", "role": "CEO & Owner"},
    {"company": "Air Compressor Engineering Co., Inc.", "ceo": "Russ Klaubert", "email": "rklaubert@aircompressoreng.com", "domain": "aircompressoreng.com", "role": "President"},
    {"company": "Total Equipment Company", "ceo": "Eric Solverson", "email": "eric.solverson@totalequipment.com", "domain": "totalequipment.com", "role": "General Manager"},
    {"company": "Airline Hydraulics Corporation", "ceo": "Mark Steffens", "email": "msteffens@airlinehyd.com", "domain": "airlinehyd.com", "role": "CEO"},
    {"company": "Air Centers of Florida", "ceo": "Andrew J. Young", "email": "a.young@acfpower.com", "domain": "acfpower.com", "role": "President & CEO"},
    {"company": "J Herbert Corp", "ceo": "Mary Selbach", "email": "mselbach@jherbertcorp.com", "domain": "jherbertcorp.com", "role": "President"},
    {"company": "Midway Industrial Supply", "ceo": "Paul Rockwell", "email": "prockwell@midwaycorp.com", "domain": "midwayindustrialsupply.com", "role": "President"},
    {"company": "JHFOSTER", "ceo": "Nicholas W. Martino", "email": "nicholas.martino@jhfoster.com", "domain": "jhfoster.com", "role": "CEO & President"},
    {"company": "Rogers Machinery Company, Inc.", "ceo": "Chris McKillop", "email": "chris.mckillop@rogers-machinery.com", "domain": "rogers-machinery.com", "role": "President"},
    {"company": "C&B Equipment", "ceo": "Ben Brocker", "email": "bbrocker@cbeuptime.com", "domain": "cbeuptime.com", "role": "President & Owner"},
    {"company": "AAP Automation", "ceo": "Wes Brown", "email": "wbrown@aapautomation.com", "domain": "aapautomation.com", "role": "Vice President"},
    {"company": "CM Buck & Associates", "ceo": "Steven Hall", "email": "shall@cmbuck.com", "domain": "cmbuck.com", "role": "President & CEO"},
    {"company": "E.W. Klein & Company", "ceo": "Eddie Ostervold", "email": "eddieo@ewklein.com", "domain": "ewklein.com", "role": "President"},
    {"company": "CompreVac Inc.", "ceo": "Jonathan Snook", "email": "jonathan@comprevac.com", "domain": "comprevac.com", "role": "President & GM"},
    {"company": "Aircom Technologies", "ceo": "Oliver Bohris", "email": "o.bohris@aircom.net", "domain": "aircom.net", "role": "Managing Director"},
    {"company": "Valley Compressor & Pump", "ceo": "Jason Hurtubise", "email": "jhurtubise@valleycompressor.com", "domain": "valleycompressor.com", "role": "General Manager"},
    {"company": "GTA Compressor Solutions", "ceo": "Steve Gray", "email": "steve@gtacompressorsolutions.ca", "domain": "gtacompressorsolutions.ca", "role": "Owner & President"},
    {"company": "HD Compression", "ceo": "Al Giffen", "email": "agiffen@hdcompression.com", "domain": "hdcompression.com", "role": "President"},
    {"company": "Triark Pumps", "ceo": "David Rozée", "email": "david@tri-ark.com", "domain": "tri-ark.com", "role": "Managing Director"},
    {"company": "Protech International", "ceo": "Joseph Todd", "email": "joseph.todd@protech-international.com", "domain": "protech-international.com", "role": "Executive Director"},
    {"company": "Vakuum Bohemia", "ceo": "Ing. Vít Němec", "email": "vit.nemec@vakuum-bohemia.cz", "domain": "vakuum-bohemia.cz", "role": "Managing Director"},
    {"company": "Greenpeg Ltd", "ceo": "Bolaji Adekunle", "email": "bolaji.adekunle@greenpeg.com", "domain": "greenpegltd.com", "role": "CEO & MD"},
    {"company": "Total Maintenance Solutions", "ceo": "Jeff Schmidt", "email": "jeff.schmidt@tmsvacuum.com", "domain": "tmsvacuum.com", "role": "General Manager"},
    {"company": "Metzger-Technik", "ceo": "Gerd Metzger", "email": "gerd.metzger@metzger-technik.de", "domain": "metzger-technik.de", "role": "Managing Director"},
    {"company": "Ultra Controlo", "ceo": "Sabino de Pompeia", "email": "sabino.pompeia@ultra-controlo.com", "domain": "ultracontrolo.com", "role": "CEO & Founder"},
    {"company": "Raptor Supplies", "ceo": "Arjun Singh", "email": "arjun@raptorsupplies.com", "domain": "raptorsupplies.com", "role": "Founder & CEO"},
    {"company": "Cisco Air Systems", "ceo": "Kent Frkovich", "email": "kent.frkovich@ciscoair.com", "domain": "ciscoair.com", "role": "President & CEO"},
    {"company": "Blake & Pendleton", "ceo": "Allen King", "email": "aking@blakeandpendleton.com", "domain": "blakeandpendleton.com", "role": "President & CEO"},
    {"company": "Fluid Flow Products", "ceo": "Pete Gherardi", "email": "petegherardi@fluidflow.com", "domain": "fluidflow.com", "role": "President"},
    {"company": "Directair", "ceo": "Allan Dolby", "email": "allan.dolby@directair.co.uk", "domain": "directair.co.uk", "role": "Managing Director"},
    {"company": "Air Supply Ltd", "ceo": "George Jackson Wright", "email": "george.wright@airsupply.co.uk", "domain": "airsupply.co.uk", "role": "Managing Director"},
    {"company": "Pattons Inc.", "ceo": "Scott Sutton", "email": "scott.sutton@pattonsinc.com", "domain": "pattonsinc.com", "role": "Vice President & GM"},
    {"company": "Dearing Compressor & Pump Co.", "ceo": "Rebecca Dearing Wall", "email": "bwall@dearingcomp.com", "domain": "dearingcomp.com", "role": "CEO"},
    {"company": "Northwest Pump & Equipment", "ceo": "Bob Mathews", "email": "bob.mathews@nwpump.com", "domain": "nwpump.com", "role": "President & CEO"},
    {"company": "Tri-State Vacuum & Pump", "ceo": "Troy Massey", "email": "troy.massey@tristateoilfield.com", "domain": "tristatevac.com", "role": "President & CEO"},
    {"company": "Vacuum Pump Services Ltd", "ceo": "Peter Douglas Bowen", "email": "p.bowen@vacuumpumpservices.co.uk", "domain": "vacuumpumpservices.co.uk", "role": "Managing Director"},
    {"company": "Air Power Products", "ceo": "Abbas Khan", "email": "akhan@airpowerproducts.com", "domain": "airpowerproducts.ca", "role": "President & CEO"},
    {"company": "Application Associates", "ceo": "Jim McEvoy", "email": "jmcevoy@applicationassociates.com", "domain": "applicationassociates.com", "role": "President"}
]

out_txt = "/Users/alt/Desktop/starr/favour/beckerpumps_procurement_master.txt"
out_csv = "/Users/alt/Desktop/starr/favour/beckerpumps_procurement_master.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(master_list):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(master_list) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company / Entity", "CEO / President Name", "Executive Email", "Domain", "Title / Role"])
    for item in master_list:
        writer.writerow([item["company"], item["ceo"], item["email"], item["domain"], item["role"]])

print(f"Master procurement files generated with {len(master_list)} entries.")
