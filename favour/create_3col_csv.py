import csv

independent_distributors = [
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
    {"company": "CompVac - Sistemas de Aire Comprimido y Vacío", "name": "Guillermo Quintin", "email": "guillermo.quintin@compvac.com.ar"}
]

out_csv = "/Users/alt/Desktop/starr/favour/becker_distributors_3col.csv"

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in independent_distributors:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully generated 3-column CSV file: {out_csv} with {len(independent_distributors)} rows.")
