#!/usr/bin/env python3
"""
Apollo.io CEO Email Finder (v2 — uses People Enrichment endpoint)
==================================================================
The /v1/mixed_people/search endpoint requires a paid plan.
This version uses /v1/people/match (enrichment) which works on FREE plans.
"""

import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error
import re

APOLLO_API_KEY = os.environ.get("APOLLO_API_KEY", "")
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
        return parts[0], parts[-1]
    elif len(parts) == 1:
        return parts[0], ""
    return "", ""


def enrich_person(first_name, last_name, domain, company_name):
    """Use Apollo People Enrichment (match) endpoint — works on free plan."""
    
    url = "https://api.apollo.io/v1/people/match"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "X-Api-Key": APOLLO_API_KEY,
    }

    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "organization_name": company_name,
        "domain": domain,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        person = result.get("person", {})
        if not person:
            return None, "", ""

        email = person.get("email", "")
        name = person.get("name", "")
        title = person.get("title", "")

        return email or None, name, title

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        if e.code == 429:
            print("\n  ⏳ Rate limited. Waiting 60s...")
            time.sleep(60)
            return enrich_person(first_name, last_name, domain, company_name)
        elif e.code == 422:
            # Unprocessable — person not found
            return None, "", ""
        else:
            print(f"\n  ❌ HTTP {e.code}: {error_body[:200]}")
            return None, "", ""
    except Exception as e:
        print(f"\n  ❌ Error: {e}")
        return None, "", ""


def main():
    if not APOLLO_API_KEY:
        print("=" * 60)
        print("ERROR: No Apollo API key found!")
        print('   export APOLLO_API_KEY="your_key_here"')
        print(f"   python3 {sys.argv[0]}")
        print("=" * 60)
        sys.exit(1)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"📂 Loaded {len(rows)} companies from {INPUT_FILE}")
    print(f"🔑 Apollo API key: ...{APOLLO_API_KEY[-6:]}")
    print(f"🔗 Using endpoint: /v1/people/match (FREE tier compatible)")
    print("=" * 60)

    results = []
    found_count = 0
    total = len(rows)

    for i, row in enumerate(rows, 1):
        company = row.get("Company Name", "")
        domain = row.get("Website Domain", "")
        ceo = row.get("CEO/President Name", "")
        ownership = row.get("Ownership Type", "")

        first, last = split_name(ceo)

        print(f"[{i}/{total}] {company} ({domain})", end="", flush=True)

        email = ""
        matched = ""

        if first and last:
            print(f" → {first} {last}...", end="", flush=True)
            found_email, name, title = enrich_person(first, last, domain, company)

            if found_email:
                email = found_email
                matched = f"{name} ({title})" if name else ""
                print(f" ✅ {email}")
                found_count += 1
            else:
                print(" ❌ No email")
        else:
            print(" ⏭️  Skipped (no CEO name)")

        results.append({
            "Company Name": company,
            "Website Domain": domain,
            "CEO/President Name": ceo,
            "Apollo Match": matched,
            "Verified Email": email,
            "Ownership Type": ownership,
        })

        time.sleep(1)

    fieldnames = ["Company Name", "Website Domain", "CEO/President Name", "Apollo Match", "Verified Email", "Ownership Type"]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print()
    print("=" * 60)
    print(f"✅ DONE! Saved to: {OUTPUT_FILE}")
    print(f"📊 Found {found_count}/{total} verified emails ({round(found_count/total*100)}%)")
    print("=" * 60)


if __name__ == "__main__":
    main()
