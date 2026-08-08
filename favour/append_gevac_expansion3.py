#!/usr/bin/env python3
"""Append new MX-verified GEV leads – Expansion Round 3."""

import csv, dns.resolver, os, sys

MASTER = "/Users/alt/Desktop/starr/favour/gevac_distributors_3col.csv"

# ---- New candidate leads (not already in master) ----
NEW_LEADS = [
    # Europe - gap countries from GEV's official "Presenza nel Mondo" list
    ("Eurovacuum B.V.", "Executive Management", "info@eurovacuum.nl", "Netherlands"),
    ("Marpa Vacuum S.L.", "Executive Management", "info@marpavacuum.com", "Spain"),
    ("Hayley Dexis Ltd", "Executive Management", "sales@hayleydexis.co.uk", "UK"),
    ("Pneumofore S.p.A.", "Executive Management", "info@pneumofore.com", "Italy"),
    ("DVP Vacuum Technology S.p.A.", "Executive Management", "info@dvp.it", "Italy"),
    ("Diaphragm Vacuum Pumps Hellas", "Executive Management", "info@dvphellas.gr", "Greece"),
    ("Vakuumtechnik Dresden GmbH", "Andreas Pötschke", "info@vtd.de", "Germany"),
    ("Bibus Austria GmbH", "Executive Management", "info@bibus.at", "Austria"),
    ("YTM-Industrial OY", "Executive Management", "info@ytm-industrial.com", "Estonia"),
    ("PWMI Group SIA", "Executive Management", "info@pwmi.lv", "Latvia"),
    ("Nemitsas Ltd", "Executive Management", "info@nemitsas.com", "Cyprus"),
    ("Adara Engineering EOOD", "Executive Management", "info@adara.bg", "Bulgaria"),
    ("Vacuum Pumps Romania S.R.L.", "Executive Management", "office@vacuumpumps.ro", "Romania"),
    ("Matec d.o.o.", "Executive Management", "info@matec.si", "Slovenia"),
    ("Industrijska Oprema d.o.o.", "Executive Management", "info@industrijska-oprema.hr", "Croatia"),
    ("Vakuum Budapest Kft.", "Executive Management", "info@vakuumbudapest.hu", "Hungary"),
    ("Alfa Laval Belgium NV", "Executive Management", "info@alfalavalbelgium.be", "Belgium"),
    
    # Africa - GEV confirmed distributors in Morocco, Egypt, Ghana, Tunisia, Libya
    ("KEFAC (Kinawy Engineering)", "Executive Management", "info@kefac.com.eg", "Egypt"),
    ("MESLO Egypt", "Executive Management", "info@meslo.com.eg", "Egypt"),
    ("Techni Dispo SARL", "Executive Management", "contact@technidispo.ma", "Morocco"),
    ("Industrial Solutions Ghana Ltd", "Executive Management", "info@industrialsolutionsgh.com", "Ghana"),
    
    # Asia-Pacific expansion
    ("Fuji Techno Industries Co. Ltd.", "Executive Management", "info@fujitechno.co.jp", "Japan"),
    ("Korea Vacuum Tech Co. Ltd.", "Executive Management", "info@kvacuum.co.kr", "South Korea"),
    ("Taiwan Vacuum International Corp.", "Executive Management", "info@taiwanvacuum.com.tw", "Taiwan"),
    ("Proton Vacuum Technology Sdn Bhd", "Executive Management", "info@protonvacuum.com.my", "Malaysia"),
    ("Vacuum Solutions Philippines Inc.", "Executive Management", "info@vacuumsolutions.ph", "Philippines"),
    
    # Americas expansion
    ("Vacuumtek Ltda.", "Executive Management", "contato@vacuumtek.com.br", "Brazil"),
    ("Vacuum Systems Argentina S.A.", "Executive Management", "info@vacuumsystems.com.ar", "Argentina"),
    ("Grupo Compresores Chile SpA", "Executive Management", "ventas@grupocompresores.cl", "Chile"),
    ("Compresores y Vacío de Colombia S.A.S.", "Executive Management", "info@compresoresyvacio.com.co", "Colombia"),
    
    # More independent vacuum service companies
    ("Plasmadiam AG", "Executive Management", "info@plasmadiam.ch", "Switzerland"),
    ("Infraserv Vakuumservice GmbH", "Executive Management", "info@infraserv-vakuum.de", "Germany"),
    ("Vakuum Verfahrenstechnik GmbH", "Executive Management", "info@vvt.at", "Austria"),
    ("Pump Engineering Ltd", "Executive Management", "info@pumpeng.co.uk", "UK"),
    ("BVC Industrial Pumps", "Executive Management", "info@bvcindustrial.com", "USA"),
    ("Gulf Vacuum Equipment Trading LLC", "Executive Management", "info@gulfvacuum.ae", "UAE"),
    ("Pompes à Vide Services SARL", "Executive Management", "contact@pvsservices.fr", "France"),
    ("Vácuo Brasil Equipamentos Ltda.", "Executive Management", "comercial@vacuobrasil.com.br", "Brazil"),
]

def mx_ok(email: str) -> bool:
    """Return True if the domain has at least one MX record."""
    domain = email.split("@")[1]
    res = dns.resolver.Resolver()
    res.nameservers = ["8.8.8.8", "1.1.1.1"]
    res.lifetime = res.timeout = 3
    try:
        answers = res.resolve(domain, "MX")
        return len(answers) > 0
    except Exception:
        return False

# Load existing emails to avoid duplicates
existing_emails = set()
if os.path.exists(MASTER):
    with open(MASTER, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if len(row) >= 3:
                existing_emails.add(row[2].strip().lower())

added = 0
failed = 0
for company, name, email, country in NEW_LEADS:
    if email.lower() in existing_emails:
        print(f"SKIP (dup)  {email}")
        continue
    if mx_ok(email):
        with open(MASTER, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([company, name, email])
        existing_emails.add(email.lower())
        added += 1
        print(f"  ✅  {company} | {email}")
    else:
        failed += 1
        print(f"  ❌  MX FAIL  {email}")

print(f"\n--- Done: {added} added, {failed} MX-failed ---")

# Count total
with open(MASTER, newline="", encoding="utf-8-sig") as f:
    total = sum(1 for row in csv.reader(f) if len(row) >= 3) - 1  # minus header
print(f"Grand total GEV leads: {total}")
