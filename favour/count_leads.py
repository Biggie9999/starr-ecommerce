import csv
import os

files = [
    "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv",
    "/Users/alt/Desktop/starr/favour/becker_distributors_3col.csv",
    "/Users/alt/Desktop/starr/favour/becker_new_distributors_3col.csv",
    "/Users/alt/Desktop/starr/favour/buschvacuum_dealers.csv"
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            rows = [r for r in reader if r]
            print(f"{os.path.basename(filepath)}: {len(rows)} leads")
