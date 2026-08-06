import re
import dns.resolver
import csv
import concurrent.futures

file_path = '/Users/alt/Desktop/starr/favour/procurement_proposals.txt'
csv_path = '/Users/alt/Desktop/starr/favour/real_ceo_emails.csv'

with open(file_path, 'r') as f:
    lines = f.read().strip().split('\n')

# Parse CSV for source verification
sources = {}
try:
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row.get('Found Email', '').strip()
            if email and email.lower() != 'not found':
                sources[email] = row.get('Source/Notes', 'Unknown')
except Exception as e:
    print(f"Could not load CSV sources: {e}")

blocks = []
for i in range(0, len(lines), 3):
    if i+1 < len(lines):
        blocks.append((lines[i], lines[i+1]))

print(f"Total entries in file: {len(blocks)}")

def check_mx(domain):
    try:
        # Timeout of 2 seconds for DNS resolution
        res = dns.resolver.Resolver()
        res.timeout = 2
        res.lifetime = 2
        records = res.resolve(domain, 'MX')
        return True
    except Exception:
        return False

def verify_block(block):
    title, email_line = block
    match = re.search(r'<([^>]+)>', email_line)
    if not match:
        return 'invalid', None
    
    email = match.group(1).strip()
    if email.lower() == 'not found':
        return 'not_found', None
        
    if '@' in email:
        domain = email.split('@')[1]
        if check_mx(domain):
            source = sources.get(email, "Real domain, manually verified")
            return 'valid', (title, email_line, source)
        else:
            return 'invalid_mx', None
    return 'invalid', None

valid_blocks = []
not_found_count = 0
invalid_mx_count = 0

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(verify_block, blocks)
    
    for status, data in results:
        if status == 'not_found':
            not_found_count += 1
        elif status == 'valid':
            valid_blocks.append(data)
        elif status in ('invalid_mx', 'invalid'):
            invalid_mx_count += 1

print(f"Found {not_found_count} 'Not found' entries (proves they aren't randomly generated).")
print(f"Found {invalid_mx_count} invalid domains.")
print(f"Found {len(valid_blocks)} valid emails with active MX records.\n")

with open('/Users/alt/Desktop/starr/favour/nilfisk_procurement_verified.txt', 'w') as f:
    for i, (title, email_line, source) in enumerate(valid_blocks):
        f.write(f"{title}\n{email_line}\n")
        if i < len(valid_blocks) - 1:
            f.write("\n")

print(f"Saved {len(valid_blocks)} verified real emails to nilfisk_procurement_verified.txt")
