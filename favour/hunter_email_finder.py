#!/usr/bin/env python3
"""
Hunter.io CEO Email Finder
============================
Reads conveyor_distributors_70.csv, queries Hunter.io's FREE API to:
1. Find the email pattern for each company domain
2. Search for the CEO/President's email specifically

SETUP:
1. Sign up FREE at: https://hunter.io/users/sign_up
2. Go to: https://hunter.io/api-keys  — copy your API key
3. Run:
   export HUNTER_API_KEY="your_key_here"
   python3 hunter_email_finder.py

Hunter.io free tier: 25 searches/month + 50 verifications/month.
For 69 companies, you may need to split across 3 months or upgrade ($49/mo for 500).
"""

import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error

HUNTER_API_KEY = os.environ.get("HUNTER_API_KEY", "")
INPUT_FILE = "conveyor_distributors_70.csv"
OUTPUT_FILE = "conveyor_distributors_with_emails.csv"

def find_email_hunter(domain, first_name, last_name, company_name):
    """Use Hunter.io Email Finder to get a specific person's email."""
    
    params = f"domain={domain}&first_name={first_name}&last_name={last_name}&api_key={HUNTER_API_KEY}"
    url = f"https://api.hunter.io/v2/email-finder?{params}"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        data = result.get("data", {})
        email = data.get("email", "")
        score = data.get("score", 0)
        position = data.get("position", "")

        if email and score >= 70:
            return email, score, position
        elif email:
            return email, score, position
        return None, 0, ""

    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("\n  ⏳ Rate limited. Waiting 60s...")
            time.sleep(60)
            return find_email_hunter(domain, first_name, last_name, company_name)
        elif e.code == 402:
            print("\n  ⚠️  Credits exhausted!")
            return "CREDITS_EXHAUSTED", 0, ""
        else:
            error_body = e.read().decode("utf-8") if e.fp else ""
            print(f"\n  ❌ HTTP {e.code}: {error_body[:150]}")
            return None, 0, ""
    except Exception as e:
        print(f"\n  ❌ Error: {e}")
        return None, 0, ""


def domain_search_hunter(domain):
    """Use Hunter.io Domain Search to find all emails at a domain."""

    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}&limit=5&seniority=senior,executive&department=executive"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        data = result.get("data", {})
        emails = data.get("emails", [])
        pattern = data.get("pattern", "")

        ceo_emails = []
        for entry in emails:
            email = entry.get("value", "")
            first = entry.get("first_name", "")
            last = entry.get("last_name", "")
            position = entry.get("position", "")
            confidence = entry.get("confidence", 0)

            if any(t in (position or "").lower() for t in ["ceo", "president", "owner", "founder", "chief executive"]):
                ceo_emails.append({
                    "email": email,
                    "name": f"{first} {last}".strip(),
                    "position": position,
                    "confidence": confidence,
                })

        return pattern, ceo_emails, emails

    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("\n  ⏳ Rate limited. Waiting 60s...")
            time.sleep(60)
            return domain_search_hunter(domain)
        elif e.code == 402:
            return "CREDITS_EXHAUSTED", [], []
        return "", [], []
    except Exception as e:
        print(f"\n  ❌ Error: {e}")
        return "", [], []


def split_name(full_name):
    """Split a CEO name into first and last, handling edge cases."""
    if not full_name or full_name.lower() == "unknown":
        return "", ""

    # Remove parenthetical notes like "(President Americas)" or "(VP/Co-Owner)"
    import re
    full_name = re.sub(r'\(.*?\)', '', full_name).strip()

    # Remove titles/suffixes
    for remove in ["Jr.", "Sr.", "III", "II", "IV", "Dr.", "Mr.", "Mrs.", "P.E."]:
        full_name = full_name.replace(remove, "").strip()

    # Handle "Co-CEOs" format like "Zach Hodge / Jordan Fullan"
    if "/" in full_name:
        full_name = full_name.split("/")[0].strip()

    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]
    elif len(parts) == 1:
        return parts[0], ""
    return "", ""


def main():
    if not HUNTER_API_KEY:
        print("=" * 60)
        print("ERROR: No Hunter.io API key found!")
        print()
        print("1. Sign up FREE at: https://hunter.io/users/sign_up")
        print("2. Go to: https://hunter.io/api-keys")
        print("3. Copy your key and run:")
        print()
        print('   export HUNTER_API_KEY="your_key_here"')
        print(f"   python3 {sys.argv[0]}")
        print("=" * 60)
        sys.exit(1)

    # Read input CSV
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"📂 Loaded {len(rows)} companies from {INPUT_FILE}")
    print(f"🔑 Hunter API key: ...{HUNTER_API_KEY[-6:]}")
    print("=" * 60)
    print()

    results = []
    found_count = 0
    credits_exhausted = False
    total = len(rows)

    for i, row in enumerate(rows, 1):
        company = row.get("Company Name", "")
        domain = row.get("Website Domain", "")
        ceo = row.get("CEO/President Name", "")
        ownership = row.get("Ownership Type", "")

        print(f"[{i}/{total}] {company} ({domain})", end="", flush=True)

        email = ""
        confidence = 0
        method = ""

        if credits_exhausted:
            print(" ⚠️  Skipped (no credits)")
        else:
            first, last = split_name(ceo)

            # Method 1: Try Email Finder (if we have a name)
            if first and last:
                print(f" → Finding {first} {last}...", end="", flush=True)
                found_email, score, position = find_email_hunter(domain, first, last, company)

                if found_email == "CREDITS_EXHAUSTED":
                    credits_exhausted = True
                    print(" ⚠️  Credits exhausted!")
                elif found_email:
                    email = found_email
                    confidence = score
                    method = "email-finder"
                    print(f" ✅ {email} (confidence: {score}%)")
                    found_count += 1
                else:
                    print(" ❌ Not found via finder", end="", flush=True)

            # Method 2: Fall back to Domain Search
            if not email and not credits_exhausted:
                print(" → Domain search...", end="", flush=True)
                pattern, ceo_emails, all_emails = domain_search_hunter(domain)

                if pattern == "CREDITS_EXHAUSTED":
                    credits_exhausted = True
                    print(" ⚠️  Credits exhausted!")
                elif ceo_emails:
                    best = ceo_emails[0]
                    email = best["email"]
                    confidence = best["confidence"]
                    method = "domain-search"
                    ceo = f"{best['name']} ({best['position']})" if best['name'] else ceo
                    print(f" ✅ {email} (confidence: {confidence}%)")
                    found_count += 1
                elif pattern and first and last:
                    # Generate email from pattern
                    email = pattern.replace("{first}", first.lower()).replace("{last}", last.lower()).replace("{f}", first[0].lower()) + "@" + domain
                    confidence = 50
                    method = f"pattern ({pattern})"
                    print(f" 🔶 {email} (from pattern, unverified)")
                    found_count += 1
                else:
                    print(" ❌ No email found")

        results.append({
            "Company Name": company,
            "Website Domain": domain,
            "CEO/President Name": ceo,
            "Verified Email": email,
            "Confidence": confidence,
            "Method": method,
            "Ownership Type": ownership,
        })

        time.sleep(2)  # Be respectful to the API

    # Write output CSV
    fieldnames = [
        "Company Name",
        "Website Domain",
        "CEO/President Name",
        "Verified Email",
        "Confidence",
        "Method",
        "Ownership Type",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print()
    print("=" * 60)
    print(f"✅ DONE! Results saved to: {OUTPUT_FILE}")
    print(f"📊 Found {found_count}/{total} emails ({round(found_count/total*100)}%)")
    if credits_exhausted:
        print("⚠️  Some lookups were skipped due to credit limits.")
        print("   Upgrade at https://hunter.io/pricing for more credits.")
    print("=" * 60)


if __name__ == "__main__":
    main()
