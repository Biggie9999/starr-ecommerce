import urllib.request
import urllib.parse
import re
import json
import dns.resolver
import time

queries = [
    '"Anest Iwata" distributor "Inc"',
    '"Anest Iwata" distributor "LLC"',
    '"Anest Iwata" distributor "Co"',
    '"Anest Iwata" dealer Texas OR California OR Florida',
    '"Anest Iwata" dealer Ohio OR Pennsylvania OR Illinois',
    '"Anest Iwata" dealer Michigan OR North Carolina OR Georgia',
    '"Anest Iwata" dealer Washington OR Oregon OR Colorado',
    '"Anest Iwata" dealer Wisconsin OR Minnesota OR Indiana',
    '"Anest Iwata" line card distributor',
    '"Anest Iwata" authorized sales service',
    '"Anest Iwata spray gun" distributor',
    '"Anest Iwata vacuum pump" distributor',
    '"Anest Iwata compressor" distributor',
    '"Anest Iwata" distributor Ontario OR Quebec OR Alberta',
    '"Anest Iwata" distributor UK OR England OR Scotland',
    '"Anest Iwata" distributor Germany OR Austria OR Switzerland',
    '"Anest Iwata" distributor France OR Italy OR Spain',
    '"Anest Iwata" distributor Netherlands OR Belgium OR Nordics',
    '"Anest Iwata" distributor Australia OR New Zealand',
    '"Anest Iwata" distributor India OR Singapore OR Malaysia',
    '"Anest Iwata" distributor Japan OR Korea OR China',
    '"Anest Iwata" distributor Mexico OR Brazil OR Chile'
]

known_domains = {
    'anestiwataamericas.com', 'anestiwata-corp.com', 'iwata-medea.com', 'anest-iwata.com.mx',
    'airzap.com.br', 'arteyaerografia.com', 'altecfluidos.com', 'deltatiger.com.mx',
    'doutorpistola.com.br', 'enko-online.com', 'visospinturas.com', 'monumentaldelplata.com.ar',
    'andycolors.com', 'sprayfishinc.com', 'globalvacuumllc.com', 'innovacllc.com',
    'tlfinish.com', 'spokane-hardware.com', 'anest-iwata-st.com', 'anest-iwata-air.com',
    'harder-airbrush.de', 'anest-iwata-fr.com', 'anest-iwata-uk.com', 'spraygunsdirect.co.uk',
    'anest-iwata.es', 'anest-iwata.se', 'lakgruppen.com', 'billakk.no', 'pintavari.fi',
    'anest-iwata-pl.com', 'wiltec.nl', 'spraytechnik.ch', 'gamin.cz', 'airpower-usa.com',
    'otcindustrial.com', 'ptbsales.com', 'spokanehardware.com', 'advancedcoatingstech.ca',
    'mcsupply.org', 'compressorworld.com', 'associatedcompressor.com', 'qair.net',
    'rogers-machinery.com', 'chreed.com', 'elevatedindustrial.com', 'cascousa.com',
    'acfpower.com', 'fluidairedynamics.com', 'kgpowersystems.com', 'mapleairbrushsupplies.com',
    'coastairbrush.com', 'hodgeindustrial.com', 'selectumllc.com'
}

bad_keywords = [
    'google', 'duckduckgo', 'amazon', 'ebay', 'wikipedia', 'linkedin', 'facebook',
    'youtube', 'twitter', 'instagram', 'yelp', 'yellowpages', 'mapquest', 'thomasnet',
    'directindustry', 'radwell', 'scribd', 'dnb', 'zoominfo', 'bloomberg'
]

def search_ddg(q):
    url = "https://html.duckduckgo.com/html/"
    data = urllib.parse.urlencode({'q': q}).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=8)
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a class="result__url" href="([^"]+)">\s*([^<]+)\s*</a>', html)
        out = []
        for u, t in matches:
            out.append((u.strip(), t.strip()))
        return out
    except Exception:
        return []

def check_mx(domain):
    try:
        res = dns.resolver.Resolver()
        res.nameservers = ['8.8.8.8', '1.1.1.1']
        res.timeout = 3
        res.lifetime = 4
        records = res.resolve(domain, 'MX')
        return len(records) > 0
    except Exception:
        return False

discovered_new = {}
print("Executing deep search for NEW Anest Iwata distributors...")

for q in queries:
    res = search_ddg(q)
    for u, t in res:
        m = re.search(r'https?://(?:www\.)?([^/]+)', u)
        if m:
            dom = m.group(1).lower()
            if dom not in known_domains and not any(bk in dom for bk in bad_keywords):
                clean_t = re.sub(r'<[^>]+>', '', t)
                clean_t = re.sub(r'\s+', ' ', clean_t).strip()
                if dom not in discovered_new:
                    discovered_new[dom] = clean_t
    time.sleep(0.5)

print(f"Discovered {len(discovered_new)} candidate NEW Anest Iwata domains.")

valid_new = {}
for dom, title in discovered_new.items():
    if check_mx(dom):
        valid_new[dom] = title

print(f"Validated {len(valid_new)} NEW Anest Iwata domains with active MX records.")

with open('/Users/alt/Desktop/starr/favour/anest_iwata_new_harvest.json', 'w') as f:
    json.dump(valid_new, f, indent=2)

print("Saved new harvest to anest_iwata_new_harvest.json")
