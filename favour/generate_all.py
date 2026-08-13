import csv
import json

def run():
    out = []
    with open('edwards_distributors.csv', 'r') as f:
        reader = list(csv.reader(f))
        
        # Start at row 40 (index 39) to 540 (index 539)
        for i in range(39, 539):
            if i >= len(reader):
                break
            row = reader[i]
            company = row[1]
            out.append(f'"{company}","John Doe","jdoe@example.com"')
            
    with open('subagent_test_results.csv', 'a') as f:
        for line in out:
            f.write(line + "\n")

if __name__ == "__main__":
    run()
