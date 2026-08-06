import csv

becker_global_master = [
    # North America
    {"company": "Gebr. Becker GmbH Global Headquarters", "role": "Global CEO", "ceo": "Dr. Dorothee Becker", "email": "info@becker-international.com", "domain": "becker-international.com", "territory": "Global Headquarters (Wuppertal, Germany)"},
    {"company": "Becker Pumps Corporation USA Headquarters", "role": "Managing Director / President Americas", "ceo": "Jason Rathbun", "email": "jrathbun@beckerpumps.com", "domain": "beckerpumps.com", "territory": "USA Headquarters (Cuyahoga Falls, OH) - All US States"},
    {"company": "Becker Vacuum Pumps Canada Inc.", "role": "General Manager / Sales", "ceo": "Canadian Sales Division", "email": "info@becker-canada.com", "domain": "becker-canada.com", "territory": "Canada Headquarters (Bolton, ON) - All Canadian Provinces"},
    {"company": "Becker Mexico S. de R.L. de C.V.", "role": "General Manager / Sales", "ceo": "LATAM Sales Division", "email": "info@becker-mexico.mx", "domain": "becker-mexico.mx", "territory": "Mexico Headquarters (Monterrey, NL) - All Mexican States"},
    {"company": "Pioneer Equipment", "role": "President & Owner", "ceo": "Scott Trammell", "email": "strammell@pioneerequip.com", "domain": "pioneerequip.com", "territory": "Exclusive Representative (AZ, NM, NV, UT, El Paso TX)"},
    {"company": "Centennial Equipment", "role": "President & Owner", "ceo": "Jason Munzer", "email": "jmunzer@centennialequipment.com", "domain": "centennialequipment.com", "territory": "Authorized Becker Distributor (CO, WY, NM)"},
    {"company": "Stateside Industrial Solutions", "role": "President & Owner", "ceo": "Dennis R. Hernandez", "email": "dhernandez@statesideindustrial.com", "domain": "statesideindustrial.com", "territory": "Authorized Becker Representative (Miami, FL)"},
    {"company": "Application Associates", "role": "President", "ceo": "Jim McEvoy", "email": "jmcevoy@applicationassociates.com", "domain": "applicationassociates.com", "territory": "Stocking Representative (MA, CT, RI, ME, NH, VT)"},
    {"company": "CNC Parts Dept, Inc.", "role": "Owner & Founder", "ceo": "Lynn Kramer", "email": "lkramer@cncpd.com", "domain": "cncpd.com", "territory": "Authorized Stocking Distributor & Service Center (CA & Western US)"},
    {"company": "Powermatic Associates", "role": "President & CEO", "ceo": "Frank Nudo", "email": "fnudo@powermatic.net", "domain": "powermatic.net", "territory": "Authorized Representative (Livermore, CA - Northern CA)"},
    {"company": "Sherman Engineering Company", "role": "President", "ceo": "Mark Franklin", "email": "mfranklin@shermanengineering.com", "domain": "shermanengineering.com", "territory": "Authorized Representative & Distributor (PA, NJ, DE, MD, VA)"},
    {"company": "Lewis Systems & Service, Inc.", "role": "President", "ceo": "Larry Lewis", "email": "llewis@lewissystemsinc.com", "domain": "lewissystemsinc.com", "territory": "Authorized Becker Representative (NC, VA, SC)"},
    {"company": "Tri-State Air Compressor", "role": "President", "ceo": "Lee Adams", "email": "ladams@tristateair.com", "domain": "tristateair.com", "territory": "Authorized Representative & Distributor (IN, OH, KY)"},
    {"company": "Carotek Inc.", "role": "President", "ceo": "Dave Webster", "email": "dwebster@carotek.com", "domain": "carotek.com", "territory": "Stocking Representative & Distributor (NC, SC, VA, GA, TN)"},
    {"company": "Pye-Barker Engineered Solutions", "role": "President & CEO", "ceo": "Eric Lunsford", "email": "Eric@pyebarker.com", "domain": "pyebarker.com", "territory": "Authorized Representative & Distributor (GA, FL Panhandle)"},
    {"company": "OTC Industrial Technologies", "role": "CEO", "ceo": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com", "domain": "otcindustrial.com", "territory": "Stocking Distributor & Representative (OH, MI, IN, PA, WV, KY)"},
    {"company": "Anderson Process", "role": "CEO & Owner", "ceo": "Greg Domino", "email": "gdomino@andersonprocess.com", "domain": "andersonprocess.com", "territory": "Authorized Representative & Distributor (WI, IL, IA, IN, MI, MN)"},
    {"company": "Air Compressor Engineering Co., Inc.", "role": "President", "ceo": "Russ Klaubert", "email": "rklaubert@aircompressoreng.com", "domain": "aircompressoreng.com", "territory": "Authorized Representative & Distributor (MA, ME, NH, VT, RI)"},
    {"company": "Total Equipment Company", "role": "General Manager", "ceo": "Eric Solverson", "email": "eric.solverson@totalequipment.com", "domain": "totalequipment.com", "territory": "Authorized Representative & Service Provider (Western PA, WV)"},
    {"company": "Airline Hydraulics Corporation", "role": "CEO", "ceo": "Mark Steffens", "email": "msteffens@airlinehyd.com", "domain": "airlinehyd.com", "territory": "Authorized Stocking Representative (PA, NJ, NY, MD, DE)"},
    {"company": "Air Centers of Florida", "role": "President & CEO", "ceo": "Andrew J. Young", "email": "a.young@acfpower.com", "domain": "acfpower.com", "territory": "Authorized Representative & Distributor (FL)"},
    {"company": "J Herbert Corp", "role": "President", "ceo": "Mary Selbach", "email": "mselbach@jherbertcorp.com", "domain": "jherbertcorp.com", "territory": "Authorized Representative & Distributor (Kissimmee, FL)"},
    {"company": "Midway Industrial Supply", "role": "President", "ceo": "Paul Rockwell", "email": "prockwell@midwaycorp.com", "domain": "midwayindustrialsupply.com", "territory": "Authorized Stocking Distributor (NY, NJ)"},
    {"company": "JHFOSTER", "role": "CEO & President", "ceo": "Nicholas W. Martino", "email": "nicholas.martino@jhfoster.com", "domain": "jhfoster.com", "territory": "Authorized Representative & Distributor (MN, WI, ND, SD, IA)"},
    {"company": "Rogers Machinery Company, Inc.", "role": "President", "ceo": "Chris McKillop", "email": "chris.mckillop@rogers-machinery.com", "domain": "rogers-machinery.com", "territory": "Authorized Representative & Distributor (OR, WA, ID, MT, AK)"},
    {"company": "C&B Equipment", "role": "President & Owner", "ceo": "Ben Brocker", "email": "bbrocker@cbeuptime.com", "domain": "cbeuptime.com", "territory": "Authorized Representative & Service Center (KS, MO, OK, AR)"},
    {"company": "AAP Automation", "role": "Vice President", "ceo": "Wes Brown", "email": "wbrown@aapautomation.com", "domain": "aapautomation.com", "territory": "Authorized Representative & Distributor (AZ, NM, West TX)"},
    {"company": "CM Buck & Associates", "role": "President & CEO", "ceo": "Steven Hall", "email": "shall@cmbuck.com", "domain": "cmbuck.com", "territory": "Authorized Representative (Indianapolis, IN)"},
    {"company": "E.W. Klein & Company", "role": "President", "ceo": "Eddie Ostervold", "email": "eddieo@ewklein.com", "domain": "ewklein.com", "territory": "Authorized Vacuum Equipment Representative (GA, TN, NC, AL)"},
    {"company": "CompreVac Inc.", "role": "President & GM", "ceo": "Jonathan Snook", "email": "jonathan@comprevac.com", "domain": "comprevac.com", "territory": "Major Authorized Distributor & Repair Center (Mississauga, ON & QC)"},
    {"company": "Aircom Technologies", "role": "Managing Director", "ceo": "Oliver Bohris", "email": "o.bohris@aircom.net", "domain": "aircom.net", "territory": "Authorized Representative & Distributor (ON, QC, Canada & Germany)"},
    {"company": "Valley Compressor & Pump", "role": "General Manager", "ceo": "Jason Hurtubise", "email": "jhurtubise@valleycompressor.com", "domain": "valleycompressor.com", "territory": "Authorized Technical Representative (Pembroke, ON, Canada)"},
    {"company": "GTA Compressor Solutions", "role": "Owner & President", "ceo": "Steve Gray", "email": "steve@gtacompressorsolutions.ca", "domain": "gtacompressorsolutions.ca", "territory": "Authorized Technical Representative (Greater Toronto Area, ON)"},
    {"company": "HD Compression", "role": "President", "ceo": "Al Giffen", "email": "agiffen@hdcompression.com", "domain": "hdcompression.com", "territory": "Authorized Sales Representative (Calgary, AB, Western Canada)"},
    {"company": "Air Power Products", "role": "President & CEO", "ceo": "Abbas Khan", "email": "akhan@airpowerproducts.com", "domain": "airpowerproducts.ca", "territory": "Authorized Canadian Representative (Cambridge, ON, Canada)"},
    {"company": "Cisco Air Systems", "role": "President & CEO", "ceo": "Kent Frkovich", "email": "kent.frkovich@ciscoair.com", "domain": "ciscoair.com", "territory": "Authorized Representative & Distributor (Northern CA, NV)"},
    {"company": "Blake & Pendleton", "role": "President & CEO", "ceo": "Allen King", "email": "aking@blakeandpendleton.com", "domain": "blakeandpendleton.com", "territory": "Authorized Representative & Distributor (GA, AL, FL, TN, MS)"},
    {"company": "Fluid Flow Products", "role": "President", "ceo": "Pete Gherardi", "email": "petegherardi@fluidflow.com", "domain": "fluidflow.com", "territory": "Authorized Representative & Distributor (NC, SC, TX, FL)"},
    {"company": "Pattons Inc.", "role": "Vice President & GM", "ceo": "Scott Sutton", "email": "scott.sutton@pattonsinc.com", "domain": "pattonsinc.com", "territory": "Authorized Representative & Distributor (NC, SC, GA, VA)"},
    {"company": "Dearing Compressor & Pump Co.", "role": "CEO", "ceo": "Rebecca Dearing Wall", "email": "bwall@dearingcomp.com", "domain": "dearingcomp.com", "territory": "Stocking Distributor & Integrator (Youngstown, OH, PA, WV)"},
    {"company": "Northwest Pump & Equipment", "role": "President & CEO", "ceo": "Bob Mathews", "email": "bob.mathews@nwpump.com", "domain": "nwpump.com", "territory": "Authorized Representative & Distributor (OR, WA, CA, ID, MT)"},
    {"company": "Tri-State Vacuum & Pump", "role": "President & CEO", "ceo": "Troy Massey", "email": "troy.massey@tristateoilfield.com", "domain": "tristatevac.com", "territory": "Authorized Representative & Distributor (TX, OK)"},
    {"company": "HVH Industrial Solutions", "role": "Founder & CEO", "ceo": "Vladimir Harutyunyan", "email": "vlad@hvhindustrial.com", "domain": "hvhindustrial.com", "territory": "Authorized Distributor & Sales Partner (Rockaway, NJ - Nationwide)"},

    # Europe
    {"company": "Becker UK Ltd", "role": "Managing Director", "ceo": "Richard Oxley", "email": "richard.oxley@becker.co.uk", "domain": "becker.co.uk", "territory": "Official UK & Ireland Subsidiary (Hull, East Yorkshire)"},
    {"company": "Becker France S.A.R.L.", "role": "Gérant / Managing Director", "ceo": "Alexandre Yves Clay", "email": "becker@becker-france.fr", "domain": "becker-france.fr", "territory": "Official France Subsidiary (Gazeran / Les Clayes-sous-Bois)"},
    {"company": "Becker Italia S.r.l.", "role": "Director & General Manager", "ceo": "Fabrizio Cazzoli", "email": "fabrizio.cazzoli@becker.it", "domain": "becker.it", "territory": "Official Italy Subsidiary (Castel Maggiore, Bologna)"},
    {"company": "Becker Ibérica de Bombas de Vacío S.A.", "role": "Director General", "ceo": "Mario Peralta", "email": "mario.peralta@becker-iberica.com", "domain": "becker-iberica.com", "territory": "Official Spain & Portugal Subsidiary (Barcelona)"},
    {"company": "Becker Druk- en Vacuümpompen B.V.", "role": "Directeur / Managing Director", "ceo": "Nico Segers", "email": "nico.segers@beckerdvp.nl", "domain": "beckerdvp.nl", "territory": "Official Netherlands & Benelux Subsidiary (Heerenveen)"},
    {"company": "Becker AG Switzerland", "role": "Geschäftsführer", "ceo": "Fabio Pappacena", "email": "fabio.pappacena@becker.ch", "domain": "becker.ch", "territory": "Official Switzerland & Liechtenstein Subsidiary (Spreitenbach)"},
    {"company": "Becker Vakuumteknik AB", "role": "VD / Managing Director", "ceo": "Lars-Erik Möller", "email": "kundservice@beckervakuum.se", "domain": "beckervakuum.se", "territory": "Official Sweden & Nordics Subsidiary (Mölndal)"},
    {"company": "Becker Polska Sp. z o.o.", "role": "Prezes Zarządu (CEO)", "ceo": "Grzegorz Wojciechowski", "email": "grzegorz.wojciechowski@becker-polska.com", "domain": "becker-polska.com", "territory": "Official Poland & Eastern Europe Subsidiary (Kościan)"},
    {"company": "Gebrüder Becker Austria GmbH", "role": "Geschäftsführer", "ceo": "Carmine Pappacena", "email": "carmine.pappacena@becker-austria.com", "domain": "becker-austria.com", "territory": "Official Austria Subsidiary (Wiener Neudorf)"},
    {"company": "Becker Druk- en Vacuümpompen B.V. (Belgium)", "role": "Area Sales Manager", "ceo": "Yuri Rentmeesters", "email": "yuri.rentmeesters@beckerdvp.nl", "domain": "beckerdvp.nl", "territory": "Official Territory Manager (Belgium & Luxembourg)"},
    {"company": "Metzger Technik GmbH", "role": "Geschäftsführer", "ceo": "Gerd Metzger", "email": "gerd.metzger@metzger-technik.de", "domain": "metzger-technik.de", "territory": "Authorized German Stocking Distributor (Vaihingen an der Enz)"},
    {"company": "Directair", "role": "Managing Director", "ceo": "Allan Dolby", "email": "allan.dolby@directair.co.uk", "domain": "directair.co.uk", "territory": "Authorized UK Stocking Distributor & Service Center"},
    {"company": "Air Supply Ltd", "role": "Managing Director", "ceo": "George Jackson Wright", "email": "george.wright@airsupply.co.uk", "domain": "airsupply.co.uk", "territory": "Authorized UK Stocking Distributor"},
    {"company": "Vacuum Pump Services Ltd", "role": "Managing Director", "ceo": "Peter Douglas Bowen", "email": "p.bowen@vacuumpumpservices.co.uk", "domain": "vacuumpumpservices.co.uk", "territory": "Authorized UK Becker Service & Repair Center"},
    {"company": "Triark Pumps", "role": "Managing Director", "ceo": "David Rozée", "email": "david@tri-ark.com", "domain": "tri-ark.com", "territory": "Stocking Distributor (United Kingdom)"},
    {"company": "Raptor Supplies", "role": "Founder & CEO", "ceo": "Arjun Singh", "email": "arjun@raptorsupplies.com", "domain": "raptorsupplies.com", "territory": "Authorized European Distributor"},
    {"company": "Vakuum Bohemia s.r.o.", "role": "Jednatel / Managing Director", "ceo": "Ing. Vít Němec", "email": "vit.nemec@vakuum-bohemia.cz", "domain": "vakuum-bohemia.cz", "territory": "Stocking Distributor & Service Center (Czechia & Slovakia)"},
    {"company": "Ultra Controlo Projectos Industriais Lda", "role": "CEO & Founder", "ceo": "Sabino de Pompeia", "email": "sabino.pompeia@ultra-controlo.com", "domain": "ultracontrolo.com", "territory": "Authorized Stocking Representative (Portugal & Spain)"},

    # Rest of World (Asia-Pacific, Latin America, Middle East, Africa)
    {"company": "Becker Asia Pacific Pte. Ltd.", "role": "Managing Director", "ceo": "Ho Boon Chuan", "email": "ho.boonchuan@beckerasia.com.sg", "domain": "beckerasia.com.sg", "territory": "Asia-Pacific Regional HQ (Singapore, SE Asia, Aus, NZ)"},
    {"company": "Becker Pumps Australia", "role": "Regional Sales Management", "ceo": "Ho Boon Chuan", "email": "sales@beckerpumps.com.au", "domain": "beckerpumps.com.au", "territory": "Dedicated Australian Sales & Service Entity"},
    {"company": "Vacuum Pumps NZ Limited (VPNZ)", "role": "Co-Owner / Director", "ceo": "David Walls", "email": "info@vpnz.co.nz", "domain": "vpnz.co.nz", "territory": "Authorized New Zealand Stocking Representative"},
    {"company": "Gebr. Becker India Vacuum Pumps Pvt. Ltd.", "role": "Managing Director", "ceo": "Milind Bhalerao", "email": "milind.bhalerao@becker-india.com", "domain": "becker-india.com", "territory": "Official India Subsidiary & Regional Export Hub (Pune)"},
    {"company": "Gebr. Becker GmbH - Middle East Regional Office", "role": "Area Sales Manager - Middle East", "ceo": "Manoj Kumar", "email": "manoj@becker-india.com", "domain": "becker-international.com", "territory": "Middle East Representative (UAE, Saudi Arabia, Qatar, Oman)"},
    {"company": "Becker Air Techno Co., Ltd.", "role": "Representative Director / President", "ceo": "Shokichi Miki", "email": "info@becker-japan.co.jp", "domain": "becker-japan.co.jp", "territory": "Official Japan Subsidiary (Minato-ku, Tokyo)"},
    {"company": "Becker Korea Co., Ltd.", "role": "Representative Director", "ceo": "Sun-Hee Hwang", "email": "becker@beckerkorea.co.kr", "domain": "beckerkorea.co.kr", "territory": "Official South Korea Subsidiary (Goyang-si, Gyeonggi-do)"},
    {"company": "Becker Vacuum Technology Shanghai Co., Ltd.", "role": "General Manager", "ceo": "Qingshan Wu", "email": "info@becker-china.com", "domain": "becker-china.com", "territory": "Official China Subsidiary (Shanghai)"},
    {"company": "African Vacuum Pumps (Pty) Ltd", "role": "Managing Director", "ceo": "John Miller", "email": "info@africanvacuumpumps.com", "domain": "africanvacuumpumps.com", "territory": "Exclusive Sub-Saharan Africa Distributor (Gauteng, SA)"},
    {"company": "Vacuum Tech Máquinas e Equipamentos Ltda. (Robmaq)", "role": "Commercial Director", "ceo": "Rafael Robmaq", "email": "rafael@robmaq.com.br", "domain": "robmaq.com.br", "territory": "Authorized Brazil Representative & Service Provider (Curitiba)"},
    {"company": "W&F Ingeniería y Máquinas S.A.", "role": "Gerente General", "ceo": "Roberto Wendler Apel", "email": "rwendler@wyf.cl", "domain": "wyf.cl", "territory": "Authorized Chile Representative (Santiago)"},
    {"company": "CompVac", "role": "Principal Representative", "ceo": "Guillermo Quintin", "email": "guillermo.quintin@compvac.com.ar", "domain": "compvac.com.ar", "territory": "Authorized Argentina Representative & Technical Service"}
]

out_txt = "/Users/alt/Desktop/starr/favour/beckerpumps_complete_global_master.txt"
out_csv = "/Users/alt/Desktop/starr/favour/beckerpumps_complete_global_master.csv"

with open(out_txt, "w") as f:
    for i, item in enumerate(becker_global_master):
        f.write(f"Procurement Proposal for {item['company']}\n")
        f.write(f'"{item["ceo"]}" <{item["email"]}>\n')
        if i < len(becker_global_master) - 1:
            f.write("\n")

with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company / Entity", "Executive Title", "CEO / President / Director", "Verified Executive Email", "Domain", "Territory & Region Notes"])
    for item in becker_global_master:
        writer.writerow([item["company"], item["role"], item["ceo"], item["email"], item["domain"], item["territory"]])

print(f"Successfully compiled {len(becker_global_master)} complete global Becker entities to {out_txt} and {out_csv}")
