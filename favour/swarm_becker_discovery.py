import urllib.request
import urllib.parse
import re
import json
import dns.resolver
import time

queries = [
    '"Becker vacuum" distributor "Inc"',
    '"Becker vacuum" distributor "LLC"',
    '"Becker vacuum" distributor "Co"',
    '"Becker vacuum" dealer Texas OR California OR Florida',
    '"Becker vacuum" dealer Ohio OR Pennsylvania OR Illinois',
    '"Becker vacuum" dealer Michigan OR North Carolina OR Georgia',
    '"Becker vacuum" dealer Washington OR Oregon OR Colorado',
    '"Becker vacuum" dealer Wisconsin OR Minnesota OR Indiana',
    '"Becker pump" line card distributor',
    '"Becker vacuum pumps" authorized sales service',
    '"Becker dry rotary vane" distributor',
    '"Becker oil-lubricated vacuum" distributor',
    '"Becker regenerative blower" distributor',
    '"Becker combined pressure" vacuum pump distributor',
    '"Becker" vacuum pump line card',
    '"Becker vacuum" distributor Ontario OR Quebec OR Alberta',
    '"Becker vacuum" distributor UK OR England OR Scotland',
    '"Becker vacuum" distributor Germany OR Austria OR Switzerland',
    '"Becker vacuum" distributor France OR Italy OR Spain',
    '"Becker vacuum" distributor Netherlands OR Belgium OR Nordics',
    '"Becker vacuum" distributor Australia OR New Zealand',
    '"Becker vacuum" distributor India OR Singapore OR Malaysia',
    '"Becker vacuum" distributor Japan OR Korea OR China',
    '"Becker vacuum" distributor Mexico OR Brazil OR Chile',
    '"Becker vacuum" distributor UAE OR Saudi Arabia OR South Africa'
]

known_domains = {
    'remequip.com', 'hvhindustrial.com', 'centennialequipment.com', 'cncpd.com',
    'sfvtechnologies.com', 'applicationassociates.com', 'pioneerequip.com',
    'statesideindustrial.com', 'powermatic.net', 'ynna.cz', 'metzger-technik.de',
    'directair.co.uk', 'airsupply.co.uk', 'vacuumpumpservices.co.uk', 'tri-ark.com',
    'raptorsupplies.com', 'ultracontrolo.com', 'vpnz.co.nz', 'africanvacuumpumps.com',
    'fluidtec.ae', 'mechatronics.ae', 'robmaq.com.br', 'wyf.cl', 'compvac.com.ar',
    'beckerpumps.com', 'becker-international.com', 'becker-canada.com', 'becker-mexico.mx',
    'becker.co.uk', 'becker-france.fr', 'becker.it', 'becker-iberica.com', 'beckerdvp.nl',
    'becker.ch', 'beckervakuum.se', 'becker-polska.com', 'becker-austria.com',
    'beckerpumps.com.au', 'becker-india.com', 'beckerasia.com.sg', 'becker-japan.co.jp',
    'beckerkorea.co.kr', 'becker-china.com', 'rogers-machinery.com', 'shermanengineering.com',
    'lewissystemsinc.com', 'carotek.com', 'pyebarker.com', 'otcindustrial.com',
    'andersonprocess.com', 'aircompressoreng.com', 'totalequipment.com', 'airlinehyd.com',
    'acfpower.com', 'jherbertcorp.com', 'midwayindustrialsupply.com', 'jhfoster.com',
    'cbeuptime.com', 'aapautomation.com', 'cmbuck.com', 'ewklein.com', 'comprevac.com',
    'aircom.net', 'valleycompressor.com', 'gtacompressorsolutions.ca', 'hdcompression.com',
    'airpowerproducts.ca', 'ciscoair.com', 'blakeandpendleton.com', 'fluidflow.com',
    'pattonsinc.com', 'dearingcomp.com', 'nwpump.com', 'tristatevac.com'
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
print("Executing deep search for NEW, previously unlisted Becker distributors...")

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

print(f"Discovered {len(discovered_new)} candidate NEW domains.")

valid_new = {}
for dom, title in discovered_new.items():
    if check_mx(dom):
        valid_new[dom] = title

print(f"Validated {len(valid_new)} NEW domains with active MX records.")

with open('/Users/alt/Desktop/starr/favour/becker_new_harvest.json', 'w') as f:
    json.dump(valid_new, f, indent=2)

print("Saved new harvest to becker_new_harvest.json")
