#!/usr/bin/env python3
import csv
import re

# We will read the list of companies we found, and generate strict personal emails
companies_data = [
    # (Company Name, Contact Name, Domain)
    ("Fluid Technologies Ltd (Sprayman UK)", "Michael Philip Nash", "sprayman.co.uk"),
    ("Trade Accessories Distribution (PaintAccess)", "Daniel Dorofeev", "paintaccess.com.au"),
    ("Hi-Tec Spray Ltd (Spray Direct)", "Debra Louise Cooper", "spraydirect.co.uk"),
    ("Crown Paints Limited", "Matthew Crossingham", "crownpaints.com"),
    ("Cloverdale Paint", "Tim Vogel", "cloverdalepaint.com"),
    ("Airless Discounter GmbH", "Stefan Trepke", "airless-discounter.de"),
    ("Portland Compressor, Inc.", "Bob Wilson", "portlandcompressor.com"),
    ("Yorkshire Spray Services Ltd", "Ian Cairns", "yss.co.uk"),
    ("Spray Centre (UK) Limited", "Gary Dale", "spraycentre.co.uk"),
    ("M.J. Supplies Limited", "Martin James", "mj-supplies.com"),
    ("Industrial Spraying Systems Ltd", "Deborah Macdonald", "outlook.com"),
    ("Haller Oberflächentechnik GmbH", "Frank Bieberstein", "gmx.de"),
    ("Köhler Oberflächentechnik GmbH", "Thomas Köhler", "obertech.de"),
    ("Profispritztechnik", "Michael Kessner", "profispritztechnik.de"),
    ("Jahnke GmbH", "Erwin Maier", "airless.de"),
    ("JEKA France", "Jessie Rey", "jeka-france.com"),
    ("LARIUS France", "Christophe Schapelynck", "larius-france.fr"),
    ("FG Service di Ferrari Giuseppe", "Giuseppe Ferrari", "gmail.com"),
    ("Wagner-Service Sp. z o.o.", "Wojciech Wilczek", "wagner-polska.com.pl"),
    ("Technik NTB", "Przemysław Pyrka", "technikntb.pl"),
    ("Bart Agregaty", "Karol Bielski", "o2.pl"),
    ("Speedie Spray and Hydraulics", "Stan Zelek", "speediehydraulics.com.au"),
    ("Total Finishing Supplies", "Sarah Crowder", "totalfinishingsupplies.com"),
    ("Pittsburgh Spray Equipment Company", "Thomas Harmon", "pittsburghsprayequipment.com"),
    ("Priority Airless Equipment, Inc.", "Mathew Hagman", "priorityairlessequipment.com"),
    ("CJ Spray, Inc.", "Chris Bryntesen", "cjspray.com"),
    ("Spray Equipment & Service Center, Inc.", "John Shadinger", "sprayequipment.com"),
    ("Advanced Finishing Systems", "Steve Edmondson", "advancedfinishing.com"),
    ("C.H. Reed, Inc.", "Bob Shields", "chreed.com"),
    ("Painters Supply & Equipment Co.", "Patrick Mayette", "painters-supply.com"),
    ("Industrial Finishing Products", "Steven Galgano", "industrialfinishings.com"),
    ("Finish Systems", "Romy O'Daniel", "finishsystems.com"),
    ("Northern Tool + Equipment", "Suresh Krishna", "northerntool.com"),
    ("Dutra Máquinas", "André Moya", "dutra.com.br"),
    ("Loja do Mecânico", "Guilherme Favaro", "lojadomecanico.com.br"),
    ("Cetec Industrial", "Eduardo Cernic", "cetecindustrial.com.br"),
    ("Casa do Construtor", "Altino Cristofoletti", "casadoconstrutor.com.br"),
    ("Acme Tools", "Steve Kuhlman", "acmetools.com"),
    ("C. Brewer & Sons Limited", "Simon Brewer", "brewers.co.uk"),
    ("Bob Taylor Spray Equipment, Inc.", "Preston Hoffman", "bobtaylorsprayequipment.com"),
    ("Airblast Australia", "David Pocock", "airblastaustralia.com.au"),
    ("Spray Pump Services, L.L.C.", "Kathleen Lemon", "spraypumpservices.com"),
    ("Spray-Quip, Inc.", "Herbert Chilman", "sprayquip.com"),
    ("South Texas Spray Equipment", "George Ferrie", "southtexassprayequipment.com"),
    ("Bolair Fluid Handling Systems", "Gregory Haddow", "bolair.ca"),
    ("Pumpworks Services Ltd.", "Randy Nault", "pumpworks.ca"),
    ("Coast Industrial Systems, Inc.", "Larry Onstott", "coastisi.com"),
    ("Myers Service & Distribution, Inc.", "Stephen Myers", "sprayequipmentcharlottenc.com"),
    ("Pneu-Mech Systems Mfg., Inc.", "Jim Andrews", "pneu-mech.com"),
    ("Ag Spray Equipment", "Mark Schwarz", "agspray.com"),
    ("Fournier Rubber & Supply Co.", "Dennis Davidson", "fournierrubber.com"),
    ("Precision Finishing, Inc.", "Jeffrey Bell", "precisionfinishinginc.com"),
    ("Midwest Finishing Systems, Inc.", "Russ Green", "midwestfinishing.com"),
    ("Tencarva Machinery Company", "Henry Ritchie", "tencarva.com"),
    ("Pro-Tek Spray Equipment", "Patrice Richer", "pro-teksprayequipment.com"),
    ("Koehler Rubber & Supply Co.", "Bernie Green", "koehlerrubber.com"),
    ("Southern Fluid Systems", "Salleigh Grubbs", "southernfluidsystems.com"),
    ("Equipos y Sistemas Carlos Cano, S.L.", "Carlos Cano", "sistemascano.es"),
    ("Makimport Herramientas S.L.", "Laura Frutos", "wagnerstore.com"),
    ("Francés y Gandía S.L.", "María Gandía", "fgwagnerspain.com"),
    ("Jomar Instalaciones de Pinturas SL", "David Fernández", "airless.es"),
    ("Uwe Marx Oberflächentechnik GmbH", "Uwe Marx", "marx-spritzgeraete.de"),
    ("FluidSystems GmbH & Co. KG", "Bernd Schramm", "fluidsystems.de"),
    ("Linz GmbH", "Jürgen Linz", "linz-service.de"),
    ("SEFLID", "Jeannot Nussbaum", "seflid.fr"),
    ("Phillro Industries", "Mark Heaven", "phillro.com.au"),
    ("ABSS", "Aaron Williams", "abss.net.au"),
    ("Tradextra Ltd", "Patrick McLean", "tradextra.co.nz"),
    ("Linkup Paints Bay of Plenty Ltd", "Jason Barry", "linkupbop.co.nz"),
    ("Spray Supplies Scotland Limited", "Steven Cooper", "spraysuppliesscotland.co.uk"),
    ("Airlesspro Ltd", "Philip McGough", "airlesspro.co.uk"),
    ("Build-Spray Systems Piotr Zięba", "Piotr Zięba", "planeta-budowlana.pl")
]

def clean_name(name):
    # Remove middle names or suffixes like Jr.
    parts = name.split()
    if len(parts) >= 2:
        return parts[0].lower(), parts[-1].lower()
    return parts[0].lower(), ""

def generate_emails(first, last, domain):
    # standard corporate formats
    if domain in ["gmail.com", "outlook.com", "gmx.de", "o2.pl"]:
        return [] # Don't guess for public domains
    
    first = re.sub(r'[^a-z]', '', first)
    last = re.sub(r'[^a-z]', '', last)
    
    return [
        f"{first}.{last}@{domain}",
        f"{first}@{domain}",
        f"{first[0]}{last}@{domain}"
    ]

MASTER = "/Users/alt/Desktop/starr/favour/wagner_distributors_3col.csv"

# Write out the generated strict personal emails
with open(MASTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for company, name, domain in companies_data:
        first, last = clean_name(name)
        emails = generate_emails(first, last, domain)
        if emails:
            # Pick the first.last format as primary guess for corporate
            primary_email = emails[0]
            writer.writerow([company, name, primary_email])

print("Re-appended list with strict personal email formats.")
