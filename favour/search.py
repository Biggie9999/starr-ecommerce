import urllib.request
import urllib.parse
import re
import sys
from html.parser import HTMLParser

class DDGParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []
        self.in_result = False
        self.current_result = {"title": "", "snippet": ""}
        self.capture_field = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "class" in attrs and "result-title" in attrs["class"]:
            self.in_result = True
            self.capture_field = "title"
        elif tag == "div" and "class" in attrs and "result-snippet" in attrs["class"]:
            self.capture_field = "snippet"

    def handle_data(self, data):
        if self.capture_field == "title":
            self.current_result["title"] += data
        elif self.capture_field == "snippet":
            self.current_result["snippet"] += data

    def handle_endtag(self, tag):
        if tag == "a" and self.capture_field == "title":
            self.capture_field = None
        elif tag == "div" and self.capture_field == "snippet":
            self.capture_field = None
            self.results.append(self.current_result)
            self.current_result = {"title": "", "snippet": ""}

def search_ddg(query):
    url = "https://lite.duckduckgo.com/lite/"
    data = urllib.parse.urlencode({'q': query}).encode('utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            parser = DDGParser()
            parser.feed(html)
            for res in parser.results:
                print(res["title"].strip())
                print(res["snippet"].strip())
                print("-" * 40)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    search_ddg(sys.argv[1])
