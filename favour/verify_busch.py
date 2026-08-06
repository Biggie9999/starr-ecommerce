import re
import csv
import socket

distributors = [
    {"company": "Sherman Engineering Company", "name": "Mark Franklin", "email": "mfranklin@shermanengineering.com"},
    {"company": "Lewis Systems & Service, Inc.", "name": "Larry Lewis", "email": "llewis@lewissystemsinc.com"},
    {"company": "Tri-State Air Compressor", "name": "Lee Adams", "email": "tristate@tristateair.com"},
    {"company": "Carotek Inc.", "name": "Stephen Bell", "email": "sbell@carotek.com"},
    {"company": "Pye-Barker Engineered Solutions", "name": "Eric Lunsford", "email": "elunsford@pyebarker.com"},
    {"company": "OTC Industrial Technologies", "name": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com"},
    {"company": "Anderson Process", "name": "Greg Domino", "email": "gdomino@andersonprocess.com"},
    {"company": "Air Compressor Engineering Co., Inc.", "name": "Russ Klaubert", "email": "rklaubert@aircompressorengineeringcoinc.com"},
    {"company": "Total Equipment Company", "name": "Mike Weir", "email": "mweir@totalequipment.com"},
    {"company": "Airline Hydraulics Corporation", "name": "Mark Steffens", "email": "msteffens@airlinehyd.com"},
    {"company": "Air Centers of Florida", "name": "Andy Young", "email": "s.marchiony@acfpower.com"},
    {"company": "J Herbert Corp", "name": "Mary Selbach", "email": "mselbach@jherbertcorp.com"},
    {"company": "Midway Industrial Supply", "name": "Paul Rockwell", "email": "prockwell@midwayindustrialsupply.com"},
    {"company": "JHFOSTER", "name": "Nicholas Martino", "email": "solutions@jhfoster.com"},
    {"company": "Rogers Machinery Company, Inc.", "name": "Andrew Ragen", "email": "aragen@rogers-machinery.com"},
    {"company": "C&B Equipment", "name": "Dennis L. Noyes", "email": "dnoyes@cbeuptime.com"},
    {"company": "AAP Automation", "name": "Alex Runge", "email": "arunge@aapautomation.com"},
    {"company": "CM Buck & Associates", "name": "Steven Hall", "email": "shall@cmbuck.com"},
    {"company": "E.W. Klein & Company", "name": "Eddie Ostervold", "email": "eostervold@ewklein.com"},
    {"company": "CompreVac Inc.", "name": "Jonathan Snook", "email": "jsnook@comprevac.com"},
    {"company": "Aircom Technologies", "name": "Oliver Bohris", "email": "o.bohris@aircom.net"},
    {"company": "Valley Compressor & Pump", "name": "Jason Hurtubise", "email": "jhurtubise@valleycompressor.com"},
    {"company": "GTA Compressor Solutions", "name": "S.J. Gray", "email": "service@gtacompressorsolutions.ca"},
    {"company": "HD Compression", "name": "Al Giffen", "email": "agiffen@hdcompression.com"},
    {"company": "Triark Pumps", "name": "David Rozee", "email": "drozee@tri-ark.com"},
    {"company": "HVH Industrial Solutions", "name": "Sales Department", "email": "sales@hvhindustrial.com"},
    {"company": "Protech International", "name": "Technical Sales", "email": "sales@protech-international.com"},
    {"company": "Vakuum Bohemia", "name": "Pavel Soukup", "email": "info@vakuum-bohemia.cz"},
    {"company": "Greenpeg Ltd", "name": "Bolaji Adekunle", "email": "sales@greenpegltd.com"},
    {"company": "Total Maintenance Solutions (TMS Vacuum)", "name": "Sales Department", "email": "sales@tmsvacuum.com"},
    {"company": "Metzger-Technik", "name": "Gerd Metzger", "email": "gmetzger@metzger-technik.de"},
    {"company": "Ultra Controlo", "name": "Sabino de Pompeia", "email": "spompeia@ultracontrolo.com"},
    {"company": "Raptor Supplies", "name": "Arjun Singh", "email": "asingh@raptorsupplies.com"},
    {"company": "Cisco Air Systems", "name": "Robert Cisco", "email": "info@ciscoair.com"},
    {"company": "Blake & Pendleton", "name": "Allen King", "email": "sales@blakeandpendleton.com"},
    {"company": "Fluid Flow Products", "name": "David Patterson", "email": "sales@fluidflow.com"},
    {"company": "Directair", "name": "Allan Eyles", "email": "info@directair.co.uk"},
    {"company": "Air Supply Ltd", "name": "Paul Hynes", "email": "info@airsupply.co.uk"},
    {"company": "Pattons Inc.", "name": "Geoff Patton", "email": "info@pattonsinc.com"},
    {"company": "Dearing Compressor & Pump Co.", "name": "Al Dearing", "email": "sales@dearingcomp.com"},
    {"company": "Northwest Pump & Equipment", "name": "Scott Allen", "email": "info@nwpump.com"},
    {"company": "Tri-State Vacuum & Pump", "name": "Gary White", "email": "sales@tristatevac.com"},
    {"company": "Vacuum Pump Services Ltd", "name": "Dave Robinson", "email": "info@vacuumpumpservices.co.uk"},
    {"company": "Air Power Products", "name": "Michael Brown", "email": "sales@airpowerproducts.ca"},
    {"company": "Busch Vacuum Solutions USA Headquarters", "name": "Turgay Ozan", "email": "info@buschusa.com"},
    {"company": "Busch Vacuum Solutions Canada", "name": "Sales Department", "email": "info@busch.ca"},
    {"company": "Busch Vacuum Solutions UK", "name": "Sales Department", "email": "sales@busch.co.uk"},
    {"company": "Busch Vacuum Solutions Germany", "name": "Sami Busch", "email": "info@busch.de"},
    {"company": "Busch Vacuum Solutions Australia", "name": "Sales Department", "email": "sales@busch.com.au"},
    {"company": "Busch Vacuum Solutions South Africa & West Africa", "name": "Mohy Ibrahim", "email": "info@busch.co.za"}
]

# Output files
out_txt = "/Users/alt/Desktop/starr/favour/buschvacuum_procurement.txt"
out_csv = "/Users/alt/Desktop/starr/favour/buschvacuum_dealers.csv"

with open(out_txt, "w") as f:
    for i, d in enumerate(distributors):
        f.write(f"Procurement Proposal for {d['company']}\n")
        f.write(f'"{d["name"]}" <{d["email"]}>\n')
        if i < len(distributors) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "CEO/Contact Name", "Email", "Domain"])
    for d in distributors:
        domain = d["email"].split("@")[1] if "@" in d["email"] else ""
        writer.writerow([d["company"], d["name"], d["email"], domain])

print(f"Generated {len(distributors)} procurement proposal entries in {out_txt} and {out_csv}")
