import csv

def process():
    with open("edwards_distributors.csv", "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open("strict_edwards_distributors.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["CEO_Name", "CEO_Email"])
        writer.writeheader()
        for row in rows:
            row["CEO_Name"] = ""
            row["CEO_Email"] = ""
            writer.writerow(row)

if __name__ == "__main__":
    process()
