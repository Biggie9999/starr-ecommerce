#!/usr/bin/env python3
"""Append new MX-verified Stark Elektromotoren leads."""

import csv, dns.resolver, os, sys

MASTER = "/Users/alt/Desktop/starr/favour/stark_distributors_3col.csv"

# ---- New candidate leads ----
NEW_LEADS = [
    ("STERNET sp. z o.o.", "Paweł Zięba", "pawel.zieba@sternet.pl"),
    ("STERNET sp. z o.o.", "Paweł Zięba", "info@sternet.pl"),
    ("CHAU THIEN CHI CO., LTD", "Tri Pham", "tri.pham@chauthienchi.com"),
    ("mk-elektromotoren ag", "Mahmut Karademir", "info@mk-elektromotoren.ch"),
]

def mx_ok(email: str) -> bool:
    """Return True if the domain has at least one MX record."""
    domain = email.split("@")[1]
    res = dns.resolver.Resolver()
    res.nameservers = ["8.8.8.8", "1.1.1.1"]
    res.lifetime = res.timeout = 3
    try:
        answers = res.resolve(domain, "MX")
        return len(answers) > 0
    except Exception:
        return False

# Initialize master file if it doesn't exist
if not os.path.exists(MASTER):
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Company", "Name", "Email"])

# Load existing emails to avoid duplicates
existing_emails = set()
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
        print(f"  ✅  {company} | {email}")
    else:
        failed += 1
        print(f"  ❌  MX FAIL  {email}")

print(f"\n--- Done: {added} added, {failed} MX-failed ---")

# Count total
with open(MASTER, newline="", encoding="utf-8-sig") as f:
    total = sum(1 for row in csv.reader(f) if len(row) >= 3) - 1  # minus header
print(f"Grand total Stark leads: {total}")
