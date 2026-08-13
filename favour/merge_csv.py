import csv

def main():
    file1 = 'final_fuji_distributors.csv'
    file2 = 'final_fuji_expansion.csv'
    output_file = 'fuji_distributors_master.csv'
    
    rows = []
    
    # Read the first file
    with open(file1, 'r', encoding='utf-8') as f1:
        reader = csv.reader(f1)
        header = next(reader)
        for row in reader:
            rows.append(row)
            
    # Read the second file (skip header)
    with open(file2, 'r', encoding='utf-8') as f2:
        reader = csv.reader(f2)
        next(reader)
        for row in reader:
            rows.append(row)
            
    # Write to master file
    with open(output_file, 'w', encoding='utf-8', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(header)
        writer.writerows(rows)
        
    print(f"Successfully merged {len(rows)} total records into {output_file}!")

if __name__ == "__main__":
    main()
