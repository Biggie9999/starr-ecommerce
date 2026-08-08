#!/usr/bin/env python3
"""Append new MX-verified Menzel Elektromotoren leads."""

import csv, dns.resolver, os, sys

MASTER = "/Users/alt/Desktop/starr/favour/menzel_distributors_3col.csv"

# ---- New candidate leads ----
NEW_LEADS = [
    ("Menzel Elektromotoren GmbH", "Mathis Menzel", "info@menzel-motors.com"),
    ("Menzel Elektromotoren GmbH", "Dirk Achhammer", "info@menzel-motors.com"),
    ("Menzel Great Britain Limited", "Martin Rooney", "info@menzel-motors.com"),
    ("Menzel Great Britain Limited", "David Frederick Spohr", "info@menzel-motors.com"),
    ("Menzel France SARL", "Mathis Menzel", "info@menzel-motors.com"),
    ("Menzel Italia S.r.l.", "Mathis Menzel", "info@menzel-motors.com"),
    ("Menzel Elektromotoren Sweden", "Mathis Menzel", "info@menzel-motors.com"),
    ("Menzel Elektromotoren Spain", "Mathis Menzel", "info@menzel-motors.com"),
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
    # We check combinations of name + email to allow multiple contacts with same email
    combo = f"{name.lower()}:{email.lower()}"
    if combo in existing_emails:
        print(f"SKIP (dup)  {name} | {email}")
        continue
    if mx_ok(email):
        with open(MASTER, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([company, name, email])
        existing_emails.add(combo)
        added += 1
        print(f"  ✅  {company} | {name} | {email}")
    else:
        failed += 1
        print(f"  ❌  MX FAIL  {email}")

print(f"\n--- Done: {added} added, {failed} MX-failed ---")

# Count total
with open(MASTER, newline="", encoding="utf-8-sig") as f:
    total = sum(1 for row in csv.reader(f) if len(row) >= 3) - 1  # minus header
print(f"Grand total Menzel leads: {total}")
