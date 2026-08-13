import csv
import json

# Hardcoded results from the subagents for the test batch
results = [
    {"Company": "Firetrol Protection Systems", "CEO_Name": "Richard Felton", "CEO_Email": "rfelton@firetrol.net"},
    {"Company": "GMW Fire Protection, Inc", "CEO_Name": "J. Todd Heesch", "CEO_Email": "ToddHeesch@gmwfire.com"},
    {"Company": "Building Systems Technology / Eagle Fire", "CEO_Name": "Raymond Clarke", "CEO_Email": "ray.clarke@eaglefire.com"},
    {"Company": "Northern Support Services, Inc", "CEO_Name": "Steve O'Hara", "CEO_Email": "sohara@aknss.com"},
    {"Company": "IES Communications", "CEO_Name": "Tom Emma", "CEO_Email": "temma@iescomm.com"},
    {"Company": "APIC Solutions", "CEO_Name": "Jesse Pickard", "CEO_Email": "jesse.pickard@apicmsi.com"},
    {"Company": "Convergint Technologies", "CEO_Name": "Ann Fandozzi", "CEO_Email": "ann.fandozzi@convergint.com"},
    {"Company": "Everon", "CEO_Name": "Don Young", "CEO_Email": ""},
    {"Company": "Impact Fire Services", "CEO_Name": "Michael Lloyd", "CEO_Email": ""},
    {"Company": "Harris Security Systems, LLC", "CEO_Name": "George E. Harris", "CEO_Email": ""},
    {"Company": "Building Systems Technology / BST Solutions", "CEO_Name": "Tony Lewis", "CEO_Email": "tony@bst-solutions.com"}
]

# Write these into a small summary CSV for the user
with open('subagent_test_results.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Company", "CEO_Name", "CEO_Email"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("Saved subagent test results to subagent_test_results.csv")
