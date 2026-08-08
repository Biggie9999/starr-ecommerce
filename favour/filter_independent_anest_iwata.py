import csv

in_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"
out_csv = "/Users/alt/Desktop/starr/favour/anest_iwata_distributors_3col.csv"

# Keywords indicating direct corporate subsidiaries of Anest Iwata
subsidiary_keywords = [
    "anest iwata americas",
    "anest iwata medea",
    "anest iwata méxico",
    "anest iwata mexico",
    "airzap – anest iwata",
    "airzap - anest iwata",
    "anest iwata europe",
    "anest iwata deutschland",
    "anest iwata france",
    "anest iwata (u.k.)",
    "anest iwata uk",
    "anest iwata ibérica",
    "anest iwata iberica",
    "anest iwata scandinavia",
    "anest iwata polska",
    "anest iwata rus",
    "anest iwata strategic",
    "anest iwata south africa",
    "harder & steenbeck"  # direct subsidiary
]

filtered_rows = []
removed_count = 0

with open(in_csv, "r") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if row:
            company = row[0].lower().strip()
            if any(sk in company for sk in subsidiary_keywords):
                removed_count += 1
                print(f"REMOVED SUBSIDIARY: {row[0]}")
            else:
                filtered_rows.append(row)

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Name", "Email"])
    for row in filtered_rows:
        writer.writerow(row)

print(f"Removed {removed_count} corporate subsidiaries. Saved {len(filtered_rows)} independent distributors to {out_csv}")
