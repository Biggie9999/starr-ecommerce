#!/usr/bin/env python3
import csv
import smtplib
import dns.resolver
import socket

input_file = "/Users/alt/Desktop/starr/favour/wagner_distributors_3col.csv"
verified_file = "/Users/alt/Desktop/starr/favour/wagner_distributors_3col_verified.csv"

def get_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        # get the highest priority MX record
        mx_record = sorted(answers, key=lambda x: x.preference)[0].exchange.to_text()
        return mx_record
    except Exception:
        return None

def verify_email(email):
    domain = email.split('@')[1]
    mx_record = get_mx_record(domain)
    
    if not mx_record:
        return False, "No MX"
        
    try:
        # SMTP lib setup
        server = smtplib.SMTP(timeout=3)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('hello@google.com')
        code, message = server.rcpt(str(email))
        server.quit()

        # 250 means OK, 251 means forwarding. Both are valid.
        if code == 250 or code == 251:
            return True, "Valid"
        else:
            return False, f"SMTP {code}"
            
    except Exception as e:
        # If it times out or blocks, we can't definitively verify it
        return False, str(e)

verified_rows = []
failed_rows = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 3:
            # Skip header
            if row[0].lower() == 'company name' or row[0].lower() == 'company':
                verified_rows.append(row)
                continue
                
            email = row[2].strip()
            print(f"Checking {email}...")
            is_valid, msg = verify_email(email)
            if is_valid:
                print(f"  ✅ VERIFIED")
                verified_rows.append(row)
            else:
                print(f"  ❌ FAILED ({msg})")
                failed_rows.append(row)

with open(verified_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(verified_rows)

print(f"\nCompleted! {len(verified_rows)} strictly verified personal emails saved. {len(failed_rows)} rejected.")
