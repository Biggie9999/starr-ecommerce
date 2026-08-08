#!/usr/bin/env python3
import csv

MASTER = "/Users/alt/Desktop/starr/favour/wagner_osint_verified_leads.csv"

# ---- New OSINT candidate leads ----
NEW_LEADS = [
    ("Pneu-Mech Systems Mfg. Inc.", "Jim Andrews", "jandrews@pneu-mech.com", "https://www.finishingandcoating.com"),
    ("Ag Spray Equipment", "Mark Schwarz", "mark.schwarz@agspray.com", "https://issuu.com"),
    ("Precision Finishing Inc.", "Jeffrey Bell", "jeffrey@precisionfinishinginc.com", "https://www.mpif.org"),
    ("Midwest Finishing Systems Inc.", "Russ Green", "russ.green@midwestfinishing.com", "https://www.facebook.com"),
    ("Tencarva Machinery Company", "Henry Ritchie", "hritchie@tencarva.com", "https://www.tencarva.com"),
    ("Southern Fluid Systems", "Salleigh Grubbs", "sgrubbs@southernfluidsystems.com", "https://www.southernfluidsystems.com"),
    ("Equipos y Sistemas Carlos Cano S.L.", "Carlos Cano", "carlos@sistemascano.es", "http://sistemascano.es")
]

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in NEW_LEADS:
        writer.writerow(row)

print("Appended 7 premium OSINT leads.")
