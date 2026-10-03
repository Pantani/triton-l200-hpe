"""Validate discoverability and agreement between public offer representations."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

from PIL import Image


SITE = Path(__file__).resolve().parents[1] / "site"
CANONICAL = "https://pantani.xyz/triton-l200-hpe/"


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.elements = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def select(self, name):
        return [attrs for tag, attrs in self.elements if tag == name]


class SEOTests(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "index.html").read_text(encoding="utf-8")
        self.elements = Elements(self.html)

    def product(self):
        blocks = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>',
            self.html,
            re.DOTALL,
        )
        self.assertEqual(len(blocks), 1)
        return json.loads(blocks[0])

    def test_sitemap_and_canonical_agree(self):
        canonical = [a["href"] for a in self.elements.select("link")
                     if a.get("rel") == "canonical"]
        self.assertEqual(canonical, [CANONICAL])
        social_urls = [a["content"] for a in self.elements.select("meta")
                       if a.get("property") == "og:url"]
        self.assertEqual(social_urls, canonical)
        self.assertNotIn("pantani.github.io", self.html)
        tree = ET.parse(SITE / "sitemap.xml")
        urls = tree.findall("{*}url/{*}loc")
        self.assertEqual([node.text for node in urls], canonical)

    def test_product_offer_agrees_with_visible_price(self):
        product = self.product()
        self.assertEqual(set(product["@type"]), {"Product", "Car"})
        self.assertEqual(product["url"], CANONICAL)
        offer = product["offers"]
        self.assertEqual(offer["url"], CANONICAL)
        self.assertEqual(offer["priceCurrency"], "BRL")
        self.assertEqual(offer["itemCondition"], "https://schema.org/UsedCondition")
        visible = re.sub(r"<script.*?</script>", "", self.html, flags=re.DOTALL)
        price = f'R$ {offer["price"]:,.0f}'.replace(",", ".")
        self.assertIn(price, visible)

    def test_schema_location_and_identity_are_truthful(self):
        product = self.product()
        place = product["offers"]["availableAtOrFrom"]
        self.assertEqual(place["@type"], "Place")
        self.assertEqual(place["address"]["@type"], "PostalAddress")
        self.assertEqual(place["address"]["addressLocality"], "São Paulo")
        forbidden = {"review", "aggregateRating", "vehicleIdentificationNumber",
                     "streetAddress", "shippingDetails", "hasMerchantReturnPolicy"}
        keys = set(re.findall(r'"([^"]+)"\s*:', json.dumps(product)))
        self.assertFalse(keys & forbidden)

    def test_schema_images_reference_public_files(self):
        for url in self.product()["image"]:
            with self.subTest(url=url):
                self.assertTrue(url.startswith(CANONICAL + "assets/"))
                local = SITE / url.removeprefix(CANONICAL)
                self.assertTrue(local.is_file())

    def test_page_does_not_block_indexing(self):
        directives = " ".join(a.get("content", "") for a in self.elements.select("meta")
                              if a.get("name", "").lower() in {"robots", "googlebot"})
        self.assertNotRegex(directives.lower(), r"\b(noindex|none)\b")
        self.assertEqual(self.elements.select("html")[0]["lang"], "pt-BR")

    def test_responsive_images_have_real_width_descriptors(self):
        sources = self.elements.select("source")
        self.assertEqual(len(sources), len(self.elements.select("img")) + 1)
        self.assertEqual(sources[0].get("media"),
                         "(max-width: 480px) and (orientation: portrait)")
        for source in sources:
            with self.subTest(srcset=source["srcset"]):
                self.assertEqual(source["type"], "image/webp")
                self.assertTrue(source["sizes"])
                self.check_widths(source["srcset"])

    def check_widths(self, srcset):
        candidates = [entry.strip().split() for entry in srcset.split(",")]
        self.assertGreaterEqual(len(candidates), 1)
        for path, width in candidates:
            with Image.open(SITE / urlparse(path).path) as photo:
                self.assertEqual(width, f"{photo.width}w")

    def test_font_dependencies_are_local_valid_woff2(self):
        links = self.elements.select("link")
        remote_hosts = {"fonts.googleapis.com", "fonts.gstatic.com"}
        self.assertFalse([link for link in links
                          if urlparse(link["href"]).netloc in remote_hosts])
        css = (SITE / "fonts.css").read_text(encoding="utf-8")
        urls = re.findall(r"url\('([^']+)'\)", css)
        self.assertTrue(urls)
        for url in urls:
            with self.subTest(url=url):
                self.assertFalse(urlparse(url).netloc)
                self.assertEqual((SITE / url).read_bytes()[:4], b"wOF2")

    def test_self_hosted_font_families_include_licenses(self):
        css = (SITE / "fonts.css").read_text(encoding="utf-8")
        families = set(re.findall(r"font-family: '([^']+)'", css))
        self.assertTrue(families)
        for family in families:
            slug = family.lower().replace(" ", "-")
            license_path = SITE / "assets" / "fonts" / f"{slug}-OFL.txt"
            self.assertIn("SIL OPEN FONT LICENSE", license_path.read_text())


if __name__ == "__main__":
    unittest.main()
