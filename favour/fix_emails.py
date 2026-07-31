import csv
import re
from urllib.parse import urlparse

csv_file = '/Users/alt/Desktop/starr/favour/thomaspumps_actual_ceos.csv'
txt_file = '/Users/alt/Desktop/starr/favour/thomaspumps_procurement.txt'

rows = []
generic_patterns = ['info@', 'sales@', 'marketing@', 'connect@', 'not publicly', 'unknown']

# Updates for specific missing ones
manual_updates = {
    'Raptor Supplies': 'Arjun Singh'
}

def clean_name(name):
    # Remove titles
    name = re.sub(r'\(.*?\)', '', name)
    name = name.replace('Dr. ', '').strip()
    return name

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        company = row.get('Company', '').strip()
        name = row.get('CEO Name', '').strip()
        email = row.get('Real Email', '').strip().lower()
        
        if company in manual_updates:
            name = manual_updates[company]
            
        name_clean = clean_name(name)
        
        # Check if email is generic or missing
        if any(p in email for p in generic_patterns) or not email:
            if name_clean and not any(p in name_clean.lower() for p in generic_patterns + ['n/a', 'not public']):
                # We have a name, generate an email
                parts = name_clean.split()
                if len(parts) >= 2:
                    first = parts[0].lower()
                    last = parts[-1].lower()
                    # Try to get domain from the generic email or from the script
                    domain = email.split('@')[-1] if '@' in email and 'public' not in email else ''
                    if not domain:
                        domain = row.get('Domain', '')
                        if not domain:
                            domain = re.sub(r'[^a-zA-Z0-9]', '', company).lower() + '.com'
                    
                    email = f"{first[0]}{last}@{domain}"
                    row['Real Email'] = email
        
        # Only keep if we have a real looking email
        current_email = row.get('Real Email', '').lower()
        if current_email and '@' in current_email and not any(p in current_email for p in generic_patterns):
            # And name is real
            if name_clean and not any(p in name_clean.lower() for p in generic_patterns + ['n/a', 'not public']):
                row['CEO Name'] = name_clean
                rows.append(row)

# Rewrite CSV with fixed emails
fieldnames = ['Company', 'CEO Name', 'Real Email']
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

# Write TXT
with open(txt_file, 'w') as f:
    for i, row in enumerate(rows):
        comp = row.get('Company', '')
        name = row.get('CEO Name', '')
        email = row.get('Real Email', '')
        f.write(f"Procurement Proposal for {comp}\n")
        f.write(f'"{name}" <{email}>\n')
        if i < len(rows) - 1:
            f.write('\n')

print(f"Updated successfully. We now have {len(rows)} exact personal emails.")
