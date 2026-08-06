import csv

anest_iwata_master = [
    # Americas Subsidiaries & Regional Network
    {"company": "ANEST IWATA Americas, Inc.", "name": "Gary Glass", "email": "info@anestiwataamericas.com"},
    {"company": "ANEST IWATA Medea Inc.", "name": "Iain Medea", "email": "iain@iwata-medea.com"},
    {"company": "ANEST IWATA México, S. de R.L. de C.V.", "name": "Gary Glass", "email": "contacto@anest-iwata.com.mx"},
    {"company": "AIRZAP – ANEST IWATA Indústria e Comércio Ltda.", "name": "Renato Laranjeira", "email": "renato@airzap.com.br"},
    {"company": "Arte y Aerografía S.A. de C.V.", "name": "Leo Llerena", "email": "contacto@arteyaerografia.com"},
    {"company": "Altec Fluidos de México S.A. de C.V.", "name": "Executive Management Team", "email": "altecfluidos1@gmail.com"},
    {"company": "Delta Tiger S.A. de C.V.", "name": "Executive Leadership", "email": "contacto@deltatiger.com.mx"},
    {"company": "Doutor Pistola", "name": "Anderson Vaz de Oliveira", "email": "contato@doutorpistola.com.br"},
    {"company": "Enko SpA (Enko Chile)", "name": "Roberto Konsens", "email": "contacto@enko.net"},
    {"company": "Visos Pinturas S.A.S.", "name": "Executive Management Team", "email": "contacto@visospinturas.com"},
    {"company": "Monumental Del Plata S.A.", "name": "Ariel Marcelo Jais", "email": "info@monumentaldelplata.com.ar"},
    {"company": "Andy Color's E.I.R.L.", "name": "Javier Glicerio Aquiño Melgarejo", "email": "ventas@andycolors.com"},

    # North American Stocking Distributors & Representatives
    {"company": "Spray Fish Inc.", "name": "Steve Fish", "email": "steve@sprayfishinc.com"},
    {"company": "Global Vacuum LLC", "name": "Mark Allen", "email": "mallen@globalvacuumllc.com"},
    {"company": "Innovac Vacuum Solutions LLC", "name": "Michael Davies", "email": "mdavies@innovacllc.com"},
    {"company": "T&L Finishing Products", "name": "Terry Leman", "email": "terry@tlfinish.com"},
    {"company": "Spokane Hardware Supply Inc.", "name": "Tom Kiemle", "email": "tomk@spokane-hardware.com"},

    # Europe Corporate Entities & Authorized Network (Africa Skipped)
    {"company": "ANEST IWATA Strategic Center S.r.l.", "name": "Takuya Matsumoto", "email": "t.matsumoto@anest-iwata-st.com"},
    {"company": "ANEST IWATA Europe GmbH", "name": "Ryosuke Kawano", "email": "r.kawano@anest-iwata-air.com"},
    {"company": "HARDER & STEENBECK GmbH & Co. KG", "name": "Jens Matthießen", "email": "j.matthiessen@harder-airbrush.de"},
    {"company": "ANEST IWATA France S.A.", "name": "Christophe Marconnet", "email": "c.marconnet@anest-iwata-fr.com"},
    {"company": "ANEST IWATA (U.K.) Ltd.", "name": "Anthony John Robson", "email": "a.robson@anest-iwata-uk.com"},
    {"company": "Morleys Derby Limited (SpraygunsDirect)", "name": "Christopher James Clarke", "email": "c.clarke@spraygunsdirect.co.uk"},
    {"company": "ANEST IWATA Ibérica, S.L.U.", "name": "Takuya Matsumoto", "email": "t.matsumoto@anest-iwata.es"},
    {"company": "ANEST IWATA Scandinavia AB", "name": "Benny Eriksson", "email": "b.eriksson@anest-iwata.se"},
    {"company": "LAKGRUPPEN A/S", "name": "Ole Thomas Dupont", "email": "o.dupont@lakgruppen.com"},
    {"company": "eTail Handel AS (Billakk.no)", "name": "Roar Johansen", "email": "r.johansen@etailhandel.no"},
    {"company": "Pintaväri Oy", "name": "Karri Glasin", "email": "k.glasin@pintavari.fi"},
    {"company": "ANEST IWATA Polska Sp. z o.o.", "name": "Wojciech Cyprian Niedźwiedź", "email": "w.niedzwiedz@anest-iwata-pl.com"},
    {"company": "Wiltec B.V.", "name": "Bart Zegers", "email": "b.zegers@wiltec.nl"},
    {"company": "Spray-Technik AG", "name": "Martin Christen", "email": "m.christen@spraytechnik.ch"},
    {"company": "Gamin s.r.o.", "name": "Radana Brábníková", "email": "r.brabnikova@gamin.cz"}
]

out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

# Remove duplicate entries
seen_emails = set()
unique_entries = []

for item in anest_iwata_master:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        seen_emails.add(em)
        unique_entries.append(item)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in unique_entries:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully compiled {len(unique_entries)} Anest Iwata distributor entries to {out_csv}")
