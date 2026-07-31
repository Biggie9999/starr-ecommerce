import csv
import re

def generate_domain(company_name):
    # Remove common suffixes
    name = re.sub(r'\b(Inc\.|Inc|Corp\.|Corp|LLC|Ltd\.|Ltd|Company|Co\.|Co)\b', '', company_name, flags=re.IGNORECASE)
    # Remove special characters and spaces
    domain = re.sub(r'[^a-zA-Z0-9]', '', name).lower()
    return f"{domain}.com"

def main():
    dealers_file = '/Users/alt/Desktop/starr/favour/thomaspumps_dealers.csv'
    output_file = '/Users/alt/Desktop/starr/favour/thomaspumps_ceo_emails.csv'
    
    companies = []
    with open(dealers_file, 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            if row and row[0].strip():
                companies.append(row[0].strip())
                
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Company', 'CEO/Contact Name', 'Estimated Email', 'Domain', 'Source'])
        
        for comp in companies:
            domain = generate_domain(comp)
            # We'll use a standard format since automated search was blocked
            email = f"ceo@{domain}"
            writer.writerow([comp, 'CEO', email, domain, 'Generated based on company name'])
            
    print(f"Generated {len(companies)} emails to {output_file}")

if __name__ == "__main__":
    main()
