import csv

dealers = [
    ("eVacuumStore", "eVacuumStore.com"),
    ("Central Vacuum Direct", "centralvacuumdirect.com"),
    ("ThinkVacuums", "thinkvacuums.com"),
    ("Vac Superstore", "vacsuperstore.com"),
    ("Not Just Vacs", "notjustvacs.com"),
    ("VacWorks", "vacworks.ca"),
    ("AAA Vacuum Centre", "aaavacuum.ca"),
    ("Armstrong Installers", "armstronginstallers.com"),
    ("Aspirateur Direct", "aspirateurdirect.com"),
    ("Aspirateur Dorion", "aspirateurdorion.com"),
    ("Built-In Vacuum", "builtinvacuum.com"),
    ("McHardy Vacuum", "mchardyvac.com"),
    ("Advantage Vacuums", "advantagevacuums.com"),
    ("Vacuum Specialists", "vacuumspecialists.com"),
    ("Superior Vacuums", "superiorvacuums.ca"),
    ("Dynamic Vacuums", "dynamicvacuums.com"),
    ("D & R Vacuum", "drvacuum.ca"),
    ("Elmira Vacuum & Electrical", "elmiravacuum.com"),
    ("Blue Mountain Vacuum Centre", "bluemountainvacuum.ca"),
    ("The Vacuum Factory", "thevacuumfactory.ca")
]

with open('/Users/alt/Desktop/starr/favour/canavac_dealers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Company', 'CEO/Contact Name', 'Domain'])
    for dealer in dealers:
        writer.writerow([dealer[0], 'CEO', dealer[1]])

