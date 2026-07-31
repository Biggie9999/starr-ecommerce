import csv

input_file = '/Users/alt/Desktop/starr/favour/thomaspumps_actual_ceos.csv'
output_file = '/Users/alt/Desktop/starr/favour/thomaspumps_procurement.txt'

entries = []

with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        company = row.get('Company', '').strip()
        ceo_name = row.get('CEO Name', '').strip()
        email = row.get('Real Email', '').strip()
        
        # In case the column is called 'CEO/Contact Name'
        if not ceo_name and 'CEO/Contact Name' in row:
            ceo_name = row['CEO/Contact Name'].strip()
            
        if not ceo_name or ceo_name.lower() == 'not publicly listed' or ceo_name.lower() == 'unknown':
            ceo_name = "General Contact"
            
        entries.append((company, ceo_name, email))

with open(output_file, 'w') as f:
    for i, (comp, name, email) in enumerate(entries):
        f.write(f"Procurement Proposal for {comp}\n")
        f.write(f'"{name}" <{email}>\n')
        if i < len(entries) - 1:
            f.write('\n')

print(f"Successfully generated {len(entries)} proposals to {output_file}")
