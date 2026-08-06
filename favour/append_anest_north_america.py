import csv

na_entities = [
    {"company": "Air Power, Inc.", "name": "Dan Senff", "email": "dsenff@airpower-usa.com"},
    {"company": "OTC Industrial Technologies", "name": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com"},
    {"company": "PTB Sales, Inc.", "name": "Pat Blackwell", "email": "pat.blackwell@ptbsales.com"},
    {"company": "Spokane Hardware Supply, Inc.", "name": "Andrew Northrop", "email": "andrew@spokanehardware.com"},
    {"company": "Advanced Coatings Technologies", "name": "Kenneth N. Withell", "email": "kwithell@actcoatings.ca"},
    {"company": "MC Supply & Service Co.", "name": "Joe Monaldi", "email": "joe@mcsupply.org"},
    {"company": "Compressor World LLC", "name": "Matt Mazanec", "email": "matt@compressorworld.com"},
    {"company": "Associated Compressor & Equipment LLC", "name": "Jeff Banbury", "email": "jbanbury@associatedcompressor.com"},
    {"company": "Q Air-California", "name": "Jimmy L. Hamilton", "email": "jimh@qair.net"},
    {"company": "Rogers Machinery Company, Inc.", "name": "Chris McKillop", "email": "chris.mckillop@rogers-machinery.com"},
    {"company": "C.H. Reed, Inc.", "name": "Bob Shields", "email": "bshields@chreed.com"},
    {"company": "Elevated Industrial Solutions", "name": "Romy O'Daniel", "email": "rodaniel@elevatedindustrial.com"},
    {"company": "CASCO USA", "name": "Jim Miller", "email": "jmiller@cascousa.com"},
    {"company": "Air Centers of Florida", "name": "John Hemken", "email": "j.hemken@acfpower.com"},
    {"company": "Fluid-Aire Dynamics", "name": "Derrick Taylor", "email": "derrick.taylor@fluidairedynamics.com"},
    {"company": "KG Power Systems", "name": "Chris Gandolfo", "email": "cgandolfo@kgpowersystems.com"},
    {"company": "Maple Airbrush Supplies", "name": "Donna Busch", "email": "info@mapleairbrushsupplies.com"},
    {"company": "Coast Airbrush", "name": "David Monnig", "email": "kustom@coastairbrush.com"},
    {"company": "Atlanta Compressor / Hodge Industrial", "name": "Morty Hodge", "email": "info@hodgeindustrial.com"},
    {"company": "Selectum LLC", "name": "Customer Leadership Team", "email": "info@selectumllc.com"}
]

out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

# Load existing entries
existing = []
seen_emails = set()

with open(out_csv, "r") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if row:
            existing.append({"company": row[0], "name": row[1], "email": row[2]})
            seen_emails.add(row[2].lower().strip())

for item in na_entities:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        seen_emails.add(em)
        existing.append(item)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in existing:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully expanded Anest Iwata CSV to {len(existing)} entries in {out_csv}")
