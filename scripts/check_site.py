#!/usr/bin/env python3
"""Small, dependency-free integrity checks for the BuyCTA static offering."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.anchors = []
        self.h1_count = 0
        self.forms = []
        self.script_sources = []
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.anchors.append(a["href"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "form":
            self.forms.append(a)
        if tag == "script" and a.get("src"):
            self.script_sources.append(a["src"])
        if tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href"))


page = Page()
page.feed(HTML)
assert page.h1_count == 1, "Exactly one main heading is expected"
assert len(page.ids) == len(set(page.ids)), "Duplicate IDs"
assert all(h[1:] in page.ids for h in page.anchors if h.startswith("#")), "Broken in-page anchor"
assert page.canonicals == ["https://buycta.com/"], "Unexpected canonical"
assert len(page.forms) == 1 and page.forms[0].get("id") == "inquiry-form"
assert not page.forms[0].get("action"), "Do not imply a backend submission"
assert not page.script_sources, "No third-party scripts should load"
assert "agent@sohadot.com" in HTML, "Acquisition contact missing"
assert "mail application" in HTML, "Mailto behavior must be disclosed"
assert "No operating business included" in HTML, "Domain-only disclosure missing"
assert "Price</span><strong>Upon inquiry" in HTML, "Public price policy changed"
assert all(urlparse(h).scheme in {"", "https", "mailto"} for h in page.anchors)
robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
assert "Sitemap: https://buycta.com/sitemap.xml" in robots
root = ET.parse(ROOT / "sitemap.xml").getroot()
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
assert [e.text for e in root.findall("s:url/s:loc", ns)] == ["https://buycta.com/"]
print("PASS: structure, inquiry semantics, public price, canonical, links, sitemap")
