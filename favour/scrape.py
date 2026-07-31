import urllib.request
import re

urls = [
    "http://ecia.pt",
    "http://emerson-technik.eu",
    "http://multivac.se",
    "http://boonsfis.com",
    "http://lsengineering.co.uk",
    "http://ftiinc.org"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        emails = set(re.findall(r"[a-zA-Z0-9.\-+_]+@[a-zA-Z0-9.\-+_]+\.[a-zA-Z]+", html))
        print(f"{url} emails: {emails}")
    except Exception as e:
        print(f"{url} failed: {e}")
