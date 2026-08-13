import csv
import sys
import time
import random
import os
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOSTINGER_EMAIL = "Matthijs.Vader@victron-energies.com"
HOSTINGER_PASSWORD = "@Echelon99"
HOSTINGER_SENDER_NAME = "Matthijs Vader"
SMTP_SERVER = "smtp.hostinger.com"
SMTP_PORT = 465

def send_hostinger_email(to_email, subject, body_text):
    msg = MIMEMultipart('related')
    msg["From"] = email.utils.formataddr((HOSTINGER_SENDER_NAME, HOSTINGER_EMAIL))
    msg["To"] = to_email
    msg["Subject"] = subject
    msg["Date"] = email.utils.formatdate(localtime=True)
    msg["Message-ID"] = email.utils.make_msgid(domain="victron-energies.com")
    
    msg_alt = MIMEMultipart('alternative')
    msg.attach(msg_alt)
    
    msg_alt.attach(MIMEText("Please enable HTML to view this email.", "plain", "utf-8"))
    msg_alt.attach(MIMEText(body_text, "html", "utf-8"))
    
    from email.mime.image import MIMEImage
    img_path = "victronenergy_logo.png"
    if os.path.exists(img_path):
        with open(img_path, 'rb') as img_file:
            img_data = img_file.read()
            image = MIMEImage(img_data, name="victronenergy_logo.png")
            image.add_header('Content-ID', '<victronenergy_logo.png>')
            image.add_header('Content-Disposition', 'inline', filename="victronenergy_logo.png")
            msg.attach(image)
    
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=60)
        server.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()
        
        # Append to IMAP Sent folder
        import imaplib
        try:
            imap_server = imaplib.IMAP4_SSL("imap.hostinger.com", 993)
            imap_server.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
            imap_server.append('\"INBOX.Sent\"', None, imaplib.Time2Internaldate(time.time()), msg.as_bytes())
            imap_server.logout()
        except Exception as imap_e:
            print(f"Warning: Could not save to Sent folder: {imap_e}")
            
        return True
    except Exception as e:
        print(f"❌ Failed to send email via SMTP: {e}")
        return False

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
    
    print(f"Starting Victron Energy campaign to {total_leads} leads...")
    print("-" * 50)
    
    for i, row in enumerate(rows, 1):
        email_addr = row.get("CEO Email", "").strip()
        full_name = row.get("CEO Name", "").strip()
        company = row.get("Company Name", "").strip()
        
        if not email_addr:
            print(f"[{i}/{total_leads}] Skipping row (No email)")
            continue
            
        first_name = full_name.split()[0] if full_name and full_name.lower() != 'purchasing manager' else "there"
        
        subject = f"Procurement Proposal for {company}"
        
        custom_body = f"""
    <p>Hello {first_name},</p>
    <p>I hope you are doing well.</p>
    <p>Victron Energy has a proposal for a partnership on a procurement project that I want you to attend to as soon as possible.</p>
    <p>A reply at your earliest convenience would be much appreciated.</p>
"""
        final_html = base_template.replace("<!-- BODY_PLACEHOLDER -->", custom_body)
            
        print(f"[{i}/{total_leads}] Sending to {full_name} at {company} ({email_addr})...")
        
        formatted_email = f'"{full_name}" <{email_addr}>'
        success = send_hostinger_email(formatted_email, subject, final_html)
        if success:
            success_count += 1
            
        delay = random.randint(1, 3)
        print(f"Waiting {delay} seconds before next email...\n")
        time.sleep(delay)
        
    print(f"\nCampaign Complete! Sent {success_count} emails successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_victronenergy_campaign.py leads.csv")
    else:
        send_campaign(sys.argv[1], "victronenergy_email_template.html")
