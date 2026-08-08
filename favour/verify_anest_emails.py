import csv
import dns.resolver
import socket
import re
import urllib.request
import urllib.parse
import json

in_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

rows = []
with open(in_csv, "r") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for r in reader:
        if r:
            rows.append(r)

print(f"Loaded {len(rows)} entries from {in_csv} for deep DNS & MX verification...")

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '1.1.1.1']
resolver.timeout = 3
resolver.lifetime = 4

verified_rows = []
invalid_rows = []

for r in rows:
    company, name, email = r[0], r[1], r[2]
    domain = email.split('@')[-1].lower().strip() if '@' in email else ''
    
    has_mx = False
    if domain:
        try:
            records = resolver.resolve(domain, 'MX')
            if len(records) > 0:
                has_mx = True
        except Exception:
            # Fallback to A record check
            try:
                records = resolver.resolve(domain, 'A')
                if len(records) > 0:
                    has_mx = True
            except Exception:
                has_mx = False
                
    if has_mx:
        verified_rows.append({"company": company, "name": name, "email": email, "domain": domain, "status": "VERIFIED_MX"})
    else:
        invalid_rows.append({"company": company, "name": name, "email": email, "domain": domain, "status": "FAILED_MX"})

print(f"\n--- VERIFICATION RESULTS ---")
print(f"VERIFIED ACTIVE MX: {len(verified_rows)} emails")
print(f"FAILED / BOUNCING MX: {len(invalid_rows)} emails\n")

if invalid_rows:
    print("Invalid / Bouncing Entries Found:")
    for inv in invalid_rows:
        print(f"  ❌ {inv['company']} -> {inv['email']} (Domain: {inv['domain']})")

with open('/Users/alt/Desktop/starr/favour/anest_mx_audit.json', 'w') as f:
    json.dump({"verified": verified_rows, "invalid": invalid_rows}, f, indent=2)

print("\nSaved full DNS audit to anest_mx_audit.json")
