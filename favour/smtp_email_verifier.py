#!/usr/bin/env python3
"""
SMTP Email Permutation Verifier
===============================
Generates common email formats for a CEO based on their name and company domain,
then connects to the domain's mail server via SMTP to check if the email exists.
"""

import csv
import smtplib
import socket
import re
import sys
import time
import dns.resolver

INPUT_FILE = "conveyor_distributors_70.csv"
OUTPUT_FILE = "conveyor_distributors_with_emails.csv"

def split_name(full_name):
    if not full_name or full_name.lower() == "unknown":
        return "", ""
    full_name = re.sub(r'\(.*?\)', '', full_name).strip()
    for remove in ["Jr.", "Sr.", "III", "II", "IV", "Dr.", "Mr.", "Mrs.", "P.E."]:
        full_name = full_name.replace(remove, "").strip()
    if "/" in full_name:
        full_name = full_name.split("/")[0].strip()
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0].lower(), parts[-1].lower()
    elif len(parts) == 1:
        return parts[0].lower(), ""
    return "", ""

def get_mx_record(domain):
    """Get the mail server for a domain"""
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = sorted(records, key=lambda x: x.preference)[0].exchange.to_text()
        return mx_record
    except Exception:
        return None

def verify_email_smtp(email, mx_record):
    """Check if an email address exists on the mail server"""
    try:
        # Setup SMTP conversation
        server = smtplib.SMTP(timeout=10)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('hello@google.com')
        code, message = server.rcpt(str(email))
        server.quit()

        # 250 means OK (address exists/accepted)
        if code == 250:
            return True
        return False
    except Exception:
        return False

def check_catch_all(domain, mx_record):
    """Check if the server accepts ALL emails (catch-all)"""
    dummy_email = f"this_email_definitely_does_not_exist_12345@{domain}"
    return verify_email_smtp(dummy_email, mx_record)

def main():
    try:
        import dns.resolver
    except ImportError:
        print("Please install dnspython: pip install dnspython")
        sys.exit(1)

    print(f"📂 Loading companies from {INPUT_FILE}")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    results = []
    found_count = 0
    total = len(rows)

    print("=" * 60)

    for i, row in enumerate(rows, 1):
        company = row.get("Company Name", "")
        domain = row.get("Website Domain", "")
        ceo = row.get("CEO/President Name", "")
        ownership = row.get("Ownership Type", "")

        first, last = split_name(ceo)
        verified_email = ""
        method = ""

        print(f"[{i}/{total}] {company} ({domain})... ", end="", flush=True)

        if not first:
            print("⏭️  Skipped (No CEO name)")
        elif not domain or "." not in domain:
            print("⏭️  Skipped (Invalid domain)")
        else:
            # 1. Get MX Record
            mx = get_mx_record(domain)
            if not mx:
                print("❌ Failed (No MX record found)")
            else:
                # 2. Check for Catch-All (if catch-all is true, we can't verify specific emails)
                if check_catch_all(domain, mx):
                    print(f"⚠️  Catch-All server (can't verify) -> Guessing: {first[0]}{last}@{domain}")
                    verified_email = f"{first[0]}{last}@{domain}"
                    method = "Guessed (Catch-All Domain)"
                else:
                    # 3. Test permutations
                    permutations = []
                    if first and last:
                        permutations = [
                            f"{first[0]}{last}@{domain}",       # jdoe@
                            f"{first}.{last}@{domain}",         # john.doe@
                            f"{first}@{domain}",                # john@
                            f"{first}{last}@{domain}",          # johndoe@
                            f"{first}_{last}@{domain}",         # john_doe@
                            f"{last}@{domain}",                 # doe@
                        ]
                    elif first:
                        permutations = [f"{first}@{domain}"]

                    found = False
                    for email in permutations:
                        if verify_email_smtp(email, mx):
                            print(f"✅ {email}")
                            verified_email = email
                            method = "SMTP Verified"
                            found = True
                            found_count += 1
                            break
                        time.sleep(0.5) # Slight delay between attempts

                    if not found:
                        print("❌ Failed (All permutations rejected)")

        results.append({
            "Company Name": company,
            "Website Domain": domain,
            "CEO/President Name": ceo,
            "Verified Email": verified_email,
            "Confidence": "100" if method == "SMTP Verified" else "50" if "Guessed" in method else "0",
            "Method": method,
            "Ownership Type": ownership,
        })

    # Write output
    fieldnames = ["Company Name", "Website Domain", "CEO/President Name", "Verified Email", "Confidence", "Method", "Ownership Type"]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("=" * 60)
    print(f"✅ DONE! Found {found_count} rock-solid verified emails.")
    print(f"Saved to: {OUTPUT_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    main()
