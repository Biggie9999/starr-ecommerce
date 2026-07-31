import csv
import os

files = ['ceos_part1.csv', 'ceos_part2.csv', 'ceos_part3.csv']
output = 'thomaspumps_actual_ceos.csv'

with open(output, 'w', newline='') as out_f:
    writer = csv.writer(out_f)
    header_written = False
    
    for filename in files:
        if not os.path.exists(filename):
            print(f"Warning: {filename} not found.")
            continue
            
        with open(filename, 'r') as in_f:
            reader = csv.reader(in_f)
            header = next(reader, None)
            
            if not header_written and header:
                writer.writerow(header)
                header_written = True
                
            for row in reader:
                if row:
                    writer.writerow(row)

print("Merged successfully.")
