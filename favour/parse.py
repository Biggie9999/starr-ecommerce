import csv

results = []
with open('edwards_distributors.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if 19 <= i <= 539:
            results.append((row[1], row[4]))

with open('batch_names.txt', 'w') as f:
    for name, city in results:
        f.write(f"{name}|{city}\n")
