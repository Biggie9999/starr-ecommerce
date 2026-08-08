import csv

all_anest_entries = [
    # Initial Batch
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
    {"company": "Spray Fish Inc.", "name": "Steve Fish", "email": "steve@sprayfishinc.com"},
    {"company": "Global Vacuum LLC", "name": "Mark Allen", "email": "mallen@globalvacuumllc.com"},
    {"company": "Innovac Vacuum Solutions LLC", "name": "Michael Davies", "email": "mdavies@innovacllc.com"},
    {"company": "T&L Finishing Products", "name": "Terry Leman", "email": "terry@tlfinish.com"},
    {"company": "Spokane Hardware Supply Inc.", "name": "Tom Kiemle", "email": "tomk@spokane-hardware.com"},
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
    {"company": "Gamin s.r.o.", "name": "Radana Brábníková", "email": "r.brabnikova@gamin.cz"},
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
    {"company": "Selectum LLC", "name": "Customer Leadership Team", "email": "info@selectumllc.com"},

    # Swarm US East & Midwest
    {"company": "Pittsburgh Spray Equipment Company", "name": "Patrick Harmon", "email": "patrick@pittsburghsprayequip.com"},
    {"company": "Atlantic Compressors, Inc.", "name": "Bill Rimer", "email": "bill@atlanticcompressors.com"},
    {"company": "Industrial Air Centers, Inc.", "name": "Dave Suder", "email": "dsuder@iacserv.com"},
    {"company": "Brabazon Pump, Compressor & Vacuum", "name": "Heath Brabazon", "email": "president@brabazon.com"},
    {"company": "Cowart Air Compressor & Generator, Inc.", "name": "Dusty Cowart", "email": "cac@cowart-inc.net"},
    {"company": "Air Compressor & Motor Co.", "name": "Lowell Jones", "email": "aircomo@aircomo.com"},
    {"company": "SprayGunner", "name": "Artem Revunov", "email": "sales@spraygunner.com"},

    # Swarm US South & West
    {"company": "Advanced Air & Vacuum Inc.", "name": "Joseph James Vanderbilt Jr.", "email": "joseph@aavsales.com"},
    {"company": "Rocha Compressed Air Specialists", "name": "Joseph A. Miller", "email": "joe@rochacorp.com"},
    {"company": "Advanced Compressed Air Solutions, LLC", "name": "Morris Lawson", "email": "sales@advancedcompressedair.com"},
    {"company": "Airquip Systems, Inc.", "name": "Grant Simpkins", "email": "admin@airquipsystems.com"},
    {"company": "Texas Compression Services", "name": "Robert Casey", "email": "sales@texascompressionservices.com"},
    {"company": "Air Compressor Solutions (ACS)", "name": "Brian Stubbs", "email": "sales@acsir.com"},
    {"company": "Lancers, Inc.", "name": "Alan Spencer", "email": "lancersscrmnto@gmail.com"},
    {"company": "The Merri Artist", "name": "Merri Sayers", "email": "info@merriartist.com"},
    {"company": "Cascade Machinery & Electric, Inc.", "name": "Michael Spring", "email": "mspring@cascade-machinery.com"},

    # Swarm Europe
    {"company": "Ultrimax Coatings Ltd", "name": "Giles Hoare", "email": "g.hoare@ultrimaxstore.com"},
    {"company": "West Midlands Compressors Ltd", "name": "Mikolaj Daniel Wrobel", "email": "m.wrobel@wmcompressors.co.uk"},
    {"company": "The Airbrush Company Ltd", "name": "Alexandra Medwell", "email": "alex@airbrushes.com"},
    {"company": "Eurospray (Ireland) Limited", "name": "Jimmy Harte", "email": "j.harte@eurosprayireland.com"},
    {"company": "ACH AUTOCOLOR Marc Becker KG", "name": "Marc Becker", "email": "m.becker@ach-autocolor.com"},
    {"company": "ALZ PLANERT (ALPA Industrievertretungen)", "name": "Robin Koch", "email": "r.koch@alz-planert.de"},
    {"company": "JEKA France", "name": "Jessie Rey", "email": "j.rey@jeka-france.com"},
    {"company": "AGL Marine", "name": "Gérard Lachkar", "email": "g.lachkar@agl-marine.com"},
    {"company": "Vip Tools", "name": "Pascal Duquenne", "email": "p.duquenne@viptools.be"},
    {"company": "IMM HM SA", "name": "Pierre Herbiet", "email": "p.herbiet@immhm.be"},
    {"company": "Racing Colors S.L.", "name": "Ivan Cureses Menéndez", "email": "i.cureses@racingcolors.com"},
    {"company": "Colourfox", "name": "Gary Gándara", "email": "g.gandara@colourfox.com"},
    {"company": "Colore Amico S.r.l.", "name": "Marzio Ferrero", "email": "m.ferrero@coloreamico.it"},
    {"company": "CROP (NonPaints)", "name": "Dexter Driessen", "email": "d.driessen@nonpaints.com"},
    {"company": "Van Veluw Compressoren B.V.", "name": "Janick van Veluw", "email": "janick@veluwcompressoren.nl"},
    {"company": "Tipro AB", "name": "Patrick Andersson", "email": "patrick@tipro.se"},
    {"company": "Färgprodukter Plym & Co AB", "name": "Andreas Plym", "email": "andreas.plym@fargprodukter.se"},
    {"company": "C. Christoffersen AS", "name": "Morten Christian Christoffersen", "email": "kikkan@cchristoffersen.no"},
    {"company": "Lakkspesialisten AS", "name": "Ole Petter Mortensen", "email": "ole.petter.mortensen@lakkspesialisten.no"},
    {"company": "Merazet S.A.", "name": "Mariusz Raczak", "email": "m.raczak@merazet.pl"},
    {"company": "Autokolor-Ukleja Group Sp. z o.o.", "name": "Maciej Ukleja", "email": "maciej@ukleja.com.pl"},
    {"company": "Toplac s.r.o.", "name": "Martin Šmerda", "email": "m.smerda@toplac.cz"},
    {"company": "ŽÁRSKÝ s.r.o.", "name": "Karel Žárský", "email": "karel.zarsky@lechler.cz"},

    # Swarm Asia-Pacific
    {"company": "TradeTools Pty Ltd", "name": "Jeremy Stewart", "email": "sales@tradetools.com"},
    {"company": "Eastern Auto Paints", "name": "Executive Leadership Team", "email": "orders@autopaints.com.au"},
    {"company": "Complete Compressed Air Systems", "name": "Executive Operations Team", "email": "sales@ccas.com.au"},
    {"company": "GPI Automotive (NZ) Ltd", "name": "Colin Edwards", "email": "sales@gpi.com.au"},
    {"company": "Smits Group", "name": "John Greenacre", "email": "sales@smitsgroup.co.nz"},
    {"company": "RA Johnstone & Co Ltd", "name": "Michael Head", "email": "cameron@raj.co.nz"},
    {"company": "Ahuja Corporation Private Limited", "name": "Lalit Ahuja", "email": "projects@ahujagroup.in"},
    {"company": "Bimpex Machines Pvt. Ltd.", "name": "Jaideep Chawla", "email": "bimpex@bimpexindia.com"},
    {"company": "Multi Industrial Supplies Pte Ltd", "name": "Alvin Tan", "email": "alvin@multi.com.sg"},
    {"company": "IWATECH Services & Sales Sdn Bhd", "name": "Executive Management Team", "email": "my@iwatech.com"},
    {"company": "Takeiki Sdn Bhd", "name": "Executive Operations Director", "email": "sales-my@takeiki.net"},
    {"company": "WLC Technology Sdn Bhd", "name": "Michael Lanny", "email": "sales@wlctechnology.com"},
    {"company": "Aceplus Technology Services Sdn Bhd", "name": "Jason Chieng", "email": "aceplus.sales@aceplustech.com.my"},
    {"company": "PT. Sinar Mutiara Cakrabuana / PT Riyadi", "name": "Ricky Jap", "email": "web@riyadi.co.id"},
    {"company": "KHM Megatools Corp.", "name": "Kim M.", "email": "sales@khmtools.com.ph"},
    {"company": "Gigatools Corporation", "name": "Executive Management Team", "email": "info@gigatools.ph"},
    {"company": "Tung Hsin Chang Corporation (THC)", "name": "Jian-Jun Chen", "email": "service@thcgroup.com.tw"},
    {"company": "Trusco Nakayama Corporation", "name": "Tetsuya Nakayama", "email": "info@trusco.co.jp"},
    {"company": "Yamazen Corporation", "name": "Koji Kishida", "email": "info@yamazen.co.jp"},

    # Swarm LATAM
    {"company": "Spray Tecnologia em Pintura Ltda", "name": "Fernando Baldin", "email": "fernando@spraytecno.com"},
    {"company": "Celmar Comercial e Importadora Ltda", "name": "Manuel Antonio Rodrigues", "email": "vendas@celmar.com.br"},
    {"company": "RC Futuro Serviço e Comércio Ltda", "name": "Ricardo Corrêa", "email": "comercial@rcfuturo.com.br"},
    {"company": "Veritec S.A.", "name": "Maria Florencia Dalle Palle", "email": "info@veritec.com.ar"},
    {"company": "La Casa del Soplete", "name": "Jorge Zucro", "email": "ventas@lacasadelsoplete.com.ar"},
    {"company": "Equipos Internacionales S.A.S. (Equinter)", "name": "Executive Management Team", "email": "ventas@equinter.co"},
    {"company": "Electro Ferro Centro S.A.C. (EFC)", "name": "David Mélinchon Morales", "email": "marketing@efc.com.pe"},
    {"company": "Dimerc Perú S.A.C.", "name": "Diego Álvarez del Villar", "email": "ventas@dimerc.pe"},
    {"company": "SAAT S.A.", "name": "Executive Management Team", "email": "saat@saat.cl"},
    {"company": "Dan Technique / Danair SpA", "name": "Executive Management Team", "email": "infodan@dan.cl"},
    {"company": "Dicema S.A.", "name": "Executive Management Team", "email": "ventas@dicema.com.gt"},
    {"company": "Grupo Solder S.A. de C.V.", "name": "Sergio González", "email": "hola@mipeleteria.com.mx"},
    {"company": "PV-Solutions, S.A. de C.V.", "name": "Executive Leadership Team", "email": "contacto@pvsolutions.com.mx"},
    {"company": "Grupo Equipa", "name": "Executive Management Team", "email": "consultor@tecnologiaenaire.mx"},
    {"company": "Tecnología en Compresión de Occidente", "name": "Executive Engineering Management", "email": "proyectos@tecencompresion.com"}
]

out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

# Remove duplicate entries based on email
seen_emails = set()
unique_entries = []

for item in all_anest_entries:
    em = item["email"].lower().strip()
    if em not in seen_emails:
        seen_emails.add(em)
        unique_entries.append(item)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for item in unique_entries:
        writer.writerow([item["company"], item["name"], item["email"]])

print(f"Successfully compiled {len(unique_entries)} unique Anest Iwata distributor entries to {out_csv}")
