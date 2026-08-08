#!/usr/bin/env python3
"""Append Americas Scanner (Round 3) MX-verified WAGNER Group leads."""

import csv, dns.resolver, os

MASTER = "/Users/alt/Desktop/starr/favour/wagner_distributors_3col.csv"

# ---- New candidate leads ----
NEW_LEADS = [
    ("Spray-Quip, Inc.", "Herbert Chilman Jr.", "sales@sprayquip.com"),
    ("South Texas Spray Equipment Rental & Repair, LLC", "George Ferrie", "chris@southtexassprayequipment.com"),
    ("Bolair Fluid Handling Systems", "Gregory Haddow", "sales@bolair.ca"),
    ("Pumpworks Services Ltd.", "Randy Nault", "sales@pumpworks.ca"),
    ("Coast Industrial Systems, Inc.", "Larry Onstott", "sales@coastisi.com"),
    ("Myers Service & Distribution, Inc.", "Stephen Myers", "info@sprayequipmentcharlottenc.com"),
    ("Pneu-Mech Systems Mfg., Inc.", "Jim Andrews", "info@pneu-mech.com"),
    ("Ag Spray Equipment", "Mark Schwarz", "sales@agspray.com"),
    ("Fournier Rubber & Supply Co.", "Dennis Davidson", "info@fournierrubber.com"),
    ("Precision Finishing, Inc.", "Jeffrey Bell", "jeffrey@precisionfinishinginc.com"),
    ("Midwest Finishing Systems, Inc.", "Russ Green", "sales@midwestfinishing.com"),
    ("Tencarva Machinery Company", "Henry Ritchie", "info@tencarva.com"),
    ("Pro-Tek Spray Equipment", "Patrice Richer", "info@pro-teksprayequipment.com"),
    ("Koehler Rubber & Supply Co. (TCH Koehler LLC)", "Bernie Green", "info@koehlerrubber.com"),
    ("Southern Fluid Systems", "Salleigh Grubbs", "info@southernfluidsystems.com")
]

def mx_ok(email: str) -> bool:
    """Return True if the domain has at least one MX record."""
    try:
        domain = email.split("@")[1]
        res = dns.resolver.Resolver()
        res.nameservers = ["8.8.8.8", "1.1.1.1"]
        res.lifetime = res.timeout = 3
        answers = res.resolve(domain, "MX")
        return len(answers) > 0
    except Exception:
        return False

# Load existing emails to avoid duplicates
existing_emails = set()
if os.path.exists(MASTER):
    with open(MASTER, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if len(row) >= 3:
                existing_emails.add(row[2].strip().lower())

added = 0
failed = 0
for company, name, email in NEW_LEADS:
    if email.lower() in existing_emails:
        print(f"SKIP (dup)  {email}")
        continue
    if mx_ok(email):
        with open(MASTER, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([company, name, email])
        existing_emails.add(email.lower())
        added += 1
        print(f"  ✅  {company} | {name} | {email}")
    else:
        failed += 1
        print(f"  ❌  MX FAIL  {email}")

print(f"\n--- Done: {added} added, {failed} MX-failed ---")

# Count total
with open(MASTER, newline="", encoding="utf-8-sig") as f:
    total = sum(1 for row in csv.reader(f) if len(row) >= 3) - 1  # minus header
print(f"Grand total Wagner leads: {total}")
