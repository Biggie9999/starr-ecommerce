import csv

input_file = "/Users/alt/Desktop/starr/favour/wagner_distributors_3col.csv"
output_file = "/Users/alt/Desktop/starr/favour/wagner_distributors_3col_cleaned.csv"

generic_prefixes = [
    "info@", "sales@", "contact@", "orders@", "admin@", 
    "customer-service@", "sac@", "handlowy@", "sprzedaz@", 
    "biuro@", "enquiries@", "mail@", "servicespezi@", 
    "commercial@", "contato@", "cetec@", "indspray@", 
    "bart-biuro@", "customer@"
]

valid_rows = []
removed_count = 0

with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    valid_rows.append(header)
    
    for row in reader:
        if len(row) >= 3:
            email = row[2].strip().lower()
            is_generic = False
            for prefix in generic_prefixes:
                if email.startswith(prefix):
                    is_generic = True
                    break
            
            if not is_generic:
                valid_rows.append(row)
            else:
                removed_count += 1

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(valid_rows)

print(f"Removed {removed_count} generic emails. Saved {len(valid_rows) - 1} valid personal emails.")

# Replace old file with cleaned one
import os
os.replace(output_file, input_file)
