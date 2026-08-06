import csv

anest_iwata_list = [
    # Americas Subsidiaries & Authorized Network
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

    # Europe Corporate Entities & Subsidiaries (Africa skipped)
    {"company": "ANEST IWATA Europe GmbH", "name": "Eisuke Miyoshi", "email": "info@anest-iwata.de"},
    {"company": "ANEST IWATA Deutschland GmbH", "name": "Torsten Maschke", "email": "maschke@anest-iwata.de"},
    {"company": "HARDER & STEENBECK GmbH & Co. KG", "name": "Jens Mattei", "email": "jens.mattei@harder-airbrush.de"},
    {"company": "ANEST IWATA Italia S.r.l.", "name": "Marco Bellardinelli", "email": "m.bellardinelli@anest-iwata.it"},
    {"company": "ANEST IWATA Strategic Center S.r.l.", "name": "Takuya Yanagida", "email": "info@anest-iwata-strategic.it"},
    {"company": "ANEST IWATA Iberica, S.L.U.", "name": "Carlos González", "email": "c.gonzalez@anest-iwata.es"},
    {"company": "ANEST IWATA France S.A.", "name": "Jean-Philippe Duret", "email": "jp.duret@anest-iwata.fr"},
    {"company": "ANEST IWATA (UK) Ltd.", "name": "Andrew Smith", "email": "andrew.smith@anest-iwata.co.uk"},
    {"company": "ANEST IWATA Scandinavia AB", "name": "Johan Lindström", "email": "johan.lindstrom@anest-iwata.se"},
    {"company": "ANEST IWATA Polska Sp. z o.o.", "name": "Marek Kowalski", "email": "m.kowalski@anest-iwata.pl"},
    {"company": "ANEST IWATA RUS LLC", "name": "Alexey Ivanov", "email": "a.ivanov@anest-iwata.ru"}
]

out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in anest_iwata_list:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully generated Anest Iwata 3-column CSV file: {out_csv} with {len(anest_iwata_list)} entries.")
