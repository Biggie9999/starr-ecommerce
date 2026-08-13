import requests
import csv
import json

API_KEY = 'fCO5Pc9Tj1UPW0GwIVPnEA'
URL = 'https://api.apollo.io/v1/mixed_people/search'

def extract_domain(website_str):
    if not website_str:
        return ""
    domain = website_str.lower().replace("http://", "").replace("https://", "").replace("www.", "")
    domain = domain.split('/')[0]
    return domain

def test_apollo():
    with open('edwards_distributors.csv', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        
    test_batch = reader[:5]
    print(f"Testing {len(test_batch)} companies...")
    
    for row in test_batch:
        domain = extract_domain(row['Website'])
        company = row['DistributorName']
        
        headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
            'X-Api-Key': API_KEY
        }
        
        payload = {
            "person_titles": ["ceo", "founder", "president", "owner", "chief executive officer", "managing director"],
            "per_page": 1
        }
        
        if domain:
            payload["q_organization_domains"] = domain
        else:
            payload["q_organization_name"] = company
            
        print(f"Querying for {company} ({domain})...")
        response = requests.post(URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            people = data.get('people', [])
            if people:
                person = people[0]
                name = person.get('name', '')
                email = person.get('email', '')
                print(f"  -> Found: {name} | {email}")
            else:
                print("  -> Found: No C-Level contacts found in Apollo")
        else:
            print(f"  -> Error: API returned status {response.status_code}")
            print(response.text)

if __name__ == '__main__':
    test_apollo()
