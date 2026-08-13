import imaplib
import email
import re
from collections import Counter
import time

HOSTINGER_EMAIL = "dan.thompson@edwardfiresafety.com"
HOSTINGER_PASSWORD = "@Echelon99"
IMAP_SERVER = "imap.hostinger.com"
SENT_FOLDER = "INBOX.Sent"

all_emails = []

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
                                all_emails.append(match.group(0).lower())
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

counts = Counter(all_emails)
duplicates = {email: count for email, count in counts.items() if count > 1}

print(f'\nFinal Duplicate Audit:')
print(f'Total UNIQUE people messaged: {len(counts)}')
print(f'Total people who got MORE THAN 1 email: {len(duplicates)}')
for email, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'  - {email}: received {count} times')
if len(duplicates) > 10:
    print(f'  ... and {len(duplicates) - 10} more')
