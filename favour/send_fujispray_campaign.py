import csv
import sys
import time
import random
import os
from send_hostinger import send_hostinger_email

def send_campaign(csv_file, template_file):
    if not os.path.exists(csv_file):
        print(f"Error: CSV file {csv_file} not found.")
        return
        
    if not os.path.exists(template_file):
        print(f"Error: Template file {template_file} not found.")
        return

    with open(template_file, 'r', encoding='utf-8') as f:
        base_template = f.read()

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    total_leads = len(rows)
    success_count = 0
    
    print(f"Starting Fuji Spray campaign to {total_leads} leads...")
    print("-" * 50)
    
    for i, row in enumerate(rows, 1):
        email = row.get("Email Address", "").strip()
        full_name = row.get("Contact Name", "").strip()
        company = row.get("Company Name", "").strip()
        
        if not email:
            print(f"[{i}/{total_leads}] Skipping row (No email)")
            continue
            
        first_name = full_name.split()[0] if full_name else "Purchasing Manager"
        
        # 1. Subject
        subject = f"Procurement Proposal for {company}"
        
        custom_body = f"""
    <p>Hello {first_name},</p>
    <p>I hope you are doing well.</p>
    <p>Fuji Spray has a proposal for a partnership on a procurement project that I want you to attend to as soon as possible.</p>
    <p>A reply at your earliest convenience would be much appreciated.</p>
"""
        final_html = base_template.replace("<!-- BODY_PLACEHOLDER -->", custom_body)
            
        print(f"[{i}/{total_leads}] Sending to {first_name} at {company} ({email})...")
        
        # 3. Send Email
        formatted_email = f'"{full_name}" <{email}>'
        success = send_hostinger_email(formatted_email, subject, final_html)
        if success:
            success_count += 1
            
        # 4. Wait to avoid spam filters
        delay = random.randint(5, 10)
        print(f"Waiting {delay} seconds before next email...\n")
        time.sleep(delay)
        
    print(f"\nCampaign Complete! Sent {success_count} emails successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_fujispray_campaign.py leads.csv")
    else:
        send_campaign(sys.argv[1], "fujispray_email_template.html")
