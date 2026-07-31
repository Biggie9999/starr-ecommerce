import csv

data = [
    ["Company", "CEO/Contact Name", "Found Email", "Source/Notes"],
    ["Vactech Sdn Bhd", "Eric Goh (General Manager)", "sales@vactech.com.my", "General sales email (Direct CEO email not found)"],
    ["Mitra Karyatama Industri", "Ery Kuncoro Adi (Founder)", "corporate@mitrakaryatama.com", "General corporate email"],
    ["Airvac Private Limited", "Not found", "sales@airvac.com.sg", "General sales email"],
    ["Astropack LLC", "Not found", "info@astropackgulf.com", "General info email"],
    ["Australian Industrial Vacuum", "Ken Schafer (Managing Director)", "sales@industrialvac.com.au", "General sales email"],
    ["Oz Cleaning Gear", "Kellen Briggs (Founder)", "kellen@ozcleaninggear.com.au", "Direct email found"],
    ["Goscor Cleaning Equipment", "Peter Esterhuizen (Managing Director)", "pesterhuizen@goscor.co.za", "Direct email found"],
    ["Kogi Environmental Solutions", "Cristian Núñez and William Arambula (Co-CEOs)", "info@kogi-es.com", "General info email"],
    ["Shiv Technology", "Atul Khairnar (Managing Director)", "atul@shivtechnology.co.in", "Direct email found"],
    ["Teejan Equipment", "Hamed Al Harrassy (Chairman)", "webenquiry@teejanequipment.com", "General inquiry email"]
]

output_file = "/Users/alt/Desktop/starr/favour/delfin_extended_result_2.csv"
with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Written to {output_file}")
