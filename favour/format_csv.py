import csv

def main():
    input_file = 'ultimate_vacumax_reps.csv'
    output_file = 'final_vacumax_reps.csv'
    
    with open(input_file, encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        
    print(f"Formatting {len(reader)} Vac-U-Max records...")
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Contact Name', 'Company Name', 'Email Address'])
        writer.writeheader()
        
        written = 0
        for row in reader:
            contact_name = row.get('CEO_Name', '').strip()
            company_name = row.get('DistributorName', '').strip()
            email_address = row.get('CEO_Email_Ultimate', '').strip()
            
            if email_address:
                writer.writerow({
                    'Contact Name': contact_name,
                    'Company Name': company_name,
                    'Email Address': email_address
                })
                written += 1
                
    print(f"Successfully wrote {written} formatted records to {output_file}!")

if __name__ == "__main__":
    main()
