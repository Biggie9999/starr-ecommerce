import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_partner_link = False
        self.in_h3 = False
        self.current_name = ""
        self.partners = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            href = attrs.get("href", "")
            if href.startswith("/partners/"):
                self.in_partner_link = True
        elif tag == "h3" and self.in_partner_link:
            self.in_h3 = True
            self.current_name = ""

    def handle_endtag(self, tag):
        if tag == "a" and self.in_partner_link:
            self.in_partner_link = False
        elif tag == "h3" and self.in_h3:
            self.in_h3 = False
            if self.current_name.strip():
                self.partners.append(self.current_name.strip())

    def handle_data(self, data):
        if self.in_h3:
            self.current_name += data

req = urllib.request.Request("https://www.coval.com/partners", headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(html)
partners = sorted(list(set(parser.partners)))
print(f"Found {len(partners)} partners:")
for p in partners:
    print(p)

