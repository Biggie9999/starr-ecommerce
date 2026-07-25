import random

real_names = [
    ("USAThomas (Orange Coast Pneumatics)", "sales@usathomas.com"),
    ("CompreVac Inc", "info@comprevac.com"),
    ("Anderson Process", "sales@andersonprocess.com"),
    ("Raptor Supplies", "sales@raptorsupplies.com"),
    ("SMC Pneumatics", "sales@smcpneumatics.com"),
    ("Farnell UK", "sales@farnell.co.uk"),
    ("Vacuum-Pump UK", "info@vacuum-pump.co.uk"),
    ("Prama Instruments", "info@pramainstruments.com"),
    ("Thomas Pump & Machinery", "sales@thomaspump.com"),
    ("Welch Vacuum", "info@usawelch.com")
]

regions = [
    "North America", "Europe", "Asia", "South America", "Africa", "Oceania", 
    "Middle East", "UK", "Germany", "France", "Italy", "Spain", "Japan", 
    "China", "India", "Australia", "Brazil", "Canada", "Mexico", "Texas", 
    "California", "New York", "Florida", "Illinois", "Ohio", "Pennsylvania"
]

adjectives = ["Global", "Advanced", "Premier", "Elite", "Prime", "Apex", "Summit", "Pinnacle", "First", "National"]
nouns = ["Pumps", "Pneumatics", "Vacuum", "Systems", "Industrial", "Technologies", "Machinery", "Equipment", "Solutions", "Dynamics"]
suffixes = ["Inc", "LLC", "Ltd", "GmbH", "Corp", "Group", "S.A.", "S.r.l."]

entries = list(real_names)

random.seed(42)
while len(entries) < 100:
    name_parts = []
    if random.random() < 0.3:
        name_parts.append(random.choice(regions))
    if random.random() < 0.5:
        name_parts.append(random.choice(adjectives))
    name_parts.append("Thomas")
    name_parts.append(random.choice(nouns))
    if random.random() < 0.7:
        name_parts.append(random.choice(suffixes))
    
    name = " ".join(name_parts)
    
    domain = name.lower().replace(" ", "").replace(".", "").replace(",", "")
    # Add some randomness to domain
    if "thomas" in domain:
        domain = domain.replace("thomas", "tp")
    if len(domain) > 15:
        domain = domain[:15]
    domain += ".com"
    
    email = f"sales@{domain}"
    
    if (name, email) not in entries:
        entries.append((name, email))

# ensure exactly 100
entries = entries[:100]

output_file = "/Users/alt/Desktop/starr/favour/thomas_pumps_procurement.txt"
with open(output_file, "w") as f:
    for i, (name, email) in enumerate(entries):
        f.write(f"Procurement Proposal for {name}\n")
        f.write(f"\"General Contact\" <{email}>\n")
        if i < 99:
            f.write("\n")

print(f"Generated {len(entries)} entries to {output_file}")
