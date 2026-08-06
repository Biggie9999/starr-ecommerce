import os
import re

def get_companies_with_generic_emails():
    companies = []
    generic_patterns = ['info@', 'sales@', 'contact@', 'office@', 'hello@', 'admin@']
    
    # Check all procurement txt files
    for filename in os.listdir('.'):
        if filename.endswith('procurement.txt') or filename.endswith('procurement_master.txt') or filename.endswith('verified.txt') or filename.endswith('proposals.txt'):
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if lines[i].startswith('Procurement Proposal for'):
                        company_name = lines[i].replace('Procurement Proposal for ', '').strip()
                        if i + 1 < len(lines):
                            email_line = lines[i+1].strip()
                            if any(gen in email_line.lower() for gen in generic_patterns):
                                # It's a generic email
                                email_match = re.search(r'<(.+?)>', email_line)
                                if email_match:
                                    email = email_match.group(1)
                                    companies.append({
                                        'company': company_name,
                                        'generic_email': email,
                                        'file': filename
                                    })
    return companies

companies = get_companies_with_generic_emails()
seen = set()
unique_comps = []
for c in companies:
    if c['company'] not in seen:
        seen.add(c['company'])
        unique_comps.append(c)

for i, c in enumerate(unique_comps):
    print(f"{i+1}. {c['company']} ({c['generic_email']})")
