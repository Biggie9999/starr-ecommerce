import csv

new_leads = [
    ["Pneumofore S.p.A.", "Daniel Hilfiker", "info@pneumofore.com"],
    ["DVP Vacuum Technology S.p.A.", "Dr. Roberto Zucchini", "info@dvp.it"],
    ["Bibus Austria GmbH", "Bernd Christian Tröster", "info@bibus.at"],
    ["Fuji Techno Industries Co. Ltd.", "Takeshi Ikinobu", "info@fujitechno.co.jp"],
    ["Korea Vacuum Tech Co. Ltd.", "Woo Hyung-chul", "info@kvacuum.co.kr"]
]

file_path = '/Users/alt/Desktop/starr/favour/gevac_distributors_3col.csv'

with open(file_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(new_leads)

print(f"Appended {len(new_leads)} recovered leads.")
