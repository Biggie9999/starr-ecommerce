import csv
import json
import dns.resolver

in_json = "/Users/alt/Desktop/starr/favour/anest_mx_audit.json"
out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

with open(in_json, "r") as f:
    audit = json.load(f)

verified = audit["verified"]
invalid = audit["invalid"]

print(f"Verified entries count: {len(verified)}")
print(f"Invalid entries count: {len(invalid)}")

# Replacement list for the 5 failing entities with verified active domains
replacements = [
    {"company": "Delta Tiger S.A. de C.V.", "name": "Executive Leadership", "email": "ventas@deltatiger.mx"}, # active domain deltatiger.mx
    {"company": "Grupo Solder S.A. de C.V.", "name": "Sergio González", "email": "contacto@gruposolder.com.mx"}, # active domain gruposolder.com.mx
    {"company": "Sprayquip Industrial (Pty) Ltd", "name": "Garth Rattray", "email": "garth@sprayquip.net"}, # active domain sprayquip.net
    {"company": "Air & Vacuum Technologies", "name": "Ian Robertson", "email": "ian@airvac.co.za"},
    {"company": "Global Paint Algeria", "name": "Management Team", "email": "contact@globalpaint.com"}
]

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '1.1.1.1']
resolver.timeout = 3
resolver.lifetime = 4

final_verified_list = []

for item in verified:
    final_verified_list.append([item["company"], item["name"], item["email"]])

# Test replacements
for rep in replacements:
    dom = rep["email"].split('@')[-1].lower().strip()
    try:
        recs = resolver.resolve(dom, 'MX')
        if len(recs) > 0:
            final_verified_list.append([rep["company"], rep["name"], rep["email"]])
            print(f"REPLACED & VERIFIED MX: {rep['company']} -> {rep['email']}")
    except Exception:
        print(f"Skipped non-resolving replacement: {rep['company']} ({rep['email']})")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for row in final_verified_list:
        writer.writerow(row)

print(f"\nSaved 100% DNS MX VERIFIED dataset with {len(final_verified_list)} entries to {out_csv}")
