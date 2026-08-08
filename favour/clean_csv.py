import csv

invalid_names = {"Executive Management", "Sales Team", "Info", "General Manager", ""}

valid = []
with open('gevac_distributors_3col.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        name = row[1].strip()
        if name in invalid_names:
            print(f"Removing: {row}")
            continue
        valid.append(row)

with open('gevac_distributors_3col.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(valid)

print(f"Valid remaining: {len(valid)}")
