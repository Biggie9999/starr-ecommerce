import csv

with open('batch_names.txt', 'r') as f:
    lines = [line.strip().split('|') for line in f.readlines()]

with open('dorking_edwards_distributors.csv', 'w', newline='') as csvfile:
    fieldnames = ['DistributorName', 'City', 'CEO_Name', 'CEO_Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(521):
        if i >= len(lines):
            break
        name, city = lines[i]
        writer.writerow({
            'DistributorName': name,
            'City': city,
            'CEO_Name': '',
            'CEO_Email': ''
        })
