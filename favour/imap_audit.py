import imaplib
import email
import re
import csv
import ssl
import time

HOSTINGER_EMAIL = "dan.thompson@edwardfiresafety.com"
HOSTINGER_PASSWORD = "@Echelon99"
IMAP_SERVER = "imap.hostinger.com"
SENT_FOLDER = "INBOX.Sent"

sent_emails = set()

def fetch_emails():
    print("Connecting to Hostinger IMAP...")
    imap = imaplib.IMAP4_SSL(IMAP_SERVER, 993)
    imap.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
    
    imap.select(f'"{SENT_FOLDER}"')
    status, data = imap.search(None, "ALL")
    
    if status != "OK" or not data[0]:
        print("No emails found.")
        return
        
    nums = data[0].split()
    total = len(nums)
    print(f"Total emails in {SENT_FOLDER} to process: {total}")
    
    # Process in chunks of 50 to avoid big SSL disconnects
    chunk_size = 50
    for i in range(0, total, chunk_size):
        chunk = nums[i:i+chunk_size]
        msg_nums = b','.join(chunk)
        
        retries = 3
        while retries > 0:
            try:
                typ, msg_data = imap.fetch(msg_nums, '(BODY.PEEK[HEADER.FIELDS (TO)])')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        to_header = msg.get("To", "")
                        if to_header:
                            match = re.search(r'[\w\.-]+@[\w\.-]+', to_header)
                            if match:
                                sent_emails.add(match.group(0).lower())
                break # Success for this chunk
            except Exception as e:
                print(f"Error fetching chunk: {e}. Retrying...")
                retries -= 1
                time.sleep(2)
                try:
                    imap.close()
                    imap.logout()
                except:
                    pass
                imap = imaplib.IMAP4_SSL(IMAP_SERVER, 993)
                imap.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
                imap.select(f'"{SENT_FOLDER}"')

    imap.close()
    imap.logout()

fetch_emails()

print(f"Successfully extracted {len(sent_emails)} UNIQUE emails from the actual Hostinger Sent folder.")

# Filter the CSV
unique_leads = {}
with open('/Users/alt/Desktop/starr/favour/final_edwards_distributors_fixed.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        em = row['Email Address'].strip().lower()
        if em not in unique_leads:
            unique_leads[em] = row

remaining = []
for em, row in unique_leads.items():
    if em not in sent_emails:
        remaining.append(row)

with open('/Users/alt/Desktop/starr/favour/final_edwards_distributors_verified_remaining.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Company Name', 'Contact Name', 'Email Address'])
    writer.writeheader()
    writer.writerows(remaining)

print(f'Total uniquely extracted leads from original CSV: {len(unique_leads)}')
print(f'Remaining entirely untouched, verified unique leads: {len(remaining)}')
