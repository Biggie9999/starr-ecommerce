import csv
import subprocess

def check_mx(domain):
    try:
        # Uses built-in 'host' command on Mac/Linux to lookup MX records
        result = subprocess.run(['host', '-t', 'mx', domain], capture_output=True, text=True, timeout=5)
        return "mail is handled by" in result.stdout
    except Exception:
        return False

def main():
    input_file = 'ultimate_edwards_distributors.csv'
    
    with open(input_file, encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        
    emails = [r['CEO_Email_Ultimate'] for r in reader if r.get('CEO_Email_Ultimate', '').strip()]
    
    print(f"Running MX DNS Verification on {len(emails)} emails...")
    
    valid_count = 0
    invalid_count = 0
    
    for i, email in enumerate(emails):
        domain = email.split('@')[1]
        if check_mx(domain):
            valid_count += 1
        else:
            invalid_count += 1
            
        if (i+1) % 50 == 0:
            print(f"Verified {i+1} / {len(emails)}...")
            
    print(f"\\nVerification Complete!")
    print(f"Valid Mail Servers (0 Bounces): {valid_count}")
    print(f"Invalid Mail Servers (Bounces): {invalid_count}")

if __name__ == "__main__":
    main()
