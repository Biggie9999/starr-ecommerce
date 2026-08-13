import csv
import smtplib
import re
import socket
import concurrent.futures
import subprocess
import time

def get_mx_record(domain):
    try:
        # Use dig to get the MX records, sorted by priority (lowest first)
        result = subprocess.run(['dig', '+short', 'MX', domain], capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout:
            lines = result.stdout.strip().split('\n')
            records = []
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    records.append((int(parts[0]), parts[1]))
            if records:
                records.sort(key=lambda x: x[0])
                # Return the exchange name (remove trailing dot if exists)
                exchange = records[0][1]
                if exchange.endswith('.'):
                    exchange = exchange[:-1]
                return exchange
    except Exception:
        pass
    return None

def verify_email(email):
    email = email.strip()
    if not email:
        return "Empty"
        
    # Syntax check
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,20})$', email.lower())
    if match == None:
        return "Invalid Syntax"
        
    domain = email.split('@')[1]
    
    # MX record check using dig
    mx_record = get_mx_record(domain)
    if not mx_record:
        return "Invalid Domain/No MX"
        
    # SMTP Check
    try:
        server = smtplib.SMTP(timeout=5)
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('hello@example.com')
        code, message = server.rcpt(email)
        server.quit()
        
        if code == 250:
            return "Valid (or Catch-All)"
        elif code >= 500:
            return f"Invalid (SMTP {code})"
        else:
            return f"Uncertain (SMTP {code})"
    except Exception as e:
        # Port 25 might be blocked locally or by the remote server
        return "Unverifiable (SMTP Timeout/Blocked) - Domain Valid"

def process_row(row):
    email = row.get("CEO_Email", "")
    status = verify_email(email)
    row["Verification_Status"] = status
    return row

def main():
    print("Starting local verification process...")
    input_file = 'enriched_edwards_distributors.csv'
    output_file = 'verified_edwards_distributors.csv'
    
    with open(input_file, encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        
    print(f"Loaded {len(reader)} rows.")
    
    fieldnames = list(reader[0].keys())
    if "Verification_Status" not in fieldnames:
        fieldnames.append("Verification_Status")
        
    results = []
    # Using threads to heavily speed up the SMTP timeouts
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(process_row, row): row for row in reader}
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            results.append(future.result())
            if (i+1) % 50 == 0:
                print(f"Processed {i+1}/{len(reader)} emails...")
                
    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
    print(f"Verification complete! Results saved to {output_file}.")

if __name__ == "__main__":
    main()
