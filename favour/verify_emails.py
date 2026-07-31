import re
import smtplib
import socket
import dns.resolver

file_path = '/Users/alt/Desktop/starr/favour/thomaspumps_procurement.txt'

with open(file_path, 'r') as f:
    lines = f.read().split('\n')

blocks = []
for i in range(0, len(lines), 3):
    if i+1 < len(lines):
        blocks.append((lines[i], lines[i+1]))

print(f"Found {len(blocks)} emails to verify.")

def verify_email(email):
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = sorted(records, key=lambda rec: rec.preference)[0].exchange.to_text()
        
        server = smtplib.SMTP(timeout=3)
        server.set_debuglevel(0)
        server.connect(mx_record, 25)
        server.ehlo_or_helo_if_needed()
        server.mail('hello@example.com')
        code, message = server.rcpt(str(email))
        server.quit()
        
        if code == 250 or code == 251 or code == 252:
            return True, "Valid"
        else:
            return False, f"SMTP {code}"
    except Exception as e:
        return False, str(e.__class__.__name__)

valid_blocks = []
for title, email_line in blocks:
    match = re.search(r'<([^>]+)>', email_line)
    if match:
        email = match.group(1)
        is_valid, msg = verify_email(email)
        print(f"{email}: {'Valid' if is_valid else 'Invalid'} ({msg})")
        if is_valid or msg == "Valid": 
            valid_blocks.append((title, email_line))

print(f"\nVerification complete. {len(valid_blocks)} valid emails.")

with open('/Users/alt/Desktop/starr/favour/thomaspumps_procurement_verified.txt', 'w') as f:
    for i, (title, email_line) in enumerate(valid_blocks):
        f.write(f"{title}\n{email_line}\n")
        if i < len(valid_blocks) - 1:
            f.write("\n")
