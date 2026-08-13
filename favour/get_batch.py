import csv
import sys
import json

start_idx = int(sys.argv[1])
batch_size = int(sys.argv[2])

with open("edwards_distributors.csv", "r", encoding="utf-8") as f:
    reader = list(csv.DictReader(f))
    batch = reader[start_idx : start_idx + batch_size]
    
    out = []
    for row in batch:
        out.append({
            "DistributorName": row.get("DistributorName", ""),
            "City": row.get("City", ""),
            "StateCode": row.get("StateCode", "")
        })
    print(json.dumps(out))
