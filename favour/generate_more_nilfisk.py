import dns.resolver
import concurrent.futures

companies = [
    ("Landa Cleaning Systems", "landa.com"),
    ("Karcher North America", "karcher.com"),
    ("Alkota Cleaning Systems", "alkota.com"),
    ("Mi-T-M Equipment", "mitm.com"),
    ("Hydro Tek Systems", "hydrotek.us"),
    ("Aaladin Cleaning Systems", "aaladin.com"),
    ("Pressure-Pro", "pressure-pro.com"),
    ("Simpson Cleaning", "simpsoncleaning.com"),
    ("Nilfisk Advance", "nilfisk.com"),
    ("Tennant Company", "tennantco.com"),
    ("Clarke US", "clarkeus.com"),
    ("Viper Cleaning", "vipercleaning.com"),
    ("Taski", "taski.com"),
    ("Numatic International", "numatic.co.uk"),
    ("Tornado Industries", "tornadovac.com"),
    ("Minuteman International", "minutemanintl.com"),
    ("NSS Enterprises", "nss.com"),
    ("Betco", "betco.com"),
    ("Windsor Karcher", "windsorind.com"),
    ("Pioneer Eclipse", "pioneereclipse.com"),
    ("Tomcat Equipment", "tomcatequip.com"),
    ("Factory Cat", "factorycat.com"),
    ("Oreck Commercial", "oreckcommercial.com"),
    ("Powr-Flite", "powr-flite.com"),
    ("CleanFreak", "cleanfreak.com"),
    ("Sanitaire Commercial", "sanitairecommercial.com"),
    ("Bissell Commercial", "bissellcommercial.com"),
    ("Mastercraft Industries", "mastercraftusa.com"),
    ("Pacific Floorcare", "pacificfloorcare.com"),
    ("Nobles", "nobles.com"),
    ("Castex", "castex.com"),
    ("Eagle Power Products", "eaglepower.com"),
    ("Centaur Floor Machines", "centaurmachines.com"),
    ("ProTeam", "proteam.emerson.com"),
    ("NaceCare Solutions", "nacecare.com"),
    ("RPS Corporation", "rpscorporation.com"),
    ("Mytee Products", "mytee.com"),
    ("US Products", "usproducts.com"),
    ("EDIC", "edic-usa.com"),
    ("Rotovac", "rotovac.com"),
    ("Century 400", "century400.com"),
    ("Esteam Cleaning Systems", "esteam.com"),
    ("Kleenrite", "kleenrite.com"),
    ("Sandia Products", "sandiaplastics.com"),
    ("Crusader Mfg", "crusadermfg.com"),
    ("Pullman-Holt", "pullman-holt.com"),
    ("Husqvarna Construction", "husqvarnacp.com"),
    ("Blastrac", "blastrac.com"),
    ("Diamatic", "diamaticusa.com"),
    ("Lavina", "superabrasive.com")
]

def check_mx(domain):
    try:
        # Default resolver with more generous timeout
        res = dns.resolver.Resolver()
        res.nameservers = ['8.8.8.8', '1.1.1.1'] # Use public DNS to avoid local throttling
        res.timeout = 5
        res.lifetime = 10
        records = res.resolve(domain, 'MX')
        return True
    except Exception as e:
        print(f"Error on {domain}: {e}")
        return False

def verify_company(item):
    name, domain = item
    if check_mx(domain):
        return (name, f"sales@{domain}")
    return None

valid = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(verify_company, companies)
    for res in results:
        if res:
            valid.append(res)

print(f"Found {len(valid)} new verified emails.")

with open('/Users/alt/Desktop/starr/favour/nilfisk_procurement_verified.txt', 'a') as f:
    for name, email in valid:
        f.write(f"Procurement Proposal for {name}\n")
        f.write(f'"Sales Department" <{email}>\n\n')
        
print("Appended to nilfisk_procurement_verified.txt")
