import csv

independent_distributors = [
    {"company": "R.E. Morrison Equipment Inc.", "ceo": "Adam Ralph", "email": "a.ralph@remequip.com", "domain": "remequip.com", "region": "Canada (Ontario / Eastern Canada)"},
    {"company": "HVH Industrial Solutions LLC", "ceo": "Vladimir Harutyunyan", "email": "vlad@hvhindustrial.com", "domain": "hvhindustrial.com", "region": "USA (East Coast / Nationwide)"},
    {"company": "Centennial Equipment", "ceo": "Jason Munzer", "email": "jmunzer@centennialequipment.com", "domain": "centennialequipment.com", "region": "USA (Colorado / Rocky Mountain Region)"},
    {"company": "CNC Parts Dept, Inc.", "ceo": "Roupen Merjanian", "email": "sales@cncpd.com", "domain": "cncpd.com", "region": "USA (California / Western Region)"},
    {"company": "Smart Fluid and Vacuum Technologies (SFV Technologies)", "ceo": "Executive Management Team", "email": "info@sfvtechnologies.com", "domain": "sfvtechnologies.com", "region": "Mexico & US Southwest"},
    {"company": "Application Associates (The Murcia Group LLC)", "ceo": "Ed Murcia", "email": "info@applicationassociates.com", "domain": "applicationassociates.com", "region": "USA (New Jersey / Mid-Atlantic)"},
    {"company": "Pioneer Equipment", "ceo": "Scott Trammell", "email": "strammell@pioneerequip.com", "domain": "pioneerequip.com", "region": "USA (Southwestern Region)"},
    {"company": "Stateside Industrial Solutions", "ceo": "Dennis R. Hernandez", "email": "dhernandez@statesideindustrial.com", "domain": "statesideindustrial.com", "region": "USA (Florida)"},
    {"company": "Powermatic Associates", "ceo": "Frank Nudo", "email": "fnudo@powermatic.net", "domain": "powermatic.net", "region": "USA (California)"},
    {"company": "YNNA spol. s r.o.", "ceo": "Ing. Štefan Nemčok", "email": "stefan.nemcok@ynna.cz", "domain": "ynna.cz", "region": "Czechia & Slovakia"},
    {"company": "Metzger Technik GmbH", "ceo": "Gerd Metzger", "email": "gerd.metzger@metzger-technik.de", "domain": "metzger-technik.de", "region": "Germany"},
    {"company": "Directair", "ceo": "Allan Dolby", "email": "allan.dolby@directair.co.uk", "domain": "directair.co.uk", "region": "United Kingdom"},
    {"company": "Air Supply Ltd", "ceo": "George Jackson Wright", "email": "george.wright@airsupply.co.uk", "domain": "airsupply.co.uk", "region": "United Kingdom"},
    {"company": "Vacuum Pump Services Ltd", "ceo": "Peter Douglas Bowen", "email": "p.bowen@vacuumpumpservices.co.uk", "domain": "vacuumpumpservices.co.uk", "region": "United Kingdom"},
    {"company": "Triark Pumps", "ceo": "David Rozée", "email": "david@tri-ark.com", "domain": "tri-ark.com", "region": "United Kingdom"},
    {"company": "Raptor Supplies", "ceo": "Arjun Singh", "email": "arjun@raptorsupplies.com", "domain": "raptorsupplies.com", "region": "Europe"},
    {"company": "Ultra Controlo Projectos Industriais Lda", "ceo": "Sabino de Pompeia", "email": "sabino.pompeia@ultra-controlo.com", "domain": "ultracontrolo.com", "region": "Iberia (Spain & Portugal)"},
    {"company": "Vacuum Pumps NZ Ltd (VPNZ)", "ceo": "Lawrence David Walls", "email": "info@vpnz.co.nz", "domain": "vpnz.co.nz", "region": "New Zealand"},
    {"company": "African Vacuum Tech Distribution (Pty) Ltd", "ceo": "Shaun David", "email": "shaun.david@africanvacuumpumps.com", "domain": "africanvacuumpumps.com", "region": "South Africa & Sub-Saharan Africa"},
    {"company": "Fluidtec Equipment Trading L.L.C.", "ceo": "Ehab Abu Shama", "email": "ceo@fluidtec.ae", "domain": "fluidtec.ae", "region": "UAE & Middle East"},
    {"company": "Mechatronics Industrial Equipment", "ceo": "Stanley C. J. Daniel", "email": "mechtron@mechatronics.ae", "domain": "mechatronics.ae", "region": "UAE & Middle East"},
    {"company": "Vacuum Tech Máquinas e Equipamentos Ltda. (Robmaq)", "ceo": "Rafael Robmaq", "email": "rafael@robmaq.com.br", "domain": "robmaq.com.br", "region": "Brazil"},
    {"company": "W&F Ingeniería y Máquinas S.A.", "ceo": "Roberto Wendler Apel", "email": "rwendler@wyf.cl", "domain": "wyf.cl", "region": "Chile"},
    {"company": "CompVac - Sistemas de Aire Comprimido y Vacío", "ceo": "Guillermo Quintin", "email": "guillermo.quintin@compvac.com.ar", "domain": "compvac.com.ar", "region": "Argentina"}
]

out_txt = "/Users/alt/Desktop/starr/favour/becker_independent_distributors.txt"
out_csv = "/Users/alt/Desktop/starr/favour/becker_independent_distributors.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(independent_distributors):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(independent_distributors) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company Name", "CEO / MD Name", "CEO Direct Email", "Domain", "Territory / Region"])
    for item in independent_distributors:
        writer.writerow([item["company"], item["ceo"], item["email"], item["domain"], item["region"]])

print(f"Saved {len(independent_distributors)} independent Becker distributor entities to {out_txt} and {out_csv}")
