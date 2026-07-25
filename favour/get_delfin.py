import urllib.request
import re

url = "https://www.delfinvacuums.com/en/company/branches"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    print("Found branches!")
    # Look for branch names
    branches = re.findall(r'<h3.*?>(.*?)</h3>', html)
    print(branches)
except Exception as e:
    print(e)
