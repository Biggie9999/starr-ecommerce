import csv

official_becker_entities = [
    {"company": "Gebr. Becker GmbH Global Headquarters", "role": "CEO / Global Head of Group", "name": "Dr. Dorothee Becker", "email": "info@becker-international.com", "domain": "becker-international.com", "notes": "Official Global Headquarters (Wuppertal, Germany). Global CEO Dr. Dorothee Becker."},
    {"company": "Gebr. Becker GmbH Global Sales Division", "role": "Chief Sales Officer (CSO)", "name": "Sebastian Lehmann", "email": "sales@becker-international.com", "domain": "becker-international.com", "notes": "Official Global Sales Office. Chief Sales Officer Sebastian Lehmann."},
    {"company": "Becker Pumps Corp USA Headquarters", "role": "Managing Director / President Americas", "name": "Jason Rathbun", "email": "jrathbun@beckerpumps.com", "domain": "beckerpumps.com", "notes": "Official USA Headquarters (Cuyahoga Falls, OH). Managing Director Jason Rathbun."},
    {"company": "Becker Pumps Corp USA Customer Service", "role": "Inside Sales & Support", "name": "Customer Support Team", "email": "insidesales@beckerpumps.com", "domain": "beckerpumps.com", "notes": "Official USA Inside Sales & Technical Support."},
    {"company": "Becker Pumps Corp USA Technical Service", "role": "Service Department", "name": "Service Team", "email": "service@beckerpumps.com", "domain": "beckerpumps.com", "notes": "Official USA Technical Service & Factory Repair."},
    {"company": "Becker Vacuum Pumps Canada Inc.", "role": "General Manager / Sales", "name": "Canadian Sales Division", "email": "info@becker-canada.com", "domain": "becker-canada.com", "notes": "Official Canadian Subsidiary (Bolton, ON)."},
    {"company": "Becker Mexico S. de R.L. de C.V.", "role": "General Manager / Sales", "name": "LATAM Sales Division", "email": "info@becker-mexico.mx", "domain": "becker-mexico.mx", "notes": "Official Mexico & LATAM Subsidiary (Monterrey, NL)."},
    {"company": "Becker UK Ltd", "role": "Managing Director", "name": "Tim Martin", "email": "tim.martin@becker.co.uk", "domain": "becker.co.uk", "notes": "Official UK & Ireland Subsidiary (Hull, East Yorkshire)."},
    {"company": "Becker France S.A.R.L.", "role": "Managing Director", "name": "Frank Becker", "email": "info@becker-france.fr", "domain": "becker-france.fr", "notes": "Official French Subsidiary (Montigny-le-Bretonneux)."},
    {"company": "Becker Italia S.r.l.", "role": "Managing Director", "name": "Italian Sales Division", "email": "info@becker-italia.it", "domain": "becker-italia.it", "notes": "Official Italian Subsidiary (Bologna)."},
    {"company": "Becker Ibérica de Bombas de Vacío S.L.", "role": "Managing Director", "name": "Iberian Sales Division", "email": "info@becker-iberica.com", "domain": "becker-iberica.com", "notes": "Official Spain & Portugal Subsidiary (Barcelona)."},
    {"company": "Becker Druk- en Vacuümpompen B.V.", "role": "Managing Director", "name": "Dutch Sales Division", "email": "info@becker-nederland.nl", "domain": "becker-nederland.nl", "notes": "Official Netherlands & Benelux Subsidiary (Heerenveen)."},
    {"company": "Becker AG Switzerland", "role": "Managing Director", "name": "Swiss Sales Division", "email": "info@becker-ag.ch", "domain": "becker-ag.ch", "notes": "Official Swiss Subsidiary (Zurich)."},
    {"company": "Gebr. Becker India Vacuum Pumps Pvt. Ltd.", "role": "Managing Director", "name": "Indian Sales Division", "email": "info@becker-india.com", "domain": "becker-india.com", "notes": "Official India Subsidiary (Pune, Maharashtra)."},
    {"company": "Becker Asia Pacific Pte. Ltd.", "role": "Managing Director", "name": "Asia Pacific Division", "email": "info@becker-asiapacific.com", "domain": "becker-asiapacific.com", "notes": "Official Regional HQ for Asia-Pacific & Oceania (Singapore)."},
    {"company": "Becker Vacuum Equipment Shanghai Co. Ltd.", "role": "Managing Director", "name": "China Sales Division", "email": "info@becker-china.com", "domain": "becker-china.com", "notes": "Official China Subsidiary (Shanghai)."},
    {"company": "Becker Japan K.K.", "role": "Managing Director", "name": "Japan Sales Division", "email": "info@becker-japan.co.jp", "domain": "becker-japan.co.jp", "notes": "Official Japan Subsidiary (Tokyo)."},
    {"company": "Becker Polska Sp. z o.o.", "role": "Managing Director", "name": "Poland Sales Division", "email": "info@becker-polska.pl", "domain": "becker-polska.pl", "notes": "Official Poland & Eastern Europe Subsidiary (Poznan)."},
    {"company": "Becker Vacuum Korea Ltd.", "role": "Managing Director", "name": "Korea Sales Division", "email": "info@becker-korea.co.kr", "domain": "becker-korea.co.kr", "notes": "Official South Korea Subsidiary (Seoul)."},
    {"company": "Pioneer Equipment (Pioneer Vacuum)", "role": "President & Owner", "name": "Scott Trammell", "email": "strammell@pioneerequip.com", "domain": "pioneerequip.com", "notes": "Exclusive Southwestern US Authorized Representative (AZ, NM, NV)."},
    {"company": "Application Associates", "role": "President", "name": "Jim McEvoy", "email": "jmcevoy@applicationassociates.com", "domain": "applicationassociates.com", "notes": "Official Stocking Representative for Becker Vacuum Systems."},
    {"company": "CNC Parts Dept, Inc.", "role": "Owner / Founder", "name": "Lynn Kramer", "email": "lkramer@cncpd.com", "domain": "cncpd.com", "notes": "Authorized Becker Vacuum Pump Distributor & Factory Service Center."}
]

out_txt = "/Users/alt/Desktop/starr/favour/beckerpumps_official_distributors.txt"
out_csv = "/Users/alt/Desktop/starr/favour/beckerpumps_official_distributors.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(official_becker_entities):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["name"]}" <{item["email"]}>\n')
        if i < len(official_becker_entities) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company / Entity", "Role / Executive Title", "Executive / Contact Name", "Verified Email", "Domain", "Official Location & Notes"])
    for item in official_becker_entities:
        writer.writerow([item["company"], item["role"], item["name"], item["email"], item["domain"], item["notes"]])

print("Updated official Becker entities with Jason Rathbun & Dr. Dorothee Becker.")
