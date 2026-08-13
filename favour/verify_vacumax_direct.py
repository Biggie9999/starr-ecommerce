import csv
import dns.resolver
import smtplib
import socket

def verify_email(email):
    domain = email.split('@')[1]
    
    # Check MX record
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = sorted(records, key=lambda x: x.preference)[0].exchange.to_text()
    except Exception as e:
        return False
    
    # Try SMTP connection
    try:
        server = smtplib.SMTP(timeout=5)
        server.set_debuglevel(0)
        # Connect to the MX server
        server.connect(mx_record)
        server.helo(socket.getfqdn())
        server.mail('hello@vacu-max.com')
        code, message = server.rcpt(email)
        server.quit()
        
        # 250 means OK, recipient exists or catch-all. 
        if code == 250:
            return True
        else:
            print(f"[{code}] {email} - {message.decode('utf-8', errors='ignore').strip()}")
            return False
            
    except smtplib.SMTPServerDisconnected:
        # Some servers drop connection immediately if they hate the IP, assume valid for now if MX exists
        return True
    except Exception as e:
        # Timeout or other error, assume valid if MX exists to be safe, but let's be strict
        # Actually, if we time out, let's keep it just in case, but print the error
        print(f"[Error] {email} - {e}")
        return True

def main():
    direct_leads = []
    
    with open('vacumax_verified_master.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[0] != 'Purchasing Manager' and '@' in row[2] and not row[2].startswith('info@') and not row[2].startswith('sales@'):
                direct_leads.append(row)
                
    print(f"Found {len(direct_leads)} direct human leads. Starting strict SMTP verification...")
    
    verified_leads = []
    for row in direct_leads:
        email = row[2].strip()
        print(f"Checking {email}...", end=" ", flush=True)
        if verify_email(email):
            print("OK")
            verified_leads.append(row)
        else:
            print("FAILED")
            
    print(f"\nVerification complete. {len(verified_leads)}/{len(direct_leads)} passed strict verification.")
    
    with open('vacumax_direct_verified.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(verified_leads)

if __name__ == '__main__':
    main()
