import os
import sys
import csv
import time
import random
from send_hostinger import send_hostinger_email

def send_campaign(csv_file, template_html_path):
    if not os.path.exists(csv_file):
        print(f"Error: Could not find {csv_file}")
        return
        
    with open(template_html_path, 'r', encoding='utf-8') as f:
        base_template = f.read()
        
    success_count = 0
    with open(csv_file, 'r', encoding='utf-8') as f:
        # Assuming format: Company, CEO Name, Email, ...
        # If it has a header, we might want to skip it, but let's check the first row
        reader = csv.reader(f)
        rows = list(reader)
        
    if rows and rows[0][0].lower() == 'company':
        rows = rows[1:] # skip header
        
    print(f"Loaded {len(rows)} leads. Starting campaign...")
    
    for row in rows:
        if len(row) < 3:
            continue
            
        company = row[0].strip()
        full_name = row[1].strip()
        email = row[2].strip()
        
        if not email or email.lower() == 'n/a':
            # Fallback to generic email if present
            if len(row) >= 4 and row[3].strip() and row[3].strip().lower() != 'n/a':
                email = row[3].strip()
            else:
                print(f"Skipping {company} - no valid email.")
                continue
                
        # 1. Validate the name - Skip if it's missing or generic
        generic_names = ['n/a', 'unknown', 'team', 'executive', 'management', 'info', 'sales', 'director', 'manager']
        if not full_name or any(gen in full_name.lower().split() for gen in generic_names):
            print(f"Skipping {company} - generic or missing name: '{full_name}'")
            continue
            
        first_name = full_name.split()[0]
        
        # 2. Personalize Subject
        subject = f"Procurement Proposal for {company}"
        
        # 2. Personalize Body
        # The base_template expects [Name] and [Company] to be replaced
        # Wait, the user wants a specific body. We will inject it into the HTML template.
        
        custom_body = f"""<p>Hello {first_name},</p>
<p>I hope you are doing well.</p>
<p>Dorner Conveyors has a proposal for a partnership on a procurement project that I want you to attend to as soon as possible.</p>
<p>A reply at your earliest convenience would be much appreciated.</p>"""

        # Replace the placeholder in the template with our custom body
        # Let's assume the template has a generic <p>Hello [Name]...</p> that we can replace.
        # It's safer to just split the template at the signature and prepend the custom body.
        
        # The signature starts at <div style="font-family: Arial
        sig_split = base_template.find('<div style="font-family: Arial')
        if sig_split != -1:
            final_html = custom_body + base_template[sig_split:]
        else:
            final_html = custom_body + base_template
            
        print(f"[{success_count+1}/{len(rows)}] Sending to {first_name} at {company} ({email})...")
        
        # 3. Send Email
        success = send_hostinger_email(email, subject, final_html)
        if success:
            success_count += 1
            
        # 4. Wait to avoid spam filters (increased slightly to avoid blocks)
        delay = random.randint(5, 10)
        print(f"Waiting {delay} seconds before next email...\n")
        time.sleep(delay)
        
    print(f"\nCampaign Complete! Sent {success_count} emails successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_bodine_campaign.py leads.csv")
    else:
        send_campaign(sys.argv[1], "dorner_email_template.html")
