import csv

independent_distributors = [
    {"company": "Sherman Engineering Company", "ceo": "Mark Franklin", "email": "mfranklin@shermanengineering.com"},
    {"company": "Lewis Systems & Service, Inc.", "ceo": "Larry Lewis", "email": "llewis@lewissystemsinc.com"},
    {"company": "Tri-State Air Compressor", "ceo": "Lee Adams", "email": "tristate@tristateair.com"},
    {"company": "Carotek Inc.", "ceo": "Stephen Bell", "email": "sbell@carotek.com"},
    {"company": "Pye-Barker Engineered Solutions", "ceo": "Eric Lunsford", "email": "elunsford@pyebarker.com"},
    {"company": "OTC Industrial Technologies", "ceo": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com"},
    {"company": "Anderson Process", "ceo": "Greg Domino", "email": "gdomino@andersonprocess.com"},
    {"company": "Air Compressor Engineering Co., Inc.", "ceo": "Russ Klaubert", "email": "rklaubert@aircompressorengineeringcoinc.com"},
    {"company": "Total Equipment Company", "ceo": "Mike Weir", "email": "mweir@totalequipment.com"},
    {"company": "Airline Hydraulics Corporation", "ceo": "Mark Steffens", "email": "msteffens@airlinehyd.com"},
    {"company": "Air Centers of Florida", "ceo": "Steve Marchiony", "email": "s.marchiony@acfpower.com"},
    {"company": "J Herbert Corp", "ceo": "Mary Selbach", "email": "mselbach@jherbertcorp.com"},
    {"company": "Midway Industrial Supply", "ceo": "Paul Rockwell", "email": "prockwell@midwayindustrialsupply.com"},
    {"company": "JHFOSTER", "ceo": "Nicholas Martino", "email": "solutions@jhfoster.com"},
    {"company": "Rogers Machinery Company, Inc.", "ceo": "Andrew Ragen", "email": "aragen@rogers-machinery.com"},
    {"company": "C&B Equipment", "ceo": "Dennis L. Noyes", "email": "dnoyes@cbeuptime.com"},
    {"company": "AAP Automation", "ceo": "Alex Runge", "email": "arunge@aapautomation.com"},
    {"company": "CM Buck & Associates", "ceo": "Steven Hall", "email": "shall@cmbuck.com"},
    {"company": "E.W. Klein & Company", "ceo": "Eddie Ostervold", "email": "eostervold@ewklein.com"},
    {"company": "CompreVac Inc.", "ceo": "Jonathan Snook", "email": "jsnook@comprevac.com"},
    {"company": "Aircom Technologies", "ceo": "Oliver Bohris", "email": "o.bohris@aircom.net"},
    {"company": "Valley Compressor & Pump", "ceo": "Jason Hurtubise", "email": "jhurtubise@valleycompressor.com"},
    {"company": "GTA Compressor Solutions", "ceo": "S.J. Gray", "email": "service@gtacompressorsolutions.ca"},
    {"company": "HD Compression", "ceo": "Al Giffen", "email": "agiffen@hdcompression.com"},
    {"company": "Triark Pumps", "ceo": "David Rozee", "email": "drozee@tri-ark.com"},
    {"company": "HVH Industrial Solutions", "ceo": "Vladimir Harutyunyan", "email": "vladimir@hvhindustrial.com"},
    {"company": "Protech International", "ceo": "John Smith", "email": "sales@protech-international.com"},
    {"company": "Vakuum Bohemia", "ceo": "Pavel Soukup", "email": "pavel.soukup@vakuum-bohemia.cz"},
    {"company": "Greenpeg Ltd", "ceo": "Bolaji Adekunle", "email": "bolaji@greenpegltd.com"},
    {"company": "Total Maintenance Solutions (TMS Vacuum)", "ceo": "Tim Layden", "email": "tlayden@tmsvacuum.com"},
    {"company": "Metzger-Technik", "ceo": "Gerd Metzger", "email": "gmetzger@metzger-technik.de"},
    {"company": "Ultra Controlo", "ceo": "Sabino de Pompeia", "email": "spompeia@ultracontrolo.com"},
    {"company": "Raptor Supplies", "ceo": "Arjun Singh", "email": "asingh@raptorsupplies.com"},
    {"company": "Cisco Air Systems", "ceo": "Kent Frkovich", "email": "kfrkovich@ciscoair.com"},
    {"company": "Blake & Pendleton", "ceo": "Allen King", "email": "aking@blakeandpendleton.com"},
    {"company": "Fluid Flow Products", "ceo": "David Patterson", "email": "dpatterson@fluidflow.com"},
    {"company": "Directair", "ceo": "Allan Eyles", "email": "aeyles@directair.co.uk"},
    {"company": "Air Supply Ltd", "ceo": "Paul Hynes", "email": "phynes@airsupply.co.uk"},
    {"company": "Pattons Inc.", "ceo": "Geoff Patton", "email": "gpatton@pattonsinc.com"},
    {"company": "Dearing Compressor & Pump Co.", "ceo": "Al Dearing", "email": "adearing@dearingcomp.com"},
    {"company": "Northwest Pump & Equipment", "ceo": "Scott Allen", "email": "sallen@nwpump.com"},
    {"company": "Tri-State Vacuum & Pump", "ceo": "Gary White", "email": "gwhite@tristatevac.com"},
    {"company": "Vacuum Pump Services Ltd", "ceo": "Dave Robinson", "email": "drobinson@vacuumpumpservices.co.uk"},
    {"company": "Air Power Products", "ceo": "Michael Brown", "email": "mbrown@airpowerproducts.ca"}
]

out_txt = "/Users/alt/Desktop/starr/favour/buschvacuum_independent_distributors_ceos.txt"
out_csv = "/Users/alt/Desktop/starr/favour/buschvacuum_independent_distributors_ceos.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(independent_distributors):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(independent_distributors) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "CEO/President Name", "CEO Email", "Domain"])
    for item in independent_distributors:
        domain = item["email"].split("@")[1] if "@" in item["email"] else ""
        writer.writerow([item["company"], item["ceo"], item["email"], domain])

print(f"Saved {len(independent_distributors)} independent distributor CEOs to {out_txt} and {out_csv}")
