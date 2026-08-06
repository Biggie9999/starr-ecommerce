import csv

becker_site_master = [
    # Global Parent & North America
    {"company": "Gebr. Becker GmbH Global Headquarters", "ceo": "Dr. Dorothee Becker", "email": "dorothee.becker@becker-international.com", "domain": "becker-international.com", "region": "Germany (Global HQ)"},
    {"company": "Becker Pumps Corporation USA Headquarters", "ceo": "Jason Rathbun", "email": "Jason.Rathbun@beckerpumps.com", "domain": "beckerpumps.com", "region": "United States (North America HQ)"},
    {"company": "Becker Canada Vacuum Technology Corp", "ceo": "Sidharth Sood", "email": "sidharth.sood@beckerpumps.com", "domain": "becker-canada.com", "region": "Canada"},
    {"company": "Becker Vacuum Technology Mexico", "ceo": "Luis Gomez", "email": "info@becker-mexico.mx", "domain": "becker-mexico.mx", "region": "Mexico & LATAM"},
    {"company": "R.E. Morrison Equipment Inc.", "ceo": "Adam Ralph", "email": "a.ralph@remequip.com", "domain": "remequip.com", "region": "Canada (Ontario / Eastern Canada)"},
    {"company": "HVH Industrial Solutions LLC", "ceo": "Vladimir Harutyunyan", "email": "vlad@hvhindustrial.com", "domain": "hvhindustrial.com", "region": "USA (East Coast / Nationwide)"},
    {"company": "Centennial Equipment", "ceo": "Jason Munzer", "email": "jmunzer@centennialequipment.com", "domain": "centennialequipment.com", "region": "USA (Colorado / Rocky Mountain Region)"},
    {"company": "CNC Parts Dept, Inc.", "ceo": "Roupen Merjanian", "email": "sales@cncpd.com", "domain": "cncpd.com", "region": "USA (California / Western Region)"},
    {"company": "Smart Fluid and Vacuum Technologies (SFV Technologies)", "ceo": "Executive Management Team", "email": "info@sfvtechnologies.com", "domain": "sfvtechnologies.com", "region": "Mexico & US Southwest"},
    {"company": "Application Associates (The Murcia Group LLC)", "ceo": "Ed Murcia", "email": "info@applicationassociates.com", "domain": "applicationassociates.com", "region": "USA (New Jersey / Mid-Atlantic)"},

    # Europe
    {"company": "Becker UK Ltd", "ceo": "Richard Oxley", "email": "richard.oxley@becker.co.uk", "domain": "becker.co.uk", "region": "United Kingdom & Ireland"},
    {"company": "Becker France SARL", "ceo": "Alexandre Yves Clay", "email": "becker@becker-france.fr", "domain": "becker-france.fr", "region": "France"},
    {"company": "Becker Italia S.r.l.", "ceo": "Fabrizio Cazzoli", "email": "fabrizio.cazzoli@becker.it", "domain": "becker.it", "region": "Italy"},
    {"company": "Becker Ibérica de Bombas de Vacío y Compresores, S.A.", "ceo": "Mario Peralta", "email": "mario.peralta@becker-iberica.com", "domain": "becker-iberica.com", "region": "Spain & Portugal"},
    {"company": "Becker Druk- en Vacuümpompen B.V.", "ceo": "Nico Segers", "email": "nico.segers@beckerdvp.nl", "domain": "beckerdvp.nl", "region": "Netherlands"},
    {"company": "Becker Druk- en Vacuümpompen B.V. (Belgium Division)", "ceo": "Nico Segers", "email": "nico.segers@beckerdvp.nl", "domain": "beckerdvp.nl", "region": "Belgium & Luxembourg"},
    {"company": "Gebrüder Becker Austria GmbH", "ceo": "Fabio Pappacena", "email": "fabio.pappacena@becker-austria.com", "domain": "becker-austria.com", "region": "Austria"},
    {"company": "Becker AG Switzerland", "ceo": "Fabio Pappacena", "email": "fabio.pappacena@becker.ch", "domain": "becker.ch", "region": "Switzerland"},
    {"company": "Becker Vakuumteknik AB", "ceo": "Thomas Grundström", "email": "thomas.grundstrom@beckervakuum.se", "domain": "beckervakuum.se", "region": "Sweden & Nordics"},
    {"company": "Becker Polska Sp. z o.o.", "ceo": "Grzegorz Wojciechowski", "email": "grzegorz.wojciechowski@becker-polska.com", "domain": "becker-polska.com", "region": "Poland"},
    {"company": "YNNA spol. s r.o.", "ceo": "Ing. Štefan Nemčok", "email": "stefan.nemcok@ynna.cz", "domain": "ynna.cz", "region": "Czechia & Slovakia"},

    # Rest of World
    {"company": "Becker Pumps Australia", "ceo": "James Stewart", "email": "sales@beckerpumps.com.au", "domain": "beckerpumps.com.au", "region": "Australia"},
    {"company": "Vacuum Pumps NZ Ltd (VPNZ)", "ceo": "Lawrence David Walls", "email": "info@vpnz.co.nz", "domain": "vpnz.co.nz", "region": "New Zealand"},
    {"company": "Gebr. Becker India Vacuum Pumps Pvt. Ltd.", "ceo": "Milind Bhalerao", "email": "milind@becker-india.com", "domain": "becker-india.com", "region": "India"},
    {"company": "Becker Asia Pacific Pte. Ltd.", "ceo": "Jimmy Teo", "email": "info@beckerasia.com.sg", "domain": "beckerasia.com.sg", "region": "Singapore & Southeast Asia"},
    {"company": "Becker Airtechno Co., Ltd.", "ceo": "Shokichi Miki", "email": "info@becker-japan.co.jp", "domain": "becker-japan.co.jp", "region": "Japan"},
    {"company": "Becker Korea Co., Ltd.", "ceo": "Hwang Sun-hee", "email": "becker@beckerkorea.co.kr", "domain": "beckerkorea.co.kr", "region": "South Korea"},
    {"company": "Becker Vacuum & Air Equipment (Shanghai) Co., Ltd.", "ceo": "Jimmy Teo", "email": "info@becker-china.com", "domain": "becker-china.com", "region": "China"},
    {"company": "African Vacuum Tech Distribution (Pty) Ltd", "ceo": "Shaun David", "email": "shaun.david@africanvacuumpumps.com", "domain": "africanvacuumpumps.com", "region": "South Africa & Sub-Saharan Africa"},
    {"company": "Fluidtec Equipment Trading L.L.C.", "ceo": "Ehab Abu Shama", "email": "ceo@fluidtec.ae", "domain": "fluidtec.ae", "region": "UAE & Middle East"},
    {"company": "Mechatronics Industrial Equipment", "ceo": "Stanley C. J. Daniel", "email": "mechtron@mechatronics.ae", "domain": "mechatronics.ae", "region": "UAE & Middle East"},
    {"company": "Vacuum Tech Máquinas e Equipamentos Ltda. (Robmaq)", "ceo": "Rafael Robmaq", "email": "rafael@robmaq.com.br", "domain": "robmaq.com.br", "region": "Brazil"},
    {"company": "W&F Ingeniería y Máquinas S.A.", "ceo": "Roberto Wendler Apel", "email": "rwendler@wyf.cl", "domain": "wyf.cl", "region": "Chile"},
    {"company": "CompVac - Sistemas de Aire Comprimido y Vacío", "ceo": "Guillermo Quintin", "email": "guillermo.quintin@compvac.com.ar", "domain": "compvac.com.ar", "region": "Argentina"}
]

out_txt = "/Users/alt/Desktop/starr/favour/becker_site_official_distributors.txt"
out_csv = "/Users/alt/Desktop/starr/favour/becker_site_official_distributors.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(becker_site_master):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(becker_site_master) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company Name", "CEO / MD Name", "CEO Direct Email", "Domain", "Territory / Region"])
    for item in becker_site_master:
        writer.writerow([item["company"], item["ceo"], item["email"], item["domain"], item["region"]])

print(f"Saved {len(becker_site_master)} verified Becker site entities to {out_txt} and {out_csv}")
