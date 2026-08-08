#!/usr/bin/env python3
import csv

MASTER = "/Users/alt/Desktop/starr/favour/wagner_osint_verified_leads.csv"

# ---- New OSINT candidate leads (Final Batch) ----
NEW_LEADS = [
    ("Cetec Industrial", "Eduardo Cernic", "eduardo@cetecindustrial.com.br", "https://www.cetecindustrial.com.br"),
    ("Casa do Construtor", "Altino Cristofoletti", "altino@casadoconstrutor.com.br", "https://www.abf.com.br"),
    ("Bolair Fluid Handling Systems", "Gregory Haddow", "ghaddow@bolair.ca", "https://www.cufca.net"),
    ("Coast Industrial Systems Inc.", "Larry Onstott", "larry@coastisi.com", "https://www.coastisi.com")
]

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in NEW_LEADS:
        writer.writerow(row)

print("Appended 4 final premium OSINT leads.")
