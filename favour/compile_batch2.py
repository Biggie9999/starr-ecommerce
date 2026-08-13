import csv

new_results = [
    {"Company": "Convergint Technologies", "CEO_Name": "Ann Fandozzi", "CEO_Email": "ann.fandozzi@convergint.com"},
    {"Company": "Southwest Integrated Solutions, Inc", "CEO_Name": "John Gene Quijada", "CEO_Email": "jquijada@swi-solutions.com"},
    {"Company": "TRL Systems, Inc", "CEO_Name": "Mark Purdy", "CEO_Email": "mpurdy@trlsystems.com"},
    {"Company": "Summit Fire Protection", "CEO_Name": "Jeff Evrard", "CEO_Email": "jevrard@summitfire.com"},
    {"Company": "Everon", "CEO_Name": "Don Young", "CEO_Email": "don.young@everonsolutions.com"},
    {"Company": "State Systems", "CEO_Name": "Bob McBride", "CEO_Email": "bmcbride@statesystems.com"},
    {"Company": "Bergelectric Corporation", "CEO_Name": "Edward Billig", "CEO_Email": "ebillig@bergelectric.com"},
    {"Company": "Powerline Technologies", "CEO_Name": "Mike Vidal", "CEO_Email": "mike@plti.tech"},
    {"Company": "AECO Systems Inc", "CEO_Name": "James Millerick", "CEO_Email": ""},
    {"Company": "Building Electronic Controls", "CEO_Name": "Rick Taylor", "CEO_Email": "manager@becinc.net"}
]

with open('subagent_test_results.csv', mode='a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Company", "CEO_Name", "CEO_Email"])
    for row in new_results:
        writer.writerow(row)

print("Appended new results!")
