#!/usr/bin/env python3
import csv

MASTER = "/Users/alt/Desktop/starr/favour/wagner_osint_verified_leads.csv"

NEW_LEADS = [
    ("J. Wagner Asia Pte. Ltd.", "Frederic Biondi", "frederic.biondi@wagner-group.com", "https://prospeo.io/email-finder/wagner-group.com/j-wagner-asia-pte-ltd")
]

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in NEW_LEADS:
        writer.writerow(row)

print("Appended 1 APAC OSINT lead.")
