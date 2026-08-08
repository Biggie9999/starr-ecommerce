import os
import sys
import smtplib
import imaplib
import time
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re

# ==========================================
# Hostinger Configuration
# Set these or pass as environment variables
# ==========================================
HOSTINGER_EMAIL = os.environ.get("HOSTINGER_EMAIL", "your-email@yourdomain.com")
HOSTINGER_PASSWORD = os.environ.get("HOSTINGER_PASSWORD", "your_password")

SMTP_SERVER = "smtp.hostinger.com"
SMTP_PORT = 465  # SSL

IMAP_SERVER = "imap.hostinger.com"
IMAP_PORT = 993  # SSL

def send_hostinger_email(to_email, subject, body_text):
    if HOSTINGER_EMAIL == "your-email@yourdomain.com" or HOSTINGER_PASSWORD == "your_password":
        print("❌ Error: Please set your HOSTINGER_EMAIL and HOSTINGER_PASSWORD in the script or environment variables.")
        return False

    # 1. Create email message
    msg = MIMEMultipart('related')
    msg["From"] = HOSTINGER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg["Date"] = email.utils.formatdate(localtime=True)
    
    msg_alt = MIMEMultipart('alternative')
    msg.attach(msg_alt)
    # Changed from plain to html to support your new signature
    msg_alt.attach(MIMEText(body_text, "html"))
    
    # Extract CID images from HTML body and attach them
    cid_matches = re.findall(r'src=["\']cid:([^"\']+)["\']', body_text)
    for cid_file in set(cid_matches):
        if os.path.exists(cid_file):
            with open(cid_file, 'rb') as img_file:
                img_data = img_file.read()
                # Create image with a professional branded name
                display_name = os.path.basename(cid_file)
                image = MIMEImage(img_data, name=display_name)
                image.add_header('Content-ID', f'<{cid_file}>')
                image.add_header('Content-Disposition', 'inline', filename=display_name)
                msg.attach(image)
        else:
            print(f"⚠️ Warning: Referenced image '{cid_file}' not found locally.")

    # 2. Send via Hostinger SMTP
    try:
        print(f"Connecting to {SMTP_SERVER}:{SMTP_PORT} via SSL...")
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email successfully sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email via SMTP: {e}")
        return False

    # 3. Save copy to Hostinger Webmail 'Sent' folder via IMAP
    try:
        print(f"Syncing copy to Hostinger Webmail 'Sent' folder via IMAP ({IMAP_SERVER})...")
        with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) as imap:
            imap.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
            
            # Try common Sent folder names for Hostinger/Titan
            sent_folders_to_try = ["Sent", "INBOX.Sent", "\"Sent Items\"", "\"Sent Messages\""]
            success = False
            for folder in sent_folders_to_try:
                try:
                    res, _ = imap.append(
                        folder,
                        "\\Seen",
                        imaplib.Time2Internaldate(time.time()),
                        msg.as_bytes()
                    )
                    if res == "OK":
                        success = True
                        print(f"✅ Saved to Hostinger {folder} folder! It will now appear in your Webmail.")
                        break
                except Exception:
                    continue
            
            if not success:
                print("⚠️ Could not find the correct 'Sent' folder. Available folders are:")
                typ, folders = imap.list()
                if typ == 'OK':
                    for f in folders:
                        print("  " + f.decode())
                
        return True
    except Exception as e:
        print(f"⚠️ Sent via SMTP, but could not save to Hostinger IMAP Sent folder: {e}")
        return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        recipient = sys.argv[1]
        subj = sys.argv[2] if len(sys.argv) > 2 else "Test Email"
        body_arg = sys.argv[3] if len(sys.argv) > 3 else "Hello, this is a test email sent via Hostinger SMTP."
        
        # If the user passed an HTML file instead of a raw string, read from the file
        if body_arg.endswith('.html') and os.path.exists(body_arg):
            with open(body_arg, 'r', encoding='utf-8') as f:
                body = f.read()
        else:
            body = body_arg
            
        send_hostinger_email(recipient, subj, body)
    else:
        print("Usage:")
        print("  python3 send_hostinger.py recipient@example.com 'Subject' 'Email Body String'")
        print("OR")
        print("  python3 send_hostinger.py recipient@example.com 'Subject' body_template.html")
