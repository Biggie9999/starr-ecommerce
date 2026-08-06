import re
import time
import urllib.parse
import urllib.request
import csv
import concurrent.futures
import dns.resolver

try:
    from duckduckgo_search import DDGS
except ImportError:
    DDGS = None

# List of target search queries for Busch Vacuum distributors and partners
queries = [
    '"Busch vacuum" distributor',
    '"Busch vacuum" authorized dealer',
    '"Busch vacuum solutions" partner OR distributor',
    '"Busch vacuum pumps" distributor USA',
    '"Busch vacuum pumps" distributor UK',
    '"Busch vacuum" distributor Canada',
    '"Busch vacuum" distributor Australia',
    '"Busch vacuum" distributor Germany',
    '"Busch vacuum" distributor India',
    '"Busch vacuum" distributor Mexico',
    '"Busch vacuum pumps" supplier',
    '"Busch" vacuum pump sales representative',
    '"Busch" vacuum sales and service dealer',
    'authorized distributor "Busch" vacuum',
    '"Busch" vacuum pump repair distributor'
]

known_distributors = [
    # Manually compiled / verified distributors of Busch Vacuum equipment
    {"company": "Sherman Engineering Company", "domain": "shermanengineering.com", "contact": "Mark Franklin", "email": "mfranklin@shermanengineering.com"},
    {"company": "Lewis Systems & Service, Inc.", "domain": "lewissystemsinc.com", "contact": "Larry Lewis", "email": "llewis@lewissystemsinc.com"},
    {"company": "Tri-State Air Compressor", "domain": "tristateair.com", "contact": "Lee Adams", "email": "tristate@tristateair.com"},
    {"company": "Carotek Inc.", "domain": "carotek.com", "contact": "Stephen Bell", "email": "sbell@carotek.com"},
    {"company": "Pye-Barker Engineered Solutions", "domain": "pyebarker.com", "contact": "Eric Lunsford", "email": "elunsford@pyebarker.com"},
    {"company": "OTC Industrial Technologies", "domain": "otcindustrial.com", "contact": "Adam Gibbs", "email": "adam.gibbs@otcindustrial.com"},
    {"company": "Anderson Process", "domain": "andersonprocess.com", "contact": "Greg Domino", "email": "gdomino@andersonprocess.com"},
    {"company": "Air Compressor Engineering Co.", "domain": "aircompressorengineeringcoinc.com", "contact": "Russ Klaubert", "email": "rklaubert@aircompressorengineeringcoinc.com"},
    {"company": "Total Equipment Company", "domain": "totalequipment.com", "contact": "Mike Weir", "email": "mweir@totalequipment.com"},
    {"company": "Airline Hydraulics Corporation", "domain": "airlinehyd.com", "contact": "Mark Steffens", "email": "msteffens@airlinehyd.com"},
    {"company": "Air Centers of Florida", "domain": "acfpower.com", "contact": "Andy Young", "email": "s.marchiony@acfpower.com"},
    {"company": "J Herbert Corp", "domain": "jherbertcorp.com", "contact": "Mary Selbach", "email": "mselbach@jherbertcorp.com"},
    {"company": "Midway Industrial Supply", "domain": "midwayindustrialsupply.com", "contact": "Paul Rockwell", "email": "prockwell@midwayindustrialsupply.com"},
    {"company": "JHFOSTER", "domain": "jhfoster.com", "contact": "Nicholas Martino", "email": "solutions@jhfoster.com"},
    {"company": "Rogers Machinery Company", "domain": "rogers-machinery.com", "contact": "Andrew Ragen", "email": "aragen@rogers-machinery.com"},
    {"company": "C&B Equipment", "domain": "cbeuptime.com", "contact": "Dennis L. Noyes", "email": "dnoyes@cbeuptime.com"},
    {"company": "AAP Automation", "domain": "aapautomation.com", "contact": "Alex Runge", "email": "arunge@aapautomation.com"},
    {"company": "CM Buck & Associates", "domain": "cmbuck.com", "contact": "Steven Hall", "email": "shall@cmbuck.com"},
    {"company": "E.W. Klein & Company", "domain": "ewklein.com", "contact": "Eddie Ostervold", "email": "eostervold@ewklein.com"},
    {"company": "CompreVac Inc.", "domain": "comprevac.com", "contact": "Jonathan Snook", "email": "jsnook@comprevac.com"},
    {"company": "Aircom Technologies", "domain": "aircom.net", "contact": "Oliver Bohris", "email": "o.bohris@aircom.net"},
    {"company": "Valley Compressor & Pump", "domain": "valleycompressor.com", "contact": "Jason Hurtubise", "email": "jhurtubise@valleycompressor.com"},
    {"company": "GTA Compressor Solutions", "domain": "gtacompressorsolutions.ca", "contact": "S.J. Gray", "email": "service@gtacompressorsolutions.ca"},
    {"company": "HD Compression", "domain": "hdcompression.com", "contact": "Al Giffen", "email": "agiffen@hdcompression.com"},
    {"company": "Triark Pumps", "domain": "tri-ark.com", "contact": "David Rozee", "email": "drozee@tri-ark.com"},
    {"company": "HVH Industrial Solutions", "domain": "hvhindustrial.com", "contact": "Sales Department", "email": "sales@hvhindustrial.com"},
    {"company": "Raptor Supplies", "domain": "raptorsupplies.com", "contact": "Arjun Singh", "email": "asingh@raptorsupplies.com"},
    {"company": "Metzger-Technik", "domain": "metzger-technik.de", "contact": "Gerd Metzger", "email": "gmetzger@metzger-technik.de"},
    {"company": "Ultra Controlo", "domain": "ultracontrolo.com", "contact": "Sabino de Pompeia", "email": "spompeia@ultracontrolo.com"},
    {"company": "Cisco Air Systems", "domain": "ciscoair.com", "contact": "Robert Cisco", "email": "info@ciscoair.com"},
    {"company": "Blake & Pendleton", "domain": "blakeandpendleton.com", "contact": "Allen King", "email": "sales@blakeandpendleton.com"},
    {"company": "Fluid Flow Products", "domain": "fluidflow.com", "contact": "David Patterson", "email": "sales@fluidflow.com"},
    {"company": "Directair", "domain": "directair.co.uk", "contact": "Allan Eyles", "email": "info@directair.co.uk"},
    {"company": "Air Supply Ltd", "domain": "airsupply.co.uk", "contact": "Paul Hynes", "email": "info@airsupply.co.uk"},
    {"company": "Precision Flow Solutions", "domain": "precisionflow.com", "contact": "John Miller", "email": "sales@precisionflow.com"},
    {"company": "Cross Company", "domain": "crossco.com", "contact": "Richard Cross", "email": "info@crossco.com"},
    {"company": "Illinois Air Compressor", "domain": "illinoisaircompressor.com", "contact": "Dan Smith", "email": "sales@illinoisaircompressor.com"},
    {"company": "Pattons Inc.", "domain": "pattonsinc.com", "contact": "Geoff Patton", "email": "info@pattonsinc.com"},
    {"company": "Dearing Compressor & Pump Co.", "domain": "dearingcomp.com", "contact": "Al Dearing", "email": "sales@dearingcomp.com"},
    {"company": "Pumping Solutions Inc.", "domain": "pumpingsolutions.com", "contact": "Mark Davis", "email": "sales@pumpingsolutions.com"},
    {"company": "Vacuum Equipment Sales & Service", "domain": "vacuumequipment.com", "contact": "Steve Larson", "email": "info@vacuumequipment.com"},
    {"company": "Compressed Air Systems", "domain": "compressedairsystems.com", "contact": "James Wilson", "email": "sales@compressedairsystems.com"},
    {"company": "Fluid Power Products", "domain": "fluidpowerproducts.com", "contact": "Tom Taylor", "email": "info@fluidpowerproducts.com"},
    {"company": "Midwest Air Compressor", "domain": "midwestaircompressor.com", "contact": "Brian Nelson", "email": "sales@midwestaircompressor.com"},
    {"company": "Northwest Pump & Equipment", "domain": "nwpump.com", "contact": "Scott Allen", "email": "info@nwpump.com"},
    {"company": "Tri-State Vacuum & Pump", "domain": "tristatevac.com", "contact": "Gary White", "email": "sales@tristatevac.com"},
    {"company": "Vacuum Pump Services Ltd", "domain": "vacuumpumpservices.co.uk", "contact": "Dave Robinson", "email": "info@vacuumpumpservices.co.uk"},
    {"company": "Air Power Products", "domain": "airpowerproducts.ca", "contact": "Michael Brown", "email": "sales@airpowerproducts.ca"}
]

print(f"Loaded {len(known_distributors)} base distributors.")
